# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: glioblastoma multiforme (GBM)
- Tissue: brain

## Input Genes
SERPINE1, EMP1, SPOCD1, ARHGAP29, IL1R1, COL6A2, MYOF, F13A1, CXCL10, CHI3L1, MET, IL6, SAA2, BIRC3, MCTP2, ANGPTL4, ICAM1, CCN1, CAV1, APLN, FOSL1, SNTG2-AS1, TPD52L1, SAA4, KRT75, ... (111 total)

## Program: EMT-Driven Invasive Dispersal
Epithelial-mesenchymal transition program enabling glioblastoma cells to escape the tumor core and infiltrate adjacent brain tissue. SERPINE1 and EMP1 regulate cell adhesion dynamics and directional migration through extracellular matrix interactions. FOSL1 maintains mesenchymal transcriptional identity, while HMGA2 sustains glioma-initiating cell properties required for sustained invasion. COL5A1 and FN1 remodel the extracellular matrix to facilitate cell movement.

**Predicted impacts**
- Enhanced directional cell migration through ECM with reduced dependence on focal adhesion stabilization
- Increased invasive capacity into surrounding brain parenchyma
- Sustained mesenchymal phenotype independent of differentiation signals
- Resistance to anoikis upon ECM detachment
- Enhanced self-renewal of glioma-initiating cell populations

**Evidence summary**
Multiple genes in this program are specifically upregulated in dispersive GBM cells within spheroid models and show enrichment in mesenchymal GBM subtypes associated with poor prognosis. SERPINE1 expression correlates with poor survival in TCGA cohorts (p=0.00014), and knockdown significantly reduces tumor growth and invasion in vivo. EMP1 knockdown decreases both tumor growth and survival in xenograft models. HMGA2 is required for glioma-initiating cell self-renewal and tumorigenicity. FOSL1 is identified as a master regulator of mesenchymal phenotype in NF1-mutant contexts. These genes collectively enable the core invasive phenotype of malignant glioblastoma.

**Atomic biological processes**
- Cell adhesion-mediated migration. Genes: SERPINE1, EMP1, FN1, COL5A1
  - [1]: SERPINE1 regulates cell adhesion to vitronectin and affects focal adhesion formation and directionality of cell movement
  - [2]: EMP1 knockdown inhibits GBM cell migration and invasion through regulation of cell-cell and cell-matrix adhesion
  - [11]: Fibronectin and vitronectin promote cell adhesion-mediated drug resistance through integrin αv signaling
- Extracellular matrix proteolysis and remodeling. Genes: COL5A1, FN1, SMOC2
  - [9]: COL5A1 regulates GBM cell migration and invasion through ECM remodeling and actin filament regulation
  - [12]: Collagen genes regulate the immunosuppressive microenvironment and EMT process of glioma through ECM remodeling
- Mesenchymal transcriptional programming. Genes: FOSL1, HMGA2
  - [38]: FOSL1 controls GBM plasticity and aggressiveness through AP-1 transcription factor regulation of mesenchymal gene expression
  - [41]: FOSL1 maintains mesenchymal identity and stem cell properties in glioblastoma through chromatin accessibility at mesenchymal genes
  - [33]: HMGA2 is highly expressed in mesenchymal GBMs and labels glioma-initiating cells

**Atomic cellular components**
- Focal adhesion complexes. Genes: SERPINE1, EMP1, FN1
  - [1]: SERPINE1 affects the number of focal adhesions and directionality of cell movement on ECM proteins
  - [8]: Integrin-FAK-paxillin-AKT signaling pathway in focal adhesions mediates GBM cell proliferation and survival

**Required genes (not in input)**
- Genes: ITGA5, ITGA3, ITGAV, FAK, FOXM1, PLAU, SOX2, NESTIN
  - [8]: Integrins α5β1 and αvβ1 serve as receptors for FN1 and vitronectin, essential for GBM invasion
  - [36]: FOXM1 and PLAU are downstream targets of HMGA2 required for GBM propagation and aggressiveness

**Program citations**
- [1]: SERPINE1 identified as modulator of GBM cell dispersal with strong prognostic correlation
- [2]: EMP1 as novel independent predictor of poor prognosis in GBM
- [9]: COL5A1-PPRC1-ESM1 axis represents novel therapeutic target for malignant GBM
- [33]: HMGA2 promotes stemness and invasiveness in glioma-initiating cells
- [38]: FOSL1 controls GBM plasticity and aggressiveness in response to NF1 alterations

## Program: Tryptophan-Pathway Immune Evasion
Comprehensive immune suppression program centered on activation of the kynurenine pathway. IDO1 and TDO2 catalyze tryptophan degradation, producing immunosuppressive kynurenine metabolites that promote regulatory T cell expansion and cytotoxic T cell apoptosis. CHI3L1 (YKL-40) upregulates IDO1/TDO2 expression and coordinates with kynurenine to inhibit anti-tumor immunity. This program operates in coordination with IL-6 and IL-1β signaling to establish a profoundly immunosuppressive microenvironment.

**Predicted impacts**
- Profound local tryptophan depletion creating selective pressure on tryptophan-dependent immune cells
- Expansion of immunosuppressive regulatory T cell populations
- Functional exhaustion and apoptosis of CD8+ cytotoxic T cells
- Reprogramming of infiltrating macrophages toward immunosuppressive phenotypes
- Recruitment of myeloid-derived suppressor cells through coordinated IDO1-AhR signaling
- Resistance to PD-1/PD-L1 checkpoint blockade through metabolic immune suppression

**Evidence summary**
IDO1 expression is significantly associated with poor overall survival in GBM patients (well-established). CHI3L1 (YKL-40) is a mesenchymal marker highly expressed in aggressive GBMs and shows positive correlation with IDO1 expression. Recent evidence demonstrates that CHI3L1 coordinates with kynurenine pathway to establish immunosuppressive microenvironment. Multiple studies show IDO1/TDO2-mediated tryptophan metabolism is a primary driver of GBM immune evasion, particularly resistant to checkpoint inhibitor monotherapy. SERPINE1 mRNA additionally contributes through direct inverse correlation with CD8+ T cell infiltration, suggesting multiple synergistic immunosuppressive mechanisms.

**Atomic biological processes**
- Tryptophan catabolism and kynurenine production. Genes: IDO1, CHI3L1
  - [23]: IDO1 catalyzes oxidation of tryptophan, depletes this essential amino acid, and generates immunosuppressive kynurenine metabolites that promote Treg expansion and CTL apoptosis
  - [32]: YKL-40 (CHI3L1) upregulates IDO1 or TDO2 to activate kynurenine pathway metabolism in GBM, coordinating with kynurenine to establish inhibitory tumor immune microenvironment
  - [20]: TDO2 in myeloid cells mediates immunosuppression through tryptophan degradation and AhR activation in IDH-mutant gliomas
- Aryl hydrocarbon receptor signaling. Genes: CHI3L1, IDO1
  - [32]: CHI3L1 regulates AhR to govern expression of IDO1 in glioma cells, where AhR is a key regulator of immunosuppressive macrophage programming
  - [20]: Kynurenine activates AhR in immune cells to suppress anti-tumor immune responses through multiple mechanisms
- Regulatory T cell expansion and CD8 T cell suppression. Genes: IDO1, CHI3L1, SERPINE1
  - [23]: IDO1 activity increases immunosuppressive regulatory T cell differentiation from naïve T cells and increases apoptosis of cytotoxic T lymphocytes
  - [4]: SERPINE1 mRNA expression inversely correlates with CD8+ T cell infiltration in diverse cancer types including GBM
  - [20]: Macrophage tryptophan deprivation specifically activates GCN2 in dendritic cells to block T cell proliferation

