# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: glioblastoma multiforme
- Tissue: brain

## Input Genes
SERPINE1, EMP1, SPOCD1, ARHGAP29, IL1R1, COL6A2, MYOF, F13A1, CXCL10, CHI3L1, MET, IL6, SAA2, BIRC3, MCTP2, ANGPTL4, ICAM1, CCN1, CAV1, APLN, FOSL1, SNTG2-AS1, TPD52L1, SAA4, KRT75, ... (111 total)

## Program: EMT-Driven Invasion Program
A coordinated gene program mediating epithelial-mesenchymal transition and cellular invasiveness in glioblastoma. This program includes transcriptional regulators (FOSL1, KLF5, NFATC2), extracellular matrix components and remodelers (SERPINE1, COL5A1, COL6A2, COL1A2, FN1, SMOC2, ITGBL1), and cell adhesion/migration effectors (EMP1, CAV1, MYOF, KANK4, ICAM1). The program drives mesenchymal identity, enhanced cell motility, and increased invasive capacity into surrounding brain tissue.

**Predicted impacts**
- Enhanced cell migration and invasiveness into brain parenchyma
- Increased mesenchymal identity with reduced epithelial markers
- Remodeling of focal adhesion architecture
- Facilitated ECM degradation and rearrangement
- Acquisition of stem-like properties
- Enhanced resistance to conventional therapies

**Evidence summary**
Multiple complementary lines of evidence support this program: (1) SERPINE1 is the most upregulated EMT gene in dispersive GBM cells and correlates with poor survival; (2) multiple collagen and adhesion molecules are coordinately expressed during mesenchymal transition; (3) FOSL1 directly controls mesenchymal gene expression including SERPINE1; (4) EMT transcription factors (FOSL1, KLF5, NFATC2) are upregulated in high-grade, invasive tumors.

**Atomic biological processes**
- transcriptional regulation of EMT. Genes: FOSL1, KLF5, NFATC2
  - [9]: FOSL1 controls mesenchymal transcriptional program and maintains EMT phenotype in GBM
  - [22]: KLF5 regulates EMT-related transcription factors and cell motility
  - [25]: NFATC2 associated with cancer progression and EMT processes
- extracellular matrix proteolysis and remodeling. Genes: SERPINE1, COL5A1, COL6A2, COL1A2, FN1, SMOC2, ITGBL1
  - [1]: SERPINE1 regulates ECM degradation via plasminogen activator system and cell-substrate adhesion
  - [5]: COL5A1 plays pivotal role in ECM remodeling and cell cytoskeleton regulation during metastasis
  - [33]: Comprehensive review of ECM components and their role in GBM invasion; collagen types I, V, VI and fibronectin critical for tumor progression
- cell adhesion and focal contact dynamics. Genes: ICAM1, CAV1, KANK4, MYOF
  - [1]: SERPINE1 regulates focal adhesion formation and cell-ECM interactions
  - [7]: ICAM-1 mediates cell-cell adhesion and macrophage-GBM interaction

**Atomic cellular components**
- focal adhesions. Genes: SERPINE1, KANK4
  - [1]: SERPINE1 controls focal adhesion dynamics during cell migration
- extracellular matrix. Genes: COL5A1, COL6A2, COL1A2, FN1, SMOC2, ITGBL1
  - [33]: ECM actively shapes GBM development and invasion

**Required genes (not in input)**
- Genes: TWIST1, SNAIL, SLUG, ZEB1, SMAD2, SMAD3, TGFB1
  - [46]: EMT master regulators including TWIST1, SNAIL, SLUG, and ZEB1 are upregulated in mesenchymal GBM

**Program citations**
- [1]: SERPINE1 identified as key regulator of GBM cell dispersal and invasion
- [5]: COL5A1 promotes GBM malignancy through EMT-related mechanisms
- [9]: FOSL1 controls mesenchymal GBM plasticity and aggressiveness
- [30]: Fibronectin expression determines distinct malignant glioma progressions via TGF-β-induced EMT
- [46]: EMT in GBM progression involves TGF-β, WNT/β-catenin, and transcription factors

## Program: Pro-Inflammatory Cytokine Signaling
A gene program centered on production and signaling of pro-inflammatory cytokines that drive GBM development and progression. This program includes IL-6, IL-8 (CXCL8), IL-1 receptor (IL1R1), IL-4 receptor (IL4R), leukemia inhibitory factor (LIF), and cardiotrophin-like cytokine factor 1 (CLCF1). These cytokines signal through receptors and downstream pathways (STAT3, NF-κB) to promote tumor cell proliferation, survival, and create an immunosuppressive microenvironment.

**Predicted impacts**
- Enhanced proliferation via STAT3 and NF-κB activation
- Increased cell survival and reduced apoptosis
- Promotion of immunosuppressive microenvironment
- Maintenance of cancer stem cell properties
- Enhanced angiogenesis through secondary signals
- Recruitment and polarization of myeloid cells

**Evidence summary**
Pro-inflammatory cytokines are markedly elevated in GBM specimens. IL-6 and IL-8 demonstrate the highest diagnostic relevance with approximately 3-fold higher probability of GBM development above threshold levels. These cytokines coordinate with each other through IL-1β-driven NF-κB amplification, creating a sustained inflammatory milieu. LIF and CLCF1 extend this program by directly supporting stemness and invasiveness while reprogramming immune cells toward suppressive functions.

**Atomic biological processes**
- IL-6 and IL-8 production and signaling. Genes: IL6, CXCL8
  - [4]: IL-6 and IL-8 are the most consistently elevated pro-inflammatory cytokines in GBM with highest diagnostic potential (RR = 2.923 and 3.151 respectively)
  - [18]: IL-6 and IL-8 participate in COX-2/PGE2 inflammatory cascade in GBM
- IL-1 receptor signaling and NF-κB activation. Genes: IL1R1, TNFAIP3
  - [4]: IL-1β binds IL-1R and activates NF-κB pathway, leading to upregulation of pro-inflammatory genes including IL-6 and IL-8
- LIF-mediated immunosuppression and stemness. Genes: LIF
  - [31]: LIF prevents GBM cell differentiation, increases cancer stem cell markers (CD133), and promotes TAM formation
- CLCF1-mediated cytokine signaling. Genes: CLCF1
  - [39]: CLCF1 (IL-6 superfamily member) promotes GBM cell proliferation, migration and invasion; serves as unfavorable prognostic marker

**Atomic cellular components**
- cytokine receptors (gp130, IL-4R, IL-1R). Genes: IL1R1, IL4R, CLCF1
  - [4]: IL-1R, IL-6R, IL-8R signaling is central to GBM cytokine-driven pathology

**Required genes (not in input)**
- Genes: STAT3, NFKB1, RELA, IL1B, TNF, IL10
  - [4]: STAT3 and NF-κB are downstream effectors of IL-1β, IL-6, and IL-8 signaling in GBM

