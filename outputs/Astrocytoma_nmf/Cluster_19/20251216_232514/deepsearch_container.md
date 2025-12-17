# Gene Program Markdown Report

## Context
- Cell type: Oligodendrocytes, Oligodendrocyte Progenitor Cells (OPCs), and Astrocytes
- Disease: Astrocytoma
- Tissue: Central Nervous System (CNS), brain

## Input Genes
LSAMP, AC110285.1, SSH2, SLC44A1, RASGEF1B, RAPGEF1, ENPP6, EPB41L2, PKP4, BMPER, PKP4-AS1, PLCB1, TMEM163, TMEM132B, TMEM108, BCAS1, GPR17, AL359091.1, SOX6, PRKCE, SRCIN1, TF, TCF7L2, FYN, PPP1R16B, ... (200 total)

## Program: Oligodendrocyte Transcriptional Specification
Master regulatory program coordinating oligodendrocyte lineage commitment and differentiation through sequential activation of stage-specific transcription factors. SOX10 initiates oligodendroglial fate and maintains progenitor identity while promoting differentiation. MYRF amplifies and completes the mature oligodendrocyte transcriptional program. SOX6 refines mature oligodendrocyte identity and myelin gene expression. TCF7L2 serves as a co-factor in SOX-containing complexes that activate oligodendrocyte-specific genes. RBPJ mediates Notch signaling effects on oligodendrocyte differentiation. ZEB2 fine-tunes transcriptional networks through repression of alternative cell fate programs. TFEB regulates lysosomal and autophagy genes critical during cellular stress responses.

**Predicted impacts**
- Enhanced commitment to oligodendrocyte fate and reduced plasticity toward alternative lineages
- Activation of complete myelin biosynthesis machinery
- Upregulation of mature oligodendrocyte structural and functional proteins
- Suppression of progenitor cell markers and proliferation programs
- Increased capacity for myelinogenesis and axon-glial interaction

**Evidence summary**
The oligodendrocyte transcriptional specification program represents the foundational regulatory tier controlling oligodendrocyte lineage commitment and differentiation. Recent single-cell transcriptomic analyses of developing CNS and glioma tissues have defined these core transcription factors as master regulators establishing and maintaining oligodendrocyte identity. The presence of all six major transcription factors (SOX10, MYRF, SOX6, TCF7L2, RBPJ, ZEB2) in the input gene list indicates a highly differentiated oligodendrocyte or OPC population. In astrocytoma context, this program is typically suppressed in tumor cells but may be preserved or partially activated in non-tumor oligodendrocytes within the microenvironment. Recent studies show that glioblastomas contain populations of mature oligodendrocytes that retain this transcriptional program despite tumor-associated stresses.

**Atomic biological processes**
- Oligodendrocyte fate specification. Genes: SOX10, MYRF, SOX6, TCF7L2, RBPJ, ZEB2, TFEB
  - [25]: SOX10 as master regulator of oligodendrocyte development
  - [26]: SOX10 and MYRF in oligodendrocyte differentiation trajectories
  - [2]: TCF7L2 in oligodendrocyte specification networks
- Notch signaling in glial differentiation. Genes: RBPJ
  - [20]: RBPJ downregulation promoting neurogenesis in astrocyte progenitors
  - [30]: RBPJ role in neuroglial lineage specification
- Stress response and cellular adaptation. Genes: TFEB
  - [25]: TFEB regulation of lysosomal function during cellular stress
  - [16]: Transcriptional responses to injury in astrocytes

**Atomic cellular components**
- Oligodendrocyte transcriptional complex. Genes: SOX10, MYRF, SOX6, TCF7L2, RBPJ
  - [25]: SOX-bHLH transcriptional complexes in oligodendrogenesis
  - [26]: MYRF as direct activator of myelin genes

**Required genes (not in input)**
- Genes: OLIG1, OLIG2, NKX2.2, NKX6.2, ASCL1
  - [25]: OLIG1 and OLIG2 as obligate oligodendrocyte regulators during development
  - [26]: NKX family transcription factors in oligodendrocyte specification
  - [2]: ASCL1 SA6 variant induces neuronal vs oligodendrocyte fate

**Program citations**
- [25]: Comprehensive characterization of oligodendrocyte development and cell states including SOX10, MYRF, and SOX6 function
- [26]: Transcriptomic and epigenomic responses of oligodendrocytes during development
- [2]: Ascl1 SA6 reprogramming and transcriptional specification in neural differentiation
- [1]: Transcriptional control of oligodendrocyte differentiation
- [20]: RBPJ role in neuroglial cell fate decisions after TBI

## Program: Myelin Protein Assembly and Structure
Coordinated expression and assembly of the structural protein scaffolding that forms the myelin sheath. MBP comprises ~30% of myelin dry weight and mediates myelin compaction. PLP1 is the most abundant CNS myelin protein and functions in myelin stability and axon-glial junctions. MOG localizes to myelin outer surface and mediates immune interactions. MAG localizes to inner myelin loops and mediates axon-glial signaling. CNP functions in myelin structure maintenance and oligodendrocyte biology. These five core myelin proteins establish the fundamental structural organization of myelinated axons. Additional membrane proteins and structural scaffolds organize the axon-glial interface.

**Predicted impacts**
- Formation of stable, compacted myelin sheath with proper thickness
- Establishment of functional myelin-axon interface
- Enhanced rapid saltatory conduction of action potentials
- Protection of axons from oxidative stress and mechanical damage
- Integration of structural support with immune regulatory functions

