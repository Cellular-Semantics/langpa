# Gene Program Markdown Report

## Context
- Cell type: astrocytes
- Disease: astrocytoma
- Tissue: brain

## Input Genes
CFI, SNTG1, PLEKHG1, PRKD1, ETV6, ADAMTS14, SCN1A, EPHA3, SLC1A2, ADCY2, COL8A1, TNIK, LINC01993, TPST1, STOX1, GLI3, GRIA1, GRIK3, GRIN2B, HS3ST3B1, KLHDC8A, LINC00511, LINC01122, IFI16, ILDR2, ... (200 total)

## Program: Cell Adhesion and Junction Organization
Multi-component program regulating cell-cell adhesive contacts through cadherin-catenin complexes, protocadherin-mediated homophilic interactions, and immunoglobulin domain-containing adhesion receptors. Normal astrocyte physiology relies on robust adhesion-dependent cell-cell contacts to establish network integrity; dysregulation of this program during astrocytoma transformation reduces contact inhibition and facilitates epithelial-to-mesenchymal-like transition, enabling increased motility and invasion.

**Predicted impacts**
- Enhanced motility and reduced contact-dependent growth inhibition
- Increased invasive capacity and matrix degradation
- Loss of epithelial-like architectural organization
- Transition toward mesenchymal-like cellular state
- Disrupted astrocyte-astrocyte network formation

**Evidence summary**
The cadherin-catenin adhesion complex represents a central nexus of adhesion-dependent signaling in astrocytes. Multiple input genes encode critical components including CDH2 (N-cadherin), CTNNA3 (α-catenin), and scaffold proteins PARD3/PARD3B. During normal astrocyte physiology, these proteins maintain robust cell-cell contacts and epithelial-like architecture. In astrocytoma, coordinated downregulation or mutation of adhesion genes drives loss of epithelial properties, permitting transition to migratory phenotype. The planar cell polarity pathway component PRICKLE2 further modulates migration through Wnt signaling. Evidence demonstrates that E-cadherin loss correlates with progression in low-grade astrocytomas, establishing adhesion complex dysregulation as a fundamental driver of invasion.

**Atomic biological processes**
- Adherens junction assembly and maintenance. Genes: CDH2, CTNNA3, PCDH9, PARD3, PARD3B
  - [12]: E-cadherin-mediated cell-cell adhesion loss occurs in low-grade astrocytomas, facilitating invasive phenotype transition
  - [59]: PARD3 organizes adherens junctions and coordinates cell polarity through recruitment of polarity complexes
- Homophilic cell recognition and synaptic adhesion. Genes: CADM1, NRCAM, ILDR2, NTM
  - [59]: NRCAM and NTM participate in homophilic and heterophilic interactions establishing neural tissue architecture and synaptic stability
- Planar cell polarity and collective cell migration. Genes: PRICKLE2, PARD3B
  - [59]: PRICKLE2 acts as component of planar cell polarity pathway influencing cell migration through Wnt signaling modulation

**Atomic cellular components**
- Cadherin-catenin complex. Genes: CDH2, CTNNA3
  - [12]: Cadherin-catenin complex loss in astrocytomas represents fundamental shift toward invasive phenotype
- Adherens junction scaffold. Genes: PARD3, PARD3B, PDZRN3
  - [59]: PARD3/PARD3B serve as molecular scaffolds organizing adherens junctions and tight junctions

**Required genes (not in input)**
- Genes: CDH1, CTNNB1, E-cadherin
  - [12]: E-cadherin encoded by CDH1 is primary adhesion molecule showing altered expression in astrocytomas, though many N-cadherin components present

**Program citations**
- [12]: Direct evidence of E-cadherin loss in low-grade astrocytoma with functional consequences for invasion
- [59]: Comprehensive evidence of PARD3, PARD3B, PRICKLE2 roles in junction organization and migration

## Program: Neuronal Ion Channel and Glutamate Homeostasis
Program governing astrocytic regulation of extracellular ion concentration and synaptic glutamate clearance through expression of glutamate transporters and ion channels. SLC1A2 encodes the primary glutamate reuptake transporter essential for terminating synaptic transmission. Multiple glutamate receptor subunits and voltage-gated ion channels dysregulated in this program enable altered calcium signaling during tumor transformation, supporting aberrant proliferation and metabolic rewiring.

**Predicted impacts**
- Altered synaptic glutamate clearance affecting neuron-astrocyte crosstalk
- Enhanced calcium-dependent proliferation through glutamate receptor activation
- Dysregulated extracellular ion homeostasis
- Aberrant calcium signaling supporting metabolic rewiring
- Potential acquisition of neuronal-like excitability properties

**Evidence summary**
Astrocytes maintain critical bidirectional communication with neurons through regulation of extracellular ion homeostasis and neurotransmitter clearance. SLC1A2 represents the primary mechanism for glutamate reuptake, essential for terminating synaptic transmission and preventing excitotoxicity. The input list includes multiple glutamate receptor subunits (GRIA1, GRIK3, GRIN2B) typically recognized as neuronal but increasingly recognized in glial physiology and tumor signaling. Voltage-gated sodium channel SCN1A and potassium channel KCND3 participate in astrocyte excitability. In glioma cells, altered expression of ion channels promotes aberrant calcium signaling and enhanced proliferative capacity. The convergence of multiple ion channel genes suggests dysregulation of electrolyte and neurotransmitter homeostasis machinery during astrocytoma transformation.

