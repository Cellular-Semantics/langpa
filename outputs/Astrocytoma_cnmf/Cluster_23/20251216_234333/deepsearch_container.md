# Gene Program Markdown Report

## Context
- Cell type: astrocytes, astrocytoma cells
- Disease: astrocytoma, glioblastoma multiforme
- Tissue: brain, central nervous system

## Input Genes
GBP1, ETV6, HLA-E, RSAD2, RUFY4, HERC6, HELZ2, SAMD9, SAMD9L, SAMHD1, GPR39, GCH1, GBP5, GBP3, PARP12, SFMBT2, ERAP2, RNF213, EPSTI1, SP100, DTX3L, SP110, SP140L, DDX60L, DDX60, ... (200 total)

## Program: Type I Interferon Production and Signaling
The type I interferon program controls production of interferon-beta (IFNB1) and initiates JAK2-STAT1-dependent signaling that serves as the master regulator of innate immune responses to viral infection and cellular stress. This program engages pattern recognition receptors and activates a cascade of interferon-stimulated gene expression that creates the antiviral state. Negative regulators (SOCS1, SOCS3) provide feedback inhibition to terminate interferon signaling, preventing pathological inflammation.

**Predicted impacts**
- Activation of downstream STAT1-dependent immune gene expression
- Establishment of antiviral state with multi-layered pathogen restriction
- Induction of MHC expression and antigen presentation machinery
- Suppression of viral replication and tumor cell proliferation
- Recruitment of adaptive immune responses

**Evidence summary**
Type I interferon signaling represents the foundational innate immune response program. IFNB1 production triggers JAK2-STAT1-dependent activation of hundreds of interferon-stimulated genes. The presence of negative regulators (SOCS1, SOCS3) alongside positive regulators indicates dynamic control of signaling amplitude. In astrocytoma context, type I interferon signaling is frequently suppressed through epigenetic and transcriptional mechanisms, but reactivation of this program shows therapeutic promise.

**Atomic biological processes**
- type I interferon production. Genes: IFNB1
  - [1]: IFNB1 encodes interferon-beta which is released as part of innate immune response to pathogens
- JAK-STAT signaling. Genes: JAK2, STAT1
  - [7]: JAK2 participates in signaling cascade from interferon receptors to STAT activation
- interferon signaling feedback inhibition. Genes: SOCS1, SOCS3
  - [2]: SOCS3 encodes STAT-induced STAT inhibitor that negatively regulates cytokine signaling
  - [37]: SOCS1 acts as suppressor of cytokine signaling with multiple immune regulatory functions

**Atomic cellular components**
- interferon-beta cytokine. Genes: IFNB1
  - [1]

**Required genes (not in input)**
- Genes: IFNAR1, IFNAR2, TYK2, STAT2, IRF9
  - [28]: IFNAR1 knockout mice demonstrate critical role of type I interferon receptor in innate immunity

**Program citations**
- [1]: Foundational definition of IFNB1 function
- [2]: SOCS3 negative regulation of cytokine signaling
- [7]: JAK2-STAT signaling involvement in interferon responses

## Program: Type II Interferon Signaling and Th1 Immunity
Type II interferon (interferon-gamma, IFNG) represents the primary effector cytokine of CD8+ cytotoxic T lymphocytes and Th1 cells, establishing the critical link between adaptive and innate immunity. IFNG signaling through IFNGR triggers JAK1/JAK2-STAT1 phosphorylation distinct from type I IFN signaling, inducing complementary but distinct immune programs. This axis drives expression of CXCL10 chemokine for T cell recruitment and HLA expression for antigen presentation.

**Predicted impacts**
- Enhanced expression of MHC class I and antigen presentation machinery
- Increased CXCL10-mediated recruitment of effector T lymphocytes
- Amplification of interferon signaling through positive feedback loops
- Suppression of tumor cell proliferation and induction of apoptosis
- Conversion of tumor microenvironment from immunosuppressive to immune-permissive state

**Evidence summary**
Type II interferon signaling integrates adaptive immune activation with innate immune responses. IFNG produced by CD8+ T cells and Th1 cells binds to IFNGR, triggering JAK1/JAK2-STAT1 signaling that is both overlapping with and distinct from type I IFN signaling. The induction of CXCL10 creates a positive feedback loop that recruits additional T cells. In glioblastoma, this program faces particular challenges including development of interferon-gamma resistance through Notch-mediated mechanisms and epigenetic silencing of STAT1 and CXCL10.

**Atomic biological processes**
- type II interferon signaling. Genes: IFNG, STAT1, JAK2
  - [3]: IFNG encodes interferon-gamma produced by T lymphocytes and NK cells
  - [19]: IFNG signaling drives CXCL10 expression and promotes immune infiltration
- T cell chemotaxis and infiltration. Genes: CXCL10
  - [16]: CXCL10 functions as potent chemoattractant for T lymphocytes
  - [19]: IFNG-CXCL10 axis promotes infiltration of T cells into tumor tissue
- MHC class I upregulation. Genes: STAT1, HLA-A, HLA-B, HLA-C
  - [19]: IFNG drives STAT1-mediated transactivation of HLA genes
- interferon regulatory factor expression. Genes: IRF1, IRF7
  - [57]: IRF proteins control interferon-responsive gene expression