**Atomic cellular components**
- Kynurenine metabolite production. Genes: IDO1, CHI3L1
  - [23]: Conversion of tryptophan into kynurenines through IDO1-catalyzed oxidation represents major immunomodulatory function

**Required genes (not in input)**
- Genes: TDO2, AhR, GCN2, FOXP3, LAT1, CD98
  - [23]: TDO2 co-expresses with IDO1 in GBM and contributes to tryptophan catabolism
  - [32]: AhR and FOXP3 are critical downstream effectors of CHI3L1-mediated immunosuppression
  - [20]: LAT1-CD98 transporter regulates tryptophan uptake necessary for metabolic immune suppression

**Program citations**
- [23]: Comprehensive review of IDO1 role in GBM immunological escape via tryptophan metabolism
- [32]: YKL-40 upregulates kynurenine pathway to establish inhibitory immune microenvironment
- [20]: Mechanistic evidence of TDO2-mediated immunosuppression in IDH-mutant gliomas
- [4]: SERPINE1 mRNA negatively correlates with CD8+ T cell infiltration in GBM

## Program: IL-6/IL-1β-NF-κB/STAT3 Signaling Axis
Central pro-inflammatory yet immunosuppressive signaling loop driven by IL-6 and IL-1β cytokines. TNF-α activation of NF-κB induces IL-6 expression, which in turn activates STAT3 signaling. This creates a self-reinforcing autocrine loop that drives tumor cell proliferation, survival, and chemoresistance while simultaneously establishing an immunosuppressive microenvironment through recruitment of myeloid cells. TNFAIP2 and TNFAIP3 are downstream targets that modulate the intensity of this inflammatory response.

**Predicted impacts**
- Enhanced tumor cell proliferation through NF-κB-driven cyclin D1 expression
- Increased chemotherapy resistance through upregulation of anti-apoptotic proteins
- Sustained STAT3 activation creating feed-forward signaling loop
- Recruitment and polarization of tumor-associated macrophages toward immunosuppressive M2 phenotype
- Increased vascular permeability and endothelial cell migration promoting angiogenesis
- Elevated production of additional immunosuppressive cytokines creating cytokine storm

**Evidence summary**
The IL-6/NF-κB/STAT3 axis is one of the most thoroughly characterized pro-tumorigenic signaling circuits in GBM. IL-6 overexpression correlates with diminished patient survival. TNF-α-induced NF-κB activation is mechanistically sufficient to drive IL-6 production and subsequent STAT3 activation in multiple GBM cell lines and patient-derived xenografts. Combined inhibition of NF-κB and STAT3 significantly increases survival in orthotopic mouse models. IL-1β signaling similarly drives IL-6 production through NF-κB and ERK1/2 phosphorylation. TNFAIP genes serve as downstream targets that regulate intensity of this inflammatory response.

**Atomic biological processes**
- NF-κB canonical activation and IL-6 induction. Genes: IL6, TNFAIP3, TNFAIP2
  - [50]: TNF-α-induced NF-κB activation is sufficient to induce IL-6 expression and activate STAT3 in GBM cells
  - [28]: NF-κB is classically considered pro-survival factor inducing IL-6 and other survival genes in GBM
- STAT3 activation via IL-6 receptor signaling. Genes: IL6, IL1R1
  - [50]: IL-6 directly activates STAT3 through IL-6R/gp130 signaling, with STAT3 also recruited to IL-6 promoter creating positive feedback loop
  - [10]: IL-6 trans-signaling induces pro-inflammatory response while classical signaling induces anti-inflammatory response in GBM context
- Myeloid cell recruitment and polarization. Genes: IL6, IL1R1, CXCL2, CXCL8
  - [10]: IL-6 and IL-1β recruit neutrophils and monocytes to inflammatory sites and induce expression of adhesion molecules on endothelial cells
  - [13]: CXCL2 and IL-8 are angiogenic factors that increase proliferation and migration through CXCR2 signaling
- Tumor cell survival and resistance to therapy. Genes: IL6, TNFAIP3, TNFAIP2
  - [25]: Sustained NF-κB activation driven by TNFα and IL-6 creates autocrine/paracrine stimulation promoting cancer stem cell phenotype
  - [28]: NF-κB induces expression of anti-apoptotic genes including Bcl-2, Bcl-xL, survivin, and IAPs that promote chemoresistance

**Atomic cellular components**
- IL-6 receptor/gp130 complex and downstream signaling. Genes: IL6, IL1R1
  - [10]: IL-6R expressed on leukocytes and hepatocytes, gp130 expressed on all nucleated cells, allowing both cell-autonomous and paracrine IL-6 effects

**Required genes (not in input)**
- Genes: TNF, TNFR1, IL6R, GP130, JAK1, JAK2, STAT3, IKK complex, SOCS3
  - [50]: TNF, TNFR1, and IKK complex are essential upstream activators of NF-κB pathway in GBM
  - [10]: IL6R, GP130, JAK proteins, and STAT3 are required for IL-6 receptor signaling

**Program citations**
- [50]: TNF-α-NF-κB-IL-6-STAT3 signaling crosstalk is central to GBM aggressiveness
- [10]: IL-6 and IL-1β are fundamental in GBM immune evasion and progression
- [28]: NF-κB modulates multiple hallmarks of cancer including proliferation, angiogenesis, invasion, and apoptosis resistance
- [25]: TNF-α-NF-κB-IL-6 loop sustains cancer stemness and therapeutic resistance

## Program: VEGFA-Driven Tumor Angiogenesis
Hypoxia-driven pro-angiogenic program centered on VEGFA expression and signaling. VEGFA stimulates endothelial cell proliferation, migration, and tube formation, providing essential nutrient and oxygen supply to growing tumors. Cooperating factors including CXCL2, CXCL8, and ANGPTL4 enhance angiogenic responses. CAV1 (caveolin-1) regulates endothelial cell function in tumor vasculature. This program is essential for tumor growth beyond hypoxic diffusion limits and is associated with poor prognosis.

**Predicted impacts**
- Enhanced endothelial cell proliferation and migration toward hypoxic tumor regions
- Formation of new tumor vasculature enabling exponential tumor growth
- Increased vascular permeability and disrupted blood-brain barrier integrity
- Selective recruitment of immunosuppressive myeloid cells while excluding CD8+ T cells
- Metabolic reprogramming of endothelial cells toward glycolytic phenotype to support tumor-promoting endothelium
- Poor prognosis associated with high VEGFA expression

**Evidence summary**
VEGFA is significantly upregulated in GBM patient samples and cell lines and correlates with poor overall survival. GBM is characterized by high degree of angiogenesis facilitated by hypoxia-inducible factor 1α-driven VEGFA expression. CXCL2 and IL-8 demonstrate angiogenic capacity in both peripheral and brain-specific endothelial cells, with CXCR2 antagonist treatment reducing endothelial sprouting. ANGPTL4 emerges as multi-functional angiogenesis promoter. CAV1-mediated endothelial metabolic reprogramming supports tumor vascular phenotype. Multiple studies confirm that targeting VEGF pathway components offers therapeutic benefit.

**Atomic biological processes**
- VEGFA-mediated endothelial cell proliferation and migration. Genes: VEGFA, CXCL2, CXCL8
  - [19]: VEGFA is upregulated in glioblastoma and stimulates endothelial cell proliferation and migration, essential for angiogenesis
  - [13]: CXCL2 shows angiogenic capacity affecting human endothelial cell sprouting and migration through CXCR2 signaling
  - [22]: GBM cell-derived EVs containing VEGF-A trigger angiogenic properties in endothelial cells
