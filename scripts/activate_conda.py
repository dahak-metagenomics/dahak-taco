#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

"""
Activate Conda

Run the commands to install a version of conda
that is acceptable to us, using pyenv.
Make this the global pyenv version.
Make sure dotfiles always update $PATH.

pyenv istall <version>
pyenv global <version>
eval "$(pyenv init -)"
"""

FNULL = open(os.devnull, 'w')

def install_pyenv():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:

        print("Activating conda...")

        version = "miniconda3-4.3.30"

        print(" - installing pyenv version %s"%(version))
        installcmd = ["pyenv","install","-f",version]
        installproc = subprocess.call(installcmd, stdout=FNULL, stderr=FNULL)

        print(" - setting global pyenv version")
        globalcmd = ["pyenv","global",version]
        globalproc = subprocess.call(globalcmd, stdout=FNULL, stderr=FNULL)

        print(" - pyenv init piped to bash")
        pyenvinitcmd = ["pyenv","init","-"]
        pyenvinitproc = subprocess.Popen(pyenvinitcmd, stdout=subprocess.PIPE)

        evalcmd = ["bash"]
        evalproc = subprocess.Popen(evalcmd, stdin=pyenvinitproc.stdout)

        print("Done.\n")
        subprocess.call(["which","python"])

if __name__=="__main__":
    install_pyenv()