**Required genes (not in input)**
- Genes: IFNGR1, IFNGR2, TYK2, MAPK1, JAK1
  - [19]: IFNG resistance mechanisms in glioma involve alterations in MAPK1 and other signaling molecules

**Program citations**
- [3]: IFNG gene description and function
- [16]: CXCL10 as chemokine ligand
- [19]: Interferon-gamma resistance in glioma development

## Program: Intracellular Pattern Recognition and Viral RNA Sensing
Cells detect viral infection through intracellular pattern recognition receptors (PRRs) including RIG-I-like receptors (RLRs: RIG-I/DDX58, MDA5/IFIH1), toll-like receptors (TLR2, TLR3), and NOD-like receptors (NOD1). These receptors specifically recognize conserved viral molecular patterns including 5'-triphosphate RNA, long double-stranded RNA, and other pathogen-associated molecular patterns. Recognition triggers mitochondrial antiviral signaling (MAVS) and downstream activation of TBK1 and IKK, leading to IRF3/IRF7 activation and type I interferon production. RNA editing by ADAR1 prevents pathological activation of MDA5 by self-derived dsRNA.

**Predicted impacts**
- Detection of viral infection or endogenous dsRNA triggers
- Activation of MAVS-dependent signaling cascade
- TBK1-mediated phosphorylation of IRF3 and IRF7
- Type I interferon production and ISG induction
- Establishment of antiviral state and programmed cell death

**Evidence summary**
Intracellular pattern recognition receptors constitute the sensory apparatus for detecting viral infection. RIG-I and MDA5 are activated by distinct forms of viral RNA, triggering mitochondrial signaling through MAVS. TLR2 and TLR3 recognize additional viral patterns. The presence of IFIH1 (MDA5), TLR2, TLR3, and NOD1 in the input list indicates robust capacity for viral sensing. Notably, RNA editing by ADAR1 prevents pathological activation of these sensors by self-derived dsRNA, suggesting that dysregulation of RNA editing could either trigger or suppress antiviral responses in astrocytomas.

**Atomic biological processes**
- 5-triphosphate RNA recognition. Genes: DDX58
  - [30]: IFIH1 encodes MDA5 which senses viral RNA through pattern recognition
- long dsRNA recognition. Genes: IFIH1
  - [30]: MDA5 recognizes long double-stranded RNA with filament formation
  - [28]: ADAR1 editing of dsRNA prevents MDA5-mediated recognition of self RNA
- Toll-like receptor signaling. Genes: TLR2, TLR3
  - [29]: TLR2 participates in pathogen recognition and apoptosis regulation
  - [31]: TLR3 enables pattern recognition receptor activity
- NOD-like receptor signaling. Genes: NOD1
  - [21]: NOD1 participates in cytokine response and antiviral immunity
- RNA editing and dsRNA sensing suppression.
  - [28]: ADAR1 editing suppresses MDA5-dependent interferon signaling by editing dsRNA

**Atomic cellular components**
- RIG-I-like receptor. Genes: DDX58, IFIH1
  - [30]: IFIH1 encodes MDA5 pattern recognition receptor
- Toll-like receptor. Genes: TLR2, TLR3
  - [31]: TLR3 enables pattern recognition receptor activity

**Required genes (not in input)**
- Genes: MAVS, TBK1, IKBKE, IRF3, NEMO, IKK-beta
  - [28]: MAVS and TBK1 are essential adapters downstream of RIG-I and MDA5

**Program citations**
- [28]: ADAR1 RNA editing suppresses MDA5-dependent interferon responses
- [30]: IFIH1 encodes MDA5 intracellular RNA sensor
- [31]: TLR3 pattern recognition receptor function

## Program: Interferon-Stimulated Gene Expression and Antiviral State
Type I and type II interferon signaling activates expression of approximately 300 interferon-stimulated genes (ISGs) that collectively create the antiviral state. This program includes multiple families of proteins: GTPases (GBP1-5) that oligomerize on pathogen compartments, interferon-induced proteins with tetratricopeptide repeats (IFIT1-3), ubiquitin ligases (TRIM family, HERC family), RNA-binding proteins (ZAP/PARP13, PARP9), nucleotide metabolism enzymes, and protein modifiers (ISG15). These genes functionally restrict viral replication through multiple mechanisms including direct viral recognition, interference with viral gene expression, and activation of cell death pathways.

**Predicted impacts**
- Multi-layered viral restriction through redundant and complementary mechanisms
- Prevention of viral gene expression and replication
- Innate immune activation and type I interferon amplification
- Enhanced adaptive immune cell recruitment and activation
- Potential tumor cell growth restriction if expressed in tumor cells

**Evidence summary**
The interferon-stimulated gene program represents the executed arm of interferon signaling, converting transcription factor activation (STAT1) into effector functions that restrict viral replication. The presence of multiple protein families with overlapping antiviral functions (GBPs, TRIMs, HERCs, PARPs, IFITs) indicates redundancy and robustness of this defense system. In astrocytoma context, expression of this program would restrict tumor growth through multiple mechanisms. The presence of ISG15 as both a modifier and a molecule that boosts adaptive immunity suggests coordinated innate-adaptive immune activation.