- Hypoxia-inducible factor-mediated angiogenesis. Genes: VEGFA
  - [19]: Glioblastoma overexpresses VEGF through hypoxia-inducible factor 1α, promoting vascular growth and tumor proliferation
- Endothelial cell metabolic reprogramming. Genes: VEGFA, ANGPTL4, CAV1
  - [34]: Angiogenic factors like VEGFA drive glycolytic phenotype in tumor endothelial cells, supporting tip cell differentiation
  - [34]: EC-derived ANGPTL4 maintains glycolytic phenotype while inhibiting lipoprotein lipase, affecting FA transport
- Vascular permeability and immune cell recruitment. Genes: VEGFA, CXCL2, CXCL8, ICAM1
  - [13]: VEGFA and CXCL2/IL-8 increase vascular permeability and promote leukocyte extravasation through upregulation of adhesion molecules

**Atomic cellular components**
- VEGF receptor signaling complex. Genes: VEGFA
  - [19]: VEGFR2 is highly accountable for downstream angiogenic properties of VEGF
- Endothelial cell junction and adhesion molecules. Genes: VEGFA, ICAM1
  - [34]: VEGFA and other immunosuppressive factors reduce expression of adhesion molecules on endothelial cells, compromising immune cell transmigration

**Required genes (not in input)**
- Genes: VEGFR2, HIF1A, FGFR1, Notch1, PHGDH, CD36
  - [19]: VEGFR2 is essential for VEGFA-mediated angiogenic signaling
  - [34]: HIF1A, PHGDH, and CD36 are required for endothelial metabolic reprogramming supporting angiogenesis

**Program citations**
- [19]: FN1 and VEGFA are potential therapeutic targets in GBM with strong prognostic association
- [13]: CXCL2/IL8/CXCR2 pathway is relevant for brain tumor malignancy and endothelial cell function
- [34]: EC-derived ANGPTL4 promotes tumor angiogenesis through metabolic reprogramming

## Program: MET-Driven Stemness and Invasiveness
Receptor tyrosine kinase signaling centered on MET activation, a critical driver of glioma stem cell self-renewal, invasiveness, and tumorigenicity. Recent evidence identifies a circular MET RNA (circMET) encoding MET404 variant that forms constitutively active receptor independent of ligand (HGF) stimulation. MET signaling promotes proliferation, survival, and migration while maintaining stem cell features. High MET404 expression predicts poor prognosis. This program is particularly important in primary GBMs with MET amplification or fusion events.

**Predicted impacts**
- Enhanced glioma stem cell self-renewal independent of exogenous HGF stimulation
- Increased tumor growth rate particularly in xenograft models
- Enhanced invasion and migration through AKT/ERK signaling
- Resistance to conventional MET inhibitors due to ligand-independent activation
- Poor prognostic outcome with high MET404 expression
- Synergistic therapeutic response to combination of MET inhibitors targeting different MET isoforms

**Evidence summary**
MET aberrations in GBM include focal amplification, chromosomal rearrangements creating gene fusions (including PTPRZ1-MET and CLIP2-MET), and the newly characterized circMET encoding MET404. CircMET/MET404 is identified as a major MET activator in glioma stem cells and predicts poor overall survival. High MET404 expression correlates with increased p-MET levels better than MET receptor expression alone. Combination of onartuzumab (MET inhibitor) and MET404-targeting antibody achieves maximal inhibition of MET signaling and prolongs mouse survival. MET targeting is validated across multiple preclinical and early clinical studies.

**Atomic biological processes**
- Ligand-independent MET activation. Genes: MET
  - [14]: CircMET encodes MET404 variant that directly interacts with MET β subunit to form constitutively activated receptor independent of HGF stimulation
  - [17]: MET overexpression contributes to chemotherapy resistance and promotes survival of cancer stem-like cells
- MET-AKT-ERK signaling cascade. Genes: MET
  - [14]: MET404 activation leads to AKT/ERK phosphorylation and activation of downstream effectors driving tumor progression
  - [17]: MET signaling activates mitogen-activated protein kinase pathway associated with aggressive glial tumors
- Glioma stem cell self-renewal. Genes: MET
  - [14]: MET404 expression is markedly higher in glioma stem cells than in differentiated cells, indicating critical role in GSC maintenance
  - [17]: MET signaling is essential for GBM stem cells, with MET inhibition suppressing tumor growth and invasiveness
- Chemotherapy and radiation resistance. Genes: MET
  - [17]: MET activation promotes DNA repair mechanisms and upregulation of survival pathways protecting from cytotoxic therapy

**Atomic cellular components**
- MET404-MET β chimeric receptor complex. Genes: MET
  - [14]: CircMET-encoded MET404 interacts with endogenous MET β subunit to form constitutively active chimeric receptor

**Required genes (not in input)**
- Genes: HGF, AKT, ERK1/2, MAPK, PTEN, PDGFRA
  - [14]: AKT and ERK pathways are essential downstream effectors of MET signaling
  - [17]: Multiple RTKs including EGFR, MET, and PDGFR are coactivated in GBM requiring poly-targeting

**Program citations**
- [14]: CircMET encodes MET404 variant promoting glioblastoma tumorigenesis with synergistic therapeutic potential
- [17]: Comprehensive review of MET receptor signaling aberrations and targeted therapies in GBM

## Program: AXL-Mediated Mesenchymal Programming
TAM receptor family member AXL-driven program promoting mesenchymal phenotype, invasion, metastasis, and immunosuppression. AXL is highly expressed in mesenchymal GBM subtype and activated by PROS1 (protein S) secreted from tumor-associated macrophages/microglia. AXL signaling activates NF-κB pathway promoting tumor growth while modifying immune microenvironment. Elevated AXL expression correlates with poor prognosis and is associated with epithelial-mesenchymal transition, stemness, and acquired therapeutic resistance.

**Predicted impacts**
- Enhanced invasive and migratory phenotype through EMT activation
- Increased stemness and resistance to therapeutic agents
- Sustained NF-κB activation promoting proliferation and survival
- Enhanced recruitment of immunosuppressive myeloid cells
- Increased production of matrix metalloproteinases and metastasis-associated genes
- Poor prognostic outcome associated with high AXL expression

**Evidence summary**
AXL is highly expressed in mesenchymal GBM subtype which corresponds to poor survival and resistant phenotype. AXL is the most highly expressed receptor tyrosine kinase in mesenchymal glioma stem cells compared to proneural cells. PROS1-AXL interactions on mesenchymal cells promote NF-κB-driven survival signals. Treatment with BGB324 (AXL inhibitor) prolongs survival in immunocompromised mice bearing mesenchymal GBM-like tumors. Notably, PD-1 checkpoint blockade increases tumor-associated macrophages and paradoxically enhances AXL activation, suggesting combination strategies may be needed. AXL is identified as potential therapeutic target for GBM particularly in mesenchymal subtype.

**Atomic biological processes**
- PROS1-mediated AXL activation in mesenchymal cells. Genes: AXL
  - [15]: PROS1 secreted by tumor-associated macrophages/microglia physically associates with and activates AXL in mesenchymal GBM cells
  - [18]: AXL is frequently overexpressed in different cancers and plays significant role in various tumor-promoting pathways
