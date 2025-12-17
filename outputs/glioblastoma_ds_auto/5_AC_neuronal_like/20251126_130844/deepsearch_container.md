# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: malignant glioblastoma (WHO grade IV)
- Tissue: brain

## Input Genes
LINC02235, AC037486.1, PCDH11X, LINC01829, AL591043.2, ZNF423, ADAMTS18, AL133538.1, DOCK2, SCN1A-AS1, AL022068.1, SEPTIN14, SGCZ, ADAM28, RYR2, DOCK8, ACER2, AC128687.3, AC120193.1, OLR1, AC110296.1, AC109466.1, SPOCK3, ST6GALNAC5, AL136441.1, ... (373 total)

## Program: Immune Checkpoint Signaling
A gene program mediating immune escape through checkpoint molecule expression and T-cell exhaustion pathways. CD96 functions as an immune checkpoint regulating CD8+ T-cell antitumor function. STAT4 regulates PD-L1 expression and immune evasion. CD163 and MSR1 mark pro-tumoral macrophage populations. OLR1 associates with immune cell infiltration and immunosuppression. TLR2 initiates pathogen recognition signaling in innate immune cells. This program collectively enables glioblastoma immune evasion via checkpoint activation and immunosuppressive microenvironment establishment.

**Predicted impacts**
- Enhanced CD8+ T-cell exhaustion and reduced anti-tumor immunity
- Increased PD-L1 expression on tumor cells and immune cells
- Macrophage skewing toward pro-tumoral M2 phenotype
- Reduced interferon-gamma production and T-cell activation
- Increased IL-10 and TGF-β secretion

**Evidence summary**
CD96, STAT4, and CD163 are consistently associated with immune evasion in glioblastoma and other cancers. CD96 directly suppresses CD8+ T-cell function through DNAM-1 inhibition. STAT4 phosphorylation increases PD-L1 transcription. CD163 and MSR1 identify pro-tumoral macrophages enriched in the glioblastoma microenvironment. This convergent pathway enables immune checkpoint activation and T-cell exhaustion, hallmarks of glioblastoma's immunosuppressive microenvironment.

**Atomic biological processes**
- CD8+ T-cell exhaustion and anergy. Genes: CD96, STAT4
  - [42]: CD96 demonstrated to regulate CD8+ T-cell antitumor function and suppress primary tumor growth in combination with other checkpoint inhibitors
  - [39]: High CD96+ cell infiltration predicts exhausted CD8+ T-cell phenotype and poor prognosis in gastric cancer
- PD-L1 transcriptional regulation. Genes: STAT4, CD96
  - [54]: STAT4 enrichment at PD-L1 DNA promoter; MET-STAT4-PD-L1 axis enforces glioma immune evasion
- Macrophage-mediated immunosuppression. Genes: CD163, MSR1, OLR1
  - [49]: MSR1 expressed on macrophages and dendritic cells; role in pro-inflammatory phenotype switching
  - [31]: CD163 marks M2-like macrophage polarization in glioblastoma; TAMs promote immunosuppression and anti-inflammatory phenotype
- Toll-like receptor signaling. Genes: TLR2
  - [44]: TLR2 cooperates with MSR1 to promote pathogen recognition and phagocytosis; activates NF-κB signaling

**Required genes (not in input)**
- Genes: PD-L1, PD-1, CTLA4, TIGIT, DNAM-1, FCER1G
  - [42]: PD-1, PD-L1, and TIGIT are canonical immune checkpoint molecules that interact with CD96

**Program citations**
- [42]: CD96 immune checkpoint regulates CD8+ T-cell function and metastasis
- [54]: MET-STAT4-PD-L1 axis in glioma immune evasion
- [31]: CD163 and Iba1 in TAM-mediated glioma progression
- [49]: MSR1 in immune regulation and macrophage phenotype

## Program: Receptor Tyrosine Kinase Signaling
A gene program comprising components of receptor tyrosine kinase (RTK) signaling pathways that drive glioblastoma proliferation, survival, and invasion. TEK (Tie2) mediates angiopoietin signaling and vessel maturation. DOCK2, DOCK8, and downstream SYK coordinate Rho GTPase activation for cytoskeletal reorganization. WIPF1 facilitates FAK-mediated actin polymerization. This program collectively enhances receptor-mediated signaling critical for glioblastoma growth and angiogenesis.

**Predicted impacts**
- Enhanced angiogenic signaling through Tie2 activation
- Increased Rac and Cdc42 GTPase activity driving cell migration
- Enhanced focal adhesion signaling and invasive capacity
- Elevated MAPK and PI3K/AKT pathway activation
- Increased cytoskeletal remodeling and invadopodia formation

**Evidence summary**
TEK/Tie2 signaling promotes glioblastoma angiogenesis and vessel maturation. DOCK2 and DOCK8 act as guanine nucleotide exchange factors (GEFs) for Rac and Cdc42, respectively, driving cytoskeletal reorganization essential for tumor cell migration. SYK couples downstream to both MAPK and PI3K/AKT pathways. WIPF1 coordinates FAK-mediated actin polymerization. Collectively, this program amplifies RTK signaling strength and transduces it into enhanced migration and invasion phenotypes characteristic of malignant glioblastoma.

**Atomic biological processes**
- Angiopoietin-Tie2 signaling. Genes: TEK
  - [45]: Angiopoietin-1 binds Tie2 receptor to enhance tumor vessel maturation and regulate vascular growth in gliomas
  - [48]: Tie2/TEK modulates interaction between glioma and brain tumor stem cells
- DOCK-mediated Rho GTPase activation. Genes: DOCK2, DOCK8
  - [7]: DOCK8 deficiency inhibits BCR signaling and B-cell development; DOCK8 mutation impairs Cdc42-dependent cell migration
  - [10]: DOCK2 is Rac GEF critical for leukocyte migration; DOCK8 is Cdc42-specific GEF regulating dendritic cell interstitial migration
- Spleen tyrosine kinase (SYK) signaling. Genes: SYK
  - [44]: SYK kinases initiate signaling downstream of Fc receptors and integrins in innate immune cells; activate MAPK and NF-κB
  - [47]: SYK phosphorylation activates NLRP3 inflammasome and IL-1β secretion via NF-κB pathway
- Actin polymerization and cytoskeletal dynamics. Genes: WIPF1
  - [21]: TRPV4 colocalizes with F-actin at cellular protrusions; activates Cdc42/N-wasp axis for invadopodia formation
  - [10]: WIPF1 and FAK mediate Rho/WASP pathway of actin polymerization for cell adhesion and migration