**Program citations**
- [4]: Comprehensive profiling of cytokine changes in GBM; IL-6 and IL-8 as key pro-inflammatory mediators
- [10]: PTX3 regulation of pro-inflammatory cytokines in GBM microenvironment
- [31]: LIF as immunosuppressive factor promoting TAM formation and cancer stemness
- [39]: CLCF1 as unfavorable prognostic marker in GBM promoting proliferation

## Program: Angiogenesis and Vascular Signaling
A gene program driving tumor neovascularization through VEGF and apelin signaling pathways. This program includes VEGFA, APLN (apelin), CHI3L1, PTX3, and CLCF1. These genes promote endothelial cell proliferation, migration, and vascular formation, particularly under hypoxic conditions. The program creates the highly vascularized phenotype characteristic of GBM and enables nutrient delivery to support rapid tumor growth.

**Predicted impacts**
- Enhanced vascular density and complexity within tumor
- Increased oxygen and nutrient delivery to tumor core
- Facilitation of tumor expansion into surrounding brain
- Promotion of aberrant vascular morphology (tortuous, leaky vessels)
- Enhanced BBB disruption and vasogenic edema
- Promotion of vascular-associated tumor cell invasion

**Evidence summary**
GBM exhibits extensive neovascularization as a hallmark feature. VEGF is the canonical driver, highly expressed particularly in necrotic and hypoxic regions. APLN provides a complementary sprouting angiogenesis signal that is essential for tumor vascular patterning. CHI3L1 and PTX3 operate through inflammatory mechanisms to support vascular formation. The synergy of multiple angiogenic signals enables the dense, pathological vasculature characteristic of aggressive GBM.

**Atomic biological processes**
- VEGF-mediated endothelial proliferation and sprouting. Genes: VEGFA
  - [16]: VEGF is essential factor for angiogenesis in GBM; upregulated in necrotic regions; VEGF and VEGFR highly expressed in GBM tissues
  - [49]: Pseudopalisading cells in GBM secrete VEGF and IL-8 to promote angiogenesis
- apelin-mediated sprouting angiogenesis. Genes: APLN
  - [21]: APLN/APLNR signaling required for GBM sprouting angiogenesis; loss of APLN reduces vascular density and tumor growth; APLN co-expressed with VEGFA in hypoxic regions
- CHI3L1-mediated angiogenesis. Genes: CHI3L1
  - [17]: CHI3L1 exerts pro-angiogenic effect promoting tumor angiogenesis through vascular endothelial cells and maintaining vascular integrity; elevated serum levels in GBM
- PTX3-mediated inflammation-driven angiogenesis. Genes: PTX3
  - [10]: PTX3 regulates macrophage-associated tumor-promoting inflammation and angiogenesis in glioblastoma

**Atomic cellular components**
- endothelial cells and vascular structures. Genes: VEGFA, APLN, CHI3L1
  - [16]: VEGF targets endothelial cells and promotes vascular proliferation; abnormal GBM vasculature leads to BBB disruption
  - [21]: APLN expressed in endothelial tip cells during sprouting angiogenesis

**Required genes (not in input)**
- Genes: VEGFR1, VEGFR2, APLNR, NRP1, NRP2, FLT1, KDR
  - [16]: VEGF receptors (VEGFR1/2) required for VEGF-mediated endothelial signaling
  - [21]: APLNR required for apelin signaling in endothelial cells

**Program citations**
- [16]: HIF-1α and VEGF are potent biomarkers of GBM prognosis; VEGF upregulated in necrotic regions
- [21]: Apelin/APLNR signaling required for in vivo tumor angiogenesis and GBM growth
- [17]: CHI3L1 elevated in GBM serum; promotes tumor angiogenesis
- [49]: Pseudopalisades hyperexpress HIF-1 and secrete VEGF and IL-8 promoting angiogenesis

## Program: Immune Evasion and Checkpoint Activation
A gene program enabling GBM escape from anti-tumor immune surveillance through upregulation of checkpoint ligands, immunosuppressive factors, and immune cell reprogramming mechanisms. This program includes PD-L1 (CD274), IDO1, complement factor H (CFH), and chemokines (CXCL10, CXCL14, CXCL2). These genes create an immunosuppressive microenvironment through T cell exhaustion, regulatory T cell expansion, myeloid-derived suppressor cell recruitment, and complement inhibition.

**Predicted impacts**
- Impaired anti-tumor CD8+ T cell response
- Expansion of immunosuppressive regulatory T cells (Tregs)
- Increased immunosuppressive myeloid cell accumulation
- Enhanced complement resistance on tumor cell surface
- Reduced responsiveness to checkpoint inhibitor monotherapy
- Creation of immunosuppressive microenvironment resistant to immunotherapy

**Evidence summary**
GBM establishes robust immune evasion through multiple complementary mechanisms. PD-L1 expression directly drives Treg expansion and T cell exhaustion. IDO1 creates a tryptophan-depleted microenvironment that sustains immunosuppression. CFH provides complement evasion, a less-appreciated but critical immune escape mechanism. Coordinated chemokine signaling recruits immune cells but reprograms them toward immunosuppressive phenotypes. The convergence of these mechanisms explains the limited efficacy of single checkpoint inhibitor therapy in GBM.

**Atomic biological processes**
- PD-L1-mediated T cell exhaustion and Treg expansion. Genes: CD274
  - [24]: PD-L1 upregulation in GBM promotes Treg expansion and maintains immunosuppressive microenvironment; elevated CD274 mRNA correlates with increased FOXP3 and poor survival
- IDO1-mediated tryptophan depletion and immunosuppression. Genes: IDO1
  - [12]: IDO1 converts tryptophan to immunosuppressive kynurenines; high IDO1 expression correlates with poor outcomes and increased tumor grade; promotes T cell apoptosis and Treg expansion
- complement evasion via CFH. Genes: CFH
  - [36]: CFH inhibits complement-mediated immune responses; increased CFH and FHL-1 associated with poor GBM survival; prevents opsonization and C3d-mediated immune cell activation
- chemokine-mediated immune cell recruitment and polarization. Genes: CXCL10, CXCL14, CXCL2
  - [8]: CXCL family (CXCL9, CXCL10, CXCL11, CXCL14) enriched in high-risk IDH wild-type gliomas; promote immunocyte infiltration but in context of immunosuppressive microenvironment with high ICG expression

**Atomic cellular components**
- immune checkpoint molecule expression. Genes: CD274
  - [24]: PD-L1 highly expressed on GBM tumor cells and myeloid cells
- immunosuppressive enzyme production. Genes: IDO1
  - [12]: IDO1 rapidly induced in response to immune surveillance in cancer

**Required genes (not in input)**
- Genes: PDCD1, CTLA4, LAG3, TIM3, FOXP3, IL10, TGFB1, STAT3
  - [24]: PD-1 and other immune checkpoints on T cells are ligands for PD-L1
  - [12]: STAT3 and other signaling mediators downstream of immunosuppressive pathways

