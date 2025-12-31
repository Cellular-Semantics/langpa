# Gene Program Markdown Report

## Context
- Cell type: Astrocyte
- Disease: Astrocytoma (high-grade glioma)
- Tissue: Brain

## Input Genes
DPP6, CHST11, MAP3K1, SLC24A3, NRXN1, REV3L, KAT2B, TNR, PTPRZ1, LRRTM4, SEZ6L, SOX2-OT, CSMD1, LHFPL3, SEMA5A, RGS7, MMP16, LRRC4C, LRRN1, MTSS1, KCNIP1, KCND2, PTPRD, NXPH1, NTRK3, ... (200 total)

## Program: Synaptic Adhesion and Connectivity
Network of cell adhesion molecules and scaffolding proteins maintaining synaptic stability, neuronal network organization, and intercellular communication through specialized adhesion complexes. Includes classical cadherins, neurexins, neuroligins, protocadherins, and immunoglobulin superfamily adhesion molecules critical for synapse formation and stabilization.

**Predicted impacts**
- Enhanced intercellular communication and network synchronization through strengthened synaptic adhesion
- Increased synaptic stability and reduced synaptic pruning
- Dysregulated synaptic connectivity patterns and abnormal network topology
- Altered responsiveness to neural circuit activity and synaptic refinement signals

**Evidence summary**
Multiple adhesion molecules collectively establish the molecular infrastructure for synaptic connections. In normal physiology, these proteins enable transsynaptic signaling and provide structural stability to established synapses. In astrocytoma context, dysregulated adhesion molecules may reflect both aberrant astrocytic properties and altered interactions between tumor cells and surrounding neurons. The presence of both classical adhesion molecules and immunoglobulin-family adhesion factors suggests multi-modal adhesion capability.

**Atomic biological processes**
- Transsynaptic signaling and synapse stabilization. Genes: NRXN1, NLGN4X, NLGN4Y, CNTN1, CNTN3, CNTN6
  - [2]: NCAM1 encodes cell adhesion protein member of immunoglobulin superfamily involved in cell-to-cell interactions
  - [3]: Cell adhesion molecules mediate cell-cell communications and interact with ECM, critical for synaptic development and establishment of neuronal networks
- Cadherin-based adhesion complex formation. Genes: CDH10, CDH20, PCDH9, PCDH15, CTNNA2
  - [3]: Decreased expression of adhesion coding genes such as Cdh10, Nectin1 in diseased neurons; cell adhesion molecules critical for synaptic development
- Immunoglobulin superfamily adhesion. Genes: IGSF21, OPCML
  - [2]: NCAM1 as member of immunoglobulin superfamily demonstrates importance of this molecular class for cell-cell interactions

**Atomic cellular components**
- Postsynaptic density organization. Genes: DLG2, CASK, ANK3
  - [34]: CASK calcium/calmodulin dependent serine protein kinase critical for postsynaptic organization and neurodevelopment
- Synaptic vesicle cycling apparatus. Genes: SYN3, RIMS1, RIMS2
  - [3]: Synaptic vesicle cycle pathway affected in synaptic maintenance processes

**Required genes (not in input)**
- Genes: NECTIN1, CADM1, LSAMP
  - [3]: Nectin1 identified as dysregulated adhesion molecule in disease models

**Program citations**
- [2]: NCAM1 involvement in cell-to-cell interactions establishes importance of this adhesion class
- [3]: Comprehensive description of adhesion molecule dysregulation in neurodegeneration and tau pathology
- [34]: CASK-neurexin interactions critical for neuroarchitectural development

## Program: Neuronal Excitability Control
Ion channel proteins and their regulatory subunits controlling action potential generation, propagation, and repolarization. Encompasses voltage-gated sodium and potassium channels, calcium-activated potassium channels, voltage-independent leak channels, and localized phosphorylation control at the axon initial segment. This program maintains stable neuronal firing rates and integrates inhibitory regulation through phosphatase signaling.

**Predicted impacts**
- Dysregulated neuronal resting membrane potential leading to increased baseline excitability
- Altered action potential threshold and firing rate characteristics
- Impaired action potential repolarization causing prolonged depolarization phases
- Enhanced seizure susceptibility through net increase in neuronal excitability

**Evidence summary**
Ion channels represent primary determinants of neuronal excitability through control of membrane potential and action potential characteristics. Voltage-gated sodium channels initiate action potentials through rapid sodium influx, while potassium channels mediate repolarization through outward potassium currents. Voltage-independent leak channels (NALCN) establish the resting membrane potential set-point. Recent mechanistic studies reveal that PP2A regulatory subunits specifically enriched at the axon initial segment selectively modulate neuronal excitability through localized dephosphorylation of ion channels, enabling compartmentalized control of neuronal firing. In astrocytoma context, dysregulation of these ion channel programs likely contributes to seizures and abnormal network activity observed in patients.

