
import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("🧬 Breast Cancer Spatial Transcriptomics Explorer")

st.markdown(
"""
Interactive visualization of:
- QC metrics
- Spatial clustering
- Marker genes
- Biomarker regions
- Spatial transcriptomics results
"""
)

# -----------------------------
# Helper function
# -----------------------------
def show_image(path, caption):

    if os.path.exists(path):

        try:
            img = Image.open(path)

            with st.expander(f"🔍 {caption}", expanded=True):

                zoom = st.slider(
                    f"Width: {caption}",
                    min_value=300,
                    max_value=1400,
                    value=700,
                    step=100,
                    key=caption
                )

                st.image(img, caption=caption, width=zoom)

        except Exception as e:
            st.warning(f"Could not load {path}: {e}")

    else:
        st.warning(f"Missing file: {path}")

# -----------------------------
# QC FIGURES
# -----------------------------
st.header("QC Metrics")

show_image(
    "results/figures/violin_qc_violin.png",
    "QC Violin Plot"
)

show_image(
    "results/figures/show_qc_spatial.png",
    "Spatial QC"
)

# -----------------------------
# HVG
# -----------------------------
st.header("Highly Variable Genes")

show_image(
    "results/figures/filter_genes_dispersion_hvg.png",
    "Highly Variable Genes"
)

# -----------------------------
# CLUSTERING
# -----------------------------
st.header("Spatial Clustering")

show_image(
    "results/figures/umap_umap_clusters.png",
    "UMAP Clusters"
)

show_image(
    "results/figures/show_spatial_clusters.png",
    "Spatial Tissue Clusters"
)

# -----------------------------
# MARKER GENES
# -----------------------------
st.header("Marker Genes")

show_image(
    "results/figures/rank_genes_groups_leiden_marker_genes.png",
    "Cluster Marker Genes"
)

# -----------------------------
# SPATIAL BIOMARKERS
# -----------------------------
st.header("Spatial Biomarkers")

biomarker_dir = "results/figures/biomarkers"

if os.path.exists(biomarker_dir):

    biomarker_files = [
        f for f in os.listdir(biomarker_dir)
        if f.endswith(".png")
    ]

    for f in sorted(biomarker_files):

        show_image(
            os.path.join(biomarker_dir, f),
            f
        )

else:
    st.warning("Biomarker directory missing")

# -----------------------------
# TABLES
# -----------------------------
st.header("Results Tables")

table_files = [
    "results/tables/qc_summary.csv",
    "results/tables/hvg_table.csv",
    "results/tables/cluster_marker_genes.csv",
    "results/tables/spatial_autocorr_genes.csv"
]

for table in table_files:

    if os.path.exists(table):

        st.subheader(os.path.basename(table))

        df = pd.read_csv(table)

        st.dataframe(df.head(20), width="stretch")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Spatial transcriptomics pipeline built with Scanpy + Squidpy + Streamlit")
