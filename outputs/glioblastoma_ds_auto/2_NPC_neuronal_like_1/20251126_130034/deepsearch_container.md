# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: malignant glioblastoma
- Tissue: brain

## Input Genes
CFAP43, NEGR1, DNAH12, LRRC2, VAT1L, ZNF804B, RBMS3, SLC14A1, GABRA5, ZBBX, ADAMTS18, CFAP52, GRM1, MAP3K19, FHAD1, TCTEX1D1, DNAAF1, DCDC2, AC005165.1, COL21A1, PKHD1, ZNF521, EPB41L4B, ERICH3, PLAGL1, ... (94 total)

## Program: Ciliary Dysfunction and Motility Defects
Coordinated dysfunction of cilia and flagella structure and function through loss-of-function variants in axonemal dynein and associated proteins. In glioblastoma context, ciliary dysfunction may impair motile cilia-dependent signaling and cellular communication, particularly relevant given that mutations in CFAP43 and DNAH5 cause morphological abnormalities in motile cilia that result in hydrocephalus and primary ciliary dyskinesia. Multiple genes encoding dynein axonemal assembly factors (DNAAFs) and outer dynein arm components are present in this program.

**Predicted impacts**
- Impaired primary cilia formation and motility may disrupt hedgehog signaling transduction and cellular sensing of microenvironmental cues
- Loss of ciliary-mediated fluid flow and mechanotransduction may compromise cell-cell communication within tumor microenvironment
- Defective cilia may alter intraflagellar transport and affect localization of signaling proteins involved in tumor progression
- Ciliary dysfunction may disrupt planar cell polarity signaling, potentially affecting collective glioma cell migration and invasion patterns

**Evidence summary**
Fourteen genes encoding core axonemal dynein components, dynein assembly factors, and associated structural proteins are present in the input list. Experimental evidence from CFAP43 and DNAH5 studies demonstrates that mutations in these genes cause severe morphological ciliary abnormalities. While the primary literature focuses on ciliary dysfunction in non-malignant contexts (hydrocephalus, infertility, primary ciliary dyskinesia), the presence of multiple ciliary genes in a glioblastoma context suggests potential role in altered cell-cell signaling and microenvironmental interactions that may contribute to GBM phenotype. The significance is moderate because direct mechanistic evidence linking ciliary dysfunction to GBM progression is limited in provided literature.

**Atomic biological processes**
- Axonemal dynein assembly. Genes: DNAAF1, CFAP43, CFAP52, CFAP61, CFAP73, CFAP100, CFAP206, CFAP221
  - [3]: Comprehensive review of dynein nomenclature and function in ciliary motility; DNAAF genes encode proteins critical for cytoplasmic preassembly of dynein arms
- Outer dynein arm structure and function. Genes: DNAH5, DNAH12, TCTEX1D1, DCDC2
  - [2]: DNAH5 novel variants cause outer dynein arm absence, leading to primary ciliary dyskinesia with structural abnormalities in ciliary axoneme
  - [3]: DNAH5 encoding dynein axonemal heavy chain 5 as core component of outer dynein arm complex
- Radial spoke and central pair apparatus. Genes: RSPH1, DRC1
  - [3]: Discussion of radial spoke proteins and their role in axonemal structure maintenance

**Atomic cellular components**
- Primary cilium axoneme. Genes: CFAP43, CFAP47, CFAP52, CFAP61, CFAP73, CFAP100, CFAP157, CFAP206, CFAP221, DNAH5, DNAH12, DNAAF1, DCDC2, TCTEX1D1, RSPH1, DRC1
  - [1]: CFAP43 knockout mice exhibit morphologic abnormality of motile cilia with dilation of brain ventricles similar to human NPH, indicating critical role in ciliary structure
  - [2]: Transmission electron microscopy analysis of ciliary structure demonstrates absence of dynein arms in PCD patients with DNAH5 mutations

**Required genes (not in input)**
- Genes: DNAH1, DNAH2, DNAH3, DNAH7, DNAH8, DNAH9, DNAI1, DNAI2, IFT88, KIF3A
  - [3]: Multiple additional dynein heavy chain and intermediate chain genes required for complete outer dynein arm assembly not present in input list

**Program citations**
- [1]: CFAP43 loss-of-function causes ciliary morphologic abnormalities and hydrocephalus phenotype in knockout mice
- [2]: DNAH5 pathogenic variants associated with primary ciliary dyskinesia demonstrate outer dynein arm absence
- [3]: Comprehensive nomenclature and functional review of dynein components and assembly factors
- [5]: DNAH5 mutations in PCD patient-derived iPSC lines demonstrate utility of patient-derived models for studying ciliary dysfunction

## Program: IL-6-Mediated Immunosuppression
Coordinated immunosuppressive signaling driven by IL-6 axis and its regulation through NEGR1 and GABAergic receptor signaling. In glioblastoma, this program supports tumor growth through myeloid-cell polarization and T-cell exhaustion. IL6R activation drives STAT3-dependent immunosuppression, while NEGR1 negatively regulates IL-6 trans-signaling. GABAergic neurons provide depolarizing input to DMG cells through GABRA5-mediated signaling, promoting tumor growth.

**Predicted impacts**
- Enhanced IL-6 signaling promotes M2 macrophage polarization and increases PD-L1 expression on myeloid cells, suppressing CD8+ T cell function
- Increased circulating IL-6 and sIL-6R create systemic immunosuppressive environment; elevated IL-6 correlates with worse overall survival
- GABAergic synaptic input depolarizes glioma cells through GABA-A receptor activation, promoting depolarization-dependent tumor growth in diffuse midline gliomas
- Combined IL-6-driven myeloid suppression and GABA-mediated glioma cell depolarization create robust immunosuppressive niche resistant to checkpoint inhibitor monotherapy
- NEGR1-mediated negative regulation of IL-6 trans-signaling could serve as brake on immunosuppression but is likely downregulated in GBM