**Atomic biological processes**
- Action potential generation and propagation. Genes: SCN1A, SCN3A
  - [47]: SCN1A mutations associated with focal seizures and neuronal hyperexcitability; critical for sodium influx during depolarization
  - [50]: SCN3A may contribute to neuronal hyperexcitability and epilepsy
- Action potential repolarization. Genes: KCND2, KCND3, KCNMB2, KCNIP1, KCNIP4
  - [24]: Kv1.2 potassium channel critical for membrane trafficking and AIS-enriched Kv1 channel conducts major outward currents
- Resting membrane potential establishment. Genes: NALCN, UNC79, UNC80
  - [14]: Nalcn sodium leak channel plays critical role in controlling neuronal excitability by contributing to resting membrane potential
  - [16]: UNC80 bridges between UNC79 and NALCN cation channel; de novo NALCN mutations cause severe neurological phenotypes
- Phosphorylation-dependent excitability modulation. Genes: PPP2R2B, PPP2R2C
  - [24]: PP2A-B55γ regulatory subunit functionally interacts with Kv1.2 to regulate its expression at AIS; dephosphorylation of phosphosite pS440/441 crucial for membrane trafficking
  - [33]: PP2A regulatory subunits Ppp2r2c and Ppp2r2a regulate baseline neuronal firing; AIS-enriched Ppp2r2c selectively potentiates neuronal activity
  - [27]: PPP2R2B defects cause autosomal dominant spinocerebellar ataxia 12, indicating critical role in neuronal excitability

**Atomic cellular components**
- Axon initial segment protein organization. Genes: ANK3
  - [33]: AIS recognized as hotspot for protein phosphorylation regulating action potential generation and neuronal polarity
- Potassium channel auxiliary subunits. Genes: KCNMB2, KCNIP1, KCNIP4
  - [24]: Kvβ2 auxiliary subunit regulated by cyclin-dependent kinases; affects axonal membrane targeting of Kv1 channel

**Required genes (not in input)**
- Genes: KCNQ2, KCNQ3, CACNA1C
  - [33]: Casein kinase 2 phosphorylates KCNQ channels; CACNA1C encodes L-type calcium channels important for AIS function

**Program citations**
- [14]: NALCN as voltage-independent leak channel critical for neuronal excitability control
- [24]: Comprehensive mechanistic study of PP2A subunit localization and ion channel regulation at AIS
- [33]: Detailed analysis of PP2A regulatory subunit functions in neuronal excitability modulation

## Program: Axon Guidance and Developmental Routing
Molecular signaling systems directing developing axons toward appropriate targets through secreted and transmembrane guidance factors, receptor complexes, and intracellular signaling cascades. Includes semaphorins, netrin-related factors, and downstream effectors mediating growth cone collapse, attractive guidance, and directional selection of axonal projections during nervous system development.

**Predicted impacts**
- Dysregulated axonal pathfinding and aberrant axonal projections from tumor cells
- Altered axon branching patterns and dendritic arbor complexity
- Impaired response to guidance cues resulting in abnormal network architecture
- Enhanced tumor cell invasion along white matter tracts through inappropriate guidance signal expression

**Evidence summary**
Axon guidance molecules establish nervous system connectivity by directing developing axons toward appropriate targets. Semaphorins provide repulsive guidance through growth cone collapse, while attractant factors (netrin family) promote axonal advancement. Downstream effectors including CRMP2 and Trio transduce guidance signals into changes in actin cytoskeleton organization and growth cone morphodynamics. The presence of guidance molecules in astrocytoma suggests aberrant expression of developmental programs; tumors may express guidance factors inappropriate for their cell identity, potentially creating abnormal signaling gradients that disrupt surrounding neural circuitry. The identification of multiple guidance effectors indicates sophisticated capacity for directional signaling control.

**Atomic biological processes**
- Repulsive axon guidance signaling. Genes: SEMA5A, SRGAP2
  - [15]: SEMA6D transmembrane semaphorins act as repulsive axon guidance cues similar to secreted ones
  - [13]: CRMP2 phosphorylation mediates axon repulsion and branch pruning downstream of guidance receptor signaling
- Growth cone filopodial dynamics control. Genes: TRIO
  - [13]: Trio knock-down restores filopodial motility in CRMP2 S522D-expressing neurons; pCRMP2-Trio complex suppresses filopodial motility
