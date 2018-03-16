logo = """
 _______  _______  _______  _______
|       ||   _   ||       ||       |
|_     _||  |_|  ||       ||   _   |
  |   |  |       ||       ||  | |  |
  |   |  |       ||      _||  |_|  |
  |   |  |   _   ||     |_ |       |
  |___|  |__| |__||_______||_______|

experimental CL interface for dahak workflows
"""

# ----------------------

taco_description = "dahak-taco is an experimental command line interface for dahak workflows"
taco_usage = """taco <workflow> [<args>]

Available workflows:
    trim_reads              Trim sequence reads

Workflows that have not been implemented yet:
    quality                 Filter reads based on quality
    tax_class               Taxonomic classification
    abundance_estimation    (Insert description here)
    variant_calling         (Insert description here)
    element_id              (Insert description here)
    functional_inference    (Insert description here)
    sample_comparison       (Insert description here)

"""

trim_reads_description = "Trim sequence reads"
trim_reads_usage = """taco trim_reads <trim_parameters> [<args>]

The parameter sets available are:
    lenient
    strict
"""