**Atomic biological processes**
- Glutamate reuptake and excitotoxicity prevention. Genes: SLC1A2
  - [33]: SLC1A2 encodes the principal glutamate transporter clearing excitatory amino acids from synapses
  - [30]: SLC1A2 expression altered in Down syndrome astrocytes with enhanced glutamate uptake capacity
- Astrocytic calcium signaling and integration. Genes: GRIA1, GRIK3, GRIN2B, KCND3, SCN1A
  - [59]: Ion channel dysregulation in glioma cells promotes aberrant calcium signaling and enhanced proliferative capacity
- Ephrin-Eph receptor signaling in glial development. Genes: EPHA3
  - [59]: EphA3 implicated in glioma progression through bidirectional signaling with ephrin ligands

**Atomic cellular components**
- Glutamate transporter complex. Genes: SLC1A2
  - [33]: SLC1A2 forms membrane-bound protein complex as principal transporter clearing excitatory amino acids
- Ionotropic glutamate receptor subunits. Genes: GRIA1, GRIK3, GRIN2B
  - [59]: AMPA, kainate, and NMDA receptor subunits participate in synaptic transmission and activity-dependent plasticity

**Required genes (not in input)**
- Genes: GLAST, GLT1, GluA2, NR1, Kv1.1
  - [33]: Alternative nomenclature for key glutamate and ion channel components important for complete pathway function

**Program citations**
- [33]: SLC1A2 encodes glutamate transporter with essential roles in synaptic transmission termination
- [30]: SLC1A2 expression dysregulation documented in pathological astrocyte states
- [59]: Comprehensive evidence of ion channel dysregulation in glioma

## Program: Axon Guidance and Neuronal Differentiation
Developmental program regulating neuronal migration, axonal outgrowth, synaptic connectivity, and the maintenance of neuronal progenitor states. Semaphorin family guidance molecules SEMA3A and SEMA3E regulate axonal patterning. Extracellular matrix proteases ADAMTS remodel the perineuronal matrix enabling plasticity. Transcriptional regulators maintain neural progenitor identity. In astrocytoma, acquisition of developmental progenitor-like states via dysregulation of this program drives functional plasticity and tumor maintenance.

**Predicted impacts**
- Acquisition of intermediate progenitor-like transcriptional programs
- Enhanced neuronal-like properties including neurite extension
- Dysregulated matrix-dependent cell migration
- Altered growth factor availability through matrix remodeling
- Maintained self-renewal capacity and reduced differentiation

**Evidence summary**
The semaphorin family of axon guidance molecules including SEMA3A and SEMA3E regulate neuronal migration, axonal outgrowth, and synaptic connectivity during development. SEMA3A suppresses tumor progression via downregulation of Lin28B, suggesting that loss of semaphorin signaling may promote astrocytoma malignancy. The extracellular matrix proteases ADAMTS6, ADAMTS9-AS2, and ADAMTS14 remodel the perineuronal matrix, essential for synaptic plasticity and, in tumoral contexts, facilitating invasion. SULF1 modifies heparan sulfate proteoglycans controlling growth factor bioavailability. The transcription factor NPAS3 regulates developmental programs including neuronal migration. Critically, SOX2-OT and INSM1 participate in maintenance of neural progenitor states; recent studies demonstrate that glioblastoma cells exploit developmental progenitor programs for tumor maintenance, with INSM1-driven transitions toward intermediate progenitor-like states functionally important in glioblastoma pathogenesis.

**Atomic biological processes**
- Semaphorin-mediated axon guidance and migration. Genes: SEMA3A, SEMA3E
  - [18]: SEMA3A suppresses tumor progression via downregulation of Lin28B
  - [21]: SEMA3A expression inhibits axon guidance through neuropilin-plexin interaction
- Matrix metalloproteinase-mediated neurite remodeling. Genes: ADAMTS6, ADAMTS9-AS2, ADAMTS14
  - [2]: ADAMTS family members cleave versican, aggrecan enabling matrix remodeling essential for cell migration and synaptic plasticity
- Neuronal progenitor state maintenance. Genes: SOX2-OT, NPAS3, INSM1
  - [3]: INSM1 drives transition toward neuronal progenitor state in glioblastoma tumorigenesis
  - [36]: INSM1 highly expressed in glioblastoma and intermediate progenitor cells during cortical development
  - [59]: NPAS3 regulates neuronal migration and synaptic plasticity during cortical development
- Heparan sulfate proteoglycan-mediated signaling regulation. Genes: SULF1
  - [25]: SULF1 modifies heparan sulfate proteoglycan structure controlling growth factor bioavailability and axon guidance signaling

**Atomic cellular components**
- Synaptic adhesion complex. Genes: NXPH1, NRCAM, NTM
  - [59]: Neurexophilin, NRCAM and neurotrimin participate in homophilic and heterophilic trans-synaptic adhesion
- Perineuronal matrix proteoglycan scaffold. Genes: ADAMTS6, ADAMTS14, SULF1
  - [2]: ADAMTS proteases remodel extracellular matrix proteoglycans essential for synaptic plasticity

**Required genes (not in input)**
- Genes: INSM1, SOX2, PLXND1, NRP1
  - [3]: INSM1 and SOX2 transcription factors central to progenitor state maintenance, though SOX2-OT lncRNA present
  - [36]: PLXND1 and NRP1 neuropilin-plexin receptors required for semaphorin signaling