**Evidence summary**
IL-6 pathway extensively characterized in GBM context with strong evidence that GBM-derived IL-6 drives myeloid-mediated immunosuppression through STAT3 activation and PD-L1 upregulation on myeloid cells. NEGR1 functionally interacts with IL-6R to attenuate trans-signaling. GABAergic receptor subunits GABRA5 and GABRG3 are present in glioma and mediate pro-tumor depolarizing input from neurons. Three genes directly support this program with multiple supporting citations demonstrating mechanistic involvement in GBM pathology.

**Atomic biological processes**
- IL-6 trans-signaling and STAT3 activation. Genes: IL6R, NEGR1
  - [20]: GBM-derived IL-6 is necessary and sufficient for myeloid PD-L1 induction through STAT3-dependent mechanism; high IL6 expression correlates with worse survival outcomes
  - [10]: NEGR1 interacts with IL-6R and negatively regulates IL-6 trans-signaling through attenuation of STAT3 phosphorylation
- GABAergic neuron-to-glioma synaptic signaling. Genes: GABRA5, GABRG3
  - [17]: DMG cells express GABA receptors and establish functional GABAergic synapses with neurons; depolarizing GABAergic input driven by NKCC1 promotes tumor growth through GABA-A receptor signaling
  - [14]: GABRA5 and GABRG expression in glioma subtypes associated with glioma progression; GABRA5 particularly enriched in aggressive Group 3 medulloblastoma and DMG
- Myeloid cell polarization and recruitment. Genes: IL6R
  - [20]: IL-6 stimulation of myeloid cells drives dose-dependent increase in PD-L1 and CD163 expression; IL-6 targeting with tocilizumab or siltuximab reduces immunosuppressive myeloid phenotype

**Atomic cellular components**
- IL-6 receptor signaling complex. Genes: IL6R, NEGR1
  - [10]: IL-6R and gp130 form the IL-6 receptor complex; NEGR1 localizes to lipid rafts where it can interact with membrane-associated IL-6R
- GABA-A receptor channel complex. Genes: GABRA5, GABRG3
  - [17]: GABRA5 and GABRG3 are subunits of GABA-A receptor channels; H3K27M-altered DMG cells express multiple GABA-A receptor subunits enabling functional depolarizing GABAergic synapses

**Required genes (not in input)**
- Genes: IL6, GP130, STAT3, JAK1, JAK2, NKCC1, GABA, GAD
  - [20]: IL-6, GP130, JAK-STAT signaling components required for immunosuppressive phenotype
  - [17]: NKCC1 chloride transporter required for depolarizing GABA effect in DMG cells; GABA synthesis and release machinery required for synaptic signaling

**Program citations**
- [10]: NEGR1 negatively regulates IL-6 trans-signaling through IL-6R interaction and STAT3 attenuation in adipocytes
- [14]: GABRA5 expression in aggressive glioma subgroups; GABA-A receptor agonism reduces cell viability in Group 3 MB
- [17]: Identification of functional GABAergic neuron-to-glioma synapses promoting tumor growth through depolarizing GABA input in DMGs
- [20]: Definitive evidence that GBM-derived IL-6 drives myeloid PD-L1 induction through STAT3 mechanism; IL-6 signaling inhibition reduces tumor growth and enhances survival

## Program: Tumor-Suppressive Chromatin Remodeling
CHD5 and related chromatin remodeling factors mediate tumor suppression through histone binding and transcriptional regulation of cell cycle inhibitors and differentiation programs. CHD5 is a member of the chromatin remodeling complex family mapping to 1p36, a region frequently deleted in cancer. CHD5 binds unmodified histone H3 through its PHD domains and regulates expression of p16 and p19 tumor suppressors. Loss of CHD5 or its functional domains abrogates tumor suppression and promotes gliomagenesis.

**Predicted impacts**
- Loss or functional impairment of CHD5 removes critical brake on glioma cell proliferation and blocks differentiation programs protective against transformation
- Intact CHD5 function maintains expression of p16 and p19 tumor suppressors, preventing aberrant cell cycle progression
- ZNF521 overexpression in SHH-pathway-driven gliomas promotes stemness maintenance and migration through enhanced Hedgehog signaling
- Combined CHD5 loss and ZNF521 upregulation would create permissive environment for glioma initiation and maintenance of stem cell properties

**Evidence summary**
CHD5 is well-established as tumor suppressor with evidence that loss of CHD5 or its functional histone-binding domains promotes glioma formation. CHD5 mutations abrogating H3 binding are unable to suppress gliomagenesis in vivo. ZNF521 serves as positive regulator of Hedgehog pathway-driven glioma, particularly in SHH-dysregulated tumors. Two genes directly support this program with strong experimental evidence from chromatin immunoprecipitation, gain/loss-of-function studies, and in vivo glioma models.

**Atomic biological processes**
- Histone-binding chromatin remodeling. Genes: CHD5
  - [27]: CHD5 dual PHDs mediate binding specifically to N-terminus of H3 lacking post-translational modifications; this interaction is essential for inhibiting proliferation and inducing differentiation
- Cell cycle inhibition and differentiation. Genes: CHD5
  - [27]: PHD-mediated H3 binding critical for CHD5 to modulate gene expression including p16/Rb and p19/p53 pathways and induce differentiation of neuroblastoma cells
  - [30]: CHD5 suppresses glioblastoma and mediates tumor suppression through MYC inhibition
- Hedgehog pathway-mediated transcription. Genes: ZNF521
  - [40]: ZNF521 interacts with GLI1/GLI2 transcription factors and recruits NuRD-HDAC complex to enhance Hedgehog-responsive promoters; high ZNF521 expression in SHH-driven medulloblastoma

