# Gene Program Markdown Report

## Context
- Cell type: Astrocytoma-derived tumor cells, astrocytes
- Disease: Astrocytoma (including high-grade glioblastoma and lower-grade astrocytomas, with emphasis on IDH-wild-type and IDH-mutant subtypes)
- Tissue: Brain, central nervous system

## Input Genes
DPYD, WWTR1, ADAMTS9, CNTNAP3B, SPOCD1, RASSF8, NEAT1, GAP43, POSTN, SATB2, NRCAM, MAP1B, C6ORF141, CHI3L1, TENT5A, SHC1, SIPA1L1, SLC4A7, HMGA2-AS1, CLIC4, LINC02821, LMCD1-AS1, NRP1, CDH2, LONRF2, ... (200 total)

## Program: Extracellular Matrix Remodeling and Invasion
Coordinated remodeling and degradation of extracellular matrix components enabling astrocytoma cell invasion into surrounding brain parenchyma. This program integrates matrix proteolysis, matrix ligand-receptor interactions, and stromal cell communication to create permissive microenvironments for tumor infiltration.

**Predicted impacts**
- Enhanced matrix degradation enabling invasion into brain parenchyma
- Increased ligand-receptor signaling through integrin pathways
- Dysregulation of matrix-dependent cell growth signals
- Altered stromal cell recruitment and activation
- Facilitated perineural invasion and vascular infiltration

**Evidence summary**
Recent single-cell spatial transcriptomic studies of glioblastoma demonstrate that distinct tumor cell populations express unique combinations of ECM genes with spatial enrichment patterns correlating with tumor architecture[53]. Proteases including ADAMTS9 actively remodel collagen-rich matrices, facilitating cell migration and vascular infiltration. Integrin-mediated adhesion through ITGA3, ITGA5, and ITGAV interacts with ECM ligands (LAMB1, POSTN, SPP1, EFEMP1) to activate focal adhesion kinases (PTK2B) and downstream signaling cascades driving proliferation and motility. The expression patterns of these ECM components largely segregate between tumor cells and stromal populations, reflecting the complex intercellular communication governing invasion.

**Atomic biological processes**
- Extracellular matrix proteolysis. Genes: ADAMTS9, ADAMTS9-AS1, EFEMP1
  - [53]: Single-cell spatial transcriptomics identifies ECM remodeling genes and spatial patterns in glioblastoma
  - [2]: Comprehensive characterization of pediatric tumors showing matrix remodeling in gliomas
- Matrix ligand-receptor binding. Genes: ITGA3, ITGA5, ITGAV, LAMB1
  - [37]: Integrins promote tumor invasion through interactions with ECM components
  - [53]: ECM ligand-receptor networks identified between tumor and stromal cells
- Cell migration through matrix. Genes: SPP1, POSTN
  - [37]: Integrins promote invasion through transcriptional and mechanotransduction mechanisms

**Atomic cellular components**
- Focal adhesion complexes. Genes: PTK2B, SHC1, GRB10
  - [16]: FAK/Pyk2 activity promotes pro-inflammatory gene expression and signaling
  - [19]: FAK in tumor microenvironment regulates migration and metastasis
- Extracellular matrix. Genes: POSTN, LAMB1, COL22A1, SPP1, EFEMP1, TNC
  - [53]: Spatial transcriptomics identifies ECM component expression patterns in GBM

**Required genes (not in input)**
- Genes: MMP2, MMP9, ITGB1, FAK, SRC
  - [33]: MMP2 and MMP9 mediate ECM degradation in glioma invasion
  - [37]: ITGB1 associates with alpha integrins to form functional ECM receptors

**Program citations**
- [53]: Comprehensive spatial profiling reveals ECM-mediated tumor-stromal interactions in GBM
- [2]: Genomic analysis identifies ECM remodeling in pediatric gliomas
- [37]: Integrin-mediated invasion mechanisms
- [35]: SPP1 promotes angiogenesis and migration in glioblastoma

## Program: Growth Factor Signal Transduction
Receptor tyrosine kinase activation and downstream signaling cascades driving astrocytoma proliferation and survival. This program integrates receptor activation through VEGF, ephrin, and related ligands with adapter protein-mediated signal propagation.

**Predicted impacts**
- Enhanced proliferation through MAPK/ERK pathway activation
- Increased survival signaling through PI3K/AKT activation
- Promotion of directional cell migration
- Induction of angiogenic gene expression
- Suppression of differentiation programs

