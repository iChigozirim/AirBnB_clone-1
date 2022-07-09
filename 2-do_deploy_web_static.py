#!/usr/bin/python3
"""Fabric script that distributes an archive to specified web servers."""
from os.path import exists
from fabric.api import env
from fabric.api import run
from fabric.api import put


env.host = ['server_ip_address']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Distributes an archive to web severs.
    
    Argument:
        archive_path (str): Path to the archive.
    """
    if exists(archive_path) is False:
        return False
    
    def result(*operations):
        """Returns True if all operations have been done correctly,
        otherwise returns False.
        """
        for operation in operations:
            if operation.failed == True:
                return False
        return True

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Uncompress the archive to the folder 
    # /data/web_static/releases/<archive filename without extension>
    # on the web server.
    archive_file = archive_path[archive_path.index('/') + 1:]
    folder_name = archive_file.replace('.tgz', '')
    folder_name = "/data/web_static/releases/" + folder_name

    op1 = run("mkdir -p {}".format(folder_name)).failed
    op2 = run("tar -xzf /tmp/{} -C {}".format(archive_file, folder_name))

    # Delete the archive from the web server
    op3 = run("rm /tmp/{}".format(archive_file))
    op4 = run("mv {}/web_static/* {}".format(folder_name, folder_name))
    op5 = run("rm -rf {}/web_static".format(folder_name))

    # Delete the symbolic link /data/web_static/current from the web server
    op6 = run('rm -rf /data/web_static/current')

    # Create a new the symbolic link /data/web_static/current on the web
    # server, linked to the new version of your code
    # (/data/web_static/releases/<archive filename without extension>)
    op7 = run("ln -s {} /data/web_static/current".format(folder_name))

    return result(op1, op2, op3, op4, op5, op6, op7)
