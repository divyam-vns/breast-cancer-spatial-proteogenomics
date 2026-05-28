
import scanpy as sc

def find_markers(adata):
    sc.tl.rank_genes_groups(
        adata,
        groupby='leiden',
        method='wilcoxon'
    )

    return adata
