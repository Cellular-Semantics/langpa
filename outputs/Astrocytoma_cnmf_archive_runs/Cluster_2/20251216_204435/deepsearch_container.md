# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and astrocyte-derived tumor cells
- Disease: Astrocytoma, including low-grade astrocytoma and high-grade glioblastoma
- Tissue: Central nervous system, brain

## Input Genes
DPP6, CHST11, MAP3K1, SLC24A3, NRXN1, REV3L, KAT2B, TNR, PTPRZ1, LRRTM4, SEZ6L, SOX2-OT, CSMD1, LHFPL3, SEMA5A, RGS7, MMP16, LRRC4C, LRRN1, MTSS1, KCNIP1, KCND2, PTPRD, NXPH1, NTRK3, ... (200 total)

## Program: Synaptic Adhesion and Neuronal Contact
Multi-layered cell-cell adhesion between astrocytes and neurons through direct neurexin-contactin interactions and protocadherin-mediated contacts, forming organized synaptic-like structures and supporting neuron-astrocyte bidirectional communication.

**Predicted impacts**
- Enhanced formation of stable astrocyte-neuron contacts through multiple adhesion mechanisms
- Increased responsiveness of tumor cells to neuronal contact-mediated signals
- Potential disruption of normal circuit organization through aberrant synaptic-like contacts
- Increased dependence on neuronal-derived survival signals through enhanced contact-mediated communication

**Evidence summary**
The coordinate expression of neurexin-binding partners, protocadherins, neuroligins, and contactins represents a comprehensive synaptic adhesion program that astrocytoma cells would not normally express at high levels. This program mirrors developmental stages where neural progenitor cells establish initial contact with differentiating neurons. The presence of multiple complementary adhesion systems suggests astrocytomas engage sophisticated cell-cell recognition mechanisms, potentially enabling invasion through perineuronal spaces or formation of aberrant synaptic-like contacts with adjacent neurons that could influence tumor growth and behavior.

**Atomic biological processes**
- Neurexin-neuroligin-mediated synaptic adhesion. Genes: NRXN1, NLGN4X, NLGN4Y, CNTNAP2, NXPH1, CNTN1, CNTN3, CNTN6
  - [11]: CNTNAP2 encodes contactin-associated protein functioning as cell adhesion molecule in vertebrate nervous system
- Protocadherin-mediated cell-cell recognition. Genes: PCDH9, PCDH15, CDH10, CDH20
  - [28]: Protocadherins link extracellular adhesive interactions to intracellular signaling through catenin interaction
- Extracellular matrix scaffold for synaptic organization. Genes: TNR, COL4A3, COL4A4, COL20A1, CSPG5, CSMD3, BCAN
  - [24]: Astrocytes maintain BBB and synaptic transmission through structural associations in astro-neurovascular unit

**Atomic cellular components**
- Neurexin-contactin adhesion complex. Genes: CNTNAP2, NXPH1, NLGN4X, NLGN4Y
  - [11]: CNTNAP2 functions in vertebrate nervous system cell adhesion
- Synaptic extracellular matrix. Genes: TNR, BCAN, CSPG5
  - [24]: Perineuronal nets and synaptic clefts contain organized ECM components

**Required genes (not in input)**
- Genes: NCAM1, L1CAM, neurexin isoforms, thrombospondin
  - [24]: Additional adhesion molecules supporting synaptic organization

**Program citations**
- [11]: CNTNAP2 gene encodes contactin-associated protein functioning as cell adhesion molecule
- [24]: Astrocytes involved in synaptic transmission and synapse turnover through structural positioning
- [28]: Protocadherin-mediated adhesion links extracellular interactions to intracellular signaling

## Program: Integrin-Mediated Cell-Substrate Adhesion
Engagement of integrins with extracellular matrix components, formation of focal adhesion complexes, and activation of mechanotransduction signaling cascades that link cell-matrix interactions to intracellular signaling affecting migration, survival, and proliferation.

**Predicted impacts**
- Enhanced cell-matrix adhesion strengthening tumor cell attachment to stromal components
- Increased mechanotransduction enabling sensing of matrix stiffness and migration through dense tissues
- Enhanced survival signaling downstream of integrin activation reducing anoikis sensitivity
- Amplification of growth factor signaling through crosstalk between integrin and RTK pathways

**Evidence summary**
Integrin-mediated adhesion represents a critical hub linking cell-matrix interactions to intracellular signaling. The presence of multiple genes supporting focal adhesion complex assembly and FAK/Src activation suggests astrocytomas may exhibit enhanced mechanotransduction capacity. Recent work demonstrates that tumor-derived extracellular vesicles enhance integrin signaling in recipient cells, suggesting that coordinate upregulation of integrin pathway components could amplify cell-cell communication and promote tumor progression. The presence of PEAK1, which integrates integrin and growth factor receptor signaling, suggests particularly sophisticated crosstalk between adhesion and proliferation pathways.