**Program citations**
- [24]: PD-L1 expression in GBM correlates with Treg expansion and poor prognosis
- [12]: IDO1 activation correlates with poor outcomes in GBM; immunotherapeutic targeting rationale
- [36]: CFH as innate immune checkpoint; overexpression associated with poor GBM survival
- [8]: CXCL family in high-risk gliomas with immunosuppressive microenvironment

## Program: Extracellular Matrix Proteolysis
A gene program controlling degradation and remodeling of extracellular matrix through multiple protease systems and their regulators. This program includes serine protease inhibitors and activators (SERPINE1, SAA1, SAA2, SAA4), metalloproteinase regulators (MYOF), and cross-linking enzymes (F13A1). These genes enable ECM degradation to facilitate tumor cell migration, invasion, and colonization of brain tissue.

**Predicted impacts**
- Increased ECM degradation facilitating invasion
- Enhanced migration through tissue barriers
- Facilitated epithelial-mesenchymal transition
- Increased availability of cryptic ECM epitopes
- Enhanced protease-mediated release of growth factors
- Support for basement membrane penetration

**Evidence summary**
GBM invasiveness critically depends on ECM proteolysis. SERPINE1, the most upregulated EMT gene in dispersive cells, coordinates with the plasminogen/plasmin system to degrade ECM. SAA proteins directly induce MMP expression and activate proteases for ECM remodeling. MYOF regulates the trafficking of proteases and their secretion. F13A1 cross-links fibrin to create protease-resistant matrix structures. The coordinate upregulation of these genes enables the ECM remodeling required for GBM invasion.

**Atomic biological processes**
- plasminogen activator system regulation. Genes: SERPINE1
  - [1]: SERPINE1 (PAI-1) is key regulator of plasminogen activator system; has central role in ECM degradation and remodeling; facilitates cell migration
- matrix metalloproteinase regulation and activation. Genes: SAA1, SAA2, SAA4, MYOF
  - [27]: SAA induces expression of MMP-2 and MMP-9; rSAA activates plasminogen and MMPs for ECM degradation
  - [41]: MYOF regulates MMP production and secretion affecting cancer cell invasion
- fibrin cross-linking and matrix stabilization. Genes: F13A1
  - [42]: F13A1 (Factor XIII-A) stabilizes fibrin networks; may regulate fibrin turnover in extravascular tumor microenvironment; TAM-derived F13A1 supports micrometastasis survival

**Atomic cellular components**
- serine protease inhibitors and activators. Genes: SERPINE1
  - [1]: SERPINE1 is member of serine proteinase inhibitor superfamily
- membrane trafficking and vesicular transport. Genes: MYOF
  - [41]: MYOF regulates membrane trafficking and receptor recycling affecting MMP secretion

**Required genes (not in input)**
- Genes: MMP2, MMP9, PLASMIN, PLG, PLAU, PLAT
  - [27]: MMP-2 and MMP-9 are direct targets of SAA-mediated induction

**Program citations**
- [1]: SERPINE1 as key regulator of ECM degradation and remodeling in GBM
- [27]: SAA induces MMP-2 and MMP-9 expression and activates ECM-degrading enzymes
- [33]: ECM actively shapes GBM tumor development through proteolytic remodeling
- [42]: F13A1 stabilizes fibrin networks in tumor microenvironment

## Program: Glioma Stem Cell Maintenance
A gene program sustaining cancer stem cell properties including self-renewal, pluripotency, and differentiation resistance. This program includes transcriptional regulators (HMGA2, KLF5, NFATC2), anti-apoptotic factors (BAG3, BIRC3), stem cell growth factors (LIF, ANGPTL4), and markers of stemness. These genes maintain the pool of tumor-initiating cells resistant to therapy and responsible for tumor recurrence.

**Predicted impacts**
- Enhanced self-renewal capacity of tumor-initiating cells
- Maintenance of pluripotency-related gene expression
- Increased resistance to differentiation signals
- Enhanced tumorigenicity in in vivo models
- Resistance to conventional chemotherapy and radiation
- Promotion of tumor recurrence and relapse

**Evidence summary**
GBM contains a population of cancer stem cells (GSCs) that drive tumor initiation, progression, and resistance to therapy. HMGA2 is elevated in the majority of primary GBMs and is required for GSC clonogenicity and in vivo tumor formation. LIF directly promotes stemness by increasing CD133 expression and preventing differentiation. ANGPTL4 induces GSC enrichment through activation of EGFR and downstream signaling. BAG3 and BIRC3 provide anti-apoptotic signals maintaining stem cell survival. KLF5 integrates multiple stemness-related processes. The coordinate expression of these factors establishes a self-renewal program resistant to differentiation.

**Atomic biological processes**
- transcriptional regulation of stemness. Genes: HMGA2, KLF5, NFATC2
  - [19]: HMGA2 mediates motility and self-renewal in GBM stem cells; increased in CD133+ GSC versus CD133- cells; promotes clonogenicity and invasion
  - [22]: KLF5 regulates stemness, proliferation, and migration; promotes cancer stem cell maintenance
- LIF-mediated stem cell self-renewal. Genes: LIF
  - [31]: LIF prevents GBM cell differentiation and increases cancer stem cell marker CD133; promotes stemness via STAT3 signaling
- ANGPTL4-mediated GSC enrichment. Genes: ANGPTL4
  - [34]: ANGPTL4 induces GSC enrichment characterized by BMI-1 and SOX2 expression; promotes stemness via EGFR/AKT/4E-BP1 cascade
- anti-apoptotic signaling in stem cells. Genes: BAG3, BIRC3
  - [23]: BAG3 promotes GBM cell survival and prevents BAX translocation to mitochondria

**Atomic cellular components**
- stem cell transcriptional machinery. Genes: HMGA2, KLF5
  - [19]: HMGA2 is transcriptional modulator mediating stem cell self-renewal

**Required genes (not in input)**
- Genes: OCT4, SOX2, NANOG, BMI1, STAT3, AKT1
  - [47]: OCT4, SOX2, and NANOG are pluripotency factors expressed in GBM stem cells
  - [34]: BMI-1 and SOX2 are markers of ANGPTL4-induced stem cell enrichment

**Program citations**
- [19]: HMGA2 promotes GBM stemness, invasion, and tumorigenicity
- [31]: LIF promotes cancer stem cell maintenance in GBM
- [34]: ANGPTL4 induces stemness and drug resistance in GBM
- [23]: BAG3 overexpressed in GBM and promotes cell survival

## Program: Hypoxia Adaptation and Response
A gene program enabling GBM survival and proliferation in low-oxygen microenvironment through metabolic reprogramming and stress response mechanisms. This program includes hypoxia-regulated genes (NDRG1, IDO1), metabolic enzymes, and cell cycle regulators. These genes allow tumor cells to adapt to severe hypoxia in the tumor core and pseudopalisading regions.

