# Gene Program Markdown Report

## Context
- Cell type: astrocytes, neural stem cells, neurons (peritumoral)
- Disease: astrocytoma (WHO grade II-IV)
- Tissue: brain, cerebral cortex, white matter tracts

## Input Genes
UNC5D, DAB1, RGS7, ANK3, GRM7, MEG8, LRRC7, SNHG14, GRM5, MEG3, KCNQ3, NRG3, RBFOX1, PPFIA2, GRIN2B, CACNA1C, ATP8A2, PLPPR4, GABRB1, ANKS1B, KCNC2, TENM2, AL024495.1, KIRREL3, CACNA1E, ... (200 total)

## Program: Glutamatergic Synaptic Transmission and Plasticity
Ionotropic and metabotropic glutamate receptor-mediated excitatory synaptic transmission and long-term potentiation/depression. Comprises NMDA receptor subunits (GRIN1, GRIN2A, GRIN2B), AMPA receptor subunits (GRIA1), metabotropic glutamate receptors (GRM5, GRM7), and associated scaffolding and signaling machinery including calcium-calmodulin-dependent protein kinases (CAMK2A, CAMK2B), presynaptic vesicle machinery (SYT1, SYT14, RIMS1, RIMS2), and postsynaptic density proteins (DLG2, GRIP1, GRIP2). In glioblastoma and astrocytoma, peritumoral neurons exhibit enhanced glutamatergic signaling with increased dendritic spine density and elevated synaptic inputs, leading to increased neuronal excitability and seizure susceptibility.

**Predicted impacts**
- Enhanced glutamatergic signaling and synaptic transmission
- Increased dendritic spine density in peritumoral neurons
- Elevated neuronal excitability and reduced seizure threshold
- Dysregulated calcium homeostasis in glioma-adjacent neurons
- Enhanced long-term potentiation in circuits containing glioma

**Evidence summary**
Multiple genes in this program show altered expression in peritumoral cortex adjacent to glioblastoma, with computational models demonstrating that modest increases in glutamatergic synaptic inputs double spike output rates and substantially increase seizure susceptibility. Paroxysmal depolarizing shifts characteristic of pre-ictal activity are detected prior to clinical seizure onset in a subset of glioma patients, correlating with upregulated glutamatergic signaling markers. This program represents a core mechanism through which glioma growth induces circuit hyperexcitability and seizure pathogenesis.

**Atomic biological processes**
- NMDA receptor-mediated calcium influx and signaling. Genes: GRIN1, GRIN2A, GRIN2B
  - [39]: GRIN1 and GRIN2A encode critical NMDA receptor subunits mediating calcium-dependent synaptic plasticity
  - [41]: GRIN1 encodes NMDA receptor subunit 1, a critical component of glutamate receptor channels
  - [26]: NMDA receptor dysfunction contributes to altered dendritic structure in tumor-adjacent neurons
- Activity-dependent synaptic strengthening through AMPA receptor trafficking. Genes: GRIA1
  - [26]: GRIA1-containing AMPA receptors show activity-dependent trafficking in peritumoral neurons
- Metabotropic glutamate receptor signaling. Genes: GRM5, GRM7
  - [7]: GRM5 and GRM7 couple to G-protein signaling modulating synaptic strength and plasticity
- Calcium-dependent kinase signaling. Genes: CAMK2A, CAMK2B
  - [40]: CAMK2B (calcium/calmodulin-dependent protein kinase II) regulates neuron migration and synaptic plasticity
  - [42]: CAMK2A autophosphorylation regulates synaptic plasticity and memory formation
- Presynaptic vesicle release and active zone organization. Genes: SYT1, SYT14, RIMS1, RIMS2
  - [7]: SYT1 and associated proteins regulate synaptic vesicle fusion and neurotransmitter release
  - [16]: RIMS proteins organize the presynaptic active zone and control readily releasable pool

**Atomic cellular components**
- Postsynaptic density organization at glutamatergic synapses. Genes: DLG2, GRIP1, GRIP2
  - [26]: DLG2 and GRIP proteins organize postsynaptic glutamate receptors and signaling complexes

**Required genes (not in input)**
- Genes: PSD95, SHANK3, Homer proteins, mGluR signaling effectors
  - [16]: PSD-95 family proteins and Homer organize postsynaptic density