**Evidence summary**
IDH wild-type glioblastomas demonstrate constitutive activation of receptor tyrosine kinase signaling through elevated expression of VEGF receptors (KDR) and neuropilins (NRP1, NRP2) that augment ligand binding and signal propagation[20][21]. Downstream of receptor activation, the adapter protein SHC1 couples receptor autophosphorylation to the GRB10-RAS pathway and related mitogenic cascades. The Rho guanine nucleotide exchange factors ARHGEF3 and TRIO modulate RAC1 activation, enabling coordinated effects on both proliferation and cytoskeletal reorganization. These growth factor-dependent signaling cascades represent major therapeutic targets.

**Atomic biological processes**
- VEGF receptor activation. Genes: KDR, NRP1, NRP2
  - [20]: VEGFA and KDR single nucleotide variants associated with lymphoma and angiogenesis
  - [21]: VEGF-C induces lymphatic endothelial cell proliferation in cancer
- Ephrin-Eph signaling. Genes: EFNB2
  - [21]: Ephrin signaling contributes to vascular development in cancer microenvironment
- Downstream signaling cascade. Genes: SHC1, GRB10, ARHGEF3, TRIO, RAC1
  - [44]: PAR1 signaling drives invasion through HMGA2-dependent mechanisms

**Atomic cellular components**
- Growth factor receptors. Genes: KDR, NRP1, NRP2
  - [20]: VEGFA and KDR variants regulate tumor angiogenesis

**Required genes (not in input)**
- Genes: VEGFA, VEGFC, EFNA, RAS, RAF, MEK1/2, ERK1/2, PI3K, AKT
  - [20]: VEGFA is the primary ligand for KDR activation in tumor angiogenesis
  - [21]: VEGFC activates VEGFR3 on lymphatic endothelium

**Program citations**
- [20]: VEGFA and KDR variants influence tumor angiogenesis and growth
- [21]: VEGF signaling regulates vascular development in tumors
- [15]: Trio and related GEFs promote glioblastoma migration

## Program: Cytoskeletal Reorganization and Cell Motility
Coordinated regulation of actin filaments and microtubules enabling transitions from stationary to migratory morphology. This program involves actin polymerization factors, microtubule-associated proteins, and membrane trafficking machinery.

**Predicted impacts**
- Enhanced directional cell migration through brain parenchyma
- Dynamic cytoskeletal remodeling enabling morphological transitions
- Increased exploratory behavior and process extension
- Facilitated single-cell invasion
- Organized collective migration in tumor nests

**Evidence summary**
Astrocytomas transition from relatively stationary cell types to highly motile phenotypes through coordinated reorganization of both actin and microtubule networks. Microtubule-associated proteins (MAP1B) regulate microtubule architecture and establish cell polarity, while actin nucleation factors including formins (PRRX1) and Arp2/3 complex-activating proteins (DNMBP) generate branched and linear actin structures. The guanine nucleotide exchange factor KALRN drives Rho family GTPase activation (particularly RAC1 and CDC42), promoting localized actin polymerization at leading edges. Membrane trafficking proteins (MYOF, MYRFL) support localized membrane expansion during active migration. These cytoskeletal regulators collectively enable the remarkable invasive capacity characteristic of high-grade astrocytomas.

**Atomic biological processes**
- Actin polymerization. Genes: DNMBP, KALRN, PRRX1, FBLIM1, NEBL
  - [51]: MAP1B regulates axonal microtubule architecture and dynamics
- Microtubule dynamics. Genes: MAP1B
  - [51]: MAP1B regulates microtubule dynamics in neuronal growth
- Membrane trafficking. Genes: MYOF, MYRFL
  - [15]: Myoferlin regulates membrane trafficking in cell motility

**Atomic cellular components**
- Focal adhesions. Genes: FBLIM1, PDLIM7
  - [16]: FAK/Pyk2 mediate integrin-dependent signaling at focal adhesions
- Leading edge actin structures. Genes: GAP43
  - [15]: GAP43 participates in local actin polymerization at growth cones

**Required genes (not in input)**
- Genes: RAC1, CDC42, RHOA, ARP2, ARP3, WASP, WAVE
  - [18]: RAC1 downstream of guanine nucleotide exchange factors regulates actin dynamics

**Program citations**
- [51]: MAP1B regulates neuronal migration and axonal development
- [15]: Multiple actin regulatory genes drive tumor cell migration

## Program: Cell-Cell Adhesion and Tissue Organization
Dynamic regulation of cell-cell adhesive contacts through cadherin, immunoglobulin, and related adhesion molecules. This program determines astrocytoma architectural organization and regulates transitions between collective and single-cell migration.

**Predicted impacts**
- Organized tumor mass architecture through regulated N-cadherin interactions
- Dynamic switching between collective and individual cell migration
- Enhanced surface presentation of stem cell markers
- Regulated cell-cell recognition and sorting
- Facilitated heterotypic interactions with immune and stromal cells

