#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

FNULL = open(os.devnull, 'w')

def install_docker():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
    else:

        print("Installing docker...")

        # -----------------------
        # Parameters:

        # User to add to the docker group
        user = "ubuntu"

        # -----------------------
        # Update aptitude and install dependencies
        print(" - updating aptitude")
        aptupdatecmd = ["apt-get","-y","update"]
        subprocess.call(aptupdatecmd, stdout=FNULL)
        
        print(" - install dependencies")
        aptinstallcmd = ["apt-get","-y","install"]
        libs = ["zlib1g-dev","ncurses-dev"]
        for lib in libs:
            subprocess.call(aptinstallcmd+[lib], stdout=FNULL)

        # -----------------------
        # Install docker
        print(" - installing docker")
        # note: this is okay to run a second time...
        wgetproc = subprocess.Popen(["wget","-qO-","https://get.docker.com"], stdout=subprocess.PIPE)
        bashproc = subprocess.call(["/bin/bash"], stdin=wgetproc.stdout, stdout=FNULL)
        subprocess.call(["sleep","30"])

        print(" - adding user %s to docker group"%(user))
        subprocess.Popen(["groupadd","-f","docker"],stdout=FNULL)
        subprocess.Popen(["usermod","-aG","docker",user],stdout=FNULL)

if __name__=="__main__":
    install_docker()


