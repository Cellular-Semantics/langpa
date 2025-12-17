# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma
- Tissue: Central nervous system (brain)

## Input Genes
ID4, DOCK7, LIFR, ANKFN1, GLIS3, ARHGEF26-AS1, DCLK1, MIR99AHG, ADCY2, SORBS1, RNF19A, PARD3B, GRAMD2B, DCLK2, GFAP, WLS, ABLIM1, TNIK, AC093535.1, BMPR1B, NTRK2, RFX4, PACRG, NKAIN3, LHFPL6, ... (200 total)

## Program: Astrocyte Identity and Maturation
Core program governing astrocytic lineage determination, differentiation, and maintenance of astrocyte-specific cellular identity through expression of canonical astrocyte markers and transcriptional regulators of astrocyte development. Dysregulation of this program in astrocytomas leads to altered differentiation capacity, acquisition of intermediate phenotypes, and expansion of progenitor-like tumor cells.

**Predicted impacts**
- Shift toward immature, proliferative astrocytic phenotypes
- Enhanced stemness characteristics and reduced terminal differentiation
- Dysregulation of developmental plasticity programs
- Acquisition of hybrid phenotypes combining astrocyte and progenitor features

**Evidence summary**
GFAP and ALDH1L1 serve as canonical astrocyte markers whose dysregulation fundamentally compromises normal astrocyte identity. Recent research demonstrates that astrocytes retain substantial developmental plasticity and can be reprogrammed toward neuronal fates. In astrocytomas, dysregulation of lineage-determining transcription factors including FOXO1, RFX proteins, and HES4 predicts exploitation of these developmental plasticity programs to maintain tumor-initiating populations.

**Atomic biological processes**
- Astrocyte differentiation and lineage commitment. Genes: GFAP, ALDH1L1, VIM, FOXO1, HES4
  - [13]: GFAP functions as structural constituent of cytoskeleton and regulates glial cell proliferation and autophagy
  - [6]: ALDH1L1 serves as complementary astrocyte marker in lineage tracing studies
  - [3]: ASCL1-mediated astrocyte-to-neuron conversion reveals fundamental plasticity of astrocytic lineage
- Transcriptional regulation of astrocyte fate. Genes: FOXO1, RFX2, RFX4, NPAS3, HES4
  - [37]: FOXO1 controls cell fate specification and metabolic homeostasis
  - [25]: HES4 functions as downstream effector of Notch signaling promoting astrocyte proliferation

**Atomic cellular components**
- Intermediate filament cytoskeleton. Genes: GFAP, VIM
  - [13]: GFAP is structural constituent of cytoskeleton

**Required genes (not in input)**
- Genes: SOX9, SOX10, OLIG2, NFIA, NFIB
  - [6]: SOX transcription factors regulate astrocyte differentiation and identity

**Program citations**
- [6]: Comprehensive characterization of astrocyte transcriptional programs across injury phases
- [13]: GFAP gene description and function
- [3]: MicroRNA-mediated neuronal detargeting and astrocyte-to-neuron conversion studies

## Program: Metabolic Reprogramming and Lipid Homeostasis
Comprehensive dysregulation of lipid metabolism, apolipoprotein signaling, and fatty acid synthesis that promotes tumor metabolic flexibility, chemotherapy resistance, and enhanced biosynthetic capacity. This program enables astrocytomas to utilize diverse nutrient sources and activate DNA repair pathways despite exposure to genotoxic stress.

**Predicted impacts**
- Enhanced chemotherapy resistance through DNA repair pathway activation
- Metabolic flexibility enabling survival in diverse microenvironmental conditions
- Increased biosynthetic capacity for rapid tumor cell proliferation
- Generation of signaling lipids promoting pro-tumoral inflammatory responses

**Evidence summary**
Recent 2025 research demonstrates that tumor-derived APOE promotes chemoresistance through SCARB1-mediated lipid uptake and activation of homologous recombination repair via the β-catenin-BRCA1/2 axis. ABCA1 dysfunction in reactive astrocytes leads to lipid accumulation and impaired cholesterol efflux. Coordinate dysregulation of lipid transporters, fatty acid desaturases, and cAMP signaling molecules predicts fundamental rewiring of astrocytoma lipid metabolism toward enhanced accumulation and utilization for both structural support and signaling lipid generation.

**Atomic biological processes**
- Apolipoprotein and lipid transport. Genes: APOE, ABCA1, PLTP, SCARA3
  - [28]: APOE-mediated lipid uptake through SCARB1 activates homologous recombination repair and confers chemoresistance
  - [64]: ABCA1 dysfunction in reactive astrocytes impairs cholesterol efflux
- Polyunsaturated fatty acid synthesis. Genes: FADS2
  - [28]: Lipid metabolism reprogramming supports tumor progression and treatment resistance