**Predicted impacts**
- Survival in severely hypoxic tumor core (0.1-1% oxygen)
- Increased tolerance to oxidative stress
- Maintenance of proliferation despite oxygen deprivation
- Enhanced invasiveness at tumor periphery
- Transition between proneural and mesenchymal states
- Support for pseudopalisade formation and function

**Evidence summary**
Hypoxia is a defining feature of GBM microenvironment, particularly in the tumor core and pseudopalisading regions. NDRG1 is a key hypoxia-responsive gene upregulated in GBM under oxygen deprivation. NDRG1 expression correlates inversely with GBM patient survival and is associated with more aggressive, mesenchymal phenotype. IDO1 is rapidly induced by interferon gamma in response to immune surveillance and operates in hypoxic conditions. The hypoxia response program enables GBM cells to survive and proliferate in regions where normal neural tissue would undergo apoptosis.

**Atomic biological processes**
- hypoxia-inducible gene expression. Genes: NDRG1
  - [26]: NDRG1 is hypoxia-inducible gene upregulated under oxygen deprivation; regulated by HIF-1α through multiple binding sites; increased expression in GBM hypoxic regions
- metabolic adaptation to hypoxia. Genes: IDO1
  - [50]: Glucose uptake via GLUT1 enhanced through PI3K/AKT and HIF pathways; HIF regulates glycolytic enzyme expression for hypoxic survival

**Atomic cellular components**
- hypoxia response elements in gene promoters. Genes: NDRG1
  - [26]: NDRG1 gene contains three HIF-1 binding sites enabling HIF-dependent transcription

**Required genes (not in input)**
- Genes: HIF1A, HIF2A, EGLN1, PHD2
  - [16]: HIF-1α and HIF-2α are master regulators of hypoxic gene expression including VEGF
  - [26]: HIF-1α directly regulates NDRG1 transcription

**Program citations**
- [26]: NDRG1 is critical for GBM survival under hypoxic stress
- [16]: HIF-1α regulates hypoxic gene expression in GBM
- [50]: Metabolic rewiring supports GBM survival in hypoxic tumor microenvironment
- [49]: Pseudopalisades are severely hypoxic regions with HIF-1 overexpression

## Program: Macrophage/Microglia Reprogramming
A gene program recruiting and reprogramming myeloid cells toward tumor-supporting phenotypes. This program includes toll-like receptor signaling (TLR2), chemokines (CXCL10, CXCL14, CXCL2), acute-phase proteins (SAA1, SAA2, SAA4, PTX3), and cell adhesion molecules (ICAM1, CCN1). These genes create a chemotactic gradient and provide signals that convert infiltrating macrophages and microglia into immunosuppressive, pro-tumoral cells.

**Predicted impacts**
- Increased infiltration of macrophages and microglia into tumor
- Conversion to immunosuppressive M2-like phenotype
- Enhanced production of pro-tumoral cytokines
- Increased tumor-associated macrophage (TAM)-mediated angiogenesis
- Reduced CD8+ T cell activation and function
- Enhanced tumor cell invasion and metastatic potential

**Evidence summary**
Glioblastoma-associated macrophages (GAMs) and microglia are the dominant immune cell population in GBM and actively support tumor growth. TLR2 activation is a key mechanism converting microglia to glioma-supportive phenotype with increased MT1-MMP expression. TLR2 knockout mice show dramatic reduction in tumor growth and improved survival. Chemokines CXCL10, CXCL14, and CXCL2 create a gradient recruiting myeloid cells. Acute-phase proteins (SAA, PTX3) directly activate macrophages and mediate inflammatory responses. ICAM-1 and CCN1 facilitate adhesive interactions between immune and tumor cells. The convergence of these signals transforms the macrophage/microglia population into tumor-supporting cells.

**Atomic biological processes**
- TLR2-mediated macrophage reprogramming. Genes: TLR2
  - [11]: TLR2 activation in microglia/macrophages converts them to glioma-supportive phenotype; increases MT1-MMP expression; TLR2 knockout significantly reduces tumor growth and increases survival
- chemokine-mediated immune cell recruitment. Genes: CXCL10, CXCL14, CXCL2
  - [8]: CXCL family chemokines enrich immunocytes in high-risk gliomas; CXCL10 serves as target for STAT3 inhibitors; modulates immune cell recruitment and polarization
- acute-phase protein signaling in immune cells. Genes: SAA1, SAA2, SAA4, PTX3
  - [27]: SAA induces chemotaxis and migration of immune cells; activates MMPs and inflammatory response
  - [10]: PTX3 mediates macrophage infiltration and polarization in GBM microenvironment
- cell adhesion-mediated immune-tumor interaction. Genes: ICAM1, CCN1
  - [7]: ICAM-1 mediates macrophage binding to GBM cells; VCAM-1 and ICAM-1 upregulated by EGFR activation

**Atomic cellular components**
- toll-like receptors. Genes: TLR2
  - [11]: TLR2 expressed on microglia and macrophages; activation drives pro-tumoral reprogramming
- chemokine receptors on myeloid cells. Genes: CXCL10, CXCL14, CXCL2
  - [8]: CXCL chemokines signal through CXCR receptors on immune cells

**Required genes (not in input)**
- Genes: CCL2, CCR2, CSF1, CSF1R, IL1B, TNF, IL10
  - [48]: CCL2-CCR2 axis critical for macrophage recruitment to GBM

**Program citations**
- [11]: TLR2 mediates microglia reprogramming to glioma-supportive phenotype
- [8]: CXCL family in myeloid cell recruitment and immunosuppressive microenvironment
- [27]: SAA induces immune cell chemotaxis and inflammatory activation
- [48]: GAMs undergo reprogramming in response to GBM-derived factors

## Program: Apoptosis Resistance and Survival Signaling
A gene program preventing programmed cell death and enabling survival under stress conditions through multiple anti-apoptotic mechanisms. This program includes inhibitor of apoptosis proteins (BIRC3, BAG3), TNF-regulated factors (TNFAIP3, TNFAIP2), and cell cycle checkpoint regulators (GADD45A). These genes suppress intrinsic and extrinsic apoptotic pathways while maintaining proliferative capacity.

**Predicted impacts**
- Resistance to intrinsic (mitochondrial) apoptosis pathway
- Reduced responsiveness to TNF-α and FAS ligand
- Enhanced survival under therapeutic stress
- Reduced sensitivity to chemotherapy and radiotherapy
- Increased cell proliferation despite damage signals
- Resistance to immunogenic cell death

**Evidence summary**
GBM cells exhibit enhanced resistance to apoptosis through multiple overlapping mechanisms. BIRC3 overexpression promotes higher-grade tumors with reduced survival. BAG3 is robustly expressed in astrocytomas and glioblastomas and its knockdown causes dramatic death of GBM cells through BAX-mediated apoptosis. TNFAIP2 knockdown induces immunogenic cell death, indicating this factor normally suppresses cell death pathways. GADD45A plays a protective role against temozolomide, suggesting DNA damage checkpoints are dysregulated. The combined action of these anti-apoptotic factors enables GBM cells to survive the hypoxic, nutrient-poor, inflammatory tumor microenvironment and tolerate cytotoxic therapies.