**Atomic biological processes**
- GTP-mediated viral restriction. Genes: GBP1, GBP2, GBP3, GBP4, GBP5, MX1, MX2
  - [6]: GBP1 protects against mitochondrial dysfunction and preserves immune function
- ubiquitin-mediated viral protein degradation. Genes: TRIM5, TRIM22, TRIM25, TRIM38, TRIM56, HERC5, HERC6
  - [13]: TRIM proteins catalyze K63-linked ubiquitination of RIG-I and other substrates
- viral RNA-specific degradation. Genes: ZC3HAV1
  - [13]: PARP13 (ZAP) binds viral RNA and promotes degradation through zinc finger domain
- ISGylation-mediated protein modification. Genes: ISG15
  - [15]: ISG15 ubiquitin-like modifier boosts CTL response through innate NK cell-dependent route
  - [18]: ISG15 modulates cancer stem cell-like characteristics in anaplastic thyroid carcinoma
- translational repression and viral replication inhibition. Genes: IFIT1, IFIT2, IFIT3
  - [15]: ISG15 modification blocks coxsackievirus protein synthesis
- PARP-family viral restriction. Genes: PARP9, PARP10, PARP12, PARP13, DTX3L
  - [13]: PARP9 enhances interferon signaling through DTX3L ubiquitin ligase complex
  - [13]: PARP12 inhibits viral replication through NS1 and NS3 degradation

**Atomic cellular components**
- GTPase protein complex. Genes: GBP1, GBP2, GBP3, GBP4, GBP5
  - [6]
- ISG15 ubiquitin-like modifier. Genes: ISG15
  - [15]: ISG15 is an ubiquitin-like protein that undergoes conjugation to target proteins

**Required genes (not in input)**
- Genes: STAT1, STAT2, IRF9, RNase L
  - [15]: STAT signaling required for ISG induction

**Program citations**
- [6]: GBP1 antiviral functions
- [13]: TRIM and PARP family antiviral functions
- [15]: ISG15 functions in immunity
- [18]: ISG15 in cancer stem cells

## Program: Immune Checkpoint Regulation and T Cell Suppression
Immune checkpoint molecules represent a critical mechanism through which tumors evade anti-tumor immunity by delivering inhibitory signals to effector T cells. This program encompasses the PD-1/PD-L1 axis (CD274 encoding PD-L1 and PDCD1LG2 encoding PD-L2), related checkpoint molecules (BTN3A1), and TNF superfamily checkpoint ligands (TNFSF14 encoding LIGHT). PD-L1 engagement with PD-1 on T cell surface transmits inhibitory signaling that suppresses TCR signaling, cytokine production, proliferation, and cytotoxic functions. Checkpoint inhibitor therapy blocking this axis has demonstrated clinical efficacy in multiple cancer types.

**Predicted impacts**
- Suppression of T cell receptor signaling
- Reduced T cell proliferation and cytokine production
- Decreased cytotoxic granule release and tumor cell killing
- Promotion of T regulatory cell differentiation
- Immune evasion and tumor progression

**Evidence summary**
PD-L1 (CD274) represents one of the most important immune evasion mechanisms in glioblastoma and other tumors. Expression of PD-L1 on tumor cells creates an immunosuppressive microenvironment that blunts anti-tumor CD8+ T cell responses. The presence of both PD-L1 and PD-L2 in the input list indicates multiple checkpoint ligands available for immune evasion. PD-L1 expression is induced through Wnt/β-catenin, NF-κB, and STAT3 pathways, all of which are often activated in glioblastoma. Checkpoint inhibitor therapies targeting this axis have demonstrated efficacy in other cancers and are under investigation in glioblastoma.

**Atomic biological processes**
- PD-L1/PD-1 inhibitory signaling. Genes: CD274, PDCD1LG2
  - [4]: CD274 encodes immune inhibitory receptor ligand expressed on T cells and B cells
  - [10]: PD-L1 regulates ciliogenesis and Hedgehog signaling in addition to immune checkpoint functions
  - [38]: PD-1/PD-L1 axis involved in microglial polarization and glioma interactions
- PD-L1 transcriptional induction. Genes: CD274, CTNNB1
  - [36]: CTNNB1-mediated Wnt/beta-catenin signaling induces PD-L1 transcription in glioblastoma
  - [12]: NF-kappaB/STAT3 signaling regulates PD-L1 expression
- butyrophilin checkpoint signaling. Genes: BTN3A1
  - [4]
- TNF superfamily checkpoint ligand signaling. Genes: TNFSF14
  - [4]

**Atomic cellular components**
- PD-L1 immune checkpoint ligand. Genes: CD274
  - [4]

**Required genes (not in input)**
- Genes: PDCD1, HAVCR2, LAG3, CTLA4
  - [4]: PD-1 and other checkpoint receptors on T cells receive inhibitory signals from checkpoint ligands

**Program citations**
- [4]: CD274 immune checkpoint molecule definition
- [10]: PD-L1 regulation and Hedgehog signaling
- [36]: PD-L1 induction through Wnt signaling in glioblastoma
- [12]: NF-kappaB/STAT3 control of PD-L1