**Evidence summary**
The myelin protein assembly program represents the most directly observable phenotype of mature oligodendrocytes—the production of myelin wrapping around axons. The five core structural proteins (MBP, PLP1, MOG, MAG, CNP) are universally considered markers of mature oligodendrocyte differentiation and myelinating capacity. Their coordinated expression reaches peak levels in mature oligodendrocytes and is largely absent in OPCs. In astrocytoma context, these proteins are typically downregulated in tumor-associated demyelinated regions but may be preserved in tumor-adjacent white matter with relatively intact oligodendrocytes. The presence of all five core structural proteins in the input gene list strongly indicates sampling of mature, myelinating oligodendrocytes. Loss of these markers in tumor tissue or adjacent regions indicates demyelination and oligodendrocyte dysfunction, which correlates with increased tumor invasiveness and worse clinical outcomes.

**Atomic biological processes**
- Myelin compaction and structural organization. Genes: MBP, PLP1, MOG, MAG, CNP
  - [25]: MBP and PLP1 as structural foundation of CNS myelin
  - [26]: Progressive myelination and myelin protein expression during development
  - [1]: MBP and PLP1 in oligodendrocyte differentiation
- Myelin-axon interface formation. Genes: PLP1, MAG, MOG, NFASC
  - [25]: Axon-glial interactions mediated by myelin proteins
  - [1]: MAG role in axon-glial signaling

**Atomic cellular components**
- Myelin sheath structural core. Genes: MBP, PLP1, MOG, MAG, CNP
  - [26]: Myelin basic protein and PLP1 as principal myelin structural components
  - [25]: Characterization of mature oligodendrocyte myelin proteins

**Required genes (not in input)**
- Genes: MPZL1, OSP, MOA
  - [25]: Additional myelin structural proteins supporting core scaffolds

**Program citations**
- [25]: Comprehensive characterization of myelin proteins and myelination during PFC development
- [26]: Expression of MBP and MOG in mature oligodendrocytes across development
- [1]: MBP and PLP1 as canonical oligodendrocyte differentiation markers

## Program: Myelin Lipid Biosynthesis and Metabolism
Specialized lipid biosynthetic pathway producing the unique lipid composition of myelin, which comprises ~70% of myelin dry weight. FA2H catalyzes hydroxylation of fatty acids to generate 2-hydroxy fatty acids that are particularly enriched in myelin and brain tissue. UGT8 synthesizes galactocerebroside and sulfatide, the major glycosphingolipids of myelin, which comprise 20-30% of myelin dry weight. CNP functions in myelin lipid metabolism and regulates oligodendrocyte proliferation and differentiation. These genes collectively ensure that oligodendrocytes synthesize lipids with the characteristic composition of myelin, including enrichment in cholesterol, galactosylceramides, and phosphatidylethanolamine. Coordinated expression of these lipid-processing enzymes with myelin protein genes ensures stoichiometric production of lipids and proteins for myelin assembly.

**Predicted impacts**
- Production of specialized myelin lipid composition with enriched 2-hydroxy fatty acids and galactosylceramides
- Proper stoichiometric ratio of lipid to protein in myelin assembly
- Enhanced myelin stability and durability
- Integration of lipid metabolism with oligodendrocyte proliferation and differentiation
- Metabolic support for continuous myelin maintenance and turnover

**Evidence summary**
The myelin lipid biosynthesis program reflects the extraordinary metabolic demands of oligodendrocytes, which must continuously synthesize and export vast quantities of lipid to maintain myelin. The three genes in this program (FA2H, UGT8, CNP) represent key enzymatic steps in generating the characteristic lipid composition of myelin. Myelin lipids are dramatically enriched in certain species compared to other cell membranes, including 2-hydroxy fatty acids (generated by FA2H) and galactosylceramides (generated by UGT8), reflecting the specialized functions of these lipids in myelin physiology. The presence of all three genes indicates metabolic competence in myelin lipid synthesis. In astrocytoma context, oligodendrocytes in the tumor microenvironment may show reduced lipid biosynthetic capacity due to metabolic stress or inflammatory signals, leading to reduced myelin production and progressive demyelination.

**Atomic biological processes**
- Fatty acid processing for myelin. Genes: FA2H
  - [25]: FA2H in myelin lipid composition
  - [1]: Fatty acid hydroxylation in oligodendrocyte differentiation
- Glycosphingolipid synthesis. Genes: UGT8
  - [25]: UGT8 in galactocerebroside and sulfatide synthesis
  - [26]: Expression of UGT8 in mature oligodendrocytes
- Myelin lipid homeostasis. Genes: CNP
  - [25]: CNP role in myelin lipid metabolism
  - [1]: CNP expression in mature oligodendrocytes

**Atomic cellular components**
- Lipid biosynthetic enzymes. Genes: FA2H, UGT8, CNP
  - [25]: FA2H and UGT8 as major myelin lipid biosynthetic enzymes
  - [26]: Specialized lipid metabolism in mature oligodendrocytes

**Required genes (not in input)**
- Genes: CERS2, SPTLC1, SGPL1
  - [25]: Additional lipid biosynthetic enzymes in specialized myelin lipid synthesis

**Program citations**
- [25]: FA2H and UGT8 expression in mature oligodendrocytes and myelin composition
- [26]: Lipid metabolism genes in oligodendrocyte differentiation
- [1]: Specialized myelin lipid synthesis in oligodendrocytes