**Atomic biological processes**
- inhibitor of apoptosis (IAP) signaling. Genes: BIRC3
  - [13]: BIRC3 (cIAP2) overexpression promotes higher grade glioma and significantly reduces tumor-free survival in mice
- BAG3-HSP70-BAX anti-apoptotic complex formation. Genes: BAG3
  - [23]: BAG3 forms complex with HSP70 and BAX preventing BAX translocation to mitochondria; BAG3 knockdown results in dramatic decrease in cell proliferation and increased apoptosis; BAG3 silencing sensitizes GBM to cell death
- TNF-mediated survival signaling. Genes: TNFAIP3, TNFAIP2
  - [35]: TNFAIP2 knockdown induces immunogenic cell death in GBM; targeting TNFAIP2 combined with anti-PD-1 improves survival
- DNA damage response and cell cycle arrest. Genes: GADD45A
  - [45]: GADD45A induced by DNA damage; contributes to p53 stabilization; plays protective role against temozolomide in GBM

**Atomic cellular components**
- mitochondrial membrane and apoptosome. Genes: BAG3, BIRC3
  - [23]: BAX localization to mitochondria is critical step in intrinsic apoptosis; BAG3-HSP70 complex prevents this translocation

**Required genes (not in input)**
- Genes: BAX, BAK, PUMA, BIM, PTEN, TP53, CASP9
  - [23]: BAX is critical pro-apoptotic factor whose translocation is prevented by BAG3-HSP70 complex

**Program citations**
- [23]: BAG3 as survival factor in GBM; target for sensitizing tumors to therapy
- [13]: BIRC3 promotes high-grade glioma and reduces tumor-free survival
- [35]: TNFAIP2 knockdown induces immunogenic cell death in GBM

## Program: Growth Factor and Receptor Signaling
A gene program coordinating mitogenic signaling through multiple growth factor receptors and their downstream effectors. This program includes receptor tyrosine kinases (MET, AXL), their ligands, and signaling molecules (SPP1, IL4R). These genes activate phosphoinositide-3-kinase/AKT/mTOR and mitogen-activated protein kinase/ERK pathways driving proliferation and survival.

**Predicted impacts**
- Enhanced proliferation via PI3K/AKT and MAPK/ERK pathways
- Increased cell survival and apoptosis resistance
- Enhanced migration and invasion
- Increased sensitivity to growth factors
- Sustained tumorigenic signaling independent of EGFR
- Potential escape from EGFR-targeted therapies

**Evidence summary**
GBM exhibits autocrine/paracrine growth factor signaling through multiple receptor tyrosine kinases beyond EGFR. HGF/MET signaling is active in GBM and predicts sensitivity to MET inhibition. AXL inhibition reduces GBM growth both in culture and in vivo. SPP1 (osteopontin) promotes tumor growth through ERK/MAPK pathway. These alternative growth factor pathways may contribute to resistance against single-target therapies and drive continued proliferation when EGFR is inhibited.

**Atomic biological processes**
- HGF/MET autocrine signaling. Genes: MET
  - [6]: HGF autocrine activation in GBM bears activated MET signaling pathway that predicts sensitivity to MET inhibitors
- AXL receptor tyrosine kinase signaling. Genes: AXL
  - [14]: AXL inhibition with BMS-777607 reduces GBM growth, migration, and invasion both in vitro and in vivo
- SPP1 (osteopontin)-mediated growth signaling. Genes: SPP1
  - [15]: Osteopontin (SPP1) promotes primary tumor growth through ERK/MAPK signaling pathway
- IL-4 receptor signaling. Genes: IL4R
  - [4]: IL-4 and IL-4R involved in cytokine signaling that affects tumor microenvironment

**Atomic cellular components**
- receptor tyrosine kinases. Genes: MET, AXL
  - [6]: MET is receptor tyrosine kinase activated by HGF

**Required genes (not in input)**
- Genes: HGF, GAS6, PI3K, AKT, MAPK, ERK1, ERK2
  - [6]: HGF is ligand for MET receptor

**Program citations**
- [6]: HGF/MET autocrine signaling in GBM with therapeutic implications
- [14]: AXL inhibition reduces GBM growth and invasiveness
- [15]: SPP1-mediated tumor growth through ERK/MAPK signaling

## Program: Transcriptional Master Regulation
A gene program establishing core transcriptional networks governing GBM phenotype through master transcription factors and their regulatory complexes. This program includes FOSL1 (AP-1 family), KLF5 (zinc finger family), NFATC2 (calcineurin-dependent), and associated regulatory proteins (RCAN2). These transcription factors control chromatin accessibility and activate large cohorts of target genes driving mesenchymal identity and stemness.

**Predicted impacts**
- Coordinate regulation of large transcriptional programs
- Maintenance of mesenchymal gene signature
- Control of chromatin accessibility at key loci
- Integration of multiple signaling inputs into transcriptional response
- Establishment of GBM subtype identity
- Resistance to differentiation signals

**Evidence summary**
Master transcription factors establish the transcriptional landscape defining GBM phenotype. FOSL1/FRA-1 is an AP-1 family member that directly controls mesenchymal gene signature including SERPINE1, ITGA3, ITGA5, and TNC. FOSL1 acts as a pioneer factor regulating chromatin accessibility at mesenchymal genes. KLF5 integrates multiple signals to control stemness, proliferation, and angiogenesis. NFATC2 is dysregulated in GBM and associates with cancer progression. RCAN2 modulates calcineurin-NFAT signaling. These transcriptional regulators form an integrated network controlling the mesenchymal, stem-like phenotype of aggressive GBM.

**Atomic biological processes**
- AP-1 transcriptional control of EMT and stemness. Genes: FOSL1
  - [9]: FOSL1/FRA-1 controls mesenchymal transcriptional program and GBM plasticity; deletion causes closing of AP-1/2 TF binding sites and opening of lineage-specific TF sites; FOSL1 deletion reduces stemness and tumorigenicity
- KLF5-mediated stemness and angiogenesis. Genes: KLF5
  - [22]: KLF5 regulates pluripotency, proliferation, migration; promotes GBM angiogenesis by inducing AGGF1
- NFAT-dependent immune and survival signaling. Genes: NFATC2
  - [25]: NFATC2 associated with GBM progression; dysregulation in multiple cancers including glioblastoma
- RCAN-mediated calcineurin regulation. Genes: RCAN2
  - [38]: RCAN1-4 inhibits NF-κB activity and growth of human malignant glioma cells; RCAN inhibits calcineurin-NFAT pathway