**Atomic cellular components**
- Cell membrane receptor complexes. Genes: TEK, DOCK2, DOCK8
  - [55]: RTK/Ras/PI3K signaling altered in 86-90% of GBM cases; RTK dimerization activates downstream signaling

**Required genes (not in input)**
- Genes: RAF, MEK, ERK1/2, PI3K, AKT, mTOR, RAC1, CDC42
  - [55]: RAF, MEK, ERK, PI3K, AKT, and mTOR are canonical downstream effectors of RTK signaling in glioblastoma

**Program citations**
- [55]: RTK/Ras/PI3K pathway altered in 86-90% of GBM; critical for GBM pathogenesis
- [7]: DOCK8 mutation impairs B-cell and T-cell immune responses relevant to glioma microenvironment
- [21]: TRPV4/Cdc42/N-wasp signaling axis regulates invasion-growth in glioblastoma

## Program: Synaptic Adhesion and Neuronal Communication
A gene program mediating cell-cell adhesion at synapses and neuron-neuron interactions through adhesion molecules and signaling proteins. CNTNAP2 is essential for synaptic function and neuronal migration; loss impairs E/I balance and cortical development. IL1RAPL1 is a synaptic adhesion molecule recruiting PTPδ and inducing excitatory synapse formation. NLGN4X encodes neuroligin-4, crucial for synaptic organization and neurotransmission. PCDH7 and PCDH11X are protocadherins involved in cell-cell recognition. SYT1 and SYN3 mediate neurotransmitter release and synaptic plasticity. This program regulates the synaptic connectivity landscape that glioma cells aberrantly reactivate.

**Predicted impacts**
- Aberrant reactivation of synaptic adhesion programs in glioma cells
- Enhanced intercellular communication and adhesion between tumor cells
- Altered calcium signaling through synaptic-like connections
- Increased neurotransmitter-like signaling in tumor microenvironment
- Formation of tumor cell-neuron hybrid synaptic structures

**Evidence summary**
CNTNAP2, IL1RAPL1, NLGN4X, and protocadherins (PCDH7, PCDH11X) are canonical synaptic adhesion molecules critical for neuronal connectivity. CNTNAP2 mutations associate with neurodevelopmental disorders through disruption of cortical lamination and E/I imbalance—hallmarks of altered neural circuit function. IL1RAPL1 recruits PTPδ to drive postsynaptic density formation. SYT1 and SYN3 mediate presynaptic vesicle dynamics. Notably, glioma cells express synaptic proteins and form tumor-neuron hybrid synapses, facilitating invasion and seizure activity. This program captures the re-expression of synaptic machinery in malignant glioblastoma.

**Atomic biological processes**
- Synaptic adhesion molecule expression. Genes: CNTNAP2, IL1RAPL1, NLGN4X, PCDH7, PCDH11X
  - [13]: CNTNAP2 is essential for synaptic function; deficiency results in decreased interneurons, impaired cortical layer modeling, and aberrant neuronal migration
  - [17]: IL1RAPL1 is a synaptic adhesion molecule localized at postsynaptic membrane; recruits PTPδ for synapse formation
  - [12]: NLGN4X mutations disrupt synaptic connectivity and synaptic organization; associated with autism and neurodevelopmental disorders
- Neurotransmitter release and synaptic transmission. Genes: SYT1, SYN3, CNTNAP2
  - [16]: CNTNAP2 involved in neuron-glia adhesion complex with contactin 2 (TAG-1) and clustering of potassium channels
- Neuronal migration and axon guidance. Genes: CNTNAP2, SLIT2, RELN
  - [33]: SLIT2 is a secretory glycoprotein binding Robo receptors; acts as axon guidance molecule and regulates radial migration of cortical neurons via autocrine signaling
  - [16]: CNTNAP2 implicated in neuronal migration, neuronal network activity, and synaptic spine development

**Atomic cellular components**
- Synaptic membrane proteins. Genes: SYT1, SYN3, CNTNAP2, IL1RAPL1, NLGN4X
  - [12]: CHRNA7 mutations reduce receptor function; CNTNAP2 clusters at synapses with postsynaptic markers
- Extracellular matrix anchoring proteins. Genes: SLIT2, RELN
  - [33]: SLIT2 binds to heparan sulfate proteoglycans and interacts with extracellular matrix; localizes within basement membrane

**Required genes (not in input)**
- Genes: CONTACTIN, PTPN, PTPRO, CONTACTIN-2, STARGAZIN
  - [13]: CONTACTIN and PTPN family members are essential partners for CNTNAP2 function in synaptic adhesion

**Program citations**
- [13]: CNTNAP2 deficiency in ASD and neurodevelopmental disorders; role in E/I balance
- [17]: IL1RAPL1 synaptic adhesion and postsynaptic density formation
- [12]: NLGN4X mutations in autism; synaptic organization and neurotransmission
- [38]: IGSF3 interaction with Kir4.1 and glioma-related epileptiform activity

## Program: Ion Channel Dysregulation and Excitotoxicity
A gene program mediating alterations in ion channel expression and calcium homeostasis that promote glioma proliferation and seizure activity. TRPV4 elevates intracellular calcium and promotes invadopodia formation via Cdc42/N-wasp signaling. TRPM8 and TRPM3 modulate calcium and cation fluxes. KCNH7, KCNIP4, RYR2, and RYR3 regulate potassium and ryanodine-sensitive calcium channels. GRIN2B encodes NMDA receptor subunit 2B, contributing to glutamate-mediated calcium signaling. FXYD5 regulates Na+/K+-ATPase. This program collectively dysregulates ion homeostasis, promoting both tumor progression and neuronal hyperexcitability manifesting as glioma-related epilepsy.

**Predicted impacts**
- Increased intracellular free calcium concentration
- Enhanced invadopodia formation and invasion capacity
- Dysregulated potassium buffering and loss of ion homeostasis
- Amplified glutamate-mediated excitatory signaling
- Glioma-related seizures and epileptiform activity
- Metabolic reprogramming via calcium-dependent kinases

**Evidence summary**
TRPV4 channel activation directly promotes glioblastoma invasion by elevating intracellular calcium and activating the Cdc42/N-wasp axis. TRPV4 expression is elevated in malignant glioma compared to low-grade glioma and correlates with poor prognosis. KCNH7, KCNIP4, and related potassium channels are downregulated in glioma, impairing potassium buffering. IGSF3-mediated suppression of Kir4.1 potassium channel function links ion dysregulation to proliferation and seizure activity. GRIN2B and glutamate receptor upregulation contribute to Ca2+-mediated excitotoxicity and formation of tumor-neuron hybrid synapses. RYR2 and RYR3 release calcium from intracellular stores. This convergent program dysregulates ion homeostasis, driving both invasion and glioma-related epileptic activity.