- Cyclic AMP signaling and metabolic adaptation. Genes: ADCY2, ADCY8, NOS1AP
  - [6]: ADCY signaling regulates metabolic gene expression in response to nutrient availability

**Atomic cellular components**
- Lipid droplets and lipid storage compartments. Genes: APOE, ABCA1
  - [28]: Enhanced lipid accumulation in tumor cells supports biosynthesis and signaling

**Required genes (not in input)**
- Genes: SREBP1, SREBP2, FASN, ACC1, CHPT1
  - [28]: Sterol regulatory element-binding proteins control lipid synthesis gene expression

**Program citations**
- [28]: Tumor-derived apolipoprotein E confers resistance to chemotherapy through lipid metabolism reprogramming
- [64]: ABCA1 dysfunction in reactive astrocytes and cholesterol efflux impairment

## Program: NTRK2 Receptor Tyrosine Kinase Signaling
Dysregulation of NTRK2-mediated neurotrophic signaling through gene fusions and altered receptor activity, leading to constitutive activation of MAPK and PI3K/AKT survival pathways. This program drives tumor proliferation, altered differentiation, and survival signaling independent of BDNF ligand availability.

**Predicted impacts**
- Constitutive activation of MAPK and PI3K/AKT survival pathways
- Enhanced proliferation independent of growth factor ligands
- Resistance to apoptotic signals and enhanced cell survival
- Acquired resistance through activation of alternative oncogenic drivers

**Evidence summary**
Recent molecular characterization of astrocytomas identified TRIM24::NTRK2 fusion genes that generate constitutively active receptors independent of BDNF ligand availability. These fusions activate both MAPK and PI3K/AKT pathways, driving tumor proliferation. Patient-derived cells from NTRK2-fusion astrocytomas initially respond to TRK inhibitors but develop resistance through acquisition of additional oncogenic drivers including FGFR2, RUNX1T1, and VEGFR signaling. This suggests NTRK2 represents one of multiple cooperating pathways in astrocytoma biology.

**Atomic biological processes**
- NTRK2-mediated receptor tyrosine kinase signaling. Genes: NTRK2
  - [21]: TRIM24::NTRK2 fusion in astrocytomas displays oncogenic capacity activating MAPK and PI3K pathways
  - [26]: BDNF/TrkB signaling activates Akt and Erk1/2 phosphorylation supporting pericyte homeostasis
- Neurotrophic factor-mediated cell survival. Genes: NTRK2
  - [9]: BDNF regulates pericyte and vascular homeostasis through TrkB signaling
  - [6]: BDNF/TrkB pathway dysregulation in chronic pathological states
- Neuregulin and ErbB signaling. Genes: NRG3
  - [56]: Neuregulin signaling regulates neonatal muscle growth and nervous system development via ErbB4

**Atomic cellular components**
- Neurotrophic receptor complexes. Genes: NTRK2
  - [21]: NTRK2 gene fusions generate constitutively active receptor tyrosine kinases

**Required genes (not in input)**
- Genes: MAPK1, MAPK3, PIK3CA, AKT1, BDNF
  - [21]: MAPK and PI3K/AKT pathways downstream of NTRK2 signaling

**Program citations**
- [21]: Comprehensive characterization and targeted treatment of TRIM24::NTRK2 astrocytomas
- [26]: BDNF supports pericyte and vascular homeostasis through TrkB signaling

## Program: Cytoskeletal Organization and Focal Adhesion
Coordinated dysregulation of focal adhesion proteins, integrin signaling components, and actin-binding proteins that reduce cell-matrix adhesion strength, facilitate cell migration and invasion, and enable remodeling of cellular morphology. This program predicts enhanced tumor cell invasiveness and metastatic potential.

**Predicted impacts**
- Reduced cell-matrix adhesion strength and increased detachment capacity
- Enhanced cell migration and invasion through brain tissue
- Altered cell morphology and increased deformability
- Disrupted mechanotransduction signaling affecting growth and survival

**Evidence summary**
Multiple genes encoding focal adhesion proteins, integrin components, and actin regulatory proteins show dysregulation in astrocytomas. Vinculin couples integrin signaling to actin dynamics; ITGB4 mediates cell-matrix interactions; dystrophin and DTNA link the cytoskeleton to extracellular matrix; NCKAP5 promotes Rac1-mediated actin polymerization. Coordinate dysregulation predicts profound alterations in tumor cell adhesion and migration capacity, enabling invasion and dissemination through restrictive brain microenvironments.

**Atomic biological processes**
- Focal adhesion assembly and remodeling. Genes: VCL, ITGB4, NCKAP5
  - [45]: Vinculin couples integrin signaling to actin cytoskeletal dynamics
- Integrin-mediated cell-matrix interactions. Genes: ITGB4, VCL
  - [43]: ITGB4 mediates cell-matrix interactions and hemidesmosomes
  - [46]: ITGB4 regulates vascular endothelial adhesion and DNA damage response