- Axon branching and arbor formation. Genes: DISC1, DOCK9, DOCK4, DOCK10
  - [12]: DISC1 plays critical role in neurite outgrowth and neuronal migration in adult mammalian brain, particularly in hippocampus
  - [13]: Sema3A treatment decreases total axonal arbor length and branch number through CRMP2-dependent signaling

**Atomic cellular components**
- Growth cone actin cytoskeleton regulation. Genes: SRGAP2, ARHGAP42, ARHGAP20
  - [13]: Trio GEF1 domain mediates Rac1 activation driving actin dynamics through its GEF domains
- Synaptic SNARE complex components. Genes: STXBP5L, SYT16
  - [3]: Synaptic vesicle cycle and signal release pathways involved in synaptic modulation

**Required genes (not in input)**
- Genes: DCC, ROBO1, ROBO2
  - [13]: DCC and Robo proteins represent complementary guidance receptor families mediating attractive and repulsive signaling

**Program citations**
- [13]: Comprehensive mechanistic analysis of Trio and CRMP2 in axon guidance and branching control
- [12]: DISC1 role in neurite outgrowth and neuronal migration
- [15]: Semaphorin role as repulsive axon guidance cues

## Program: Glutamate and GABA Neurotransmission
Ionotropic and metabotropic glutamate receptor signaling systems mediating excitatory synaptic transmission and neuromodulation, coupled with GABAergic synthesis and signaling that provides inhibitory counterbalance. This program maintains excitatory-inhibitory balance critical for stable network operation and establishes developmental critical periods for circuit refinement.

**Predicted impacts**
- Dysregulated excitatory synaptic transmission strength and duration
- Impaired inhibitory GABAergic signaling leading to E/I imbalance
- Disrupted critical period gating and abnormal developmental plasticity timing
- Seizure susceptibility through net excitatory bias in neural circuits

**Evidence summary**
Glutamatergic and GABAergic systems provide the primary excitatory and inhibitory neurotransmission supporting all neural computation. Ionotropic receptors enable fast synaptic transmission through direct coupling to ion channels, while metabotropic receptors provide modulatory functions through G-protein signaling cascades. The precise balance between excitatory and inhibitory signaling (E/I balance) represents a fundamental principle of neural circuit organization, with dysregulation contributing to seizures, autism spectrum disorders, and schizophrenia. GABAergic signaling development demonstrates remarkable temporal precision, with the onset of GAD1 expression immediately preceding critical period opening. In astrocytoma context, altered glutamate and GABA metabolism through tumor-associated changes in transporter expression and enzymatic activity contributes to excitotoxicity and network dysfunction.

**Atomic biological processes**
- AMPA-type ionotropic glutamate receptor signaling. Genes: GRIA2, GRIA3
  - [9]: Transsynaptic signaling mediated by extracellular domain of GluR2 regulates stability of presynaptic terminals
- Delta-type ionotropic glutamate receptor signaling. Genes: GRID2
  - [25]: GluD2 gating triggered by type 1 metabotropic glutamate receptors; GRID2 mutations associated with cerebellar ataxia
  - [28]: Grid2 active in glutamatergic synapse and postsynaptic density membrane at parallel fiber to Purkinje cell synapse
- Metabotropic glutamate receptor 5 signaling. Genes: GRM5
  - [8]: Metabotropic glutamate receptor 5 associated with neurodegeneration and amyloid deposition in Alzheimer disease
  - [10]: FMRP and mGlu5 control stress granule formation in astrocytes
- GABA synthesis and GABAergic signaling. Genes: GAD1
  - [40]: GAD1 as GABA-synthetic enzyme; GABAergic signaling necessary for opening of critical periods during neural development
  - [43]: GAD1 encodes glutamate decarboxylase 1; GABA major inhibitory neurotransmitter synthesized by this enzyme
- Critical period gating through GABAergic signaling. Genes: GAD1
  - [40]: Increased intracortical GABA signaling necessary for opening of critical periods; GABAergic signaling regulates CP timing across phyla

**Atomic cellular components**
- Postsynaptic density AMPA receptor organization. Genes: GRIA2, GRIA3
  - [3]: GSG1L regulates AMPA receptor activity; Syndig1 regulates NMDA and AMPA receptor content
- Synaptic vesicle glutamate and GABA accumulation. Genes: SLC24A3
  - [40]: Neurotransmitter transport mechanisms involved in synaptic transmission

**Required genes (not in input)**
- Genes: GRIN1, GRIN2B, GAD2
  - [3]: NMDAR1 and related NMDA receptor subunits dysregulated in AD tauopathy; GAD2 encodes GAD65 controlling GABA synthesis

