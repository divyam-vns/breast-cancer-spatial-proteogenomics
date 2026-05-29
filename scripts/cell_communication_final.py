
import scanpy as sc
import squidpy as sq
import pandas as pd
import matplotlib.pyplot as plt

adata = sc.read("data/processed/TME_FINAL_FIXED.h5ad")

adata.obs["TME"] = adata.obs["TME"].astype("category")

# spatial graph
sq.gr.spatial_neighbors(adata)

# interaction matrix
sq.gr.interaction_matrix(
    adata,
    cluster_key="TME"
)

# neighborhood enrichment
sq.gr.nhood_enrichment(
    adata,
    cluster_key="TME"
)

# save interaction plot
sq.pl.interaction_matrix(
    adata,
    cluster_key="TME",
    cmap="Reds"
)
plt.savefig(
    "results/figures/cell_communication/tme_interaction_matrix.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# save enrichment plot
sq.pl.nhood_enrichment(
    adata,
    cluster_key="TME",
    cmap="coolwarm"
)
plt.savefig(
    "results/figures/cell_communication/tme_neighborhood_enrichment.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()