- Actin polymerization and cell migration. Genes: NCKAP5
  - [17]: Rac1 GTPase and WAVE complexes regulate actin polymerization driving cell migration
- Dystrophin complex-mediated cytoskeletal linkage. Genes: DTNA, DMD
  - [6]: DMD and DTNA mediate mechanical coupling between intracellular and extracellular structures

**Atomic cellular components**
- Focal adhesion complexes. Genes: VCL, ITGB4
  - [45]: Vinculin localizes to focal adhesions and adherens junctions
- Dystrophin-associated protein complex. Genes: DTNA, DMD
  - [6]: DMD-associated proteins link cytoskeleton to extracellular matrix
- Actin polymerization machinery. Genes: NCKAP5
  - [17]: Rac1 and WAVE complexes drive actin dynamics

**Required genes (not in input)**
- Genes: FAK, SRC, PXN, ACTN4, ARP2
  - [45]: Focal adhesion kinase and Src family kinases regulate focal adhesion dynamics

**Program citations**
- [45]: MCAM and cell adhesion molecule roles in vascular and tumor biology
- [43]: ITGB4 mediates cell-matrix interactions and regulates migratory capacity

## Program: Cell-Cell Adhesion and Polarity
Dysregulation of cadherins, polarity complexes, and gap junction proteins that disrupt normal cell-cell contacts, reduce intercellular communication, and compromise epithelial organization. This program predicts reduced adhesive constraints on tumor cell behavior and enhanced capacity for dissemination.

**Predicted impacts**
- Reduced cell-cell adhesion and increased cellular independence
- Disrupted epithelial organization and loss of contact inhibition
- Impaired intercellular communication and reduced transmission of anti-proliferative signals
- Enhanced capability for single-cell dissemination and invasion

**Evidence summary**
CDH11 mediates cell-cell adhesion and participates in TGF-β-dependent epithelial-to-mesenchymal transition. PARD3 and PARD3B regulate cell polarity and tight junction assembly; their dysfunction disrupts organized cell-cell contacts and promotes invasion. GJA1 forms gap junctions mediating direct intercellular communication; reduced GJA1 function frequently occurs in gliomas and associates with enhanced proliferation. Coordinate dysregulation of these cell-cell adhesion and polarity genes predicts fundamental disruption of epithelial organization and enhanced tumor cell independence.

**Atomic biological processes**
- Cadherin-mediated cell-cell adhesion. Genes: CDH11
  - [15]: CDH11 mediates cell-cell adhesion and is involved in TGF-beta-stimulated migration
- Cell polarity establishment and maintenance. Genes: PARD3, PARD3B
  - [33]: PARD3 regulates invasion and metastasis through control of tight junction assembly
  - [35]: PARD3 in PAR complex for functional tight junctions
- Gap junction-mediated intercellular communication. Genes: GJA1
  - [60]: GJA1/connexin-43 forms gap junctions for direct intercellular communication

**Atomic cellular components**
- Adherens junctions. Genes: CDH11
  - [15]: CDH11 participates in adherens junction assembly and stability
- Polarity complexes. Genes: PARD3, PARD3B
  - [33]: PAR3-containing protein complexes regulate tight junction formation
- Gap junctions. Genes: GJA1
  - [60]: GJA1 forms connexons that mediate cell-cell channel communication

**Required genes (not in input)**
- Genes: CDH1, CTNNB1, CTNND1, OCLN, CLDN
  - [15]: E-cadherin and catenins regulate cell adhesion; claudins and occludin mediate tight junctions

**Program citations**
- [15]: CDH11 role in glioblastoma cell migration
- [33]: PARD3 regulation of tight junction assembly and metastasis

## Program: Ion Homeostasis and Calcium Signaling
Dysregulation of ion channels, transporters, and calcium signaling machinery that disrupts normal astrocytic ion buffering, pH regulation, and calcium oscillations. This program predicts altered cellular excitability, impaired metabolic coupling to neuronal activity, and dysregulation of calcium-dependent gene expression.

**Predicted impacts**
- Impaired ion buffering capacity and altered pH homeostasis
- Dysregulated cellular excitability and altered response to neuronal activity
- Disrupted calcium oscillations and loss of coupled astrocyte activation
- Altered calcium-dependent gene expression affecting proliferation and differentiation

**Evidence summary**
Astrocytes maintain specialized ion buffering capacity critical for normal CNS function. SLC4A4 participates in pH regulation; potassium channels including KCNQ5 and KCNN3 regulate excitability; ITPR2 mediates calcium release from endoplasmic reticulum. Dysregulation of these ion homeostasis genes in astrocytomas would predictably impair the buffering capacity that characterizes normal astrocytes, with consequent alterations in osmoregulation, pH control, and calcium signaling that favor tumor cell proliferation while reducing metabolic support for neurons.

**Atomic biological processes**
- Sodium-bicarbonate cotransport and pH regulation. Genes: SLC4A4
  - [10]: SLC4A4 participates in pH regulation and ion homeostasis in astrocytes