- EMT regulation and mesenchymal marker upregulation. Genes: AXL
  - [18]: AXL activation initiates reversible transition from epithelial to mesenchymal phenotype, enhancing cell invasiveness and metastatic potential
  - [18]: Elevated AXL levels are crucial for downregulation of pro-epithelial factors like E-cadherin while upregulating mesenchymal markers like N-cadherin
- NF-κB activation and tumor cell survival. Genes: AXL
  - [15]: PROS1-driven phosphorylation of AXL induces NF-κB activation in mesenchymal GSC
  - [18]: AXL enhances transcriptional expression of EMT regulators through activation of PI3K and NF-κB pathways
- Immune microenvironment remodeling. Genes: AXL
  - [15]: AXL activation promotes CD11b+ macrophage/microglia infiltration into tumors, supporting immunosuppressive microenvironment
  - [18]: AXL promotes immunosuppression, inflammatory responses, and acquired therapeutic resistance in multiple malignancies

**Atomic cellular components**
- AXL receptor and PROS1 ligand complex. Genes: AXL
  - [15]: AXL forms signaling complex with PROS1 ligand secreted from tumor-associated myeloid cells

**Required genes (not in input)**
- Genes: PROS1, GAS6, TYRO3, MERTK, PI3K, NF-κB
  - [15]: PROS1 is primary ligand for AXL in glioma context, while GAS6 is ligand for other TAM receptors
  - [18]: PI3K and NF-κB are essential downstream effectors of AXL signaling

**Program citations**
- [15]: AXL regulates immune microenvironment in glioblastoma through PROS1-dependent pathway
- [18]: Comprehensive review of AXL signaling in cancer including EMT, stemness, and immune modulation

## Program: Apoptosis Evasion and Drug Resistance
Multi-layered anti-apoptotic program centered on Inhibitor of Apoptosis (IAP) proteins BIRC3 and BAG3. BIRC3 (cIAP2) is uniquely prognostic of survival in GBM, with low expression associated with favorable outcomes and high expression correlating with shorter survival. BAG3 maintains HSP70-mediated suppression of BAX translocation to mitochondria, preventing apoptotic signaling. Both proteins are upregulated in response to standard therapy (temozolomide, radiation), contributing to therapeutic resistance. STAT3 and PI3K signaling pathways drive this therapy-induced resistance.

**Predicted impacts**
- Enhanced survival following exposure to DNA damaging chemotherapy
- Reduced apoptosis following ionizing radiation therapy
- Sustained proliferation despite conventional therapeutic insults
- Treatment-induced enrichment of therapy-resistant GBM cell populations
- Shorter overall survival in patients with high BIRC3 expression
- Potential synthetic lethality with dual inhibition of IAPs and complementary pathway components

**Evidence summary**
BIRC3 is the only IAP whose differential expression is significantly associated with long-term survival in GBM patients using TCGA dataset analysis. BIRC3 expression increases with tumor recurrence and is upregulated in response to both temozolomide and radiation. Both STAT3 and PI3K signaling pathways mechanistically drive BIRC3 upregulation in response to therapy. BAG3 is overexpressed in majority of astrocytomas and glioblastomas with expression increasing with tumor grade. BAG3 silencing sensitizes GBM cells to multiple death inducers including chemotherapy. Combined inhibition strategies targeting both NF-κB/STAT3 and IAP family members show promise for overcoming therapeutic resistance.

**Atomic biological processes**
- BIRC3-mediated caspase inhibition. Genes: BIRC3
  - [57]: BIRC3 overexpression suppresses caspase activation in GBM and inhibits apoptosis in response to temozolomide treatment
  - [60]: BIRC3 is unique among IAPs in correlating with shorter survival in both low-grade and high-grade gliomas
- BAG3-HSP70-BAX complex formation. Genes: BAG3
  - [43]: BAG3 promotes binding of HSC/HSP70 to pro-apoptotic BAX, preventing BAX translocation to mitochondria and protecting from apoptosis
  - [43]: BAG3 silencing results in dramatic decrease in cell proliferation and increased caspase-3 activation in GBM cells
- Therapy-induced BIRC3 upregulation. Genes: BIRC3
  - [57]: Irradiation and temozolomide treatment induce BIRC3 expression through STAT3 and PI3K signaling pathways
  - [60]: BIRC3 expression increases in response to standard therapy for GBM, contributing to apoptosis evasion
- NF-κB-mediated anti-apoptotic gene expression. Genes: BIRC3, BAG3
  - [28]: NF-κB induces expression of anti-apoptotic genes including Bcl-2, Bcl-xL, survivin, and IAPs in GBM
  - [25]: Sustained NF-κB activation promotes expression of anti-apoptotic regulators including IAPs

**Atomic cellular components**
- Mitochondrial outer membrane and BAX localization. Genes: BAG3
  - [43]: BAG3-mediated prevention of BAX translocation to mitochondrial membrane prevents mitochondrial depolarization and apoptosis
- Caspase cascade and apoptosome formation. Genes: BIRC3
  - [57]: BIRC3 prevents caspase-3 activation and necrosis in GBM response to chemotherapy

**Required genes (not in input)**
- Genes: BAX, BAD, HSP70, HSC70, Caspase-3, Caspase-9, Bcl-2, Bcl-xL
  - [43]: BAX and BAD are pro-apoptotic BCL2 family members whose function is regulated by BAG3
  - [28]: Anti-apoptotic BCL2 family members and caspases are key targets of NF-κB in GBM

**Program citations**
- [57]: BIRC3 is novel driver of therapeutic resistance in GBM through apoptosis evasion
- [43]: BAG3 is overexpressed in glioblastoma and promotes apoptosis evasion through HSP70-BAX interactions
- [60]: BIRC3 facilitates malignant progression from low-grade to high-grade glioma

## Program: Innate Immune Pattern Recognition
Interferon-mediated innate immune response program centered on toll-like receptor signaling (TLR2) and interferon-stimulated gene expression. TLR2 expressed on glioma-associated microglia rapidly responds to tumor antigens and modulates inflammation-associated immune responses including phagocytosis. TLR2-MHC I axis on microglia contributes to CD8+ T cell proliferation and activation. GBP family proteins (GBP2, GBP5) are downstream effectors of interferon signaling involved in pathogen defense and tumor immunity. MX2 is interferon-induced antiviral protein with emerging roles in tumor immunogenicity.

**Predicted impacts**
- Enhanced innate immune recognition of glioblastoma antigens by resident and infiltrating immune cells
- Increased microglial phagocytosis activity in tumor-bearing brains
- Upregulation of MHC I on antigen-presenting cells supporting CD8+ T cell activation
- Coordinated activation of multiple interferon-responsive genes creating antiviral/anti-tumor state
- Potential for therapeutic enhancement through TLR2 agonists or interferon stimulation
- Complex relationship between interferon responses and immune evasion requiring careful pathway analysis

**Evidence summary**
TLR2 is preferentially expressed on microglia in tumor-bearing brain and is essential for tumor-triggered MHC I upregulation. GBM tissues with high TLR2 level show similar co-occurrence patterns with MHC I molecules in patient samples. CD8+ T cell infiltration correlates with TLR2 level in GBM tissues. GBP family members are interferon-inducible and involved in immune regulation. GBP2 is overexpressed in gliomas relative to normal brain, and knockdown suppresses glioma proliferation and migration through EGFR pathway. GBP5 drives tumor malignancy through multiple signaling pathways and shows prognostic value. MX2 represents interferon-induced protein with anti-viral properties and emerging roles in tumor immunity.

**Atomic biological processes**
- TLR2-mediated innate immune activation. Genes: TLR2
  - [26]: Microglial TLR2 rapidly responds to brain tumor and modulates inflammation-associated immune responses including phagocytosis
  - [29]: TLR2 gene expression is elevated in U87-MG glioblastoma cell line compared to peripheral blood mononuclear cells