**Atomic cellular components**
- chromatin regulatory complexes. Genes: FOSL1
  - [9]: FOSL1/FRA-1 acts as pioneer factor controlling chromatin accessibility at target genes

**Required genes (not in input)**
- Genes: SMAD2, SMAD3, SMAD4, TEAD4, HCF1, BRD4
  - [9]: FOSL1 interacts with co-factors to regulate transcription
  - [22]: KLF5 interacts with multiple transcriptional co-regulators

**Program citations**
- [9]: FOSL1 controls GBM plasticity through chromatin remodeling and mesenchymal transcriptional control
- [22]: KLF5 as key transcription factor in cancer including GBM
- [25]: NFAT proteins in GBM progression

## Program: Inflammatory Lipid Mediator Signaling
A gene program centered on production and signaling of arachidonic acid-derived inflammatory mediators, particularly prostaglandins. This program includes cyclooxygenase-2 (PTGS2), its target prostaglandin E2 (PGE2), and downstream signaling through EP receptors. These genes create a pro-inflammatory microenvironment promoting tumor growth and therapeutic resistance.

**Predicted impacts**
- Increased local PGE2 concentration in tumor microenvironment
- Enhanced GBM cell proliferation via EP1 receptor
- Increased GBM cell survival and radiation resistance via EP2 and EP4
- Enhanced GBM cell migration
- Maintenance of cancer stem cell self-renewal
- Promotion of angiogenesis and immunosuppression

**Evidence summary**
The COX-2/PGE2 inflammatory axis is elevated in most human glioblastomas and contributes to tumor development and progression. COX-2 induction is particularly high in recurrent tumors, suggesting correlation with malignancy. Microglia express COX-2 and produce PGE2 in response to glioma-derived factors. PGE2 acts through multiple EP receptors on GBM cells with distinct functional outcomes: EP1 promotes proliferation, EP2 and EP4 promote survival and radiation resistance. PGE2 also promotes cancer stem cell maintenance and angiogenesis. Generic COX-2 inhibitors have shown limited efficacy in GBM likely due to broad off-target effects, suggesting more selective targeting of PGE2 terminal synthases or EP receptors as therapeutic strategies.

**Atomic biological processes**
- COX-2/PGE2 inflammatory cascade. Genes: PTGS2
  - [18]: Elevated COX-2 and associated inflammation contribute to GBM development; mPGES-1 functionally coupled to COX-2 for PGE2 synthesis; COX-2 expression higher in recurrent grade II gliomas
- PGE2-mediated EP receptor signaling. Genes: PTGS2
  - [18]: EP1 selective antagonists decrease GBM proliferation; EP2 agonists enhance GBM survival after radiation; EP4 activation induces Id1 and promotes radiation resistance

**Atomic cellular components**
- cyclooxygenase-2 enzyme. Genes: PTGS2
  - [18]: COX-2 (PTGS2) induced in response to inflammatory stimuli in GBM

**Required genes (not in input)**
- Genes: PGES, PTGES, PTGES2, EP1, EP2, EP4
  - [18]: mPGES-1 (PTGES) functionally coupled to COX-2 for PGE2 synthesis; EP1-EP4 receptors mediate PGE2 effects

**Program citations**
- [18]: COX-2/PGE2 signaling as alternative therapeutic target for GBM beyond COX-2 inhibition
- [4]: IL-1β upregulates COX-2 expression in GBM inflammation

## Program: Cellularity and Structural Organization
A gene program involving structural proteins and organizational factors contributing to GBM cellularity and architectural features. This program includes ribosomal proteins (RPS5, RPS18, RPS27), cell cycle regulators, and developmental morphogens (SLIT3). These genes support basic cellular infrastructure and mass while also modulating cell behavior.

**Predicted impacts**
- Enhanced protein synthesis capacity
- Increased ribosomal biogenesis
- Support for rapid proliferation
- Potentially altered cell morphology and migration
- Modified developmental signaling

**Evidence summary**
Ribosomal proteins are components of the translation machinery required for protein synthesis. GBM cells have dramatically elevated protein synthesis rates to support rapid proliferation and biosynthesis. Elevated ribosomal protein expression likely reflects the high translational demand of these tumors. SLIT3 is a developmental morphogen involved in axon guidance and cell migration; its dysregulation in GBM may contribute to aberrant cell migration patterns. These factors represent the basic cellular machinery and organizational principles underlying GBM expansion.

**Atomic biological processes**
- protein synthesis and ribosome biogenesis. Genes: RPS5, RPS18, RPS27
  - [50]: Ribosomal proteins contribute to high protein synthesis rates required for rapid GBM cell proliferation
- developmental morphogen signaling. Genes: SLIT3
  - [46]: SLIT proteins involved in developmental pathways; dysregulation affects cell migration and invasion

**Atomic cellular components**
- ribosome and translational machinery. Genes: RPS5, RPS18, RPS27
  - [50]: Enhanced protein synthesis machinery supports biosynthetic demands of rapidly proliferating GBM

**Required genes (not in input)**
- Genes: RPTOR, MTOR, TOP1

**Program citations**
- [50]: Metabolic rewiring in GBM includes enhanced protein synthesis

## Program: Metabolic Adaptation and Nutrient Sensing
A gene program enabling GBM cells to survive and proliferate in nutrient-poor, hypoxic tumor microenvironment through metabolic flexibility and nutrient scavenging. This program includes amino acid metabolism genes (IDO1, kynurenine pathway), lipid-handling genes (GPD1, DHRS3, LRAT), and nutrient transporters (SLC10A6, GPC5). These genes allow metabolic switching and nutrient acquisition to sustain tumor growth.

**Predicted impacts**
- Enhanced survival in nutrient-deprived microenvironment
- Increased biosynthetic capacity for rapid proliferation
- Metabolic flexibility enabling adaptation to regional microenvironmental variations
- Simultaneous immunosuppression through tryptophan depletion
- Acquisition of lipids for membrane biogenesis and signaling
- Reduced dependence on exogenous nutrient availability

**Evidence summary**
GBM exhibits extensive metabolic rewiring enabling survival in the nutrient-poor, hypoxic tumor microenvironment. Tryptophan metabolism via IDO1 simultaneously provides metabolic fuel and creates immunosuppression through kynurenine production. Lipid metabolism is enhanced, particularly at the invasive tumor margin where EGFR/AKT signaling is active. Glucose transporters are upregulated through PI3K/AKT, enabling increased glycolysis. Alternative amino acid pathways (glutamine, arginine) become dominant under hypoxic conditions. This metabolic adaptation program is essential for GBM progression and therapeutic resistance.

**Atomic biological processes**
- tryptophan catabolism and amino acid metabolism. Genes: IDO1
  - [12]: IDO1 converts tryptophan to immunosuppressive kynurenines; provides metabolic advantage while creating immunosuppressive microenvironment
  - [50]: Glutamine and tryptophan metabolism upregulated in GBM for metabolic flexibility