**Atomic biological processes**
- Calcium influx and intracellular calcium elevation. Genes: TRPV4, TRPM8, TRPM3, RYR2, RYR3, GRIN2B
  - [21]: TRPV4 stimulation promotes glioblastoma cell migration and invasion; TRPV4 regulates invadopodia and filopodia formation via Cdc42/N-wasp axis
  - [11]: Alterations in Ca2+ toolkit (TRPC and TRPV channels) in glioblastoma; increased expression of TRPC1, TRPC6, TRPV1, TRPV2
  - [8]: Glutamate-mediated calcium signaling provides positive feedback to promote glioma formation; enhanced Ca2+ activates nitric oxide synthase
- Potassium channel dysregulation and ion imbalance. Genes: KCNH7, KCNIP4, FXYD5
  - [38]: IGSF3 interacts with Kir4.1 to suppress potassium buffering; impaired K+ handling linked to glioma proliferation and seizure activity
- Glutamate-mediated excitotoxicity. Genes: GRIN2B
  - [8]: Glutamatergic and calcium signaling provides positive feedback for glioma formation; upregulation of GluRs and enhanced glutamate release facilitate seizure-like activity

**Atomic cellular components**
- Calcium-activated signaling complexes. Genes: TRPV4, TRPM8, RYR2, GRIN2B
  - [8]: CaMK2A intimately interacts with GluRs; elevated intracellular Ca2+ activates downstream kinases and promotes metabolic reprogramming

**Required genes (not in input)**
- Genes: STIM1, ORAI1, CAMK2A, CAMK2D, KNCJ10
  - [11]: STIM1 and ORAI1 mediate store-operated calcium entry; CAMK2A couples calcium to downstream signaling in glioma
  - [38]: KNCJ10 (Kir4.1) is essential for potassium buffering but suppressed by IGSF3 in glioma

**Program citations**
- [21]: TRPV4 elevated in malignant glioma; TRPV4/Cdc42/N-wasp axis regulates invasion and invadopodia formation
- [38]: IGSF3-Kir4.1 interaction impairs potassium buffering; dysregulation linked to glioma proliferation and seizures
- [8]: Glutamate-calcium signaling provides positive feedback for glioma progression
- [11]: Calcium channel alterations in glioblastoma stem cells and glioma tissue

## Program: Extracellular Matrix Remodeling and Invasion
A gene program controlling extracellular matrix (ECM) degradation, remodeling, and production that facilitates glioma invasion and infiltration into normal brain parenchyma. ADAMTS3, ADAMTS14, and ADAMTS18 are metalloproteases cleaving lecticans and other ECM components. POSTN (periostin) is upregulated in cancer-associated fibroblasts and promotes ECM remodeling and invasion. SULF1 modifies heparan sulfate proteoglycans. COL4A6, COL12A1, COL19A1 are collagen scaffolds. SMOC2 and other matricellular proteins regulate cell-matrix interactions. This program collectively restructures the brain microenvironment to enable glioma cell dissemination.

**Predicted impacts**
- Enhanced ECM degradation and proteolytic remodeling
- Increased invasive capacity into surrounding brain parenchyma
- Altered collagen fiber alignment facilitating migration
- Enhanced cell-matrix interactions promoting dissemination
- Reduced ECM mechanical impedance to tumor infiltration

**Evidence summary**
ADAMTS metalloproteases are the predominant ECM-degrading enzymes in glioma. BEHAB/brevican, a CNS-specific lecticans, requires ADAMTS-mediated cleavage at specific sites (396SRG398) to promote glioma invasion in vitro and in vivo. Periostin (POSTN) is highly expressed in matrix-remodeling cancer-associated fibroblasts (matCAFs) and promotes both CAF migration and ECM remodeling. SULF1 modifies heparan sulfate, altering growth factor availability and cell-matrix interactions. Collagen organization influences glioma invasiveness—intermediate collagen density maximizes invasion. This program collectively restructures the neural ECM, reducing mechanical resistance to glioma infiltration and creating pro-invasive microenvironment.

**Atomic biological processes**
- Lectin cleavage and ECM degradation. Genes: ADAMTS3, ADAMTS14, ADAMTS18
  - [18]: BEHAB/brevican proteolytic processing by ADAMTS family at specific sites is necessary for pro-invasive effect in glioma
- Periostin-mediated matrix remodeling. Genes: POSTN
  - [32]: POSTN exclusively upregulated in cancer-associated fibroblasts (matCAFs); promotes fibroblast proliferation, migration, and ECM remodeling
  - [35]: POSTN mediates collagen production and ECM remodeling in tissue fibrosis and cancer
- Heparan sulfate proteoglycan modification. Genes: SULF1
  - [33]: SLIT2 is a ligand of heparan sulfate proteoglycan glypican-1; proper localization within basement membrane is key for axon guidance
- Collagen fiber organization. Genes: COL4A6, COL12A1, COL19A1
  - [15]: Collagen density and organization in ECM profoundly influence glioma invasion; intermediate collagen concentrations maximize invasion in vitro

**Atomic cellular components**
- Extracellular matrix scaffold. Genes: POSTN, ADAMTS3, COL4A6, COL12A1, SMOC2
  - [15]: ECM composition includes fibrous collagen and afibrous components; glioma cells interact with both via cell-cell and cell-ECM contacts

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP1, TIMP2, ADAMTS1, ADAMTS2
  - [18]: MMP2 and MMP9 are major ECM-degrading enzymes; TIMP1/2 are natural inhibitors

**Program citations**
- [18]: ADAMTS-mediated BEHAB/brevican cleavage necessary for glioma invasion
- [32]: POSTN upregulation in cancer-associated fibroblasts; promotes ECM remodeling and invasion
- [15]: ECM composition and organization profoundly influence glioma invasion patterns

## Program: Angiogenesis and Vascular Development
A gene program regulating blood vessel formation and vascular endothelial cell function that supports glioma growth. VEGFD (VEGF-D) is secreted by tumor cells and activates VEGFR-2 and VEGFR-3 on endothelial cells. TEK (Tie2) mediates angiopoietin signaling for vessel maturation and stabilization. KLF5 promotes glioblastoma angiogenesis by inducing AGGF1 gene transcription in glioma-associated endothelial cells. This program collectively drives pathological neovascularization that perfuses the tumor and enables growth beyond diffusion limits.

**Predicted impacts**
- Increased endothelial cell proliferation and vascular sprouting
- Enhanced vascular permeability and blood-brain barrier dysfunction
- Vessel stabilization and reduced hemorrhagic necrosis
- Increased oxygen and nutrient delivery to tumor
- Promotion of glioma cell intravasation and dissemination

