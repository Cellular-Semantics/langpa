# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: malignant glioblastoma
- Tissue: brain

## Input Genes
LINC01727, AC117464.1, XYLT1, MMD2, EEPD1, AC013265.1, MYO5B, PLA2G4A, KCNIP1, ITGB4, AC019068.1, UNC5D, MIR3681HG, LINC02125, LINC02246, LRRC4C, LUCAT1, MDGA2, AC077690.1, CTXND1, AL353138.1, CDH18, MN1, AL356737.2, NKAIN3, ... (55 total)

## Program: CD44-mediated Invasive Adhesion
Coordinated regulation of cell-cell and cell-matrix adhesion through CD44 receptor interactions with hyaluronic acid and other extracellular matrix components. CD44 mediates formation of microtentacles and stabilizes migrating cell morphology during glioma invasion through orchestration of cytoskeletal dynamics and downstream signaling pathways.

**Predicted impacts**
- Enhanced dynamic adhesion enabling rapid migration through matrix-rich brain parenchyma
- Switching between individual and collective migration modes
- Increased tumor cell invasiveness and reduced chemoresistance through CD44-mediated multidrug transporter activation
- Resistance to conventional therapies through CD44-dependent survival signaling

**Evidence summary**
CD44 is highly overexpressed in GBM and directly mediates invasion through hyaluronic acid-rich extracellular matrix via formation of long, thin protrusions (microtentacles). These structures are stabilized by CD44-mediated coupling of microtubule and actin dynamics through IQGAP1 and engage both glia-dependent and glia-independent migration modes. CD44 also activates multiple pro-survival signaling pathways including PI3K/AKT and Src-family kinases, supporting both invasion and proliferation.

**Atomic biological processes**
- CD44-hyaluronic acid binding and mechanotransduction. Genes: CD44
  - [9]: Describes CD44 as HA receptor mediating adhesion, microtentacle formation, and mechanotransduction in GBM invasion
  - [12]: Details CD44 conformational changes and weak contact-based adhesion enabling rapid GBM cell attachment to HA matrix
- Cytoskeletal linking and microtubule-actin dynamics. Genes: CD44, ITGB4
  - [9]: IQGAP1-CLIP170 complex stabilizes microtentacles through microtubule and actin filament coordination
  - [12]: ERM protein coupling and RhoGTPase activation downstream of CD44 binding
- Growth factor receptor crosstalk and Src family kinase activation. Genes: CD44, ITGB4
  - [12]: CD44 interactions with EGFR and ErbB2 through adaptor molecules activate Src, PI3K/AKT, and MAPK pathways

**Atomic cellular components**
- Microtentacle protrusions. Genes: CD44
  - [9]: Dynamic CD44-coated tubular protrusions extending tens of micrometers, containing microtubules and actin filaments
- Focal adhesion complexes. Genes: CD44, ITGB4
  - [12]: CD44-mediated assembly of weak, transient adhesive structures distinct from integrin focal adhesions

**Required genes (not in input)**
- Genes: EGFR, ErbB2, IQGAP1, CLIP170, ERM
  - [9]: IQGAP1-CLIP170 complex required for microtentacle stabilization
  - [12]: EGFR and ErbB2 required for CD44-mediated growth factor receptor crosstalk

**Program citations**
- [9]: Mechanism of CD44-mediated microtentacle formation in GBM adhesion and invasion
- [12]: CD44 dual activities in promoting invasion and proliferation via multiple signaling pathways in GBM
- [20]: CD44v maintenance of SLC7A11 protein stability affecting tumor formation

## Program: Integrin-mediated Migration and EMT
ITGB4 integrin functions as a mechanosensor promoting tumor migration and invasion through epithelial-mesenchymal transition (EMT) programs, activated by engagement with extracellular ligands and coordinated with growth factor receptor signaling via focal adhesion kinase and phosphoinositide 3-kinase pathways.

**Predicted impacts**
- Enhanced FAK-mediated signaling promoting migration and invasion capacity
- Coordinated activation of EMT programs enhancing mesenchymal phenotype
- Increased phosphorylation and activation of downstream AKT and ERK pathways
- Promotion of collective invasion through matrix-associated signaling

**Evidence summary**
ITGB4 is upregulated in aggressive GBM subtypes and promotes migration and invasion through multiple interconnected mechanisms. Engagement of ITGB4 with extracellular ligands triggers Src kinase-mediated FAK phosphorylation, activating both PI3K/AKT and ERK signaling cascades that promote cellular motility. ITGB4 also induces EMT programs marked by increased Slug expression, with Slug knockdown reversing the invasive phenotype. ITGB4 overexpression dramatically accelerates tumor growth in xenograft models and is predictive of poor prognosis in multiple cancer types including glioma.

**Atomic biological processes**
- Integrin αβ4 ligand engagement and FAK phosphorylation. Genes: ITGB4
  - [15]: ITGB4 engagement with HLA-1 triggers Src kinase phosphorylation and FAK recruitment
  - [18]: ITGB4-mediated Src kinase activation leading to FAK phosphorylation at Y1510
- PI3K/AKT and MAPK signaling activation. Genes: ITGB4
  - [18]: FAK activation stimulates PI3K/AKT and ERK signaling promoting tumor cell migration
  - [15]: ITGB4 promotes EMT via upregulation of Slug and involvement of AKT/Sox2-Nanog
- EMT and stemness program activation. Genes: ITGB4
  - [15]: ITGB4 overexpression promotes EMT in parallel with Slug upregulation; Slug knockdown reverses invasion

**Atomic cellular components**
- Hemidesmosomes and focal adhesion complexes. Genes: ITGB4
  - [18]: α6β4 integrin release from hemidesmosomes and cooperation with growth factor receptors

**Required genes (not in input)**
- Genes: FAK, Src, SLUG, E-cadherin
  - [18]: FAK and Src kinases are essential downstream effectors of ITGB4 signaling
  - [15]: SLUG is essential mediator of ITGB4-induced EMT

**Program citations**
- [15]: ITGB4 promotes HCC proliferation, invasion, and EMT via Slug-mediated mechanisms
- [18]: Comprehensive review of ITGB4 mechanisms in tumor migration and invasion across multiple cancer types

## Program: N-cadherin-dependent Context-specific Migration
N-cadherin (CDH2) functions as a context-dependent regulator of glioma cell migration, promoting movement on neural cell surfaces while inhibiting migration through extracellular matrix. Intercellular homotypic N-cadherin interactions enable collective invasion through alternating engagement with different cellular environments.

**Predicted impacts**
- Promotion of migration along white matter tracts and gray matter interfaces
- Facilitation of collective invasion with coordinated cell movement
- Dynamic switching between migration routes based on local environment
- Reduced individual cell migration capacity but enhanced coordinated advancement