**Program citations**
- [3]: INSM1 knockdown disrupts oncogenic function and inhibits in vivo tumorigenicity in glioblastoma models
- [36]: INSM1 highly expressed in glioblastoma, driving intermediate progenitor network supporting tumor plasticity
- [2]: ADAMTS proteases drive matrix remodeling in pediatric high-grade gliomas

## Program: Kinase Signaling Cascade and Proliferation
Multi-component program coordinating cell proliferation, migration, and metabolic state transitions through serine-threonine kinases and tyrosine kinases. PRKD1 regulates protein secretion and cytoskeletal dynamics. PRKCA participates in growth factor signaling cascades. MAP3K14 activates non-canonical NF-κB signaling relevant to stromal remodeling. NUAK1 and NEK6 coordinate cell cycle progression. Enhanced kinase signaling activity during astrocytoma transformation supports rapid proliferation and phenotypic plasticity characteristic of malignant progression.

**Predicted impacts**
- Enhanced proliferative capacity and G1/S phase transition
- Increased protein secretion supporting tumor-stromal interactions
- Enhanced migratory and invasive phenotype
- Metabolic adaptation to support rapid growth
- Altered centrosome dynamics enabling chromosomal instability

**Evidence summary**
Multiple serine-threonine kinases coordinate astrocyte proliferation, migration, and metabolic state transitions. PRKD1 integrates downstream of phospholipase C and calcium signaling with emerging roles in regulating epithelial-to-mesenchymal transition balance. PRKCA participates in multiple signaling cascades including those downstream of PDGF receptor activation, which is a critical driver of pediatric high-grade gliomas. The mitogen-activated protein kinase kinase kinase MAP3K14 activates non-canonical NF-κB signaling, with potential roles in stromal remodeling and immune regulation within the tumor microenvironment. NUAK1 regulates energy metabolism and cell polarity during migration. NEK6 coordinates cell cycle progression and centrosome dynamics. The kinase program collectively enables enhanced proliferative signaling, metabolic adaptation, and phenotypic plasticity characteristic of astrocytic tumors.

**Atomic biological processes**
- Protein kinase D-mediated cytoskeletal regulation. Genes: PRKD1
  - [59]: PRKD1 regulates protein secretion, cytoskeletal dynamics, and cellular migration through phosphorylation of myosin light chain kinase and cofilin
- Protein kinase C signaling in growth factor responses. Genes: PRKCA
  - [17]: PRKCA participates in signaling cascades downstream of PDGF receptor activation
- Non-canonical NF-κB pathway activation. Genes: MAP3K14
  - [39]: MAP3K14 activates non-canonical NF-κB signaling with roles in stromal remodeling and immune regulation
- AMPK-related energy sensing and cell polarity. Genes: NUAK1
  - [59]: NUAK1 AMPK-related kinase regulates energy metabolism and cell polarity during migration
- Cell cycle and centrosome dynamics. Genes: NEK6
  - [59]: NEK6 nima-related kinase coordinates cell cycle progression and centrosome dynamics

**Atomic cellular components**
- Serine-threonine kinase complexes. Genes: PRKD1, PRKCA, NUAK1, NEK6
  - [59]: Multiple serine-threonine kinases coordinate proliferation and migration signaling

**Required genes (not in input)**
- Genes: ERK1/2, AKT, mTORC1
  - [6]: Downstream MAPK and PI3K/AKT effectors frequently hyperactivated in astrocytomas

**Program citations**
- [17]: PRKCA and PDGFRA signaling central to pediatric high-grade glioma pathogenesis
- [59]: Comprehensive evidence of kinase roles in cell cycle, migration, and metabolism

## Program: Phosphatase Signaling and Feedback Control
Program encompassing protein tyrosine phosphatases and lipid phosphatases that provide negative feedback on growth factor signaling and maintain signaling homeostasis. PTPRZ1 maintains specialized glycosylation controlling catalytic activity. PTPRT, PTPRJ, PTPRG, and PTPN9 dephosphorylate receptor tyrosine kinases. PTEN antagonizes PI3K signaling as a critical tumor suppressor. Dysregulation of this program removes brakes on proliferative signaling, particularly PI3K/AKT pathway hyperactivation characteristic of astrocytomas.

**Predicted impacts**
- Hyperactivation of PI3K/AKT signaling upon PTEN loss
- Enhanced proliferation through mTORC1 pathway
- Increased survival signaling and reduced apoptosis
- Metabolic rewiring supporting rapid growth
- Resistance to growth inhibitory signals

**Evidence summary**
The protein tyrosine phosphatase receptor PTPRZ1 maintains a specialized glycosylation signature in brain tissue controlling its catalytic activity, with dysregulation promoting glioma growth. PTPRT, PTPRJ, PTPRG, and PTPN9 encode additional phosphatases that dephosphorylate and inactivate receptor tyrosine kinases, serving as negative feedback regulators of growth factor signaling. PTEN, the critical phosphatidylinositol-3,4,5-trisphosphate phosphatase, antagonizes PI3K signaling; loss of PTEN expression or mutation occurs in approximately 30-40% of glioblastomas and promotes hyperactivation of AKT-mediated signaling. Notably, PTEN mutations cooperate with TP53 and ATRX mutations to block differentiation of neural stem cells via repression of SOX2. The coordinated activity of kinases and phosphatases maintains signaling homeostasis; dysregulation of this balance, particularly through PTEN loss, removes critical brakes on proliferative signaling.

