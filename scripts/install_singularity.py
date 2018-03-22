#!/usr/bin/env python
import getpass
import subprocess


def install_singularity():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
    else:

        # -----------------------
        # Update aptitude and install dependencies
        aptupdatecmd = ["apt-get","-y","update"]
        subprocess.call(aptupdatecmd)
        
        aptinstallcmd = ["apt-get","-y","install"]
        subprocess.call(aptinstallcmd+["zlib1g-dev"])
        subprocess.call(aptinstallcmd+["ncurses-dev"])

        # -----------------------
        # Install docker
        wgetproc = subprocess.Popen(["wget","-qO-","https://get.docker.com"], stdout=subprocess.PIPE)
        bashproc = subprocess.Popen(["/bin/bash"], stdin=wgetproc.stdout, stdout=subprocess.PIPE)

        subprocess.call(["usermod","-aG","docker","ubuntu"])

        # -----------------------
        # Install singularity:
        wgetproc = subprocess.Popen(["wget","-O-","http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list"],stdout=subprocess.PIPE)
        bashproc = subprocess.Popen(["/bin/bash"], stdin=wgetproc.stdout, stdout=subprocess.PIPE)

        keyupdatecmd = ["apt-key","adv","--recv-keys","--keyserver","hkp://pool.sks-keyservers.net:80","0xA5D32F012649A5A9"]
        subprocess.call(keyupdatecmd)

        subprocess.call(aptupdatecmd)
        subprocess.call(aptinstallcmd+["singularity-container"])
        
        print("-"*40)
        print()
        print("Singularity is now installed. Log out and log back in for docker group to take effect.")
        print()
        print("-"*40)

if __name__=="__main__":
    install_singularity()