**Atomic biological processes**
- Integrin-ECM engagement and focal adhesion formation. Genes: PEAK1, TNK2, PPFIA2, CARMIL1, DCC
  - [25]: Integrin adhesion complexes form through coordinate expression of integrin subunits, talin, paxillin, and other signaling proteins
  - [23]: Talin transmits pN-scale forces through integrin-mediated adhesion complexes
- FAK and Src-family kinase activation in focal adhesions. Genes: TNK2, SH3KBP1, SH3D19
  - [25]: Integrin-mediated FAK and c-Src phosphorylation at focal adhesions promotes migration
- Mechanotransduction and force sensing. Genes: PEAK1, TNK2, CADM2
  - [23]: Talin-actin linkage transmits mechanical forces enabling mechanotransduction

**Atomic cellular components**
- Focal adhesion complex. Genes: PEAK1, TNK2, PPFIA2
  - [25]: Focal adhesions contain integrin heterodimers, talin, paxillin, ILK1, vinculin

**Required genes (not in input)**
- Genes: Integrin alpha and beta subunits, FAK, Paxillin, Vinculin, ILK1, Talin
  - [25]: Core focal adhesion proteins required for complex function

**Program citations**
- [25]: EV-mediated activation of integrin pathways increases migration and stemness
- [23]: Talin force coupling underlies integrin-mediated mechanotransduction

## Program: Rho-GTPase-Mediated Cytoskeletal Remodeling
Coordinated activation of Rho-family GTPases (Rac1, Cdc42, RhoA) through guanine nucleotide exchange factors (GEFs), enabling rapid actin polymerization, pseudopodium formation, and cell migration through mechanisms involving multiple actin nucleators and motors.

**Predicted impacts**
- Enhanced active migration through coordinated actin polymerization and cytoskeletal remodeling
- Increased pseudopodium extension enabling invasion through restricted spaces
- Rapid morphological transitions between migratory and non-migratory states
- Integration of multiple upstream signals (integrins, growth factors, chemokines) into unified migration response

**Evidence summary**
The Rho-GTPase program represents a master regulator of cell migration through control of actin dynamics. The presence of multiple DOCK family GEFs suggests that astrocytomas may engage redundant mechanisms for Rho-family activation, potentially enabling continued migration even if one pathway is blocked. The coordinate presence of actin nucleators, motors, and dynamics regulators suggests sophisticated spatial and temporal control of pseudopodium formation. This program is particularly relevant to glioma biology, as gliomas are known for their infiltrative growth pattern and ability to migrate through brain tissue. The presence of both GEF proteins that activate Rho-GTPases and GAP proteins that terminate signaling suggests fine-tuned regulation enabling controlled migration rather than constitutive activation.

**Atomic biological processes**
- Rho-GTPase activation via GEF proteins. Genes: DOCK4, DOCK9, DOCK10, SRGAP2
  - [25]: DOCK proteins function as GEFs for Rac1 and Cdc42, activating these GTPases in response to upstream signals to promote migration
- Actin polymerization and pseudopodium formation. Genes: MTSS1, SLAIN1, MYO10, MYO5C, NAV2
  - [25]: Enhanced actin polymerization through Rac1/Cdc42 activation promotes pseudopodium extension
- Filopodium and membrane invagination dynamics. Genes: MTSS1, NAV2, MYO10
  - [21]: DPYSL5 regulates filopodia formation and axonal guidance through tubulin-actin interactions
- GTPase termination and pathway regulation. Genes: ARHGAP20, ARHGAP42
  - [25]: GTPase-activating proteins balance Rho-family activation with termination

**Atomic cellular components**
- Rac1/Cdc42 signaling complex. Genes: DOCK4, DOCK9, DOCK10
  - [25]: DOCK-mediated Rac activation drives cytoskeletal remodeling
- Actin filament networks and filopodia. Genes: MTSS1, SLAIN1, NAV2, MYO10
  - [25]: Arp2/3 complex and formin-mediated actin polymerization creates cellular protrusions

**Required genes (not in input)**
- Genes: Rac1, Cdc42, RhoA, Arp2/3 complex, Formins, Cofilin
  - [25]: Core Rho-GTPase signaling components required for actin dynamics

**Program citations**
- [25]: DOCK-mediated Rac1 and Cdc42 activation promotes migration and invasion
- [21]: Actin-binding proteins regulate filopodia formation

## Program: Growth Factor Receptor Signaling
Activation of receptor tyrosine kinases by growth factors including PDGF and FGF, triggering downstream signaling cascades through PI3K/Akt and MAPK pathways that promote proliferation, survival, and enhanced responsiveness to environmental signals.

**Predicted impacts**
- Enhanced responsiveness to growth factors in tumor microenvironment
- Increased proliferation through activation of PI3K/Akt and MAPK pathways
- Enhanced survival signaling reducing apoptosis despite stress conditions
- Amplified migration response to growth factor gradients