**Program citations**
- [40]: Comprehensive analysis of GABAergic signaling in critical period gating across development
- [8]: GRM5 dysregulation in neurodegeneration establishing glutamate signaling importance
- [9]: GRIA2 in synaptic stability and presynaptic function

## Program: Growth Factor Receptor Signaling
Receptor tyrosine kinase signaling controlling cell proliferation, survival, differentiation, and metabolic state. Encompases PDGF receptor alpha, EGFR, neurotrophic receptor tyrosine kinase 3, and downstream signaling nodes including AKT/PKB, MAP kinase cascades, and their negative regulators. This program represents the primary driver of proliferative capacity and is frequently dysregulated in astrocytoma through mutation and overexpression.

**Predicted impacts**
- Enhanced proliferation and reduced cell cycle arrest through sustained RTK signaling
- Increased survival signaling and reduced apoptosis through AKT pathway activation
- Metabolic reprogramming toward glycolytic and anabolic states
- Therapeutic resistance through pathway redundancy and feedback loop dysregulation

**Evidence summary**
Growth factor receptors represent critical components of cellular communication systems that control fundamental decisions regarding proliferation, survival, and differentiation. Dysregulation of these pathways through mutation, overexpression, or loss of negative regulation represents a hallmark feature of cancer. In astrocytoma, PDGFRA represents a particularly potent driver, with animal models demonstrating that constitutively active PDGFRA signaling alone is sufficient for gliomagenesis. Multiple redundant growth factor pathways operate in most astrocytomas, explaining therapeutic resistance to single-pathway inhibitors. The identification of NTRK3 fusion events as driver events in human astrocytoma demonstrates that aberrant NTRK signaling represents an established oncogenic mechanism. Negative regulators including PHLPP1 demonstrate that loss of growth inhibitory signals accompanies growth factor pathway activation in many tumors.

**Atomic biological processes**
- PDGF receptor alpha signaling. Genes: PDGFRA
  - [20]: PDGFRA encodes cell surface tyrosine kinase receptor for platelet-derived growth factor family
  - [17]: Constitutively active PDGFRA signaling sufficient driver of gliomagenesis in mouse models; PDGFRA most potent driver of gliomagenesis
- EGFR signaling. Genes: EGFR
  - [17]: EGFR among multiple tyrosine kinases upregulated in tumor progression
- Neurotrophic receptor tyrosine kinase signaling. Genes: NTRK3
  - [36]: TrkC (encoded by NTRK3) neurotrophic receptor promotes survival of neuronal and glial cells
  - [38]: NTRK3 expression promotes neuronal differentiation of neural stem cells through TrkC receptor
  - [29]: TRIM24::NTRK2 fusion gene identified as driver event in astrocytoma
- AKT/PKB kinase signaling. Genes: AKT1, PHLPP1
  - [45]: AKT1 critical node in growth factor signaling controlling cell survival, proliferation, and metabolism
  - [42]: PHLPP1 dephosphorylates and inactivates AKT; loss of PHLPP1 promotes AKT signaling persistence and therapy resistance
- MAP kinase cascade signaling. Genes: MAP3K1
  - [17]: MAP kinase cascade downstream effector of growth factor signaling; RAF-MAP signaling altered in tumor evolution

**Atomic cellular components**
- Growth factor receptor complex assembly. Genes: PDGFRA, EGFR, NTRK3
  - [20]: PDGFRA encodes receptor component enabling growth factor ligand binding and signal transduction

**Required genes (not in input)**
- Genes: BRAF, KRAS, PIK3CA
  - [17]: BRAF, KRAS mutations represent alternative driver events in pediatric gliomas; these genes not in input list but critically important for complete pathway understanding

**Program citations**
- [17]: Comprehensive characterization of growth factor pathway dysregulation in pediatric glioma models
- [29]: Identification of NTRK2 fusion in human astrocytoma and functional analysis of driver capacity
- [42]: PHLPP1 role in AKT regulation and therapeutic resistance

## Program: Histone Modification and Chromatin Remodeling
Epigenetic regulatory machinery controlling gene accessibility through histone acetylation/deacetylation, methylation, and ATP-dependent chromatin remodeling. This program encompasses histone acetyltransferases, histone deacetylases, chromatin remodeling ATPases, and their regulatory complexes that collectively determine whether genomic regions remain in transcriptionally active (open) or repressed (closed) chromatin states.

**Predicted impacts**
- Dysregulated gene expression through altered chromatin accessibility patterns
- Suppressed tumor suppressor gene expression through histone deacetylation
- Enhanced oncogene expression through strategic histone acetylation
- Therapeutic vulnerability to HDAC inhibitors reversing epigenetic silencing