**Program citations**
- [26]: Comprehensive characterization of aberrant neural activity in peritumoral cortex with computational modeling
- [33]: Glioma-induced glutamate elevation and altered neuronal excitability
- [39]: NMDA receptor disease-associated variants and functional roles
- [41]: GRIN1 as critical NMDA receptor component
- [7]: Glutamate receptor signaling and synaptic plasticity mechanisms

## Program: GABAergic Inhibitory Synaptic Transmission
Fast inhibitory GABAergic synaptic transmission mediated by ionotropic GABA-A receptors and slower inhibition through metabotropic GABA-B receptors. GABA-A receptor subunits (GABRA2, GABRB1, GABRG2) form chloride channels mediating fast inhibition, while GABBR2 (metabotropic GABA-B receptor) couples to G-protein pathways. This program maintains excitatory-inhibitory balance in neural circuits. In astrocytoma, dysfunction of GABAergic inhibition contributes to hyperexcitability and seizure susceptibility through reduced inhibitory tone and altered interneuron function.

**Predicted impacts**
- Reduced inhibitory synaptic transmission in peritumoral cortex
- Impaired excitatory-inhibitory balance leading to circuit hyperexcitability
- Increased seizure susceptibility through loss of inhibitory tone
- Dysfunction of interneuron-mediated circuit regulation
- Enhanced vulnerability to glutamate-induced excitotoxicity

**Evidence summary**
GABAergic inhibition is compromised in the peritumoral region of glioblastomas, with reduced GABA reuptake by astrocytes and impaired interneuron function contributing to the shift toward hyperexcitability. Inflammatory mediators in the tumor microenvironment preferentially affect GABAergic neurons, further disrupting the balance. The presence of spike-wave discharges and high gamma-band activity in glioma-bearing animals indicates synchronous firing consistent with reduced inhibition.

**Atomic biological processes**
- Ionotropic GABA-A receptor-mediated fast inhibition. Genes: GABRA2, GABRB1, GABRG2
  - [33]: Reduced GABAergic inhibition contributes to peritumoral neuronal hyperexcitability
- Metabotropic GABA-B receptor signaling and presynaptic inhibition. Genes: GABBR2
  - [49]: GABBR2 metabotropic signaling provides presynaptic inhibition and homeostatic regulation

**Required genes (not in input)**
- Genes: GAD65, GAD67, VGAT, GABA transporter 1
  - [33]: GABAergic machinery essential for inhibitory transmission

**Program citations**
- [33]: GABAergic dysfunction in peritumoral cortex
- [26]: Excitatory-inhibitory imbalance in tumor-associated seizures
- [49]: GABBR2 and GABAergic signaling in neurological function

## Program: Voltage-Gated Ion Channels and Neuronal Excitability Control
L-type and non-L-type voltage-gated calcium channels (CACNA1C, CACNA1D, CACNA1E) and potassium channels (KCNQ3, KCNC2, KCNJ3, KCNMA1, KCNMB2) that determine neuronal resting potential, action potential generation, and intrinsic excitability. CACNA1C is a pleiotropic psychiatric disease gene affecting neural circuit development. Potassium channels provide repolarizing conductances that regulate frequency-dependent firing and suppress neuronal hyperexcitability. In glioma-adjacent neurons, dysregulation of this program shifts excitability toward pathological states, particularly through altered M-channel (KCNQ) and BK-channel (KCNMA1/KCNMB2) function.

**Predicted impacts**
- Increased intrinsic neuronal excitability in peritumoral neurons
- Enhanced voltage deflections in soma in response to dendritic inputs
- Reduced threshold for action potential generation
- Impaired frequency-dependent regulation of firing
- Greater susceptibility to paroxysmal depolarizing shifts and seizures

**Evidence summary**
Peritumoral neurons show increased firing frequency slopes and enhanced intrinsic excitability during tumor progression. Computational modeling demonstrates that even modest changes in dendritic spine density, as observed in tumor-adjacent tissue, substantially increase the voltage deflection at the soma through enhanced synaptic conductance, effectively lowering the action potential threshold. Early tumor growth (14 days post-injection) shows transient elevation of intrinsic excitability preceding clinical seizure manifestation, suggesting dysregulation of voltage-gated channel function as an early biomarker.