- lipid metabolism and biosynthesis. Genes: GPD1, DHRS3, LRAT
  - [50]: Lipid synthesis upregulated at tumor leading edge via EGFR/AKT pathway; PTEN-deficient tumors show altered lipid droplet accumulation
- nutrient transport and scavenging. Genes: SLC10A6, GPC5
  - [50]: Glucose transporters upregulated via PI3K/AKT pathway; alternative nutrient pathways activated in hypoxic regions

**Atomic cellular components**
- metabolic enzymes and transporters. Genes: IDO1, GPD1, DHRS3, LRAT
  - [50]: Enhanced metabolic enzyme expression supports biosynthetic demands in nutrient-poor microenvironment

**Required genes (not in input)**
- Genes: GLUT1, GLUT3, LDHA, PKM, GLS1, ASNS
  - [50]: Glucose transporters and glycolytic enzymes critical for GBM metabolic reprogramming

**Program citations**
- [50]: Comprehensive analysis of metabolic rewiring in GBM including glycolysis, glutamine, and tryptophan metabolism
- [12]: IDO1 activation in cancer metabolism and immunosuppression

## Program: DNA Damage Response and Genomic Stability
A gene program responding to DNA damage and maintaining genomic stability under therapeutic and oxidative stress. This program includes DNA damage-inducible genes (GADD45A), cell cycle checkpoints (RRAD, NPR3), and oxidative stress responses. These genes enable GBM cells to survive DNA-damaging therapies and maintain proliferation despite accumulated genomic alterations.

**Predicted impacts**
- Enhanced tolerance of DNA damage from radiation and chemotherapy
- Continued proliferation despite checkpoint signals
- Maintenance of genomic stability despite accumulated mutations
- Reduced sensitivity to temozolomide
- Potential development of therapeutic resistance

**Evidence summary**
GBM cells develop resistance to DNA-damaging therapies through altered DNA damage response mechanisms. GADD45A protects GBM cells from temozolomide-induced death by stabilizing p53. Checkpoint control genes are dysregulated, enabling continued proliferation despite DNA damage signals. This allows accumulation of additional mutations that may drive further tumor progression while simultaneously conferring resistance to genotoxic therapies.

**Atomic biological processes**
- DNA damage sensing and p53 response. Genes: GADD45A
  - [45]: GADD45A induced by DNA damage; contributes to p53 stabilization; plays protective role against temozolomide-induced GBM cell death
- cell cycle checkpoint control. Genes: RRAD, NPR3
  - [50]: Cell cycle checkpoint genes dysregulated in GBM enabling continued proliferation despite DNA damage

**Atomic cellular components**
- DNA damage sensing machinery. Genes: GADD45A
  - [45]: GADD45A part of DNA damage response machinery

**Required genes (not in input)**
- Genes: TP53, ATM, ATR, CHEK2, MDM2
  - [45]: p53 is downstream target of GADD45A in DNA damage response

**Program citations**
- [45]: GADD45A plays protective role against temozolomide treatment in GBM

