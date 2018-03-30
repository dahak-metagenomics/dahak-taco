#!/usr/bin/env python3
import os
import getpass
import tempfile
import subprocess


def install_pyenv():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:
        # Install snakemake
        conda_version = "miniconda3-4.3.30"

        installcmd = ["pyenv","install",conda_version]
        subprocess.call(installcmd)
        
        globalcmd = ["pyenv","global",conda_version]
        subprocess.call(globalcmd)

        # ---------------------------
        # Install snakemake

        pyenvbin = os.environ['HOME']
        condabin = pyenvbin+"/.pyenv/shims/conda"

        subprocess.call([condabin,"update"])

        subprocess.call([condabin,"config","--add","channels","r"])
        subprocess.call([condabin,"config","--add","channels","default"])
        subprocess.call([condabin,"config","--add","channels","conda-forge"])
        subprocess.call([condabin,"config","--add","channels","bioconda"])

        subprocess.call([condabin,"install","--yes","-c","bioconda","snakemake"])

        # ---------------------------
        # Install osf cli client
        
        pyenvbin = os.environ['HOME']
        pipbin = pyenvbin+"/.pyenv/shims/pip"

        subprocess.call([pipbin,"install","--upgrade","pip"])
        subprocess.call([pipbin,"install","--user","osfclient"])



if __name__=="__main__":
    install_pyenv()