**Atomic biological processes**
- L-type calcium channel-mediated calcium signaling. Genes: CACNA1C
  - [9]: CACNA1C genetic variation associated with brainstem volume and circuit development
  - [12]: Cacna1c deletion impairs hippocampal neurogenesis and behavioral outcomes
- M-channel (KCNQ) suppression of neuronal excitability. Genes: KCNQ3
  - [9]: KCNQ3 mutations associated with neonatal epilepsy and hyperexcitability
- Fast-spiking interneuron potassium conductance. Genes: KCNC2
  - [49]: KCNC2 encodes Kv3-family potassium channel in fast-spiking neurons
- BK calcium-activated potassium channel feedback inhibition. Genes: KCNMA1, KCNMB2
  - [26]: Calcium-activated potassium channels provide rapid feedback to stabilize firing frequency

**Required genes (not in input)**
- Genes: KCNE auxiliary subunits, Kv7-associated regulatory proteins
  - [9]: Ion channel auxiliary subunits regulate voltage-gated channel function

**Program citations**
- [26]: Computational modeling of intrinsic excitability changes in tumor-adjacent neurons
- [9]: CACNA1C as pleiotropic psychiatric disease gene
- [12]: Cacna1c effects on hippocampal neurogenesis and behavior

## Program: Axon Guidance and Neuronal Migration Control
Secreted and membrane-bound guidance cues (SEMA3C, netrin ligands), their receptors (ROBO1, ROBO2, DCC, UNC5D), and cell adhesion molecules (CHL1, CNTNAP2, CNTN5, SEZ6L, SEZ6L2) that direct axonal projections and neuronal migration during development. SEMA3C binds plexin receptors to repel axons, while ROBO1/2 bind Slit ligands for repulsive guidance. DCC and UNC5D function as netrin receptors for attractive or repulsive guidance depending on co-receptor context. In astrocytoma, glioma cells exploit this guidance landscape to migrate along white matter tracts and infiltrate surrounding tissue directionally. Patient-derived glioblastoma cell lines migrate along axons toward neural spheroids in vitro.

**Predicted impacts**
- Altered guidance of glioma cell migration along white matter tracts
- Enhanced infiltrative behavior through co-option of axon guidance landscape
- Directional migration of tumor cells toward neural target tissue
- Disruption of normal axon-axon contacts and circuit organization
- Altered peritumoral axonal integrity and network connectivity

**Evidence summary**
Patient-derived glioblastoma cell lines migrate directionally along axons toward neural spheroids in live imaging assays, demonstrating that tumor cells actively exploit axon guidance mechanisms during infiltration. The expression of axon guidance receptors in glioma cells and the altered expression of guidance ligands in the tumor microenvironment suggest active remodeling of this program during tumorigenesis. Genetic studies in other cancers show that loss of repulsive guidance through SLIT-ROBO pathway disruption promotes migration, implicating this pathway in astrocytoma infiltration.

**Atomic biological processes**
- Semaphorin-plexin-mediated repulsive axon guidance. Genes: SEMA3C, PLXNA2, PLXNA4
  - [22]: SEMA3F semaphorin family members mediate repulsive axon guidance during neuronal development
- Slit-roundabout repulsive guidance signaling. Genes: ROBO1, ROBO2
  - [31]: ROBO1 roundabout receptor mediates Slit-dependent repulsive axon guidance
  - [29]: ROBO2 encodes roundabout guidance receptor for axon guidance and migration
- Netrin-attractive and repulsive guidance signaling. Genes: DCC, UNC5D
  - [31]: DCC and UNC5 function as netrin receptors with context-dependent guidance effects
- Cell adhesion molecule-mediated axon-axon fasciculation and stabilization. Genes: CNTNAP2, CNTN5, SEZ6L, SEZ6L2, CHL1
  - [37]: L1CAM plays role in nervous system development including neuronal migration and differentiation
  - [14]: CNTNAP2 contactin-associated protein plays essential role in neural development

**Required genes (not in input)**
- Genes: Netrin-1, Slit ligands, Plexin-B receptors, Neuropilin co-receptors
  - [31]: Netrin and Slit ligands required for receptor-mediated guidance

**Program citations**
- [27]: Glioblastoma cell migration directionally along axons toward neural spheroids
- [31]: Slit-Robo signaling inhibition promotes cancer cell migration
- [29]: ROBO2 function in axon guidance and cell migration
- [37]: L1CAM role in nervous system development and potential in glioma