- Potassium channel activity and excitability. Genes: KCNQ5, KCNN3
  - [6]: Potassium channels regulate astrocyte and neuronal excitability
- Inositol 1,4,5-trisphosphate-mediated calcium release. Genes: ITPR2
  - [6]: ITPR2 mediates IP3-dependent calcium mobilization and astrocyte calcium oscillations
- Calcium-dependent signaling and gene expression. Genes: ITPR2, KCNN3
  - [6]: Astrocyte calcium oscillations coordinate activation and metabolic coupling

**Atomic cellular components**
- Ion transport proteins. Genes: SLC4A4, KCNQ5, KCNN3
  - [10]: SLC4A4 and potassium channels mediate ion homeostasis
- Calcium release channels. Genes: ITPR2
  - [6]: ITPR represents endoplasmic reticulum calcium release channel

**Required genes (not in input)**
- Genes: SLC1A2, GLUL, GS, GluN2B, GRIN2B
  - [10]: Glutamate transporters and NMDA receptors participate in astrocyte ion homeostasis

**Program citations**
- [6]: Comprehensive characterization of astrocyte activation and ion homeostasis
- [10]: Astrocyte-specific functions in ion buffering and homeostasis

## Program: Extracellular Matrix Remodeling
Dysregulation of matricellular proteins, ECM structural components, and matrix-degrading enzymes that fundamentally reorganizes the tumor microenvironment. This program facilitates angiogenesis, immune cell recruitment, and tumor cell invasion while simultaneously altering cell-ECM interactions that normally constrain cell behavior.

**Predicted impacts**
- Enhanced angiogenesis and neovascularization of tumors
- Increased immune cell infiltration into tumor microenvironment
- Facilitated tumor cell invasion and dissemination
- Altered cell-ECM signaling affecting proliferation and survival

**Evidence summary**
The input gene list includes matricellular proteins EFEMP1 (fibulin-3) and SPARCL1 (hevin) that typically restrict angiogenesis and promote cell adhesion, plus ECM components TNC (tenascin C) and COL28A1. Dysregulation of these genes predicts fundamentally remodeled tumor microenvironment. Importantly, TNC exhibits complex pro-tumoral roles, promoting invasion and EMT-like transitions while inhibiting chemosensitivity through PI3K/AKT signaling. TIMP3 regulates matrix metalloproteinase activity; loss of TIMP3 permits enhanced ECM degradation and invasion capacity. The balance between matricellular proteins restricting angiogenesis and ECM remodeling promoting tumor progression represents a critical determinant of astrocytoma aggressiveness.

**Atomic biological processes**
- Matricellular protein regulation of cell-ECM interactions. Genes: EFEMP1, SPARCL1
  - [27]: EFEMP1 (fibulin-3) regulates cell adhesion, differentiation, and angiogenesis as matricellular protein
- Angiogenesis regulation and blood vessel formation. Genes: EFEMP1, SPARCL1, TNC, COL28A1
  - [27]: Matricellular proteins restrict angiogenesis while ECM remodeling promotes neovascularization
- Epithelial-to-mesenchymal transition and invasion. Genes: TNC
  - [55]: TNC promotes glioma cell malignancy and inhibits chemosensitivity through PI3K/AKT activation
- Matrix metalloproteinase regulation and ECM degradation. Genes: TIMP3
  - [55]: TIMP3 inhibits matrix metalloproteinases regulating ECM degradation

**Atomic cellular components**
- Structural ECM proteins. Genes: COL28A1
  - [27]: Collagen and other structural proteins provide mechanical support
- Matricellular proteins. Genes: EFEMP1, SPARCL1
  - [27]: EFEMP1 and SPARCL1 serve as matricellular proteins regulating cell-ECM interactions
- Protease inhibitors and ECM-degrading enzymes. Genes: TIMP3
  - [55]: TIMP3 inhibits matrix metalloproteinases

**Required genes (not in input)**
- Genes: MMP2, MMP9, ADAMTS, VEGF, FGF
  - [55]: Matrix metalloproteinases and growth factors regulate ECM remodeling and angiogenesis

**Program citations**
- [55]: TNC promotes glioma cell malignancy and chemoresistance
- [27]: Matricellular proteins and angiogenesis regulation in tumor biology

## Program: Glutamate Metabolism and Neurotransmitter Transport
Dysregulation of glutamate transporters, glutamine cycling machinery, and neurotransmitter handling that disrupts the specialized metabolic relationship between astrocytes and neurons. This program predicts impaired extracellular glutamate clearance, glutamate-mediated excitotoxicity in surrounding neurons, and altered paracrine glutamate signaling supporting tumor cell proliferation.

