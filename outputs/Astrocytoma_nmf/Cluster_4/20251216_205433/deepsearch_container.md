# Gene Program Markdown Report

## Context
- Cell type: astrocytoma tumor cells (derived from glial lineage with neuronal differentiation features)
- Disease: astrocytoma (WHO grades I-IV diffuse astrocytic gliomas)
- Tissue: brain, particularly cerebral cortex and white matter tracts

## Input Genes
ALCAM, GALNT13, DNM3, ADGRL3, MIR181A2HG, SH3D19, NOVA1, GRIK2, GRIA2, GLCCI1, MAP2, ARPP21, PCDH15, FAM110B, EGFR, MAML2, SNTG1, OR4N2, CSMD3, RAB27B, KLRC2, SOX6, AL353784.1, AL512308.1, AC002069.2, ... (200 total)

## Program: Glutamatergic and GABAergic Neurotransmitter Signaling
This program encompasses ionotropic glutamate receptors (AMPA, kainate, delta receptors), GABA-A receptors, and associated regulatory proteins that establish functional synaptic transmission in astrocytoma cells. These components enable tumor cells to respond to neurotransmitters in the microenvironment and establish neuron-tumor synaptic contacts. Expression of calcium-permeable AMPA receptors (GRIA2, GRIA4) supports intracellular calcium elevation and downstream survival signaling.

**Predicted impacts**
- Enhanced intracellular calcium signaling supporting tumor cell proliferation and survival
- Formation of functional synaptic contacts with peritumoral neurons
- Aberrant neuronal activity in tumor microenvironment, potential seizure susceptibility
- Metabolic coupling with neurons through neurotransmitter exchange

**Evidence summary**
Recent transcriptomic studies of glioblastoma identified neuronal marker expression in specific tumor cell subpopulations, with GRIA2 and other glutamate receptor subunits showing elevated expression in some glioma samples[54][70]. The presence of complete ionotropic receptor machinery in tumor cells suggests functional synaptic competence. Glutamate released by tumor cells activates AMPA receptors on peritumoral neurons, driving aberrant firing and contributing to seizure activity in approximately 30-40% of supratentorial glioma patients[70].

**Atomic biological processes**
- ionotropic glutamate receptor trafficking and localization. Genes: GRIA2, GRIA4, GRIK2, DPP6, LHFPL3, NXPH1
  - [34]: Describes GluA1 CTD-dependent AMPAR trafficking and subcellular localization in different cell types
- calcium signaling through ionotropic glutamate receptors. Genes: GRIA2, GRIA4, GRIK2, GRID2, CACNA1A, SLC8A3
  - [70]: Describes glutamate-induced calcium signaling in peritumoral neurons and correlation with seizure activity
- GABAergic neurotransmission and inhibitory synaptic signaling. Genes: GABRB3
  - [54]: Discusses GABAergic neuronal fate specification by Ascl1 and related factors

**Atomic cellular components**
- postsynaptic glutamate receptor complex. Genes: GRIA2, GRIA4, GRIK2, DPP6, LHFPL3
  - [34]: AMPAR subunits form tetrameric receptors with auxiliary proteins regulating trafficking and function
- synaptic auxiliary protein subunits. Genes: DPP6, LHFPL3, NXPH1
  - [34]: DPP6 and LHFPL3 are auxiliary proteins that modulate AMPAR biophysical properties

**Program citations**
- [34]: GluA1 cytoplasmic tail regulates intracellular AMPAR trafficking and synaptic transmission onto inhibitory neurons
- [70]: Aberrant neuronal activity in peritumoral cortex driven by tumor-derived glutamate and altered peritumoral gene expression
- [54]: GABAergic neuronal conversion and GABRB3 expression in reprogrammed cells

## Program: Synaptic Adhesion and Cell-Cell Contact Machinery
This program comprises synaptic cell adhesion molecules including neurexins, neuroligins, contactins, and cadherins that mediate neuron-neuron and neuron-tumor cell contacts. These proteins form the structural basis for synaptic formation, stabilization, and function. The program enables astrocytoma cells to form organized contacts with peritumoral neurons and potentially with neighboring tumor cells adopting neuronal phenotypes.

**Predicted impacts**
- Formation of synaptic-like contacts between tumor cells and peritumoral neurons
- Direct neuron-tumor cell communication enabling bidirectional signaling
- Dynamic regulation of cell-cell adhesion strength during tumor invasion
- Potential spread of signals through tumor-neuron circuits affecting seizure threshold

