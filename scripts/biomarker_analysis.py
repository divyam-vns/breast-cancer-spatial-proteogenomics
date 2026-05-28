
import scanpy as sc

def biomarker_analysis(adata):

    markers = sc.get.rank_genes_groups_df(adata, group=None)

    strong = markers[
        (markers['pvals_adj'] < 0.05) &
        (markers['logfoldchanges'] > 0.5)
    ]

    return strong