## Program: Antigen Processing and Presentation
Adaptive immune responses require that astrocytoma-associated antigens be processed and presented on major histocompatibility complex (MHC) molecules to activate CD8+ and CD4+ T cells. This program encompasses MHC class I-restricted presentation (involving HLA-A, HLA-B, HLA-C, HLA-E, HLA-F) and MHC class II-restricted presentation (involving CIITA as master regulator and NLRC5 as major MHC class I regulator). The program includes proteasomal degradation (PSMB9 immunoproteasome subunit), peptide transport into ER (TAP1, TAP2), and peptide-MHC complex assembly (TAPBP/tapasin).

**Predicted impacts**
- Processing of tumor-associated antigens (TAAs) into immunogenic peptides
- Presentation of TAA-derived peptides on MHC class I to CD8+ T cells
- Presentation of TAA-derived peptides on MHC class II to CD4+ helper T cells
- Priming of anti-tumor CD8+ and CD4+ T cell responses
- Activation of both cytotoxic and helper immune functions

**Evidence summary**
Antigen presentation represents the essential step linking tumor antigen recognition to adaptive immune activation. The complete antigen processing machinery is present in the input list: proteasomal degradation (PSMB9), peptide transport (TAP1/TAP2), complex assembly (TAPBP), and MHC molecules (HLA-A/B/C/E/F). CIITA and NLRC5 control expression of this entire program at the transcriptional level. In glioblastoma, downregulation of MHC class I expression represents a canonical immune evasion mechanism, indicating that restoration of MHC expression through CIITA or NLRC5 activation could enhance immunogenicity.

**Atomic biological processes**
- proteasomal antigen processing. Genes: PSMB9
  - [26]
- TAP-mediated peptide transport. Genes: TAP1, TAP2
  - [26]
- peptide loading onto MHC class I. Genes: TAPBP
  - [26]
- MHC class I expression. Genes: HLA-A, HLA-B, HLA-C, HLA-E, HLA-F
  - [26]
- MHC class II master transcriptional regulation. Genes: CIITA
  - [23]: CIITA functions as master controller of adaptive and intrinsic immunity
- MHC class I transcriptional regulation. Genes: NLRC5
  - [21]: NLRC5 plays role in cytokine response and antiviral immunity

**Atomic cellular components**
- MHC class I molecule. Genes: HLA-A, HLA-B, HLA-C, HLA-E, HLA-F
  - [26]: HLA-E belongs to HLA class I heavy chain paralogues
- proteasome. Genes: PSMB9
  - [26]
- TAP complex. Genes: TAP1, TAP2
  - [26]

**Required genes (not in input)**
- Genes: CTSB, CTSL, CTSS, PSMA1, PSMA2, PSMB1, PSMB8, PSMB10
  - [26]

**Program citations**
- [21]: NLRC5 role in antiviral immunity and MHC expression
- [23]: CIITA master controller of immune gene expression
- [26]: HLA and MHC molecule biology

## Program: Death Receptor Signaling and Regulated Cell Death
Regulated cell death programs including apoptosis, pyroptosis, and necroptosis represent critical mechanisms through which cytotoxic lymphocytes eliminate tumor cells. This program encompasses TNF superfamily death ligands (TNFSF10 encoding TRAIL), death receptor-associated proteins (CASP4, MLKL), and regulators of these pathways (CFLAR encoding c-FLIP, ZBP1). TRAIL engages death receptors DR4/DR5 on target cells, recruiting FADD and caspase-8 to initiate caspase-dependent apoptosis. c-FLIP inhibits both death receptor-induced apoptosis and caspase-1-mediated pyroptosis. Necroptosis can be triggered by ZBP1-RIPK3 signaling when caspase-8 is inhibited.

**Predicted impacts**
- Tumor cell death in response to cytotoxic lymphocyte contact
- Activation of apoptotic, pyroptotic, or necroptotic cell death
- Potential immune activation through pyroptosis-induced cytokine release
- Tumor growth suppression and elimination of immune-resistant cells

**Evidence summary**
Death receptor signaling represents the primary mechanism through which CD8+ cytotoxic T lymphocytes kill tumor cells. TRAIL (TNFSF10) engagement of death receptors activates caspase-8-dependent apoptosis. c-FLIP (CFLAR) provides a critical brake on this pathway, explaining why tumors expressing high c-FLIP show resistance to death receptor signaling. The presence of both TNFSF10 and CFLAR in the input list indicates tension between death-promoting and death-inhibiting signals. Pyroptosis represents an alternative cell death pathway that generates additional immune activation through cytokine release. The presence of ZBP1 and MLKL indicates capacity for necroptotic cell death.

**Atomic biological processes**
- TRAIL-mediated apoptosis induction. Genes: TNFSF10
  - [47]: Death ligands including TRAIL trigger apoptosis by promoting caspase-8 dimerization and activation
- caspase-8-mediated apoptotic signaling. Genes: CFLAR
  - [47]: CFLAR regulates caspase-8 activation downstream of death receptors
- caspase-4-mediated pyroptosis. Genes: CASP4
  - [27]: caspase-4 activation induces pyroptosis, though NLRP3 inflammasome activation required for IL-1beta maturation
- gasdermin-mediated regulated cell death.
  - [25]: Pyroptosis is gasdermin-mediated regulated cell death that recruits immune cells
- necroptosis execution. Genes: MLKL
  - [47]: MLKL functions as executor of necroptosis downstream of RIPK3