**Predicted impacts**
- Impaired extracellular glutamate clearance and elevated extracellular glutamate
- Glutamate-mediated excitotoxicity in surrounding neurons
- Paracrine glutamate signaling supporting tumor proliferation through autocrine receptors
- Disrupted glutamate-glutamine cycle compromising neuronal neurotransmitter synthesis

**Evidence summary**
SLC1A3 (EAAT1/GLAST) represents the primary astrocytic glutamate transporter responsible for removing glutamate from extracellular space. Recent research demonstrates that SLC1A3 expression is significantly downregulated in astrocytes responding to traumatic brain injury and other stressful stimuli, resulting in impaired glutamate clearance and elevated extracellular glutamate. In astrocytomas, dysregulation of SLC1A3 would similarly impair glutamate clearance while potentially creating paracrine glutamate signaling that supports tumor cell proliferation through activation of glutamate receptors. The presence of CLU encoding clusterin, a secreted chaperone involved in stress response and lipid transport, suggests integration of glutamate metabolism with broader stress response and metabolic programs.

**Atomic biological processes**
- Extracellular glutamate clearance. Genes: SLC1A3
  - [10]: SLC1A3 (EAAT1/GLAST) represents primary astrocytic glutamate transporter
  - [6]: SLC1A3 downregulation in reactive astrocytes impairs glutamate clearance
  - [18]: Glutamate transporters SLC1A3 and SLC1A2 dysregulation in disease
- Glutamate-glutamine cycle. Genes: SLC1A3
  - [10]: Astrocytes accumulate glutamate and convert to glutamine for neuronal recycling
- Stress response and lipid metabolism in astrocytes. Genes: CLU
  - [26]: Clusterin participates in lipid transport and stress response in astrocytes

**Atomic cellular components**
- Glutamate transporter proteins. Genes: SLC1A3
  - [10]: SLC1A3 represents plasma membrane glutamate transporter

**Required genes (not in input)**
- Genes: GLUL, GS, GRIN1, GRIN2A, GRIN2B
  - [10]: Glutamine synthetase and NMDA receptors participate in glutamate metabolism

**Program citations**
- [10]: Astrocyte-specific glutamate transporter SLC1A3 and glutamate-glutamine cycle
- [6]: SLC1A3 downregulation in reactive and injured astrocytes

## Program: Developmental Signaling and Stemness
Dysregulation of developmental signaling pathways including Notch and Wnt/β-catenin that promote maintenance of progenitor-like tumor cells with enhanced self-renewal capacity. This program connects transcriptional regulation to stemness acquisition and supports tumor-initiating cell populations.

**Predicted impacts**
- Enhanced self-renewal capacity and stemness acquisition
- Expansion of tumor-initiating cell populations
- Reduced terminal differentiation and increased progenitor maintenance
- Enhanced tumorigenic potential and resistance to differentiation therapy

**Evidence summary**
HES4 functions as a direct target of Notch signaling promoting astrocyte progenitor proliferation while inhibiting differentiation. YAP1 represents a critical downstream effector of both Hippo and Wnt/β-catenin pathways, controlling proliferation, survival, and stemness through multiple effector networks. Recent 2025 research demonstrates that YAP1 dysregulation through Hippo pathway inactivation or enhanced Wnt/β-catenin signaling promotes nuclear YAP1 localization and increased transcriptional activity. In astrocytomas, dysregulation of developmental signaling through HES4 and YAP1 would predictably promote maintenance of progenitor-like phenotypes with enhanced self-renewal capacity but reduced differentiation capacity, expanding the tumor-initiating cell pool.

**Atomic biological processes**
- Notch signaling and progenitor maintenance. Genes: HES4
  - [25]: Notch1 pathway regulates glioma stem cell characteristics
- YAP/Hippo signaling and transcriptional regulation. Genes: YAP1
  - [36]: KSR1 scaffolds the Hippo pathway regulating YAP transcriptional activity
  - [39]: Piezo1-mediated mechanotransduction controls YAP signaling and cell fate
- Wnt/β-catenin signaling in tumor stemness. Genes: YAP1
  - [49]: RGS20 regulates glioma stemness through WNT/β-catenin pathway

**Atomic cellular components**
- Transcriptional machinery. Genes: YAP1, HES4
  - [36]: YAP functions as transcriptional co-activator binding TEAD family

**Required genes (not in input)**
- Genes: NOTCH1, JAG1, DLL1, WNT3A, CTNNB1
  - [25]: Notch ligands and canonical Wnt pathway components regulate stemness

**Program citations**
- [36]: KSR1 scaffolds Hippo signaling and regulates YAP function
- [49]: RGS20 regulates glioma stemness through WNT/β-catenin signaling

## Program: Synaptic Organization and Neural Circuit Formation
Expression of genes encoding synaptic proteins, vesicular transport machinery, and neurotransmitter receptors that may reflect aberrant expression of neuronal genes due to transformation or alternatively represent altered astrocyte-neuron communication within the tumor microenvironment. This program predicts dysregulation of normal astrocyte-neuron metabolic coupling.

