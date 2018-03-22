#!/usr/bin/env python
import getpass
import subprocess


def install_pyenv():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:
        # Install pyenv 
        curlcmd = ["curl","-L","https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer"]
        curlproc = subprocess.Popen(curlcmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        subprocess.Popen(["/bin/bash"], stdin=curlproc.stdout, stdout=subprocess.DEVNULL)

        # We don't need to add ~/.pyenv/bin to $PATH,
        # it is already done.


if __name__=="__main__":
    install_pyenv()