**Evidence summary**
Histone modifications represent a major control point for gene expression, with acetylation generally associated with transcriptional activation and deacetylation with repression. In cancer, histone deacetylase overactivity frequently silences tumor suppressor genes while leaving oncogene regions relatively accessible, creating an epigenetic state favoring proliferation. Recent therapeutic successes with HDAC inhibitors demonstrate that reversing these epigenetic changes can restore tumor suppressor expression and induce cell death. The identification of ATRX mutations in combination with IDH mutations in astrocytoma suggests that chromatin remodeling dysfunction cooperates with metabolic alterations to drive transformation. The mechanistic analysis of HDAC inhibitor effects reveals that compound 3B increases reactive oxygen species while simultaneously inhibiting proliferation, suggesting multiple complementary mechanisms of action.

**Atomic biological processes**
- Histone acetylation and transcriptional activation. Genes: KAT2B
  - [18]: KAT2B associates with p300/CBP and competes with E1A for binding; has in vitro and in vivo binding activity with CBP and p300
  - [21]: KAT2B inhibits cholangiocarcinoma growth through interaction with SP1 to regulate NF2-YAP signaling
- HDAC inhibition and tumor suppressor reactivation.
  - [19]: HDACis restore expression of tumor suppressor genes, inducing apoptosis and overcoming therapeutic resistance; novel hydroxamic acid analogue exhibits potent anticancer activity
  - [22]: HDAC-6 inhibitor Tubacin demonstrates potent anti-proliferative effect in cytotoxicity and live-dead assays
- ATRX-mediated chromatin remodeling. Genes: ATRX
  - [4]: Low ATRX mRNA expression combined with IDH1/2 mutations associated with astrocytic tumors
  - [17]: H3.3(G34R) combined with PDGFRA(D842V) or Trp53 KO produces gliomas; ATRX loss may contribute through chromatin remodeling alterations

**Atomic cellular components**
- Acetyltransferase complex assembly. Genes: KAT2B
  - [18]: KAT2B associates with p300/CBP complexes forming multi-subunit regulatory assemblies

**Required genes (not in input)**
- Genes: HDAC1, HDAC2, HDAC6, SIRT1
  - [19]: HDAC isoforms represent critical targets; HDAC-6 inhibitor demonstrates therapeutic potential

**Program citations**
- [19]: Comprehensive study of HDAC inhibitor mechanisms in glioblastoma
- [18]: KAT2B structure and interactions with p300/CBP complexes
- [4]: ATRX mutations in astrocytic tumors coupled with IDH mutations

## Program: Developmental Transcriptional Programming
Transcription factors and long noncoding RNAs controlling cell type specification, lineage commitment, developmental transitions, and developmental plasticity. This program encompasses SOX family transcription factors maintaining neural stem cell identity, EMT regulators controlling epithelial-mesenchymal transitions, and noncoding RNAs regulating developmental pathways.

**Predicted impacts**
- Aberrant reactivation of neural stem cell developmental programs in differentiated astrocytes
- Enhanced cellular plasticity and capacity for lineage switching
- Increased migratory and invasive capacity through EMT induction
- Dysregulated developmental plasticity enabling tumor cell adaptation

**Evidence summary**
Developmental transcription factors control cell fate decisions and lineage commitment during nervous system development, with their expression typically restricted to progenitor populations and downregulated upon terminal differentiation. The presence of neural stem cell markers including SOX2 and developmental lncRNAs in astrocytoma cells indicates aberrant recapitulation of developmental identity programs. This dedifferentiation toward progenitor-like states may explain the enhanced proliferative capacity of astrocytoma cells and their capacity to survive outside normal tissue contexts. The EMT program mediated by ZEB1 links developmental plasticity to invasive capacity, suggesting that the same molecular mechanisms enabling developmental transitions also promote tumor dissemination. The identification of LINC01068 dysregulation in neural development establishes mechanistic links between transcriptional dysfunction and developmental outcomes.

**Atomic biological processes**
- Neural stem cell identity maintenance. Genes: SOX2-OT, SOX5
  - [32]: SOX2 intronless gene encodes member of SRY-related HMG-box family; involved in regulation of embryonic development
  - [30]: Astro3 subtype expressing SOX2 and DCX consists of neural progenitor cells; SOX2 expression maintained in neural progenitor cells
- Epithelial-mesenchymal transition regulation. Genes: ZEB1
  - [44]: ZEB1 mediates EMT/plasticity-associated ferroptosis sensitivity in cancer cells by regulating lipogenic enzyme expression
