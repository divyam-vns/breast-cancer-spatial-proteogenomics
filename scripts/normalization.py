
import scanpy as sc

def normalize_and_select_hvg(adata):
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    sc.pp.highly_variable_genes(
        adata,
        flavor='seurat',
        n_top_genes=2000
    )

    return adata