**Evidence summary**
Recent studies using electrophysiology and spatial transcriptomics in glioblastoma have documented direct synaptic contacts between tumor cells and peritumoral neurons, with postsynaptic currents recorded from neurons contacting tumor cells[70]. These neuron-tumor synapses involve canonical synaptic proteins and mediate both electrical and chemical signaling. The presence of neurexins, neuroligins, contactins, and cadherin family members in the input list suggests that astrocytoma cells can establish multiple types of cell-cell contacts with complementary adhesion properties that support complex tissue interactions[54].

**Atomic biological processes**
- synaptic adhesion complex assembly. Genes: NRXN1, NLGN4X, CNTN1, CNTNAP2, DLGAP1, CADM2
  - [54]: NRXN1 and related adhesion molecules are upregulated during neuronal differentiation and synaptic plasticity
  - [70]: Peritumoral neurons form excitatory electrochemical synapses with surrounding tumor cells
- cadherin-mediated cell-cell adhesion and migration. Genes: CDH2, CDH10, CDH13, CDH20, PCDH15, PCDH11X
  - [15]: CDH2 expression promotes epithelial-mesenchymal transition and tumor cell migration
- postsynaptic scaffolding and organization. Genes: DLGAP1, DLGAP1-AS4, ERC2
  - [54]: DLGAP proteins organize postsynaptic density and cluster neurotransmitter receptors

**Atomic cellular components**
- presynaptic neurexin complexes. Genes: NRXN1
  - [12]: Neurexins function as presynaptic adhesion molecules interacting with neuroligin postsynaptically
- postsynaptic neuroligin complexes. Genes: NLGN4X
  - [54]: Neuroligin expression increases during neuronal differentiation and synaptic stabilization
- contactin-based adhesion complexes. Genes: CNTN1, CNTNAP2, CNTN3
  - [9]: CNTN1 and CNTNAP2 modulate synaptic organization and stabilize postsynaptic structures
- cadherin adherens junctions. Genes: CDH2, CDH10, CDH13, CDH20
  - [15]: Classical cadherins mediate calcium-dependent cell-cell adhesion

**Program citations**
- [54]: Neurexin1 expression linked to glutamatergic neuronal identity and synaptic organization
- [70]: Tumor cells form direct synaptic contacts with peritumoral neurons
- [9]: CNTNAP2 and contactins stabilize synaptic structures
- [12]: NRXN1 functions in synaptic adhesion

## Program: Epithelial-Mesenchymal Transition and Invasive Phenotype
This program centers on ZEB1, a master regulator of epithelial-mesenchymal transition (EMT), and associated factors that promote mesenchymal differentiation, invasion, and therapy resistance. ZEB1 directly represses epithelial adhesion genes and promotes expression of mesenchymal and invasion-associated factors. The program enables astrocytoma cells to transition from indolent, differentiated states to highly invasive, stem-like states capable of single-cell migration through brain tissue.

**Predicted impacts**
- Enhanced tumor cell invasion and single-cell dissemination through brain tissue
- Transition to stem-like, therapy-resistant phenotype
- Increased expression of proteases enabling ECM degradation
- Reduced contact inhibition and enhanced migration along tissue planes and vessels
- Poor prognosis and increased likelihood of tumor recurrence after surgery

**Evidence summary**
ZEB1 expression in glioblastoma strongly correlates with invasive phenotype, poor prognosis, and reduced overall survival[16]. Recent studies have demonstrated that ZEB1-mediated EMT in glioblastoma is associated with a specific mesenchymal cell state (MES II) enriched at the tumor invasive margin and characterized by enhanced stemness, therapy resistance, and invasion-associated gene expression[51]. The presence of ZEB1 and associated EMT factors in the input list suggests that the gene program being analyzed includes mechanisms for dynamic phenotypic switching between differentiated and mesenchymal-invasive states[15][16].

**Atomic biological processes**
- transcriptional repression of epithelial markers. Genes: ZEB1
  - [15]: ZEB1 directly represses E-cadherin and epithelial adhesion gene expression
  - [16]: ZEB1 is a pivotal EMT transcription factor regulating epithelial-to-mesenchymal transition
- activation of mesenchymal markers and invasion genes. Genes: ZEB1, CDH2, MMP16
  - [15]: ZEB1 and TNS1 positive feedback loop promotes EMT and metastasis
- cell migration and invasion through tissue barriers. Genes: ZEB1, CDH2, MMP16, ADAMTS6, ADAMTS19, FERMT1
  - [35]: CAF-mediated collagen remodeling and MMP degradation precedes tumor cell invasion
  - [51]: Loss of pericytes increases mesenchymal glioma cell state and invasion