**Evidence summary**
N-cadherin (CDH2) exhibits paradoxical effects on glioma migration depending on the cellular environment. High N-cadherin expression accelerates migration on neurons and astrocytes through homotypic interactions but inhibits migration through extracellular matrix. This context-dependent regulation is mediated through changes in leading edge stimulation versus trailing edge inhibition. N-cadherin depletion stimulates ECM invasion and reduces migration on neural cells, suggesting that N-cadherin levels determine choice of invasion routes. In vivo, this mechanism may promote selective invasion along white matter and gray matter interfaces.

**Atomic biological processes**
- Homotypic N-cadherin-mediated cell-cell adhesion. Genes: CDH18
  - [41]: N-cadherin maintains intercellular contacts during collective glioma migration; N-cad depletion stimulates migration on ECM but not on neural cells
- Neural cell-glioma heterotypic adhesion signaling. Genes: CDH18
  - [41]: Glioma cells migrate rapidly on N-cadherin ECD and N-cad-expressing astrocytes; migration speed depends on endogenous N-cad

**Atomic cellular components**
- Adherens junction assembly. Genes: CDH18
  - [41]: N-cadherin localizes differentially in leader and follower cells during collective migration

**Required genes (not in input)**
- Genes: CDH2, catenins, p120-catenin
  - [41]: Adherens junction proteins are required for N-cadherin-mediated signaling

**Program citations**
- [41]: N-cadherin differentially regulates glioma migration based on environmental context

## Program: Extracellular Matrix Remodeling
Active ECM remodeling via ADAMTS family proteases, collagen biosynthesis and deposition, and tenascin-C expression in glioblastoma creates a permissive microenvironment for tumor progression. ECM components serve as both structural scaffolds and bioactive signaling molecules regulating tumor cell behavior.

**Predicted impacts**
- Enhanced tumor cell migration through enzymatic matrix degradation
- Creation of physical scaffolds supporting collective invasion
- Generation of bioactive ECM fragments promoting tumor cell signaling
- Promotion of vascular invasion and angiogenesis through TNC-mediated effects

**Evidence summary**
ECM remodeling is a hallmark of GBM progression involving coordinated expression of matrix proteases (ADAMTS4/5), collagen biosynthesis (including brain-specific COL20A1), and glycoprotein deposition (TNR, TNC). This dynamic remodeling actively shapes tumor development by providing permissive migration substrates and generating bioactive signaling molecules. High fibrillar collagen expression correlates with high stroma fraction and poor GBM prognosis. Tenascin-C is particularly enriched in hypervascularized areas and promotes angiogenesis and immune evasion.

**Atomic biological processes**
- Matrix metalloproteinase and ADAMTS-mediated proteolysis. Genes: ADAMTS5
  - [42]: ADAMTS4/5 and matrix metalloproteinases remodel collagen and other ECM components in GBM
  - [49]: Matrix-degrading proteases ADAMTS4 and ADAMTS5 are expressed in glioblastomas and facilitate tumor invasion
- Collagen deposition and crosslinking. Genes: COL20A1
  - [39]: COL20A1 is brain-specific collagen expressed in neuronal lineage tumors including GBM and LGG
  - [42]: COL1A1 is positively correlated with stroma fraction and associated with poor survival in GBM
- Tenascin-C and TNR glycoprotein expression. Genes: TNR
  - [26]: Tenascin-C is overexpressed in GBM, plays critical role in tumor progression, and serves as therapeutic target
  - [29]: TNC and TNR share similar expression profiles in GBM and contribute to immunosuppressive microenvironment

**Atomic cellular components**
- Basement membrane composition. Genes: COL20A1
  - [42]: ECM of brain tumors includes collagen IV, laminin, and fibronectin lining blood vessels
- Perivascular ECM niche. Genes: TNR, COL20A1
  - [42]: Collagen I, tenascin-C, vitronectin and hyaluronan surround tumor cells surrounding vasculature

**Required genes (not in input)**
- Genes: MMP2, MMP9, collagen I, laminin, fibronectin
  - [42]: Additional proteases and ECM components essential for GBM matrix remodeling

**Program citations**
- [26]: Tenascin-C is overexpressed in GBM and serves as therapeutic target for CAR T cells
- [39]: Collagen profiles predict genetic features and patient prognosis across tumor types
- [42]: Comprehensive review of collagen and ECM receptors in driving glioma progression
- [49]: Systematic review of ECM role in shaping glioblastoma tumor development

## Program: Metabolic Reprogramming and Redox Homeostasis
Coordinated upregulation of oxidative phosphorylation (via PPARGC1A), cystine-glutamate exchange (via SLC7A11), and DNA repair mechanisms (via EEPD1) enables glioblastoma cells to manage replication stress, maintain redox balance, and sustain proliferation under nutrient-limited conditions.

**Predicted impacts**
- Enhanced ATP production supporting high energy demands of proliferation
- Maintenance of reducing potential enabling rapid biosynthesis
- Protection from ferroptosis and oxidative stress-induced apoptosis
- Sustained proliferation under nutrient-limited tumor microenvironment
- Increased resistance to oxidative therapy-induced damage

**Evidence summary**
Glioblastoma cells reprogram metabolism to sustain proliferation and manage replication stress. PGC-1α drives enhanced oxidative phosphorylation, particularly in ASCL1 subtype tumors, increasing mitochondrial content and ATP generation. Simultaneously, SLC7A11 upregulation increases cystine uptake for glutathione synthesis, protecting cells from oxidative stress and ferroptosis. EEPD1 stabilizes replication forks under stress conditions, enabling cells to survive continuous DNA damage from oncogenic signaling. These coordinated metabolic adaptations are especially critical under glucose deprivation and are associated with poor patient prognosis.

**Atomic biological processes**
- PPARGC1A-driven mitochondrial biogenesis and OXPHOS. Genes: PPARGC1A
  - [19]: PGC-1α drives small cell neuroendocrine cancer progression and OXPHOS activity; correlates with ASCL1 subtype
- SLC7A11-mediated cystine uptake and glutathione synthesis. Genes: SLC7A11
  - [20]: SLC7A11/xCT transports cystine for glutathione synthesis protecting from oxidative stress and ferroptosis
  - [23]: High cell density increases glioblastoma cell viability under glucose deprivation via xCT system
- EEPD1-mediated replication fork stability. Genes: EEPD1
  - [8]: EEPD1 provides DNA resistance to replication stress enabling better cell survival; correlated with poor prognosis

**Atomic cellular components**
- Mitochondrial cristae and electron transport chain. Genes: PPARGC1A
  - [19]: PGC-1α overexpression increases mitochondrial content (TOMM20) and OXPHOS capacity
- Plasma membrane cystine/glutamate antiporter. Genes: SLC7A11
  - [20]: SLC7A11 is 12-transmembrane transporter mediating 1:1 cystine-glutamate exchange

**Required genes (not in input)**
- Genes: ASCL1, GPX4, GSH synthase, complex I
  - [19]: ASCL1 lineage correlates with PGC-1α expression in small cell neuroendocrine carcinoma
  - [20]: GPX4 essential for ferroptosis resistance downstream of SLC7A11-mediated GSH synthesis

