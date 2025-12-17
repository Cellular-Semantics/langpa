# glioblastoma_ds_auto

## Source data description

Source data comes from an analysis of scRNAseq and spatial transcriptomics data from multiple human Glioblastoma samples (de Jong et al. 2025). In this paper, scRNAseq data was analysed using cell2fate (Aivazidis et al. 2025), a Bayesian generative model designed to infer temporal expression modules from RNA velocity data. This analysis was run separately for each tumor subclone. The RNA velocity modules inferred by cell2fate were subsequently hierarchically clustered. The clustering utilized the Jaccard distance of the top 200 genes in each module for the purpose of inter-clone module annotation. This process resulted in the identification of 15 meta-modules.  These gene lists were analysed  using over-representation analysis of MGSigDB signatures and by testing enrichment across separately derived malignant cell state annotations (e.g. OPC-like). The latter were used in the naming of meta-modules.

We took each metamodule gene list (table S10 in de Jong et al., 2025) and ran pseudo-gene set enrichment using langpa.

## Results

### 0_Gliosis

**Context**: malignant glioblastoma cells

**Genes**: 111 total, 0 covered by programs (0%)

#### Runs

- **20251126_135814**: [deepsearch_container.md](0_Gliosis/20251126_135814/deepsearch_container.md) | [deepsearch_structured.json](0_Gliosis/20251126_135814/deepsearch_structured.json)
- **20251126_125238**: [deepsearch_container.md](0_Gliosis/20251126_125238/deepsearch_container.md) | [deepsearch_structured.json](0_Gliosis/20251126_125238/deepsearch_structured.json)

### 10_AC_gliosis_like_2

**Context**: malignant glioblastoma cells

**Genes**: 118 total, 0 covered by programs (0%)

#### Runs

- **20251126_144326**: [deepsearch_container.md](10_AC_gliosis_like_2/20251126_144326/deepsearch_container.md) | [deepsearch_structured.json](10_AC_gliosis_like_2/20251126_144326/deepsearch_structured.json)
- **20251126_132637**: [deepsearch_container.md](10_AC_gliosis_like_2/20251126_132637/deepsearch_container.md) | [deepsearch_structured.json](10_AC_gliosis_like_2/20251126_132637/deepsearch_structured.json)

### 11_OPC_like_1

**Context**: malignant glioblastoma cells

**Genes**: 109 total, 0 covered by programs (0%)

#### Runs

- **20251126_144843**: [deepsearch_container.md](11_OPC_like_1/20251126_144843/deepsearch_container.md) | [deepsearch_structured.json](11_OPC_like_1/20251126_144843/deepsearch_structured.json)
- **20251126_133059**: [deepsearch_container.md](11_OPC_like_1/20251126_133059/deepsearch_container.md) | [deepsearch_structured.json](11_OPC_like_1/20251126_133059/deepsearch_structured.json)

### 12_NPC_neuronal_like_3

**Context**: malignant glioblastoma cells

**Genes**: 159 total, 0 covered by programs (0%)

#### Runs

- **20251126_145428**: [deepsearch_container.md](12_NPC_neuronal_like_3/20251126_145428/deepsearch_container.md) | [deepsearch_structured.json](12_NPC_neuronal_like_3/20251126_145428/deepsearch_structured.json)
- **20251126_133359**: [deepsearch_container.md](12_NPC_neuronal_like_3/20251126_133359/deepsearch_container.md) | [deepsearch_structured.json](12_NPC_neuronal_like_3/20251126_133359/deepsearch_structured.json)

### 1_OPC_AC_like_1

**Context**: malignant glioblastoma cells

**Genes**: 55 total, 0 covered by programs (0%)

#### Runs

- **20251126_140224**: [deepsearch_container.md](1_OPC_AC_like_1/20251126_140224/deepsearch_container.md) | [deepsearch_structured.json](1_OPC_AC_like_1/20251126_140224/deepsearch_structured.json)
- **20251126_125736**: [deepsearch_container.md](1_OPC_AC_like_1/20251126_125736/deepsearch_container.md) | [deepsearch_structured.json](1_OPC_AC_like_1/20251126_125736/deepsearch_structured.json)

### 2_NPC_neuronal_like_1

**Context**: malignant glioblastoma cells

**Genes**: 94 total, 0 covered by programs (0%)

#### Runs

- **20251126_140831**: [deepsearch_container.md](2_NPC_neuronal_like_1/20251126_140831/deepsearch_container.md) | [deepsearch_structured.json](2_NPC_neuronal_like_1/20251126_140831/deepsearch_structured.json)
- **20251126_130034**: [deepsearch_container.md](2_NPC_neuronal_like_1/20251126_130034/deepsearch_container.md) | [deepsearch_structured.json](2_NPC_neuronal_like_1/20251126_130034/deepsearch_structured.json)

### 3_NPC_neuronal_like_2

**Context**: malignant glioblastoma cells

**Genes**: 136 total, 0 covered by programs (0%)

#### Runs

- **20251126_141307**: [deepsearch_container.md](3_NPC_neuronal_like_2/20251126_141307/deepsearch_container.md) | [deepsearch_structured.json](3_NPC_neuronal_like_2/20251126_141307/deepsearch_structured.json)
- **20251126_130035**: [deepsearch_container.md](3_NPC_neuronal_like_2/20251126_130035/deepsearch_container.md) | [deepsearch_structured.json](3_NPC_neuronal_like_2/20251126_130035/deepsearch_structured.json)

### 4_AC_gliosis_like_1

**Context**: malignant glioblastoma cells

**Genes**: 99 total, 0 covered by programs (0%)

#### Runs

- **20251126_141722**: [deepsearch_container.md](4_AC_gliosis_like_1/20251126_141722/deepsearch_container.md) | [deepsearch_structured.json](4_AC_gliosis_like_1/20251126_141722/deepsearch_structured.json)

### 5_AC_neuronal_like

**Context**: malignant glioblastoma cells

**Genes**: 373 total, 0 covered by programs (0%)

#### Runs

- **20251126_142015**: [deepsearch_container.md](5_AC_neuronal_like/20251126_142015/deepsearch_container.md) | [deepsearch_structured.json](5_AC_neuronal_like/20251126_142015/deepsearch_structured.json)
- **20251126_130844**: [deepsearch_container.md](5_AC_neuronal_like/20251126_130844/deepsearch_container.md) | [deepsearch_structured.json](5_AC_neuronal_like/20251126_130844/deepsearch_structured.json)