## Program: Postsynaptic Scaffolding and Synaptic Organization
Postsynaptic density (PSD) scaffolding proteins including membrane-associated guanylate kinases (DLG2), ankyrin repeat proteins (ANKS1B), MAGUK family members (MAGI3), and synapse-organizing proteins (LRRTM4, SHANK2) that organize the dense proteinaceous matrix underlying the postsynaptic membrane. These proteins coordinate positioning and stabilization of neurotransmitter receptors, signaling enzymes, and trans-synaptic adhesion molecules. DLG2 anchors NMDA receptors and scaffolds signaling complexes. LRRTM4 functions as postsynaptic cell adhesion molecule interacting with presynaptic neurexins. In glioma-adjacent neurons, increased dendritic spine density requires coordinated assembly of new postsynaptic densities.

**Predicted impacts**
- Enhanced postsynaptic density assembly at new dendritic spines
- Increased synaptic strength through receptor organization and clustering
- Altered dendritic spine stability and morphology
- Dysregulated synaptic plasticity signaling
- Potential links between synaptic organization and tumor cell proliferation

**Evidence summary**
Glioma-adjacent neurons exhibit increased dendritic spine density, which requires corresponding assembly of new postsynaptic densities. Recent studies using advanced imaging reveal altered postsynaptic nanostructure in models of neurodevelopmental disorders featuring synaptic dysfunction. The scaffolding proteins DLG2 and related MAGUKs regulate both synaptic function and cell proliferation, suggesting functional links between aberrant synaptic organization and tumor-cell proliferation signals in low-grade gliomas.

**Atomic biological processes**
- PSD-93-mediated NMDA receptor anchoring and signaling complex organization. Genes: DLG2
  - [16]: DLG2 (PSD-93) anchors NMDA receptors and organizes postsynaptic signaling complexes
- Ankyrin repeat protein-based postsynaptic organization. Genes: ANKS1B
  - [16]: ANKS1B localizes to dendritic spines and interacts with postsynaptic proteins
- Trans-synaptic adhesion through neurexin-ligand interactions. Genes: LRRTM4, SHANK2
  - [14]: CNTNAP2 member of neurexin superfamily plays essential role in neural development

**Required genes (not in input)**
- Genes: PSD-95, SAP102, Homer proteins, GKAP/SAPAP
  - [16]: PSD-95 family and Homer proteins organize postsynaptic density

**Program citations**
- [16]: Postsynaptic scaffolding proteins in synaptic organization and nanostructure
- [26]: Increased dendritic spine density in tumor-adjacent neurons
- [14]: CNTNAP2 in neural development and organization

## Program: RNA Splicing Regulation and Neuronal Differentiation
Splicing regulators (SRRM4, RBFOX1, CELF4) controlling alternative splicing patterns critical for neuronal development and plasticity. SRRM4 promotes inclusion of neuron-specific exons and drives differentiation toward neuronal fate. RBFOX1 regulates alternative splicing of neuronal genes including those involved in stress response and BDNF/TRKB signaling, with loss of function leading to disrupted stress response mechanisms. CELF4 regulates alternative splicing particularly during neuronal development. Coordinated developmental changes in splicing factor expression drive transitions from embryonic to adult isoforms. In astrocytoma, dysregulation of splicing programs may alter balance between pro-survival and pro-death isoforms.

**Predicted impacts**
- Aberrant production of embryonic isoforms in tumor cells and peritumoral neurons
- Disrupted balance between pro-survival and pro-death protein isoforms
- Altered stress response through dysregulated BDNF/TRKB signaling
- Enhanced tumor cell plasticity through retention of developmental isoforms
- Dysregulated ion channel and receptor isoform composition

**Evidence summary**
Low-grade astrocytomas maintain expression of neural stem cell-associated genes and exhibit incomplete differentiation, suggesting disrupted developmental splicing programs. Developmental changes in splicing factor expression are essential for progression from embryonic to adult neural states. INSM1 drives intermediate progenitor identity in glioblastoma cells and is essential for tumorigenicity, suggesting reactivation of developmental transcriptional networks including those controlling splicing. Dysregulation of RBFOX1-controlled splicing of stress response genes could influence both tumor cell and peritumoral neuron responses to microenvironmental stress.