## Program: Glial Cell Adhesion and Junction Proteins
Coordinated expression of adhesion molecules and junction proteins that establish and maintain stable associations between oligodendrocytes and axons, between oligodendrocytes and other glial cells, and between glial cells and the extracellular matrix. PKP4 functions as a desmosomal plaque protein linking cadherins to intermediate filaments. Classical cadherins (PCDH7, CDH19) mediate calcium-dependent cell-cell adhesion critical for axon-glial junctions. CAMs (CADM1, CADM2) mediate homophilic adhesion and synaptic assembly. CLDN11 forms tight junctions at the blood-brain barrier and contributes to glial-glial sealing. NFASC localizes to axon initial segments and nodes of Ranvier where it coordinates adhesion and ion channel organization. These adhesion molecules collectively organize the multi-layered junction architecture that compartmentalizes nervous tissue and maintains proper cellular relationships.

**Predicted impacts**
- Stable axon-glial junctions with appropriate mechanical strength
- Compartmentalization of nervous tissue and prevention of immune infiltration
- Proper node of Ranvier architecture and rapid action potential conduction
- Maintenance of blood-brain barrier integrity
- Prevention of pathological cell migration and invasion
- Establishment of glial-glial networks with proper spacing and communication

**Evidence summary**
The glial cell adhesion program represents the structural architecture that organizes the nervous system into functional compartments and establishes the critical intercellular contacts that support neuronal function. The presence of multiple independent adhesion systems (desmosomal, classical cadherin, CAM, claudin, and nodal adhesion proteins) indicates multiple redundant mechanisms ensuring robust adhesion. In normal CNS, this multi-layered adhesion system maintains proper cellular relationships and prevents inappropriate cell migration. In astrocytoma context, adhesion molecules are frequently downregulated, contributing to loss of contact inhibition, enhanced cell migration and invasion, and disruption of normal glial-neuronal relationships. Studies of high-grade gliomas consistently show reduced expression of adhesion proteins including cadherins, claudins, and CAMs, which enables tumor cells to escape their tissue context and promotes invasive behavior.

**Atomic biological processes**
- Axon-glial junction formation and maintenance. Genes: PCDH7, CDH19, CADM1, CADM2, MAG, MOG
  - [25]: Cadherin-mediated axon-glial junctions during myelination
  - [1]: CDH19 and PCDH7 in axon-glial interactions
  - [26]: Oligodendrocyte-axon interface proteins
- Desmosomal and adherens junction assembly. Genes: PKP4
  - [35]: PKP4 function in desmosomal plaque assembly
- Blood-brain barrier and tight junction formation. Genes: CLDN11
  - [25]: CLDN11 expression at glial-endothelial junctions
  - [26]: Tight junction proteins in BBB function
- Node of Ranvier organization. Genes: NFASC
  - [25]: NFASC localization to nodes and paranodes

**Atomic cellular components**
- Cadherin-based adhesion complex. Genes: PCDH7, CDH19, CADM1, CADM2
  - [25]: Cadherin-catenin complexes in axon-glial junctions
- Desmosomal plaque. Genes: PKP4
  - [35]: PKP4-mediated desmosomal organization
- Tight junction strands. Genes: CLDN11
  - [25]: CLDN11 as core tight junction protein

**Required genes (not in input)**
- Genes: NCAM1, NCAM2, L1CAM, CONTACTIN
  - [25]: Additional adhesion molecules in glial-neuronal interactions

**Program citations**
- [25]: Comprehensive characterization of adhesion proteins in CNS development and mature tissue
- [26]: Cadherin and claudin expression in oligodendrocyte development
- [1]: Adhesion molecules in axon-glial interactions
- [16]: Altered adhesion protein expression following CNS injury

## Program: Semaphorin-Plexin Axon Guidance Signaling
Extracellular signaling system mediating repulsive and attractive guidance cues that establish proper neural circuit architecture and maintain appropriate axon-glial relationships. SEMA3E, SEMA4D, SEMA5A, and SEMA5B represent a family of secreted and membrane-bound ligands that signal through plexin and neuropilin receptors on responding cells. SEMA4D is expressed on oligodendrocytes and functions as a growth inhibitory signal preventing axon overgrowth. SEMA3E and SEMA5A function as chemorepellents during axon guidance. These semaphorins signal through plexin receptors which activate downstream Rho GTPase signaling cascades. The semaphorin-Rho signaling axis dynamically remodels the cytoskeleton to produce morphological changes and altered migratory behavior.

**Predicted impacts**
- Repulsion of axons from oligodendrocyte processes during development and maintenance of established myelination patterns
- Prevention of aberrant axon growth within myelinated regions
- Dynamically adjustable oligodendrocyte morphology in response to local axonal signals
- Integration of multiple guidance cues to establish proper neural circuit topology
- Maintenance of appropriate spacing between axons and glial processes

**Evidence summary**
The semaphorin-plexin signaling program provides cell-cell communication mechanisms that allow oligodendrocytes to sense and respond to the axonal environment, and allow axons to respond to glial signals. Semaphorin ligands are secreted or membrane-tethered proteins that signal at cell-cell contacts or over short distances, making them ideal for local circuit organization. SEMA4D expression on oligodendrocytes creates a biochemical boundary that discourages excessive axon growth within myelinating regions, helping to maintain appropriate g-ratios (ratio of axon diameter to myelinated fiber diameter). In astrocytoma context, semaphorin signaling is often dysregulated, with altered semaphorin and plexin expression contributing to aberrant axon-tumor cell interactions and disrupted neural circuit function. Additionally, semaphorin signaling plays roles in immune cell migration and interaction with tumor cells, contributing to the immunological landscape of glioblastomas.

