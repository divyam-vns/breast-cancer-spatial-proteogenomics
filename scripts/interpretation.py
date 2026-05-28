
import scanpy as sc
import squidpy as sq

def interpret_spatial_domains(adata):

    sc.tl.rank_genes_groups(adata, groupby='leiden')

    sq.pl.spatial_scatter(
        adata,
        color='leiden'
    )

    return adata