**Predicted impacts**
- Aberrant expression of neuronal genes in non-neuronal tumor cells
- Altered astrocyte-neuron communication and reduced metabolic coupling
- Dysregulation of paracrine signaling between tumor and neurons
- Potential acquisition of neuronal-like properties in transformed astrocytes

**Evidence summary**
While astrocytomas are non-neuronal tumors, the input gene list includes multiple genes encoding synaptic proteins (SYTL4, CADPS, PRUNE2) and neurotransmitter receptors (GRIK1). This dysregulation may reflect either aberrant expression of neuronal genes due to transformation-associated loss of cell-type specificity, or alternatively, may represent expression of synaptic-associated genes that contribute to altered astrocyte-neuron communication within the tumor microenvironment. Recent research demonstrates that astrocytes express non-synaptic neurotransmitter receptors and participate in complex signaling with neuronal and other glial cells. Dysregulation of synaptic gene expression in astrocytomas may facilitate paracrine signaling that simultaneously promotes tumor proliferation while disrupting normal astrocyte support functions.

**Atomic biological processes**
- Vesicular neurotransmitter transport. Genes: SYTL4, CADPS
  - [3]: SYTL4 (granuphilin) participates in vesicle docking and exocytosis
- Cytoskeletal regulation of synaptic assembly. Genes: PRUNE2
  - [3]: PRUNE2 participates in cytoskeletal regulation and vesicular trafficking
- Glutamate receptor signaling. Genes: GRIK1
  - [12]: GRIK1 encodes kainate receptor subtype with astrocyte roles

**Atomic cellular components**
- Synaptic vesicles and docking machinery. Genes: SYTL4, CADPS
  - [3]: SYTL4 and CADPS regulate exocytosis and vesicle release
- Neurotransmitter receptors. Genes: GRIK1
  - [12]: GRIK1 represents glutamate receptor subtype

**Required genes (not in input)**
- Genes: SNAP25, VAMP2, STX1A, SYNAPSIN, SPECTRIN
  - [3]: Core synaptic proteins mediating vesicle release and synaptic transmission

**Program citations**
- [3]: Synaptic protein expression in astrocyte-to-neuron conversion studies
- [12]: GRIK1 and other glutamate receptor roles in astrocytes

## Program: Inflammatory and Immune Response
Dysregulation of inflammatory signaling, pattern recognition receptors, and cytokine/chemokine networks that creates a pro-tumoral inflammatory microenvironment. This program predicts recruitment of immune cells, establishment of immunosuppressive niches, and paracrine signaling supporting tumor growth.

**Predicted impacts**
- Enhanced local complement activation and recruitment of immune cells
- Establishment of pro-tumoral type 2 immune responses
- Increased immune infiltration into tumor microenvironment
- Altered balance between pro-tumoral and anti-tumor immune responses

**Evidence summary**
Recent research on astrocyte biology reveals that astrocytes undergo profound transcriptional reprogramming in response to injury and inflammatory stimuli, acquiring pro-inflammatory phenotypes characterized by upregulation of interferons, complement components, and cytokine/chemokine networks. MASP1 participates in complement activation through the lectin pathway; IL33 represents an IL-1 family cytokine participating in type 2 immune responses and astrocyte-immune cell interactions; IFI44L participates in interferon-mediated immune responses. In astrocytomas, dysregulation of these inflammatory genes would promote local complement activation, recruitment of pro-tumoral immune cells, and creation of an immunosuppressive microenvironment supporting tumor growth.

**Atomic biological processes**
- Complement pathway activation. Genes: MASP1
  - [27]: MASP1 participates in complement activation through the lectin pathway
- IL-33 signaling and astrocyte-immune interactions. Genes: IL33
  - [23]: IL33 upregulation in astrocytes participates in neuron-astrocyte interactions during injury
- Interferon and cytokine signaling. Genes: IFI44L
  - [6]: Astrocytes upregulate interferon and inflammatory cytokines in response to injury

**Atomic cellular components**
- Pattern recognition receptors. Genes: MASP1
  - [27]: MASP1 and complement components recognize pathogen-associated patterns

**Required genes (not in input)**
- Genes: TNF, IL1B, IL6, CXCL10, CCL2
  - [6]: Pro-inflammatory cytokines and chemokines upregulated in reactive astrocytes

**Program citations**
- [27]: Complement pathway and inflammatory response in tumor biology
- [6]: IL33 and inflammatory signaling in astrocytes

## Program: Treatment Resistance and Genomic Instability
Dysregulation of metabolic plasticity, DNA repair pathways, autophagy, and checkpoint control that collectively enables astrocytomas to survive genotoxic chemotherapy and accumulate genomic alterations. This program connects metabolic reprogramming to genomic instability and predicts enhanced treatment resistance.