**Program citations**
- [19]: PGC-1α drives SCNC progression and metabolic reprogramming via OXPHOS
- [20]: Comprehensive review of SLC7A11 in cancer metabolism and ferroptosis resistance
- [8]: EEPD1 dysregulation correlates with poor prognosis and affects immune infiltration

## Program: Immune Evasion and Checkpoint Regulation
Coordinated suppression of MHC class I antigen presentation via altered NLRC5 signaling and expression of immunomodulatory molecules enables glioblastoma cells to escape T cell recognition. Extracellular vesicle-mediated transfer of Arc protein facilitates intercellular communication within tumor cell networks and immune evasion.

**Predicted impacts**
- Reduced MHC class I expression on tumor cell surface limiting CD8+ T cell recognition
- Enhanced intercellular communication through EV-mediated mRNA transfer
- Promotion of glioma cell heterogeneity and plasticity through Arc signaling
- Facilitation of adaptive immune evasion mechanisms

**Evidence summary**
GBM cells suppress adaptive immune responses through multiple coordinated mechanisms. NLRC5-dependent MHC class I expression is often reduced in GBM, limiting antigen presentation to CD8+ T cells. Simultaneously, glioma cells express high levels of Arc/Arg3.1, which forms retrovirus-like capsid particles that encapsulate and transfer mRNA between tumor cells via extracellular vesicles. This Arc-mediated intercellular communication promotes glioma cell heterogeneity and affects synaptic plasticity in surrounding neurons, further modulating the tumor microenvironment. CD44-mediated signaling also contributes to immune evasion through effects on metabolic reprogramming and inflammatory responses.

**Atomic biological processes**
- NLRC5-dependent MHC class I transcriptional regulation. Genes: NLRC5
  - [21]: NLRC5 is transcriptional regulator of MHC class I genes, TAP1, and LMP2 required for antigen presentation
  - [24]: NLRC5 beyond MHC I regulation contributes to innate and adaptive immune responses
- Arc-mediated extracellular vesicle biogenesis and intercellular communication. Genes: ARC
  - [31]: Arc/Arg3.1 protein forms capsid-like particles encapsulating mRNA for intercellular transfer via EVs in glioma
  - [34]: ARC gene expression associated with high infiltration of stromal and immune cells in breast cancer
- CD44-mediated immune cell suppression. Genes: CD44
  - [20]: CD44v maintains SLC7A11 protein stability affecting tumor formation and immune evasion

**Atomic cellular components**
- MHC class I-peptide complex. Genes: NLRC5
  - [21]: NLRC5 activates promoters of MHC class I genes and related components for antigen presentation
- Extracellular vesicles and exosomes. Genes: ARC
  - [31]: Arc EVs contain Arc/Arg3.1 protein and Arc mRNA enabling intercellular transfer

**Required genes (not in input)**
- Genes: TAP1, LMP2, β2-microglobulin, IFN-γ
  - [21]: NLRC5 regulates TAP1, LMP2, and β2-microglobulin as part of MHC class I pathway

**Program citations**
- [21]: NLRC5 is transcriptional regulator of MHC class I antigen presentation
- [31]: Arc protein involved in extracellular vesicle-mediated mRNA transfer between glioma cells
- [24]: NLRC5 functions beyond MHC I regulation in immune responses

## Program: Ganglioside and Glycosylation-based Signaling
Expression of ganglioside synthesis enzymes (ST8SIA1, ST8SIA5) and glycosyltransferases (CHST8, XYLT1) in glioblastoma promotes tumor progression through enhanced cell surface glycosylation. GD3 ganglioside and related glycosphingolipids activate oncogenic signaling cascades and promote stemness, angiogenesis, and immune evasion.

**Predicted impacts**
- Enhanced GD3 expression promoting glioma stemness and self-renewal capacity
- Activation of oncogenic RTK signaling through GD3-mediated receptor clustering
- Increased tumor angiogenesis through GD3-promoted VEGF release
- Enhanced immunosuppression through ganglioside-mediated T cell inhibition
- Altered cell adhesion and metastatic potential through modified cell surface glycosylation

**Evidence summary**
GBM cells express elevated levels of glycosylation machinery including ganglioside and heparan sulfate biosynthetic enzymes. GD3 ganglioside concentration strongly correlates with GBM grade and is essential for glioma stemness, as demonstrated by dramatic reduction in tumorosphere formation and tumor initiation following GD3S knockdown. GD3 promotes stemness through c-Met signaling pathway activation and recruits mutated receptor tyrosine kinases to glycolipid-enriched microdomains for ligand-independent activation. GD3 also drives angiogenesis and immune evasion in glioblastoma. XYLT1-dependent GAG biosynthesis similarly affects tumor progression through both cell surface signaling and extracellular matrix composition.

**Atomic biological processes**
- ST8SIA-mediated sialic acid chain synthesis. Genes: ST8SIA1, ST8SIA5
  - [43]: ST8SIA1 and ST8SIA5 catalyze sialic acid transfer; GD3 concentration correlates with GBM grade
- XYLT1-mediated xylose attachment for GAG biosynthesis. Genes: XYLT1
  - [6]: XYLT1 catalyzes first step of GAG biosynthesis; dysregulated GAG composition in glioblastoma promotes progression
  - [3]: XYLT1 glycosyltransferase activates NF-κB signaling to promote metastasis of early-stage lung adenocarcinoma
- CHST8-mediated carbohydrate sulfation. Genes: CHST8
  - [43]: Carbohydrate-modifying enzymes including sulfotransferases affect GBM development
- GD3-mediated RTK activation and MAP kinase signaling. Genes: ST8SIA1, ST8SIA5
  - [43]: GD3 recruits mutated RTKs to glycolipid-enriched microdomains and activates AKT, Src, and ERK signaling

**Atomic cellular components**
- Glycolipid-enriched microdomains (rafts). Genes: ST8SIA1, ST8SIA5
  - [43]: GD3 recruits receptor tyrosine kinases to GEM/rafts for ligand-independent activation
- Heparan sulfate and chondroitin sulfate GAG chains. Genes: XYLT1, CHST8
  - [6]: XYLT1 catalyzes first step of HS/CS biosynthesis; dysregulation in glioblastoma affects cell surface properties

**Required genes (not in input)**
- Genes: GD3S, c-Met, RTK, VEGF
  - [43]: GD3S, c-Met, and RTK activation are central to GD3-mediated glioma progression

**Program citations**
- [43]: Comprehensive review of GD3 ganglioside as promising therapeutic target in glioma
- [6]: α-Xylosides inhibit GAG biosynthesis and glioma cell viability
- [3]: XYLT1 activates NF-κB signaling to promote cancer metastasis