**Atomic cellular components**
- ZEB1 transcription factor complex. Genes: ZEB1
  - [16]: ZEB1 is a zinc-finger homeodomain transcription factor with two zinc-finger clusters
- N-cadherin-based adherens junctions. Genes: CDH2
  - [15]: N-cadherin (CDH2) mediates cell-cell adhesion and promotes mesenchymal phenotype
- focal adhesion and migration machinery. Genes: FERMT1, DLGAP1, PIK3R3
  - [35]: Integrin and focal adhesion proteins enable cell migration through ECM

**Program citations**
- [15]: TNS1-ZEB1 positive feedback loop in lung cancer promotes EMT and metastasis
- [16]: ZEB1 in liver cancer and EMT processes, including roles in glioma
- [51]: Mesenchymal glioma cell states MES I and MES II associated with invasion and poor prognosis
- [35]: CAF-mediated ECM remodeling and MMP-dependent invasion

## Program: Neural Progenitor Identity and Stemness Maintenance
This program encompasses transcription factors and signaling pathways that maintain neural stem cell and progenitor cell identity in astrocytoma cells. Key components include SOX family transcription factors (SOX2, SOX4, SOX6), Notch pathway components (DLL1, DLL3, MAML2), and related developmental signaling factors. The program enables astrocytoma cells to maintain self-renewal capacity, resist differentiation, and exhibit enhanced proliferation characteristic of cancer stem cells.

**Predicted impacts**
- Enhanced tumor cell proliferation through maintenance of progenitor state
- Increased self-renewal capacity and cancer stem cell properties
- Resistance to differentiation signals promoting tumor aggressiveness
- Enhanced potential for tumor recurrence after therapy targeting differentiated cells
- Integration with growth factor signaling to optimize proliferation

**Evidence summary**
Cancer stem cells in glioblastoma maintain neural stem cell programs characterized by high expression of SOX2, OLIG2, and related factors[59]. These cells drive tumor initiation, growth, and recurrence. The presence of Notch pathway components (DLL1, DLL3, MAML2) reflects the role of Notch signaling in maintaining undifferentiated states through lateral inhibition, where high Notch activity suppresses neuronal differentiation and promotes progenitor maintenance. Recent work identified that INSM1, a neuronal progenitor-associated transcription factor, is highly expressed in glioblastoma and functionally supports tumor progression through maintenance of intermediate progenitor-like cell states[59].

**Atomic biological processes**
- neural stem cell specification and maintenance. Genes: SOX6, SOX4, SOX2-OT, OLIG2, RBPJ
  - [59]: INSM1 governs neuronal progenitor state in glioblastoma driving tumor progression
  - [21]: SOX2 and related factors specify neural identity during embryonic development
- Notch signaling-mediated progenitor maintenance. Genes: DLL1, DLL3, MAML2, RBPJ
  - [21]: DLL1 and DLL3 are Notch ligands establishing progenitor-differentiated neuron gradient
  - [54]: Rbpj deletion promotes neurogenesis, indicating RBPJ maintains progenitor identity
- cancer stem cell self-renewal and tumorigenesis. Genes: SOX2-OT, CREB5, RBPJ
  - [59]: INSM1 knockdown disrupts oncogenic gene expression and inhibits glioblastoma tumorigenicity

**Atomic cellular components**
- SOX transcription factor complexes. Genes: SOX6, SOX4, OLIG2
  - [59]: SOX transcription factors regulate neuronal progenitor fate specification
- Notch signaling complex at cell membrane. Genes: DLL1, DLL3
  - [21]: DLL1 and DLL3 activate Notch receptors through trans-cellular interaction
- Notch coactivator complex in nucleus. Genes: MAML2
  - [40]: MAML2 is a mastermind-like coactivator in Notch signaling

**Program citations**
- [59]: INSM1 governs neuronal progenitor state driving glioblastoma tumorigenicity
- [54]: RBPJ deletion promotes neurogenesis, indicating stemness regulation
- [21]: DLL1 and DLL3 establish neural progenitor-differentiated neuron gradients
- [40]: MAML2 in Notch signaling and transcriptional regulation

## Program: Growth Factor Receptor Signaling and Proliferation Control
This program encompasses growth factor receptors (EGFR, NTRK3, IGF1R) and their downstream signaling mediators that drive tumor cell proliferation, survival, and invasiveness. These receptors activate MAPK/ERK, PI3K/AKT, and JAK/STAT signaling cascades. The program integrates with other cellular programs to coordinate proliferation signals with metabolic capacity and survival.