**Atomic biological processes**
- Receptor tyrosine phosphatase-mediated signal attenuation. Genes: PTPRZ1, PTPRT, PTPRJ, PTPRG, PTPN9
  - [31]: PTPRZ1 maintains brain-specific glycosylation controlling catalytic activity in glioma
- Phosphatidylinositol-3-phosphate hydrolysis and PI3K antagonism. Genes: PTEN
  - [8]: PTEN phosphatase antagonizes PI3K signaling with loss in approximately 30-40% of glioblastomas
- Phospholipase C-mediated second messenger generation. Genes: PLCB4, PLCE1, PLCH1, PLCG2
  - [32]: Phospholipase C enzymes generate inositol-1,4,5-trisphosphate and diacylglycerol second messengers
- Phospholipid D-mediated membrane dynamics. Genes: PLD5
  - [52]: Phosphatidic acid-generating PLD participates in membrane dynamics and cytoskeletal organization

**Atomic cellular components**
- Protein tyrosine phosphatase catalytic domain. Genes: PTPRZ1, PTPRT, PTPRJ
  - [31]: Receptor protein tyrosine phosphatases contain extracellular and catalytic intracellular domains
- PI3K/AKT regulatory checkpoint. Genes: PTEN
  - [8]: PTEN functions as critical negative regulator of phosphatidylinositol-3,4,5-trisphosphate

**Required genes (not in input)**
- Genes: PI3K, AKT, mTORC1, TSC1/TSC2
  - [8]: Downstream PI3K/AKT/mTOR pathway components essential for understanding PTEN's tumor-suppressive function

**Program citations**
- [8]: PTEN loss frequency and functional consequences in glioblastoma well-established
- [3]: PTEN cooperates with TP53 and ATRX in neural stem cell transformation
- [31]: PTPRZ1 dysregulation in glioma pathogenesis

## Program: Growth Factor Receptor Signaling and MAPK Pathway
Program governing growth factor-dependent proliferation through receptor tyrosine kinase activation and downstream MAPK pathway signaling. PDGFRA represents one of the most frequently altered genes in pediatric high-grade gliomas with activating mutations and amplifications. PDGFC and PDGFRL encode alternative ligands and co-receptors. TGFBR2 participates in complex signaling with both tumor-suppressive and tumor-promoting roles. Dysregulation of this program through PDGFRA activation or BRAF fusion-driven MAPK signaling drives proliferation independent of multiple growth factor inputs.

**Predicted impacts**
- Constitutive MAPK/ERK pathway activation through PDGFRA oncogenic mutations
- Enhanced proliferation independent of exogenous growth factors
- Metabolic reprogramming supporting rapid tumor growth
- Dysregulated TGF-beta signaling affecting immune cell infiltration
- Increased angiogenesis through VEGF-independent mechanisms

**Evidence summary**
PDGFRA, encoding the alpha isoform of the platelet-derived growth factor receptor, represents one of the most frequently altered genes in pediatric high-grade gliomas. Activating PDGFRA mutations or amplifications drive tumorigenesis independent of additional genetic hits in some contexts, demonstrating its sufficiency as a driver oncogene in brain tumors. PDGFC and PDGFRL encode alternative ligands and co-receptors in the PDGF signaling pathway; PDGFRL may modulate PDGFRA signaling intensity. TGFBR2 participates in both tumor-suppressive and tumor-promoting signaling depending on cellular context and downstream effectors. Recent CAR T cell therapy approaches employ multiplex genetic disruption of TGFBR2 alongside other immunosuppressive barriers to enhance anti-tumor activity. The convergent dysregulation of multiple growth factor pathways, including PDGFRA amplification, BRAF fusion, and NF1 loss, characterizes pediatric gliomas.

**Atomic biological processes**
- PDGF receptor-mediated proliferation signaling. Genes: PDGFRA, PDGFC, PDGFRL
  - [6]: PDGFRA mutations and amplifications represent major oncogenic drivers of pediatric high-grade gliomas
  - [17]: PDGFRa signaling essential for cardiac fibroblast maintenance and constitutively active PDGFRA sufficient driver in mouse models
- TGF-beta receptor signaling and immune regulation. Genes: TGFBR2
  - [29]: TGFBR2 participates in complex tumor-suppressive and tumor-promoting signaling depending on cellular context
  - [26]: CAR T cell therapy employs multiplex genetic disruption of TGFBR2 to overcome immunosuppression
- Parathyroid hormone receptor signaling and calcium homeostasis. Genes: PTH2R
  - [59]: PTH2R may participate in calcium-dependent signaling relevant to tumor metabolism
- Oncostatin M-mediated tumor-stromal interactions. Genes: OSMR
  - [59]: OSMR coordinates cytokine signaling relevant to tumor-stromal interactions

**Atomic cellular components**
- Platelet-derived growth factor receptor complex. Genes: PDGFRA, PDGFRL
  - [17]: PDGFRA and PDGFRL form ligand-activated receptor tyrosine kinase complexes
- TGF-beta signaling complex. Genes: TGFBR2
  - [29]: TGFBR2 associates with ligand and type I receptor to activate downstream signaling

**Required genes (not in input)**
- Genes: BRAF, NF1, RAF1, MEK1/2, ERK1/2
  - [1]: BRAF fusion frequency in pilocytic astrocytomas; RAF1 present but BRAF not in input list
  - [42]: RAF1 promotes MAPK signaling; downstream MEK/ERK components essential for full pathway function

**Program citations**
- [6]: PDGFRA as potent driver of gliomagenesis with frequent oncogenic alterations
- [2]: Patient-derived tumoroids preserve PDGFRA alterations with maintained driver functions
- [26]: TGFBR2 as therapeutic target in solid tumor immunotherapy