**Atomic cellular components**
- CHD5-NuRD chromatin remodeling complex. Genes: CHD5
  - [27]: CHD5 belongs to CHD family of chromatin remodeling proteins; functions through PHD-histone interactions to regulate transcription
- ZNF521-GLI-NuRD complex. Genes: ZNF521
  - [40]: ZNF521 contains N-terminal NuRD-binding motif; interacts with GLI1 and GLI2 and recruits HDAC-NuRD complex for transcriptional activation of Hedgehog targets

**Required genes (not in input)**
- Genes: CDKN2A, RB1, TP53, HDAC1, RBBP7, CHD4, GLI1, GLI2, SUFU
  - [27]: p16/Rb and p19/p53 tumor suppressor pathways are primary targets of CHD5 regulation; HDAC1 and NuRD complex components essential for CHD5 function
  - [40]: GLI1, GLI2, and SUFU required for ZNF521-mediated Hedgehog pathway activation

**Program citations**
- [27]: CHD5 PHD-mediated H3 binding essential for tumor suppression; CHD5 loss enhances proliferation and compromises p16/Rb and p19/p53 pathways
- [30]: CHD5 suppresses glioblastoma development with insights into therapeutic targeting for 1p36 deletions
- [40]: ZNF521 cooperation with Hedgehog transcription factors; high expression in SHH-driven medulloblastoma correlates with aggressive phenotype

## Program: Extracellular Matrix Remodeling and Invasion
POSTN, THBS1, and collagen genes coordinate extracellular matrix remodeling to promote glioma cell invasion, angiogenesis, and immune suppression. POSTN secreted by glioma stem cells recruits tumor-associated macrophages (TAMs) and promotes invasive phenotype through NF-κB signaling. THBS1 is upregulated with glioma grade and mediates both angiogenesis and invasion while contributing to immune suppression. Collagen genes define mesenchymal GBM subtype with prognostic implications.

**Predicted impacts**
- POSTN-mediated TAM recruitment creates immunosuppressive microenvironment enriched in M2 macrophages expressing immunosuppressive cytokines and PD-L1
- POSTN-driven NF-κB activation in glioma cells enhances EMT, invasiveness, and chemoresistance
- THBS1 upregulation promotes both angiogenesis and invasion while simultaneously suppressing CD8+ T cell proliferation through TNF-β-mediated mechanisms
- Elevated collagen deposition creates physical barrier to immune infiltration and promotes mesenchymal GBM phenotype associated with poor prognosis
- N-cadherin dynamics enable context-dependent migration on neural cells versus inhibited invasion into ECM-rich regions, allowing differential spatial invasion patterns

**Evidence summary**
Five genes encoding ECM remodeling factors present in input list with substantial experimental evidence from glioma models. POSTN extensively characterized as GSC-secreted factor that recruits immunosuppressive macrophages and promotes invasion. THBS1 elevated in high-grade gliomas and linked to poor prognosis through dual mechanisms of angiogenesis regulation and immune suppression. Collagen genes define mesenchymal GBM subtype with distinct molecular and clinical features. N-cadherin-related genes contribute to context-dependent migration. Strong evidence from TCGA analysis, immunofluorescence studies, and genetically engineered mouse models.

**Atomic biological processes**
- POSTN-mediated macrophage recruitment. Genes: POSTN
  - [9]: GSC-secreted POSTN recruits M2 tumor-associated macrophages; POSTN knockdown reduces TAM density and tumor growth; overexpression of POSTN accelerates xenograft growth and increases M2 TAM recruitment
  - [12]: POSTN-induced NF-κB signaling and EMT processes promote GBM malignancy and chemoresistance
- THBS1-mediated angiogenesis and invasion. Genes: THBS1
  - [21]: TGFβ1 induces THBS1 expression through SMAD3 binding; THBS1 mediates both angiogenesis regulation and invasion; tumor cell-bound CD47 involved in THBS1 effects on invasion
  - [24]: THBS1 expression increases with glioma grade; hypomethylation and overexpression predict unfavorable prognosis; THBS1 correlates with immune and inflammatory responses
- Collagen-mediated mesenchymal transition. Genes: COL21A1, COL13A1, COL23A1, COL26A1
  - [11]: Collagen expression patterns define glioma subtypes with distinct molecular features and survival outcomes; fibrillar collagens COL1A1 define mesenchymal subtype with poorest prognosis; minor collagens exhibit dynamic expression across GBM subtypes
- N-cadherin-mediated cell-cell adhesion dynamics. Genes: CDH7
  - [51]: N-cadherin homotypic interactions differentially regulate glioma migration depending on microenvironment; N-cadherin stimulates migration on neural cells but inhibits invasion into ECM; N-cadherin cleavage by ADAM-10 promotes glioma cell migration
  - [54]: N-cadherin cleavage by ADAM proteases is prerequisite for glioma migration; increased N-cadherin cleavage rate in glioblastoma compared to normal brain

**Atomic cellular components**
- POSTN-secreted glycoprotein. Genes: POSTN
  - [9]: GSC-secreted POSTN protein acts as chemoattractant for macrophages and monocytes; POSTN acts through integrin signaling and toll-like receptor pathways
- Thrombospondin-1 matricellular protein. Genes: THBS1
  - [21]: THBS1 is matricellular protein with roles in angiogenesis regulation, cell migration, and macrophage-mediated immune suppression; expressed in both tumor cells and vasculature
- Collagen-rich extracellular matrix. Genes: COL21A1, COL13A1, COL23A1, COL26A1
  - [11]: Fibrillar collagens and minor collagens define structural organization of GBM microenvironment; collagen composition correlates with stroma fraction, molecular subtype, and survival
- N-cadherin adhesion junction. Genes: CDH7
  - [51]: N-cadherin localizes to filamentous connections in migrating glioma leader cells and epithelial-like junctions in follower cells; regulates collective invasion