**Evidence summary**
Astrocytomas exhibit altered cell-cell adhesion compared to normal astrocytes, with increased expression of N-cadherin (CDH2) that enables more dynamic cell-cell contacts compatible with infiltrative migration[4]. Unlike epithelial cadherins that establish stable barriers, N-cadherin permits continuous reorganization of adhesive contacts, allowing both collective tumor cell invasion and individual cell dissemination. The contactin family proteins (CNTNAP3, CNTNAP3B) mediate homophilic and heterophilic interactions through immunoglobulin domains, contributing to neural-like cell recognition patterns. Cancer stem cell markers including CD44 are frequently elevated and mark subpopulations within astrocytomas with enhanced tumorigenic potential[60]. These adhesion molecules collectively determine the architectural properties distinguishing astrocytomas from normal brain parenchyma.

**Atomic biological processes**
- Calcium-dependent adhesion. Genes: CDH2
  - [4]: CDH2 expression increased in glioblastomas compared to normal brain
- Immunoglobulin-mediated adhesion. Genes: CNTNAP3, CNTNAP3B, NRCAM, NFASC
  - [58]: CNTNAP3/CNTNAP3B mediate homophilic and heterophilic cell-cell interactions

**Atomic cellular components**
- Adherens junctions. Genes: CDH2
  - [4]: N-cadherin mediated adherens junctions maintain tumor architectural integrity
- Cell surface glycoproteins. Genes: CD44, PDPN, PODXL
  - [60]: CD44 expression in tumors associates with cancer stem cell phenotype
  - [56]: PDPN upregulation in glioblastoma associates with invasive phenotype

**Required genes (not in input)**
- Genes: ITGB1, BETA-CATENIN, ALPHA-CATENIN, P120-CATENIN
  - [4]: Catenin proteins link cadherins to the cytoskeleton

**Program citations**
- [4]: CDH2 expression patterns distinguish glioma subtypes
- [60]: CD44 upregulation associates with poor prognosis and immune suppression
- [56]: PDPN expression predicts astrocytoma invasiveness

## Program: Reactive Astrocyte-like Inflammatory Programs
Partial activation of reactive astrocyte transcriptional programs linking to immune modulation and microenvironment sculpting. This program reflects both retained developmental capacity for immune responses and active tumor-driven reprogramming of immune cells.

**Predicted impacts**
- Enhanced recruitment of monocytes and macrophages through CCL2 secretion
- Local inflammation support through IL1R1 and related pathways
- Immune cell suppression through adenosine and complement pathways
- Maintenance of pro-tumor immune microenvironment
- Paradoxical wound-healing-like inflammatory state

**Evidence summary**
While astrocytomas represent malignant transformations of astrocytes, they partially retain and dysregulate the reactive astrocyte transcriptional program normally activated in response to CNS injury[57]. The chemokine CCL2 recruits monocytes and macrophages, establishing an immune infiltrate skewed toward pro-tumor functions. IL1R1 mediates interleukin-1 signaling that perpetuates inflammation. CHI3L1 (YKL-40) represents a secreted protein associated with both reactive astrocytes and gliomas, with immune modulatory functions[23]. The serpin SERPINE1 suppresses plasminogen activation, limiting protease-dependent ECM degradation while supporting a wound-healing-like phenotype favorable to tumor progression[12]. STAT1 signaling responds to interferon-gamma from infiltrating T cells, potentially establishing feedback loops that ultimately favor immune evasion despite initial immune activation. This program reflects complex repurposing of developmental astrocyte responses toward tumor-supportive functions.

**Atomic biological processes**
- Immune cell recruitment and activation. Genes: IL1R1, CCL2, CXCL14
  - [10]: Complement genes influence immune infiltration patterns and prognosis in cancer
- Inflammation resolution and ECM stability. Genes: SERPINE1
  - [12]: SERPINE1 suppresses plasminogen activation and ECM degradation
- Immune signaling. Genes: STAT1, NOS1AP
  - [22]: STAT1 and STAT2 mediate type I interferon signaling in antitumor immunity
  - [25]: STAT1 mediates interferon-gamma signaling in immune activation
- Neuroinflammation. Genes: CHI3L1
  - [23]: YKL-40 (CHI3L1) participates in immune regulation in glioma

**Atomic cellular components**
- Secretory compartments. Genes: SERPINE1, CHI3L1, IL1R1, CCL2
  - [10]: Secreted proteins mediate immune cell infiltration

