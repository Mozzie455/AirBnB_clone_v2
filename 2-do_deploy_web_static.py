#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
    contents of the web_static folder
"""


from fabric.api import *
from datetime import datetime
import os

env.hosts = ['44.210.150.72']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ fabric script to deploy to a server """
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")
    filename = filename[1]
    fname = filename.split('.')
    fname = fname[0]

    newpath = '/data/web_static/releases/{}/'.format(fname)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(newpath))
        run("tar -xzf /tmp/{} -C {}".format(filename, newpath))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(newpath, newpath))
        run("rm -rf {}web_static".format(newpath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newpath))
        return True
    except:
        return False