## Program: Transcriptional Regulation and Developmental Progenitor State
Program governing transcriptional control of cell fate specification, proliferation-differentiation balance, and maintenance of neural progenitor identity through transcription factors and chromatin regulators. ETV1 and ETV6 regulate genes involved in proliferation and differentiation. RFX4 participates in developmental gene regulation. ARID5B, PRDM16, and DPF3 control chromatin accessibility and histone modifications. SOX2-OT lncRNA participates in progenitor state maintenance. This program enables dysregulated acquisition and maintenance of intermediate progenitor-like cellular states in astrocytomas.

**Predicted impacts**
- Dysregulated proliferation-differentiation balance favoring proliferation
- Maintenance of progenitor-like transcriptional state
- Reduced expression of differentiation-associated genes
- Enhanced stemness and self-renewal capacity
- Aberrant developmental program activation in tumor context

**Evidence summary**
ETV1 and ETV6 encode members of the ETS family of transcription factors regulating genes involved in proliferation, differentiation, and cell migration. ETV6 serves as a constraint on transcriptional activity of fusion proteins in certain malignancies, with potential analogous roles in regulating fusion-driven gliomas. RFX4 participates in transcriptional regulation of developmental genes. ARID5B, PRDM16, and DPF3 control chromatin accessibility and histone modifications essential for establishing transcriptional landscapes. SOX2-OT, the long non-coding RNA overlapping SOX2, participates in the maintenance of neural progenitor states. Critically, recent studies demonstrate that intermediate progenitor cell-like states driven by transcription factor INSM1 are functionally important in glioblastoma pathogenesis. INSM1 is highly expressed in human glioblastoma tumors and, during cortical development, in intermediate progenitor cells. While INSM1 is not directly present in the input list, multiple input genes including SOX2-OT, NPAS3, and RFX4 regulate developmental transcriptional programs that establish and maintain progenitor-like states.

**Atomic biological processes**
- ETS transcription factor-mediated proliferation control. Genes: ETV1, ETV6
  - [14]: ETV6 constrains transcriptional activity of fusion proteins; ETV1 associated with tumorigenesis
- Regulatory factor X-mediated developmental gene expression. Genes: RFX4
  - [59]: RFX4 encodes regulatory factor X participating in transcriptional regulation of developmental genes
- Chromatin accessibility and histone modification control. Genes: ARID5B, PRDM16, DPF3
  - [24]: ARID5B implicated in chromatin accessibility and nucleosome positioning
  - [28]: PRDM16 participates in chromatin-mediated transcriptional repression and developmental fate specification
  - [59]: DPF3 serves as subunit of histone deacetylase complexes removing activating marks
- Neural progenitor state maintenance via long non-coding RNA. Genes: SOX2-OT
  - [59]: SOX2-OT lncRNA participates in maintenance of neural progenitor state
- Intermediate progenitor transcriptional programming. Genes: NPAS3
  - [3]: INSM1-mediated transition toward intermediate progenitor state functionally important in glioblastoma
  - [36]: NPAS3 regulates neuronal migration and developmental programs during cortical development

**Atomic cellular components**
- ETS transcription factor DNA-binding domain. Genes: ETV1, ETV6
  - [14]: ETS family members bind conserved ETS binding sites in promoter regions
- Histone deacetylase complex. Genes: DPF3
  - [59]: DPF3 associates with HDAC to remove activating acetylation marks

**Required genes (not in input)**
- Genes: SOX2, INSM1, TBR2, NEUROG2
  - [3]: SOX2 and INSM1 transcription factors critical for progenitor state, though SOX2-OT present
  - [36]: TBR2 and NEUROG2 intermediate progenitor markers not present in input list

**Program citations**
- [3]: INSM1 knockdown disrupts oncogenic function and inhibits tumorigenicity, indicating functional importance of progenitor-like state
- [36]: Comprehensive evidence of INSM1-mediated intermediate progenitor state in glioblastoma
- [14]: ETV6 regulatory roles in transcriptional control

## Program: Cytoskeletal Remodeling and Cell Migration
Program coordinating actin and microtubule network reorganization essential for cell migration and morphological changes during astrocytoma invasion. FMN2 initiates linear actin filament assembly. PARD3/PARD3B organize polarized cytoskeletal elements. DTNA stabilizes cortical actin. Myosin motors MYO5B, MYO1E, and MYO16 power cellular movements. PRICKLE2 participates in planar cell polarity signaling regulating coordinated migration. Dysregulation enables enhanced motility and invasive capacity characteristic of malignant astrocytomas.

**Predicted impacts**
- Enhanced cell migration and invasion capacity
- Increased filopodial extension and membrane protrusions
- Dysregulated contact inhibition allowing collective migration
- Altered cell morphology from epithelial to fibroblastoid
- Support for blood vessel invasion and perivascular migration

**Evidence summary**
Cell migration during astrocytoma invasion requires coordinated reorganization of actin and microtubule networks. FMN2 encodes formin 2, an actin nucleator that initiates linear actin filament assembly essential for filopodial protrusions and cell migration. PARD3 and PARD3B organize polarized distribution of cytoskeletal elements, with PARD3 functioning as a key component of the par polarity complex. DTNA encodes dystrophin, an actin-associated protein that stabilizes the cortical actin cytoskeleton at the plasma membrane. MYO5B, MYO1E, and MYO16 encode myosin motors that power cellular movements and transport along actin filaments. MYBPC1 encodes a myosin-binding protein C that modulates myosin motor kinetics. PRICKLE2 participates in planar cell polarity signaling, a conserved developmental pathway regulating coordinated cell migration. The convergence of multiple actin-regulating genes suggests enhanced motility and invasive capacity during astrocytoma progression.

