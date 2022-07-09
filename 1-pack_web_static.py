#!/usr/bin/python3
"""Defines the function do_pack."""
import datetime
from os.path import isdir
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
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )

    res = local("tar -czvf {} web_static".format(file_name), capture=True)
    if res.failed:
        return None
    return file_name