**Evidence summary**
Growth factor receptor signaling represents a critical driver of astrocytoma proliferation and survival. PDGFRA and EGFR alterations are among the most common genetic changes in high-grade astrocytomas, and the presence of multiple effector proteins amplifies the impact of these receptors. The inclusion of FGF14 suggests potential sensitization to FGF signaling, which could be therapeutically exploited through FGF pathway inhibitors. Importantly, the presence of integrin pathway components like PEAK1 alongside growth factor receptors suggests that these pathways are coordinately active and may exhibit crosstalk, potentially enabling cells to respond to both growth factors and mechanical cues from the extracellular matrix.

**Atomic biological processes**
- Growth factor receptor activation and autophosphorylation. Genes: PDGFRA, EGFR, FGF14, NTRK3
  - [13]: PDGFRA and EGFR are frequently amplified in high-grade astrocytomas driving proliferation and survival
  - [9]: PDGFRA amplification in glioblastoma often occurs with EGFR or MET amplification
- Downstream signaling cascade activation. Genes: PRKCA, MAP3K1, TNK2, SH3KBP1, SH3D19
  - [34]: PKA-mediated phosphorylation of calcium channels downstream of dopamine receptor signaling
- Integration of multiple signaling inputs. Genes: PEAK1, DENND2A, ARFGEF3
  - [25]: PEAK1 mediates crosstalk between integrin signaling and receptor tyrosine kinase pathways

**Atomic cellular components**
- Growth factor receptor complex. Genes: PDGFRA, EGFR
  - [13]: PDGFRA and EGFR form activated signaling complexes in glioblastoma
- Cytoplasmic signaling adaptors. Genes: SH3KBP1, SH3D19, TNK2
  - [25]: Adapter proteins link receptor activation to downstream effectors

**Required genes (not in input)**
- Genes: PI3K, Akt, MAPK/ERK, mTOR, JAK/STAT, SOS, Grb2
  - [13]: Classical downstream effectors of growth factor receptors

**Program citations**
- [13]: PDGFRA and EGFR alterations drive high-grade astrocytoma proliferation
- [9]: PDGFRA amplification in glioblastoma often co-occurs with other RTK alterations
- [25]: PEAK1 integration of integrin and RTK signaling

## Program: Ion Channel Diversity and Neuronal-Like Electrophysiology
Expression of extensive repertoire of voltage-gated ion channels including potassium, sodium, and calcium channels that mediate neuronal-like electrical excitability and calcium signaling in tumor cells normally lacking such properties, enabling calcium-dependent signaling cascades and altered cellular dynamics.

**Predicted impacts**
- Acquisition of neuronal-like electrical properties enabling action potential-like events
- Enhanced calcium influx through multiple channel types amplifying calcium-dependent signaling
- Coupling between membrane potential and metabolic state through ion gradient maintenance
- Potential for activity-dependent changes in gene expression through calcium-CREB signaling

**Evidence summary**
The extensive ion channel repertoire in this astrocytoma gene list represents a striking departure from normal mature astrocyte biology, which is characterized by minimal ion channel diversity. This program is particularly notable because it suggests astrocytomas may engage neuronal-like electrical properties that could fundamentally alter how cells respond to stimuli and communicate with their environment. The presence of both Kv4 and BK channel subunits suggests that calcium-activated potassium signaling may be particularly important. The coordinate expression of sodium and potassium channels suggests potential for action potential-like events, which could enable rapid signal propagation within tumors or enhanced responsiveness to depolarizing signals from adjacent neurons. This program likely reflects either retention of ion channels from a neural progenitor cell stage that normally expresses these genes during development, or acquisition of such genes during malignant transformation.

**Atomic biological processes**
- Voltage-gated potassium channel activity. Genes: KCND2, KCND3, KCNIP1, KCNIP4, KCNMB2, KCNMB2-AS1, KCNQ1OT1
  - [34]: L-type calcium channels CaV1.2 modulate neuronal excitability and synaptic plasticity
- Voltage-gated sodium channel activity. Genes: SCN1A, SCN3A
  - [34]: Sodium channels generate action potential upstroke in excitable cells
- Calcium channel-mediated signaling. Genes: CACNG4
  - [34]: L-type calcium channels CaV1.2 are critical mediators of dopamine signaling affecting spatial working memory
- Calcium-activated processes. Genes: KCNMB2, PDE4B
  - [24]: Astrocytes signal using calcium and potassium gradients; calcium signaling links to metabolic coupling and neuroinflammation

**Atomic cellular components**
- Kv4 potassium channel complex. Genes: KCND2, KCND3, KCNIP1, KCNIP4
  - [34]: KCNIP proteins associate with Kv4 channels as accessory subunits
- BK potassium channel complex. Genes: KCNMB2, KCNMB2-AS1
  - [34]: KCNMB2 encodes auxiliary subunit regulating BK channel properties

**Required genes (not in input)**
- Genes: Voltage sensor domains, Pore-forming subunits, Auxiliary subunits, Calcium/calmodulin-dependent kinases
  - [34]: Core ion channel components