- ZBP1-RIPK3 necroptosis trigger. Genes: ZBP1
  - [47]: ZBP1 senses viral infection and triggers RIPK3-mediated necroptosis

**Atomic cellular components**
- death receptor. Genes: TNFSF10
  - [47]

**Required genes (not in input)**
- Genes: FADD, CASP8, RIPK3, RIPK1, GSDMD, NLRP3, CASPASE1
  - [47]: FADD, CASP8, RIPK3 are essential adapters in death receptor signaling

**Program citations**
- [25]: Pyroptosis definition and immune recruitment
- [27]: Caspase-4 in pyroptosis
- [47]: Death receptor signaling and c-FLIP regulation

## Program: Metabolic Reprogramming and Tryptophan Metabolism
Immune cell function depends critically on metabolic states, with tryptophan metabolism representing a critical immune regulatory node. IDO1 (indoleamine 2,3-dioxygenase 1) catalyzes conversion of tryptophan to kynurenine, depleting tryptophan and generating immunosuppressive metabolites. IDO1 expression is directly induced by STAT1 downstream of interferon signaling, creating a negative feedback loop. Kynurenine pathway metabolites promote T regulatory cell (Treg) differentiation and suppress effector T cell functions. GCH1 catalyzes BH4 synthesis critical for NO production and immune function. SAMHD1 regulates intracellular dNTP levels critical for cell proliferation and genome stability, with depletion in tumors increasing chemotherapy sensitivity and immune activation.

**Predicted impacts**
- Suppression of effector T cell functions through tryptophan depletion
- Promotion of T regulatory cell differentiation via kynurenine metabolites
- Immune evasion through metabolic reprogramming
- Potential sensitization to chemotherapy through SAMHD1 targeting
- Enhanced tumor immunity through IDO1 inhibition

**Evidence summary**
Tryptophan metabolism has emerged as a critical immune regulatory checkpoint in cancer. IDO1-mediated tryptophan depletion represents a classic tumor immune evasion mechanism present in glioblastoma. The therapeutic potential of combining IDO1 inhibition with radiotherapy has been demonstrated experimentally, suggesting clinical translation potential. SAMHD1 represents an additional metabolic checkpoint regulating dNTP pools; depletion of SAMHD1 increases sensitivity to nucleoside-based chemotherapy and activates innate immunity through enhanced viral-like sensing. The presence of both IDO1 and SAMHD1 in the input list highlights metabolic checkpoints as key vulnerabilities of astrocytomas.

**Atomic biological processes**
- tryptophan catabolism. Genes: IDO1
  - [9]: Tryptophan metabolism represents metabolic node in glioblastoma
  - [11]: IDO1 promotes tryptophan metabolism and immune suppression in colorectal cancer
- kynurenine pathway activation. Genes: IDO1
  - [9]: IDO1 inhibition enhances RT response in glioblastoma
- tetrahydrofolate synthesis. Genes: GCH1
  - [30]
- dNTP level regulation. Genes: SAMHD1
  - [33]: SAMHD1 dNTPase regulates intracellular dNTP levels for cell proliferation control
  - [35]: SAMHD1 suppresses innate immune responses through dNTP regulation in differentiated monocytes
- nucleotide kinase activity. Genes: CMPK2
  - [30]

**Required genes (not in input)**
- Genes: STAT1, KYNU, AADC, ALDH1A1, AHR, IL6, IFNG
  - [9]: Interferon-STAT1 axis induces IDO1 expression

**Program citations**
- [9]: IDO1 in glioblastoma metabolism and RT response
- [11]: IDO1 immune suppression in cancer
- [33]: SAMHD1 in tumor cell chemotherapy resistance
- [35]: SAMHD1 innate immune suppression

## Program: Epigenetic Regulation of Immune Responses
Gene expression is controlled not only at the transcriptional level but also through epigenetic mechanisms including histone post-translational modifications, DNA methylation, and chromatin accessibility. EZH2 catalyzes H3K27 trimethylation, a repressive histone mark, and high EZH2 expression is associated with poor prognosis in glioblastoma. EZH2 inhibition promotes tumor immunogenicity through reactivation of silenced immune programs. SP100, SP110, and SP140 encode nuclear body proteins (PML nuclear bodies) that regulate immune-related transcription and serve as predictive biomarkers of immunotherapy response. These proteins represent epigenetic regulators controlling the balance between immune activation and tolerance.

**Predicted impacts**
- Reactivation of silenced immune genes through EZH2 inhibition
- Enhanced immune checkpoint expression and function
- Increased interferon responsiveness through SP proteins
- Synergy with checkpoint inhibitor therapy
- Improved tumor immunogenicity and immune cell infiltration

**Evidence summary**
Epigenetic mechanisms represent a critical layer of immune gene regulation in astrocytoma. High EZH2 expression and H3K27me3 deposition at immune loci represent mechanisms of immune evasion. EZH2 inhibitors are under investigation for glioblastoma based on preclinical evidence that they enhance immunogenicity. PML nuclear bodies serve as regulatory hubs integrating interferon signaling with transcriptional control. SP proteins modulate STAT1 signaling and represent novel immune regulatory factors. The presence of these epigenetic regulators in the input list reflects the multi-layered epigenetic control of immune responses.