## Program: Neural-like Developmental Signaling
Coordinated expression of neuroligin/netrin receptor systems (LRRC4C, MDGA2, UNC5D) and guidance molecule receptors (RGMA, DAB1) in glioblastoma mimics developmental neural signaling pathways. These systems regulate glioma cell migration patterns, synaptic-like contacts, and interactions with host neural tissue.

**Predicted impacts**
- Enhanced glioma cell migration through neural pathways along white matter tracts
- Formation of neuroglial synaptic-like contacts promoting tumor progression
- Escape from repulsive guidance cues enabling migration into neural tissue
- Exploitation of developmental neural wiring for dissemination

**Evidence summary**
GBM cells express neural-like signaling machinery that enables them to navigate the brain microenvironment using developmental programs. LRRC4C functions as tumor suppressor in gliomas and mediates synaptic-like interactions. MDGA2 interacts with neuroligin-2 to regulate synapse formation, suggesting gliomas may form pseudo-synaptic contacts with host neurons. UNC5D and RGMA are repulsive guidance molecule receptors; however, high RGMA and NEO1 expression in GBM is associated with poor prognosis, suggesting gliomas exploit these pathways for migration. DAB1 mediates reelin signaling important for developmental neuronal positioning. These neural-mimicry pathways allow GBM cells to integrate into host neural circuits and exploit developmental migration programs.

**Atomic biological processes**
- MDGA2-neuroligin-2 inhibitory synapse regulation. Genes: MDGA2
  - [27]: MDGAs bind neuroligin-2 with nanomolar affinity and suppress NL2-dependent inhibitory synapse formation
- LRRC4C-mediated synapse formation and plasticity. Genes: LRRC4C
  - [51]: LRRC4 (NGL-2) mediates formation of Schaffer collateral synapses and affects information input pathways
  - [54]: LRRC4C involved in axon guidance, synapse formation, and may function as tumor suppressor in gliomas
- UNC5D/FLRT-mediated repulsive guidance and apoptosis. Genes: UNC5D
  - [25]: UNC5D has intracellular death domain triggering apoptosis; FLRT2 is repulsive ligand in deep cortical layers
  - [28]: UNC-5 family netrin receptors regulate axon guidance, cell migration, and cell survival
- RGMA-neogenin repulsive guidance signaling. Genes: RGMA
  - [44]: RGMA elevated in GBM; binds NEO1 receptor activating RhoA-ROCK1 signaling; associated with poor survival
  - [47]: RGMA correlates with poor glioma prognosis; co-expression with NEO1 predicts patient outcomes
- DAB1-mediated reelin signaling and neuronal positioning. Genes: DAB1
  - [14]: DAB1 stabilizes leading processes in Rap1-dependent manner during neuronal migration
  - [17]: Reelin-DAB1 signaling regulates neuronal migration through alternative splicing and differential SH2 protein recruitment

**Atomic cellular components**
- Synaptic adhesion complexes. Genes: MDGA2, LRRC4C
  - [27]: MDGA and neuroligin proteins form cell-cell adhesion interfaces at inhibitory synapses
- Growth cone guidance structures. Genes: UNC5D, RGMA
  - [25]: Netrin receptors regulate growth cone collapse and directional migration

**Required genes (not in input)**
- Genes: neuroligin-2, netrin-1, netrin-4, neogenin, reelin, Rap1
  - [27]: Neuroligin-2 is ligand for MDGA interactions
  - [25]: Netrin-4 and FLRT are ligands for UNC5D receptor

**Program citations**
- [44]: RGMA is elevated in GBM and associated with poor prognosis through NEO1 interaction
- [51]: LRRC4 is tumor suppressor in gliomas and regulates synaptic plasticity
- [27]: MDGA interactions with neuroligin-2 regulate inhibitory synapse formation
- [25]: UNC5 receptors regulate migration and survival through FLRT interactions

## Program: GFAP Isoform-dependent Malignancy
Dynamic regulation of GFAP alternative splicing in glioblastoma, with increased GFAPδ expression and elevated GFAPδ/GFAPα ratio marking malignant transformation. GFAPδ-dependent signaling promotes invasiveness through MAPK pathway modulation and extracellular matrix interaction changes.

**Predicted impacts**
- Enhanced tumor invasiveness through DUSP4-mediated MAPK modulation
- Increased risk for early recurrence and poor prognosis
- Altered ECM engagement promoting migration through brain parenchyma
- Enhanced malignant gene expression programs in high-grade tumors

**Evidence summary**
GFAP alternative splicing produces two major isoforms—GFAPα in differentiated astrocytes and GFAPδ in neural stem cells. High-grade glioblastomas show elevated GFAPδ expression and increased GFAPδ/GFAPα ratio compared to lower-grade gliomas. This isoform switch is not merely a marker of malignancy but actively drives invasiveness through multiple mechanisms. The GFAPδ isoform induces DUSP4 (MAPK phosphatase 2) expression, which regulates the MAPK-signaling pathway critical for tumor malignancy. Additionally, increased GFAPδ/GFAPα ratio activates genes controlling glioma-ECM interactions, directly promoting cell invasiveness. Immunohistochemical detection of high GFAPδ expression predicts increased risk of early recurrence and warrants aggressive patient follow-up.

**Atomic biological processes**
- GFAP alternative splicing and isoform switching. Genes: GFAP
  - [13]: GFAPδ expression maintained in high-grade astrocytomas; GFAPδ/α ratio increased in grade IV astrocytoma
  - [16]: GFAP isoform-specific analysis necessary to distinguish differentiation state and malignancy in astrocytomas
- DUSP4/MAPK phosphatase activation by GFAPδ. Genes: GFAP
  - [13]: Higher GFAPδ/α ratio induces DUSP4 expression; DUSP4 correlates with worse prognosis and regulates MAPK-signaling
- ECM interaction pathway modulation. Genes: GFAP
  - [13]: Higher GFAPδ/α ratio activates genes involved in glioma-ECM interactions and increases invasiveness capability

**Atomic cellular components**
- Intermediate filament cytoskeleton. Genes: GFAP
  - [13]: GFAP isoforms form intermediate filament structures with differential cellular effects

**Required genes (not in input)**
- Genes: DUSP4, MAPK, ERK
  - [13]: DUSP4 is key downstream mediator of GFAPδ-induced malignancy through MAPK regulation

**Program citations**
- [13]: GFAPδ is promising biomarker and therapeutic target in glioblastoma
- [16]: Importance of GFAP isoform-specific analyses in astrocytoma malignancy assessment

## Program: Long Non-Coding RNA Regulatory Networks
Dysregulated expression of multiple long non-coding RNAs (lncRNAs) in glioblastoma orchestrates tumor progression through competing endogenous RNA (ceRNA) networks, regulation of mRNA stability, and modulation of chromatin structure. lncRNAs serve as scaffolds for transcriptional regulation and affect immune cell infiltration.