**Predicted impacts**
- Enhanced chemotherapy resistance through DNA repair pathway activation
- Metabolic plasticity enabling survival under diverse nutrient-stressed conditions
- Accumulated genomic alterations and clonal evolution
- Activation of alternative oncogenic drivers upon single-pathway inhibition

**Evidence summary**
Recent 2025 research demonstrates that tumor-derived APOE promotes chemoresistance through SCARB1-mediated lipid uptake and activation of homologous recombination repair pathways via the β-catenin-BRCA1/2 axis. The coordinate dysregulation of lipid metabolism genes (APOE, ABCA1, PLTP, FADS2) enables metabolic flexibility and enhanced DNA repair capacity. Patient-derived cells from NTRK2-fusion astrocytomas initially respond to TRK inhibitors but develop resistance through acquisition of additional oncogenic drivers including FGFR2, RUNX1T1, and VEGFR signaling. This suggests that astrocytomas exploit multiple interconnected pathways, and disruption of any single pathway triggers compensatory activation of alternative pathways. Enhanced autophagy capacity through dysregulation of genes like LYST (lysosomal trafficking regulator) supports tumor cell survival under therapy-induced stress.

**Atomic biological processes**
- DNA damage and repair pathway activation. Genes: APOE, NTRK2
  - [28]: APOE-mediated lipid uptake activates homologous recombination repair via β-catenin-BRCA1/2 axis
  - [21]: NTRK2-fusion astrocytomas acquire additional oncogenic drivers in response to TRK inhibitor treatment
- Metabolic flexibility and chemotherapy resistance. Genes: APOE, ABCA1, PLTP, FADS2
  - [28]: Enhanced lipid metabolism confers chemotherapy resistance
- Autophagy and lysosomal function. Genes: LYST
  - [6]: Dysregulated autophagy in astrocytes participates in stress response

**Atomic cellular components**
- DNA repair machinery. Genes: APOE
  - [28]: β-catenin-BRCA1/2 complexes mediate homologous recombination repair
- Autophagy and lysosomal compartments. Genes: LYST
  - [6]: Lysosomes and autophagy machinery regulate cellular stress responses

**Required genes (not in input)**
- Genes: BRCA1, BRCA2, RAD51, TP53, MDM2
  - [28]: Core DNA repair and checkpoint control genes

