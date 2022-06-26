#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of a folder.
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder on an
    AirBnB Clone repo.
    """
    dt = datetime
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )

    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
        if local("tar -czvf {} web_static".format(file_name)).failed is True:
            return None
    return file_name