**Predicted impacts**
- Dysregulated expression of tumor suppressor and oncogene networks
- Altered immune cell recruitment and infiltration patterns
- Enhanced tumor cell proliferation and survival through miRNA depletion
- Modulation of cell cycle checkpoints and apoptosis evasion
- Increased epithelial-mesenchymal transition and stemness programs

**Evidence summary**
lncRNAs comprise a substantial fraction of the dysregulated transcriptome in glioblastoma. Multiple lncRNAs in the input list function through competing endogenous RNA (ceRNA) networks, where they sequester miRNAs away from mRNA targets, thereby indirectly regulating protein-coding gene expression. These lncRNAs affect critical cancer phenotypes including proliferation, invasion, EMT, apoptosis resistance, and immune infiltration. lncRNAs also scaffold transcriptional regulatory complexes and stabilize mRNA through protein interactions. The overall effect is rewiring of gene regulatory networks to promote malignant properties and suppress anti-tumor immune responses.

**Atomic biological processes**
- ceRNA-mediated miRNA sponging and mRNA regulation. Genes: LINC01727, AC117464.1, LINC02125, LINC02246, LINC01776, LINC01117, LINC02328, AL353138.1, AL356737.2, AL159156.1, AC077690.1, AC019068.1, AC013265.1, AC233296.1, AC124254.2, AC007344.1, MIR3681HG, LUCAT1
  - [11]: lncRNAs act as competing endogenous RNAs regulating mRNA stability through miRNA binding in ESCC and other cancers
  - [37]: lncRNAs regulate expression of proto-oncogenes and tumor suppressors through competing endogenous RNA networks
- lncRNA scaffolding of transcriptional complexes. Genes: LINC01727, AC117464.1, LINC02125, LINC02246, LINC01776, LINC01117, LINC02328, AL353138.1, AL356737.2, AL159156.1, AC077690.1, AC019068.1, AC013265.1, AC233296.1, AC124254.2, AC007344.1, MIR3681HG, LUCAT1
  - [37]: lncRNAs scaffold transcription factor complexes and interact with HuR affecting mRNA stability
- lncRNA-mediated immune infiltration and microenvironment remodeling. Genes: LINC01727, AC117464.1, LINC02125, LINC02246, LINC01776, LINC01117, LINC02328, AL353138.1, AL356737.2, AL159156.1, AC077690.1, AC019068.1, AC013265.1, AC233296.1, AC124254.2, AC007344.1, MIR3681HG, LUCAT1
  - [4]: lncRNAs change immune microenvironment contributing to cancer phenotype and immune cell infiltration

**Atomic cellular components**
- lncRNA-miRNA complexes. Genes: LINC01727, AC117464.1, LINC02125, LINC02246, LINC01776, LINC01117, LINC02328, AL353138.1, AL356737.2, AL159156.1, AC077690.1, AC019068.1, AC013265.1, AC233296.1, AC124254.2, AC007344.1, MIR3681HG, LUCAT1
  - [37]: lncRNAs serve as ceRNA competing for miRNA binding through shared miRNA response elements

**Required genes (not in input)**
- Genes: miRNA targets, HuR, transcription factors
  - [37]: lncRNAs interact with regulatory proteins to affect gene expression

**Program citations**
- [37]: Comprehensive review of lncRNA functions and unique features in cancer
- [4]: lncRNAs regulate immune cell infiltration and tumor microenvironment in HNSCC
- [11]: lncRNAs regulate EMT, cell cycle, stemness, and apoptosis in esophageal squamous cell carcinoma

## Program: PI3K/AKT Signaling Modulation
INPP4B phosphatase regulates PI3K/AKT signaling by converting PI(3,4)P2 to PI(3)P, with context-dependent effects on tumor progression. In PIK3CA-mutant ER+ breast cancers, INPP4B promotes Wnt/β-catenin signaling through late endosome formation, while in triple-negative breast cancers, INPP4B loss enhances AKT activation.

**Predicted impacts**
- Context-dependent modulation of AKT signaling strength
- Enhanced Wnt/β-catenin pathway activation in specific tumor contexts
- Altered response to PI3K inhibitor therapies
- Differential tumor suppressor versus oncogenic activities in different cancer subtypes

**Evidence summary**
INPP4B exhibits dual roles as both tumor suppressor and oncogene depending on cancer subtype and mutational context. In triple-negative breast cancers (often PTEN-null), INPP4B loss enhances oncogenic AKT signaling. However, in PIK3CA-mutant ER+ breast cancers, INPP4B functions as an oncogene by promoting Wnt/β-catenin activation through late endosome signaling. This paradoxical function stems from INPP4B's role in converting PI(3,4)P2 to PI(3)P on late endosomes, which recruits ESCRT machinery and facilitates endosomal trafficking of GSK3β for lysosomal degradation, thereby stabilizing β-catenin. This discovery indicates that PI3K pathway regulation is highly context-dependent and that therapeutic targeting requires understanding of specific genomic backgrounds.

**Atomic biological processes**
- INPP4B-mediated phosphoinositide conversion on late endosomes. Genes: INPP4B
  - [33]: INPP4B converts PI(3,4)P2 to PI(3)P on late endosomes, promoting Hrs-dependent endosome formation
- PI3K/AKT pathway regulation. Genes: INPP4B
  - [33]: INPP4B suppresses AKT signaling by converting PI(3,4)P2 downstream of class I PI3K
  - [36]: INPP4B knockdown in ER-positive breast cancer cells increases Akt activation
- Wnt/β-catenin crosstalk with PI3K signaling. Genes: INPP4B
  - [33]: INPP4B promotes late endosome-mediated Wnt/β-catenin activation through GSK3β lysosomal degradation

**Atomic cellular components**
- Late endosome signaling hub. Genes: INPP4B
  - [33]: INPP4B generates PI(3)P on late endosomes recruiting Hrs and facilitating intraluminal vesicle formation
- ESCRT complex assembly. Genes: INPP4B
  - [33]: PI(3)P recruits Hrs (ESCRT member) promoting late endosome maturation

**Required genes (not in input)**
- Genes: PI3K, AKT, Hrs, GSK3β, β-catenin
  - [33]: PI3K, AKT, Hrs, GSK3β, and β-catenin are essential components of INPP4B signaling pathways

**Program citations**
- [33]: INPP4B facilitates PI3Kα-dependent late endosome formation and Wnt signaling crosstalk
- [36]: INPP4B regulates PI3K/AKT signaling in ER-positive breast cancer

## Program: Calcium-dependent Cell Adhesion
CDH18 and DCHS2 encode calcium-dependent cadherins mediating neural cell adhesion and affecting tumor progression through modulation of adhesive properties and immune cell interactions. CDH18 associates with macrophages in tumor microenvironment and affects immunotherapy resistance.

**Predicted impacts**
- Altered glioma cell adhesion and invasiveness based on calcium availability
- Modulation of immune cell-tumor cell interactions
- Effects on chemotherapy resistance through macrophage engagement
- Influence on tumor microenvironment composition and function