**Evidence summary**
VEGF-D exhibits higher mitogenic potency than VEGF-A and is upregulated in glioblastoma in response to anti-VEGF-A therapy, enabling antiangiogenic resistance. VEGF-D activates both VEGFR-2 (blood angiogenesis) and VEGFR-3 (lymphangiogenesis), providing dual-pathway vascular stimulation. TEK/Tie2 signaling complements VEGF-D by stabilizing nascent vessels through angiopoietin binding. KLF5-driven AGGF1 expression in glioma-associated endothelial cells further amplifies angiogenic signals. This convergent program overcomes anti-VEGF-A therapy and sustains the neovascular network essential for glioma progression.

**Atomic biological processes**
- VEGF-D signaling and vascular proliferation. Genes: VEGFD
  - [50]: VEGF-D is a secreted glycoprotein binding VEGFR-2 and VEGFR-3; higher mitogenic ability than VEGF-A; upregulated in glioblastoma
  - [53]: VEGF-D mature form strongly supports angiogenesis and lymphangiogenesis; dual functionality in coordinating vascular and lymphatic growth
- Tie2-angiopoietin vascular stabilization. Genes: TEK
  - [45]: Angiopoietin-1 activates Tie2 to enhance tumor vessel maturation; inhibits vascular leakage
- KLF5-mediated angiogenic factor expression. Genes: KLF5
  - [19]: KLF5 promotes glioblastoma angiogenesis by inducing AGGF1 transcription in glioma-associated endothelial cells

**Atomic cellular components**
- Vascular endothelial cell surface receptors. Genes: VEGFD, TEK
  - [53]: VEGFR2 and VEGFR3 are primary receptors for VEGF-D; expressed on endothelial cells and lymphatic endothelial cells

**Required genes (not in input)**
- Genes: VEGFA, VEGFR1, VEGFR2, ANGPT1, ANGPT2, FLT1
  - [50]: VEGF-A and angiopoietins are canonical angiogenic factors; VEGFR1/2 are essential receptors

**Program citations**
- [50]: VEGF-D role in glioblastoma angiogenesis and resistance to anti-VEGF therapy
- [45]: Angiopoietin-Tie2 signaling in glioma vessel maturation
- [19]: KLF5 promotes glioblastoma angiogenesis via AGGF1

## Program: Wnt/β-Catenin Self-Renewal Signaling
A gene program mediating Wnt signaling pathway activation that promotes glioma stem cell self-renewal and inhibits differentiation. WNT16 is a Wnt ligand activating canonical β-catenin signaling. This program drives stemness maintenance and chemotherapy resistance characteristic of glioblastoma stem cells (GSCs), which are responsible for tumor recurrence.

**Predicted impacts**
- Increased glioma stem cell self-renewal capacity
- Enhanced resistance to differentiation signals
- Improved tumor growth and propagation
- Enhanced chemotherapy and radiotherapy resistance
- Tumor recurrence and regrowth after standard therapy

**Evidence summary**
WNT/β-catenin signaling is aberrantly activated in glioblastoma and drives GSC self-renewal. β-catenin and TCF4 nuclear accumulation correlates with glioma grade and poor prognosis. Inhibition of WNT signaling via β-catenin modulation impedes glioma stem cell clonogenic growth. WNT signaling activation promotes GSC stemness while inhibiting differentiation, enabling indefinite self-renewal and tumor propagation. This program captures the dysregulated developmental pathway that maintains glioma stem cell identity.

**Atomic biological processes**
- Canonical Wnt/β-catenin pathway activation. Genes: WNT16
  - [27]: WNT signaling involved in maintaining stemness of normal stem cells; aberrant activation in GBM promotes GSC growth and invasion
  - [30]: Dysregulation of Wnt pathway supports onset of cancer stem cells (CSCs); alterations in Wnt components discriminate normal from malignant cells in adult brain
- Stemness maintenance and self-renewal. Genes: WNT16
  - [30]: β-catenin nuclear localization and TCF4 expression significantly higher in glioma than normal brain tissue; positively correlates with WHO grade

**Required genes (not in input)**
- Genes: FZD, LRP5, LRP6, GSK3B, APC, AXIN, TCF, LEF1, β-CATENIN
  - [30]: FZD, LRP, GSK3B, APC, AXIN, TCF, and β-catenin are canonical Wnt pathway components

**Program citations**
- [27]: WNT signaling roles in GSC self-renewal and glioma progression
- [30]: Wnt/β-catenin pathway dysregulation in glioblastoma; correlation with WHO grade and poor prognosis

## Program: Epithelial-Mesenchymal Transition and Invasion
A gene program regulating epithelial-mesenchymal transition (EMT) that enables glioma cell migration, invasion, and dissemination. EMT transcription factors (TWIST-family, SNAIL-family, ZEB-family, SOX2) promote acquisition of mesenchymal phenotype and down-regulation of epithelial markers. TGM2 (tissue transglutaminase) is upregulated during EMT and promotes invasion. POSTN supports EMT through CAF interactions. This program collectively drives the phenotypic plasticity enabling glioma cells to invade adjacent brain tissue and metastasize.

**Predicted impacts**
- Increased cell motility and migration capacity
- Enhanced invasive capability into surrounding brain parenchyma
- Reduced intercellular adhesion and increased dissemination
- Acquisition of stem cell-like properties
- Increased resistance to chemotherapy and radiotherapy

**Evidence summary**
EMT is fundamentally linked to glioma invasion and stemness. TWIST, SNAIL, and ZEB transcription factors suppress E-cadherin and promote mesenchymal marker expression. TGM2 (transglutaminase-2) catalyzes cross-linking of EMT-related proteins and supports invasion. POSTN from cancer-associated fibroblasts promotes EMT through YAP1/TEAD1 signaling. Notably, the E-cadherin to N-cadherin switch is not universally required in glioblastoma EMT, suggesting context-dependent mechanisms. This program captures the phenotypic plasticity enabling glioma dissemination and therapy resistance.

**Atomic biological processes**
- EMT transcription factor activation. Genes: TGM2
  - [56]: TWIST1 mediates EMT by inhibiting E-cadherin and promoting N-cadherin expression; drives invasive glioma phenotype
  - [59]: SNAIL, TWIST, and ZEB families are major EMT regulators; overexpression associated with invasive ability and chemotherapy resistance
- E-cadherin to N-cadherin switch. Genes: TGM2
  - [56]: Loss of E-cadherin often accompanied by increased N-cadherin; N-cadherin overexpression linked to invasion and metastasis
- Vimentin upregulation and EMT markers. Genes: TGM2
  - [56]: Overexpression of vimentin linked to enhanced invasiveness and metastasis in glioblastoma; EMT marker