**Atomic biological processes**
- SRRM4-mediated neuronal differentiation through neuron-specific splicing. Genes: SRRM4
  - [35]: SRRM4 neuronal-specific splicing regulator promotes neuron-specific exon inclusion during differentiation
- RBFOX1-controlled stress response splicing. Genes: RBFOX1
  - [8]: RBFOX1 loss of function disrupts BDNF/TRKB and CRH signaling leading to altered stress response
  - [11]: RBFOX1 regulates RNA splicing and transcriptional networks in human neuronal development
- CELF4-mediated splicing during neuronal development. Genes: CELF4
  - [35]: CELF4 CUGBP family splicing factor regulates alternative splicing during brain development
- Developmental regulation of splicing factors through poison exon inclusion. Genes: SRRM4, RBFOX1
  - [35]: UCR-associated poison exons trigger nonsense-mediated decay of splicing factor transcripts

**Required genes (not in input)**
- Genes: SRSF1, SRSF6, hnRNP family members, Spliceosome components
  - [35]: SR and hnRNP splicing factor families regulate developmental alternative splicing

**Program citations**
- [35]: Ultraconserved regions regulate splicing factor expression and developmental alternative splicing programs
- [8]: RBFOX1 regulates stress response mechanisms through BDNF/TRKB signaling
- [3]: INSM1 drives intermediate progenitor state essential for glioblastoma tumorigenicity

## Program: Cytoskeletal Dynamics and Dendritic Morphology
Cytoskeletal regulators (ANK3, ABLIM2, VAV3, DYNC1I1, SPTBN4, PAK5) controlling actin polymerization, microtubule dynamics, and cell morphology. ANK3 links membrane proteins to spectrin-actin cytoskeleton. ABLIM2 modulates actin organization influencing dendritic morphology. VAV3 is Rho GTPase exchange factor regulating Rac1 activity and actin polymerization. DYNC1I1 transports vesicles along microtubules. SPTBN4 provides structural support for neuronal cytoskeleton. PAK5 functions downstream of Rho GTPases to regulate dendritic spine morphology through phosphorylation of LIMK and cofilin. In astrocytoma, enhanced dendritic spine density requires active cytoskeletal remodeling, and glioma cell migration requires extensive cytoskeletal remodeling.

**Predicted impacts**
- Enhanced dendritic spine formation and remodeling in tumor-adjacent neurons
- Increased glioma cell motility and infiltration through cytoskeletal remodeling
- Mesenchymal transformation of tumor cells promoting migration
- Altered dendritic and axonal morphology in peritumoral tissue
- Dysregulated intracellular trafficking and organelle positioning

**Evidence summary**
Glioma-adjacent neurons exhibit dramatically increased dendritic spine density, fundamentally dependent on coordinated actin polymerization and microtubule dynamics. Loss of pericytes in the glioma microenvironment leads to mesenchymal transformation of tumor cells involving upregulation of PAK and Rho GTPase signaling. Aberrant activation of these pathways promotes a motile phenotype compatible with enhanced infiltration. The intersection of cytoskeletal dynamics with oncogenic signaling pathways suggests links between structural remodeling and tumor cell proliferation.

**Atomic biological processes**
- Ankyrin-spectrin-actin linkage and cell morphology. Genes: ANK3, SPTBN4
  - [13]: ANK3 ankyrin-3 links integral membrane proteins to spectrin-actin cytoskeleton
- Actin polymerization and dendritic spine morphogenesis. Genes: ABLIM2, VAV3, PAK5
  - [21]: CDC42 and Rho GTPases regulate actin polymerization and dendritic spine dynamics
- Microtubule-based intracellular transport. Genes: DYNC1I1
  - [26]: Dynein heavy chain involved in intracellular vesicle transport
- Rho GTPase-effector signaling in migration and morphology. Genes: VAV3, PAK5
  - [6]: Loss of pericytes promotes mesenchymal transformation involving altered cytoskeletal organization
  - [52]: Mesenchymal glioma cell state characterized by Wnt and PAK signaling pathway activation

**Required genes (not in input)**
- Genes: Cofilin, LIMK, Profilin, Arp2/3 complex
  - [21]: Actin regulatory proteins downstream of PAK and Rho GTPases

**Program citations**
- [26]: Dendritic spine morphology alterations in tumor-adjacent neurons
- [6]: Pericyte loss drives mesenchymal transformation in glioblastoma
- [52]: Mesenchymal tumor cells interact with immune cells to drive invasive phenotype