**Evidence summary**
CDH18 is a calcium-dependent cadherin expressed in neurons and central nervous system. In glioblastoma, CDH18 expression correlates with tumor progression stage and prognosis. CDH18 associates with immune checkpoint molecules and macrophages in the tumor microenvironment, suggesting it plays a role in immune modulation. Lower CDH18 expression increases glioma cell invasion and migration, while higher expression reduces chemotherapy resistance. CDH18 likely supports calcium-mediated adhesion between tumor cells and facilitates immune cell infiltration. DCHS2 is a related large cadherin also involved in cell adhesion and may cooperate with CDH18 in regulating glioma-immune interactions.

**Atomic biological processes**
- Calcium-dependent CDH18 adhesion. Genes: CDH18
  - [38]: CDH18 is calcium-dependent adhesion protein supporting intercellular adhesion; altered expression affects tumor progression
- CDH18-mediated immune cell interactions. Genes: CDH18
  - [38]: CDH18 associates with macrophages in tumor microenvironment affecting immune infiltration and chemotherapy response
- DCHS2 cadherin-mediated cell adhesion. Genes: DCHS2
  - [56]: DCHS2 encodes large protein containing many cadherin domains functioning in cell adhesion

**Atomic cellular components**
- Adherens junctions. Genes: CDH18, DCHS2
  - [38]: Cadherins interact with catenins forming adherens junctions crucial for cellular signaling and adhesion

**Required genes (not in input)**
- Genes: catenins, calcium, calmodulin
  - [38]: Catenins and calcium are required for CDH18-mediated adhesion

**Program citations**
- [38]: CDH18 is novel promising biomarker in UCEC with roles in tumor progression and immune modulation

## Program: Transcriptional Co-regulator Activity
MN1 meningioma-1 acts as essential co-factor in MLL fusion leukemias maintaining active transcription of HOXA cluster genes and their targets. MN1 high expression marks poor prognosis and its loss impairs leukemia proliferation, suggesting potential broader roles in glioblastoma transcriptional control.

**Predicted impacts**
- Maintenance of proliferative and survival gene expression programs
- Resistance to differentiation and apoptosis cues
- Altered chromatin architecture and transcriptional memory
- Poor prognosis association in affected tumors

**Evidence summary**
MN1 is a transcriptional co-factor with established roles in MLL-rearranged acute myeloid leukemia where it functions as an independent poor prognostic marker. MN1 maintains active chromatin at HOXA cluster genes and their downstream targets including anti-apoptotic BCL2, MCL1, and Survivin. MN1 deletion dramatically impairs MLL-AF9 leukemia proliferation and colony formation in vitro and prevents leukemia initiation in vivo. While MN1's role in glioblastoma is not explicitly characterized in the search results, MN1 high expression in other cancer types suggests it may function similarly to maintain proliferative and survival gene programs in brain tumors.

**Atomic biological processes**
- MN1-mediated transcriptional maintenance of HOXA cluster. Genes: MN1
  - [45]: MN1 maintains active transcription of HOXA9 and HOXA10 critical downstream genes of MLL fusion leukemias
- MN1-dependent regulation of anti-apoptotic factors. Genes: MN1
  - [45]: MN1 regulates target genes including BCL2, MCL1, and Survivin promoting cell survival

**Atomic cellular components**
- Transcriptional co-regulator complexes. Genes: MN1
  - [45]: MN1 functions as co-factor in chromatin-associated complexes affecting transcription

**Required genes (not in input)**
- Genes: HOXA9, HOXA10, BCL2, MCL1, Survivin
  - [45]: HOXA cluster genes and downstream targets are regulated by MN1

**Program citations**
- [45]: MN1 is indispensable for MLL fusion leukemia and serves as therapeutic target

## Program: Heparan Sulfate Proteoglycan Signaling
GPC5 glypican-5 heparan sulfate proteoglycan functions as tumor suppressor in glioblastoma and other cancers by promoting Sonic Hedgehog co-receptor activity and antagonizing Wnt/β-catenin signaling. Reduced GPC5 expression correlates with increased proliferation and poor prognosis.

**Predicted impacts**
- Reduced proliferation through Wnt/β-catenin pathway antagonism
- Decreased cell migration and invasiveness
- Impaired tumor growth in xenograft models
- Enhanced differentiation and reduced stemness

**Evidence summary**
GPC5 is a heparan sulfate proteoglycan anchored to the cell surface via GPI linkage. In lung adenocarcinoma and other cancers, GPC5 functions as tumor suppressor. GPC5 expression is significantly reduced in tumors compared to normal tissue, often through epigenetic silencing by hypermethylation or microRNA-mediated repression. Restoration of GPC5 expression inhibits tumor growth by antagonizing Wnt/β-catenin signaling and promoting differentiation. GPC5 also functions as Sonic Hedgehog co-receptor through its highly sulfated GAG chains, particularly at primary cilia. Polymorphisms in GPC5 are associated with multiple sclerosis and other inflammatory demyelinating diseases, underscoring its role in immune regulation.

**Atomic biological processes**
- GPC5-mediated Sonic Hedgehog co-receptor function. Genes: GPC5
  - [57]: GPC5 enhances Sonic Hedgehog signaling by promoting Shh binding to Patched-1 via sulfated GAG chains
- GPC5-dependent Wnt/β-catenin pathway antagonism. Genes: GPC5
  - [57]: Restoration of GPC5 in lung adenocarcinoma inhibits tumor growth by suppressing Wnt/β-catenin signaling

**Atomic cellular components**
- Primary cilium localization. Genes: GPC5
  - [57]: GPC5 is strategically localized at primary cilia for Hedgehog pathway regulation
- Cell surface heparan sulfate chains. Genes: GPC5
  - [57]: GPC5 is HSPG with highly sulfated GAG chains serving as co-receptor for signaling molecules
  - [50]: GPC5 is glypican family member with GPI anchor attachment to plasma membrane

**Required genes (not in input)**
- Genes: Sonic Hedgehog, Patched-1, Wnt, β-catenin
  - [57]: Shh and Wnt pathway components are downstream of GPC5 signaling

**Program citations**
- [57]: GPC5 is glypican with pivotal role in developmental processes and tumor suppression
- [50]: GPC5 and glypican family members regulate cell proliferation and growth

## Program: Histamine Receptor Signaling
HRH1 histamine H1-receptor promotes tumorigenesis through ERK/EGR1 signaling axis while HRH2 H2-receptor antagonizes these effects. The HRH2/HRH1 expression ratio predicts patient survival, suggesting bimodal histamine signaling roles in glioblastoma and other cancers.

**Predicted impacts**
- Enhanced tumor cell proliferation and survival through H1R-mediated ERK signaling
- Increased chemokine-mediated immune cell recruitment and tumor-promoting inflammation
- Protective effects through H2R-mediated ERK suppression
- Bimodal regulation of tumor growth based on HRH2/HRH1 expression ratio

