import scanpy as sc
import os
import pandas as pd

atlas_path = '/Users/christophebecavin/Documents/testatlas/HTAP_691048/outs/filtered_feature_bc_matrix.h5'
CELLRANGER_FILE = "/outs/filtered_feature_bc_matrix.h5"
cellranger_path = atlas_path.replace(CELLRANGER_FILE, "")
cellranger_path = os.path.join(cellranger_path, "outs")
clust_path = os.path.join(cellranger_path, "analysis", "clustering", "graphclust", "clusters.csv")
rna_umap = os.path.join(cellranger_path, "analysis", "umap", "2_components", "projection.csv")
rna_tsne = os.path.join(cellranger_path, "analysis", "tsne", "2_components", "projection.csv")
rna_pca = os.path.join(cellranger_path, "analysis", "pca", "10_components", "projection.csv")


print(f"Read atlas {atlas_path}")
adata = sc.read_10x_h5(atlas_path)
adata.var_names_make_unique()


# Add cluster
if os.path.exists(clust_path):
    print(f"Add cluster from {clust_path}")
    df_cluster = pd.read_csv(clust_path, index_col=0)
    adata.obs['cellranger_graphclust'] = df_cluster["Cluster"]

if os.path.exists(rna_umap):
    print(f"Add umap from {rna_umap}")
    df_umap = pd.read_csv(rna_umap, index_col=0)
    adata.obsm['X_umap'] = df_umap

if os.path.exists(rna_tsne):
    print(f"Add t-SNE from {rna_tsne}")
    df_tsne = pd.read_csv(rna_tsne, index_col=0)
    adata.obsm['X_tsne'] = df_tsne

if os.path.exists(rna_pca):
    print(f"Add pca from {rna_pca}")
    df_pca = pd.read_csv(rna_pca, index_col=0)
    adata.obsm['X_pca'] = df_pca

print(f"Your adata is ready")
print(adata)