## Program: Extracellular Matrix Interactions and Cell Adhesion
Extracellular matrix (ECM) proteins (FRAS1, EDIL3, NELL1) and cell adhesion molecules (TENM2, FAM155A, NTM, CHL1) mediating cell-ECM and cell-cell interactions. FRAS1 encodes ECM component important for tissue adhesion and structural organization. EDIL3 encodes EGF-like and discoidin domains involved in cell-cell interactions and vascular development. NELL1 upregulated during bone cell differentiation with emerging roles in neuronal development. TENM2 functions as trans-synaptic adhesion molecule and circuit regulator. FAM155A involved in developmental cell-cell interactions. NTM (neurotrimin) involved in cell-cell interactions regulating neuronal migration. These molecules establish cellular scaffold organizing tissue architecture and specifying cell-cell contacts.

**Predicted impacts**
- Spatial organization of ECM in distinct tumor microenvironmental niches
- Altered peritumoral neuron-ECM interactions affecting synaptic stability
- Enhanced glioma cell-stromal cell interactions through dysregulated ECM
- Disruption of normal tissue architecture in peritumoral zone
- Remodeling of extracellular space promoting tumor infiltration

**Evidence summary**
Spatial transcriptomic profiling reveals that ECM signaling pathways are extensively dysregulated in glioblastoma, with different GBM cell populations and stromal cell types showing largely non-overlapping ECM expression patterns. Vascular endothelial cells and immune cells in the perivascular niche express distinct ECM signatures supporting their specialized functions. The spatial organization of ECM components reflects the complex microarchitecture of glioblastomas where distinct cellular niches express different ECM components. Altered ECM composition disrupts perisynaptic matrix structure, contributing to synaptic reorganization in tumor-adjacent neurons.

**Atomic biological processes**
- ECM structural organization and tissue adhesion. Genes: FRAS1, EDIL3, NELL1
  - [24]: ECM components dysregulated in glioblastoma compared to normal brain
  - [55]: Single-cell spatial profiling maps expression of nearly 400 ECM genes in GBM
- Cell-cell recognition and trans-synaptic adhesion. Genes: TENM2, FAM155A, NTM, CHL1
  - [55]: Novel ECM ligand-receptor networks between GBM and stromal cells
- Perivascular niche ECM organization. Genes: FRAS1, EDIL3
  - [6]: Perivascular niche characterized by specific ECM signatures and cellular organization

**Required genes (not in input)**
- Genes: Fibronectin, Laminin, Perlecan, Versican
  - [55]: Major ECM components dysregulated in glioblastoma

**Program citations**
- [24]: ECM ligand-receptor networks in glioblastoma perivascular niche
- [55]: Spatial profiling of matrisome identifies cell-specific ECM expression in GBM
- [6]: Perivascular niche organization in glioblastoma

## Program: Neurotrophic Signaling and Growth Factor Cascades
Receptor tyrosine kinases and growth factor signaling mediating survival, plasticity, and circuit development. ERBB4 encodes ErbB-4 receptor tyrosine kinase binding neuregulin ligands, particularly in parvalbumin-positive GABAergic interneurons. NRG1 and NRG3 encode neuregulin growth factors important for myelination, axon-glia interactions, and synaptic plasticity. RBFOX1-regulated BDNF/TRKB signaling controls stress response mechanisms. These pathways activate PI3K and MAPK cascades. In astrocytoma, dysregulated neurotrophic signaling promotes survival of tumor-supporting immune cells, drives tumor cell proliferation, and alters neurotrophic factor availability for peritumoral neurons.

**Predicted impacts**
- Altered interneuron survival and functional integration in peritumoral tissue
- Enhanced alternatively activated macrophage polarization in tumor microenvironment
- Disrupted neurotrophic support for peritumoral neurons
- Tumor cell proliferation through aberrant neurotrophic receptor activation
- Enhanced immune cell recruitment and polarization toward tumor-supportive states

**Evidence summary**
NRG1-ERBB4 signaling regulates conversion between microglial activation states, promoting anti-inflammatory M2 phenotype through inhibition of NF-kappaB pathway. In the tumor microenvironment, dysregulation of neurotrophic signaling contributes to skewing of immune cells toward tumor-supporting phenotypes. Pediatric high-grade gliomas show NTRK fusion events with constitutively active neurotrophic receptor signaling driving oncogenic transformation. Altered neurotrophic factor signaling in peritumoral zones affects local neuronal survival and plasticity.