**Atomic cellular components**
- Adherens junction remodeling. Genes: TGM2, POSTN
  - [59]: EMT involves disruption of E-cadherin/catenin complexes; remodeling of adherens junctions enabling migration

**Required genes (not in input)**
- Genes: TWIST, SNAIL, ZEB, SOX2, CDH1, CDH2, VIM
  - [56]: TWIST, SNAIL, ZEB, SOX2 are canonical EMT transcription factors; CDH1/2 and VIM are marker genes

**Program citations**
- [56]: EMT and E-cadherin/N-cadherin switching in glioblastoma invasion
- [59]: EMT transcription factors and stemness maintenance in glioma
- [32]: POSTN promotes EMT and invasion in gastric cancer; relevant to glioma microenvironment

## Program: Hypoxia-Responsive Transcription
A gene program activated under hypoxic conditions (low oxygen) in glioblastoma that drives metabolic reprogramming, angiogenesis, and stemness maintenance. This program includes HIF-1α and HIF-2α-dependent transcriptional responses, though HIFs themselves are not in the input list. VEGFD, TEK, and KLF5 are key HIF-target genes promoting angiogenesis. Downstream metabolic enzymes (ME1 for gluconeogenesis; SUCLG2 for TCA cycle) support hypoxic metabolism. This program collectively enables tumor survival and growth in the hypoxic glioblastoma microenvironment.

**Predicted impacts**
- Enhanced survival under hypoxic stress
- Increased VEGF production and angiogenesis
- Metabolic shift toward glycolysis and amino acid metabolism
- Enhanced glioma stem cell self-renewal
- Resistance to hypoxia-induced apoptosis

**Evidence summary**
Hypoxia is endemic to glioblastoma due to rapid growth outpacing oxygen diffusion. HIF-1α and HIF-2α accumulation activates transcriptional programs supporting glioma survival, proliferation, and stemness. VEGFD is a canonical HIF-target gene promoting angiogenesis that partially circumvents hypoxic stress. TEK-mediated vessel maturation further improves perfusion. KLF5 drives glioma-associated endothelial cell angiogenic programs. ME1 and SUCLG2 support hypoxic metabolic reprogramming. Notably, IDH-mutant gliomas exhibit altered HIF signaling, suggesting context-dependent hypoxic responses. This program captures the transcriptional adaptation enabling glioblastoma survival in its oxygen-poor microenvironment.

**Atomic biological processes**
- Angiogenic factor upregulation. Genes: VEGFD, TEK, KLF5
  - [57]: Under hypoxia, HIF1α upregulates expression of VEGF and other pro-angiogenic factors; essential for glioblastoma vascularization
  - [60]: HIF-1α and HIF-2α regulate VEGF expression; HIF-2α promotes stem cell phenotype in glioblastoma stem cells
- Metabolic reprogramming and glycolysis. Genes: ME1, SUCLG2
  - [57]: Under hypoxia, HIF1α promotes glycolysis via upregulation of HK2 and PDK1; shift from glucose to glutamine metabolism
  - [60]: HIF-regulated metabolic reprogramming essential for glioblastoma survival and proliferation in hypoxic microenvironment
- Cancer stem cell maintenance. Genes: VEGFD, KLF5
  - [57]: Hypoxia-induced HIF1α promotes stemness and self-renewal of GSCs; maintains pluripotency markers
  - [60]: HIF-2α serves unique role in GSC development and maintenance; induces pluripotent stem cell markers (OCT4, NANOG, SOX2)

**Required genes (not in input)**
- Genes: HIF1A, HIF2A, HIF3A, PHD2, PHD3, VHL, HK2, PDK1, GLUT1
  - [57]: HIF1A, HIF2A, PHD, and VHL are central to hypoxic signaling; HK2, PDK1, GLUT1 are HIF-target metabolic genes

**Program citations**
- [57]: Hypoxia-induced HIF signaling in glioblastoma; metabolic reprogramming and GSC maintenance
- [60]: HIF-1α and HIF-2α in stemness and metabolic adaptation in glioblastoma

## Program: Lipid Metabolism and Signaling
A gene program regulating lipid metabolism, storage, and signaling that supports glioblastoma proliferation and stemness. PLD1 (phospholipase D1) catalyzes phosphatidic acid production, acting as both an enzymatic catalyst and scaffolding protein in Wnt/β-catenin, PI3K/Akt, and HIF signaling. OLR1 (LOX-1) is a scavenger receptor mediating oxidized lipid uptake and promoting EMT and stemness. ACER2 (alkaline ceramidase 2) regulates ceramide metabolism. This program collectively integrates lipid signaling into core oncogenic pathways.

**Predicted impacts**
- Enhanced PI3K/Akt and mTOR signaling
- Increased Wnt/β-catenin pathway activation
- Enhanced stemness and self-renewal capacity
- Improved metabolic flexibility under diverse nutrient conditions
- Reduced immune cell infiltration and T-cell activation

**Evidence summary**
PLD1 operates as both an enzymatic catalyst and scaffolding platform in glioblastoma oncogenic signaling. PLD1 catalyzes production of phosphatidic acid (PA), a signaling lipid, while its protein domains scaffold Wnt/β-catenin and PI3K/Akt pathway components. PLD1-mediated HIF-1α translation and protein stabilization supports hypoxic survival. Targeting PLD1 decreases RB1 and promotes E2F1-dependent apoptosis via miR-192/4465. OLR1 is a scavenger receptor mediating oxidized lipid uptake; high OLR1 expression correlates with EMT, stemness, and immune escape. This convergent program integrates lipid signaling into core stem cell renewal and metabolic adaptation pathways.

**Atomic biological processes**
- Phospholipase D signaling. Genes: PLD1
  - [20]: PLD1 catalyzes PA production; acts as scaffold protein in Wnt/β-catenin and PI3K/Akt pathways; dual roles in HIF-1α regulation
- Oxidized lipid uptake and scavenging. Genes: OLR1
  - [25]: OLR1 expression associated with cancer immune escape and targeting OLR1 increases tumor T-cell infiltration
  - [52]: MSR1 mediates uptake of modified lipoprotein; involved in metabolic inflammation and cancer progression
- Cancer stem cell self-renewal via lipid signaling. Genes: PLD1, OLR1
  - [20]: PLD1 governs self-renewal of cancer-initiating cells through E2F1–miR-4496–β-catenin axis

**Atomic cellular components**
- Plasma membrane lipid microdomains. Genes: PLD1, OLR1
  - [20]: PLD1 acts as scaffold protein to increase signaling efficiency and coordinate complex upstream signals

**Required genes (not in input)**
- Genes: PTEN, PI3K, AKT, mTOR, WNT, FZD, GSK3B
  - [20]: PLD1 scaffolds and coordinates PI3K/Akt and Wnt pathway signaling