**Atomic biological processes**
- Actin filament nucleation and polymerization. Genes: FMN2
  - [59]: FMN2 formin nucleates linear actin filament assembly essential for filopodial protrusions
- Cortical actin stabilization and plasma membrane anchoring. Genes: DTNA
  - [59]: DTNA dystrophin stabilizes cortical actin cytoskeleton at plasma membrane
- Myosin motor-powered cellular movements. Genes: MYO5B, MYO1E, MYO16, MYBPC1
  - [59]: Myosin motors power cellular movements and transport along actin filaments
- Planar cell polarity and coordinated migration. Genes: PRICKLE2, PARD3, PARD3B
  - [59]: Planar cell polarity pathway regulates coordinated cell migration and tissue elongation
- Microtubule dynamics in neuronal migration. Genes: DCLK2
  - [59]: DCLK2 doublecortin-like kinase participates in microtubule dynamics during migration

**Atomic cellular components**
- Linear actin filament. Genes: FMN2
  - [59]: FMN2 initiates formation of linear actin filaments through formin catalysis
- Cortical actin network. Genes: DTNA, PARD3
  - [59]: Dystrophin and PARD3 organize cortical actin network architecture
- Myosin motor complexes. Genes: MYO5B, MYO1E, MYO16, MYBPC1
  - [59]: Myosin motors associate with actin filaments to generate force

**Required genes (not in input)**
- Genes: RAC1, CDC42, WASP, Arp2/3
  - [59]: RAC1, CDC42 GTPases and WASP/Arp2/3 complexes essential for actin nucleation but not in input

**Program citations**
- [59]: Comprehensive evidence of cytoskeletal regulation in cell migration

## Program: Synaptic Plasticity and Neuron-Astrocyte Communication
Program mediating bidirectional astrocyte-neuron interactions through synaptic adhesion molecules, neurotransmitter receptors, and synaptic plasticity regulators. NLGN4X encodes neuroligin participating in trans-synaptic adhesion. NRXN3 encodes neurexin as presynaptic partner. NXPH1 and NTM participate in synaptic stabilization. PCP4 associates with postsynaptic density. In astrocytoma context, expression of these neuronal genes may reflect acquisition of progenitor-like properties or enhanced expression supporting tumor-neuron crosstalk promoting neuroinflammation.

**Predicted impacts**
- Aberrant expression of neuronal adhesion molecules in tumor cells
- Enhanced neuro-immune signaling and neuroinflammation
- Potential acquisition of neuronal-like synaptic properties
- Altered neurotransmitter responsiveness
- Modified astrocyte-neuron communication supporting tumor growth

**Evidence summary**
The input gene list includes multiple components of the synaptosomal proteome, suggesting potential roles in mediating astrocyte-neuron crosstalk or, in the context of astrocytoma, potentially reflecting aberrant adoption of neuronal-like properties by tumor cells. NLGN4X encodes a neuronal member of the neuroligin adhesion molecule family coordinating trans-synaptic adhesion. NRXN3 encodes neurexin-3, a presynaptic adhesion molecule binding neuroligins to organize synaptic architecture. GRIN2B and GRIA1 encode subunits of ionotropic glutamate receptors with established roles in synaptic transmission and activity-dependent plasticity. GRIK3 encodes a kainate receptor subunit involved in fast synaptic transmission. NTM and NXPH1 participate in synaptic stabilization through homophilic and heterophilic interactions. PCP4 encodes a Purkinje cell protein associating with the postsynaptic density potentially modulating glutamate receptor trafficking. These genes collectively reflect the nervous system context in which astrocytes reside; however, their expression in astrocytic tumors suggests potential acquisition of neuronal-like properties or enhanced expression of genes supporting astrocyte-neuron communication.

**Atomic biological processes**
- Trans-synaptic adhesion and synapse organization. Genes: NLGN4X, NRXN3, NXPH1, NTM
  - [59]: Neuroligin, neurexin, neurexophilin, and neurotrimin coordinate trans-synaptic adhesion and synapse stability
- Postsynaptic density organization. Genes: PCP4
  - [59]: PCP4 associates with postsynaptic density and modulates glutamate receptor trafficking
- Ionotropic glutamate receptor function. Genes: GRIN2B, GRIA1, GRIK3, NETO2
  - [59]: NMDA, AMPA, and kainate receptor subunits mediate fast synaptic transmission

**Atomic cellular components**
- Synaptic cleft adhesion complex. Genes: NLGN4X, NRXN3
  - [59]: Neuroligin-neurexin trans-synaptic pair organizes synaptic structure
- Postsynaptic density protein scaffold. Genes: PCP4
  - [59]: PCP4 serves as component of postsynaptic density protein assembly

**Required genes (not in input)**
- Genes: PSD95, SAP102, Homer1, PICK1
  - [59]: Postsynaptic density scaffolding proteins essential for glutamate receptor organization

**Program citations**
- [59]: Comprehensive evidence of synaptic components involved in trans-synaptic signaling

