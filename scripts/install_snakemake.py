#!/usr/bin/env python3
import os, sys
import getpass
import tempfile
import subprocess

"""
Install Snakemake

This script runs the necessary commands to install Snakemake.
"""

FNULL = open(os.devnull, 'w')

def install_snakemake():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:

        print("Installing snakemake...")

        # ---------------------------
        # Install snakemake

        pyenvbin = os.environ['HOME']
        condabin = pyenvbin+"/.pyenv/shims/conda"

        print(" - Adding channels:")

        print("     - r")
        subprocess.call([condabin,"config","--add","channels","r"]          , stdout=FNULL)

        print("     - default")
        subprocess.call([condabin,"config","--add","channels","default"]    , stdout=FNULL)

        print("     - conda-forge")
        subprocess.call([condabin,"config","--add","channels","conda-forge"], stdout=FNULL)

        print("     - bioconda")
        subprocess.call([condabin,"config","--add","channels","bioconda"]   , stdout=FNULL)

        #subprocess.call([condabin,"install","--yes","-c","bioconda","snakemake"])

        print(" - Installing snakemake")
        condacmd = ["conda","install","-y","-c","bioconda","snakemake"]
        subprocess.call(condacmd, stdout=FNULL)

        # ---------------------------
        # Install osf cli client
        
        pyenvbin = os.environ['HOME']
        pipbin = pyenvbin+"/.pyenv/shims/pip"

        print(" - Upgrading pip")
        subprocess.call([pipbin,"install","--upgrade","pip"]   , stdout=FNULL)

        print(" - Installing OSF CLI client")
        subprocess.call([pipbin,"install","--user","osfclient"], stdout=FNULL)


        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Snakemake and the OSF client are now installed.")
        print("     Test that snakemake is working using the following one-liner:\n")
        print("         python -c 'import snakemake'")
        print()


if __name__=="__main__":
    install_snakemake()