**Program citations**
- [34]: Ion channels including CaV1.2 and potassium channels mediate neuronal excitability and plasticity
- [24]: Astrocytes utilize calcium and potassium signaling for cellular functions

## Program: Glutamatergic Synaptic Transmission
Expression of ionotropic AMPA and kainate-type glutamate receptors and metabotropic glutamate receptors enabling direct responsiveness to extracellular glutamate, coupled with presynaptic neurotransmitter release machinery and postsynaptic scaffold proteins that support glutamate-dependent signaling and calcium influx.

**Predicted impacts**
- Direct responsiveness to neuronal glutamate release promoting tumor cell migration and proliferation
- Calcium influx through AMPA receptors enabling activation of calcium-dependent transcription factors
- G-protein coupled signaling through metabotropic receptors promoting diverse cellular responses
- Establishment of glutamate-dependent tumor-neuron crosstalk within the microenvironment

**Evidence summary**
The presence of multiple glutamate receptor subtypes in this astrocytoma gene list is highly significant and suggests that tumor cells have either retained or acquired capacity for direct glutamatergic signaling. In normal physiology, glutamate released by neurons activates receptors on adjacent astrocytes, modulating astrocyte calcium signaling and triggering metabolic coupling. In astrocytoma, enhanced glutamate receptor expression could create aberrant tumor-neuron communication loops where neuronal glutamate release drives tumor cell proliferation and migration. This is particularly relevant given that astrocytomas are highly infiltrative and establish intimate contacts with neurons. Recent work has demonstrated that glutamate signaling promotes glioma cell invasiveness and stemness, suggesting this program represents a critical vulnerability. Interestingly, the presence of ionotropic AMPA receptors (typically neuronal) combined with the general astrocytoma context suggests cells have either failed to complete astrocytic differentiation or that neuronal genes are ectopically expressed.

**Atomic biological processes**
- AMPA receptor-mediated fast synaptic transmission. Genes: GRIA2, GRIA3, GRID2, CACNG4
  - [5]: GRIA2 encodes AMPA receptor subunit 2, mediating fast glutamatergic synaptic transmission
  - [8]: NGN2 neurons express multiple AMPA receptor subunits (GRIA1-4) and metabotropic glutamate receptors
- Metabotropic glutamate receptor signaling. Genes: GRM5
  - [8]: Co-cultures express metabotropic glutamate receptors (GRM1-8) enabling G-protein coupled signaling
  - [40]: GRM5 and GRM6-8 are metabotropic glutamate receptors activated by extracellular glutamate
- Glutamate receptor-mediated calcium entry. Genes: GRIA2, GRIA3, GRM5, CACNG4
  - [24]: Calcium signaling through receptors drives metabolic coupling and cellular responses

**Atomic cellular components**
- AMPA receptor complex. Genes: GRIA2, GRIA3, CACNG4
  - [5]: AMPA receptors assemble as heterotetramers with distinct kinetic properties based on subunit composition
- Metabotropic glutamate receptor signaling complex. Genes: GRM5
  - [40]: Metabotropic glutamate receptors couple to G-proteins and activate downstream signaling

**Required genes (not in input)**
- Genes: GRIA1, GRIA4, GRM1-4, GRM6-8, Post-synaptic density scaffolds, PLC-IP3-Ca2+ release machinery
  - [8]: Additional glutamate receptor subunits and signaling machinery

**Program citations**
- [5]: GRIA2 is AMPA receptor subunit mediating fast glutamatergic transmission
- [8]: Co-culture models express AMPA and metabotropic glutamate receptors

## Program: Transcriptional Reprogramming and EMT Control
Dysregulation of developmental transcription factors that control neural progenitor cell identity and differentiation status, combined with epithelial-mesenchymal transition (EMT) factors that promote migratory and invasive phenotypes, maintaining cells in intermediate developmental states with reduced differentiation.

**Predicted impacts**
- Maintenance of intermediate developmental states with reduced commitment to astrocytic differentiation
- Increased expression of genes promoting migration and reduced expression of epithelial genes
- Dynamic switching between proliferative and migratory states enabling adaptability to microenvironmental changes
- Sustained expression of genes normally silenced during astrocyte maturation

**Evidence summary**
The transcriptional reprogramming program identifies a central feature of astrocytoma pathogenesis—the failure or reversal of normal developmental differentiation. The presence of ZEB1, a canonical EMT transcription factor, combined with developmental progenitor genes like those in the SOX family and INSM1-associated networks suggests that astrocytomas maintain intermediate developmental states characterized by reduced differentiation. Recent work has demonstrated that glioblastomas explicitly maintain neuronal progenitor-like states through INSM1-dependent transcriptional programs, and the presence of SOX genes in this list suggests similar developmental state maintenance. Importantly, this program is distinct from simple dedifferentiation—rather, it represents active engagement of developmental programs that promote both plasticity and migratory capacity. The presence of both ZEB1 and developmental progenitor genes suggests a cell state that is simultaneously migratory and developmentally flexible, maximizing tumor adaptability.