**Atomic biological processes**
- ERBB4 receptor tyrosine kinase signaling in interneuron development. Genes: ERBB4
  - [17]: ERBB4 expressed in parvalbumin-positive interneurons, regulates conversion between microglial activation states
- Neuregulin ligand signaling through ErbB receptors. Genes: NRG1, NRG3, ERBB4
  - [19]: NRG1 neuregulin family member enables ErbB-2 class receptor binding
  - [17]: Neuregulin-1 regulates microglial phenotype via ErbB4
- BDNF/TRKB signaling in stress response and neuroprotection. Genes: RBFOX1
  - [8]: RBFOX1 regulates BDNF/TRKB signaling affecting stress response and psychiatric health

**Required genes (not in input)**
- Genes: BDNF, TRKB, ErbB2/HER2, ErbB3
  - [8]: BDNF and TRKB as key components of neurotrophic signaling

**Program citations**
- [17]: ERBB4-NRG1 signaling in microglial phenotype regulation
- [8]: RBFOX1 and BDNF/TRKB signaling in stress response mechanisms
- [43]: NTRK fusion events in pediatric high-grade gliomas

## Program: Developmental Transcriptional Regulation and Neural Identity
Transcriptional control of neuronal and glial identity specification and differentiation state maintenance. While input gene list contains few direct transcription factors, splicing regulators (RBFOX1, SRRM4) and their targets provide indirect transcriptional effects. Recent research reveals that INSM1 transcription factor drives intermediate progenitor cell-like state in glioblastoma, governs plasticity and tumorigenicity. This program reflects reactivation of developmental transcriptional networks in malignant gliomas. Low-grade astrocytomas maintain higher expression of neural stem cell markers, suggesting incomplete execution of differentiation programs. High-grade astrocytomas show mixed glial-neuronal marker expression indicating profound dysregulation of transcriptional identity programs.

**Predicted impacts**
- Reactivation of developmental neuronal differentiation programs in glial tumors
- Maintenance of neural stem cell-like state preventing terminal differentiation
- Mixed or failed glial-neuronal lineage specification
- Enhanced cellular plasticity and adaptability to therapeutic pressure
- Expression of developmental isoforms of ion channels and receptors

**Evidence summary**
Glioblastomas exhibit reactivation of developmental transcriptional networks, particularly those governing intermediate progenitor cell identity through INSM1. INSM1 is highly expressed in human glioblastoma tumors and, during normal cortical development, specifically in intermediate progenitor cells that give rise to neurons. INSM1 knockdown disrupts oncogenic gene expression and reduces tumorigenicity, highlighting functional importance of this developmental state. Low-grade astrocytomas maintain higher expression of neural stem cell markers and show incomplete oligodendroglial differentiation, suggesting that developmental programs remain partially active or terminal differentiation is blocked.

**Atomic biological processes**
- INSM1-driven intermediate progenitor cell identity in glioblastoma.
  - [3]: INSM1 governs intermediate progenitor state that drives glioblastoma tumorigenicity and plasticity
- Splicing factor control of developmental transcriptional programs. Genes: SRRM4, RBFOX1
  - [35]: Developmental splicing program changes coordinate with brain maturation
- Dysregulated neuronal vs glial lineage specification.
  - [3]: Triple mutant neural stem cells express intermediate progenitor markers and tumorigenicity

**Required genes (not in input)**
- Genes: INSM1, SOX2, Tbr2, NeuroD family, REST
  - [3]: Core transcriptional regulators of neural differentiation programs