**Atomic biological processes**
- Semaphorin-plexin signal transduction. Genes: SEMA3E, SEMA4D, SEMA5A, SEMA5B
  - [13]: Ephrin-Eph signaling parallel to semaphorin-plexin axes in neural signaling
  - [25]: Semaphorin signaling in axon guidance and glial development
  - [1]: SEMA4D as oligodendrocyte-expressed growth inhibitor
- Axon guidance and pathfinding. Genes: SEMA3E, SEMA5A, SEMA5B, NTN1, SEMA6D
  - [13]: Axon guidance mechanisms including semaphorin signaling
  - [25]: Semaphorins in establishing proper neural circuit architecture
- Oligodendrocyte-axon spacing regulation. Genes: SEMA4D, MAG
  - [1]: SEMA4D-mediated inhibition of axon overgrowth within myelinated regions
  - [25]: SEMA4D in maintaining proper myelin thickness

**Atomic cellular components**
- Semaphorin ligand family. Genes: SEMA3E, SEMA4D, SEMA5A, SEMA5B, SEMA6D
  - [25]: Diverse semaphorin family members in CNS guidance

**Required genes (not in input)**
- Genes: PLXNA1, PLXNA2, PLXND1, NRP1, NRP2
  - [25]: Plexin and neuropilin receptors as semaphorin signal transducers

**Program citations**
- [25]: Comprehensive analysis of semaphorin-plexin signaling in CNS development and glial interactions
- [13]: Ephrin-Eph and related guidance signaling in neural circuits
- [1]: SEMA4D expressed on oligodendrocytes as axon growth inhibitor

## Program: Rho GTPase Signaling and Cytoskeletal Dynamics
Coordinated signaling system regulating Rho family GTPase (RhoA, Rac1, Cdc42) activation and downstream cytoskeletal remodeling. GEFs (guanine nucleotide exchange factors) including ARFGEF3, RASGEF1B, and RAPGEF1 promote GDP-GTP exchange to activate Rho GTPases. GAPs (GTPase-activating proteins) including ARHGAP5 and ARHGAP31 promote GTP hydrolysis to inactivate Rho GTPases. Downstream effector proteins including SHROOM4 (links Rho signaling to actomyosin dynamics), ADD3 (links Rho signaling to actin polymerization), and FRMD proteins mediate focal adhesion dynamics. This integrated program dynamically remodels actin and microtubule cytoskeletons in response to external signals, enabling cell morphological changes, migration, and process outgrowth.

**Predicted impacts**
- Dynamic remodeling of actin cytoskeleton in response to environmental cues
- Rapid transition between exploratory and retracted cell morphology
- Enhanced migratory capacity and process extension
- Responsive adjustment of focal adhesions at cell-substrate interface
- Integration of multiple guidance signals into coordinated cytoskeletal response

**Evidence summary**
The Rho GTPase signaling program represents one of the most fundamental and extensively interconnected cytoskeletal regulatory systems in cells. Rho family GTPases (RhoA, Rac1, Cdc42) serve as molecular switches that transduce extracellular signals into cytoskeletal rearrangements, and are regulated by a large family of GEFs and GAPs that provide signal specificity and spatial localization. The presence of multiple GEFs, multiple GAPs, and multiple downstream effectors in the input gene list indicates a high capacity for dynamic cytoskeletal remodeling in response to environmental signals. In oligodendrocytes, Rho signaling controls process outgrowth and retraction, allowing individual oligodendrocytes to dynamically adjust their morphology as they extend processes along multiple axons. In astrocytoma context, Rho signaling is typically enhanced in tumor cells, contributing to their increased motility and invasiveness, while simultaneously altered Rho signaling in tumor-associated oligodendrocytes might contribute to their reduced myelinating capacity and altered responses to the tumor microenvironment.

**Atomic biological processes**
- Rho GTPase activation by GEFs. Genes: ARFGEF3, RASGEF1B, RAPGEF1
  - [25]: GEF-mediated Rho GTPase activation in cell morphology and migration
  - [26]: Rho signaling in glial cell differentiation
- Rho GTPase inactivation by GAPs. Genes: ARHGAP5, ARHGAP31
  - [25]: GAP-mediated Rho GTPase inactivation
- Actomyosin dynamics and stress fiber formation. Genes: SHROOM4, ADD3, FRMD5, FRMD4B, FRMD4A
  - [25]: SHROOM proteins in controlling actomyosin contractility
  - [26]: Cytoskeletal dynamics in oligodendrocyte process extension
- Focal adhesion assembly and disassembly. Genes: FRMD5, FRMD4B, FRMD4A
  - [25]: FRMD proteins in focal adhesion dynamics

**Atomic cellular components**
- Rho GTPase regulatory complex. Genes: ARFGEF3, RASGEF1B, RAPGEF1, ARHGAP5, ARHGAP31
  - [25]: GEF and GAP proteins as Rho regulators
- Actomyosin contractile apparatus. Genes: SHROOM4, ADD3
  - [25]: SHROOM-mediated organization of actomyosin
- Focal adhesion complex. Genes: FRMD5, FRMD4B, FRMD4A
  - [25]: FRMD proteins as FAK-associated focal adhesion regulators

**Required genes (not in input)**
- Genes: RHOA, RAC1, CDC42, SRF
  - [25]: Core Rho GTPases and downstream transcriptional regulators

**Program citations**
- [25]: Comprehensive analysis of Rho GTPase signaling in CNS development and glial cell dynamics
- [26]: Rho signaling in oligodendrocyte differentiation and process extension