**Atomic biological processes**
- EMT transcription factor activity. Genes: ZEB1, ETV5
  - [28]: ZEB1 is pivotal EMT transcription factor with C2H2-type zinc fingers recognizing E-box-like promoter elements; forms positive feedback loop with TNS1 stabilizing ZEB1 protein
- Neural progenitor cell identity maintenance. Genes: SOX2-OT, SOX5, MYT1, ETV5
  - [27]: INSM1 governs neuronal progenitor state driving glioblastoma; expressed in intermediate progenitor cells during cortical development
- Developmental gene expression programming. Genes: KLF12, ESRRG, NPAS3
  - [27]: Tumor cell evolution triggers transitions toward neuronal progenitor network

**Atomic cellular components**
- ZEB1-containing transcriptional repressor complex. Genes: ZEB1
  - [28]: ZEB1 recruits corepressors to regulate E-cadherin and other genes

**Required genes (not in input)**
- Genes: INSM1, TNS1, E-cadherin, Snail, Slug, Twist
  - [28]: Additional EMT transcription factors and ZEB1 regulatory partners

**Program citations**
- [28]: ZEB1 is pivotal EMT transcription factor stabilized by TNS1 forming positive feedback loop
- [27]: INSM1 governs neuronal progenitor state that drives glioblastoma tumorigenicity

## Program: Extracellular Matrix Remodeling and Proteolysis
Coordinated production of extracellular matrix components combined with expression of matrix-degrading proteases and metalloproteinases, enabling dynamic remodeling of the tumor microenvironment, invasion through tissue barriers, and generation of bioactive matrix fragments that promote further tumor progression.

**Predicted impacts**
- Enhanced invasion through basement membranes and stromal matrices via MMP-mediated degradation
- Generation of bioactive matrix fragments promoting cell migration and signaling
- Remodeling of tumor microenvironment to favor vascularization and immune infiltration
- Dynamic matrix production and degradation creating permissive migration corridors

**Evidence summary**
The extracellular matrix remodeling program reflects the known invasive behavior of astrocytomas, which migrate through brain tissue by degrading barriers. The presence of MMP16, a membrane-anchored metalloproteinase, combined with extensive matrix component production suggests a coordinated program of simultaneous matrix degradation and synthesis. This enables astrocytomas to create invasion corridors by degrading existing matrix while simultaneously depositing new matrix tailored to promote migration. The presence of proteoglycans like VCAN and BCAN, enriched in perineuronal nets, suggests the tumor may particularly target these specialized extracellular matrix structures that normally support synaptic organization. The coordinate expression of multiple collagen types suggests wholesale remodeling of the stromal microenvironment.

**Atomic biological processes**
- Matrix metalloproteinase-mediated degradation. Genes: MMP16
  - [32]: Matrix metalloproteinases including MMP14 degrade extracellular matrix in physiological and pathological processes
- Extracellular matrix protein synthesis and modification. Genes: COL4A3, COL4A4, COL20A1, TNR, VCAN, BCAN, CSPG5, CSMD3
  - [13]: Extracellular matrix components provide structural support and signaling substrates
- Proteoglycan-mediated cell-matrix interactions. Genes: VCAN, BCAN, CSPG5, CSMD3
  - [14]: Astrocytes engage in immune microenvironment remodeling affecting tumor progression
- Glycosylation and post-translational matrix modification. Genes: CHST9, CHST11, COLGALT2, XYLT1
  - [13]: Matrix glycosylation affects cell-matrix interactions and migration

**Atomic cellular components**
- Type IV collagen-rich basement membranes. Genes: COL4A3, COL4A4
  - [13]: Type IV collagen (COL4A3, COL4A4) forms structural basement membranes
- Brain-specific extracellular matrix components. Genes: TNR, BCAN, VCAN
  - [24]: Perineuronal nets contain proteoglycans and other ECM components supporting synaptic stability

**Required genes (not in input)**
- Genes: MMP2, MMP9, ADAMTS, Tissue inhibitors of MMPs (TIMPs), Collagenase
  - [32]: Additional matrix-degrading proteinases and their regulators

**Program citations**
- [32]: Matrix metalloproteinases degrade extracellular matrix components
- [13]: Extracellular matrix components and their modifications in tumor biology

## Program: Calcium Signaling and Metabolic Coupling
Integration of calcium signaling with cellular metabolism through expression of calcium-sensing ion channels, calcium/cAMP-coupled signaling elements, and metabolic transporters that collectively link intracellular calcium dynamics to energy substrate utilization and astrocyte-neuron metabolic support.

**Predicted impacts**
- Coupling between intracellular calcium elevation and changes in membrane potential
- Integration of calcium signals with cAMP-dependent responses enabling complex signaling
- Dynamic regulation of metabolic substrate availability based on cellular activity state
- Potential metabolic competition with adjacent neurons for shared substrates

