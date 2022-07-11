#!/usr/bin/python3
"""Defines the function do_pack."""
import datetime
from os.path import isdir
from os.path import exists
from fabric.api import env
from fabric.api import run
from fabric.api import put
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder on
    an AirBnB Clone repo.
    """
    if isdir("./versions") is False:
        res = local("mkdir /versions", capture=True)
        if res.failed:
            return None

    time = datetime.datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year, time.month, time.day, time.hour, time.minute, time.second
    )

    res = local("tar -czvf {} web_static".format(file_name), capture=True)
    if res.failed:
        return None
    return file_name


env.host = ["3.228.25.64", "3.238.123.138"]
env.user = "ubuntu"


def result(*operations):
    """Returns True if all operations have been done correctly,
    otherwise returns False.
    """
    for operation in operations:
        if operation.failed == True:
            return False
    return True


def do_deploy(archive_path):
    """Distributes an archive to web severs.

    Argument:
        archive_path (str): Path to the archive.
    """
    if exists(archive_path) is False:
        return False

    put(archive_path, "/tmp/")

    archive_file = archive_path[archive_path.index("/") + 1 :]
    folder_name = archive_file.replace(".tgz", "")
    folder_name = "/data/web_static/releases/" + folder_name

    op1 = run("mkdir -p {}".format(folder_name)).failed
    op2 = run("tar -xzf /tmp/{} -C {}".format(archive_file, folder_name))
    op3 = run("rm /tmp/{}".format(archive_file))
    op4 = run("mv {}/web_static/* {}".format(folder_name, folder_name))
    op5 = run("rm -rf {}/web_static".format(folder_name))
    op6 = run("rm -rf /data/web_static/current")
    op7 = run("ln -s {} /data/web_static/current".format(folder_name))

    return result(op1, op2, op3, op4, op5, op6, op7)


def deploy():
    """Creates and distributes an archive to web severs."""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return None
