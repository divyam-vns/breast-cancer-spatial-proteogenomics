
import streamlit as st
import scanpy as sc
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Spatial Transcriptomics Explorer",
    layout="wide"
)

st.title(" Breast Cancer Spatial Transcriptomics Explorer")

@st.cache_data
def load_data():
    adata = sc.read("data/processed/checkpoint_step10_biomarkers.h5ad")
    return adata

adata = load_data()

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.header("Controls")

gene = st.sidebar.selectbox(
    "Select Gene",
    adata.var_names[:2000]
)

# ---------------------------
# UMAP
# ---------------------------
st.subheader(" UMAP Clusters")

fig1 = sc.pl.umap(
    adata,
    color="leiden",
    show=False,
    return_fig=True
)

st.pyplot(fig1)

# ---------------------------
# Spatial Plot
# ---------------------------
st.subheader(f" Spatial Expression: {gene}")

fig2 = sc.pl.spatial(
    adata,
    color=gene,
    show=False,
    return_fig=True
)

st.pyplot(fig2)

# ---------------------------
# Metadata
# ---------------------------
st.subheader(" Dataset Summary")

st.write(adata)
