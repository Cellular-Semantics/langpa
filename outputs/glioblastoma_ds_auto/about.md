## Source data description

Source data comes from an analysis of scRNAseq and spatial transcriptomics data from multiple human Glioblastoma samples (de Jong et al. 2025). In this paper, scRNAseq data was analysed using cell2fate (Aivazidis et al. 2025), a Bayesian generative model designed to infer temporal expression modules from RNA velocity data. This analysis was run separately for each tumor subclone. The RNA velocity modules inferred by cell2fate were subsequently hierarchically clustered. The clustering utilized the Jaccard distance of the top 200 genes in each module for the purpose of inter-clone module annotation. This process resulted in the identification of 15 meta-modules.  These gene lists were analysed  using over-representation analysis of MGSigDB signatures and by testing enrichment across separately derived malignant cell state annotations (e.g. OPC-like). The latter were used in the naming of meta-modules.

We took each metamodule gene list (table S10 in de Jong et al., 2025) and ran pseudo-gene set enrichment using langpa. 