**Predicted impacts**
- Enhanced proliferation through constitutive growth factor receptor signaling
- Increased survival through AKT-mediated suppression of apoptotic pathways
- Activation of metabolic pathways supporting high proliferation rates
- Potential intrinsic resistance to targeted therapy through receptor redundancy
- Enhanced invasion through integrin and cytoskeletal signaling crosstalk

**Evidence summary**
EGFR is the most frequently altered growth factor receptor in glioblastoma, with amplification present in approximately 45% of classical subtype gliomas[11]. EGFR-amplified glioblastomas show enhanced proliferation and specific cellular states including the GPC-like (glial progenitor-like) state characterized by high expression of proliferation-associated genes[57]. Additionally, NTRK fusions have been identified in rare gliomas and drive aggressive growth through constitutive activation of kinase signaling[68]. The presence of multiple growth factor receptors in the input list suggests that astrocytoma cells employ receptor redundancy to maintain proliferation signals even when individual receptors are targeted by therapy[68].

**Atomic biological processes**
- growth factor receptor activation and autophosphorylation. Genes: EGFR, NTRK3, IGF1R
  - [11]: EGFR is frequently amplified in glioblastoma and drives proliferation
  - [22]: NTRK3 is a receptor tyrosine kinase for neurotrophins
- PI3K/AKT survival signaling. Genes: EGFR, NTRK3, IGF1R, PIK3R3
  - [68]: TRIM24::NTRK2 fusion activates PI3K pathway in epithelioid glioblastoma
- MAPK/ERK proliferation signaling. Genes: EGFR, NTRK3, IGF1R
  - [68]: NTRK fusion gene activation of MAPK/ERK and PI3K/AKT pathways in glioma
- fibroblast growth factor signaling. Genes: FGF12, FGF14
  - [62]: FGF signaling drives proliferation in pediatric high-grade gliomas

**Atomic cellular components**
- EGFR receptor tyrosine kinase complex. Genes: EGFR
  - [11]: EGFR is frequently altered in glioblastoma
- NTRK receptor tyrosine kinase. Genes: NTRK3
  - [68]: NTRK2 involved in TRIM24::NTRK2 fusion in epithelioid glioblastoma
- fibroblast growth factor receptor complex. Genes: FGF12, FGF14
  - [62]: FGFR signaling important in pediatric glioma

**Program citations**
- [11]: EGFR pathway substrate 8 mediates glioma cell proliferation and survival
- [68]: TRIM24::NTRK2 fusion and NTRK2 signaling in glioblastoma
- [57]: GPC-like tumor cell state associated with EGFR amplification
- [62]: FGFR signaling in pediatric high-grade glioma models

## Program: Extracellular Matrix Remodeling and Proteolytic Invasion
This program comprises proteases (MMP16, ADAMTS6, ADAMTS19) and ECM components (VCAN, COL11A1, SMOC1) that enable extracellular matrix degradation and remodeling. Tumor cells expressing these proteins can breach anatomical barriers, invade peritumoral tissue, and evade surgical resection. The program is particularly important for tumor infiltration beyond the visible tumor margin.

**Predicted impacts**
- Enhanced tumor cell invasion through brain parenchyma
- Evasion from surgical resection through infiltration beyond visible tumor boundary
- Remodeling of perivascular spaces enabling vascular co-option
- Immune suppression through ECM-mediated immunosuppressive signaling
- Increased metastatic potential through enhanced proteolytic capacity

**Evidence summary**
ECM remodeling is a fundamental aspect of glioblastoma progression. Recent studies using 3D in vitro models have demonstrated that matrix metalloproteinases enable cancer cell invasion through sequential ECM degradation and remodeling[35]. VCAN expression is frequently elevated in glioblastoma and promotes invasion while simultaneously creating an immunosuppressive microenvironment[47]. The presence of multiple protease family members and ECM components in the input list suggests that astrocytoma cells maintain robust proteolytic and ECM remodeling capacity, enabling both individual cell invasion and collective migration through brain tissue[48].

**Atomic biological processes**
- matrix metalloproteinase-mediated ECM degradation. Genes: MMP16
  - [35]: MMP-mediated collagen degradation precedes cancer cell invasion and spheroid expansion
  - [48]: MMP16 is involved in ECM breakdown in tissue remodeling
- ADAMTS protease-mediated ECM degradation. Genes: ADAMTS6, ADAMTS19
  - [35]: Proteolytic ECM degradation is critical for tumor cell invasion
- tumor cell migration through degraded ECM. Genes: MMP16, ADAMTS6, ADAMTS19, FERMT1
  - [35]: CAF-driven collagen matrix remodeling promotes cancer cell invasion and dissemination
- ECM composition and stiffness regulation. Genes: VCAN, VCAN-AS1, COL11A1
  - [47]: Versican is a major chondroitin sulfate proteoglycan in the extracellular matrix

