from ._codebook_loader import load_codebook

def load_metadata_tab():
    return load_codebook("metadata")

def load_tables_tab():
    return load_codebook("tables")

def load_project_tab():
    return load_codebook("project")

def load_nlp_performance():
    return load_codebook("nlp_performance")