**Required genes (not in input)**
- Genes: COL1A1, COL1A2, COL4A1, COL4A2, LAMA4, LAMB2, LAMC1, NCAN, BCAN, VCAN, TIMP1, TIMP2, TIMP3, TIMP4, MMP2, MMP9, ADAM10, ITGA3, ITGA5, ITGB1, CD47
  - [8]: Multiple ECM components including fibrillar collagens, laminins, proteoglycans, and MMPs regulate GBM angiogenesis and endothelial cell function
  - [21]: ADAM10 protease mediates N-cadherin cleavage; CD47 interaction with SIRPα involved in THBS1 effects on invasion

**Program citations**
- [9]: POSTN knockdown in GSCs reduces TAM density and tumor growth; overexpression increases M2 TAM recruitment and tumor progression
- [11]: Comprehensive analysis of collagen expression patterns defining GBM subtypes and predicting genetic features and survival outcomes
- [12]: POSTN-induced NF-κB signaling promotes GBM malignancy and chemoresistance
- [21]: TGFβ1-SMAD3-THBS1 axis regulates GBM invasion; THBS1 inhibition enhances anti-angiogenic therapy efficacy
- [24]: THBS1 as prognostic biomarker of GBM malignancy; hypomethylation predicts unfavorable outcomes
- [51]: N-cadherin dynamics regulate context-dependent glioma migration through homotypic interactions

## Program: Metabolic Reprogramming and Energy Homeostasis
KSR2, ADCY8, SLC22A3, and ion channel proteins coordinate metabolic reprogramming of glioma cells to enhance proliferation and chemoresistance. KSR2 integrates mitogenic and metabolic signaling through AMPK, regulating both glycolytic and oxidative metabolism. ADCY8 polymorphisms correlate with glioma risk in sex-specific manner through cAMP pathway modulation. SLC22A3 functions as tumor suppressor through metabolic homeostasis. Ion channels including KCNJ3 and CACNA2D1 regulate cell volume, calcium signaling, and metabolic capacity.

**Predicted impacts**
- Loss of KSR2 through praja2-mediated degradation shifts glioma metabolism toward glycolysis and away from oxidative phosphorylation, reducing AMPK activity and metabolic flexibility
- ADCY8 dysregulation creates sex-biased susceptibility to glioma with enhanced cAMP suppression promoting female glioma development
- Reduced SLC22A3 expression and function impairs organic cation homeostasis and promotes metabolic dysfunction favoring tumor growth
- Enhanced potassium and calcium channel activity facilitates regulatory volume decrease enabling glioma cell invasion through confined CNS spaces
- Coordinated metabolic reprogramming reduces energy expenditure on antitumor immune responses while enhancing biosynthetic capacity for rapid proliferation

**Evidence summary**
Five genes directly support metabolic reprogramming program with established roles in glioma energy homeostasis. KSR2 extensively characterized as critical regulator of both mitogenic signaling and metabolic capacity through AMPK interaction. ADCY8 polymorphisms linked to sex-specific glioma risk through cAMP pathway modulation. SLC22A3 identified as favorable prognostic biomarker downregulated in GBM. Ion channels KCNJ3 and CACNA2D1 mediate volume regulation essential for GBM invasion and proliferation. Evidence from metabolic flux analysis, genetic mouse models, and clinical correlation studies.

**Atomic biological processes**
- KSR2-AMPK metabolic integration. Genes: KSR2
  - [57]: KSR2 essential to tumor cell energy homeostasis; KSR2 interacts with AMPK subunits and promotes AMPK phosphorylation; KSR2 depletion reduces glycolytic and oxidative metabolism
  - [60]: Praja2 E3 ubiquitin ligase degrades KSR2, restraining AMPK activity and attenuating oxidative metabolism in GBM; praja2 preferentially expressed in IDH1 wild-type GBM
- cAMP pathway and adenylate cyclase regulation. Genes: ADCY8
  - [25]: ADCY8 polymorphisms correlate with glioma risk in sex-specific manner; cAMP pathway sexually dimorphic with differential ADCY8 capacity between males and females; ADCY inhibition promotes Nf1-deficient astrocyte growth specifically in females
  - [28]: cAMP pathway well-known to be sexually dimorphic; ADCY8 SNPs affected glioma risk in sex-specific fashion, elevating risk for females while reducing risk for males
- Urea and organic cation transport. Genes: SLC14A1, SLC22A3
  - [46]: SLC14A1 gene encodes UT-B protein, membrane channel crucial for passive urea transport; SLC14A1 downregulation associated with renal cell carcinoma development; elevated expression inhibits lung squamous cell carcinoma
- Potassium and calcium-dependent cell volume regulation. Genes: KCNJ3, CACNA2D1
  - [58]: BK channels, IK channels, and K2P channels regulate glioma cell volume dynamics critical for proliferation and migration; EAG2 channel selective membrane enrichment at G2/M phase facilitates cell volume reduction and mitotic entry
  - [55]: Depolarization through membrane potential manipulation reduces intracranial tumor growth; regulatory volume decrease through K+ and Cl- efflux facilitates invasion through confined spaces

**Atomic cellular components**
- KSR2-AMPK metabolic signaling complex. Genes: KSR2
  - [57]: KSR2 serves as scaffold protein mediating Ras with respect to ERK signaling and also acts as platform for AMPK regulation
- Adenylate cyclase-cAMP signaling axis. Genes: ADCY8
  - [25]: ADCY8 encodes adenylate cyclase 8; modulates cAMP synthesis downstream of CXCL12 and other GPCR agonists
- SLC transporter family proteins. Genes: SLC14A1, SLC22A3
  - [46]: SLC14A1 encodes UT-B urea transporter; SLC22A3 encodes OCT3 organic cation transporter; both regulate metabolite homeostasis
