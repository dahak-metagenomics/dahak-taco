#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

FNULL = open(os.devnull, 'w')

def install_singularity():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
    else:

        print("installing singularity...")

        # -----------------------
        # Parameters:

        # User to add to the docker group
        user = "ubuntu"

        # -----------------------
        # Update aptitude and install dependencies
        print(" - updating aptitude and install dependencies")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        aptupdatecmd = ["apt-get","-y","update"]
        subprocess.call(aptupdatecmd, stdout=FNULL)
        
        print(" - updating aptitude and install dependencies")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        aptinstallcmd = ["apt-get","-y","install"]
        libs = ["zlib1g-dev","ncurses-dev"]
        for lib in libs:
            subprocess.Popen(aptinstallcmd+[lib], stdout=FNULL)

        # -----------------------
        # Install docker
        print(" - installing docker")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        wgetproc = subprocess.Popen(["wget","-qO-","https://get.docker.com"], stdout=subprocess.PIPE)
        bashproc = subprocess.Popen(["/bin/bash"], stdin=wgetproc.stdout, stdout=FNULL)

        print(" - adding user %s to docker group"%(user))
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        subprocess.Popen(["usermod","-aG","docker",user],stdout=FNULL)

        # -----------------------
        # Install singularity:
        print(" - installing singularity aptitude sources")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        wgetproc = subprocess.Popen(["wget","-O-","http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list"],stdout=subprocess.PIPE)
        bashproc = subprocess.Popen(["/bin/bash"], stdin=wgetproc.stdout, stdout=FNULL)

        print(" - installing singularity aptitude key")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        keyupdatecmd = ["apt-key","adv","--recv-keys","--keyserver","hkp://pool.sks-keyservers.net:80","0xA5D32F012649A5A9"]
        subprocess.Popen(keyupdatecmd, stdout=FNULL)

        print(" - updating aptitude repositories")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        subprocess.Popen(aptupdatecmd, stdout=FNULL)

        print(" - intsalling singularity")
        x = input('Proceed? (y/N): ')
        if x is not 'y':
            raise
        subprocess.Popen(aptinstallcmd+["singularity-container"], stdout=FNULL)
        
        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Singularity is now installed.")
        print("     Log out and log back in for the docker group to take effect.")
        print()

if __name__=="__main__":
    install_singularity()