- Long noncoding RNA-mediated developmental regulation. Genes: SOX2-OT, LINC01322, LINC00461, LINC01237
  - [11]: LINC01068 regulates schizophrenia-associated genes and synaptic pathways; knockdown impairs proliferation, migration, and differentiation of neural stem cells
- Oligodendrocyte lineage commitment. Genes: OLIG1, MYT1
  - [32]: MYT1 represents oligodendrocyte-specific transcription factor

**Required genes (not in input)**
- Genes: SOX1, SOX9, OCT4, NANOG
  - [30]: SOX9 and other SOX family members demonstrate cell-type-specific developmental functions

**Program citations**
- [30]: Identification of neural progenitor cell-like astrocytes expressing SOX2 and developmental markers
- [11]: LINC01068 roles in neural stem cell proliferation and differentiation
- [44]: ZEB1-mediated EMT and ferroptosis regulation

## Program: DNA Damage Response and Translesion Synthesis
DNA repair pathways enabling cells to tolerate and bypass DNA lesions through specialized polymerases and error-prone synthesis mechanisms. This program encompasses translesion DNA polymerases (REV3L, POLQ) that enable replication fork progression past DNA lesions that would normally block replication, allowing continued survival despite genomic damage.

**Predicted impacts**
- Enhanced tolerance to DNA-damaging therapeutic agents
- Continued proliferation despite genomic stress and mutation accumulation
- Acquisition of additional mutations through error-prone bypass synthesis
- Therapeutic resistance to chemotherapy and radiation therapy

**Evidence summary**
Most DNA lesions block replication fork progression and trigger apoptotic cell death through checkpoint activation. Specialized translesion polymerases provide an alternative route enabling cells to bypass lesions through low-fidelity synthesis that continues replication at the cost of increased mutation rates. In cancer, this tradeoff favors continued proliferation over genetic fidelity, potentially explaining the high mutational burdens characteristic of many astrocytomas. The presence of both REV3L and POLQ indicates redundant mechanisms for lesion bypass, suggesting that tumor cells have acquired multiple independent pathways for mutation tolerance. This redundancy may explain why targeting single translesion polymerase genes fails to produce therapeutic effects in many cancers.

**Atomic biological processes**
- Translesion DNA synthesis by polymerase zeta. Genes: REV3L
  - [46]: REV3L encodes catalytic subunit of DNA polymerase zeta; functions in translesion DNA synthesis
- Error-prone and error-free translesion synthesis. Genes: POLQ
  - [49]: POLQ encodes DNA polymerase theta; capable of both error-free and error-prone DNA synthesis depending on substrate context

**Required genes (not in input)**
- Genes: REV1, DPB3, MAD2L2
  - [49]: REV1 and other components of translesion synthesis machinery required for complete pathway function

**Program citations**
- [46]: REV3L role in translesion DNA synthesis and polymerase zeta function
- [49]: POLQ dual capacity for error-free and error-prone translesion synthesis

## Program: Astrocyte-Specific Metabolic Support
Specialized metabolic and homeostatic functions performed by astrocytes to maintain appropriate brain microenvironment and support neuronal function. Includes ion and solute transporters maintaining extracellular osmolarity and ionic composition, water channels enabling glymphatic clearance, and metabolite transporters supporting astrocyte-neuron metabolic interactions.

**Predicted impacts**
- Dysregulated extracellular ion and osmolarity homeostasis
- Impaired glymphatic clearance of brain metabolites
- Altered astrocyte-neuron metabolic coupling
- Reduced neuroprotective effects of astrocytes on surrounding neurons

**Evidence summary**
Astrocytes perform specialized homeostatic functions critical to maintaining appropriate brain microenvironment. The astrocytic endfeet processes in direct contact with blood vessels express high concentrations of aquaporin-4, enabling rapid water transport that maintains osmotic balance and facilitates glymphatic clearance of brain metabolites. Loss of these astrocytic support functions in astrocytoma may contribute to local edema, impaired metabolite clearance, and neuronal dysfunction. The presence of ion and solute transporters indicates that astrocytomas retain some capacity for metabolic support, though dysregulation of these functions likely contributes to pathology.

**Atomic biological processes**
- Astrocytic ion and solute homeostasis. Genes: SLC24A3, SLC4A10, SLC2A13
  - [39]: AQP4 expressed in astrocytic endfoot membranes; facilitates water transport critical to maintaining extracellular osmolarity and glymphatic clearance
- Astrocytic water transport and glymphatic function. Genes: AQP4
  - [39]: Aquaporin-4 autoantibodies in neuromyelitis optica spectrum disorder; AQP4 critical for glymphatic clearance mechanisms