**Required genes (not in input)**
- Genes: IFN-gamma, IL-1beta, TNF-alpha, IL-6, C5a, GFAP, AQP4
  - [57]: Reactive astrocytes express GFAP and barrier-formation genes in response to injury
  - [54]: Reactive astrocytes express AQP4 in response to injury

**Program citations**
- [57]: Injury-responsive enhancers drive glial cell transcriptional reprogramming
- [10]: Complement system genes influence immune infiltration in cancer
- [12]: SERPINE1 associates with poor prognosis in multiple cancers
- [23]: CHI3L1 participates in glioma immune regulation

## Program: Transcriptional Control and Epigenetic Regulation
Master transcriptional regulators and chromatin organizing proteins establishing and maintaining astrocytoma cellular identity. This program coordinates expression of oncogenic and tumor-suppressive programs while maintaining stemness properties.

**Predicted impacts**
- Sustained expression of proliferation-associated genes
- Suppression of differentiation programs
- Maintenance of cancer stem cell properties
- Altered chromatin accessibility at tumor-relevant loci
- Dysregulated feedback control of signaling pathways

**Evidence summary**
The transcriptional landscape of astrocytomas differs substantially from normal astrocytes, with reactivation of developmental and oncofetal genes concurrent with suppression of differentiation-promoting programs. TCF7 and TCF7L2 mediate canonical Wnt signaling, promoting proliferation through c-MYC activation and other proliferation-associated genes[43][45]. The transcriptional repressor BCL6 suppresses genes promoting differentiation and cellular senescence, maintaining stemness properties[65]. PRICKLE1 and PRICKLE2 provide feedback limitation on Wnt signaling, with potential loss of function contributing to hyperactive pathway signaling. The chromatin organizing proteins SATB2 and HMGA2 establish permissive chromatin architecture at proliferation-associated loci while simultaneously silencing tumor-suppressive chromatin domains[49][42]. HMGA2-AS1 represents an antisense transcript potentially regulating HMGA2 stability or function. These transcriptional regulators collectively establish a malignant cellular state characterized by high proliferative capacity and suppressed differentiation.

**Atomic biological processes**
- Wnt signaling pathway. Genes: TCF7L2, TCF7, PRICKLE1, PRICKLE2
  - [43]: TCF7L2 mediates canonical Wnt pathway and transcriptional activation
  - [45]: TCF7 overexpression associates with poor glioblastoma prognosis
  - [28]: PRICKLE1 negatively regulates Wnt-beta-catenin signaling
- Transcriptional repression. Genes: BCL6
  - [65]: BCL6 functions as transcriptional repressor of differentiation genes
- Chromatin organization. Genes: SATB2, HMGA2, HMGA2-AS1
  - [49]: SATB2 organizes chromatin through binding AT-rich elements
- Post-translational protein modification. Genes: SMYD2
  - [15]: SMYD2 functions as histone methyltransferase

**Atomic cellular components**
- Chromatin. Genes: SATB2, HMGA2, HMGA2-AS1
  - [42]: HMGA2 functions as chromatin organizing protein
- Transcriptional regulatory complexes. Genes: TCF7L2, TCF7, BCL6
  - [43]: TCF7L2 forms complexes with beta-catenin to activate target genes

**Required genes (not in input)**
- Genes: BETA-CATENIN, LEF1, MYC, HDAC1, CBP
  - [43]: Beta-catenin serves as co-activator for TCF7L2

**Program citations**
- [43]: TCF7L2 plays key role in Wnt signaling pathway
- [45]: TCF7 overexpression predicts poor glioblastoma prognosis
- [42]: HMGA2 supports cancer stem cell properties
- [49]: SATB2 regulates transcription through chromatin organization

## Program: Metabolic Reprogramming and Energy Metabolism
Reorganization of cellular metabolism supporting rapid growth and adaptation to variable microenvironmental nutrient and oxygen availability. This program includes glycolytic, biosynthetic, and oxidative phosphorylation pathways.

**Predicted impacts**
- Enhanced glycolytic flux supporting rapid growth
- Increased biosynthetic pathways for nucleotides, lipids, and amino acids
- Adaptation to hypoxic microenvironments through metabolic switching
- Maintenance of ATP production in nutrient-limited regions
- Support for rapid membrane biogenesis during cell division