## Program: DOCK Family Cytoskeletal Remodeling
Specialized subset of GEFs specifically activating Rac1 and Cdc42 (but not RhoA) through direct catalytic mechanism distinct from Dbl-family GEFs. DOCK4, DOCK6, and DOCK10 collectively represent this program. DOCK family members are characterized by large catalytic domains and specific interactions with regulatory proteins and particular Rho family GTPases. Functionally, DOCK-mediated signaling tends to drive processes associated with cell migration, process extension, and exploratory morphology rather than contractile stress fiber formation. DOCK6 has been specifically implicated in oligodendrocyte process outgrowth and establishment of appropriate oligodendrocyte-axon spacing during myelinogenesis. Multiple DOCK members likely provide redundancy and allow fine-tuned regulation of Rac and Cdc42 in different cellular contexts.

**Predicted impacts**
- Preferential activation of lamellipodial and filopodial protrusion over stress fiber formation
- Enhanced oligodendrocyte process outgrowth and exploratory morphology
- Dynamic process extension along multiple axons
- Responsive adjustment of process branching and spacing
- Enhanced migratory and invasive capacity in transformed cells

**Evidence summary**
DOCK family proteins represent a specialized GEF subfamily that functions distinctly from the classical Dbl-family GEFs in producing a bias toward Rac1/Cdc42 activation rather than RhoA activation. This functional distinction has important consequences: RhoA activation promotes stress fiber formation and contractility, whereas Rac1/Cdc42 activation promotes lamellipodial and filopodial protrusion. In oligodendrocytes, DOCK-mediated Rac activation drives process outgrowth and the dynamic adjustment of process morphology needed for myelinating up to 50 axonal segments. DOCK proteins also function in immune cell migration, particularly in dendritic cells and lymphocytes, suggesting this program may interface with immune responses in the tumor microenvironment. In astrocytoma context, enhanced DOCK-mediated signaling would promote invasive migration of both tumor cells and potentially immune cells, while altered DOCK signaling in tumor-associated oligodendrocytes might contribute to their reduced myelinating capacity.

**Atomic biological processes**
- Rac1 and Cdc42 activation. Genes: DOCK4, DOCK6, DOCK10
  - [25]: DOCK family proteins as specific Rac/Cdc42 activators
  - [26]: Rac signaling in oligodendrocyte process dynamics
- Cell process extension and outgrowth. Genes: DOCK4, DOCK6
  - [25]: DOCK6 role in oligodendrocyte process extension
- Immune cell migration. Genes: DOCK10
  - [25]: DOCK10 function in immune cell migratory responses

**Atomic cellular components**
- DOCK GEF complex. Genes: DOCK4, DOCK6, DOCK10
  - [25]: DOCK family as specialized GEF subfamily

**Required genes (not in input)**
- Genes: ELMO1, ELMO2, ELMO3
  - [25]: ELMO proteins as regulatory partners of DOCK GEFs

**Program citations**
- [25]: DOCK6 and DOCK family proteins in cell morphology and process dynamics
- [26]: DOCK signaling in oligodendrocyte development

## Program: Phospholipase Signaling and Lipid Second Messengers
Coordinated phospholipid signaling system generating lipid second messengers that regulate calcium mobilization, kinase activation, and metabolic state. PLCB1 hydrolyzes PIP2 to generate IP3 and DAG, mobilizing calcium from intracellular stores and activating PKC. PLD1 catalyzes hydrolysis of phosphatidylcholine to generate phosphatidic acid, a lipid second messenger regulating mTOR signaling and metabolic processes. GNB4 and GNAI1 encode G protein components that activate PLCB1 downstream of G-protein-coupled receptors. PRKCE encodes PKC epsilon, a major effector of PLCB1-generated DAG. The kinase cascade initiated by phospholipase signaling includes multiple serine/threonine and tyrosine kinases that phosphorylate diverse substrates including ion channels, transcription factors, and structural proteins.

**Predicted impacts**
- Rapid calcium mobilization in response to extracellular signals
- PKC-mediated phosphorylation of downstream targets
- Integration of neurotransmitter and growth factor signals
- Metabolic reprogramming through phosphatidic acid-mTOR signaling
- Coupling of energy state to gene expression and cell proliferation

**Evidence summary**
Phospholipase signaling represents a central hub that integrates multiple extracellular signals into coordinated intracellular responses. GPCR activation of heterotrimeric G proteins leads to PLC-mediated generation of two lipid second messengers (IP3 and DAG) that activate complementary pathways: IP3 mobilizes calcium through ITPR2, while DAG activates PKC. Additionally, PLD1-mediated generation of phosphatidic acid serves as a direct activator of mTOR signaling and nutrient sensing. In oligodendrocytes, this signaling program allows responses to neurotransmitters, growth factors, and metabolic status. The presence of complete GPCR-G protein-PLCB1-PKC cascade components indicates robust capacity for signal integration. In astrocytoma context, enhanced phospholipase signaling contributes to the constitutive growth signaling and altered metabolic state characteristic of tumor cells.

**Atomic biological processes**
- GPCR-PLC-IP3 calcium signaling. Genes: GNAI1, GNB4, PLCB1, ITPR2
  - [25]: G protein-coupled receptor activation of phospholipase C
  - [16]: Calcium signaling downstream of activated astrocytes
  - [26]: Calcium mobilization in glial cell differentiation
- PKC-mediated protein phosphorylation. Genes: PRKCE
  - [25]: PKC epsilon downstream of DAG generation