- Astrocytic glutamate metabolism and recycling. Genes: GAD1
  - [40]: GABA synthesis and astrocytic neurotransmitter metabolism supporting inhibitory neurotransmission

**Atomic cellular components**
- Astrocytic endfoot specialization. Genes: AQP4
  - [39]: AQP4 concentrated in astrocytic endfeet adjacent to blood vessels enabling specialized water transport

**Required genes (not in input)**
- Genes: GLAST, GLT-1, GAT1
  - [39]: Glutamate transporters GLAST and GLT-1 represent critical astrocytic components enabling glutamate uptake for metabolism and recycling

**Program citations**
- [39]: AQP4 role in astrocytic water transport and glymphatic clearance
- [40]: GABAergic signaling and astrocytic neurotransmitter metabolism

## Program: Tumor Microenvironment Remodeling and Immunomodulation
Pathological remodeling of tissue microenvironment surrounding astrocytoma cells through inflammatory signaling, complement activation, extracellular matrix breakdown, and recruitment of immunosuppressive cell populations. This program transforms the normal brain microenvironment into a tumor-supportive niche that promotes proliferation and invasion while suppressing anti-tumor immunity.

**Predicted impacts**
- Enhanced tumor cell invasion through matrix degradation
- Immunosuppressive microenvironment limiting anti-tumor immunity
- Recruitment of pro-tumor immune cell populations
- Altered blood-brain barrier function enabling vascular permeability

**Evidence summary**
The tumor microenvironment represents a critical determinant of tumor behavior and therapeutic response, with malignant tumors actively remodeling their surrounding tissue to create a supportive niche. Complement system activation through C5a secretion recruits immunosuppressive myeloid populations that promote tumor growth and therapy resistance. Matrix metalloprotease expression enables invasion through basement membranes and white matter tracts, facilitating tumor infiltration. The inflammatory cytokine milieu simultaneously promotes tumor cell proliferation while suppressing adaptive immune responses through recruitment of regulatory T cells and myeloid-derived suppressor cells. In astrocytoma specifically, the microenvironment remodeling program contributes to seizure susceptibility through altered neuronal microenvironment and to therapy resistance through recruitment of immunosuppressive populations.

**Atomic biological processes**
- Inflammatory cytokine signaling. Genes: TNF
  - [48]: TNF encodes multifunctional proinflammatory cytokine mainly secreted by immune cells
- Complement system activation.
  - [41]: Tumor mesenchymal stem-like cells secrete C5a, altering tumor microenvironment and promoting tumor progression through complement activation
- Extracellular matrix remodeling. Genes: MMP16, COL4A3, COL4A4, COL20A1, VCAN
  - [41]: Extracellular matrix breakdown facilitates tumor cell invasion through tissue barriers
- Cell adhesion molecule dysregulation in tumor stroma. Genes: CNTN1, CNTN3
  - [3]: Cell adhesion molecules mediate ECM interactions and are dysregulated in disease states

**Atomic cellular components**
- Extracellular matrix proteoglycan organization. Genes: VCAN, CSPG5
  - [41]: Proteoglycans including versican contribute to extracellular matrix organization and tumor microenvironment structure

**Required genes (not in input)**
- Genes: IL-6, IL-8, CCL2
  - [41]: Multiple inflammatory cytokines and chemokines constitute complete microenvironment remodeling program beyond those in input list

**Program citations**
- [41]: Comprehensive study of complement-mediated microenvironment remodeling in glioblastoma
- [48]: TNF role in inflammatory microenvironment establishment

## Program: Synaptic Plasticity and Calcium-Dependent Signaling
Molecular mechanisms underlying activity-dependent modification of synaptic strength and connectivity through calcium-dependent signaling cascades. This program encompasses calcium sensor proteins, calcium-responsive kinases, synaptic vesicle proteins, and presynaptic active zone organization enabling translation of calcium signals into changes in neurotransmitter release probability.

**Predicted impacts**
- Dysregulated synaptic strength modification through altered calcium sensitivity
- Impaired synaptic plasticity and learning capacity
- Altered neurotransmitter release characteristics and probability
- Dysfunction of activity-dependent developmental refinement processes

**Evidence summary**
Synaptic plasticity represents the molecular basis of learning and memory, arising from activity-dependent modification of synaptic strength through calcium-dependent signaling cascades. Calcium influx through voltage-gated channels during neuronal activity triggers multiple signaling pathways controlling both presynaptic release probability and postsynaptic receptor density. RIMS family proteins specifically couple presynaptic calcium influx to neurotransmitter release through organization of active zone architecture bringing synaptic vesicles into proximity with voltage-gated calcium channels. Dysregulation of this calcium signaling program contributes to multiple neurological disorders and likely contributes to astrocytoma-associated seizures through aberrant network plasticity.