- MHC class I upregulation and CD8 T cell cross-priming. Genes: TLR2
  - [26]: TLR2 is essential for tumor-triggered increase of MHC I in microglia, contributing to CD8+ T cell proliferation and activation
- Interferon-stimulated gene expression. Genes: TLR2, GBP2, GBP5, MX2
  - [30]: GBP5 is induced primarily by interferons and exerts diverse effects within tumor microenvironment, modulating host immune responses
  - [27]: GBP2 is highly expressed in glioma tissues and knockdown impairs proliferation and migration of glioma cells
- NF-κB and IRF3 pathway activation. Genes: TLR2, GBP2, GBP5
  - [30]: GBP5 activates NF-κB signaling pathway and interacts with signaling proteins involved in IRF3 activation
  - [29]: TLR signaling leads to NF-κB activation and secretion of pro-inflammatory cytokines through MyD88-dependent pathway

**Atomic cellular components**
- Toll-like receptor 2 signaling complex. Genes: TLR2
  - [26]: TLR2 expressed on microglia forms signaling complex to rapidly sense tumor antigens
- Interferon-induced GTPase family. Genes: GBP2, GBP5, MX2
  - [30]: GBP family consisting of guanylate-binding proteins represents interferon-induced GTPases involved in pathogen defense

**Required genes (not in input)**
- Genes: MyD88, IRAK, TRAF6, TAK1, IRF3, IRF7, STAT1, STAT3, MHC-I, CD8A
  - [26]: MyD88 and downstream kinases are essential for TLR2 signaling to activate NF-κB pathway
  - [30]: IRF family transcription factors and STAT proteins are critical downstream effectors of interferon signaling

**Program citations**
- [26]: Glial TLR2-driven innate immune responses and CD8+ T cell activation critical in brain tumor immunity
- [27]: GBP2 facilitates glioma progression through KIF22 and EGFR signaling pathway
- [30]: GBP5 is promising biomarker and therapeutic target in glioma

## Program: Extracellular Matrix Composition and Immunomodulation
Comprehensive collagen-centered program remodeling the glioma extracellular matrix to establish immunosuppressive microenvironment. Six collagen genes (COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2) collectively regulate immune infiltration and EMT processes. Collagen expression correlates positively with stromal and immune scores but creates immunosuppressive phenotype. SPP1 (osteopontin) participates in ECM remodeling and tumor progression. These genes collectively confer cell adhesion-mediated drug resistance and establish permissive microenvironment for tumor growth.

**Predicted impacts**
- Establishment of dense collagen-rich microenvironment reducing immune cell mobility
- Enhanced integrin-FAK-AKT signaling promoting tumor cell survival and proliferation
- Conferred cell adhesion-mediated drug resistance through ECM interactions
- Paradoxical immune infiltration despite immunosuppressive function of collagen matrix
- Enhanced invasion and EMT through ECM-supported signaling
- Poor prognosis associated with high collagen expression despite immune cell presence
- Potential for matrix-targeting therapies to enhance immunotherapy

**Evidence summary**
Six collagen genes show coordinated upregulation in GBM and correlate with poor overall survival and higher WHO grade. Collagen expression positively correlates with stromal and immune scores but paradoxically associates with immunosuppressive microenvironment. High collagen expression in IDH wildtype patients (compared to IDH mutant) predicts shorter survival. Collagen genes are positively correlated with infiltration of multiple immune cell types but suppress immune function. COL3A1 knockdown significantly inhibits GBM cell migration, invasion, and EMT in vitro. Collagen genes regulate immunosuppressive cytokine production including IL-6. SPP1 (osteopontin) is additionally involved in ECM remodeling and tumor progression. This program represents significant therapeutic target for both inhibiting invasion and enhancing immunotherapy.

**Atomic biological processes**
- Collagen fiber deposition and ECM architecture. Genes: COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2
  - [12]: Six collagen genes (COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2) regulate ECM composition and play important role in immunosuppressive microenvironment of glioma
  - [11]: Laminin, vitronectin, and fibronectin from ECM proteins are abundant in clinical GBM tumors and promote cell adhesion-mediated drug resistance
- Integrin-mediated FAK/AKT signaling. Genes: COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2
  - [11]: ECM proteins including collagen confer CAMDR through integrin αv activation of FAK/paxillin/AKT signaling pathway
  - [12]: Collagen gene expressions positively correlate with integrin-mediated signaling in glioma cells
- Immune cell infiltration and activation. Genes: COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2
  - [12]: Collagen gene expressions correlate with infiltration of B cells, CD8+ T cells, CD4+ T cells, macrophages, neutrophils, and dendritic cells in LGG and GBM
  - [12]: However, high collagen expression shows significantly poor prognosis despite immune infiltration, indicating immunosuppressive nature of collagen-enriched microenvironment
- EMT and invasive phenotype support. Genes: COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2
  - [12]: Collagen genes are significantly involved in EMT process of glioma, with knockdown of COL3A1 suppressing migration, invasion, and EMT process

**Atomic cellular components**
- Fibrillar collagen network. Genes: COL1A1, COL1A2, COL3A1, COL5A2
  - [12]: Collagen genes form fibrillar matrix architecture of glioma tumor microenvironment
- Basement membrane components. Genes: COL4A1, COL4A2
  - [11]: COL4 and laminin are abundant in basement membranes forming blood-brain barrier around tumor vasculature

**Required genes (not in input)**
- Genes: ITGA1, ITGB1, ITGAV, FAK, Paxillin, AKT, IL-6, MMPs
  - [11]: Integrin αv and β1 serve as collagen receptors mediating FAK/AKT signaling
  - [12]: IL-6 is co-expressed with collagen genes in glioma tissue

**Program citations**
- [12]: Collagen genes regulate immunosuppressive microenvironment and EMT process of glioma
- [11]: ECM proteins including collagen confer cell adhesion-mediated drug resistance in GBM
- [9]: COL5A1 plays unique role in GBM invasion and metastasis

## Program: Stemness Maintenance and Self-Renewal
Multi-component program sustaining glioma stem cell (GSC) properties including self-renewal, differentiation capacity, and tumorigenicity. HMGA2 is central transcriptional modulator maintaining GSC propagation and clonogenicity. ANGPTL4 promotes stemness enrichment through EGFR/AKT/4E-BP1 cascade, particularly in temozolomide-resistant populations. PROM1 (CD133) serves as GSC marker. This program is essential for tumor initiation, recurrence following therapy, and resistance to conventional treatments.

**Predicted impacts**
- Enhanced capacity for unlimited self-renewal and differentiation into multiple cell types
- Increased resistance to chemotherapy, radiation, and targeted therapies
- Maintenance of tumor-initiating phenotype despite conventional treatment
- Enhanced invasive capacity and propensity for distant dissemination
- Tumor recurrence following initial therapy response
- Poor prognostic outcome associated with high HMGA2 or ANGPTL4 expression

**Evidence summary**
HMGA2 is highly expressed in majority of primary GBM tumors and is elevated 9.3-fold in CD133+ stem cells compared to CD133- cells. HMGA2 depletion dramatically reduces GBM stemness, invasion, and tumorigenicity. ANGPTL4 is specifically upregulated in GSCs and overexpression induces GSC enrichment even in non-stem populations. ANGPTL4 expression correlates with TMZ resistance through stemness enrichment. Combination of HMGA2 and ANGPTL4 programs is particularly active in mesenchymal GBMs. PROM1 (CD133) serves as reliable marker of stemness and tumorigenicity in GBM populations.

