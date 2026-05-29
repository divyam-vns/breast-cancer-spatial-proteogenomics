
# TME Annotation Pipeline

import pandas as pd

def run_tme_annotation(adata, tme_markers):
    cluster_col = "leiden"
    clusters = adata.obs[cluster_col]

    expr_df = pd.DataFrame(
        adata.X.toarray() if hasattr(adata.X, "toarray") else adata.X,
        columns=adata.var_names,
        index=clusters
    ).groupby(level=0).mean()

    cluster_scores = expr_df.copy()

    for cell_type, genes in tme_markers.items():
        genes = [g for g in genes if g in cluster_scores.columns]
        cluster_scores[cell_type] = cluster_scores[genes].mean(axis=1)

    cluster_scores["TME_label"] = cluster_scores[list(tme_markers.keys())].idxmax(axis=1)

    return cluster_scores