## Program: Extracellular Matrix Remodeling and Invasion
Program governing degradation and remodeling of extracellular matrix surrounding astrocytes, facilitating cell invasion, angiogenesis, and immune infiltration during astrocytoma progression. A2M functions as general protease inhibitor. ADAMTS family members cleave matrix proteoglycans. COL8A1 encodes basement membrane collagen. F3 encodes fibronectin providing migration scaffold. P3H2 modifies collagen structure. The convergent dysregulation of matrix remodeling genes enables increased degradation of basement membrane and interstitial matrix supporting malignant invasion.

**Predicted impacts**
- Increased matrix protein degradation enabling invasion
- Reduced basement membrane integrity facilitating vascular invasion
- Enhanced angiogenesis through matrix remodeling
- Increased immune cell infiltration into tumor
- Perivascular migration of tumor cells along blood vessels

**Evidence summary**
The extracellular matrix surrounding astrocytes undergoes profound remodeling during glioma progression, both supporting tumor growth and facilitating invasion. A2M encodes alpha-2-macroglobulin serving as a general protease inhibitor binding and inactivating multiple proteases, thereby regulating matrix turnover and growth factor bioavailability. ADAMTS6, ADAMTS9-AS2, and ADAMTS14 encode ADAMTS family members that cleave versican, aggrecan, and other matrix proteoglycans, thereby driving matrix remodeling essential for cell migration. COL8A1 encodes type VIII collagen found in basement membranes; dysregulation of basement membrane composition facilitates tumor cell invasion. F3 encodes fibronectin providing a scaffold for cell migration and integrin-mediated signaling. P3H2 encodes prolyl 3-hydroxylase 2 participating in collagen modification and crosslinking. FHIT functions as a tumor suppressor through sensing of accumulated adenosine nucleotides and triggering of apoptosis in response to DNA damage; FHIT expression is frequently lost in malignancies including gliomas.

**Atomic biological processes**
- Matrix metalloproteinase-mediated matrix degradation. Genes: ADAMTS6, ADAMTS9-AS2, ADAMTS14
  - [2]: ADAMTS family members cleave versican, aggrecan, and other proteoglycans driving matrix remodeling
- Protease inhibition and extracellular matrix stability. Genes: A2M
  - [59]: Alpha-2-macroglobulin serves as general protease inhibitor regulating matrix turnover
- Basement membrane composition and structure. Genes: COL8A1
  - [59]: Type VIII collagen found in basement membranes; dysregulation facilitates tumor cell invasion
- Fibronectin-mediated cell migration scaffold. Genes: F3
  - [59]: Fibronectin provides scaffold for cell migration and integrin-mediated signaling
- Collagen modification and matrix crosslinking. Genes: P3H2
  - [59]: Prolyl 3-hydroxylase participates in collagen modification and crosslinking
- Tumor suppressor function and apoptosis induction. Genes: FHIT
  - [47]: FHIT functions as tumor suppressor through sensing accumulated nucleotides and triggering apoptosis

**Atomic cellular components**
- Metalloproteinase ADAMTS catalytic domain. Genes: ADAMTS6, ADAMTS14
  - [2]: ADAMTS metalloproteinases contain catalytic domains cleaving matrix proteins
- Basement membrane proteoglycan network. Genes: COL8A1
  - [59]: Basement membrane contains collagen network providing structural support

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP1, TIMP2
  - [2]: Classic matrix metalloproteinases MMP2/9 and their TIMP inhibitors important for matrix remodeling

**Program citations**
- [2]: ADAMTS proteases drive matrix remodeling in pediatric high-grade gliomas
- [47]: FHIT loss in gliomas and functional consequences

## Program: Metabolic Flexibility and Tumor Microenvironment Adaptation
Program coordinating metabolic rewiring enabling tumor cells to switch between glycolysis and oxidative phosphorylation, supporting survival in hostile microenvironmental conditions including hypoxia and nutrient deprivation. Mitochondrial protein SUCLG2 regulates oxidative phosphorylation. HBEGF promotes growth and immune evasion. AXL receptor coordinates growth factor and immune signaling. NAMPT catalyzes NAD+ biosynthesis. PDE enzymes regulate cyclic nucleotide signaling. OXR1 provides antioxidant protection. This metabolic flexibility represents a critical adaptation enabling astrocytoma cells to resist metabolic stress and therapy.

**Predicted impacts**
- Enhanced survival in hypoxic and nutrient-deprived microenvironments
- Metabolic switching between glycolysis and OXPHOS supporting therapy resistance
- Increased NAD+ availability supporting DNA repair and genomic stability
- Reduced reactive oxygen species accumulation protecting against oxidative stress
- Enhanced immune evasion through AXL-mediated signaling
- Resistance to metabolic stress-induced cell death

**Evidence summary**
Recent evidence indicates that glioblastoma cells exhibit metabolic flexibility, dynamically switching between glycolysis and oxidative phosphorylation to survive therapeutic stress. The mitochondrial protein SUCLG2 interacts with LMNA to regulate oxidative phosphorylation capacity; knockdown of SUCLG2 suppresses glioblastoma proliferation by impairing mitochondrial function and lactate metabolism. HBEGF, a heparin-binding epidermal growth factor, promotes glioblastoma initiation, proliferation, and invasion via EGFR and AXL signaling. AXL encodes a receptor tyrosine kinase participating in both growth factor signaling and immune evasion through interaction with ligand TIM4 expressed by macrophages. NAMPT catalyzes the first committed step in NAD+ biosynthesis from nicotinamide, essential for maintaining energy charge and supporting DNA repair processes. PDE4D and PDE1C encode phosphodiesterases that degrade cyclic nucleotides, thereby reducing PKA and Epac signaling intensity. OXR1 encodes oxidation resistance protein 1 participating in antioxidant responses protecting against reactive oxygen species. These metabolic regulators collectively enable astrocytoma cells to adapt to the hostile tumor microenvironment and resist metabolic stress during therapy.

