from os.path import join

# Set your custom configuration here
config = {
    'data_dir': 'data/'
}

SNAKEMAKE_RULES_PATH = "rules/"

include: join(SNAKEMAKE_RULES_PATH, "dahak/biocontainers.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/sourmash_sbt.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/calculate_signatures.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/trimmed_data.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/kaiju.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/kaiju2krona.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/filter_taxa.rule")
include: join(SNAKEMAKE_RULES_PATH, "dahak/krona_visualization.rule")