**Program citations**
- [20]: PLD1 as key player in cancer stemness and Wnt/PI3K cross-talk
- [25]: OLR1 in cancer immune escape and EMT

## Program: Tumor-Associated Macrophage Polarization
A gene program regulating polarization and activation of tumor-associated macrophages (TAMs) that create an immunosuppressive microenvironment. CD163 identifies M2-like pro-tumor macrophages enriched in glioblastoma. MSR1 (CD204) is a macrophage-specific receptor involved in pro-inflammatory phenotype. OLR1 is overexpressed in myeloid-derived suppressor cells (MDSCs) and promotes immunosuppression. LCP2 and FYB1 facilitate leukocyte signaling. VSIG4 is an immunosuppressive receptor on macrophages. This program collectively recruits and polarizes TAMs toward anti-tumor immunity suppression.

**Predicted impacts**
- Increased macrophage infiltration into glioblastoma
- Polarization toward pro-tumor M2 phenotype
- Enhanced IL-10 and TGF-β secretion
- Reduced CD8+ T-cell activation and infiltration
- Increased glioma stem cell maintenance via IL-33

**Evidence summary**
CD163, a marker of M2-like pro-tumor macrophages, is highly expressed in glioblastoma-associated macrophages (Iba1+ cells). CD163-positive macrophages secrete anti-inflammatory cytokines (IL-10, TGF-β) that suppress CD8+ T-cell responses. IL-6 promotes CD40 expression and M2 polarization via Stat3/HIF-1α. Notably, Iba1+ TAMs produce IL-33, which feeds back to glioma stem cells to maintain stemness and support tumor progression. MSR1 (CD204) mediates lipid uptake and links lipid metabolism to macrophage polarization. OLR1 is enriched in pro-tumor PMN-MDSCs. VSIG4 on macrophages delivers immunosuppressive signals. This convergent program shapes the TAM-rich immunosuppressive microenvironment enabling glioblastoma immune evasion.

**Atomic biological processes**
- M2 macrophage polarization. Genes: CD163, MSR1
  - [31]: CD163 marks M2-like macrophage polarization; IL-33 produced by Iba1+ TAMs feeds back to GSCs to maintain stemness
  - [34]: IL-6 promotes macrophage transition to pro-tumor phenotype and secretion of IL-10 and TGF-β
- Immunosuppressive cell recruitment. Genes: OLR1, LCP2
  - [25]: OLR1 expression associated with T-cell exhaustion and immunosuppressive cell infiltration
  - [34]: CCL8 secreted by TAMs binds CCR5/CCR1 to activate ERK1/2 in glioma cells
- Leukocyte adhesion and migration. Genes: LCP2, FYB1
  - [10]: DOCK2 critical for leukocyte migration and trafficking; DOCK8 deficiency impairs immune cell development
- Immunosuppressive checkpoint signaling. Genes: VSIG4
  - [34]: VSIG4 is B7 family member functioning as immunosuppressive receptor on macrophages

**Atomic cellular components**
- Macrophage surface receptors. Genes: CD163, MSR1, OLR1, VSIG4
  - [49]: MSR1 and CD163 are macrophage-specific scavenger receptors; CD36 also involved in lipid uptake

**Required genes (not in input)**
- Genes: IL10, TGFB1, IL6, CCL2, CSF1, M-CSFR
  - [31]: IL-10, TGF-β, IL-6, and CCL2 are key cytokines in macrophage polarization and immune suppression

**Program citations**
- [31]: CD163, Iba1, and IL-33 in TAM-mediated glioma progression
- [34]: TAM polarization and CCL8 secretion in glioma immune evasion
- [25]: OLR1 in immunosuppressive cell infiltration
- [49]: MSR1 in macrophage-mediated immune regulation

## Program: GTPase Activation and Cytoskeletal Remodeling
A gene program regulating small GTPase (Rho, Rac, Cdc42) activation and actin cytoskeleton reorganization that enables glioma cell migration and invasion. DOCK2 and DOCK8 are guanine nucleotide exchange factors (GEFs) that activate Rac (DOCK2) and Cdc42 (DOCK8). Downstream effectors (N-WASP, WAVE) nucleate actin filaments. WIPF1 facilitates FAK-Rac coupling. STAC and RCAN2 coordinate Cdc42 and calcium signaling. This program collectively enables rapid morphological changes and invasion-promoting cellular protrusions.

**Predicted impacts**
- Enhanced Rac1 activation and lamellipodia formation
- Enhanced Cdc42 activation and filopodia formation
- Increased actin polymerization and cytoskeletal reorganization
- Enhanced cell migration velocity and invasiveness
- Increased invadopodia formation for ECM degradation

**Evidence summary**
DOCK2 and DOCK8 are non-canonical GEFs lacking DH domains but retaining GDP-GTP exchange activity via DHR-2 domains. DOCK2-Rac coupling promotes lymphocyte migration; DOCK8-Cdc42 coupling regulates interstitial dendritic cell migration. In glioblastoma, TRPV4 activates Cdc42 downstream to N-WASP, promoting invadopodia formation and invasion. WIPF1 links FAK to Rho/WASP pathway actin polymerization. STAC coordinates Cdc42 signaling. Collectively, this program enables rapid GTPase cycling and actin dynamics underlying glioma cell motility and invasive morphology.

**Atomic biological processes**
- Rac1 GTPase activation. Genes: DOCK2
  - [10]: DOCK2 mediates GDP-GTP exchange for Rac; crystal structure shows DHR-2 domain binds Rac exclusively at lobes B and C
- Cdc42 GTPase activation. Genes: DOCK8, TRPV4
  - [10]: DOCK8 is Cdc42-specific GEF; different lobe orientation than DOCK2-Rac1 complex
  - [21]: TRPV4 activates Cdc42/N-wasp axis in glioblastoma; promotes invadopodia and filopodia formation
- Actin filament nucleation and polymerization. Genes: WIPF1
  - [10]: DOCK8 couples to LRAP35a and MRCKα to phosphorylate myosin II regulatory light chain (MLC2)

**Atomic cellular components**
- Guanine nucleotide exchange factor complexes. Genes: DOCK2, DOCK8, STAC
  - [10]: DOCK DHR-2 domain is core GEF module; DOCK8 associates with adaptor proteins like LRAP35a

**Required genes (not in input)**
- Genes: RAC1, CDC42, NWASP, WAVE, ARPC, ARP2, ARP3, FAK
  - [10]: RAC1, CDC42, N-WASP, and WAVE are canonical downstream effectors of DOCK GEFs

