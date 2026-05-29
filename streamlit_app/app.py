import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("🧬 Breast Cancer Spatial Transcriptomics Explorer")

st.markdown(
"""
Integrated spatial multi-omics dashboard:
- QC & preprocessing
- Spatial clustering
- Marker genes & biomarkers
- TME (Tumor Microenvironment) analysis
- Cell–cell communication
- Pathway enrichment
- Spatial functional modules
"""
)

# =========================================================
# SAFE IMAGE DISPLAY WITH ZOOM
# =========================================================
def show_image(path, caption):

    if os.path.exists(path):

        try:
            img = Image.open(path)

            with st.expander(f"🔍 {caption}", expanded=False):

                zoom = st.slider(
                    f"Size: {caption}",
                    min_value=300,
                    max_value=1400,
                    value=800,
                    step=100,
                    key=path
                )

                st.image(img, caption=caption, width=zoom)

        except Exception as e:
            st.warning(f"Could not load {path}: {e}")

    else:
        st.warning(f"Missing file: {path}")


# =========================================================
# QC SECTION
# =========================================================
st.header("🧪 QC Metrics")

show_image("results/figures/violin_qc_violin.png", "QC Violin Plot")
show_image("results/figures/show_qc_spatial.png", "Spatial QC")

# =========================================================
# HVG + PREPROCESSING
# =========================================================
st.header("📊 Highly Variable Genes")

show_image("results/figures/filter_genes_dispersion_hvg.png", "HVG Selection")

# =========================================================
# CLUSTERING
# =========================================================
st.header("🧬 Spatial Clustering")

show_image("results/figures/umap_umap_clusters.png", "UMAP Clusters")
show_image("results/figures/show_spatial_clusters.png", "Spatial Clusters")

# =========================================================
# MARKER GENES + BIOMARKERS
# =========================================================
st.header("🧠 Marker Genes & Biomarkers")

show_image("results/figures/rank_genes_groups_leiden_marker_genes.png", "Marker Genes")
show_image("results/figures/spatial_biomarker_example.png", "Spatial Biomarkers Example")
show_image("results/figures/top_biomarker_spatial.png", "Top Biomarker Map")

# Biomarker folder
biomarker_dir = "results/figures/biomarkers"
if os.path.exists(biomarker_dir):
    for f in sorted(os.listdir(biomarker_dir)):
        if f.endswith(".png"):
            show_image(os.path.join(biomarker_dir, f), f)

# =========================================================
# PATHWAY ENRICHMENT (ALL CLUSTERS)
# =========================================================
st.header("🧬 Pathway Enrichment")

show_image("results/figures/pathways_all_clusters_overview.png", "Pathway Overview")
show_image("results/figures/pathways_summary_all_clusters.png", "Pathway Summary")

pathway_dir = "results/figures/pathway_enrichment"
if os.path.exists(pathway_dir):
    for cluster in sorted(os.listdir(pathway_dir)):
        cluster_path = os.path.join(pathway_dir, cluster)
        if os.path.isdir(cluster_path):
            st.subheader(f"Cluster {cluster}")
            for f in sorted(os.listdir(cluster_path)):
                if f.endswith(".png"):
                    show_image(os.path.join(cluster_path, f), f)

# =========================================================
# TME ANALYSIS
# =========================================================
st.header("🧫 Tumor Microenvironment (TME)")

show_image("results/figures/tme_spatial_map.png", "TME Spatial Map")
show_image("results/figures/tissue_domains.png", "Tissue Domains")

tme_figs = [
    "results/figures/tme_cluster_scores.png",
    "results/figures/step9_spatial_feature_overlay.png",
    "results/figures/show_step9_spatial_architecture.png"
]

for f in tme_figs:
    show_image(f, os.path.basename(f))

# =========================================================
# CELL–CELL COMMUNICATION
# =========================================================
st.header("🔗 Cell–Cell Communication")

show_image("results/figures/cell_communication/tme_interaction_matrix.png", "TME Interaction Matrix")
show_image("results/figures/cell_communication/tme_neighborhood_enrichment.png", "Neighborhood Enrichment")
show_image("results/figures/_cluster_interactions.png", "Cluster Interactions")

# =========================================================
# TABLES
# =========================================================
st.header("📊 Data Tables")

table_files = [
    "results/tables/qc_summary.csv",
    "results/tables/hvg_table.csv",
    "results/tables/cluster_marker_genes.csv",
    "results/tables/spatial_autocorr_genes.csv",
    "results/tables/top10_marker_genes_per_cluster.csv",
    "results/tables/spatial_biomarkers_top10.csv",
    "results/tables/figure_index.csv",
    "results/tables/tme/cluster_scores_tme.csv",
    "results/tables/tme/spot_tme_labels.csv",
    "results/tables/tme/cluster_functional_annotation.csv",
    "results/tables/pathways/top_pathways_per_cluster.csv",
    "results/tables/cell_communication/tme_interaction_matrix.csv",
    "results/tables/cell_communication/tme_nhood_enrichment_zscore.csv"
]

for table in table_files:
    if os.path.exists(table):
        st.subheader(os.path.basename(table))
        df = pd.read_csv(table)
        st.dataframe(df.head(30), use_container_width=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.success("🚀 Full Spatial Multi-Omics Explorer Loaded")
st.caption("Built with Scanpy + Squidpy + Pathway + TME + Cell Communication modules")
