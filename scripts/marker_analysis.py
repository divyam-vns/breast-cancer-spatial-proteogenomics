
import scanpy as sc

def marker_analysis(adata):

    sc.tl.rank_genes_groups(
        adata,
        groupby='leiden',
        method='wilcoxon'
    )

    return adata
