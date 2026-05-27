
import scanpy as sc

def run_qc(adata):
    adata.var['mt'] = adata.var_names.str.startswith('mt-')

    sc.pp.calculate_qc_metrics(
        adata,
        qc_vars=['mt'],
        inplace=True
    )

    adata = adata[adata.obs['n_genes_by_counts'] > 200, :]
    adata = adata[adata.obs['total_counts'] > 500, :]

    return adata