**Evidence summary**
Histamine signaling through H1 and H2 receptors exhibits bimodal effects on tumor development. H1R activation promotes colorectal carcinogenesis through elevated ERK phosphorylation and EGR1 upregulation, leading to increased cancer cell proliferation and survival. Conversely, H2R activation suppresses these effects by antagonizing ERK signaling. The HRH2/HRH1 expression ratio predicts patient survival, with higher H2R to H1R ratios correlating with improved outcomes. Elevated HRH1 expression predicts poor survival in colorectal, lung, and other cancers. H1R antagonists suppress tumorigenesis while H2R antagonists promote tumor growth, suggesting therapeutic potential for H1R blockade combined with H2R agonism.

**Atomic biological processes**
- HRH1-mediated ERK activation and proliferation. Genes: HRH1
  - [32]: H1R activation promotes ERK phosphorylation and EGR1 expression supporting cancer cell survival
- HRH2-mediated ERK suppression. Genes: HRH1
  - [32]: H2R signaling suppresses ERK and chemokine gene expression induced by H1R activation
- Histamine-mediated chemokine expression. Genes: HRH1
  - [32]: H1R activation increases CCL20 and IL8 chemokine expression; H2R suppresses these effects

**Atomic cellular components**
- G-protein coupled receptors. Genes: HRH1
  - [32]: HRH1 and HRH2 are G-protein coupled receptors transducing histamine signaling

**Required genes (not in input)**
- Genes: ERK, EGR1, CCL20, IL8
  - [32]: ERK and EGR1 are downstream effectors of H1R signaling

**Program citations**
- [32]: Distinct roles of histamine H1 and H2 receptor signaling in colorectal cancer

