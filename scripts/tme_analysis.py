
import scanpy as sc

def tumor_microenvironment_analysis(adata):

    sc.pl.spatial(adata, color='leiden')
    sc.pl.spatial(adata, color='total_counts')

    return adata