- G-protein-coupled inward rectifier and voltage-gated calcium channels. Genes: KCNJ3, CACNA2D1
  - [58]: KCNJ3 encodes GIRK1 inward rectifier K+ channel; CACNA2D1 encodes α2δ-1 auxiliary subunit of voltage-gated calcium channels; both participate in cell volume regulation and calcium signaling

**Required genes (not in input)**
- Genes: AMPK, PRKAA1, PRKAA2, PRKAG1, PRKAG2, ERK1, ERK2, KRAS, HRAS, NRAS, CXCL12, CXCR4, PDK1, PDH, PKM, LDHA, GLS, GLUD1
  - [57]: AMPK catalytic and regulatory subunits essential for KSR2-mediated metabolic integration; ERK and Ras components required for mitogenic signaling through KSR2
  - [33]: Multiple metabolic enzymes including PDH, PKM, LDHA required for glycolytic reprogramming; insulin signaling pathway components essential for proliferation

**Program citations**
- [25]: ADCY8 polymorphisms correlate with glioma risk in sex-specific manner; cAMP pathway differentially affects male versus female glioma susceptibility
- [57]: KSR2 essential to tumor cell energy homeostasis; critical to integration of mitogenic and metabolic signaling pathways
- [58]: Potassium channels regulate glioma proliferation, migration, and apoptosis; dysfunction confers pro-proliferative signals through calcium signaling
- [59]: SLC22A3 independent favorable prognostic biomarker; low expression associated with high-risk GBM
- [60]: Praja2-mediated KSR2 degradation attenuates oxidative metabolism in IDH1 wild-type GBM

## Program: Neurotransmitter Signaling and Synaptic Communication
GRM1 and GRM4 metabotropic glutamate receptors mediate pro-tumor glutamatergic signaling that drives glioma proliferation and suppresses antitumor immunity. NRG3 neuregulin ligand activates ErbB4 receptors involved in glial differentiation and survival signaling. Dysregulation of these synaptic communication pathways enables glioma cells to integrate signals from surrounding neurons and facilitate tumor progression through glutamate-calcium signaling and neuregulin-ErbB crosstalk.

**Predicted impacts**
- Elevated mGluR1/5 signaling in glioma cells activates PI3K/AKT/mTOR pro-survival axis and drives proliferation through positive feedback enhancement of glutamate release
- mGluR2/3 signaling suppresses G1/S transition in subset of GBM cells, potentially promoting quiescent glioma stem cell population resistant to cytotoxic therapy
- GRM4 upregulation in glioma creates immunosuppressive microenvironment by suppressing NK and T cell antitumor immunity through cAMP modulation
- NRG3-ErbB4 signaling enhances glial cell differentiation and survival while simultaneously promoting expression of neurotransmitter receptors that sensitize glioma cells to neuronal input
- Coordinated dysregulation of mGluR and neuregulin signaling enables glioma cells to parasitize neuron-derived glutamate and neuregulin signals for self-promotion while suppressing immune surveillance

**Evidence summary**
Three genes support neurotransmitter signaling program with evidence that glioma cells aberrantly express and respond to synaptic signaling molecules. GRM1 and GRM4 intensively studied in glioma context with evidence that dysregulated glutamate-mGluR signaling drives proliferation and suppresses immunity. GRM4 specifically identified as suppressor of antitumor immune responses. NRG3 as neuregulin family member participates in ErbB4 signaling important for CNS glia. Evidence from pathway analysis, single-cell RNA sequencing, and immunotherapy studies.

**Atomic biological processes**
- Metabotropic glutamate receptor signaling. Genes: GRM1, GRM4
  - [13]: Group I mGluRs (mGluR1, mGluR5) and Group II mGluRs abundantly expressed in GBM cells; mGluR1/5 activation drives PI3K/AKT/mTOR pathway to tumorigenesis; mGluR2/3 stimulate cell proliferation by negative regulation of G1/S phase transition
  - [16]: GRM4 metabotropic glutamate receptor 4 suppresses antitumor immunity; GRM4 deficiency promotes NK, CD4+, and CD8+ T cell activation through cAMP pathway; GRM4 high-GRM4 low signature correlates with improved survival in melanoma
- Glutamate-calcium signaling in tumorigenesis. Genes: GRM1, GRM4
  - [13]: Elevated intracellular Ca2+ via NMDAR and mGluR activation hastens glutamate release, intensifies glutamatergic receptor activation, and drives glioma proliferation; Ca2+ signaling provides positive feedback to promote glioma formation
- Neuregulin-ErbB signaling in glial cells. Genes: NRG3
  - [19]: NRG-1 is crucial for proliferation, differentiation, and survival of glial cells; NRG-ErbB pathway induces receptors for neurotransmitters including GABA and NMDA; NRG-2 has essential role in postnatal and adult brain

**Atomic cellular components**
- Metabotropic glutamate receptor complex. Genes: GRM1, GRM4
  - [13]: mGluR1 and mGluR5 (Group I) coupled to IP3 and DAG signaling; mGluR2/3 (Group II) negatively regulate adenylyl cyclase; all subtypes activate phospholipase C and modulate intracellular calcium
- Neuregulin-1 ligand and ErbB4 receptor. Genes: NRG3
  - [19]: NRG proteins bind ErbB4 with high specificity in central nervous system; NRG-ErbB signaling activates PI3K, Ras-MAPK, and JAK-STAT pathways

**Required genes (not in input)**
- Genes: GRIN1, GRIN2A, GRIN2B, GRIN2C, GRIN2D, GRIA1, GRIA2, GRIA3, GRIA4, GRIK1, GRIK2, GRM2, GRM3, GRM5, GRM6, GRM7, GRM8, PLCB, IP3R, RYANR, ERBB4, ERBB2, ERBB3
  - [13]: Multiple NMDA and AMPA receptor subunits, multiple mGluR subtypes, and downstream signaling components required for complete glutamatergic signaling network in glioma
  - [19]: ErbB4 is primary receptor for NRG-1 in CNS; ErbB2 and ErbB3 form heterodimers with ErbB4 to modulate ligand binding and signaling