- Phosphatidic acid-mTOR signaling. Genes: PLD1
  - [25]: PLD1-mediated phosphatidic acid generation in metabolic signaling

**Atomic cellular components**
- Phospholipase signaling complex. Genes: PLCB1, GNAI1, GNB4, PRKCE
  - [25]: PLCB1 and associated G proteins in signal transduction

**Required genes (not in input)**
- Genes: GPCR, GNA12, PRKCA, PRKCB
  - [25]: Broader G protein and PKC family members in phospholipase signaling

**Program citations**
- [25]: Phospholipase C and G protein signaling in nervous system development
- [16]: Calcium signaling in astrocyte responses

## Program: Ion Channel Regulation and Neuronal Excitability Interface
Coordinated expression of ion channels that regulate cellular excitability and calcium homeostasis in oligodendrocytes. KCNS3 encodes voltage-gated potassium channel that contributes to outward potassium currents and influences cellular excitability. P2RX7 encodes purinergic ATP-gated ion channel mediating calcium influx in response to extracellular ATP and functioning in innate immune signaling. GLRA3 encodes glycine receptor subunit mediating responses to glycine and inhibitory neurotransmission. ITPR2 encodes IP3 receptor mediating store-operated calcium release. These four genes collectively represent major routes for calcium entry into oligodendrocytes. Precise calcium homeostasis is critical for oligodendrocyte health and function, as both excessive and deficient calcium signaling can trigger apoptosis.

**Predicted impacts**
- Regulated cellular excitability through potassium efflux
- Calcium influx in response to extracellular ATP and immune signals
- Response to inhibitory neurotransmitters through glycine receptors
- Calcium homeostasis through store-operated and IP3-mediated release
- Integration of multiple excitatory and inhibitory signals

**Evidence summary**
Ion channels in oligodendrocytes provide multiple mechanisms for sensing the extracellular environment and regulating calcium homeostasis, which is critical for cell survival and function. Unlike neurons, oligodendrocytes have non-excitable membranes and do not generate action potentials, but they express diverse ion channels that regulate resting membrane potential and calcium signaling. The presence of multiple calcium entry routes (KCNS3-mediated depolarization allowing voltage-gated calcium entry, P2RX7-mediated ATP response, GLRA3 glycine response) indicates robust capacity for calcium mobilization in response to various signals. However, excessive or prolonged calcium elevation leads to calcium toxicity and cell death, making tight regulation of calcium crucial. In astrocytoma context, altered ion channel expression and calcium signaling in tumor-associated oligodendrocytes may contribute to their dysfunction, while simultaneously altered calcium signaling in tumor cells contributes to their transformed phenotype and responsiveness to growth factors.

**Atomic biological processes**
- Voltage-gated potassium channel function. Genes: KCNS3
  - [25]: Potassium channel expression in oligodendrocytes
  - [26]: Ion channel regulation of oligodendrocyte excitability
- Purinergic ATP signaling and calcium influx. Genes: P2RX7
  - [32]: P2RX7 role in complement-mediated cytotoxicity
- Glycine receptor signaling. Genes: GLRA3
  - [16]: Inhibitory neurotransmission and glial responses
  - [1]: Glycine receptor in neuronal-glial signaling
- IP3-mediated calcium release. Genes: ITPR2
  - [25]: ITPR2 in store-operated calcium signaling

**Atomic cellular components**
- Ion channel complex. Genes: KCNS3, P2RX7, GLRA3, ITPR2
  - [25]: Diverse ion channel types in oligodendrocytes

**Required genes (not in input)**
- Genes: CACNA1C, CACNB3, ATP2A2
  - [25]: Voltage-gated calcium channels and calcium-ATPases in calcium homeostasis

**Program citations**
- [25]: Ion channel expression and function in oligodendrocytes
- [32]: P2RX7 in complement-mediated immune responses
- [16]: Calcium signaling in glial cells

## Program: Protein Tyrosine and Serine/Threonine Kinase Signaling
Integrated signaling cascade integrating extracellular signals through tyrosine and serine/threonine phosphorylation of downstream targets. FYN encodes Src family tyrosine kinase mediating signaling downstream of RTKs and adhesion molecules with roles in axon-glial signaling and myelination. AATK encodes apoptosis-associated tyrosine kinase functioning in calcium-dependent signaling and neuronal differentiation. SGK1 encodes serum- and glucocorticoid-regulated kinase 1 phosphorylating ion channels and stress response substrates. PRKCE encodes PKC epsilon, serine/threonine kinase activated by DAG from phospholipase signaling. PPP2R2B encodes regulatory subunit of PP2A phosphatase, which dephosphorylates downstream targets and serves as major brake on kinase signaling. This coordinated kinase-phosphatase network dynamically phosphorylates numerous substrates controlling cell differentiation, migration, and metabolic state.

**Predicted impacts**
- Integration of receptor tyrosine kinase and adhesion signals
- Phosphorylation-based regulation of protein function and localization
- Stress-responsive kinase activation through SGK1
- Balanced kinase-phosphatase activity maintaining dynamic equilibrium
- Responsive adjustment of differentiation, migration, and metabolic state

**Evidence summary**
Protein phosphorylation represents one of the most extensively interconnected signaling networks in cells, with thousands of potential kinase-substrate pairs providing nearly unlimited specificity and dynamic regulation. FYN, as a Src family kinase, functions downstream of multiple receptor systems including RTKs, integrins, and immune receptors, making it a convergence point for multiple extracellular signals. SGK1 functions as a nutrient and stress sensor, being activated in response to serum, glucocorticoids, and osmotic stress, making it important for metabolic integration. The presence of PPP2R2B (PP2A regulatory subunit) indicates existence of a major phosphatase that can dephosphorylate and inactivate kinase signaling, establishing feedback control. In oligodendrocytes, this kinase-phosphatase program is essential for integrating differentiation signals during development and responding to injury and inflammatory signals in disease. In astrocytoma context, the kinase signaling landscape is dramatically altered, with many tumors showing constitutive activation of growth-promoting kinases.