**Atomic biological processes**
- PRC2-mediated immune gene silencing. Genes: EZH2
  - [50]: EZH2 inhibition promotes tumor immunogenicity
- H3K27 trimethylation. Genes: EZH2
  - [50]: EZH2 catalyzes H3K27 trimethylation repressive histone mark
- nuclear body immune regulation. Genes: SP100, SP110, SP140L, PML
  - [56]: SP110 is leukocyte-specific nuclear body component
  - [57]: SP140 inhibits STAT1 signaling and induces IFN-gamma in tumor-associated macrophages
- immune checkpoint biomarker prediction. Genes: SP140L
  - [57]: SP140 is predictive biomarker of immunotherapy response

**Atomic cellular components**
- PRC2 complex. Genes: EZH2
  - [50]
- PML nuclear body. Genes: SP100, SP110, PML
  - [5]: PML participates in type I interferon-induced ISG expression
  - [56]: SP100 and SP110 are nuclear body scaffold proteins

**Required genes (not in input)**
- Genes: SUZ12, EED, DNMT1, DNMT3A, DNMT3B, HDAC1, HDAC2
  - [50]: PRC2 complex members control epigenetic repression

**Program citations**
- [5]: PML nuclear body and interferon-induced ISG expression
- [50]: EZH2 and tumor immunogenicity
- [56]: SP100 nuclear body protein
- [57]: SP140 and immunotherapy response prediction

## Program: Cell Adhesion and Immune Cell Trafficking
Tumor cell invasion and immune cell trafficking depend critically on cell adhesion molecules and signaling proteins controlling cell-cell and cell-matrix interactions. ICAM1 encodes intercellular adhesion molecule 1, which mediates T cell adhesion to endothelial cells and infiltration into tumor tissue. ICAM1 expression is induced by interferons and TNF, indicating inflammatory microenvironment. Focal adhesion kinases (PTK2/FAK, PTK2B/Pyk2) regulate cell adhesion, migration, and invasion through integrin-mediated signaling. PARD3 controls epithelial cell polarity and epithelial-mesenchymal transition. EPCAM and LAMB1 participate in cell-cell adhesion and extracellular matrix interactions. CD44 functions as a cell adhesion molecule and hyaluronic acid receptor implicated in metastasis.

**Predicted impacts**
- Enhanced immune cell trafficking into tumor microenvironment
- Promotion of tumor cell invasion and metastasis
- EMT-mediated acquisition of stem cell-like properties
- Increased T cell-tumor cell interactions
- Potential enhancement or suppression of anti-tumor immunity depending on cell type

**Evidence summary**
Cell adhesion molecules and associated signaling proteins control the physical and chemical interactions between tumor cells and immune cells. ICAM1 promotes immune cell trafficking into tumors, potentially enhancing anti-tumor immunity. However, the presence of EMT-promoting factors (PARD3, EPCAM, CD44) suggests tumor cells may acquire invasive properties and potentially EMT-driven immune evasion. Focal adhesion kinases regulate both tumor cell and immune cell migration. The balance between these factors likely determines whether the adhesion program promotes or suppresses anti-tumor immunity.

**Atomic biological processes**
- T cell extravasation and infiltration. Genes: ICAM1
  - [42]: ICAM1 encodes cell surface glycoprotein mediating T cell adhesion on endothelial cells
- focal adhesion signaling. Genes: PTK2B
  - [41]: PTK2B regulates cell adhesion and inside-out signaling
  - [44]: FAK-paxillin interactions indispensable for cell adhesion and migration
- epithelial-mesenchymal transition. Genes: PARD3, EPCAM, CD44
  - [45]: EPCAM promotes metastasis through CD44 signaling
  - [47]: PARD3 participates in EMT regulation
- extracellular matrix interaction. Genes: LAMB1
  - [45]: EPCAM and related molecules regulate cell-matrix interactions

**Atomic cellular components**
- ICAM1 adhesion molecule. Genes: ICAM1
  - [42]: ICAM1 is intercellular adhesion molecule
- focal adhesion complex. Genes: PTK2B
  - [44]: FAK-paxillin interactions in focal adhesion assembly

**Required genes (not in input)**
- Genes: ITGA1, ITGA2, ITGB1, ITGB3, PECAM1, JAMS, SELECTINS
  - [42]: Integrins and other adhesion molecules in immune trafficking

**Program citations**
- [41]: PTK2B in cell adhesion
- [42]: ICAM1 cell adhesion molecule
- [44]: FAK and focal adhesion signaling
- [45]: EPCAM and CD44 in metastasis

## Program: Complement Regulation and Inflammatory Control
The complement system represents a critical component of innate immunity that can target tumor cells for destruction or alternatively suppress immune responses depending on context. CFH encodes complement factor H, which regulates the alternative complement pathway by preventing uncontrolled C3 activation and protecting host cells from complement-mediated damage. CFHR1 participates in atypical hemolytic uremic syndrome (aHUS) through dysregulation of complement. SERPING1 encodes C1 esterase inhibitor, which inhibits multiple serine proteases in complement cascade. The balance between complement activation and inhibition influences inflammatory responses and anti-tumor immunity.

