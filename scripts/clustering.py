
import scanpy as sc

def run_clustering(adata):
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=0.5, flavor='igraph', n_iterations=2)
    return adata
