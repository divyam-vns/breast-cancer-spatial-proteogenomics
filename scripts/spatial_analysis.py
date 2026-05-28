
import squidpy as sq
import scanpy as sc

def spatial_analysis(adata):

    sq.gr.spatial_neighbors(adata)
    sq.gr.nhood_enrichment(adata, cluster_key='leiden')
    sq.gr.spatial_autocorr(adata, mode='moran')

    return adata