**Atomic biological processes**
- HMGA2-mediated transcriptional control of stemness. Genes: HMGA2
  - [33]: HMGA2 is highly expressed in glioma-initiating cells and is required for their self-renewal and clonogenicity
  - [36]: HMGA2 maintains self-renewal and tumorigenicity of glioma-initiating cells through transcriptional control
- ANGPTL4-EGFR-AKT signaling in GSC enrichment. Genes: ANGPTL4
  - [31]: ANGPTL4 induces GSC enrichment characterized by BMI-1 and SOX2 expression through EGFR/AKT/4E-BP1 cascade, resulting in TMZ resistance
  - [31]: ANGPTL4 secretion upregulated in GSCs and induces spheroid formation and stemness marker expression
- Stem cell marker expression. Genes: HMGA2, PROM1
  - [33]: CD133 expression identifies GBM stem-like cells with enhanced clonogenic potential
  - [36]: SOX2, NESTIN, CD133, and β-catenin are stem-like markers ubiquitously expressed in glioma-initiating cells
- Resistance to chemotherapy. Genes: ANGPTL4, HMGA2
  - [31]: ANGPTL4 mediates TMZ resistance through enrichment of cancer stem cells with enhanced survival capacity

**Atomic cellular components**
- Stemness transcriptional regulatory complexes. Genes: HMGA2
  - [33]: HMGA2 functions as architectural transcription factor through chromatin remodeling and protein-protein interactions

**Required genes (not in input)**
- Genes: SOX2, NESTIN, BMI-1, Sp4, FOXM1, PLAU, β-catenin
  - [33]: SOX2, NESTIN, and β-catenin are downstream targets of HMGA2 in GSC maintenance
  - [31]: Sp4 transcription factor upregulates ANGPTL4 promoter activity in TMZ-resistant GBM

**Program citations**
- [33]: HMGA2 sustains self-renewal and invasiveness of glioma-initiating cells
- [31]: ANGPTL4 induces TMZ resistance of glioblastoma through cancer stemness enrichment
- [36]: HMGA2 maintains self-renewal and tumorigenicity of glioma-initiating cells

## Program: Immune Checkpoint and T Cell Suppression
Program establishing immune checkpoint-mediated suppression of anti-tumor T cell responses. PD-L1 (CD274) is upregulated on GBM cells and tumor-associated myeloid cells, interacting with PD-1 on T cells to inhibit proliferation and promote exhaustion. LIF (leukemia inhibitory factor) contributes to immunosuppressive signaling. SAA1 and SAA2 (serum amyloid A) are acute-phase proteins upregulated in GBM and involved in immune suppression. These factors collectively establish profound resistance to checkpoint blockade immunotherapy.

**Predicted impacts**
- Suppression of effector T cell proliferation and cytokine production
- Promotion of CD8+ T cell exhaustion and functional impairment
- Expansion of immunosuppressive regulatory T cell populations
- Evasion of checkpoint inhibitor monotherapy despite PD-L1/PD-1 blockade
- Poor prognostic outcome associated with high CD274 expression
- Potential for combination strategies targeting multiple checkpoint pathways

**Evidence summary**
CD274 (PD-L1) mRNA expression in GBM correlates positively with FOXP3 (Treg marker), and elevated CD274 predicts worse survival. GBM cell-derived PD-L1+ extracellular vesicles suppress T cell activation through PD-L1-PD-1 interactions. Recombinant PD-L1 significantly increases iTreg populations from activated T cells (p<0.001), and this effect is reversed by nivolumab (anti-PD-1). However, monotherapy with anti-PD-1 has shown limited clinical benefit in GBM patients, suggesting additional immunosuppressive mechanisms. SAA1 and SAA2 are upregulated in GBM and participate in immune modulation through acute-phase response mechanisms.

**Atomic biological processes**
- PD-L1/PD-1 axis-mediated T cell exhaustion. Genes: CD274
  - [39]: PD-L1 (CD274) induces and maintains regulatory T cells in glioblastoma through PD-1 receptor interaction
  - [42]: Plasma PD-L1 is significantly higher in GBM compared to healthy controls and represents promising prognostic marker
- GBM cell-derived extracellular vesicles expressing PD-L1. Genes: CD274
  - [22]: GBM cell-derived EVs express PD-L1 at surface to prevent T cell activation and proliferation, promoting immune evasion
- Regulatory T cell expansion. Genes: CD274
  - [39]: PD-L1 exposure increases inducible Treg (iTreg) populations from activated T cells (18.3% vs 6.5% in activated alone)
- Acute phase response and immune modulation. Genes: SAA1, SAA2
  - [58]: SAA is acute-phase protein upregulated in glioma that modulates invasiveness through integrin signaling

**Atomic cellular components**
- PD-L1/PD-1 receptor-ligand complex. Genes: CD274
  - [39]: CD274 (PD-L1) binds to PD-1 receptor on activated T cells to deliver inhibitory signal

**Required genes (not in input)**
- Genes: PD-1, PDCD1, FOXP3, LAG-3, TIM-3
  - [39]: PD-1 (PDCD1) and FOXP3 are essential for PD-L1-mediated T cell suppression
  - [42]: Multiple checkpoint molecules including LAG-3 and TIM-3 contribute to T cell exhaustion

**Program citations**
- [39]: PD-L1 induces and maintains regulatory T cells in glioblastoma
- [42]: Plasma PD-L1 as biomarker in clinical management of GBM
- [22]: GBM-derived EVs express PD-L1 on surface to suppress T cells

## Program: mRNA-Based Mesenchymal Signaling
Non-coding functional program where SERPINE1 mRNA itself, independent of protein-coding function, confers mesenchymal characteristics through sequestration of microRNAs and regulation of splicing factors. SERPINE1 mRNA binds to TRA2B splicing factor, downregulating immune response-associated genes. This program represents emerging evidence of regulatory RNAs functioning independently of protein translation, with implications for therapeutic targeting.

**Predicted impacts**
- Enhanced cell migration and invasion independent of SERPINE1 protein expression
- Resistance to anoikis through mRNA-mediated sequestration of anti-survival miRNAs
- Increased glycolytic activity driven by mRNA signaling
- Suppression of immune response genes reducing anti-tumor immunity
- Reduced CD8+ T cell infiltration correlating with SERPINE1 mRNA expression
- Resistance to miRNA-based therapeutic approaches

**Evidence summary**
Recent work demonstrates SERPINE1 mRNA confers mesenchymal characteristics independent of its protein product. When translation is blocked by mutation of start codons (Serpine1ATG*), enhanced migratory and invasive abilities are maintained. SERPINE1 mRNA acts as competing endogenous RNA (ceRNA) to sequester miRNAs affecting multiple cellular processes. Most significantly, SERPINE1 mRNA acts through TRA2B to downregulate immune response-associated genes, showing inverse correlation with CD8+ T cell infiltration in colon adenocarcinomas. This emerging program suggests targeting SERPINE1 mRNA through antisense oligonucleotides or other RNA-based therapeutics could enhance T cell infiltration.

**Atomic biological processes**
- SERPINE1 mRNA-TRA2B splicing factor interactions. Genes: SERPINE1
  - [51]: SERPINE1 mRNA downregulates immune response genes through TRA2B splicing factor without affecting TRA2B mRNA levels
  - [4]: SERPINE1 mRNA acts per se as post-transcriptional regulator in addition to encoding SERPINE1 protein
