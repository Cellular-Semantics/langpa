# glioblastoma_ds_auto

## Source data description

Source data comes from an analysis of scRNAseq and spatial transcriptomics data from multiple human Glioblastoma samples (de Jong et al. 2025). In this paper, scRNAseq data was analysed using cell2fate (Aivazidis et al. 2025), a Bayesian generative model designed to infer temporal expression modules from RNA velocity data. This analysis was run separately for each tumor subclone. The RNA velocity modules inferred by cell2fate were subsequently hierarchically clustered. The clustering utilized the Jaccard distance of the top 200 genes in each module for the purpose of inter-clone module annotation. This process resulted in the identification of 15 meta-modules.  These gene lists were analysed  using over-representation analysis of MGSigDB signatures and by testing enrichment across separately derived malignant cell state annotations (e.g. OPC-like). The latter were used in the naming of meta-modules.

We took each metamodule gene list (table S10 in de Jong et al., 2025) and ran pseudo-gene set enrichment using langpa.

## Results

### 0_Gliosis

**Context**: malignant glioblastoma cells

**Genes**: 111 total, 67 covered by programs (60%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| EMT-Driven Invasive Dispersal | 7 | 6% | 5 |
| Tryptophan-Pathway Immune Evasion | 3 | 3% | 4 |
| IL-6/IL-1β-NF-κB/STAT3 Signaling Axis | 6 | 5% | 4 |
| VEGFA-Driven Tumor Angiogenesis | 6 | 5% | 3 |
| MET-Driven Stemness and Invasiveness | 1 | 1% | 2 |
| AXL-Mediated Mesenchymal Programming | 1 | 1% | 2 |
| Apoptosis Evasion and Drug Resistance | 2 | 2% | 3 |
| Innate Immune Pattern Recognition | 4 | 4% | 3 |
| Extracellular Matrix Composition and Immunomodulation | 7 | 6% | 3 |
| Stemness Maintenance and Self-Renewal | 3 | 3% | 3 |
| Immune Checkpoint and T Cell Suppression | 4 | 4% | 3 |
| mRNA-Based Mesenchymal Signaling | 1 | 1% | 2 |
| EMT-Driven Invasion Program | 15 | 14% | 5 |
| Pro-Inflammatory Cytokine Signaling | 7 | 6% | 4 |
| Angiogenesis and Vascular Signaling | 5 | 5% | 4 |
| Immune Evasion and Checkpoint Activation | 7 | 6% | 4 |
| Extracellular Matrix Proteolysis | 7 | 6% | 4 |
| Glioma Stem Cell Maintenance | 7 | 6% | 4 |
| Hypoxia Adaptation and Response | 2 | 2% | 4 |
| Macrophage/Microglia Reprogramming | 11 | 10% | 4 |
| Apoptosis Resistance and Survival Signaling | 6 | 5% | 3 |
| Growth Factor and Receptor Signaling | 4 | 4% | 3 |
| Transcriptional Master Regulation | 4 | 4% | 3 |
| Inflammatory Lipid Mediator Signaling | 1 | 1% | 2 |
| Cellularity and Structural Organization | 4 | 4% | 1 |
| Metabolic Adaptation and Nutrient Sensing | 6 | 5% | 2 |
| DNA Damage Response and Genomic Stability | 3 | 3% | 1 |

</details>

#### Runs

- **20251126_135814**: [deepsearch_container.md](0_Gliosis/20251126_135814/deepsearch_container.md) | [deepsearch_structured.json](0_Gliosis/20251126_135814/deepsearch_structured.json)
- **20251126_125238**: [deepsearch_container.md](0_Gliosis/20251126_125238/deepsearch_container.md) | [deepsearch_structured.json](0_Gliosis/20251126_125238/deepsearch_structured.json)

### 10_AC_gliosis_like_2

**Context**: malignant glioblastoma cells

**Genes**: 118 total, 62 covered by programs (53%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Extracellular Matrix Remodeling and Invasion | 18 | 15% | 4 |
| RTK/MAPK Signaling Inhibition and Feedback | 7 | 6% | 4 |
| Wnt/β-catenin Pathway Activation | 2 | 2% | 2 |
| Angiogenesis and Vascular Remodeling | 5 | 4% | 3 |
| Glioma Stem Cell Maintenance and Self-Renewal | 5 | 4% | 4 |
| Calcium Signaling and Ion Homeostasis | 8 | 7% | 4 |
| Mesenchymal Differentiation and Epithelial-Mesenchymal Transition | 11 | 9% | 3 |
| Hypoxia Response and Metabolic Adaptation | 5 | 4% | 3 |
| Immune Modulation and Inflammatory Signaling | 8 | 7% | 2 |
| Epithelial-Mesenchymal Transition | 18 | 15% | 3 |
| Calcium-Mediated Proliferation and Survival | 13 | 11% | 2 |
| Glioma Stem Cell Maintenance | 11 | 9% | 2 |
| Integrin-Mediated Cell Invasion | 11 | 9% | 2 |
| Extracellular Matrix Remodeling | 11 | 9% | 2 |
| Receptor Tyrosine Kinase Signaling | 11 | 9% | 2 |
| Immune Microenvironment Modulation | 5 | 4% | 2 |
| Cuproptosis and Metabolic Reprogramming | 1 | 1% | 1 |
| Tetraspanin-Mediated Cell Adhesion | 1 | 1% | 1 |
| Transcriptional Regulation of Differentiation | 2 | 2% | 1 |

</details>

#### Runs

- **20251126_144326**: [deepsearch_container.md](10_AC_gliosis_like_2/20251126_144326/deepsearch_container.md) | [deepsearch_structured.json](10_AC_gliosis_like_2/20251126_144326/deepsearch_structured.json)
- **20251126_132637**: [deepsearch_container.md](10_AC_gliosis_like_2/20251126_132637/deepsearch_container.md) | [deepsearch_structured.json](10_AC_gliosis_like_2/20251126_132637/deepsearch_structured.json)

### 11_OPC_like_1

**Context**: malignant glioblastoma cells

**Genes**: 109 total, 82 covered by programs (75%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Oligodendrocyte differentiation and myelin formation | 10 | 9% | 6 |
| Notch signaling and neural stem cell maintenance | 3 | 3% | 6 |
| Synaptic adhesion and neuronal crosstalk | 9 | 8% | 5 |
| Ion homeostasis and osmotic cell volume regulation | 8 | 7% | 4 |
| Cell cycle progression and proliferation | 2 | 2% | 2 |
| Extracellular matrix remodeling and vasculature assembly | 8 | 7% | 4 |
| Integrin-mediated cell adhesion and migration | 3 | 3% | 3 |
| Lipid metabolism and myelin-derived nutrient scavenging | 6 | 6% | 1 |
| Growth factor receptor signaling networks | 4 | 4% | 4 |
| Lin28-let-7 axis regulating stemness and differentiation | 1 | 1% | 2 |
| Developmental transcriptional regulation and cell fate specification | 2 | 2% | 5 |
| Extracellular Matrix Remodeling and Cell Adhesion | 16 | 15% | 3 |
| Ion Channel-Mediated Cell Motility | 9 | 8% | 2 |
| Oligodendrocyte Lineage Progenitor Identity | 7 | 6% | 3 |
| Notch Signaling and Stem Cell Maintenance | 5 | 5% | 2 |
| Lipid Metabolism and Sphingolipid Remodeling | 10 | 9% | 3 |
| Cell Migration and Invasion Machinery | 11 | 10% | 3 |
| Growth Factor Receptor Signaling and Proliferation | 8 | 7% | 3 |
| Mesenchymal Transition and Invasion Program | 8 | 7% | 3 |
| Mitochondrial Dynamics and Cellular Metabolism | 5 | 5% | 2 |
| Proteolytic Processing and Proteasomal Activity | 3 | 3% | 2 |
| Signal Transduction Modulation and cAMP/Calcium Signaling | 5 | 5% | 1 |
| Endosomal Recycling and Receptor Trafficking | 2 | 2% | 1 |

</details>

#### Runs

- **20251126_144843**: [deepsearch_container.md](11_OPC_like_1/20251126_144843/deepsearch_container.md) | [deepsearch_structured.json](11_OPC_like_1/20251126_144843/deepsearch_structured.json)
- **20251126_133059**: [deepsearch_container.md](11_OPC_like_1/20251126_133059/deepsearch_container.md) | [deepsearch_structured.json](11_OPC_like_1/20251126_133059/deepsearch_structured.json)

### 12_NPC_neuronal_like_3

**Context**: malignant glioblastoma cells

**Genes**: 159 total, 112 covered by programs (70%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Terminal Neuronal Differentiation Blockade | 14 | 9% | 4 |
| GABAergic Synaptic Tumor Promotion | 10 | 6% | 2 |
| Axon Guidance & Cell Adhesion Dysregulation | 14 | 9% | 4 |
| Vascular Growth Factor Signaling & Angiogenesis | 4 | 3% | 2 |
| Ion Channel & Electrolyte Homeostasis Dysregulation | 5 | 3% | 3 |
| Synaptic Plasticity & Dendritic Maturation | 11 | 7% | 3 |
| Axonal Maintenance & Cytoskeletal Integrity | 7 | 4% | 2 |
| Apoptosis Resistance & Cell Survival Pathways | 4 | 3% | 3 |
| Retinoic Acid & MAPK-CaMKII Signaling Integration | 1 | 1% | 1 |
| Metabolic Reprogramming & Warburg Effect Activation | 8 | 5% | 2 |
| Extracellular Matrix Remodeling & Cell Migration | 12 | 8% | 2 |
| G-Protein-Coupled Receptor & Neuroendocrine Signaling | 3 | 2% | 1 |
| Glutamate-calcium excitatory signaling | 12 | 8% | 4 |
| Neuronal differentiation transcription factor cascade | 10 | 6% | 4 |
| Axon guidance and cell adhesion | 16 | 10% | 5 |
| GABAergic inhibitory neurotransmission | 5 | 3% | 4 |
| Synaptic proteins and cytoskeletal dynamics | 6 | 4% | 2 |
| Thrombospondin-mediated synaptogenesis and immune regulation | 0 | 0% | 1 |
| Neuronal activity-sensing signaling cascade | 2 | 1% | 2 |
| Neurofibromatosis and growth factor signaling | 3 | 2% | 3 |
| Long non-coding RNA and RNA processing | 24 | 15% | 1 |
| Apoptosis regulation and cell death | 2 | 1% | 1 |

</details>

#### Runs

- **20251126_145428**: [deepsearch_container.md](12_NPC_neuronal_like_3/20251126_145428/deepsearch_container.md) | [deepsearch_structured.json](12_NPC_neuronal_like_3/20251126_145428/deepsearch_structured.json)
- **20251126_133359**: [deepsearch_container.md](12_NPC_neuronal_like_3/20251126_133359/deepsearch_container.md) | [deepsearch_structured.json](12_NPC_neuronal_like_3/20251126_133359/deepsearch_structured.json)

### 1_OPC_AC_like_1

**Context**: malignant glioblastoma cells

**Genes**: 55 total, 48 covered by programs (87%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| CD44-mediated Invasive Adhesion | 2 | 4% | 3 |
| Integrin-mediated Migration and EMT | 1 | 2% | 2 |
| N-cadherin-dependent Context-specific Migration | 1 | 2% | 1 |
| Extracellular Matrix Remodeling | 3 | 5% | 4 |
| Metabolic Reprogramming and Redox Homeostasis | 3 | 5% | 3 |
| Immune Evasion and Checkpoint Regulation | 3 | 5% | 3 |
| Ganglioside and Glycosylation-based Signaling | 4 | 7% | 3 |
| Neural-like Developmental Signaling | 5 | 9% | 4 |
| GFAP Isoform-dependent Malignancy | 1 | 2% | 2 |
| Long Non-Coding RNA Regulatory Networks | 18 | 33% | 3 |
| PI3K/AKT Signaling Modulation | 1 | 2% | 2 |
| Calcium-dependent Cell Adhesion | 2 | 4% | 1 |
| Transcriptional Co-regulator Activity | 1 | 2% | 1 |
| Heparan Sulfate Proteoglycan Signaling | 1 | 2% | 2 |
| Histamine Receptor Signaling | 1 | 2% | 1 |
| Extracellular Matrix Remodeling and Invasion | 10 | 18% | 8 |
| Cell-Cell Adhesion and Migration Plasticity | 5 | 9% | 3 |
| Ferroptosis Suppression and Redox Defense | 2 | 4% | 4 |
| Immune Evasion Through Glycosylation | 4 | 7% | 2 |
| Metabolic Reprogramming for Proliferation | 2 | 4% | 4 |
| Tumor Microenvironment Immune Regulation | 4 | 7% | 4 |
| Neural Guidance Cues and Developmental Plasticity | 6 | 11% | 5 |
| Transcriptional and Epigenetic Plasticity Control | 2 | 4% | 3 |
| Cytoskeletal Dynamics and Cell Motility | 4 | 7% | 3 |
| Signaling Pathway Integration and Crosstalk | 3 | 5% | 5 |

</details>

#### Runs

- **20251126_140224**: [deepsearch_container.md](1_OPC_AC_like_1/20251126_140224/deepsearch_container.md) | [deepsearch_structured.json](1_OPC_AC_like_1/20251126_140224/deepsearch_structured.json)
- **20251126_125736**: [deepsearch_container.md](1_OPC_AC_like_1/20251126_125736/deepsearch_container.md) | [deepsearch_structured.json](1_OPC_AC_like_1/20251126_125736/deepsearch_structured.json)

### 2_NPC_neuronal_like_1

**Context**: malignant glioblastoma cells

**Genes**: 94 total, 48 covered by programs (51%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Ciliary Dysfunction and Motility Defects | 16 | 17% | 4 |
| IL-6-Mediated Immunosuppression | 4 | 4% | 4 |
| Tumor-Suppressive Chromatin Remodeling | 2 | 2% | 3 |
| Extracellular Matrix Remodeling and Invasion | 7 | 7% | 6 |
| Metabolic Reprogramming and Energy Homeostasis | 6 | 6% | 5 |
| Neurotransmitter Signaling and Synaptic Communication | 3 | 3% | 3 |
| BMP-Mediated Developmental Signaling | 1 | 1% | 2 |
| Motile Cilia-Axoneme Assembly Dysregulation | 19 | 20% | 7 |
| Extracellular Matrix Remodeling and Stiffness | 7 | 7% | 5 |
| GABAergic Neuron-to-Glioma Synaptic Communication | 8 | 9% | 5 |
| Glioma Stem Cell Self-Renewal and Differentiation | 6 | 6% | 5 |
| Immune Evasion and T-Cell Exhaustion | 3 | 3% | 7 |
| Calcium Signaling and Neuronal Activity Coupling | 3 | 3% | 4 |
| Cell Adhesion Molecule-Mediated Neural Development and Migration | 3 | 3% | 5 |
| Metabolic Adaptation and Nutrient Uptake | 3 | 3% | 2 |

</details>

#### Runs

- **20251126_140831**: [deepsearch_container.md](2_NPC_neuronal_like_1/20251126_140831/deepsearch_container.md) | [deepsearch_structured.json](2_NPC_neuronal_like_1/20251126_140831/deepsearch_structured.json)
- **20251126_130034**: [deepsearch_container.md](2_NPC_neuronal_like_1/20251126_130034/deepsearch_container.md) | [deepsearch_structured.json](2_NPC_neuronal_like_1/20251126_130034/deepsearch_structured.json)

### 3_NPC_neuronal_like_2

**Context**: malignant glioblastoma cells

**Genes**: 136 total, 82 covered by programs (60%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Extracellular Matrix Remodeling and Invasion | 14 | 10% | 5 |
| Cell Adhesion and Synaptic-Like Junctions | 10 | 7% | 6 |
| Growth Factor Receptor Signaling | 5 | 4% | 4 |
| Ion Channel-Mediated Cellular Signaling | 16 | 12% | 4 |
| Axon Guidance and Repulsive Signaling | 9 | 7% | 4 |
| RNA Binding and Post-transcriptional Regulation | 3 | 2% | 5 |
| Transcriptional Control of Neural Differentiation | 6 | 4% | 2 |
| Glioma Stem Cell Maintenance and Stemness | 15 | 11% | 3 |
| Spatial Gene Expression Heterogeneity | 12 | 9% | 3 |
| Metabolic Reprogramming and Lipid Synthesis | 4 | 3% | 3 |
| Extracellular Matrix Remodeling | 15 | 11% | 5 |
| Cadherin-Mediated Cell Adhesion | 6 | 4% | 3 |
| Calcium Signaling Through Ion Channels | 9 | 7% | 5 |
| Synaptic Development and Adhesion | 9 | 7% | 4 |
| Receptor Tyrosine Kinase Signaling | 5 | 4% | 4 |
| Transcriptional Repression of Neural Differentiation | 8 | 6% | 4 |
| Neuropeptide and Neurosecretion Pathways | 5 | 4% | 3 |
| Cyclic Nucleotide Signaling and Cell Motility | 4 | 3% | 2 |
| RNA-Binding and Post-Transcriptional Control | 12 | 9% | 2 |

</details>

#### Runs

- **20251126_141307**: [deepsearch_container.md](3_NPC_neuronal_like_2/20251126_141307/deepsearch_container.md) | [deepsearch_structured.json](3_NPC_neuronal_like_2/20251126_141307/deepsearch_structured.json)
- **20251126_130035**: [deepsearch_container.md](3_NPC_neuronal_like_2/20251126_130035/deepsearch_container.md) | [deepsearch_structured.json](3_NPC_neuronal_like_2/20251126_130035/deepsearch_structured.json)

### 4_AC_gliosis_like_1

**Context**: malignant glioblastoma cells

**Genes**: 99 total, 30 covered by programs (30%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Aquaporin-mediated osmotic water transport and migration | 5 | 5% | 3 |
| Aerobic glycolysis-dependent nutrient acquisition | 2 | 2% | 3 |
| Extracellular matrix remodeling and invasive phenotype | 9 | 9% | 4 |
| Complement system activation and immune modulation | 6 | 6% | 4 |
| Glioma stem cell self-renewal and maintenance | 8 | 8% | 3 |
| Tumor-associated astrocyte and glial cell reprogramming | 4 | 4% | 3 |
| Gap junction communication and chemoresistance | 2 | 2% | 2 |
| Pericyte recruitment and vascular stability | 1 | 1% | 1 |
| Immune cell infiltration and M2 macrophage polarization | 5 | 5% | 4 |
| Metabolic reprogramming and hypoxia adaptation | 4 | 4% | 3 |

</details>

#### Runs

- **20251126_141722**: [deepsearch_container.md](4_AC_gliosis_like_1/20251126_141722/deepsearch_container.md) | [deepsearch_structured.json](4_AC_gliosis_like_1/20251126_141722/deepsearch_structured.json)

### 5_AC_neuronal_like

**Context**: malignant glioblastoma cells

**Genes**: 373 total, 102 covered by programs (27%)

#### Details

<details>
<summary>Gene Programs</summary>

| Program Name | Genes | % of Total | Citations |
|---|---|---|---|
| Immune Checkpoint Signaling | 6 | 2% | 4 |
| Receptor Tyrosine Kinase Signaling | 5 | 1% | 3 |
| Synaptic Adhesion and Neuronal Communication | 10 | 3% | 4 |
| Ion Channel Dysregulation and Excitotoxicity | 9 | 2% | 4 |
| Extracellular Matrix Remodeling and Invasion | 9 | 2% | 3 |
| Angiogenesis and Vascular Development | 3 | 1% | 3 |
| Wnt/β-Catenin Self-Renewal Signaling | 1 | 0% | 2 |
| Epithelial-Mesenchymal Transition and Invasion | 2 | 1% | 3 |
| Hypoxia-Responsive Transcription | 5 | 1% | 2 |
| Lipid Metabolism and Signaling | 3 | 1% | 2 |
| Tumor-Associated Macrophage Polarization | 6 | 2% | 4 |
| GTPase Activation and Cytoskeletal Remodeling | 6 | 2% | 2 |
| Calcium-mediated cell migration | 9 | 2% | 6 |
| Extracellular matrix degradation and invasion | 10 | 3% | 4 |
| Cell adhesion and synaptic protein scaffolding | 9 | 2% | 6 |
| Tumor-associated macrophage polarization and immune suppression | 11 | 3% | 7 |
| Wnt/β-catenin pathway and stemness maintenance | 5 | 1% | 5 |
| Cholinergic immune modulation | 1 | 0% | 2 |
| DOCK protein-mediated immune synapse formation | 3 | 1% | 2 |
| Long non-coding RNA regulation of GBM processes | 38 | 10% | 2 |
| Neuron-glioma synaptic plasticity | 4 | 1% | 4 |
| Scavenger receptor and pattern recognition signaling | 5 | 1% | 4 |

</details>

#### Runs

- **20251126_142015**: [deepsearch_container.md](5_AC_neuronal_like/20251126_142015/deepsearch_container.md) | [deepsearch_structured.json](5_AC_neuronal_like/20251126_142015/deepsearch_structured.json)
- **20251126_130844**: [deepsearch_container.md](5_AC_neuronal_like/20251126_130844/deepsearch_container.md) | [deepsearch_structured.json](5_AC_neuronal_like/20251126_130844/deepsearch_structured.json)
