#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of a folder.
"""
from fabric.api import *


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder on an
    AirBnB Clone repo.
    """
    name = ""
    run("tar -cv archive.tgz /web_static/*.")