**Program citations**
- [28]: APOE and metabolic plasticity in chemotherapy resistance
- [21]: NTRK2-fusion astrocytomas and acquired treatment resistance

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
2. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
3. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
4. Available from: https://www.ncbi.nlm.nih.gov/gene/546
5. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
6. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
7. Available from: https://www.ncbi.nlm.nih.gov/gene/3400
8. Qinghua L, Wenqiang Q, Qian C, Chris S, Wenlin H, Jing Y, et al.. Brain-derived neurotrophic factor supports pericyte and vascular homeostasis in the aging brain.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41327464/
9. Haesung L, Ngoc BT, Sook-Jeong L. Astrocytic gatekeeping of neural circuitry and synaptic balance in an autism mouse model: mechanistic insights beyond . Frontiers in cell and developmental biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41367497/?fc=None&ff=20251215163942&v=2.18.0.post22+67771e2
10. Available from: https://www.ncbi.nlm.nih.gov/gene/3399
11. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
12. Available from: https://www.ncbi.nlm.nih.gov/gene/24387
13. Available from: https://www.ncbi.nlm.nih.gov/gene/999
14. Available from: https://www.ncbi.nlm.nih.gov/gene/1009
15. Available from: https://www.ncbi.nlm.nih.gov/gene/51684
16. Available from: https://www.ncbi.nlm.nih.gov/gene/5879
17. André LTES, Pedro HP de O, Bruno YY-M, Jéssica da SF, Jonatan PA, Helder IN, et al.. Complement pathway dysregulation and astrocyte alterations in Down syndrome: evidence from postmortem brain tissue and iPSC-derived astrocytes.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41350900/?fc=None&ff=20251210050700&v=2.18.0.post22+67771e2
18. Available from: https://www.ncbi.nlm.nih.gov/gene/24069
19. Available from: https://www.ncbi.nlm.nih.gov/gene/20512
20. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
21. Available from: https://www.ncbi.nlm.nih.gov/gene/29499
22. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
23. Available from: https://www.ncbi.nlm.nih.gov/gene/4851
24. Phan TT, Shin S, Kim HJ, Lee K, Kim T-Y, Lee J-H, et al.. Harnessing theta-gamma coupled brainwaves using ultrasound for spinal astrocyte revitalization and sustained neuropathic pain relief in mice. Nature Communications [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41467-025-66980-6
25. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
26. Lou X, Shi Y, Qin Y, Zhang W, Ye Z, Wang F, et al.. Tumor-derived apolipoprotein E confers resistance to temozolomide in pancreatic neuroendocrine tumors. Cell Death &amp; Disease [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41419-025-08317-1
27. Available from: https://www.ncbi.nlm.nih.gov/gene/361
28. Available from: https://www.ncbi.nlm.nih.gov/gene/341
29. Yusuf AM, Ilce BY, Alhaj HA, Hamoudi R. α-synuclein in Parkinson’s disease: a central point of convergence with depression. npj Parkinson's Disease [Internet]. 2025Nov20;11(1). Available from: https://www.nature.com/articles/s41531-025-01167-w
30. Available from: https://www.ncbi.nlm.nih.gov/gene/5629
31. Available from: https://www.ncbi.nlm.nih.gov/gene/56288
32. Available from: https://www.ncbi.nlm.nih.gov/gene/4217
33. Available from: https://www.ncbi.nlm.nih.gov/gene/93742
34. Sayedyahossein S, Babu SMR, Li Z, Banerjee R, Tran A, Thines L, et al.. KSR1 is a scaffold for the Hippo signaling pathway. Communications Biology [Internet]. 2025Dec1;8(1). Available from: https://www.nature.com/articles/s42003-025-09009-4
35. Available from: https://www.ncbi.nlm.nih.gov/gene/2308
36. Available from: https://www.ncbi.nlm.nih.gov/gene/83596
37. Hu YJ, Wu X, Wang F, Jin Y, Jin Y, Liu Y, et al.. Piezo1-mediated mechanotransduction controls osteocyte maturation and dendrite development via a YAP-CCN-Src signaling axis. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-65636-9
38. Available from: https://www.ncbi.nlm.nih.gov/gene/56458
39. Available from: https://www.ncbi.nlm.nih.gov/gene/598
40. Available from: https://www.ncbi.nlm.nih.gov/gene/2152
41. Available from: https://www.ncbi.nlm.nih.gov/gene/3691
42. Available from: https://www.ncbi.nlm.nih.gov/gene/20563
43. Available from: https://www.ncbi.nlm.nih.gov/gene/4162
44. Available from: https://www.ncbi.nlm.nih.gov/gene/192897
45. Available from: https://www.ncbi.nlm.nih.gov/gene/9353
46. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z
47. Guo C, Zhang J, Zhang S, Moon J, Yang R, Guan X, et al.. Programmable Argonaute-mediated single-nucleotide variant sequencing of cell-free DNA for multi-cancer early detection. Nature Communications [Internet]. 2025Dec3;. Available from: https://www.nature.com/articles/s41467-025-66893-4
48. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
49. Sibley LA, Cowan MN, Kelly AG, Amadi NA, Babcock IW, Labuzan SA, et al.. Caspase-8 expression in CD8
                    <sup>+</sup>
                    T cells promotes pathogen restriction in the brain during
                    <i>Toxoplasma gondii</i>
                    infection. Science Advances [Internet]. 2025Dec12;11(50). Available from: https://www.science.org/doi/10.1126/sciadv.adz4468
50. Available from: https://www.ncbi.nlm.nih.gov/gene/3371
51. Available from: https://www.ncbi.nlm.nih.gov/gene/2066
52. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=3371
53. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
54. Available from: https://www.ncbi.nlm.nih.gov/gene/12505
55. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
56. Available from: https://www.ncbi.nlm.nih.gov/gene/20358
57. Available from: https://www.ncbi.nlm.nih.gov/gene/7130
58. Available from: https://www.ncbi.nlm.nih.gov/gene/3566
59. Available from: https://www.ncbi.nlm.nih.gov/gene/19
60. Available from: https://www.ncbi.nlm.nih.gov/gene/3976
61. Available from: https://www.ncbi.nlm.nih.gov/gene/11303
62. Bai Y, Zhang X, Wang X, Wang M, Shen T. Characterizing and decoding ultraconserved regions uncovers their regulatory significance in human brain development and disorders. Communications Biology [Internet]. 2025Nov27;8(1). Available from: https://www.nature.com/articles/s42003-025-09115-3
63. Meng J, Zhang Y, Zhu M, Du Y, Yao Y, Liu S, et al.. Single-cell profiling reveals a shared proinflammatory macrophage signature across multiple organs in myopia. Cell Discovery [Internet]. 2025Dec2;11(1). Available from: https://www.nature.com/articles/s41421-025-00835-8
64. Jiang R, Lu Z, Li F, Zhu Y, Yang M, Zhang S, et al.. scCirclehunter delineates ecDNA-containing cells using single-cell ATAC-seq, with a focus on glioblastoma. Cell Discovery [Internet]. 2025Dec9;11(1). Available from: https://www.nature.com/articles/s41421-025-00842-9
65. da SNL, de MGVRM, Oliveira-Nazareth Y, da SRS, Campello-Costa P. Effects of caffeine on neuroinflammation in anxiety and depression: a systematic review of rodent studies. Translational Psychiatry [Internet]. 2025Nov17;15(1). Available from: https://www.nature.com/articles/s41398-025-03668-x
66. Available from: http://json-schema.org/draft-07/schema#",