**Atomic biological processes**
- Oxidative phosphorylation and mitochondrial metabolism. Genes: SUCLG2
  - [52]: SUCLG2 knockdown suppresses glioblastoma proliferation by impairing mitochondrial function and lactate metabolism
- Growth factor signaling and immune evasion. Genes: HBEGF, AXL
  - [49]: HBEGF promotes glioblastoma initiation, proliferation, and invasion via EGFR and AXL signaling
  - [34]: AXL receptor tyrosine kinase participates in growth factor signaling and immune evasion
- NAD+ biosynthesis and energy homeostasis. Genes: NAMPT
  - [49]: NAMPT catalyzes first committed step in NAD+ biosynthesis essential for energy charge and DNA repair
- Cyclic nucleotide signaling modulation. Genes: PDE4D, PDE1C
  - [59]: Phosphodiesterases degrade cyclic nucleotides reducing PKA and Epac signaling intensity
- Reactive oxygen species defense. Genes: OXR1
  - [59]: OXR1 encodes oxidation resistance protein participating in antioxidant responses
- Immune cell infiltration regulation. Genes: PSEN1
  - [49]: PSEN1 expresses involvement in immune responses and cell chemotaxis

**Atomic cellular components**
- Mitochondrial oxidative phosphorylation machinery. Genes: SUCLG2
  - [52]: SUCLG2 associates with mitochondrial membrane proteins regulating respiratory chain
- Growth factor receptor signaling complex. Genes: HBEGF, AXL
  - [49]: HBEGF ligand binds EGFR and AXL receptors activating downstream signaling

**Required genes (not in input)**
- Genes: HIF1A, LDHA, PKM2, MTOR
  - [55]: HIF1A, LDHA, PKM2 encode key glycolytic enzymes; mTOR central metabolic checkpoint

**Program citations**
- [52]: SUCLG2 demonstrates direct metabolic control of glioblastoma proliferation through mitochondrial function
- [55]: Metabolic flexibility and OXPHOS switching demonstrated in tumor radiotherapy resistance
- [49]: Comprehensive immune and metabolic gene interactions in tumor microenvironment

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
2. 2. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
3. 3. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/546
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/6469
6. 6. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/5728
9. 9. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/12355/
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/19211
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/24842
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/999
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/2130
15. 15. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/21803
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/10371
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/3428
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/207
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/20346
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/3456
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/57650
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/100130776
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
26. 26. Murray R, Chowdhury MR, Botticello-Romero NR, Desai K, Chilakapati SR, Chong B, et al.. Multiplex gene-editing strategy to engineer allogeneic EGFR-targeting CAR T-cells with improved efficacy against solid tumors. Nature Communications [Internet]. 2025Nov23;. Available from: https://www.nature.com/articles/s41467-025-66737-1
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/6304
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/79923
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/7048
30. 30. André LTES, Pedro HP de O, Bruno YY-M, Jéssica da SF, Jonatan PA, Helder IN, et al.. Complement pathway dysregulation and astrocyte alterations in Down syndrome: evidence from postmortem brain tissue and iPSC-derived astrocytes.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41350900/?fc=None&ff=20251210050700&v=2.18.0.post22+67771e2
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/5803
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/23236
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/6506
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/558
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/2767
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
37. 37. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
38. 38. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/5894
40. 40. Yuan Y, Yue Q, Wang Y, Du Z, Wang X, Yan F, et al.. AI-augmented intraoperative decision-making workflows in diffuse midline glioma biopsy using cryosection pathology. Nature Communications [Internet]. 2025Nov26;. Available from: https://www.nature.com/articles/s41467-025-66853-y
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/51147
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/406921
43. 43. Launspach M, Macos J, Afzal S, Hohmann J, Appis ML, Pilgram M, et al.. Personalized CRISPR knock-in cytokine gene therapy to remodel the tumor microenvironment and enhance CAR T cell therapy in solid tumors. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-67328-w
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/11197
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
46. 46. Li R, Han Q, Zeng T, Wen B, Zheng Z, Bao X, et al.. Machine learning identifies inflammation-related diagnostic biomarkers for primary myelofibrosis with clinical validation. Scientific Reports [Internet]. 2025Nov20;15(1). Available from: https://www.nature.com/articles/s41598-025-24756-4
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/672
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/20878
49. 49. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/2237
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/11799
52. 52. Liu Z, Lim S-H, Jung S. Targeting tumor metabolic flexibility enhances radiotherapeutic efficacy via mitochondrial complex I Inhibition in an intracranial S180 sarcoma mouse model. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-29326-2
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/3265
54. 54. Wang S, Jiang T, Wang T, Yang Z, Wang T, Zhang X, et al.. CMKLR1/PKA signaling reinforces sonic hedgehog pathway to promote medulloblastoma pathogenesis. Oncogenesis [Internet]. 2025Nov17;14(1). Available from: https://www.nature.com/articles/s41389-025-00582-1
55. 55. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/283131
57. 57. Available from: https://www.ncbi.nlm.nih.gov/gene/2737
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/406952
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/60674
60. 60. Available from: http://json-schema.org/draft-07/schema#",
