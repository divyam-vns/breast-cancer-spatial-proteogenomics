
import scanpy as sc
import squidpy as sq

adata = sc.read("data/processed/TME_FINAL_FIXED.h5ad")

adata.obs["TME"] = adata.obs["TME"].astype("category")

sq.gr.spatial_neighbors(adata)

sq.gr.interaction_matrix(
    adata,
    cluster_key="TME"
)

sq.gr.nhood_enrichment(
    adata,
    cluster_key="TME"
)

sq.pl.interaction_matrix(
    adata,
    cluster_key="TME",
    cmap="Reds"
)

sq.pl.nhood_enrichment(
    adata,
    cluster_key="TME",
    cmap="coolwarm"
)
