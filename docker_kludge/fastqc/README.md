# fastqc Dockerfile

This dockerfile downloads fastqc from a recent version of miniconda.

Build the docker image:

```
docker build -t dahak_fastqc .
```

or, to use a Dockerfile with a different name, use the `-f` flag:

```
docker build -t dahak_fastqc -f Dockerfile.custom .
```

Test out the image:

```
docker run -it dahak_fastqc fastqc -h
```

should print out fastqc help.