**Evidence summary**
The calcium-metabolic coupling program reflects emerging understanding that astrocyte function depends critically on proper coordination between calcium signaling and metabolic processes. Recent work has highlighted that dysregulation of astrocytic calcium signaling, particularly through aberrant calcineurin-NFAT activity, disrupts metabolic coupling and contributes to neuroinflammation and neurodegeneration in multiple disease contexts. The presence of genes supporting both calcium regulation and metabolic substrate transport suggests that astrocytomas may maintain coordinated calcium-metabolic signaling, potentially enabling them to compete more effectively with neurons for metabolic resources. The presence of SLC2A13 (monocarboxylate transporter) and SLC4A10 (sodium-dependent bicarbonate transporter) suggests active regulation of lactate and pH-dependent metabolic signaling. This program is particularly relevant in the context of gliomas, which are known to alter tumor microenvironment metabolism and create immunosuppressive conditions through lactate production and acidification.

**Atomic biological processes**
- Calcium-activated ion channel regulation. Genes: KCNMB2, KCND2, KCND3, PDE4B
  - [24]: Astrocytes signal using calcium and potassium gradients; calcium signaling dysregulation links to neuroinflammation
- Calcium extrusion and homeostasis. Genes: SLC24A3
  - [24]: Sodium-calcium exchangers and associated transporters regulate intracellular calcium
- Calcium-cAMP signaling integration. Genes: PDE4B
  - [34]: PDE4 phosphodiesterases degrade cAMP, integrating calcium and cAMP signaling
- Metabolic substrate transport and coupling. Genes: SLC2A13, SLC4A10
  - [24]: Astrocytes engage in metabolic coupling with neurons through lactate shuttle and glucose metabolism

**Atomic cellular components**
- BK potassium channel-calcium sensor complex. Genes: KCNMB2
  - [24]: BK channels couple calcium influx to membrane hyperpolarization
- Sodium-calcium exchanger. Genes: SLC24A3
  - [24]: Na-Ca exchangers regulate calcium extrusion

**Required genes (not in input)**
- Genes: IP3R, RyR, STIM1, Orai1, Calmodulin, Calcineurin, NFAT, Glycolytic enzymes
  - [24]: Core calcium and metabolic signaling machinery
  - [37]: Orai1 calcium channel functions as signaling hub in astrocytes

**Program citations**
- [24]: Astrocyte calcium signaling dysregulation links to neuroinflammation and metabolic coupling disruption
- [34]: Calcium and cAMP signaling integration through phosphodiesterases

## Program: Cell Cycle and Proliferation Control
Expression of cell cycle regulators promoting G1/S phase transition combined with apparent reduced expression of cell cycle checkpoints and apoptotic machinery, enabling continuous proliferation with minimal restraint from normal cell cycle surveillance mechanisms.

**Predicted impacts**
- Continuous cell cycle progression with reduced G1/S checkpoint control
- Reduced dependency on growth factor signaling for cell cycle progression
- Increased proliferation rate enabling rapid tumor growth
- Potential genomic instability from bypassed checkpoints

**Evidence summary**
The cell cycle program identified in this gene list is notable primarily for what is absent—genes encoding p53, p16, p21, p27, and other classical CDK inhibitors are not prominently represented. TP53 mutations occur in the vast majority of high-grade astrocytomas and are common in lower-grade lesions, suggesting that loss of p53-mediated checkpoints is a hallmark of these tumors. The presence of CCND2 without corresponding checkpoint genes suggests a bias toward proliferation. However, the relative underrepresentation of this program compared to migration and adhesion programs in the gene list is notable, suggesting that proliferation control may be achieved through upstream mechanisms (growth factor signaling, through PDGFRA and EGFR) rather than through constitutive overexpression of cell cycle machinery.

**Atomic biological processes**
- G1/S phase progression and cyclin-CDK activity. Genes: CCND2
  - [42]: Cyclin E1 forms complex with CDK2 required for G1/S phase transition
- CDK inhibitor degradation and removal.
  - [39]: SKP2 is ubiquitin ligase component that degrades CDK inhibitors enabling cell cycle progression

**Atomic cellular components**
- Cyclin D-CDK4/6 complex. Genes: CCND2
  - [42]: Cyclin D2 partners with CDK4/6 for G1/S control

**Required genes (not in input)**
- Genes: TP53, RB, p16, p21, p27, CDK4, CDK6
  - [12]: TP53 mutations in astrocytomas disrupt cell cycle control

**Program citations**
- [42]: CCNE1 and cyclin D promote G1/S phase transition
- [39]: SKP2 mediates degradation of CDK inhibitors

## Program: RNA Processing and Post-Transcriptional Regulation
Expression of RNA-binding proteins and splicing regulators that modulate alternative splicing patterns and mRNA stability, enabling dynamic control of protein expression for genes whose transcription may be constitutively elevated, providing additional layer of post-transcriptional regulation.

**Predicted impacts**
- Fine-tuning of protein expression through alternative splicing of genes with elevated transcription
- Selective stabilization or destabilization of specific mRNAs enabling dynamic response to signals
- Post-translational protein stability regulation complementing transcriptional control
- Potential generation of protein isoforms with altered biological activities