**Atomic cellular components**
- membrane-anchored MMP complex. Genes: MMP16
  - [48]: MMP16 is a membrane-anchored matrix metalloproteinase
- secreted ADAMTS proteases. Genes: ADAMTS6, ADAMTS19
  - [35]: ADAMTS proteases are secreted and degrade ECM components
- proteoglycan ECM components. Genes: VCAN
  - [47]: Versican is a large chondroitin sulfate proteoglycan

**Program citations**
- [35]: CAF-mediated ECM remodeling precedes cancer cell invasion
- [47]: Versican is a major ECM component in cancers
- [48]: MMP16 is involved in tissue remodeling
- [56]: ECM ligand-receptor networks in GBM

## Program: Metabolic Plasticity and Hypoxic Adaptation
This program includes genes supporting metabolic flexibility under hypoxic and nutrient-limited conditions characteristic of glioblastoma microenvironments. Components include lipid and nucleotide metabolism regulators (LDLRAD3, LDLRAD4), error-prone DNA polymerases (REV3L), cell cycle checkpoint regulators (TFDP2), and protein degradation machinery (CBLB, MARCH1). The program enables astrocytoma cells to survive and proliferate when oxygen and nutrient availability are severely limited.

**Predicted impacts**
- Enhanced survival under hypoxic, nutrient-limited microenvironmental conditions
- Metabolic flexibility supporting rapid growth despite nutrient scarcity
- Genomic instability enabling rapid evolution of resistance mechanisms
- Integration of metabolic capacity with cell cycle progression
- Reduced dependence on conventional aerobic glucose metabolism

**Evidence summary**
Glioblastomas frequently develop in hypoxic microenvironments where oxygen availability is severely limited due to inadequate vascular perfusion. Tumor cells respond through HIF-driven metabolic reprogramming, including shifts toward enhanced lipid metabolism, glutamine-dependent anaplerosis, and glycolytic pathways[10][62]. The presence of error-prone DNA polymerases (REV3L) in tumor cells suggests they employ genomic plasticity as a survival strategy, generating genetic diversity that enables rapid evolution of resistance mechanisms. Additionally, maintained metabolic flexibility through alternative lipid and nucleotide synthesis pathways enables astrocytoma cells to proliferate even in severely nutrient-deprived conditions[62].

**Atomic biological processes**
- alternative lipid metabolism pathways. Genes: LDLRAD3, LDLRAD4
  - [10]: IDH1-driven metabolic reprogramming including reductive glutamine carboxylation
- error-prone DNA synthesis and genomic plasticity. Genes: REV3L
  - [62]: REV3L-mediated error-prone DNA polymerase activity contributes to genomic instability
- cell cycle checkpoint control and proliferation regulation. Genes: TFDP2
  - [62]: TFDP2 regulates E2F-dependent gene expression at G1/S checkpoint
- protein turnover and ubiquitin-proteasome degradation. Genes: CBLB, MARCH1
  - [35]: Protein degradation regulates cellular composition and metabolic capacity

**Atomic cellular components**
- lipoprotein receptor complex. Genes: LDLRAD3, LDLRAD4
  - [49]: LRP1B regulates LDL receptor signaling and lipid metabolism
- DNA polymerase zeta complex. Genes: REV3L
  - [62]: REV3L is the catalytic subunit of DNA polymerase zeta
- E2F transcription factor complex. Genes: TFDP2
  - [62]: TFDP2 partners with E2F transcription factors

**Program citations**
- [10]: IDH1 activity and metabolic reprogramming in radiation-resistant tumors
- [62]: Genomic heterogeneity in pediatric high-grade gliomas with acquisition of CNAs during progression
- [30]: Metabolic and epigenetic dysregulation in IDH1/2-mutant gliomas

## Program: Chromatin Remodeling and Transcriptional Control
This program encompasses chromatin-modifying enzymes (KAT2B histone acetyltransferase, CXXC4) and transcriptional regulators (ZNF genes, ELAVL4, NOVA1) that determine which genes are accessible for transcription and therefore actively expressed in tumor cells. The program enables rapid transcriptional reprogramming in response to microenvironmental signals and therapy, supporting the phenotypic plasticity characteristic of aggressive gliomas.

**Predicted impacts**
- Enhanced transcriptional plasticity enabling rapid phenotypic switching
- Stabilization of growth factor and survival factor mRNAs
- Epigenetic silencing of differentiation genes maintaining stemness
- Alternative splicing diversity supporting multiple cell programs simultaneously
- Integration of developmental and microenvironmental signals into coherent transcriptional response