**Program citations**
- [10]: DOCK2 and DOCK8 as Rho GTPase GEFs in immune cell migration
- [21]: TRPV4-Cdc42-N-wasp axis in glioblastoma invasion

## Bibliography
1. Available from: https://www.genecards.org/cgi-bin/carddisp.pl?gene=LINC02235
2. Minerva MC, Fanggeng Z, V SP, Samantha LW, Li M, Louise PW, et al.. Genetic variation in PCDH11X is associated with susceptibility to late-onset Alzheimer's disease.. Nature genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2873177/
3. Timpika C, Napat A, Anchalee T, Chadamas S, Somchai P, Piti U, et al.. Roles of Zinc Finger Protein 423 in Proliferation and Invasion of Cholangiocarcinoma through Oxidative Stress.. Biomolecules [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6681239/
4. Available from: https://maayanlab.cloud/Harmonizome/search?q=Protein-tyrosine+phosphatase%2C+receptor%2Fnon-receptor+type
5. Available from: https://www.proteinatlas.org/ENSG00000102290-PCDH11X/cancer
6. Yuan H, Li-Jun T, Xiang-Ding C, Jonathan G, Hong-Wen D. Identification of novel variants associated with osteoporosis, type 2 diabetes and potentially pleiotropic loci using pleiotropic cFDR method.. Bone [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6364698/
7. Gu H, Xie M, Zhao S, Luo X, Huang Y, Yang L, et al.. DOCK8 gene mutation alters cell subsets, BCR signaling, and cell metabolism in B cells. Cell Death &amp; Disease [Internet]. 2024Dec1;15(11). Available from: https://www.nature.com/articles/s41419-024-07180-w
8. Zhe P, Kuo-Chieh L, Amber K, Gabriell E, Hoau-Yan W. Pathway analysis of glutamate-mediated, calcium-related signaling in glioma progression.. Biochemical pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
9. Tao X, Feng Y, Rushan F, Jing Q, Wenbin C. CHRNA7 inhibits cell invasion and metastasis of LoVo human colorectal cancer cells through PI3K/Akt signaling.. Oncology reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26719016/
10. Kazufumi K, Takehito U, Yoshinori F. DOCK family proteins: key players in immune surveillance mechanisms.. International immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6949370/
11. Valérie C, Elodie T, Nadine D, Patricia A, Bruno C. Calcium Channels in Adult Brain Neural Stem Cells and in Glioblastoma Stem Cells.. Frontiers in cellular neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7691577/
12. Mohammed A-B, Nermin KS, Adel SB, Eman AB, Reem E. Decoding the genetic landscape of autism: A comprehensive review.. World journal of clinical pediatrics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11438927/
13. Laila YA, Dost MH, Abdulrahman MA, Nadra EE, Aurangzeb TH. Low Plasma Levels of Contactin-Associated Protein-Like 2 in Children with Autism Spectrum Disorder: Links to Neural Development.. Neuropsychiatric disease and treatment [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11646403/
14. Mariana R-B, Caterina M, Nicolas L, Laura G, Christelle M, Christine S-N, et al.. Novel IL1RAPL1 mutations associated with intellectual disability impair synaptogenesis.. Human molecular genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4867007/
15. Brenda MR, Laura JK. The role of extracellular matrix in glioma invasion: a cellular Potts model approach.. Biophysical journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2599859/
16. Reiner O, Karzbrun E, Kshirsagar A, Kaibuchi K. Regulation of neuronal migration, an emerging topic in autism spectrum disorders. Journal of Neurochemistry [Internet]. 2015Nov13;136(3). Available from: https://onlinelibrary.wiley.com/doi/10.1111/jnc.13403
17. Available from: https://www.semanticscholar.org/paper/c3bf37c20c7c21a10a6a01764b6b02c448aa0237
18. Mariano SV, Susan H, Russell TM. BEHAB/brevican requires ADAMTS-mediated proteolytic cleavage to promote glioma invasion.. Journal of neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
19. Yao L, Ceshi C. The roles and regulation of the KLF5 transcription factor in cancers.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
20. Lim SH, Lee H, Lee HJ, Kim K, Choi J, Han JM, et al.. PLD1 is a key player in cancer stemness and chemoresistance: Therapeutic targeting of cross-talk between the PI3K/Akt and Wnt/β-catenin pathways. Experimental &amp; Molecular Medicine [Internet]. 2024Jul1;56(7). Available from: https://www.nature.com/articles/s12276-024-01260-9
21. Yang W, Wu P-fei, Ma J-xing, Liao M-jun, Xu L-shan, Yi L. TRPV4 activates the Cdc42/N-wasp pathway to promote glioblastoma invasion by altering cellular protrusions. Scientific Reports [Internet]. 2020Aug25;10(1). Available from: https://www.nature.com/articles/s41598-020-70822-4
22. Available from: https://aacrjournals.org/cancerdiscovery/article/8/1/108/112872/Somatic-Superenhancer-Duplications-and-Hotspot
23. Wenjun T, Richu L, Yonghong D, Qiaoling S, Xiaofei L, Yongshi L. PLD1 overexpression promotes invasion and migration and function as a risk factor for Chinese glioma patients.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5593623/
24. Giorgia C, Hélène C, Oana C, Dimitra G. TRP Channels in Brain Tumors.. Frontiers in cell and developmental biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33928077/
25. Lei W, Yuantong L, Weiwei D, Tianfu W, Linlin B, Lei C. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10454104/
26. Available from: https://en.wikipedia.org/wiki/Glial_cell_line-derived_neurotrophic_factor
27. Available from: https://www.nature.com/articles/labinvest2015140
28. Yu L, Hao Z, Ji Z, Xiaojun Z, Wenjing Y, Wei L, et al.. Identification of Immune-Related Prognostic Biomarkers Based on the Tumor Microenvironment in 20 Malignant Tumor Types With Poor Prognosis.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7438715/
29. Zhinian L, Yu J, Tao L, Jianbao Z, Shuilin Z. Signaling of glial cell line-derived neurotrophic factor and its receptor GFRα1 induce Nurr1 and Pitx3 to promote survival of grafted midbrain-derived neural stem cells in a rat model of Parkinson disease.. Journal of neuropathology and experimental neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/21865882/
30. Mariachiara Z, Patricia G, Sihana Z, Marzia C, Patrizia DI, Francesco C, et al.. The Role of Wnt Signal in Glioblastoma Development and Progression: A Possible New Pharmacological Target for the Therapy of This Tumor.. Genes [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5852601/
31. Haneya F, Yuqi Z, Islam A, Manuel BG. TAMing Gliomas: Unraveling the Roles of Iba1 and CD163 in Glioblastoma.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12070867/
32. Ching HT, Fuda X, Peiyao Y, Jialin W, Yang L, Bonan C, et al.. POSTN is exclusively activated in cancer-associated fibroblasts and leads to unfavorable prognosis of patients with gastric cancer.. Molecular and clinical oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12278709/
33. Tian J, Guozhen N, Chunping W, Xiaomeng T, Jian X, Xue L, et al.. Cell-autonomous action of . Frontiers in molecular neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11646887/
34. Tang F, Wang Y, Zeng Y, Xiao A, Tong A, Xu J. Tumor-associated macrophage-related strategies for glioma immunotherapy. npj Precision Oncology [Internet]. 2023Aug19;7(1). Available from: https://www.nature.com/articles/s41698-023-00431-7
35. Yang Y, Li S, Bian L, Dai X, Hu J, Ma Y, et al.. Periostin mediates collagen production, ECM remodeling and myofibroblast differentiation in breast prosthesis capsule formation. Scientific Reports [Internet]. 2025Jul15;15(1). Available from: https://www.nature.com/articles/s41598-025-11409-9
36. Meng K, Tao Z, Bo X. Expression of the axon guidance factor Slit2 and its receptor Robo1 in patients with Hirschsprung disease: An observational study.. Medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8376357/
37. Chen W, Wang F, Yu X, Qi J, Dong H, Cui B, et al.. LncRNA MIR31HG fosters stemness malignant features of non-small cell lung cancer via H3K4me1- and H3K27Ace-mediated GLI2 expression. Oncogene [Internet]. 2023Nov10;43(18). Available from: https://www.nature.com/articles/s41388-023-02883-4
38. Rachel NC, Isamu A, Jochen M, Brittney L, Yeunjung K, Malcolm FM, et al.. Glioma epileptiform activity and progression are driven by IGSF3-mediated potassium dysregulation.. Neuron [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9991983/
39. Chang X, Hanji F, Yun G, Kuan Y, Jieti W, Chao L, et al.. Impact of intratumoural CD96 expression on clinical outcome and therapeutic benefit in gastric cancer.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9746045/
40. Rasmani H, Rinku D, Arati T. Glioblastoma stem cell long non-coding RNAs: therapeutic perspectives and opportunities.. Frontiers in genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11249581/
41. Available from: https://livrepository.liverpool.ac.uk/3137928/1/200850788_Jan2020.pdf
42. Deepak M, Ailin L, Jason M, Amelia RA, Kimberley S, Stephen JB, et al.. CD96 Is an Immune Checkpoint That Regulates CD8. Cancer immunology research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30894377/
43. Tomislav K, Ewelina ML, Michiel L, Cosmin IC, Christopher WF, Angelica S, et al.. Transcription factor mesenchyme homeobox protein 2 (MEOX2) modulates nociceptor function.. The FEBS journal [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/35029322/
44. Clifford AL. Src-family and Syk kinases in activating and inhibitory pathways in innate immune cells: signaling cross talk.. Cold Spring Harbor perspectives in biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3039931/
45. Yvonne R, Marcia RM, Karl HP. The role of angiopoietins during angiogenesis in gliomas.. Brain pathology (Zurich, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8095963/
46. Kokotović T, Lenartowicz EM, Langeslag M, Ciotu CI, Fell CW, Scaramuzza A, et al.. Transcription factor mesenchyme homeobox protein 2 (MEOX2) modulates nociceptor function. The FEBS Journal [Internet]. 2022Feb16;289(12). Available from: https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.16347
47. Theobald SJ, Simonis A, Mudler JM, Göbel U, Acton R, Kohlhas V, et al.. Spleen tyrosine kinase mediates innate and adaptive immune crosstalk in SARS‐CoV‐2 mRNA vaccination. EMBO Molecular Medicine [Internet]. 2022Jul4;14(8). Available from: https://www.embopress.org/doi/10.15252/emmm.202215888
48. Available from: https://www.oncotarget.com/article/204/
49. Jack G, José LM-R, Matthias T. The role of macrophage scavenger receptor 1 (MSR1) in inflammatory disorders and cancer.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9618966/
50. Syeda MZB, Peter H. Vascular Endothelial Growth Factor-D (VEGF-D): An Angiogenesis Bypass in Malignant Tumors.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10487419/
51. Ji W, Liu Y, Xu B, Mei J, Cheng C, Xiao Y, et al.. Bioinformatics Analysis of Expression Profiles and Prognostic Values of the Signal Transducer and Activator of Transcription Family Genes in Glioma. Frontiers in Genetics [Internet]. 2021Jul2;12. Available from: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2021.625234/full
52. Sheng W, Ji G, Zhang L. Role of macrophage scavenger receptor MSR1 in the progression of non-alcoholic steatohepatitis. Frontiers in Immunology [Internet]. 2022Dec15;13. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1050984/full
53. Lee C, Kim M-J, Kumar A, Lee H-W, Yang Y, Kim Y. Vascular endothelial growth factor signaling in health and disease: from molecular mechanisms to therapeutic perspectives. Signal Transduction and Targeted Therapy [Internet]. 2025May19;10(1). Available from: https://www.nature.com/articles/s41392-025-02249-0
54. Qiang-Wei W, Li-Hua S, Ying Z, Zheng W, Zheng Z, Zhi-Liang W, et al.. MET overexpression contributes to STAT4-PD-L1 signaling activation associated with tumor-associated, macrophages-mediated immunosuppression in primary glioblastomas.. Journal for immunotherapy of cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8527154/
55. Available from: https://www.nature.com/articles/sigtrans201740
56. Pu X. The significance of epithelial-mesenchymal transition (EMT) in the initiation, plasticity, and treatment of glioblastoma.. Genes & diseases [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12547761/
57. Tingyu S, Jun Z, Xiang Z, Xinggang M. The Role of Hypoxia and Cancer Stem Cells in Development of Glioblastoma.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10177528/
58. Lifeng M, Zheng J, Jiwei W, Ning Y, Qichao Q, Wenjing Z, et al.. Epithelial membrane protein 1 promotes glioblastoma progression through the PI3K/AKT/mTOR signaling pathway.. Oncology reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6609345/
59. Yu-Bao L, Tian-Jiao S, Yu-Tong C, Zong-Yan C, Jia-Yu Z, Feng M, et al.. Targeting the Epithelial-to-Mesenchymal Transition in Cancer Stem Cells for a Better Clinical Outcome of Glioma.. Technology in cancer research & treatment [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7586027/
60. Abd GM, Laird MC, Ku JC, Li Y. Hypoxia-induced cancer cell reprogramming: a review on how cancer stem cells arise. Frontiers in Oncology [Internet]. 2023Aug8;13. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2023.1227884/full