**Program citations**
- [13]: Glutamatergic signaling may pathologically exaggerate in glioma, promoting transformation of astroglia to glioma through mGluR1/5-PI3K/AKT/mTOR pathway
- [16]: GRM4 targeting represents novel approach for cancer immunotherapy; GRM4 deficiency promotes antitumor immunity through NK and CD8+ T cell activation
- [19]: NRG-1-ErbB4 pathway crucial for proliferation, differentiation, and survival of glial cells and Schwann cells; regulates neurotransmitter receptor expression

## Program: BMP-Mediated Developmental Signaling
BMP6 and related bone morphogenetic protein signaling promotes quiescent glioma stem cell phenotype while conferring resistance to radiation and chemotherapy. BMP pathway activation induces differentiation while suppressing proliferation through ID protein modulation. BMP signaling defines population of slow-cycling glioma stem cells that may represent reservoir for tumor recurrence following cytotoxic therapy.

**Predicted impacts**
- BMP6 signaling promotes and maintains quiescent glioma stem cell population resistant to proliferation-targeting therapeutics
- BMP-induced ID1 activity suppresses differentiation, preserving stem cell properties and long-term tumorigenic potential
- Enhanced MGMT and ATM expression through BMP signaling confers chemoresistance and radioresistance, reducing efficacy of adjuvant therapy
- BMP-positive GSC population may serve as cellular reservoir for tumor recurrence following cytotoxic therapy targeting proliferative population
- Slow-cycling BMP-positive GSCs remain chemosensitive to differentiation-inducing drugs but resistant to cell-cycle-targeting agents

**Evidence summary**
One gene (BMP6) directly represents BMP signaling program in input list. Extensive evidence from glioma stem cell studies demonstrates that BMP pathway activation defines quiescent GSC population distinct from proliferative TGF-β-positive population. BMP signaling confers therapy resistance through dual mechanisms: maintenance of stemness through ID1 activity and enhanced DNA repair through MGMT and ATM upregulation. Evidence from patient-derived GSC lines, in vivo xenograft models, and gene expression profiling of primary GBM specimens.

**Atomic biological processes**
- BMP-SMAD transcriptional signaling. Genes: BMP6
  - [15]: BMP and TGF-β signaling define divergent molecular identities in glioblastoma; BMP pathway activation through pSmad1 marks relatively quiescent GSCs; BMP treatment inhibits cell proliferation through SMAD-mediated transcription
- ID protein-mediated differentiation suppression. Genes: BMP6
  - [15]: BMP pathway inhibits proliferation through ID1 modulation; ID1 knockdown impairs cell invasion and increases survival in glioma models; BMP-mediated ID1 activity suppresses differentiation while maintaining stemness
- DNA repair pathway activation. Genes: BMP6
  - [15]: BMP4 treatment increases MGMT expression and activates ATM serine/threonine kinase; BMP pathway activation confers relative resistance to radiation and temozolomide through enhanced DNA repair

**Atomic cellular components**
- BMP receptor-SMAD signaling complex. Genes: BMP6
  - [15]: BMP ligands bind serine-threonine kinase receptors to phosphorylate R-SMADs; phosphorylated SMAD1/5/8 (pSmad1) localizes to nucleus and cooperates with co-factors to activate target genes

**Required genes (not in input)**
- Genes: BMPR1A, BMPR1B, BMPR2, SMAD1, SMAD5, SMAD8, SMAD4, ID1, ID2, ID3, ID4, MGMT, ATM, SIX1, SNAIL, SNAIL2
  - [15]: BMP receptor signaling through SMAD1/5/8-SMAD4 complex; ID proteins act downstream as transcriptional effectors suppressing differentiation; MGMT and ATM mediate therapy resistance

**Program citations**
- [15]: BMP and TGF-β signaling define divergent GSC identities; BMP pathway marks quiescent stem cells with resistance to radiation and chemotherapy
- [18]: BMP developmental pathway deregulation contributes to glioblastoma tumorigenicity through ID protein effects on stem cell properties