**Atomic biological processes**
- Tyrosine kinase signaling. Genes: FYN, AATK
  - [13]: Tyrosine kinase signaling in glutamatergic neurons downstream of Eph receptors
  - [25]: FYN-mediated signaling in glial development
- Serine/threonine kinase signaling. Genes: PRKCE, SGK1
  - [25]: PKC and SGK signaling in glial cells
- Protein phosphatase 2A-mediated dephosphorylation. Genes: PPP2R2B
  - [16]: PP2A subunits in regulating phosphorylation cascades
  - [25]: PP2A-B subunits in phosphorylation control

**Atomic cellular components**
- Tyrosine kinase complex. Genes: FYN, AATK
  - [13]: Tyrosine kinase family members in signal transduction
- Serine/threonine kinase complex. Genes: PRKCE, SGK1
  - [25]: PKC family and related kinases in second messenger signaling
- Protein phosphatase 2A regulatory complex. Genes: PPP2R2B
  - [25]: PP2A as major serine/threonine phosphatase

**Required genes (not in input)**
- Genes: SRC, LYN, YES, PKA
  - [25]: Related tyrosine kinases and cAMP-dependent protein kinase in CNS signaling

**Program citations**
- [25]: Kinase signaling in glial cell development and function
- [13]: Tyrosine kinase signaling in neural physiology
- [16]: Phosphorylation cascades in astrocyte responses

## Program: Extracellular Matrix Organization and Remodeling
Coordinated production and modification of extracellular matrix components creating structural support and providing cell-matrix signaling interfaces. ACAN encodes aggrecan, large proteoglycan particularly abundant in perineuronal nets (PNNs) that regulate synaptic plasticity and stability. TNR encodes tenascin R, ECM glycoprotein contributing to PNN structural integrity and modulating neural plasticity. NTN1 encodes netrin-1, functioning as both axon guidance molecule and ECM-associated protein. SMOC1 encodes secreted modular calcium-binding protein, ECM component regulating cell-matrix interactions. ADAMTS14 encodes metallopeptidase cleaving ECM proteins during tissue remodeling. These ECM components are particularly enriched around neurons receiving strong inhibitory inputs and in regions of activity-dependent refinement. The ECM program collectively organizes perineuronal nets, glial scars, and tissue architecture.

**Predicted impacts**
- Organization of perineuronal nets surrounding stabilized neuronal populations
- Regulation of synaptic plasticity through ECM stabilization
- Structural support for glial-neuronal networks
- Controlled ECM remodeling during development and injury
- Cell-matrix signaling providing positional and developmental cues

**Evidence summary**
The extracellular matrix represents a dynamic tissue component that extends beyond simple structural support to provide complex signaling information and regulate cellular behavior. Perineuronal nets, specialized ECM structures surrounding certain neurons, have emerged as critical regulators of synaptic plasticity and critical periods of development. ACAN and TNR represent the core structural components of PNNs, which are particularly abundant around parvalbumin-positive inhibitory interneurons in cerebral cortex and other regions. The presence of netrin-1 (NTN1) indicates an integration of axon guidance signaling with ECM organization. In the tumor microenvironment, ECM organization is dramatically altered, with both excessive ECM deposition (leading to desmoplastic reactions) and degradation (creating permissive invasion conditions). The presence of ADAMTS14, a potent ECM protease, suggests capacity for matrix remodeling that could facilitate either tumor invasion or tissue repair depending on context.

**Atomic biological processes**
- Perineuronal net assembly and maintenance. Genes: ACAN, TNR, NTN1, SMOC1
  - [25]: Aggrecan and tenascin R in perineuronal net structure
  - [1]: ECM molecules in synaptic plasticity and stabilization
- ECM proteolysis and remodeling. Genes: ADAMTS14
  - [25]: ADAMTS metallopeptidases in ECM remodeling
- Axon guidance through ECM. Genes: NTN1
  - [25]: Netrin-1 as both ligand and ECM component

**Atomic cellular components**
- Perineuronal net structure. Genes: ACAN, TNR, NTN1, SMOC1
  - [25]: PNN composed of proteoglycans, glycoproteins, and ECM proteins
- ECM-modifying enzyme. Genes: ADAMTS14
  - [25]: ADAMTS proteases in ECM proteolysis

**Required genes (not in input)**
- Genes: BREVICAN, NEUROCAN, VERSICAN, LINK PROTEIN
  - [25]: Additional proteoglycans and link proteins in perineuronal net assembly

**Program citations**
- [25]: Comprehensive analysis of ECM organization in CNS development including perineuronal nets
- [1]: ECM in synaptic plasticity and neural circuit refinement

## Program: Autophagy, Protein Quality Control, and Cellular Stress Response
Coordinated system for selective protein degradation, damaged organelle removal, and cellular stress adaptation ensuring oligodendrocyte survival under normal and stress conditions. TFEB encodes transcription factor EB that regulates genes involved in lysosomal function, autophagy, and cellular stress responses, serving as master regulator of lysosomal biogenesis. TRIM2 and RNF144A encode ubiquitin ligases mediating selective ubiquitination of protein substrates targeting them for proteasomal or autophagy-mediated degradation. UST encodes ubiquitin-specific peptidase removing ubiquitin modifications from substrates. These autophagy and proteolysis genes ensure oligodendrocytes can respond to cellular stress by initiating protein degradation, removing damaged components, and restoring homeostasis. This program is particularly activated during oxidative stress, energy depletion, and inflammatory challenge characteristic of tumor microenvironment.

