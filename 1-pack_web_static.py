#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
    contents of the web_static folder
"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    ret = local("tar -czvf {} web_static".format(path))
    if ret.failed:
        return None
    return path
