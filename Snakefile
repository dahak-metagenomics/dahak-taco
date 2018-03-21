from os.path import join

## Set your custom configuration here
#config = {
#    'application': {
#        'component': {
#            'setting': 'vaue'
#        }
#    }
#}

SNAKEMAKE_RULES_PATH = "rules/"

include: join(SNAKEMAKE_RULES_PATH, "dahak/biocontainers.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/sourmash_sbt.rule")

