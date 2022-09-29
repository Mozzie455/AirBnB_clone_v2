#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
    contents of the web_static folder
"""


from datetime import datetime
from fabric.api import run, env, hosts, put


env.hosts = ['34.229.63.14', '100.27.49.144']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not archive_path:
        return False

    env.user = 'ubuntu'
    env.disable_known_hosts = True
    env.key_filename = "~/.ssh/id_rsa"

    file_ext = archive_path.split("/")[-1]
    file_name = file_ext.split(".")[0]
    sym_link = "/data/web_static/current"

    put(archive_path, "/tmp/")

    run("mkdir -p /data/web_static/releases/{}".format(file_name))

    ret = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
              file_name, file_name))
    if ret.failed:
        return False
    ret = run("rm -fr {}".format(archive_path))
    if ret.failed:
        return False
    ret = run("rm -f /data/web_static/current")
    if ret.failed:
        return False
    ret = run("ln -s /data/web_static/releases/{}/web_static {}".format(
              file_name, sym_link))
    if ret.failed:
        return False

    return True