**Predicted impacts**
- Regulation of complement-mediated tumor cell destruction
- Suppression of excessive complement-driven inflammation
- Modulation of complement-C5a-mediated immune cell recruitment
- Prevention of complement-induced bystander damage
- Balance between complement-dependent cell-mediated cytotoxicity and immune tolerance

**Evidence summary**
Complement represents a double-edged sword in anti-tumor immunity: complement activation can promote direct tumor cell destruction through membrane attack complex formation, but excessive complement activation can also suppress adaptive immunity through C5a-mediated recruitment of immunosuppressive myeloid cells. The presence of complement inhibitors (CFH, SERPING1) alongside potential complement activators suggests dynamic regulation of complement in the astrocytoma microenvironment. CFH loss in retinal pigment epithelium leads to inflammation and NF-kappaB dysregulation, suggesting that complement regulation is intimately linked to inflammatory signaling.

**Atomic biological processes**
- alternative complement pathway regulation. Genes: CFH, CFHR1
  - [46]: CFH regulates complement alternative pathway and NF-kappaB signaling
- complement cascade inhibition. Genes: SERPING1
  - [46]
- complement-mediated inflammation. Genes: CFH, CFHR1
  - [46]: Complement dysregulation contributes to inflammation
  - [48]: Complement alternative pathway dysregulation in aHUS

**Required genes (not in input)**
- Genes: C3, C5, C5AR1, C5AR2, C1Q, C1R, C1S, C2, C4A, C4B, FB, FD
  - [46]: Core complement pathway components

**Program citations**
- [46]: CFH regulation of complement and NF-kappaB
- [48]: CFHR1 and complement dysregulation

## Program: RNA Processing and Stability Control
Multiple genes in the input list participate in RNA processing, stability, and modifications that control expression of immune genes and viral restriction factors. DDX60 and DDX60L encode helicases with roles in RNA sensing and innate immune activation. HELZ2 participates in helicase-dependent processes. ZC3HAV1 encodes a zinc finger CCCH-type containing viral-associated protein involved in viral restriction and antiviral immunity. WARS encodes tryptophanyl-tRNA synthetase loading tryptophan onto tRNA during protein synthesis. ZCCHC2 participates in zinc finger motif-dependent RNA binding. PLSCR1 (phospholipid scramblase 1) participates in antiviral responses and apoptosis. These genes collectively regulate the synthesis, modification, and degradation of RNA molecules critical to immune responses.

**Predicted impacts**
- Enhanced recognition of viral and self-derived dsRNA through helicase activity
- Restriction of viral replication through direct RNA binding and degradation
- Regulation of immune gene expression through RNA stability control
- Modulation of cell death pathways through RNA-mediated mechanisms
- Fine-tuning of interferon responses through RNA processing

**Evidence summary**
RNA processing represents an underappreciated layer of immune gene regulation. DDX helicases participate in MDA5-dependent viral RNA sensing, while ZAP/PARP13 directly binds viral RNA for restriction. The presence of these RNA-processing factors indicates sophisticated control of viral and potentially tumor-associated RNA recognition. WARS controls tryptophan availability for protein synthesis, linking to tryptophan metabolism. PLSCR1 participates in antiviral responses and apoptosis. The RNA processing program reflects the critical importance of RNA-level mechanisms in innate immunity.

**Atomic biological processes**
- dsRNA-dependent helicase activity. Genes: DDX60, DDX60L, DDX58
  - [28]: DDX helicase proteins participate in MDA5-dependent RNA sensing
- viral RNA restriction. Genes: ZC3HAV1
  - [28]
- tRNA charging and protein synthesis. Genes: WARS
  - [30]
- RNA binding and processing. Genes: ZCCHC2
  - [28]
- antiviral and apoptotic signaling. Genes: PLSCR1
  - [30]

**Required genes (not in input)**
- Genes: ADAR1, RNase L, PKR, OAS enzymes, MAVS
  - [28]: ADAR1 RNA editing suppresses MDA5-dependent responses

**Program citations**
- [28]: DDX60 and RNA helicase activity in antiviral immunity
- [30]: RNA binding and antiviral functions

## Program: Astrocyte Activation and Neuroinflammation
Astrocytes represent the primary glial cell type in the central nervous system and serve critical roles in both neural support and immune regulation. Recent evidence from traumatic brain injury demonstrates that astrocytes undergo robust activation characterized by pro-inflammatory gene expression programs in the acute phase, followed by gradual shift toward mixed phenotype with neurodegenerative and regenerative elements in chronic phases. Key acute-phase genes include pro-inflammatory cytokines (IL-1, IL-6, TNF, IFNG), interferon-responsive genes (IFN-α/γ responses), complement activation (C4b), and apoptosis-related genes. This program integrates innate immune sensor activation (TLR2, TLR3, MYD88) with downstream inflammatory signaling to coordinate astrocyte-mediated neuroinflammation.

**Predicted impacts**
- Robust astrocyte activation with pro-inflammatory gene expression
- Enhanced interferon responsiveness and ISG induction
- Increased cytokine and chemokine production promoting immune cell infiltration
- Activation of complement cascade and apoptosis programs
- Transition from acute inflammatory to chronic degenerative phenotype
- Potential neural tissue damage and inflammation-mediated pathology in astrocytoma context