## Bibliography
1. Huicong Z, Yuhao L, Huixia L. Correlation of BUB1 and BUB1B with the development and prognosis of endometrial cancer.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11269704/
2. Available from: https://data.broadinstitute.org/gsea-msigdb/msigdb/annotations_versioned/Human_Symbol_with_Remapping_MSigDB.v7.0.chip
3. Available from: https://aacrjournals.org/cancerres/article/85/9/1628/762058/The-Glycosyltransferase-XYLT1-Activates-NF-B
4. Xueying W, Kui C, Erliang G, Xionghui M, Lunhua G, Cong Z, et al.. Identification of Immune-Related LncRNA Pairs for Predicting Prognosis and Immunotherapeutic Response in Head and Neck Squamous Cell Carcinoma.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8116744/
5. Available from: http://sc-ovdb.com
6. Mausam K, Javier V-M, Yuki O, Chakrapani K, Katharine C, Esraa M, et al.. Synthesis and Screening of α-Xylosides in Human Glioblastoma Cells.. Molecular pharmaceutics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8483608/
7. Available from: https://patents.google.com/patent/US10793914B2/en
8. Yang G, Shujin L, Zhan S, Bingchen C, Ziang W, Peng Y, et al.. EEPD1 is identified as a predictor of prognosis and immune microenvironment through pan-cancer analysis and related to progression of colorectal cancer.. Heliyon [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11021989/
9. Wolf KJ, Shukla P, Springer K, Lee S, Coombes JD, Choy CJ, et al.. A mode of cell adhesion and migration facilitated by CD44-dependent microtentacles. Proceedings of the National Academy of Sciences [Internet]. 2020May7;117(21). Available from: https://www.pnas.org/doi/10.1073/pnas.1914294117
10. Yongbo Z, Yingying Z, Xiaopeng S, Hua L, Jinmei S, Chunyu H, et al.. Modulation of Stem Cells as Therapeutics for Severe Mental Disorders and Cognitive Impairments.. Frontiers in psychiatry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7205035/
11. Yuning L, Zhenyi L, Hongyan X, Wenzhen Z, Ruonan P, Zhongying Z, et al.. Functions and mechanisms of long non-coding RNA in esophageal squamous cell carcinoma (Review).. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12242912/
12. Akihiro I, Takanori O, Masahiro N, Yoshihiro O, Kosuke K, Hajime Y, et al.. A Narrative Review on CD44's Role in Glioblastoma Invasion, Proliferation, and Tumor Recurrence.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
13. Roxana R, George EDP, Radu MG, Felix MB. GFAPδ: A Promising Biomarker and Therapeutic Target in Glioblastoma.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8971704/
14. Santos JF, Isabel M-G, Cristina G-S, Sarah RH-P, Ulrich M. Reelin regulates cadherin function via Dab1/Rap1 to control neuronal migration and lamination in the neocortex.. Neuron [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/21315259/
15. Li X-L, Liu L, Li D-D, He Y-P, Guo L-H, Sun L-P, et al.. Integrin β4 promotes cell invasion and epithelial-mesenchymal transition through the modulation of Slug expression in hepatocellular carcinoma. Scientific Reports [Internet]. 2017Jan13;7(1). Available from: https://www.nature.com/articles/srep40464
16. Emma J van B, Jessy V van A, Pierre AJR, Elly MH. Importance of GFAP isoform-specific analyses in astrocytoma.. Glia [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6617972/
17. Zhihua G, Roseline G. Reelin-Disabled-1 signaling in neuronal migration: splicing takes the stage.. Cellular and molecular life sciences : CMLS [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4457513/
18. Guichen H, Minfeng Z, Damin L, Jinxiao L, Qian T, Chutong X, et al.. The mechanism of ITGB4 in tumor migration and invasion.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335651/
19. Varuzhanyan G, Chen C-C, Freeland J, He T, Tran W, Song K, et al.. PGC-1α drives small cell neuroendocrine cancer progression toward an ASCL1-expressing subtype with increased mitochondrial capacity. Proceedings of the National Academy of Sciences [Internet]. 2024Nov26;121(49). Available from: https://www.pnas.org/doi/10.1073/pnas.2416882121
20. Jyotsana N, Ta KT, DelGiorno KE. The Role of Cystine/Glutamate Antiporter SLC7A11/xCT in the Pathophysiology of Cancer. Frontiers in Oncology [Internet]. 2022Feb23;12. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.858462/full
21. Meissner TB, Li A, Biswas A, Lee K-H, Liu Y-J, Bayir E, et al.. NLR family member NLRC5 is a transcriptional regulator of MHC class I genes. Proceedings of the National Academy of Sciences [Internet]. 2010Jul16;107(31). Available from: https://www.pnas.org/doi/10.1073/pnas.1008684107
22. Available from: https://aacrjournals.org/mct/article/15/5/774/175733/The-Role-of-PGC1-in-Cancer-Metabolism-and-its
23. Itsuki Y, Shige HY, Hironori K. High cell density increases glioblastoma cell viability under glucose deprivation via degradation of the cystine/glutamate transporter xCT (SLC7A11).. The Journal of biological chemistry [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/32265299/
24. Benkő S, Kovács EG, Hezel F, Kufer TA. NLRC5 Functions beyond MHC I Regulation—What Do We Know So Far?. Frontiers in Immunology [Internet]. 2017Feb17;8. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2017.00150/full
25. Yamagishi S, Bando Y, Sato K. Involvement of Netrins and Their Receptors in Neuronal Migration in the Cerebral Cortex. Frontiers in Cell and Developmental Biology [Internet]. 2021Jan15;8. Available from: https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2020.590009/full
26. Jana de S, Eliana M, Martin P, Valérie W, Suzel D, Karl S, et al.. Targeting the extracellular matrix with Tenascin-C-specific CAR T cells extends survival in preclinical models of glioblastoma.. Journal for immunotherapy of cancer [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41188009/
27. Lee K, Kim Y, Lee S-J, Qiang Y, Lee D, Lee HW, et al.. MDGAs interact selectively with neuroligin-2 but not other neuroligins to regulate inhibitory synapse development. Proceedings of the National Academy of Sciences [Internet]. 2012Dec17;110(1). Available from: https://www.pnas.org/doi/10.1073/pnas.1219987110
28. Makoto T, Yuki H, Hong Z, Haruka S, Atsushi T, Shinji S, et al.. Laminar and areal expression of unc5d and its role in cortical cell survival.. Cerebral cortex (New York, NY : 1991) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/21216843/
29. Day ZI, Roberts-Thomson S, Nouri YJ, Dalton NS, Wang SS, Davenport A, et al.. Defining the extracellular matrix for targeted immunotherapy in adult and pediatric brain cancer. npj Precision Oncology [Internet]. 2025Jun14;9(1). Available from: https://www.nature.com/articles/s41698-025-00956-z
30. Kangduk L, Yoonji K, Sung-Jin L, Yuan Q, Dongmin L, Hyun WL, et al.. MDGAs interact selectively with neuroligin-2 but not other neuroligins to regulate inhibitory synapse development.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/23248271/
31. Aya AO, Dmitry B, Julian MR, Olga G, Gleb S, Elena T, et al.. Retrovirus-like gag protein Arc/Arg3.1 is involved in extracellular-vesicle-mediated mRNA transfer between glioma cells.. Biochimica et biophysica acta General subjects [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37995879/
32. Zhongcheng S, Robert SF, Melinda AE, Chunxu G, Anne H, Angela M, et al.. Distinct roles of histamine H1- and H2-receptor signaling pathways in inflammation-associated colonic tumorigenesis.. American journal of physiology Gastrointestinal and liver physiology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6383385/
33. Rodgers SJ, Ooms LM, Oorschot VMJ, Schittenhelm RB, Nguyen EV, Hamila SA, et al.. INPP4B promotes PI3Kα-dependent late endosome formation and Wnt/β-catenin signaling in breast cancer. Nature Communications [Internet]. 2021May25;12(1). Available from: https://www.nature.com/articles/s41467-021-23241-6
34. Available from: https://aacrjournals.org/cancerres/article/84/6_Supplement/2549/739906/Abstract-2549-Activity-regulated-cytoskeleton
35. Available from: https://www.aging-us.com/article/204089/text
36. Clare GF, Lisa MO, Miriel H, Jessica V, Sandra AO, Ewan KM, et al.. Inositol polyphosphate 4-phosphatase II regulates PI3K/Akt signaling and is lost in human basal-like breast cancers.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3009830/
37. Kenzui T, Nobuyoshi A. The Functions and Unique Features of LncRNAs in Cancer Development and Tumorigenesis.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7826647/
38. Xiaoxuan T, Shanxing D, Jie Q, Ruilan Z, Jing L, Limei Z, et al.. Calcium-dependent adhesion protein CDH18, a potential biomarker for prognosis in uterine corpus endometrial carcinoma.. Frontiers in molecular biosciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11864935/
39. Guo KS, Brodsky AS. Tumor collagens predict genetic features and patient outcomes. npj Genomic Medicine [Internet]. 2023Jul6;8(1). Available from: https://www.nature.com/articles/s41525-023-00358-9
40. Available from: https://www.dovepress.com/get_supplementary_file.php?f=231796.docx
41. Available from: https://rupress.org/jcb/article/223/6/e202401057/276615/N-cadherin-dynamically-regulates-pediatric-glioma
42. Leo SP, Paul HH. The pathobiology of collagens in glioma.. Molecular cancer research : MCR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3836242/
43. Victoria H, Nathalie B-K, Alexandre B, Carole C, Aurélie T, Dominique F-B, et al.. GD3 ganglioside is a promising therapeutic target for glioma patients.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11000324/
44. Available from: https://www.dovepress.com/elevated-rgma-expression-predicts-poor-prognosis-in-patients-with-glio-peer-reviewed-fulltext-article-OTT
45. Amit S, Nidhi J, Razif G, Dirk H, Florian K, Robert KS, et al.. Meningioma 1 is indispensable for mixed lineage leukemia-rearranged acute myeloid leukemia.. Haematologica [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7193500/
46. Available from: https://academic.oup.com/noa/article-pdf/6/1/vdae038/57181368/vdae038.pdf
47. Thi LP, Hyun-Jin K, Suk JL, Moon-Chang C, Sung-Hak K. Elevated RGMA Expression Predicts Poor Prognosis in Patients with Glioblastoma.. OncoTargets and therapy [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34588781/
48. Available from: https://iris.unimore.it/handle/11380/1300547
49. Salvatore M, Grazia M, Rina DB, Lucia L, Pierpaolo M, Federica F, et al.. The Extracellular Matrix in Glioblastomas: A Glance at Its Structural Modifications in Shaping the Tumoral Microenvironment-A Systematic Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
50. Yafei L, Ping Y. GPC5 gene and its related pathways in lung cancer.. Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3020075/
51. Kun D, Minghua W. Leucine-rich repeats containing 4 protein (LRRC4) in memory, psychoneurosis, and glioblastoma.. Chinese medical journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10106153/
52. Available from: https://www.ovid.com/journals/injc/pdf/10.1002/ijc.21258~matrix-degrading-proteases-adamts4-and-adamts5-disintegrins
53. Available from: https://aacrjournals.org/cancerres/article/67/1/57/532997/Role-for-Amplification-and-Expression-of-Glypican
54. Available from: https://www.thermofisher.com/antibody/product/LRRC4C-Antibody-Polyclonal/PA5-31873
55. Available from: https://www.proteinatlas.org/ENSG00000182132-KCNIP1
56. Available from: https://www.genecards.org/cgi-bin/carddisp.pl?gene=DCHS2
57. Available from: https://maayanlab.cloud/Harmonizome/gene/GPC5
58. Available from: https://www.ncbi.nlm.nih.gov/gene/65023
59. Available from: https://www.ncbi.nlm.nih.gov/sites/entrez?Db=gene&Cmd=DetailsSearch&Term=54798
60. Available from: https://www.ncbi.nlm.nih.gov/gene/2262