**Predicted impacts**
- Rapid clearance of misfolded or damaged proteins
- Removal of damaged mitochondria and organelles through mitophagy and autophagy
- Restoration of cellular homeostasis after oxidative or energetic stress
- Prevention of protein aggregation and cellular dysfunction
- Enhanced survival of oligodendrocytes in tumor microenvironment stress

**Evidence summary**
Protein quality control systems, including the ubiquitin-proteasome system and autophagy-lysosome system, are essential for cell survival during stress conditions. TFEB serves as a master regulator of these systems, being activated in response to stress signals and upregulating the genes encoding lysosomal enzymes and autophagy machinery. The presence of TFEB alongside TRIM2 and RNF144A (ubiquitin ligases) and UST (deubiquitinase) indicates a complete capacity for targeted protein degradation. In oligodendrocytes, which are particularly metabolically active cells due to continuous myelin synthesis and maintenance, these protein quality control systems are essential. In astrocytoma context, tumor cells often show altered autophagy, with both increased autophagy in some contexts (supporting cell survival under metabolic stress) and decreased autophagy in others, while simultaneously the tumor microenvironment stress (hypoxia, nutrient deprivation, inflammation) triggers autophagy in surrounding cells including oligodendrocytes. Enhanced autophagy in tumor-associated oligodendrocytes might represent attempted adaptation to stress but could also contribute to their progressive dysfunction and death.

**Atomic biological processes**
- Lysosomal biogenesis and autophagy initiation. Genes: TFEB
  - [25]: TFEB as master regulator of lysosomal genes
  - [16]: Lysosomal dysfunction in chronic TBI
- Selective protein ubiquitination for degradation. Genes: TRIM2, RNF144A
  - [25]: E3 ubiquitin ligases in selective protein degradation
- Deubiquitination and ubiquitin recycling. Genes: UST
  - [16]: Ubiquitin-specific peptidases in protein quality control

**Atomic cellular components**
- Ubiquitin proteasome system. Genes: TRIM2, RNF144A, UST
  - [25]: E3 ligases and ubiquitin cascade in protein degradation
- Lysosomal autophagy machinery. Genes: TFEB
  - [25]: Lysosomal biogenesis controlled by TFEB

**Required genes (not in input)**
- Genes: ATG7, ATG12, LC3, SQSTM1
  - [25]: Core autophagy machinery genes required for functional autophagy

**Program citations**
- [25]: Lysosomal biogenesis and autophagy in glial cell stress responses
- [16]: Autophagy and protein quality control in chronic pathological conditions

## Bibliography
1. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
2. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
3. Available from: https://www.ncbi.nlm.nih.gov/gene/18015
4. Available from: https://www.ncbi.nlm.nih.gov/gene/546
5. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
6. Dimitriou C, Anesti M, Kaplanis S, Mourtzi T, Dimopoulou A, Dimitrakopoulos D, et al.. Platelets regulate neural and oligodendroglial progenitors when infiltrating the brain parenchyma. Communications Biology [Internet]. 2025Nov24;8(1). Available from: https://www.nature.com/articles/s42003-025-09028-1
7. Available from: https://www.ncbi.nlm.nih.gov/gene/8502
8. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
9. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
10. Available from: https://www.ncbi.nlm.nih.gov/gene/5318
11. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=18508
12. Liu Y, Hu J-J, Cao B, Chen P, Peng B, Yao H, et al.. EphB1-NR2B receptor signaling in glutamatergic neurons of the ventroposteromedial thalamic nucleus regulates emergence from anesthesia. Science Advances [Internet]. 2025Dec5;11(49). Available from: https://www.science.org/doi/10.1126/sciadv.adw7972
13. Available from: https://www.ncbi.nlm.nih.gov/gene/121021
14. Available from: https://www.ncbi.nlm.nih.gov/gene/13641
15. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
16. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
17. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
18. Available from: https://www.ncbi.nlm.nih.gov/gene/2260
19. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
20. Available from: https://www.ncbi.nlm.nih.gov/gene/4804
21. Jiang R, Lu Z, Li F, Zhu Y, Yang M, Zhang S, et al.. scCirclehunter delineates ecDNA-containing cells using single-cell ATAC-seq, with a focus on glioblastoma. Cell Discovery [Internet]. 2025Dec9;11(1). Available from: https://www.nature.com/articles/s41421-025-00842-9
22. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
23. Zhang J, Li M, Wang M, Sun Y, Yin C, Yang S, et al.. Single-cell spatiotemporal transcriptomic and chromatin accessibility profiling in developing postnatal human and macaque prefrontal cortex. Nature Neuroscience [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41593-025-02150-7
24. Available from: https://www.ncbi.nlm.nih.gov/gene/21898
25. Available from: https://www.ncbi.nlm.nih.gov/gene/12053
26. Available from: https://www.ncbi.nlm.nih.gov/gene/18033
27. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
28. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
29. Available from: https://www.ncbi.nlm.nih.gov/gene/6622
30. Available from: https://www.ncbi.nlm.nih.gov/gene/5894
31. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
32. Available from: http://json-schema.org/draft-07/schema#",
