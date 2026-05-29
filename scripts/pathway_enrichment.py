
# Pathway Enrichment Pipeline (Upgrade B)

import os
import pandas as pd
import gseapy as gp

def run_pathway_enrichment(cluster_genes):
    os.makedirs('results/tables/pathways', exist_ok=True)
    os.makedirs('results/figures/pathways', exist_ok=True)

    all_results = []

    for cluster_id, genes in cluster_genes.items():
        genes = [g for g in genes if isinstance(g, str)][:100]

        if len(genes) < 10:
            continue

        enr = gp.enrichr(
            gene_list=genes,
            gene_sets=["GO_Biological_Process_2023", "MSigDB_Hallmark_2020"],
            organism="human",
            outdir=f"results/pathway_enrichment/cluster_{cluster_id}",
            cutoff=0.5
        )

        df = enr.results.copy()
        df["cluster"] = cluster_id
        all_results.append(df)

        df.to_csv(f"results/tables/pathways/cluster_{cluster_id}.csv", index=False)

    all_pathways = pd.concat(all_results, ignore_index=True)
    all_pathways.to_csv("results/tables/pathways/all_clusters_full.csv", index=False)

    return all_pathways
