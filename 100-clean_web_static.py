#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
    contents of the web_static folder
"""


from datetime import datetime
from fabric.api import local, env, hosts, put, run


env.hosts = ['34.229.63.14', '100.27.49.144']


def do_clean(number=0):
    """distributes an archive to your web servers"""

    env.user = 'ubuntu'
    env.disable_known_hosts = True
    env.key_filename = "~/.ssh/id_rsa"

    if number == 0:
        number += 1

    num = local("ls versions/ | wc -l", capture=True)
    if int(num) == 1:
        num = 2
    if int(num) == 0:
        return

    local("ls -d $PWD versions/* | tail -{} | xargs rm -f --".format(
        int(num) - int(number)))

    run("cd /data/web_static/releases")
    run("ls -1t | tail -{} | xargs rm --".
        format(int(num) - int(number)))