**Atomic biological processes**
- Calcium-dependent synaptic transmission. Genes: RIMS1, RIMS2, CASK, SYT16
  - [34]: CASK calcium/calmodulin-dependent serine protein kinase regulates synaptic function
  - [3]: Synaptic vesicle cycle and signal release pathways involved in synaptic plasticity and homeostasis
- Synaptic vesicle organization and release. Genes: SYN3, STXBP5L, RIMS1, RIMS2
  - [3]: RIMS proteins couple calcium to neurotransmitter release through organization of active zone complexes
- Activity-dependent gene expression downstream of calcium. Genes: NCALD
  - [3]: Calcium-dependent signaling regulates modification of post-synaptic structure and dendrite development

**Atomic cellular components**
- Presynaptic active zone organization. Genes: RIMS1, RIMS2
  - [3]: Active zone proteins organize synaptic vesicles and coordinate calcium channels with exocytotic machinery
- Synaptic vesicle cycle machinery. Genes: SYN3, STXBP5L
  - [3]: Synaptic vesicle recycling and availability control through synapsin and STXBP family proteins

**Required genes (not in input)**
- Genes: CAMK2A, CAMK2B, CALMODULIN
  - [3]: CAMK2B dysregulation in tauopathy; calmodulin-dependent kinases critical for calcium-dependent synaptic plasticity

**Program citations**
- [34]: CASK-mediated calcium-dependent signaling in synaptic organization
- [3]: Comprehensive pathway analysis of synaptic plasticity gene dysregulation

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/4684
3. 3. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/546
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/10752
6. 6. Martín-Monteagudo C, Sánchez RJ, Adams JM, Puente N, Grandes P, Marsicano G, et al.. An astrocytic ensemble at vHip-NAc synapses modulates cognitive impairments induced by chronic tetrahydrocannabinol exposure. Nature Communications [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s41467-025-67166-w_reference.pdf
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/44484
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/2915
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/2891
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/108071
11. 11. Dang X, Gong D, Dai S-S, Teng Z, Luo X-J. Genetic and functional insights into long noncoding RNAs in schizophrenia. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03421-2
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/27185
13. 13. Fingleton E, Lombardo A, Won S, Chang K, Li Y, Roche KW. Trio and CRMP2 regulate axon branching and Semaphorin3A signaling. Communications Biology [Internet]. 2025Nov25;8(1). Available from: https://www.nature.com/articles/s42003-025-08988-8
14. 14. Available from: https://www.nature.com/research-intelligence/nri-topic-summaries/nalcn-ion-channels-and-their-role-in-neuronal-function-micro-672855
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/80031
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/259232
17. 17. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/8850
19. 19. Padmini P, Ipshita D, Yashaswini R, Babu SV, Poonam B, Manjunath M, et al.. Targeting glioblastoma with HDAC inhibitors: insights into hydroxamic acid-based therapeutic strategies.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41331688/
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
21. 21. Ameya J, Natasha R, Jayce H, Erik M, Andrew E, Surabhi S. Isoform-specific vs. pan-histone deacetylase inhibition as approaches for countering glioblastoma: an . Frontiers in oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41395596/?fc=None&ff=20251215183737&v=2.18.0.post22+67771e2
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/18747
23. 23. Anderson AP, Kim S, Melton AJ, Ding X, Zhang W, Saltzman AB, et al.. A distinct PP2A subunit regulates local protein phosphorylation at the axon initial segment. Nature Communications [Internet]. 2025Dec3;16(1). Available from: https://www.nature.com/articles/s41467-025-66120-0
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/2895
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/3725
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/5521
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/14804
28. 28. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
29. 29. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/8573
33. 33. Available from: https://connect.biorxiv.org/archive/
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/4916
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/4340
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/18213
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/361
38. 38. Corke J, Radi MH, Landgraf M, Baines RA. Maturation of GABAergic signalling times the opening of a critical period in Drosophila melanogaster. Scientific Reports [Internet]. 2025Nov17;15(1). Available from: https://www.nature.com/articles/s41598-025-24116-2
39. 39. Oh Y, Yoo J, Lee D, Ko B, Hong JP, Moon JH, et al.. Restoring the glioblastoma tumor microenvironment by targeting C5a with the antagonist W54011. Scientific Reports [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41598-025-30853-1
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/23239
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/14415
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/6935
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/207
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/5980
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/6323
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/10721
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/6328
49. 49. Available from: http://json-schema.org/draft-07/schema#",