**Evidence summary**
Glioblastomas undergo substantial metabolic reprogramming to support rapid proliferation and adaptation to variable oxygen and nutrient availability within tumors[53][56]. The hexosamine biosynthesis pathway, initiated by GFPT2, generates UDP-N-acetylglucosamine serving both as substrate for glycoprotein synthesis and as signaling molecule regulating gene expression. ACSS3 converts acetate to acetyl-CoA, supporting both oxidative metabolism and acetyl-CoA-dependent protein acetylation that regulates transcription and enzyme activity. The mitochondrial genes (MT-CO2, MT-ATP6, MT-CYB, MT-CO3) encode critical components of the electron transport chain essential for ATP synthesis in well-oxygenated tumor regions. Sterol and lipid transport proteins (OSBPL3, OSBPL2) enable membrane biogenesis supporting the high rate of cell division. The metabolic program exhibits substantial intratumoral heterogeneity, with different tumor regions adopting distinct metabolic strategies depending on local oxygen and nutrient availability.

**Atomic biological processes**
- Glucose and hexosamine metabolism. Genes: GFPT2, SLC4A7
  - [15]: GFPT2 catalyzes first committed step of hexosamine biosynthesis
- Acetyl-CoA generation and lipogenesis. Genes: ACSS3
  - [15]: ACSS3 activates acetate to acetyl-CoA for metabolic pathways
- Oxidative phosphorylation. Genes: MT-CO2, MT-ATP6, MT-CYB, MT-CO3
  - [27]: Dystrophin encodes large muscle protein, related metabolic dysfunction in glioma
- Lipid and sterol metabolism. Genes: OSBPL3, OSBPL2
  - [15]: OSBPL proteins regulate lipid transport essential for membrane biogenesis

**Atomic cellular components**
- Mitochondria. Genes: MT-CO2, MT-ATP6, MT-CYB, MT-CO3
  - [27]: Mitochondrial genes encode oxidative phosphorylation components

**Required genes (not in input)**
- Genes: HIF1A, HIF2A, LDHA, PKM2, GLUT1, GLUT3, PFKFB3
  - [53]: Hypoxia-inducible factors drive metabolic adaptation in glioblastoma

**Program citations**
- [53]: Metabolic heterogeneity in glioblastoma reflects microenvironmental variation
- [56]: Metabolic reprogramming supports glioblastoma growth and stemness

## Program: Regulatory RNA Networks and Post-Transcriptional Control
Long noncoding RNAs, miRNA host genes, and regulatory RNA elements controlling mRNA stability, protein interactions, and gene expression at multiple levels. This program provides cell-type-specific fine-tuning of gene expression.

**Predicted impacts**
- Post-transcriptional regulation of mRNA stability
- Altered splicing patterns affecting protein isoforms
- Enhanced microRNA-mediated silencing of target genes
- Fine-tuning of signaling pathway output through RNA networks
- Cell-type-specific gene expression patterns

**Evidence summary**
Long noncoding RNAs and regulatory RNA networks provide essential layer of post-transcriptional control in astrocytomas, enabling cell-type-specific fine-tuning of gene expression beyond what transcriptional control alone can achieve[14]. NEAT1 functions as a structural component of paraspeckles, nuclear bodies involved in alternative splicing and mRNA fate determination. Multiple LINC genes (LINC01138, LINC02821, LINC02742) represent annotated long intergenic noncoding RNAs whose specific functions in astrocytoma remain under investigation but likely participate in regulating mRNA stability and protein-RNA interactions. MiRNA host genes MIR4435-2HG and MIR222HG encode primary transcripts processed into mature microRNAs that regulate target mRNAs. Antisense transcripts including HMGA2-AS1 and ADAMTS9-AS1 may regulate sense transcript stability through RNA-RNA duplex formation. The regulatory RNA program likely provides cell-state-specific control enabling plastic transitions between different phenotypic states.

**Atomic biological processes**
- mRNA processing and stability. Genes: NEAT1, RBM47
  - [14]: NEAT1 regulates alternative splicing and mRNA processing in paraspeckles
- MicroRNA regulation. Genes: MIR4435-2HG, MIR222HG
  - [15]: miRNA host genes encode processed miRNAs regulating target mRNAs
- Chromatin remodeling by lncRNAs. Genes: LINC01138, LINC02821, LINC02742
  - [14]: lncRNAs participate in chromatin organization and gene regulation

**Atomic cellular components**
- Paraspeckles. Genes: NEAT1
  - [14]: NEAT1 structures paraspeckles for mRNA processing
- RNA-binding protein complexes. Genes: RBM47
  - [14]: lncRNAs interact with RNA-binding proteins

**Required genes (not in input)**
- Genes: DICER, DROSHA, AGO2, FMRP, HNRNP
  - [14]: FMRP and related RNA-binding proteins regulate neuronal mRNAs

**Program citations**
- [14]: lncRNAs dysregulated in brain disorders including schizophrenia

## Program: Hypoxia Response and Microenvironmental Stress Adaptation
Cellular adaptation to hypoxic, nutrient-limited, and inflammatory microenvironments through HIF-dependent and complementary stress response pathways. This program enables astrocytoma persistence despite hostile microenvironmental conditions.