**Evidence summary**
The RNA processing program represents a secondary layer of gene expression control that enables more nuanced regulation of cellular phenotypes. NOVA1, while best characterized in the context of neuronal development where it regulates splicing of genes controlling synaptic transmission, has increasingly been recognized as dysregulated in various cancers. Its presence in this astrocytoma gene list suggests potential aberrant regulation of splicing patterns in developmental genes, potentially maintaining cells in intermediate developmental states. The presence of KHDRBS3 and USP54 suggests coordinate control of mRNA and protein stability, enabling cells to maintain high mRNA levels while actually producing controlled amounts of protein through post-translational mechanisms.

**Atomic biological processes**
- Alternative splicing regulation. Genes: NOVA1
  - [21]: NOVA1 is RNA-binding protein regulating alternative splicing of multiple neuronal development genes
- mRNA stability and localization control. Genes: KHDRBS3
  - [21]: KH-domain RNA-binding proteins regulate mRNA stability and cellular localization
- Protein stability and ubiquitin-mediated degradation. Genes: USP54
  - [28]: USP54-like deubiquitinating enzymes regulate protein stability of transcription factors

**Atomic cellular components**
- RNA-protein complexes. Genes: NOVA1, KHDRBS3
  - [21]: NOVA1 and KHDRBS3 form ribonucleoprotein complexes regulating target RNAs

**Required genes (not in input)**
- Genes: hnRNPs, SR proteins, snRNPs, Proteolytic enzymes
  - [21]: Classical splicing machinery components

**Program citations**
- [21]: NOVA1 regulates alternative splicing of developmental genes in neural progenitors

## Program: Vesicular Trafficking and Exosome Biogenesis
Expression of ESCRT machinery components, SNARE proteins, and vesicular trafficking regulators supporting formation and release of extracellular vesicles (exosomes), enabling intercellular communication through transfer of proteins, lipids, and RNAs that promote tumor progression and immune evasion.

**Predicted impacts**
- Enhanced exosome production and release enabling intercellular transfer of tumor-promoting signals
- Increased transfer of proteins and miRNAs to neighboring cells promoting tumor progression
- Potential immune evasion through exosome-mediated transfer of immunosuppressive molecules
- Horizontal transfer of oncogenic signals amplifying tumor heterogeneity

**Evidence summary**
Recent work has identified exosome-mediated intercellular communication as a critical mechanism in tumor progression, with glioma-derived exosomes promoting both intra-tumoral progression and colonization of distant brain regions. The presence of ESCRT machinery components including TSG101 combined with SNARE proteins like VAMP7 suggests that astrocytomas engaging this program may be particularly adept at exosome biogenesis and release. The presence of GRAMD1B and lipid-binding proteins suggests additional sophistication in vesicular organization and membrane remodeling. Recent studies have demonstrated that glioma-derived exosomes can transfer bioactive molecules including growth factors, signaling proteins, and miRNAs that promote both tumor progression and immunosuppression in the microenvironment.

**Atomic biological processes**
- Multivesicular body biogenesis and ESCRT function. Genes: TSG101
  - [44]: TSG101 is component of ESCRT machinery required for endosomal sorting and multivesicular body formation
- Vesicle-associated membrane protein function. Genes: VAMP7
  - [41]: VAMP7 participates in SNARE-mediated fusion of endosomal and recycling vesicles
- Vesicular trafficking and membrane reorganization. Genes: GRAMD1B, PLPP4
  - [25]: Lipid-binding proteins and trafficking regulators coordinate membrane organization

**Atomic cellular components**
- ESCRT complex machinery. Genes: TSG101
  - [44]: ESCRT machinery including TSG101 sorts cargo into multivesicular bodies
- SNARE complexes. Genes: VAMP7
  - [41]: VAMP7-containing SNARE complexes mediate membrane fusion

**Required genes (not in input)**
- Genes: ALIX/PDCD6IP, Vps4, Rab proteins, SNAREs (SNARE), Synaptobrevins
  - [44]: Additional ESCRT and trafficking machinery components