- microRNA sequestration and sponge activity. Genes: SERPINE1
  - [51]: SERPINE1 mRNA confers mesenchymal properties through sequestration of miRNAs affecting cell migration, invasion, and anoikis resistance
- Immune response gene suppression. Genes: SERPINE1
  - [4]: SERPINE1 mRNA downregulates expression of genes primarily associated with immune response through TRA2B-mediated mechanism
  - [51]: SERPINE1 mRNA expression negatively correlates with CD8A and CD3 levels in colon tumor surgical samples

**Atomic cellular components**
- RISC complex association of SERPINE1 mRNA. Genes: SERPINE1
  - [4]: SERPINE1 mRNA abundance in RISC complex increases 11.5-fold upon TGF-β treatment, indicating active involvement in RNA silencing

**Required genes (not in input)**
- Genes: TRA2B, microRNAs
  - [51]: TRA2B is splicing factor regulated by SERPINE1 mRNA to control immune gene expression

**Program citations**
- [51]: SERPINE1 mRNA per se confers mesenchymal characteristics independent of protein-coding function
- [4]: SERPINE1 mRNA has non-coding biological function affecting immune infiltration

## Bibliography
1. Fidan S, Ahmet C, İlknur S-E, Nazli E, Alp E, Fırat U, et al.. Identification of . Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
2. Lifeng M, Zheng J, Jiwei W, Ning Y, Qichao Q, Wenjing Z, et al.. Epithelial membrane protein 1 promotes glioblastoma progression through the PI3K/AKT/mTOR signaling pathway.. Oncology reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6609345/
3. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5692520/
4. Polo-Generelo S, Rodríguez-Mateo C, Torres B, Pintor-Tortolero J, Guerrero-Martínez JA, König J, et al.. Serpine1 mRNA confers mesenchymal characteristics to the cell and promotes CD8+ T cells exclusion from colon adenocarcinomas. Cell Death Discovery [Internet]. 2024Mar6;10(1). Available from: https://www.nature.com/articles/s41420-024-01886-8
5. Miao L, Jiang Z, Wang J, Yang N, Qi Q, Zhou W, et al.. Epithelial membrane protein 1 promotes glioblastoma progression through the PI3K/AKT/mTOR signaling pathway. Oncology Reports [Internet]. 2019Jun19;. Available from: https://www.spandidos-publications.com/10.3892/or.2019.7204/abstract
6. Available from: https://www.proteinatlas.org/ENSG00000137962-ARHGAP29/cancer/glioma
7. Yi M, Li T, Niu M, Zhang H, Wu Y, Wu K, et al.. Targeting cytokine and chemokine signaling pathways for cancer therapy. Signal Transduction and Targeted Therapy [Internet]. 2024Jul22;9(1). Available from: https://www.nature.com/articles/s41392-024-01868-3
8. Kimberly AR-C, Mitra N, Tae JL, Balveen K, Ji YY. The complex relationship between integrins and oncolytic herpes Simplex Virus 1 in high-grade glioma therapeutics.. Molecular therapy oncolytics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9233184/
9. Tsai H-F, Chang Y-C, Li C-H, Chan M-H, Chen C-L, Tsai W-C, et al.. Type V collagen alpha 1 chain promotes the malignancy of glioblastoma through PPRC1-ESM1 axis activation and extracellular matrix remodeling. Cell Death Discovery [Internet]. 2021Oct26;7(1). Available from: https://www.nature.com/articles/s41420-021-00661-3
10. Omar RA, Juan CQ, Ignacio C-A. The language of glioblastoma: A tale of cytokines and sex hormones communication.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12063100/
11. Qi Y, Weikun X, Songping S, Alireza S, Jesse L, Stephanie KS. Extracellular Matrix Proteins Confer Cell Adhesion-Mediated Drug Resistance Through Integrin α . Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8021872/
12. Wen Y, Hecheng Z, Jun T, Zhaoqi X, Quanwei Z, Yudong C, et al.. Identification of collagen genes related to immune infiltration and epithelial-mesenchymal transition in glioma.. Cancer cell international [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8147444/
13. Ruth MU, Anne B, Irina K, Peter V, Güliz A, Susan B. The CXCL2/IL8/CXCR2 Pathway Is Relevant for Brain Tumor Malignancy and Endothelial Cell Function.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33807899/
14. Zhong J, Wu X, Gao Y, Chen J, Zhang M, Zhou H, et al.. Circular RNA encoded MET variant promotes glioblastoma tumorigenesis. Nature Communications [Internet]. 2023Jul25;14(1). Available from: https://www.nature.com/articles/s41467-023-40212-1
15. Hirokazu S, Kyung-Don K, Justin TG, Mutsuko M, Hai Y, Junfeng S, et al.. Activation of the Receptor Tyrosine Kinase AXL Regulates the Immune Microenvironment in Glioblastoma.. Cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5984695/
16. Zhou C, Gao Y, Ding P, Wu T, Ji G. The role of CXCL family members in different diseases. Cell Death Discovery [Internet]. 2023Jul1;9(1). Available from: https://www.nature.com/articles/s41420-023-01524-9
17. Abdulhameed A-G, Bruce H, Morag P. Aberrant . Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10854665/
18. Yadav M, Sharma A, Patne K, Tabasum S, Suryavanshi J, Rawat L, et al.. AXL signaling in cancer: from molecular insights to targeted therapies. Signal Transduction and Targeted Therapy [Internet]. 2025Feb10;10(1). Available from: https://www.nature.com/articles/s41392-024-02121-7
19. Mijung I, Jungwook R, Wonyi J, Wanyeon K. FN1 and VEGFA Are Potential Therapeutic Targets in Glioblastoma as Determined by Bioinformatics Analysis.. Cancer genomics & proteomics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11696323/
20. Friedrich M, Sankowski R, Bunse L, Kilian M, Green E, Ramallo GC, et al.. Tryptophan metabolism drives dynamic immunosuppressive myeloid states in IDH-mutant gliomas. Nature Cancer [Internet]. 2021May24;2(7). Available from: https://www.nature.com/articles/s43018-021-00201-z
21. Ivana M, Federica C, Emiliano D, Tamara I, Giuseppe MDP, Enrico P, et al.. Heterogeneity Matters: Different Regions of Glioblastoma Are Characterized by Distinctive Tumor-Supporting Pathways.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7601979/
22. Simon T, Jackson E, Giamas G. Breaking through the glioblastoma micro-environment via extracellular vesicles. Oncogene [Internet]. 2020May4;39(23). Available from: https://www.nature.com/articles/s41388-020-1308-2
23. Hamed H, Mehrdad M, Ali AS, Mehryar HR. The immunosuppressive role of indoleamine 2, 3-dioxygenase in glioblastoma: mechanism of action and immunotherapeutic strategies.. Medical oncology (Northwood, London, England) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9206138/
24. Kacper AW, Natalia O, Maria P, Kamil W, Karolina S, Jakub M, et al.. In Search for Reliable Markers of Glioma-Induced Polarization of Microglia.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6013650/
25. Tannous BA, Badr CE. A TNF-NF-κB-STAT3 loop triggers resistance of glioma-stem-like cells to Smac mimetics while sensitizing to EZH2 inhibitors. Cell Death &amp; Disease [Internet]. 2019Mar19;10(4). Available from: https://www.nature.com/articles/s41419-019-1505-5
26. Chi YC, Sae-Bom J, Hee JY, Bum-Kyu C, Sang SK, Masanobu O, et al.. Glial TLR2-driven innate immune responses and CD8. Glia [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30720218/
27. Ren Y, Yang B, Guo G, Zhang J, Sun Y, Liu D, et al.. GBP2 facilitates the progression of glioma via regulation of KIF22/EGFR signaling. Cell Death Discovery [Internet]. 2022Apr18;8(1). Available from: https://www.nature.com/articles/s41420-022-01018-0
28. Kirk EC, Ramin AM, Bakhtiar Y. Nuclear factor-κB in glioblastoma: insights into regulators and targeted therapy.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4767244/
29. Amir MM, Jalil M, Masoud SM. Gene Expression Quantification of Toll like Receptors 2, 4 and Co-molecules in Human Glioblastoma Cell Line (U87-MG): Toward a New In vitro Model of Inflammation.. Iranian journal of basic medical sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3586846/
30. Jianliang L, Wei W. Guanylate-binding protein 5: a promising biomarker and therapeutic target.. Infection and immunity [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12418754/
31. Yu-Ting T, An-Chih W, Wen-Bin Y, Tzu-Jen K, Jian-Ying C, Wen-Chang C, et al.. ANGPTL4 Induces TMZ Resistance of Glioblastoma by Promoting Cancer Stemness Enrichment via the EGFR/AKT/4E-BP1 Cascade.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6888274/
32. Hui C, Xuemei Z, Ziyi W, Jing L, Yingbin L, Rong S. Activated kynurenine pathway metabolism by YKL-40 establishes an inhibitory immune microenvironment and drives glioblastoma development.. Cellular and molecular life sciences : CMLS [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11668713/
33. Harpreet K, Sabeen ZA, Lauren H, Marianne H-C, Isabella T, Xing-Gang M, et al.. The transcriptional modulator HMGA2 promotes stemness and tumorigenicity in glioblastoma.. Cancer letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
34. Kane K, Edwards D, Chen J. The influence of endothelial metabolic reprogramming on the tumor microenvironment. Oncogene [Internet]. 2024Nov20;44(2). Available from: https://www.nature.com/articles/s41388-024-03228-5
35. Available from: https://www.jci.org/articles/view/147552
36. Available from: https://www.oncotarget.com/article/9744/text/
37. Tommaso S, Claudia A, Miriam dell' A, Lucia M, Andrea M, Filippo G, et al.. ZFP36 stabilizes RIP1 via degradation of XIAP and cIAP2 thereby promoting ripoptosome assembly.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4424499/
38. Carolina M, Thomas U, Paula K, Barbara O, Annalisa I, Yuliia D, et al.. NF1 regulates mesenchymal glioblastoma plasticity and aggressiveness through the AP-1 transcription factor FOSL1.. eLife [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34399888/
39. Joseph D, Jonathan BL, Daniel O, Yuping L, Dorina V, Gurvinder K, et al.. The immune checkpoint protein PD-L1 induces and maintains regulatory T cells in glioblastoma.. Oncoimmunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5993506/
40. Selmi T, Martello A, Vignudelli T, Ferrari E, Grande A, Gemelli C, et al.. ZFP36 expression impairs glioblastoma cell lines viability and invasiveness by targeting multiple signal transduction pathways. Cell Cycle [Internet]. 2012May15;11(10). Available from: https://www.tandfonline.com/doi/full/10.4161/cc.20309
41. Available from: https://elifesciences.org/articles/64846
42. Masood AB, Batool S, Bhatti SN, Ali A, Valko M, Jomova K, et al.. Plasma PD-L1 as a biomarker in the clinical management of glioblastoma multiforme—a retrospective cohort study. Frontiers in Immunology [Internet]. 2023Jul17;14. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1202098/full
43. Michelina F, Luis DV, Kamel K, Renato F, Giosuè S, Vincenzo G, et al.. BAG3 protein is overexpressed in human glioblastoma and is a potential target for therapy.. The American journal of pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3124067/
44. Lan S, Xiaona Z, Yanmeng L, Wei C, Shanna W, Bei Z, et al.. KLF5 regulates epithelial-mesenchymal transition of liver cancer cells in the context of p53 loss through miR-192 targeting of ZEB2.. Cell adhesion & migration [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/32965165/
45. Prabhu KS, Therachiyil L, Masoodi T, Bhat AA, Uddin S. GADD45: a crucial component of the DNA damage response and a potential cancer therapeutic target. Expert Opinion on Therapeutic Targets [Internet]. 2025Dec8;. Available from: https://www.tandfonline.com/doi/full/10.1080/14728222.2025.2589807?src=
46. Roth C, Paulini L, Hoffmann ME, Mosler T, Dikic I, Brunschweiger A, et al.. <scp>BAG3</scp> regulates cilia homeostasis of glioblastoma via its <scp>WW</scp> domain. BioFactors [Internet]. 2024Apr24;50(6). Available from: https://iubmb.onlinelibrary.wiley.com/doi/full/10.1002/biof.2060
47. Yao L, Ceshi C. The roles and regulation of the KLF5 transcription factor in cancers.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
48. Hsiao-Han W, Tsuey-Yu C, Wei-Chen L, Kuo-Chen W, Jyh-Wei S. GADD45A plays a protective role against temozolomide treatment in glioblastoma cells.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5562912/
49. Ren Y, Chen M, Wu G, Ji D, Zhou GG, Ren P-G, et al.. High accumulation of Mx2 renders limited multiplication of oncolytic herpes simplex virus-1 in human tumor cells. Scientific Reports [Internet]. 2021Oct27;11(1). Available from: https://www.nature.com/articles/s41598-021-00691-y
50. McFarland BC, Hong SW, Rajbhandari R, Twitty GB, Gray GK, Yu H, et al.. NF-κB-Induced IL-6 Ensures STAT3 Activation and Tumor Aggressiveness in Glioblastoma. PLoS ONE [Internet]. 2013Nov11;8(11). Available from: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0078728
51. Anastasiya VL, Alesya VS, Vladimir AG, Julia AB, Elizaveta MS, George SK, et al.. Multi-Omics Analysis of Glioblastoma Cells' Sensitivity to Oncolytic Viruses.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8582528/
52. Braden CM, Suk WH, Rajani R, George BT, G KG, Hao Y, et al.. NF-κB-induced IL-6 ensures STAT3 activation and tumor aggressiveness in glioblastoma.. PloS one [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/24244348/
53. Lin C, Yang S, Shen S, Hsieh Y, Hsu F, Chen C, et al.. Serum amyloid A1 in combination with integrin αVβ3 increases glioblastoma cells mobility and progression. Molecular Oncology [Internet]. 2018Apr17;12(5). Available from: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.12196
54. Alberto M, Cecilia G, Barbara B. Pentraxin 3, a non-redundant soluble pattern recognition receptor involved in innate immunity.. Vaccine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/12763682/
55. Wang D, Berglund A, Kenchappa RS, Forsyth PA, Mulé JJ, Etame AB. BIRC3 is a novel driver of therapeutic resistance in Glioblastoma. Scientific Reports [Internet]. 2016Feb18;6(1). Available from: https://www.nature.com/articles/srep21710
56. Franciele HK, Renata CA, Renato RM, Silvya SM-E, Ana C. Dual effect of serum amyloid A on the invasiveness of glioma cells.. Mediators of inflammation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3596950/
57. Available from: https://ashpublications.org/blood/article/107/1/151/21731/The-pattern-recognition-receptor-PTX3-is-recruited
58. Loyola VG, Tiffany D, Yuhui Y, Gregory NF, Ganiraju M, Arvind R, et al.. Analysis of the inhibitors of apoptosis identifies BIRC3 as a facilitator of malignant progression in glioma.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5355046/