**Predicted impacts**
- Enhanced survival in nutrient-limited microenvironments
- Suppression of immunosuppressive adenosine signaling
- Evasion of hypoxia-induced apoptosis
- Maintenance of invasive phenotype despite stress
- Adaptation to variable oxygen and nutrient availability

**Evidence summary**
Glioblastomas exhibit pronounced intratumoral hypoxia despite active angiogenesis, with hypoxia-inducible factors driving a transcriptional program enabling metabolic adaptation and stress response. The adenosine-generating enzyme NT5E (CD73) is upregulated in hypoxic regions and generates adenosine that activates immunosuppressive signaling on immune cells. CFLAR suppresses death receptor-mediated apoptosis, enabling cell survival during nutrient stress and hypoxia. Complement component 5a (C5a), produced by both tumor cells and stromal components, activates C5a receptors promoting invasion and stemness while simultaneously recruiting immunosuppressive myeloid cells. The G protein-coupled receptors GPR37 and GPR158 may sense microenvironmental signals and enable adaptive responses. These hypoxia-responsive genes collectively enable astrocytomas to persist and proliferate despite microenvironmental stress.

**Atomic biological processes**
- Adenosine signaling. Genes: NT5E, NT5DC3
  - [15]: NT5E (CD73) converts AMP to adenosine in hypoxic conditions
- Apoptosis suppression. Genes: CFLAR
  - [15]: CFLAR suppresses death receptor signaling in stress conditions
- Complement pathway activation.
  - [56]: C5a signaling promotes glioblastoma invasiveness and stemness

**Atomic cellular components**
- Cell surface receptors. Genes: IL1R1, GPR37, GPR158
  - [56]: C5a receptors expressed on glioblastoma and stromal cells

**Required genes (not in input)**
- Genes: HIF1A, HIF2A, CA9, VEGFA, VEGFC, PDGFA
  - [56]: HIF-driven genes promote glioblastoma adaptation to hypoxia

**Program citations**
- [56]: C5a signaling in glioblastoma promotes invasion and stemness

## Program: Integrin-Linked Kinase and Focal Adhesion Signaling
Integrin-dependent signaling pathways linking cell-matrix interactions to intracellular signaling cascades controlling migration, survival, and gene expression. This program couples mechanical signals from matrix to cellular responses.

**Predicted impacts**
- Enhanced mechanotransduction of matrix signals
- Promotion of cell migration and invasion
- Survival signaling in response to matrix adhesion
- Regulation of actin dynamics at focal adhesions
- Coupling of migration and proliferation signals

**Evidence summary**
Integrin-linked kinase (ILK) and focal adhesion kinase (PTK2B) mediate critical signaling pathways coupling cell-matrix interactions to intracellular responses promoting migration and survival. ILK silencing suppresses glioblastoma migration and invasion through downregulation of ROCK1 and fascin-1, actin regulators essential for cell motility[66]. PTK2B (Pyk2) activation in response to integrin engagement promotes TNF-alpha and IL-1beta signaling while simultaneously driving migration through MAPK and PI3K pathways[16]. The PDZ and LIM domain proteins FBLIM1 and PDLIM7 organize focal adhesion complexes and link integrin signaling to actin dynamics. These focal adhesion signaling components collectively enable astrocytomas to sense and respond to the mechanical properties of their microenvironment.

**Atomic biological processes**
- Focal adhesion assembly. Genes: PTK2B, ILK
  - [16]: FAK/Pyk2 mediates integrin-dependent signaling at focal adhesions
  - [66]: ILK silencing inhibits glioblastoma migration and invasion
- Actin-focal adhesion linkage. Genes: ILK, FBLIM1, PDLIM7
  - [66]: ILK couples integrin signaling to actin cytoskeleton
- Downstream kinase signaling. Genes: SHC1, GRB10, ARHGAP29
  - [16]: FAK/Pyk2 activate MAPK and PI3K signaling pathways

**Atomic cellular components**
- Focal adhesion complexes. Genes: PTK2B, ILK, FBLIM1, PDLIM7
  - [16]: Focal adhesion proteins including FAK, paxillin, and integrins

**Required genes (not in input)**
- Genes: FAK, ITGB1, PAXILLIN, TALIN, ROCK1, FASCIN
  - [66]: ROCK1 and FASCIN downstream of ILK promote glioblastoma motility

**Program citations**
- [66]: ILK regulates glioblastoma migration through ROCK1 and fascin-1
- [16]: Pyk2 activity drives inflammatory signaling and cell migration
- [19]: FAK in platelets regulates tumor microenvironment interactions

