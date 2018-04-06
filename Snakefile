from os.path import join

# See subworkflow documentation:
# https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#snakefiles-sub-workflows

subworkflow read_filtering:
    workdir: "."
    snakefile: "rules/read_filtering/Snakefile"

subworkflow taxonomic_classification:
    workdir: "."
    snakefile: "rules/taxonomic_classification/Snakefile"

