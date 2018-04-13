FROM continuumio/miniconda

MAINTAINER cmreid@ucdavis.edu

RUN conda config --add channels defaults \
    && conda config --add channels conda-forge \
    && conda config --add channels bioconda \
    && conda install -y conda-forge::openjdk fastqc=0.11.7