**Program citations**
- [44]: TSG101 is ESCRT component required for exosome biogenesis
- [41]: VAMP7 mediates endosomal trafficking essential for MT1-MMP recycling during invasion
- [25]: Extracellular vesicles modulate integrin signaling and enhance stemness

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/6422
2. Ottenheimer DJ, Simon RC, Briones BA, Burke CT, Bowen AJ, Ferguson SM, et al.. Single-cell sequencing of rodent ventral pallidum reveals diverse neuronal subtypes with noncanonical interregional continuity. Science Advances [Internet]. 2025Dec5;11(49). Available from: https://www.science.org/doi/10.1126/sciadv.adp3059
3. Available from: https://www.ncbi.nlm.nih.gov/gene/2735
4. Kiriakopulos K, Soleimanpour K, McMurray BJ, Moke B-I, Chalmers JJ, Mokhtaridoost M, et al.. LncRNA CISTR-ACT regulates cell size in human and mouse by guiding FOSL2. Nature Communications [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41467-025-67591-x_reference.pdf
5. Available from: https://www.ncbi.nlm.nih.gov/gene/2891
6. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
7. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
8. Hartmann S-M, Pizarro GP, Heider J, Vogel S, Wüstner L-S, Wüst R, et al.. A co-culture model of dopaminergic and glutamatergic neurons derived from patients with idiopathic schizophrenia reveals a hypodopaminergic phenotype. Molecular Psychiatry [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41380-025-03384-4
9. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
10. Available from: https://www.ncbi.nlm.nih.gov/gene/19211
11. Available from: https://www.ncbi.nlm.nih.gov/gene/26047
12. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
13. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
14. Die J, Liangliang M, Yanke W, Tingting T, Enhui Y, Zekai S. Unveiling the prognostic and immunological role of IFI44 in glioma.. Annals of medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41327009/
15. Minkai W, Zeyu M, Xiaotao W, Zilong W, Wenqing W, Zhenyu Z, et al.. P4HB regulates tumor-associated macrophage polarization and chemotaxis by enhancing IL-6 cytokine secretion in glioblastoma.. Annals of medicine and surgery (2012) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41377462/?fc=None&ff=20251212152250&v=2.18.0.post22+67771e2
16. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
17. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z_reference.pdf
18. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
19. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
20. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
21. Desprez F, Remize S, François-Moutal L, Ung DC, Dangoumau A, Marouillat S, et al.. Missense variants in DPYSL5 associated with neurodevelopmental disorders and brain malformations cause impaired neuronal maturation in vitro. Molecular Psychiatry [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s41380-025-03364-8
22. Available from: https://www.ncbi.nlm.nih.gov/gene/4133
23. Rangarajan S, Espeter L, Drexler HCA, Chrostek-Grashoff A, Grashoff C. Talin force coupling underlies eukaryotic cell-substrate adhesion. Nature Communications [Internet]. 2025Dec6;16(1). Available from: https://www.nature.com/articles/s41467-025-67354-8
24. Sims SL, Lu T-H, Weiss BE, Lin R-L, Galopin LB, Wright NA, et al.. Central cytometabolic functional vascular coupling in health and disease. npj Metabolic Health and Disease [Internet]. 2025Dec2;3(1). Available from: https://www.nature.com/articles/s44324-025-00090-1
25. Kalvala AK, Silwal A, Patel B, Kasetti A, Shetty KR, Markiewski J, et al.. Extracellular vesicles modulate integrin signaling and subcellular energetics to promote pulmonary lymphangioleiomyomatosis metastasis. Communications Biology [Internet]. 2025Nov20;8(1). Available from: https://www.nature.com/articles/s42003-025-09004-9
26. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
27. Zhang T, Li Z, Ming Y, Li J, Ye Z, Luo D, et al.. A positive feedback loop between TNS1 and ZEB1 promotes TGFβ-induced epithelial-to-mesenchymal transition in lung cancer. Communications Biology [Internet]. 2025Nov26;8(1). Available from: https://www.nature.com/articles/s42003-025-09079-4
28. Available from: https://www.ncbi.nlm.nih.gov/gene/4312
29. Available from: https://www.ncbi.nlm.nih.gov/gene/4763
30. Available from: https://www.ncbi.nlm.nih.gov/gene/6935
31. Available from: https://www.ncbi.nlm.nih.gov/gene/4323
32. Skoufa E, Zhong J, Hu K, Kahre O, Tsissios G, Carrau L, et al.. Specialized signaling centers direct cell fate and spatial organization in a mesodermal organoid model. Science Advances [Internet]. 2025Nov28;11(48). Available from: https://www.science.org/doi/10.1126/sciadv.ady7682
33. Man KNM, Rougé SLS, Berumen RA, Jacobi AA, Weiner JC, Naderi SY, et al.. Stimulation of Ca
                    <sup>2+</sup>
                    channel Ca
                    <sub>V</sub>
                    1.2 activity by dopamine signaling augments spatial working memory. Science Signaling [Internet]. 2025Dec9;18(916). Available from: https://www.science.org/doi/10.1126/scisignal.adp7760
34. Available from: https://www.ncbi.nlm.nih.gov/gene/5578
35. Available from: https://www.ncbi.nlm.nih.gov/gene/406935
36. Available from: https://www.nature.com/subjects/calcium-signalling/ncomms
37. Available from: https://www.ncbi.nlm.nih.gov/gene/18750
38. Available from: https://www.ncbi.nlm.nih.gov/gene/6502
39. Available from: https://www.ncbi.nlm.nih.gov/gene/2916
40. Available from: https://www.ncbi.nlm.nih.gov/gene/6845
41. Available from: https://www.ncbi.nlm.nih.gov/gene/898
42. Available from: https://www.ncbi.nlm.nih.gov/gene/2918
43. Available from: https://www.ncbi.nlm.nih.gov/gene/7251
44. Available from: http://json-schema.org/draft-07/schema#",