## Bibliography
1. Fidan S, Ahmet C, İlknur S-E, Nazli E, Alp E, Fırat U, et al.. Identification of . Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
2. Lifeng M, Zheng J, Jiwei W, Ning Y, Qichao Q, Wenjing Z, et al.. Epithelial membrane protein 1 promotes glioblastoma progression through the PI3K/AKT/mTOR signaling pathway.. Oncology reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6609345/
3. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5692520/
4. Pawel J, Piotr D, Marcin K, Edyta W-G, Barbara M, Agnieszka Z-L. Cytokine Profile in Development of Glioblastoma in Relation to Healthy Individuals.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671437/
5. Hsing-Fang T, Yu-Chan C, Chien-Hsiu L, Ming-Hsien C, Chi-Long C, Wen-Chiuan T, et al.. Type V collagen alpha 1 chain promotes the malignancy of glioblastoma through PPRC1-ESM1 axis activation and extracellular matrix remodeling.. Cell death discovery [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8548600/
6. Qian X, Robert B, Liang K, Julie K, Maria LA, Andrea W, et al.. Hepatocyte growth factor (HGF) autocrine activation predicts sensitivity to MET inhibition in glioblastoma.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3258605/
7. Yanhua Z, Weiwei Y, Kenneth A, Jie H, Zhimin L. Epidermal growth factor (EGF)-enhanced vascular cell adhesion molecule-1 (VCAM-1) expression promotes macrophage and glioblastoma cell interaction and tumor cell invasion.. The Journal of biological chemistry [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/24045955/
8. Zeyu W, Yuze L, Yuyao M, Hao Z, Ziyu D, Xun Z, et al.. The CXCL Family Contributes to Immunosuppressive Microenvironment in Gliomas and Assists in Gliomas Chemotherapy.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8482424/
9. Available from: https://elifesciences.org/articles/64846
10. Sarah AS, Alessio A, Ayomide ES, Giuseppe P, Fabiola DL, Emanuela E, et al.. Pentraxin 3: A Main Driver of Inflammation and Immune System Dysfunction in the Tumor Microenvironment of Glioblastoma.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11083335/
11. Katyayni V, Feng H, Min-Chi K, Petya BG, Frank S, Andreas P, et al.. Toll-like receptor 2 mediates microglia/brain macrophage MT1-MMP expression and glioma expansion.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3813418/
12. Hamed H, Mehrdad M, Ali AS, Mehryar HR. The immunosuppressive role of indoleamine 2, 3-dioxygenase in glioblastoma: mechanism of action and immunotherapeutic strategies.. Medical oncology (Northwood, London, England) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9206138/
13. Loyola VG, Tiffany D, Yuhui Y, Gregory NF, Ganiraju M, Arvind R, et al.. Analysis of the inhibitors of apoptosis identifies BIRC3 as a facilitator of malignant progression in glioma.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5355046/
14. Julia O, Robert T, Sören K, Josefine R, Irina K, Melina N, et al.. Inhibiting receptor tyrosine kinase AXL with small molecule inhibitor BMS-777607 reduces glioblastoma growth, migration, and invasion in vitro and in vivo.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4891090/
15. Rafael S, Nidhi N, Jingyi S, Anja S, Wilko T, Boyan KG, et al.. Increased Circulating Osteopontin Levels Promote Primary Tumour Growth, but Do Not Induce Metastasis in Melanoma.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10135562/
16. Dimitra PV, Panagiotis GD, Kerasia G, Antonios DB, Kyriaki A, Konstantina Z, et al.. Hypoxia-inducible factor 1alpha and vascular endothelial growth factor in Glioblastoma Multiforme: a systematic review going beyond pathologic implications.. Oncology research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11267112/
17. Ming-Cheng C, Chun-Tang C, Ping-Fang C, Ying-Cheng C. The Role of Chitinase-3-like Protein-1 (YKL40) in the Therapy of Cancer and Other Chronic-Inflammation-Related Diseases.. Pharmaceuticals (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10976000/
18. Jianxiong J, Jiange Q, Qianqian L, Zhi S. Prostaglandin E2 Signaling: Alternative Target for Glioblastoma?. Trends in cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5518646/
19. Harpreet K, Sabeen ZA, Lauren H, Marianne H-C, Isabella T, Xing-Gang M, et al.. The transcriptional modulator HMGA2 promotes stemness and tumorigenicity in glioblastoma.. Cancer letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
20. Franz K, Nina G, Joseph EQ, Lee-Ann VDV, Hongbo C, Pavel K, et al.. Tristetraprolin Limits Inflammatory Cytokine Production in Tumor-Associated Macrophages in an mRNA Decay-Independent Manner.. Cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4526390/
21. Anne F, Stefanie K, Raymond M, Josefine R, Frank LH, Roland EK. Apelin Controls Angiogenesis-Dependent Glioblastoma Growth.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7312290/
22. Yao L, Ceshi C. The roles and regulation of the KLF5 transcription factor in cancers.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
23. Michelina F, Luis DV, Kamel K, Renato F, Giosuè S, Vincenzo G, et al.. BAG3 protein is overexpressed in human glioblastoma and is a potential target for therapy.. The American journal of pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3124067/
24. Joseph D, Jonathan BL, Daniel O, Yuping L, Dorina V, Gurvinder K, et al.. The immune checkpoint protein PD-L1 induces and maintains regulatory T cells in glioblastoma.. Oncoimmunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5993506/
25. Mohadese M, Siti NMH, Khairul BAAN, Siti AZ, Ahmad A. Nuclear Factor of Activated T Cells (NFAT) Proteins as Targeted Molecules in Diseases: A Narrative Review.. Cureus [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11736229/
26. Yukiko N, Hiroshi I, Hiroki N, Takashi F, Fumitaka Y, Atsushi O, et al.. A Tumor Suppressor Gene, N-myc Downstream-Regulated Gene 1 (NDRG1), in Gliomas and Glioblastomas.. Brain sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9029626/
27. Franciele HK, Renata CA, Renato RM, Silvya SM-E, Ana C. Dual effect of serum amyloid A on the invasiveness of glioma cells.. Mediators of inflammation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3596950/
28. Shuli X, Eliot MR, John L. Sensitization of glioma cells to Fas-dependent apoptosis by chemotherapy-induced oxidative stress.. Cancer research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/15958570/
29. Wenqi C, Tianlu W, Juan F. From mechanisms to therapies: the multifaceted roles of guanylate-binding protein 2 in immunity, cancer, and beyond.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12571816/
30. Chih-Wei C, Cheng-Han Y, Yuan-Ho L, Ya-Chin H, Tain-Junn C, Sheng-Tsung C, et al.. The Fibronectin Expression Determines the Distinct Progressions of Malignant Gliomas via Transforming Growth Factor-Beta Pathway.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8038731/
31. Jianming W, Chun-Yuan C, Xue Y, Fan Z, Juan L, Zhaohui F, et al.. Leukemia inhibitory factor, a double-edged sword with therapeutic implications in human diseases.. Molecular therapy : the journal of the American Society of Gene Therapy [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9931620/
32. Sophie EK, Filomena OG-E, Sean EL, Michal ON, Arndt R, Sabine K, et al.. Drug Resistance in Glioma Cells Induced by a Mesenchymal-Amoeboid Migratory Switch.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773151/
33. Salvatore M, Grazia M, Rina DB, Lucia L, Pierpaolo M, Federica F, et al.. The Extracellular Matrix in Glioblastomas: A Glance at Its Structural Modifications in Shaping the Tumoral Microenvironment-A Systematic Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
34. Yu-Ting T, An-Chih W, Wen-Bin Y, Tzu-Jen K, Jian-Ying C, Wen-Chang C, et al.. ANGPTL4 Induces TMZ Resistance of Glioblastoma by Promoting Cancer Stemness Enrichment via the EGFR/AKT/4E-BP1 Cascade.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6888274/
35. Chongxian H, Shenbao S, Mengjiao G, Jingsen J, Chengcheng M, Tianwei W, et al.. Targeting TNFAIP2 induces immunogenic cell death and sensitizes glioblastoma multiforme to anti-PD-1 therapy.. Journal of neuro-oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37819535/
36. Ruchi S, Elizabeth BG, Michael JC, Ryan TB, Jian G, Edward FP, et al.. Complement factor H: a novel innate immune checkpoint in cancer immunotherapy.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10883309/
37. Available from: https://www.ncbi.nlm.nih.gov/gene/4600
38. Sun-Kyung L, Joohong A. Regulator of Calcineurin (RCAN): Beyond Down Syndrome Critical Region.. Molecules and cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7468584/
39. Shang-Hang S, Jian-Feng G, Ju H, Qian Z, Yi C. Bromodomain-containing protein 4 activates cardiotrophin-like cytokine factor 1, an unfavorable prognostic biomarker, and promotes glioblastoma . Annals of translational medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9096406/
40. Junhong L, Mingrong Z, Xingwang Z, Yufan X, Shuxin Z, Wentao F, et al.. Prognostic Significance of Preoperative Albumin to Alkaline Phosphatase Ratio in Patients with Glioblastoma.. Journal of Cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8408110/
41. Marisa CE, Yangjin K, Ruth L, William EA, Douglas AK, Avner F. Mechanistic modeling of the effects of myoferlin on tumor cell invasion.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3250187/
42. Katalin D, Fruzsina F, Dániel T. Factor XIII-A in Diseases: Role Beyond Blood Coagulation.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7867190/
43. Wenjun Z, Na L, Qianxia L, Xin C, Xiaoyu L, Min F, et al.. Development and validation of an inflammatory response-related prognostic model and immune infiltration analysis in glioblastoma.. Annals of translational medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9929762/
44. A EC, N S. G protein-coupled receptors as oncogenic signals in glioma: emerging therapeutic avenues.. Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4180709/
45. Hsiao-Han W, Tsuey-Yu C, Wei-Chen L, Kuo-Chen W, Jyh-Wei S. GADD45A plays a protective role against temozolomide treatment in glioblastoma cells.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5562912/
46. Yasuo I. Epithelial-mesenchymal transition in glioblastoma progression.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4774466/
47. Álvaro FLR, Daniela P da CT, Mucio L de AC, Andressa RR, Ester SR, Carlos GC. Expression of pluripotency-related genes in human glioblastoma.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8903226/
48. Jun M, Clark CC, Ming L. Macrophages/Microglia in the Glioblastoma Tumor Microenvironment.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8198046/
49. Yuan R, Donald LD, Erwin GVM, Daniel JB. 'Pseudopalisading' necrosis in glioblastoma: a familiar morphologic feature that links vascular pathology, hypoxia, and angiogenesis.. Journal of neuropathology and experimental neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/16783163/
50. Available from: https://pmc.ncbi.nlm.nih.gov/articles/pmid/39859381/
