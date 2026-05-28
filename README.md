
# 🧬 Breast Cancer Spatial Proteogenomics

## 🔬 Overview
End-to-end spatial transcriptomics analysis of breast cancer tissue using Scanpy + Squidpy.

We identify:
- spatial tissue architecture
- transcriptional clusters
- biomarker genes
- spatial gene activity hotspots

---

## 🧪 Workflow

### 1. QC & Filtering
- gene/spot filtering
- mitochondrial QC
- spatial QC visualization

### 2. Normalization
- library size normalization
- log transformation
- HVG selection

### 3. Dimensionality Reduction
- PCA
- UMAP embedding

### 4. Clustering
- Leiden clustering
- spatial domain identification

### 5. Marker Discovery
- differential gene expression per cluster
- spatial biomarker mapping

### 6. Spatial Biology
- spatial autocorrelation
- cluster interaction analysis

---

## 📊 Key Outputs
- QC plots
- UMAP cluster maps
- spatial tissue maps
- biomarker gene expression maps
- marker gene tables

---

## 🧠 Biological Insight
Identified spatially distinct transcriptional domains showing:
- metabolic heterogeneity
- mitochondrial activity gradients
- region-specific gene expression programs

---

## 🛠 Tech Stack
Scanpy · Squidpy · Pandas · Matplotlib · Python · Colab

---

## 📂 Reproducibility
All steps are reproducible via:
- scripts/
- notebooks/
- saved checkpoints