**Program citations**
- [3]: INSM1 governs intermediate progenitor state essential for glioblastoma pathogenesis
- [35]: Developmental regulation of splicing programs controlling neuronal differentiation

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/546
2. Available from: https://www.ncbi.nlm.nih.gov/gene/5727
3. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
4. Available from: https://www.ncbi.nlm.nih.gov/gene/23627
5. Available from: https://www.ncbi.nlm.nih.gov/gene/4763
6. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
7. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
8. Leggieri A, García-González J, Hosseinian S, Ashdown P, Anagianni S, Wang X, et al.. rbfox1 LoF mutants show disrupted bdnf/trkb2 and crhb/nr3c2 expression and increased cortisol levels during development coupled with signs of allostatic overload in adulthood. Translational Psychiatry [Internet]. 2025Nov19;15(1). Available from: https://www.nature.com/articles/s41398-025-03703-x
9. Available from: https://www.ncbi.nlm.nih.gov/gene/775
10. Available from: https://www.ncbi.nlm.nih.gov/gene/85461
11. Available from: https://www.ncbi.nlm.nih.gov/gene/54715
12. Available from: https://www.ncbi.nlm.nih.gov/gene/12288
13. Available from: https://www.ncbi.nlm.nih.gov/gene/287
14. Available from: https://www.ncbi.nlm.nih.gov/gene/26047
15. Available from: https://www.ncbi.nlm.nih.gov/gene/6900
16. Yuan Y, Li Y, Yang F, Jiang Y, Ding Y, Xiao Y, et al.. Sh3rf3 Deficiency drives autism-like behaviors via presynaptic dysfunction in mice. Molecular Psychiatry [Internet]. 2025Nov25;. Available from: https://www.nature.com/articles/s41380-025-03370-w
17. Available from: https://www.ncbi.nlm.nih.gov/gene/2066
18. Hsu T-T, Chen C-P, Lin M-H, Hung T-E, Haung T-N, Wang C-Y, et al.. Shared and divergent alteration of whole-brain connectivity and sensory deficits in multiple autism mouse models. Molecular Psychiatry [Internet]. 2025Nov20;. Available from: https://www.nature.com/articles/s41380-025-03340-2
19. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
20. Available from: https://www.ncbi.nlm.nih.gov/gene/20346
21. Available from: https://www.ncbi.nlm.nih.gov/gene/998
22. Available from: https://www.ncbi.nlm.nih.gov/gene/6405
23. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
24. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
25. Available from: https://www.ncbi.nlm.nih.gov/gene/3265
26. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
27. Tsang VSK, Riccio F, Wilson AS, Nudds H, Coombes JD, Wurdak H, et al.. A human iPSC-based neural spheroid platform for modelling glioblastoma infiltration using high-content imaging. Scientific Reports [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41598-025-30914-5
28. Available from: https://www.ncbi.nlm.nih.gov/gene/10419
29. Available from: https://www.ncbi.nlm.nih.gov/gene/6092
30. Available from: https://www.ncbi.nlm.nih.gov/gene/4830
31. Available from: https://www.ncbi.nlm.nih.gov/gene/6091
32. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
33. Available from: https://www.ncbi.nlm.nih.gov/gene/4072
34. Bai Y, Zhang X, Wang X, Wang M, Shen T. Characterizing and decoding ultraconserved regions uncovers their regulatory significance in human brain development and disorders. Communications Biology [Internet]. 2025Nov27;8(1). Available from: https://www.nature.com/articles/s42003-025-09115-3
35. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
36. Available from: https://www.ncbi.nlm.nih.gov/gene/3897
37. Available from: https://www.ncbi.nlm.nih.gov/gene/5978
38. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=2903
39. Available from: https://www.ncbi.nlm.nih.gov/gene/12323
40. Available from: https://www.ncbi.nlm.nih.gov/gene/2902
41. Available from: https://www.ncbi.nlm.nih.gov/gene/12322
42. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
43. Yenisehirli G, Borges S, Braun SS, Zuniga AN, Quintana GI, Kutsnetsoff JN, et al.. Identification of targetable epigenetic vulnerabilities for uveal melanoma. Cell Death &amp; Disease [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41419-025-08295-4
44. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
45. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
46. Available from: https://www.ncbi.nlm.nih.gov/gene/9734
47. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
48. Available from: https://www.ncbi.nlm.nih.gov/gene/20358
49. Gundermann DG, Lymer S, Lennon J, Blau J. A rapid and dynamic role for FMRP in the plasticity of adult neurons. Nature Communications [Internet]. 2025Nov23;. Available from: https://www.nature.com/articles/s41467-025-66487-0
50. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
51. Abramian A, Damaskou A, Toonen RF, Verhage M. Growth factor supplementation modulates survival, morphology, and network activity of neurogenin-2 induced human neurons. Scientific Reports [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41598-025-31868-4_reference.pdf
52. Available from: http://json-schema.org/draft-07/schema#",