**Evidence summary**
Tumor cells employ extensive transcriptional plasticity to adapt to rapidly changing microenvironmental conditions. Histone-modifying enzymes like KAT2B enable rapid shifts between open and closed chromatin states, determining which genes are accessible for transcription[62]. RNA-binding proteins NOVA1 and ELAVL4 stabilize mRNAs encoding neurotrophic factors and neuronal markers, supporting expression of programs linked to neuronal differentiation or progenitor identity[41][44]. The presence of multiple zinc-finger transcription factors suggests integration of multiple signaling pathways into coherent transcriptional control. Additionally, recent work emphasizes that alternative splicing driven by RNA-binding proteins creates transcript diversity that supports cellular heterogeneity and phenotypic plasticity in glioma[60].

**Atomic biological processes**
- histone acetylation and chromatin opening. Genes: KAT2B
  - [62]: Chromatin remodeling drives distinct tumor cell programs in glioma
- post-transcriptional mRNA stabilization and regulation. Genes: ELAVL4, NOVA1
  - [41]: ELAVL4 involved in 3'-UTR-mediated mRNA stabilization
  - [44]: ELAVL4 promotes BDNF expression through selective mRNA stabilization
- zinc finger transcription factor-mediated gene regulation. Genes: ZNF804A, ZNF804B, ZNF704, ZNF124
  - [16]: ZEB1 contains zinc finger clusters for DNA binding
- alternative splicing regulation. Genes: NOVA1, ELAVL4, CELF2
  - [60]: Alternative splicing drives glioma cellular heterogeneity

**Atomic cellular components**
- histone acetyltransferase complex. Genes: KAT2B
  - [62]: KAT2B is a histone acetyltransferase
- RNA-binding protein regulatory complexes. Genes: ELAVL4, NOVA1, CELF2
  - [41]: ELAVL4 and NOVA1 are RNA-binding proteins
- zinc-finger transcription factor complexes. Genes: ZEB1, ZNF804A, ZNF804B
  - [16]: ZEB1 is a zinc finger E-box-binding homeobox transcription factor

**Program citations**
- [62]: Chromatin remodeling in pediatric high-grade glioma
- [41]: ELAVL4 in 3'-UTR-mediated mRNA stabilization
- [44]: ELAVL4 promotes BDNF expression
- [60]: Alternative splicing in glioma cellular heterogeneity

## Program: Calcium Signaling and Synaptic Plasticity Integration
This program integrates calcium signaling components including calcium-permeable ion channels (GRIA2, GRIA4, GRID2, CACNA1A), calcium exchangers (SLC8A3), and calcium-responsive signaling proteins (CASK) that enable rapid intracellular calcium elevation and downstream signaling cascade activation. The program supports both neuronal-type synaptic plasticity and tumor cell-specific survival and proliferation signals through calcium-dependent pathways.

**Predicted impacts**
- Sustained intracellular calcium signaling supporting tumor cell survival and proliferation
- Coupling of neurotransmitter signaling to intracellular signaling cascade activation
- Integration of multiple calcium sources (ionotropic receptors, voltage-gated channels) into coordinated response
- Activation of calcium-dependent enzymes promoting metabolic switching and gene expression changes
- Potential for seizure propagation through calcium wave amplification in peritumoral neurons

**Evidence summary**
Calcium signaling is a critical nexus integrating neurotransmitter signaling, growth factor signaling, and transcriptional control. The presence of multiple calcium-permeable ion channels (GRIA2, GRIA4, GRID2) and calcium-regulatory proteins (SLC8A3, CASK) suggests that astrocytoma cells maintain active calcium signaling capable of supporting both plasticityassociated gene expression and survival signals[34][70]. CASK is particularly interesting as it combines scaffolding function with calcium-dependent kinase activity, enabling rapid integration of multiple signaling pathways[20]. The presence of CALCRL and VIPR2 extends calcium signaling to G-protein coupled receptor-mediated calcium mobilization, creating additional calcium signaling routes. Recent studies have demonstrated that tumor-derived glutamate activates calcium-permeable AMPA receptors on peritumoral neurons, driving aberrant calcium dynamics and seizure activity[70].

**Atomic biological processes**
- calcium influx through ionotropic receptors. Genes: GRIA2, GRIA4, GRID2, CACNA1A
  - [34]: Calcium-permeable AMPA receptors support calcium signaling and synaptic plasticity
  - [70]: Calcium influx through glutamate receptors in peritumoral neurons
- calcium homeostasis and extrusion. Genes: SLC8A3
  - [70]: SLC8A3 sodium-calcium exchanger regulates intracellular calcium