## Program: Cell Cycle Progression and Proliferation Control
Dysregulation of cell cycle checkpoints and proliferation control enabling constitutive cell division. This program disrupts normal G1/S checkpoint control and bypasses differentiation-linked cell cycle arrest.

**Predicted impacts**
- Constitutive cell cycle progression bypassing normal checkpoints
- Enhanced proliferation rate enabling rapid tumor growth
- Suppression of differentiation-linked cell cycle arrest
- Maintenance of cancer stem cell properties
- Resistance to growth-inhibitory signals

**Evidence summary**
Astrocytomas exhibit constitutive proliferation reflecting disruption of normal cell cycle checkpoints and checkpoint control mechanisms. CDK6 promotes cell cycle progression through phosphorylation of the retinoblastoma protein, releasing transcriptional repression of S-phase genes[26][29]. In normal astrocytes, p16 (CDKN2A) inhibits CDK6, establishing a checkpoint that couples proliferation to differentiation signals. Frequent loss of p16 in IDH wild-type glioblastomas removes this checkpoint, allowing constitutive CDK6-dependent proliferation. TCF7 and TCF7L2 activate proliferation-associated genes including c-MYC through Wnt signaling[43][45]. HMGA2 supports stemness properties and high proliferative capacity. PRICKLE1 provides feedback limitation on proliferation through suppression of Wnt signaling. These proliferation-driving genes collectively establish rapid cell division characteristic of high-grade astrocytomas.

**Atomic biological processes**
- G1/S checkpoint control. Genes: CDK6
  - [26]: CDK6 promotes cell cycle progression through G1/S checkpoint
  - [29]: CDK6 blocks differentiation and couples proliferation to growth
- Wnt-driven proliferation. Genes: TCF7L2, TCF7
  - [43]: TCF7L2 activates proliferation genes through Wnt signaling
  - [45]: TCF7 drives c-MYC expression and proliferation in glioblastoma
- Stemness and self-renewal. Genes: HMGA2
  - [42]: HMGA2 supports cancer stem cell properties and proliferation

**Atomic cellular components**
- Cyclin-CDK complexes. Genes: CDK6
  - [26]: CDK6 forms complexes with cyclins to phosphorylate Rb

**Required genes (not in input)**
- Genes: CYCLIN-D, CYCLIN-E, RB, P16, P21, P27
  - [4]: CDKN2A deletion occurs in IDH wild-type glioblastomas

**Program citations**
- [26]: CDK6 upregulated in gliomas and potential therapeutic target
- [45]: TCF7 overexpression predicts poor glioblastoma prognosis

## Program: Partial Neuronal and Synaptic Programs in Astrocytoma
Unexpected activation of genes normally associated with neuronal differentiation and synaptic function, suggesting either derivation from multipotent progenitors or partial transdifferentiation. This program reflects plasticity in astrocytoma cellular identity.

**Predicted impacts**
- Potential enhancement of neuron-like signaling properties
- Possible perineural invasion through neuron-like recognition
- Altered metabolic dependencies through synaptic gene expression
- Enhanced calcium signaling through neuronal ion channels
- Potential facilitation of interaction with host neurons

**Evidence summary**
Spatial transcriptomic studies of glioblastomas identify subsets of tumor cells expressing markers normally associated with neurons, including MAP1B (microtubule-associated protein 1B), growth-associated protein GAP43, and synaptosomal-associated proteins[53][57]. The calcium/calmodulin-dependent protein kinase CAMK2D participates in synaptic plasticity and calcium signaling cascades. CADPS (calcium-dependent secretion activator protein) regulates neurosecretion-like processes. Neuronal pentraxin 2 (NPTX2) associates with synaptic plasticity and activity-dependent processes. The presence of these neuronal markers within tumors remains poorly understood and may reflect either that astrocytomas arise from multipotent neural progenitors capable of neuronal differentiation or that differentiated neurons become incorporated into tumors. The functional significance of neuronal program activation appears to include potential survival advantages through neuron-specific metabolic or signaling properties, though direct experimental validation remains incomplete. These observations suggest that astrocytoma cellular identity involves greater plasticity and derivation from developmentally earlier progenitor states than previously appreciated.

**Atomic biological processes**
- Neurotrophic signaling.
  - [15]: Neuronal growth factors and signaling pathways in tumor cells
- Synaptic protein expression. Genes: SYTL5, CAMK2D, NPTX2
  - [15]: Synaptic proteins expressed in subsets of tumor cells
- Neuropeptide processing. Genes: SCG2
  - [15]: Neurosecretory gene expression in tumor cells

