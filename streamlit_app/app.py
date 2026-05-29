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
- Biomarkers
- TME interactions
- Ligand–Receptor signaling
- Cell–Cell communication networks
"""
)

# -----------------------------
# SAFE IMAGE FUNCTION (WITH ZOOM)
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
                    value=800,
                    step=100,
                    key=caption
                )

                st.image(img, caption=caption, width=zoom)

        except Exception as e:
            st.warning(f"Could not load {path}: {e}")

    else:
        st.warning(f"Missing file: {path}")

# =====================================================
# QC SECTION
# =====================================================
st.header("🧪 QC Metrics")

show_image("results/figures/violin_qc_violin.png", "QC Violin Plot")
show_image("results/figures/show_qc_spatial.png", "Spatial QC")

# =====================================================
# HVG SECTION
# =====================================================
st.header("📈 Highly Variable Genes")

show_image("results/figures/filter_genes_dispersion_hvg.png", "HVG Plot")

# =====================================================
# CLUSTERING
# =====================================================
st.header("🧬 Spatial Clustering")

show_image("results/figures/umap_umap_clusters.png", "UMAP Clusters")
show_image("results/figures/show_spatial_clusters.png", "Spatial Clusters")

# =====================================================
# MARKER GENES
# =====================================================
st.header("🔬 Marker Genes")

show_image(
    "results/figures/rank_genes_groups_leiden_marker_genes.png",
    "Cluster Marker Genes"
)

# =====================================================
# SPATIAL BIOMARKERS
# =====================================================
st.header("🧫 Spatial Biomarkers")

biomarker_dir = "results/figures/biomarkers"

if os.path.exists(biomarker_dir):

    biomarker_files = [
        f for f in os.listdir(biomarker_dir)
        if f.endswith(".png")
    ]

    for f in sorted(biomarker_files):
        show_image(os.path.join(biomarker_dir, f), f)

else:
    st.warning("Biomarker directory missing")

# =====================================================
# TME ANALYSIS (NEW)
# =====================================================
st.header("🧠 Tumor Microenvironment (TME) Analysis")

tme_dir = "results/figures/tme"

tme_figs = [
    ("tme_interaction_matrix.png", "TME Interaction Matrix"),
    ("tme_cluster_scores.png", "TME Cluster Scores"),
    ("tme_heatmap.png", "TME Heatmap")
]

for f, cap in tme_figs:
    show_image(os.path.join(tme_dir, f), cap)

# =====================================================
# LIGAND–RECEPTOR SIGNALING (NEW)
# =====================================================
st.header("🔗 Ligand–Receptor Signaling")

lr_dir = "results/figures/ligand_receptor"

lr_figs = [
    ("lr_network.png", "Ligand–Receptor Network"),
    ("lr_heatmap.png", "Ligand–Receptor Heatmap"),
    ("lr_dotplot.png", "Ligand–Receptor Dotplot")
]

for f, cap in lr_figs:
    show_image(os.path.join(lr_dir, f), cap)

# =====================================================
# CELL–CELL COMMUNICATION (NEW)
# =====================================================
st.header("🤝 Cell–Cell Communication")

cc_dir = "results/figures/cell_communication"

cc_figs = [
    ("interaction_matrix.png", "Interaction Matrix"),
    ("cluster_interactions.png", "Cluster Interaction Network"),
    ("neighborhood_enrichment.png", "Neighborhood Enrichment")
]

for f, cap in cc_figs:
    show_image(os.path.join(cc_dir, f), cap)

# =====================================================
# TABLES
# =====================================================
st.header("📊 Results Tables")

table_files = [
    "results/tables/qc_summary.csv",
    "results/tables/hvg_table.csv",
    "results/tables/cluster_marker_genes.csv",
    "results/tables/spatial_autocorr_genes.csv",
    "results/tables/tme_cluster_scores.csv",
    "results/tables/ligand_receptor_summary.csv",
    "results/tables/interaction_matrix.csv"
]

for table in table_files:

    if os.path.exists(table):

        st.subheader(os.path.basename(table))

        df = pd.read_csv(table)

        st.dataframe(df.head(20), use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown(
"🧬 Spatial Transcriptomics Pipeline (Scanpy + Squidpy + TME + LR + Cell Communication)"
)