- calcium-dependent protein kinase signaling. Genes: CASK
  - [20]: CASK combines scaffolding and kinase activity activated by calcium
- calcium-responsive transcription factor activation. Genes: CALCRL, VIPR2
  - [34]: Calcium signaling activates transcription factors driving plasticity and gene expression

**Atomic cellular components**
- calcium-permeable AMPA receptor channels. Genes: GRIA2, GRIA4
  - [34]: GRIA subunits form calcium-permeable AMPA receptors
- voltage-gated calcium channel complex. Genes: CACNA1A
  - [26]: CACNA1A encodes L-type voltage-gated calcium channel alpha subunit
- sodium-calcium exchanger. Genes: SLC8A3
  - [70]: SLC8A3 is a sodium-calcium exchanger
- calcium-activated CASK kinase complex. Genes: CASK
  - [20]: CASK combines scaffolding and calcium-dependent kinase activity

**Program citations**
- [34]: GluA1 CTD and AMPAR calcium permeability
- [70]: Tumor-derived glutamate and peritumoral neuronal calcium signaling
- [20]: CASK calcium-dependent kinase activity
- [26]: SCN3A and voltage-gated channels

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/546
2. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
3. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
4. Anamaria S, Cristian-Ionut O, Raluca IV, Madalina B, Manuela E, Sorin V, et al.. Unpredictable Evolution of Pilocytic Astrocytoma in Adults: A Case Series and Diagnostic Challenges.. The American journal of case reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41382984/?fc=None&ff=20251213032813&v=2.18.0.post22+67771e2
5. Yufan Y, Nitin W, Yuki A, Sachin G, Sean S, Ali S, et al.. Pediatric H3 K27-altered diffuse midline gliomas may consist of two clinically relevant subsets based on patient age and molecular genetic profile.. Neuro-oncology advances [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41393244/?fc=None&ff=20251215162242&v=2.18.0.post22+67771e2
6. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
7. Available from: https://www.ncbi.nlm.nih.gov/gene/4133
8. Available from: https://www.ncbi.nlm.nih.gov/gene/25595
9. Available from: https://www.ncbi.nlm.nih.gov/gene/26047
10. Veo B, Wang D, DeSisto J, Pierce A, Brunt B, Bompada PC, et al.. Single-cell multi-omics identifies metabolism-linked epigenetic reprogramming as a driver of therapy-resistant medulloblastoma. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65466-9
11. Available from: https://www.ncbi.nlm.nih.gov/gene/13649
12. Available from: https://www.ncbi.nlm.nih.gov/gene/9378
13. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
14. Available from: https://www.ncbi.nlm.nih.gov/gene/2059
15. Zhang T, Li Z, Ming Y, Li J, Ye Z, Luo D, et al.. A positive feedback loop between TNS1 and ZEB1 promotes TGFβ-induced epithelial-to-mesenchymal transition in lung cancer. Communications Biology [Internet]. 2025Nov26;8(1). Available from: https://www.nature.com/articles/s42003-025-09079-4
16. Ester G-S, Carlos AR-H, Ana M-R, Lucia G-C, Laura F, Javier V. Epithelial to Mesenchymal Transition Transcriptional Regulator ZEB1 in Liver Cancer: Oncogenic Roles and Therapeutic Potential.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41303618/
17. Gkogka A, Malwade S, Koskuvi M, Ohtonen S, Molnar E, Bose R, et al.. Human oligodendrocyte progenitor cells mediate synapse elimination through TAM receptor activation. Nature Communications [Internet]. 2025Dec5;16(1). Available from: https://www.nature.com/articles/s41467-025-66521-1
18. Available from: https://www.ncbi.nlm.nih.gov/gene/1739
19. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
20. Available from: https://www.ncbi.nlm.nih.gov/gene/8573
21. Makwana K, Tilley L, Chakravarty P, Thompson J, Baillie-Benson P, Rodriguez-Polo I, et al.. Modelling co-development between the somites and neural tube in human trunk-like structures. Nature Cell Biology [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41556-025-01813-8
22. Available from: https://www.ncbi.nlm.nih.gov/gene/4916
23. Available from: https://www.ncbi.nlm.nih.gov/gene/6323
24. Available from: https://www.ncbi.nlm.nih.gov/gene/13388
25. Available from: https://www.ncbi.nlm.nih.gov/gene/18213
26. Available from: https://www.ncbi.nlm.nih.gov/gene/6328
27. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
28. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/12355/
29. Available from: https://www.ncbi.nlm.nih.gov/gene/5727
30. Xuan-Hao P, Bei-Wu L, Nan W, Jing S, Yu-Fei G. Metabolic and epigenetic dysregulation in IDH1/2-mutant gliomas: A microglial-mediated mechanism of blood-brain barrier disruption.. International immunopharmacology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41349464/?fc=None&ff=20251207033947&v=2.18.0.post22+67771e2
31. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
32. Available from: https://www.ncbi.nlm.nih.gov/gene/19206
33. Leana-Sandoval G, Madrid A, Kolli AV, Chinn CA, Sandoval MA, Lo I, et al.. The GluA1 cytoplasmic tail regulates intracellular AMPA receptor trafficking and synaptic transmission onto dentate gyrus GABAergic interneurons, gating response to novelty. Molecular Psychiatry [Internet]. 2025Nov22;. Available from: https://www.nature.com/articles/s41380-025-03328-y
34. Pranav M, Ankur DB, Cor R, Ma KHD, Wilma M, Gerrit JL, et al.. Inter-spheroid proximity and matrix remodeling determine cancer associated fibroblast mediated cancer cell invasion.. Acta biomaterialia [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41271076/
35. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
36. Uzay B, Zhang KJ, Monteggia LM, Kavalali ET. Dopaminergic tone inhibits spontaneous glutamate release and augments homeostatic synaptic plasticity. Molecular Psychiatry [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41380-025-03374-6
37. Juan W, Yuxin H, Jin G, Li C, Li Z, Huai W. Nicotine Activates PI3K/AKT Pathway to Induce Cellular Proliferation, Invasion, and Migration in HPV-16 Positive Cervical Cancer SiHa Cells.. Journal of applied toxicology : JAT [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41338183/
38. Available from: https://www.ncbi.nlm.nih.gov/gene/6714
39. Available from: https://www.ncbi.nlm.nih.gov/gene/84441
40. Available from: https://www.ncbi.nlm.nih.gov/gene/1996
41. Available from: https://www.ncbi.nlm.nih.gov/gene/14812
42. Available from: https://www.ncbi.nlm.nih.gov/gene/23373
43. Available from: https://www.ncbi.nlm.nih.gov/gene/15572
44. Available from: https://www.ncbi.nlm.nih.gov/gene/17389
45. Available from: https://www.ncbi.nlm.nih.gov/gene/16971
46. Available from: https://www.ncbi.nlm.nih.gov/gene/1462
47. Available from: https://www.ncbi.nlm.nih.gov/gene/4325
48. Available from: https://www.ncbi.nlm.nih.gov/gene/53353
49. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=13003
50. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
51. Available from: https://www.ncbi.nlm.nih.gov/gene/14804
52. Han Y, Han M, Wang T, Zhang H, Liu H, Zheng Y, et al.. Inhibiting the formation of neutrophil extracellular traps to prevent the recurrence of post-operative glioblastoma. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-65933-3
53. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
54. Dylan SLH, Sara BA, Vilde P, Alessio L, Maya JSL, David S, et al.. Genomic heterogeneity drives distinct infiltration patterns in glioblastoma.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41316429/
55. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z
56. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
57. Xiao S, Deanna T, Minghui L, Xiaozhou Y, Runxin W, Maya W, et al.. A single-cell atlas of RNA alternative splicing in the glioma-immune ecosystem.. Genome biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41387900/?fc=None&ff=20251213032053&v=2.18.0.post22+67771e2
58. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
59. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
60. He G-qian, He S-jia, Jing X-yu, Dai Y-ling, Guo X, Gao J, et al.. Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance. Oncogene [Internet]. 2025Nov27;. Available from: https://www.nature.com/articles/s41388-025-03635-2
61. Available from: https://www.ncbi.nlm.nih.gov/gene/355
62. Yuan Y, Yue Q, Wang Y, Du Z, Wang X, Yan F, et al.. AI-augmented intraoperative decision-making workflows in diffuse midline glioma biopsy using cryosection pathology. Nature Communications [Internet]. 2025Nov26;. Available from: https://www.nature.com/articles/s41467-025-66853-y
63. Available from: https://www.ncbi.nlm.nih.gov/gene/5621
64. Shapiro I, Debaix H, Kräuchi C, Abate A, Bornstein SR, Nölting S, et al.. (Non)canonical Wnt signaling, cytoarchitecture and stemness: new insights from primary nonmetastatic, primary metastatic, regional and distant metastatic models of adrenocortical carcinoma. Experimental &amp; Molecular Medicine [Internet]. 2025Nov28;57(11). Available from: https://www.nature.com/articles/s12276-025-01507-z
65. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
66. Available from: https://www.ncbi.nlm.nih.gov/gene/3371