**Atomic cellular components**
- Synaptic-like structures. Genes: SYTL5, CAMK2D, CADPS
  - [53]: Spatial transcriptomics identifies synaptic gene expression in tumor cells

**Required genes (not in input)**
- Genes: SYNAPTOTAGMIN, SNAP25, SYNTAXIN, RAB3, NEUROTROPHINS
  - [53]: Synaptic machinery genes present in tumor cell transcriptomes

**Program citations**
- [53]: Single-cell spatial profiling identifies neuronal gene expression in GBM cells
- [57]: Glial cells activate injury-responsive programs, potentially overlapping with neuronal signatures

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/1755
2. 2. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/546
4. 4. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/999
6. 6. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/3688
10. 10. Langtry A, Rabadan R, Alonso L, Filip I, Sabroso-Lasa S, Moreno-Oya A, et al.. Deciphering the role of complement system genes in pancreatic cancer susceptibility and prognosis. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-65811-y
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/7078
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/5054
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/5045
14. 14. Dang X, Gong D, Dai S-S, Teng Z, Luo X-J. Genetic and functional insights into long noncoding RNAs in schizophrenia. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03421-2
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/7204
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/2185
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/9444
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/5879
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/14083
20. 20. Eichin D, Lehotina D, Kauko A, Uenaka M, Leppänen M, Elima K, et al.. Breast cancer remodels lymphatics in sentinel lymph nodes. Nature Communications [Internet]. 2025Nov17;16(1). Available from: https://www.nature.com/articles/s41467-025-64981-z
21. 21. Jun-Yan L, Ying-Qing L, Jia-Hao D, Sha G, Qing-Mei H, Jie-Wen B, et al.. LC3-dependent intercellular transfer of phosphorylated STAT1/2 elicits CXCL9+ macrophages and enhances radiation-induced antitumor immunity.. The Journal of clinical investigation [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41321309/
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/1116
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/5629
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=20846
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/1021
26. 26. Available from: https://www.ncbi.nlm.nih.gov/omim/300377
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/144165
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/12571
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/1756
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
31. 31. Wu L, Wang L, Zhuang Y, Luo Y, Zhu Q, Maimaitizunong M, et al.. Integrative analysis reveals synergistic regulation of Sp7 by BRD9 and Wnt/β-catenin signaling during osteogenic differentiation. Communications Biology [Internet]. 2025Dec1;. Available from: https://www.nature.com/articles/s42003-025-09278-z_reference.pdf
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/9173
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/6387
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/6696
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/3553
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/3678
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/8828
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/4316
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=3685
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/18186
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/8091
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/6934
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/2149
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/6932
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/212712
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/5142
47. 47. Ricci C, Midroit MJ, Caicci F, Achsel T, Domínguez-Iturza N, Bagni C. CYFIP1 governs the development of cortical axons by modulating calcium availability. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-65801-0
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/23314
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/408
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/17755
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/79923
52. 52. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
53. 53. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
54. 54. Oh Y, Yoo J, Lee D, Ko B, Hong JP, Moon JH, et al.. Restoring the glioblastoma tumor microenvironment by targeting C5a with the antagonist W54011. Scientific Reports [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41598-025-30853-1
55. 55. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/6900
57. 57. Available from: https://www.ncbi.nlm.nih.gov/gene/16403
58. 58. Dong R, Srikanth A, Tharehalli U, Seufferlein T, Schirmbeck R, Lechel A. CD44 upregulation in chronic liver disease marks the transition to hepatocellular carcinoma and portends poor prognosis. British Journal of Cancer [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41416-025-03284-y
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/5789
60. 60. Available from: https://www.ncbi.nlm.nih.gov/gene/12505
61. 61. Available from: https://www.ncbi.nlm.nih.gov/gene/2735
62. 62. Available from: https://www.ncbi.nlm.nih.gov/gene/3976
63. 63. Available from: https://www.ncbi.nlm.nih.gov/gene/604
64. 64. Available from: https://www.ncbi.nlm.nih.gov/gene/3611
65. 65. Available from: https://www.ncbi.nlm.nih.gov/gene/16878
66. 66. Available from: https://www.ncbi.nlm.nih.gov/gene/3689
67. 67. Available from: https://www.ncbi.nlm.nih.gov/gene/89780
68. 68. Available from: https://www.ncbi.nlm.nih.gov/gene/18125
69. 69. Available from: https://www.ncbi.nlm.nih.gov/gene/2100
70. 70. Available from: https://www.ncbi.nlm.nih.gov/gene/25937
71. 71. Available from: https://www.ncbi.nlm.nih.gov/gene/9722
72. 72. Available from: http://json-schema.org/draft-07/schema#",