## Bibliography
1. Yoshiro M, Shintaro Y, Akira K, Chisei S, Hiroyuki M, Naohiro Y, et al.. Nonsense mutation in . Neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6598815/
2. Dalal AA-M, Basel HA, Petra P, Heymut O. Novel pathogenic variants of . Frontiers in genetics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/39045318/
3. Bryony B, Heymut O, George BW, Gregory JP, K KP, Elspeth AB, et al.. Consensus nomenclature for dyneins and associated assembly factors.. The Journal of cell biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8754002/
4. Available from: https://www.proteinatlas.org/search/FAP
5. Nora D, Julia D, Anais S, Alexandra H, Gudrun G, Nico L, et al.. Generation of two human induced pluripotent stem cell lines (MHHi017-A, MHHi017-B) from a patient with primary ciliary dyskinesia carrying a homozygous mutation (c.7915C > T [p.Arg2639*]) in the DNAH5 gene.. Stem cell research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/32470793/
6. Available from: https://maayanlab.cloud/Harmonizome/gene_set/testis/BioGPS+Mouse+Cell+Type+and+Tissue+Gene+Expression+Profiles
7. Hyejin K, Ji-Sook H, Bogman L, Jinpyo H, Soojin L. Newly Identified Cancer-Associated Role of Human Neuronal Growth Regulator 1 (NEGR1).. Journal of Cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4107236/
8. Lucas CB, Gabriel CM, Manoela H, Valéria PF. Identification of established and novel extracellular matrix components in glioblastoma as targets for angiogenesis and prognosis.. Neurogenetics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/38775886/
9. Wenchao Z, Susan QK, Zhi H, William F, Xiaoguang F, Jeremy P, et al.. Periostin secreted by glioblastoma stem cells recruits M2 tumour-associated macrophages and promotes malignant growth.. Nature cell biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4312504/
10. Yoo A, Lee S. Neuronal growth regulator 1 may modulate interleukin-6 signaling in adipocytes. Frontiers in Molecular Biosciences [Internet]. 2023Apr28;10. Available from: https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2023.1148521/full
11. Guo KS, Brodsky AS. Tumor collagens predict genetic features and patient outcomes. npj Genomic Medicine [Internet]. 2023Jul6;8(1). Available from: https://www.nature.com/articles/s41525-023-00358-9
12. Shang Y, Liang Y, Zhang B, Wu W, Peng Y, Wang J, et al.. Periostin-mediated activation of NF-κB signaling promotes tumor progression and chemoresistance in glioblastoma. Scientific Reports [Internet]. 2025Apr22;15(1). Available from: https://www.nature.com/articles/s41598-025-92969-8
13. Zhe P, Kuo-Chieh L, Amber K, Gabriell E, Hoau-Yan W. Pathway analysis of glutamate-mediated, calcium-related signaling in glioma progression.. Biochemical pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
14. Rafael B, Matheus D, Osvaldo M, Jurandir MRF, Rafael R, Marcelo ACF, et al.. Gene Expression of GABA. Brain sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969028/
15. Sachdeva R, Wu M, Johnson K, Kim H, Celebre A, Shahzad U, et al.. BMP signaling mediates glioma stem cell quiescence and confers treatment resistance in glioblastoma. Scientific Reports [Internet]. 2019Oct10;9(1). Available from: https://www.nature.com/articles/s41598-019-51270-1
16. Wan Z, Sun R, Liu Y-W, Li S, Sun J, Li J, et al.. Targeting metabotropic glutamate receptor 4 for cancer immunotherapy. Science Advances [Internet]. 2021Dec10;7(50). Available from: https://www.science.org/doi/10.1126/sciadv.abj4226
17. Barron T, Yalçın B, Su M, Byun YG, Gavish A, Shamardani K, et al.. GABAergic neuron-to-glioma synapses in diffuse midline gliomas. Nature [Internet]. 2025Feb19;639(8056). Available from: https://www.nature.com/articles/s41586-024-08579-3
18. Jeongwu L, Myung JS, Kevin W, Nicholas MD, Aiguo L, Chui HC, et al.. Epigenetic-mediated dysfunction of the bone morphogenetic protein pathway inhibits differentiation of glioblastoma-initiating cells.. Cancer cell [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/18167341/
19. Jamie-Lee P, Naomi A, Panimaya JM, Terrance GJ. ErbB4 in the brain: Focus on high grade glioma.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9471956/
20. Jonathan BL, Jason BL, Yuping DL, Joseph DD, Winward C, Dorina V, et al.. Glioblastoma-Derived IL6 Induces Immunosuppressive Peripheral Myeloid Cell PD-L1 and Promotes Tumor Growth.. Clinical cancer research : an official journal of the American Association for Cancer Research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6571046/
21. Daubon T, Léon C, Clarke K, Andrique L, Salabert L, Darbo E, et al.. Deciphering the complex role of thrombospondin-1 in glioblastoma development. Nature Communications [Internet]. 2019Mar8;10(1). Available from: https://www.nature.com/articles/s41467-019-08480-y
22. Véronique D-T, Ivan B, Sophie V, Anne L, Claude-Alain M, Francis C, et al.. Differential distribution of erbB receptors in human glioblastoma multiforme: expression of erbB3 in CD133-positive putative cancer stem cells.. Journal of neuropathology and experimental neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3173752/
23. Available from: https://derisilab.ucsf.edu/pdfs/Glio.pdf
24. Chunxiao Q, Lei L, Jinqu H, Gang W, Jiyuan L, Shaowu O. Thrombospondin-1 is a prognostic biomarker and is correlated with tumor immune microenvironment in glioblastoma.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7681197/
25. Nicole MW, Tao S, Jingqin L, Robert CM, Patricia CP, Sara G, et al.. The cyclic AMP pathway is a sex-specific modifier of glioma risk in type I neurofibromatosis patients.. Cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4286430/
26. Miriam F-G, Alejandra C-L, David M-H, Margarita L-L, Ricardo G-R, Alejandro S, et al.. Role of the Ca2+ channel α2δ-1 auxiliary subunit in proliferation and migration of human glioblastoma cells.. PloS one [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9754164/
27. Shilpi P, Alex K, Thomas S, Hannes V, Leemor J-T, W RM, et al.. Chd5 requires PHD-mediated histone 3 binding for tumor suppression.. Cell reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3575599/
28. Nicole MW, Tao S, Joshua BR. Targeting brain tumor cAMP: the case for sex-specific therapeutics.. Frontiers in pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4516881/
29. Fernández-Gallardo M, Corzo-Lopez A, Muñoz-Herrera D, Leyva-Leyva M, González-Ramírez R, Sandoval A, et al.. Role of the Ca2+ channel α2δ-1 auxiliary subunit in proliferation and migration of human glioblastoma cells. PLOS ONE [Internet]. 2022Dec15;17(12). Available from: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0279186
30. Available from: https://aacrjournals.org/cancerres/article/84/5_Supplement_1/B014/734336/Abstract-B014-CHD5-suppresses-glioblastoma-by
31. M ML, A M. PI3Kinase signaling in glioblastoma.. Journal of neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3116122/
32. Available from: https://www.nature.com/articles/cddis2013433
33. Sun Y, Wang H. Revealing propionate metabolism-related genes in glioblastoma and investigating their underlying mechanisms. Frontiers in Oncology [Internet]. 2025Apr17;15. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1529369/full
34. Liu H, Tang T. MAPK signaling pathway-based glioma subtypes, machine-learning risk model, and key hub proteins identification. Scientific Reports [Internet]. 2023Nov4;13(1). Available from: https://www.nature.com/articles/s41598-023-45774-0
35. Sheng-Hua C, Yan-Bin M, Dong-Fu F, Hong Z, Zhi-An Z, Zhi-Qiang L, et al.. Upregulation of SATB1 is associated with the development and progression of glioma.. Journal of translational medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3492129/
36. Xuejing Z, Jaclyn C, Yapeng C, Qiming JW. Multifaceted Functions of Protein Kinase D in Pathological Processes and Human Diseases.. Biomolecules [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005150/
37. Xiaoguang F, Zhi H, Wenchao Z, Qiulian W, Andrew ES, Gaoliang O, et al.. The zinc finger transcription factor ZFX is required for maintaining the tumorigenic potential of glioblastoma stem cells.. Stem cells (Dayton, Ohio) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/24831540/
38. Alice F, Massimo G, Isabella R. Leucine-rich repeat kinase 2-related functions in GLIA: an update of the last years.. Biochemical Society transactions [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33960369/
39. Simon M, Dmitri S, Caren Z, Vanessa F, Astrid K, Robin H, et al.. Migration pattern, actin cytoskeleton organization and response to PI3K-, mTOR-, and Hsp90-inhibition of glioblastoma cells with different invasive capacities.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5542187/
40. Stefania S, Marco G, Valeria L, Ylenia M, Emanuela C, Annamaria A, et al.. The stem cell-associated transcription co-factor, ZNF521, interacts with GLI1 and GLI2 and enhances the activity of the Sonic hedgehog pathway.. Cell death & disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6763495/
41. Iannotta L, Fasiczka R, Favetta G, Zhao Y, Giusto E, Dall’Ara E, et al.. PAK6 rescues pathogenic LRRK2-mediated ciliogenesis and centrosomal cohesion defects in a mutation-specific manner. Cell Death &amp; Disease [Internet]. 2024Oct17;15(10). Available from: https://www.nature.com/articles/s41419-024-07124-4
42. Vanina DH, Aida K, Laura L, Sune M, Bjarne WK, Jussi PP, et al.. Multiple formin proteins participate in glioblastoma migration.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7391617/
43. Ti-Chun C, Wen-Jeng W, Wei-Ming L, Meng-Shin S, Yow-Ling S, Chien-Feng L. SLC14A1 prevents oncometabolite accumulation and recruits HDAC1 to transrepress oncometabolite genes in urothelial carcinoma.. Theranostics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33052246/
44. Igor FT, Valentina LK, Nathan L, Santosh K. Molecular mechanisms of OLIG2 transcription factor in brain cancer.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5288170/
45. Chia-Wei C, Yi-Chin C, Yin-Cheng H, Yi-Chuan C. EGR3 Promotes Glioblastoma Cell Growth with Upregulation of MYC and CDK1.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40649712/
46. Jing S, Ruili S, Xilan Y. Role of the human solute carrier family 14 member 1 gene in hypoxia-induced renal cell carcinoma occurrence and its enlightenment to cancer nursing.. BMC molecular and cell biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10024409/
47. Myers BL, Brayer KJ, Paez-Beltran LE, Villicana E, Keith MS, Suzuki H, et al.. Transcription factors ASCL1 and OLIG2 drive glioblastoma initiation and co-regulate tumor cell types and migration. Nature Communications [Internet]. 2024Nov28;15(1). Available from: https://www.nature.com/articles/s41467-024-54750-9
48. Chia-Wei C, Yi-Chin C, Yin-Cheng H, Yi-Chuan C. EGR3 Promotes Glioblastoma Cell Growth with Upregulation of MYC and CDK1.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12249872/
49. Sergey MI, Alexey AL, Olga AT. Analysis of transcription profiles for the identification of master regulators as the key players in glioblastoma.. Computational and structural biotechnology journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11832006/
50. Dongxin J, Yunqian L. Unraveling the immunosuppressive microenvironment of glioblastoma and advancements in treatment.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12119497/
51. Available from: https://rupress.org/jcb/article/223/6/e202401057/276615/N-cadherin-dynamically-regulates-pediatric-glioma
52. Available from: https://www.proteinatlas.org/ENSG00000155966-AFF2
53. Wenbo Z, Wanhong Z, Henghao W, Xinsheng H. Harnessing innate immunity against glioblastoma microenvironment.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12331708/
54. Carolina N, Ana SR, Ricardo T, Diogo SC, Joaquim R, Cláudia F, et al.. Cadherin Expression and EMT: A Focus on Gliomas.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533397/
55. Available from: https://rupress.org/jcb/article/206/2/151/37817/Targeting-potassium-channels-in-cancerPotassium
56. Khanppnavar B, Maier J, Herborg F, Gradisch R, Lazzarin E, Luethi D, et al.. Structural basis of organic cation transporter-3 inhibition. Nature Communications [Internet]. 2022Nov7;13(1). Available from: https://www.nature.com/articles/s41467-022-34284-8
57. Mario RF, MaLinda DH, Robert EL. Kinase suppressor of Ras 2 (KSR2) regulates tumor cell transformation via AMPK.. Molecular and cellular biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3430199/
58. Samar Y, Nisreen M, Mohamed S, Mohamad R, Dalal HH. Potassium Ion Channels in Glioma: From Basic Knowledge into Therapeutic Applications.. Membranes [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10144598/
59. Qingbei L, Shiling X, Yunda W, Haocong W, Didong X. Expression and clinical significance of organic cation transporter family in glioblastoma multiforme.. Irish journal of medical science [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34080124/
60. Rossella DD, Rosa I, Laura R, Luca R, Maria AO, Emanuela S, et al.. Targeted inhibition of ubiquitin signaling reverses metabolic reprogramming and suppresses glioblastoma growth.. Communications biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9345969/