**Evidence summary**
Astrocytes represent the cellular origin of astrocytomas, and understanding astrocyte biology is critical for comprehending tumor-immune interactions in these malignancies. Recent evidence shows that astrocytes mount robust interferon responses characterized by upregulation of TLR signaling, pro-inflammatory cytokines, and interferon-responsive genes. The acute inflammatory phase gradually transitions toward a mixed phenotype incorporating neurodegenerative genes. In astrocytoma context, malignant transformation likely involves either constitutive suppression of these acute inflammatory programs (promoting immune evasion) or dysregulated maintenance of chronic inflammatory programs (promoting tumor growth and resistance). The presence of TLR genes, interferon-responsive genes, and IL1R1 in the input list reflects the capacity of astrocytes to mount innate immune responses.

**Atomic biological processes**
- pro-inflammatory cytokine expression. Genes: IL1R1, IL15
  - [52]: TBI astrocytes display upregulation of pro-inflammatory cytokines IL-1, IL-6, TNF, IFN-γ
- Toll-like receptor signaling. Genes: TLR2
  - [52]: Acute TBI astrocytes show enrichment in Toll-like receptor signaling genes Tlr2, Myd88
- interferon-alpha response.
  - [52]: GSEA reveals significant enrichment in interferon-α responses in acute TBI astrocytes
- interferon-gamma response.
  - [52]: GSEA reveals significant enrichment in interferon-γ responses in acute TBI astrocytes
- complement activation.
  - [52]: Genes involved in complement activation (C4b) enriched in acute TBI astrocytes
- apoptosis program.
  - [52]: Apoptosis-related genes including Tradd enriched in acute TBI astrocytes
- chronic neurodegeneration and cellular dysfunction.
  - [52]: Chronic TBI phase shows upregulation of genes involved in neurodegeneration including App and S1pr1

**Atomic cellular components**
- astrocyte activation state. Genes: GFAP, APOE, CD44, CXCL10
  - [52]: Pan-reactive astrocyte markers including Gfap, Apoe, Cd44, Serpina3n, Cxcl10 prominently expressed

**Required genes (not in input)**
- Genes: GFAP, APOE, IL1B, IL6, TNF, IFNG, MYD88, TREM2, TYROBP, INPP5D
  - [52]: Key astrocyte activation genes and markers identified in comprehensive astrocyte transcriptomic analysis

**Program citations**
- [52]: Comprehensive RNA-seq analysis of astrocyte activation following traumatic brain injury

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/3456
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/9021
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/3458
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/5371
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/14468
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/15978
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/3620
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/15930
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
12. 12. Xia J, Tang X, Zhu Q, Xu Y. PARPs in liver diseases. npj Gut and Liver [Internet]. 2025Dec3;2(1). Available from: https://www.nature.com/articles/s44355-025-00043-x
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/100038882
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/3627
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=9636
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/57674
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/84166
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/4261
20. 20. Lilljebjörn H, Peña-Martínez P, Thorsson H, Henningsson R, Rissler M, Landberg N, et al.. The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-66546-6
21. 21. Shang Q, Wang Z, Peng J, Yang D, Li W, Huang X, et al.. Epithelial pyroptosis-induced TREM1+ macrophages activate Th17 cells to accelerate oral mucosal inflammation. Cell Death Discovery [Internet]. 2025Nov29;. Available from: https://www.nature.com/articles/s41420-025-02853-7_reference.pdf
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/3133
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/837
24. 24. Sun T, Li Q, Geisinger JM, Hu S-B, Fan B, Su S, et al.. ADAR1 editing is necessary for only a small subset of cytosolic dsRNAs to evade MDA5-mediated autoimmunity. Nature Genetics [Internet]. 2025Dec;57(12). Available from: https://www.nature.com/articles/s41588-025-02430-9
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/7097
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/64135
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/142980
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/4299
29. 29. Sun J, Zheng W, Zhang Z-G, Zhou H, Wang S, Huang D, et al.. Selective depletion of tumor-associated SAMHD1 enhances chemotherapeutic efficacy and antitumor immune responses. Signal Transduction and Targeted Therapy [Internet]. 2025Dec15;10(1). Available from: https://www.nature.com/articles/s41392-025-02523-1
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/6689
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/25939
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/8651
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/8835
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/3554
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/2185
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/3383
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/16177
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/14083
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/4072
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/3075
42. 42. Newton K, Wickliffe KE, Maltzman A, Dugger DL, Reyes JJ, Bacarro N, et al.. cFLIP suppresses caspase-1- and MLKL-independent perinatal lethality driven by auto-processing impaired caspase-8 D387A. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01650-0
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/3078
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/8837
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
46. 46. Stark JC, Gray MA, Ibarlucea-Benitez I, Lustig M, Bond A, Cho B, et al.. Antibody-lectin chimeras for glyco-immune checkpoint blockade. Nature Biotechnology [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41587-025-02884-6
47. 47. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
48. 48. Shuo S, Yu H, Haiying L, Chengyan W, Shu Z, Xiaowei Z, et al.. Beyond the genome: epigenetic regulation of immune responses and T cells in brain tumors.. Frontiers in immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41341594/?fc=None&ff=20251205024612&v=2.18.0.post22+67771e2
49. 49. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/3431
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/11262
52. 52. Available from: http://json-schema.org/draft-07/schema#",
53. 53. Available from: their functional roles in interferon signaling
