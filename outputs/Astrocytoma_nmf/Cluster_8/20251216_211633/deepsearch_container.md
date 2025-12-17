# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma
- Tissue: Central nervous system (brain)

## Input Genes
CARNS1, MOBP, ERMN, ST18, PTGDS, TF, FOLH1, NKAIN2, PLEKHH1, MYO1D, PLP1, CTNNA3, CNDP1, MOG, ENPP2, EDIL3, MAP7, MAG, SELENOP, RNF220, AK5, PPP1R14A, CDH19, PEX5L, RNASE1, ... (200 total)

## Program: Oligodendroglial Transcriptional Specification
Master regulatory program controlling specification and differentiation of oligodendrocyte lineage through coordinated expression of lineage-specific transcription factors. These factors activate downstream transcriptional programs that establish oligodendroglial cell identity and suppress conflicting cell fates. In astrocytoma context, aberrant reactivation of this developmental program may contribute to cellular plasticity and malignant properties.

**Predicted impacts**
- Enhanced cellular plasticity and stemness features in astrocytoma cells
- Aberrant activation of developmental programs normally silenced in mature astrocytes
- Potential therapeutic resistance through retention of oligodendroglial specification capacity
- Dysregulation of terminal differentiation programs

**Evidence summary**
The oligodendroglial transcriptional specification program is anchored by NKX6-2 and SOX10, master regulators that control the entire developmental pathway from neural progenitor cells to mature oligodendrocytes. These transcription factors are normally silenced in differentiated astrocytes but may be aberrantly reactivated in astrocytomas. The presence of MYRF, which drives terminal oligodendroglial differentiation, suggests that the tumor microenvironment or transformed astrocytes themselves may reactivate developmental programs. This program is particularly significant in astrocytoma as reactivation of developmental transcriptional programs is a hallmark of malignant transformation and contributes to cellular dedifferentiation and enhanced proliferative capacity.

**Atomic biological processes**
- Transcriptional regulation of oligodendroglial differentiation. Genes: NKX6-2, SOX10, MYRF
  - [2]: OLIG2 encodes basic helix-loop-helix transcription factor expressed in oligodendroglial tumors
  - [3]: SOX10 encodes SRY-box transcription factor involved in regulation of embryonic development and oligodendrocyte specification
  - [4]: Nkx2.2 regulates myelination-associated genes during oligodendrocyte differentiation
- Cell differentiation and lineage commitment. Genes: NKX6-2, SOX10
  - [12]: NKX6-2 enables sequence-specific DNA binding and is involved in cell differentiation and regulation of DNA-templated transcription

**Required genes (not in input)**
- Genes: OLIG1, OLIG2, POU3F1, PDGFRα
  - [2]: OLIG2 is a key oligodendroglial master regulator
  - [4]: Zfp488 regulates oligodendrocyte differentiation alongside SOX10 and Nkx2.2

**Program citations**
- [2]: OLIG2 in oligodendroglial tumors
- [3]: SOX10 in embryonic development
- [4]: Nkx2.2 in oligodendrocyte differentiation
- [12]: NKX6-2 in cell differentiation

## Program: Myelin Structural Proteins and Compaction
Comprehensive program encoding structural proteins and enzymes essential for myelin formation, maintenance, and compaction. This program includes major myelin lipoproteins, cell adhesion molecules stabilizing myelin lamellae, and enzymatic machinery supporting the unique lipid composition of myelin. Dysregulation in astrocytoma may reflect aberrant oligodendroglial differentiation within the tumor or disrupted support for myelin integrity.

**Predicted impacts**
- Disrupted myelin integrity and white matter organization
- Altered oligodendrocyte function and maturation within tumor microenvironment
- Impaired metabolic support for neuronal axons dependent on myelination
- Enhanced infiltration through white matter tracts

**Evidence summary**
The myelin program encompasses classical myelin structural proteins (MBP, PLP1, MOG, CNP, OPALIN, MAG, PLLP) as well as enzymes supporting myelin lipid synthesis and metabolism (UGT8, FA2H, ELOVL7, MAL). While myelin proteins are canonically expressed in oligodendrocytes rather than astrocytes, their presence in the astrocytoma gene list may reflect: (1) oligodendroglial elements within the tumor, (2) aberrant expression by astrocytoma cells themselves as a manifestation of cellular plasticity, or (3) dysfunction of the support astrocytes normally provide to oligodendrocytes. The dysregulation of this program in astrocytoma contributes to white matter damage and metabolic disruption characteristic of these tumors.

**Atomic biological processes**
- Myelin structural protein synthesis and assembly. Genes: MBP, PLP1, MOG, CNP, OPALIN, MAG
  - [1]: Genes associated with myelin proteins downregulated in chronic TBI astrocytes
- Myelin lipid synthesis and processing. Genes: UGT8, FA2H, ELOVL7, MAL
  - [6]: V-ATPase maintains lysosomal acidification essential for lipid-processing enzymes involved in cholesterol and sphingolipid metabolism

**Atomic cellular components**
- Myelin sheath structure. Genes: MBP, PLP1, MOG, OPALIN, MAG, PLLP
  - [1]: Myelin-related genes dysregulated in astrocyte transcriptome

**Required genes (not in input)**
- Genes: MBP, PLP, PMP22
  - [4]: Key oligodendrocyte differentiation regulated by SOX10 and Nkx2.2

**Program citations**
- [1]: Myelin genes dysregulated in astrocyte transcriptome
- [6]: Lysosomal acidification essential for lipid processing

## Program: Myelin Lipid Biosynthesis and Homeostasis
Specialized metabolic program controlling synthesis, transport, and maintenance of the unusual lipid composition characteristic of myelin membranes. Myelin is approximately 70-80% lipid by dry weight, with enriched cholesterol, galactocerebroside, and sulfatides. This program includes fatty acid elongases, hydroxylases, ATP-binding cassette transporters, and sterol-binding proteins essential for establishing and maintaining myelin lipid composition.

**Predicted impacts**
- Altered lipid composition of cell membranes in astrocytoma cells
- Dysregulated cholesterol and lipid homeostasis supporting tumor proliferation
- Enhanced or reduced membrane fluidity affecting cell migration and invasion
- Impaired normal glial support for myelination

**Evidence summary**
This program specifically addresses the metabolic machinery for synthesizing and maintaining the extraordinary lipid composition of myelin. ELOVL7 and FA2H mediate fatty acid modifications essential for myelin lipids. OSBPL1A, ABCA2, ABCA6, and ABCA8 regulate cholesterol and lipid transport and distribution. UGT8 and ST6GALNAC3 catalyze glycosphingolipid synthesis. In astrocytoma, dysregulation of this lipid program could contribute to altered membrane properties, enhanced invasion and migration, and disrupted metabolic support for normal myelination.

**Atomic biological processes**
- Very long-chain fatty acid synthesis. Genes: ELOVL7, FA2H
  - [6]: Lysosomal acidification maintains proper sorting of lysosomal enzymes for lipid metabolism
- Cholesterol and glycosphingolipid metabolism. Genes: OSBPL1A, UGT8, ST6GALNAC3
  - [6]: Lysosomal acidification essential for activity of lipid-processing enzymes involved in cholesterol and sphingolipid metabolism and for cholesterol export

**Atomic cellular components**
- Lipid transporter complexes. Genes: ABCA2, ABCA6, ABCA8, OSBPL1A
  - [6]: ER-lysosome contact sites regulate lipid exchange

**Required genes (not in input)**
- Genes: SPTLC1, ASAH1, GALC
  - [6]: Critical for sphingolipid and galactosylceramide metabolism

**Program citations**
- [6]: Lysosomal acidification and lipid metabolism

## Program: Astrocyte-Neuron Metabolic Coupling and Lactate Shuttle
Program supporting metabolic communication between astrocytes and neurons through glucose uptake by astrocytes, glycolytic lactate production, and lactate export to neurons as a preferred fuel source. The astrocyte-neuron lactate shuttle (ANLS) is fundamental to brain energy metabolism and neural function. Disruption of this program in astrocytoma contributes to metabolic dysfunction in the peritumoral region and may promote seizures through impaired neuronal energy metabolism.

**Predicted impacts**
- Impaired neuronal energy metabolism in peritumoral region
- Enhanced seizure susceptibility through metabolic substrate deprivation
- Altered glutamate-glutamine cycling affecting neurotransmitter balance
- Disrupted astrocyte-neuron communication at metabolic level

**Evidence summary**
The astrocyte-neuron lactate shuttle program is centered on glucose transporters (particularly GLUT3, though primarily neuronal, with activity-dependent trafficking) and metabolic regulators supporting lactate production and export. GLUT3 undergoes PKCε-dependent phosphorylation at specific residues enabling activity-dependent plasma membrane translocation, allowing neurons to rapidly increase glucose uptake during heightened activity. GPR37, LPAR1, and SLC44A1 participate in lipid and amino acid metabolism with potential roles in regulating metabolic homeostasis. The presence of these genes in the astrocytoma list suggests dysregulation of the ANLS program, with consequences for peritumoral neural tissue. This dysregulation contributes to metabolic stress and seizure development characteristic of astrocytomas.

**Atomic biological processes**
- Glucose uptake and glycolytic metabolism. Genes: GLUT3, LPAR1
  - [15]: GLUT3 activity-dependent plasma translocation regulated by PKCε phosphorylation enables increased neuronal glucose uptake during activity
  - [16]: Astrocytic Cx43 maintains glycolytic metabolism and lactate production essential for neuronal excitability
- Neuronal excitability and synaptic transmission support. Genes: GLUT3, GPR37, SLC44A1
  - [16]: Reduced lactate synthesis correlates with diminished neuronal excitability and depressive-like behaviors

**Atomic cellular components**
- Glucose transporter membrane trafficking. Genes: GLUT3, SLC24A2
  - [15]: GLUT3 phosphorylation at Thr232 and Ser246 by PKCε promotes binding to KLC1 and activity-dependent plasma membrane insertion

**Required genes (not in input)**
- Genes: GLS, GLUL, LDH, MCT1
  - [16]: Lactate and glutamine metabolism essential for astrocyte-neuron metabolic coupling

**Program citations**
- [15]: GLUT3 activity-dependent translocation and PKCε phosphorylation
- [16]: Astrocytic metabolism and neuronal excitability coupling

## Program: Glutamate-Glutamine Cycle and Amino Acid Homeostasis
Program maintaining extracellular glutamate at physiological levels through astrocytic uptake of glutamate, conversion to glutamine by glutamine synthetase, release of glutamine to neurons, and recycling back to glutamate. This cycle is essential for preventing excitotoxicity, maintaining the neurotransmitter pool, and supporting neurotransmitter synthesis. Dysregulation in astrocytoma leads to excessive glutamate accumulation and excitotoxic damage.

**Predicted impacts**
- Excessive extracellular glutamate accumulation causing excitotoxic neuronal damage
- Enhanced seizure activity through disrupted glutamate homeostasis
- Impaired neurotransmitter synthesis and recycling
- Tumor-neuron crosstalk enabling aberrant neuronal-tumor synaptic connections

**Evidence summary**
Dysregulation of glutamate homeostasis is a hallmark feature of astrocytomas. Glioma cells produce excessive glutamate through multiple mechanisms including impaired glutamate reuptake and enhanced glutamate release. Recent studies have demonstrated that glioma cells cause elevation of local glutamate concentration and alter neuronal excitability via the non-synaptic xCT transporter system and by impairing local glutamate reuptake. Furthermore, neurons in the peritumoral region form excitatory electrochemical synapses with tumor cells, creating direct communication pathways that facilitate tumor progression through direct and paracrine signaling. The amino acid transporter genes in this list (SLC7A14, SLC22A15, SLC44A1) participate in amino acid homeostasis and suggest dysregulation of glutamate handling in astrocytomas.

**Atomic biological processes**
- Amino acid transport and neurotransmitter recycling. Genes: SLC7A14, SLC22A15
  - [13]: Glioma cells cause elevation of local glutamate concentration and alter neuronal excitability via impaired glutamate reuptake
- Extracellular glutamate regulation. Genes: SLC7A14, SLC44A1
  - [13]: Tumor-neuron crosstalk alters neuronal functioning through glutamate dysregulation

**Required genes (not in input)**
- Genes: GLT1, GLAST, GLUL, GLS
  - [13]: Essential for glutamate reuptake and recycling

**Program citations**
- [13]: Glioma-induced glutamate dysregulation and neuronal excitability alterations

## Program: Cell-Cell Adhesion and Neuronal-Glial Communication
Program establishing and maintaining physical contacts between cells through adhesion molecules, linking these adhesive interactions to cytoskeletal organization and cellular signaling. This program is essential for neural tissue organization, neuronal-glial interactions, and tripartite synapse formation. Loss of adhesion and aberrant signaling in astrocytoma enables infiltrative growth and disrupts normal neuron-glia communication.

**Predicted impacts**
- Reduced contact-dependent growth inhibition promoting tumor proliferation
- Enhanced tumor cell migration and invasion through white matter
- Disrupted neuron-glia communication affecting synaptic function
- Loss of normal adhesive signaling that constrains differentiation programs

**Evidence summary**
Cell adhesion molecules including CDH19 (cadherin 19), CTNNA3 (catenin alpha 3), and immunoglobulin superfamily members (CNTN2, CNTNAP4) establish the physical and signaling contacts essential for normal neural tissue organization and neuron-glia interactions. CDH19 mediates homophilic cell-cell adhesion while CTNNA3 links cadherins to the actin cytoskeleton. CNTN2 (contactin 2, axonin-1) and CNTNAP4 are immunoglobulin superfamily adhesion molecules involved in myelin formation and neuron-glia interactions. Loss of these adhesion molecules is a hallmark of malignant transformation, enabling tumor cells to lose contact-dependent growth inhibition and acquire enhanced migratory capability. Recent transcriptomic studies of astrocytes in chronic TBI revealed significant downregulation of cell adhesion genes, suggesting that adhesion molecule dysregulation accompanies astrocytic activation and is likely magnified in astrocytoma.

**Atomic biological processes**
- Homophilic cadherin-mediated cell-cell adhesion. Genes: CDH19, CTNNA3
  - [1]: Cell adhesion genes including CDH19 downregulated in chronic TBI astrocytes
- Immunoglobulin superfamily adhesion. Genes: CNTN2, CNTNAP4
  - [13]: Neuronal-glial communication through adhesion molecules affected by tumor microenvironment

**Atomic cellular components**
- Cadherin-catenin complex linkage to cytoskeleton. Genes: CDH19, CTNNA3
  - [1]: Cell adhesion complexes dysregulated in astrocyte transcriptome

**Required genes (not in input)**
- Genes: E-cadherin, N-cadherin
  - [1]: Cadherins essential for cell-cell adhesion

**Program citations**
- [1]: Cell adhesion genes dysregulated in astrocyte activation
- [13]: Neuronal-glial communication in tumor context

## Program: Axonal Guidance and Growth Cone Signaling
Program regulating axonal outgrowth, guidance, and growth cone dynamics through secreted and membrane-bound guidance cues and their receptors. Semaphorins and their plexin receptors constitute major components of this program, mediating both attractive and repulsive signals that shape neural circuit development and organization. In astrocytoma, dysregulation of axonal guidance contributes to peritumoral neuronal dysfunction and altered circuit connectivity.

**Predicted impacts**
- Altered axonal outgrowth and guidance in peritumoral region
- Aberrant circuit connectivity affecting neural function
- Enhanced immune cell recruitment through chemotactic mechanisms
- Disrupted tripartite synapse organization

**Evidence summary**
Semaphorins are a large family of secreted or membrane-associated proteins serving as guidance cues for axons and mediators of cell-cell communication. SEMA4D (semaphorin 4D) is expressed by immune cells and glial cells and participates in immune regulation and axonal guidance. In the context of astrocytoma, semaphorin dysregulation may contribute to altered axonal guidance in the peritumoral region, facilitating aberrant circuit connectivity and contributing to neurological symptoms including seizures.

**Atomic biological processes**
- Semaphorin-mediated axonal repulsion. Genes: SEMA4D
  - [13]: Peritumoral neurons exhibit altered electrophysiological properties and synaptic connections

**Required genes (not in input)**
- Genes: PLXN, UNC5
  - [13]: Plexin and Unc5 receptors essential for semaphorin signaling

**Program citations**
- [13]: Altered circuit organization in peritumoral region

## Program: Lysosomal Acidification and Autophagy Flux
Program maintaining lysosomal function through V-ATPase-mediated acidification of lysosomal lumen, enabling activation of lysosomal hydrolytic enzymes and supporting autophagy flux. Proper lysosomal function is essential for protein degradation, organellar turnover, and cellular homeostasis. Disruption of lysosomal acidification leads to accumulation of undegraded substrates and exacerbation of cellular stress responses.

**Predicted impacts**
- Impaired protein degradation and accumulation of misfolded proteins
- Reduced autophagy flux and organellar turnover
- Enhanced cellular stress responses and potential for proteostasis collapse
- Metabolic burden from incomplete protein turnover

**Evidence summary**
Recent research has emphasized the critical importance of lysosomal acidification for maintaining cellular homeostasis through proper protein degradation and organellar turnover. ASPA (aspartoacylase) participates in NAA metabolism relevant to glial function. QDPR (quinoid dihydrofolate reductase) maintains cellular redox balance. KLK6 (kallikrein 6) is a serine protease involved in proteolytic processing, and recent studies have identified KLK6 as a candidate biomarker for neurodegenerative disease with progressive downregulation during disease progression. Disruption of lysosomal acidification impairs protein degradation, leading to accumulation of undegraded substrates and exacerbation of cellular stress responses. In astrocytoma, dysregulation of this program contributes to the metabolic stress imposed by rapid tumor proliferation and enables selection for tumor cells with enhanced proteostatic capacity.

**Atomic biological processes**
- Lysosomal acidification and enzyme activation. Genes: ASPA, QDPR
  - [6]: V-ATPase maintains acidic lysosomal lumen essential for hydrolytic enzyme activation and cargo degradation
- Autophagy flux and cargo processing. Genes: ASPA, KLK6
  - [6]: V-ATPase plays critical roles in autophagy and endolysosomal dynamics

**Atomic cellular components**
- Lysosomal lumen and acidic compartments. Genes: ASPA, CA2
  - [6]: Lysosomal pH maintenance critical for proper organellar function

**Required genes (not in input)**
- Genes: ATP6V1, TFEB
  - [6]: V-ATPase essential for lysosomal acidification and TFEB regulates lysosomal biogenesis

**Program citations**
- [6]: Lysosomal acidification and V-ATPase function
- [14]: KLK6 as disease progression biomarker

## Program: Serine Protease-Mediated Proteolysis and Protease Inhibition
Program regulating proteolytic cleavage of proteins through serine proteases and their inhibitors, maintaining proteostasis and cellular protein composition. This program includes kallikrein-related peptidases involved in extracellular matrix remodeling, blood coagulation, and neuropeptide processing, as well as mechanisms for their regulation through serpin protease inhibitors.

**Predicted impacts**
- Altered extracellular matrix composition through dysregulated protease activity
- Impaired protein processing and neuropeptide generation
- Enhanced or reduced proteostatic burden depending on protease balance
- Altered ECM remodeling affecting tumor invasion and angiogenesis

**Evidence summary**
KLK6 (kallikrein-related peptidase 6) represents a serine protease involved in proteolytic processing with emerging roles in neural pathology. Recent multiomics studies identified KLK6 as progressively downregulated during spinocerebellar ataxia type 2 disease progression, suggesting that loss of KLK6 activity contributes to neurodegeneration through impaired proteolytic processing. ADAMTS proteases (ADAMTS4, ADAMTS18) represent additional serine proteases involved in extracellular matrix remodeling. The presence of these proteases in the astrocytoma gene list suggests dysregulation of proteolytic processing programs that affect both the tumor microenvironment composition and cellular protein degradation. While specific serpin inhibitors are not explicitly listed, the presence of serine proteases suggests dysregulation of protease inhibitory mechanisms as well.

**Atomic biological processes**
- Serine protease activity and regulation. Genes: KLK6
  - [14]: KLK6 progressively downregulated during disease progression; SERPINB1 regulates proteases including KLK6
- Protein substrate processing. Genes: KLK6, ADAMTS4, ADAMTS18
  - [14]: Dysregulation of protease family members correlates with neurodegeneration

**Required genes (not in input)**
- Genes: SERPINB1, SERPINA3
  - [14]: SERPINB1 regulates cathepsins and kallikrein-related peptidases in proteostasis

**Program citations**
- [14]: KLK6 progressive downregulation in neurodegeneration

## Program: Actin Cytoskeletal Dynamics and Cell Projection Organization
Program regulating actin polymerization, depolymerization, and remodeling to control cell morphology and projection formation. This program includes actin nucleators, polymerization promoting proteins, and regulatory factors that control the dynamic remodeling of actin cytoskeleton. Astrocytes characteristically exhibit extensive branching processes maintained through this program; loss of these morphological features accompanies malignant transformation.

**Predicted impacts**
- Altered astrocyte morphology from branched to rounded appearance
- Enhanced cell motility and invasive capacity
- Loss of astrocytic process interactions with neurons and synapses
- Reduced capacity for metabolic substrate distribution through processes

**Evidence summary**
Astrocytes are morphologically complex cells characterized by extensive branching processes that extend throughout neural tissue. This morphology is essential for astrocytic functions including metabolic support of neurons and synaptic regulation. The provided gene list includes regulators of actin dynamics critical for cell projection formation. COBL (cordon-bleu) nucleates and regulates actin filaments promoting process formation and elongation. SHROOM4 (shroom family member 4) regulates cell shape changes through actin-binding mechanisms. SLAIN1 (SLAIN motif family member 1) participates in microtubule dynamics and cellular architecture. CSRP1 (cysteine and glycine-rich protein 1) is an actin-binding protein regulating cytoskeletal dynamics. DAAM2 (disheveled-associated activator of morphogenesis 2) promotes actin polymerization. The dramatic morphological changes accompanying malignant transformation of astrocytes—from complex branching cells to rounded tumor cells—are enabled by dysregulation of these actin and cytoskeletal programs.

**Atomic biological processes**
- Actin filament nucleation and polymerization. Genes: COBL, DAAM2
  - [1]: Cell projection organization genes dysregulated in astrocyte activation
- Cell morphology and motility control. Genes: SHROOM4, SLAIN1
  - [1]: Cell projection organization involves cytoskeletal reorganization

**Atomic cellular components**
- Actin filament structures. Genes: COBL, SHROOM4, SLAIN1, CSRP1
  - [1]: Cell projection organization related to actin dynamics

**Required genes (not in input)**
- Genes: ARP2/3, Profilin
  - [1]: Essential for actin polymerization and cell projection formation

**Program citations**
- [1]: Cell projection organization genes in astrocyte activation

## Program: Microtubule Organization and Intracellular Vesicular Transport
Program regulating microtubule dynamics, stability, and motor-driven transport of intracellular vesicles and organelles. Microtubules form the primary tracks for long-distance intracellular transport and are essential for establishing cell polarity, forming cilia, and enabling specialized cellular morphologies. Dysregulation of this program in astrocytoma affects cellular architecture, organellar distribution, and trafficking of signaling molecules.

**Predicted impacts**
- Altered intracellular transport and organellar distribution
- Impaired trafficking of signaling molecules to specific cellular compartments
- Enhanced or reduced cell migration capacity
- Disrupted metabolic substrate trafficking to neuronal support sites

**Evidence summary**
Microtubule-based intracellular transport is essential for astrocytic function, enabling distribution of metabolic substrates through branching processes and trafficking of signaling molecules to specific cellular compartments. MAP7 (microtubule associated protein 7) regulates microtubule stability and intracellular vesicular transport. TPPP (tubulin polymerization promoting protein) promotes microtubule assembly and stability. KIF6 (kinesin family member 6) encodes a kinesin motor protein driving microtubule-based transport. TUBB4A encodes beta-tubulin 4a, a microtubule structural component. DNAJC6 encodes auxilin, a co-chaperone involved in clathrin coat disassembly and vesicular trafficking. These genes collectively establish programs for regulating microtubule dynamics and enabling the complex intracellular trafficking required for astrocytic function.

**Atomic biological processes**
- Microtubule stabilization and dynamics. Genes: MAP7, TPPP
  - [1]: Cell projection organization involves microtubule dynamics
- Motor protein-driven transport. Genes: KIF6, DNAJC6
  - [15]: KLC1 binds phosphorylated GLUT3 enabling kinesin-driven transport of GLUT3 to plasma membrane

**Atomic cellular components**
- Microtubule cytoskeleton. Genes: MAP7, TPPP, TUBB4A
  - [1]: Microtubule components dysregulated in astrocyte activation

**Required genes (not in input)**
- Genes: Dynein, DCTN1
  - [15]: Motor proteins essential for vesicular transport

**Program citations**
- [1]: Cell projection organization involving microtubule dynamics
- [15]: KLC1-mediated kinesin transport of GLUT3

## Program: Potassium Channel Regulation and Osmotic Homeostasis
Program controlling extracellular potassium concentration and maintaining osmotic balance through potassium channel expression and regulation. Astrocytes are critical for extracellular potassium buffering, preventing accumulation of extracellular K+ that would cause neuronal hyperexcitability and seizures. This program includes potassium channels, osmolarity sensors, and ions channel regulatory kinases.

**Predicted impacts**
- Impaired extracellular potassium buffering leading to hyperexcitability
- Enhanced seizure susceptibility through K+ dysregulation
- Altered osmotic balance in tumor microenvironment
- Disrupted volume homeostasis and cellular swelling

**Evidence summary**
Astrocytes play a critical role in maintaining extracellular ion concentrations, particularly potassium, which must be tightly regulated to prevent neuronal hyperexcitability and seizures. The provided gene list includes genes encoding potassium channels and osmotic regulatory factors. KCNK1 (potassium two pore domain channel subfamily K member 1) and KCNMB4 (potassium calcium-activated channel subfamily M regulatory beta subunit 4) encode components of potassium channel complexes involved in astrocytic uptake of excess extracellular potassium. SGK1 (serum and glucocorticoid-regulated kinase 1) is a kinase involved in regulating ion channel function and osmotic homeostasis. ATP1B1 (ATPase Na+/K+ transporting subunit beta 1) is the regulatory subunit of the Na+/K+ ATPase, essential for maintaining ion gradients. Recent studies have identified that astrocytes contain a TRPV4/AQP4 complex that functions as a key osmosensor coupling osmotic stress to cellular response mechanisms. Dysregulation of ion homeostasis in astrocytomas contributes to the osmotic stress characteristic of solid tumors and may exacerbate seizure susceptibility.

**Atomic biological processes**
- Extracellular potassium buffering. Genes: KCNK1, KCNMB4, SGK1
  - [5]: Astrocytes contain TRPV4/AQP4 complex that functions as osmosensor coupling osmotic stress to cellular response
- Osmotic homeostasis regulation. Genes: SGK1, ATP1B1
  - [5]: TRPV4/AQP4 complex couples osmotic stress to cellular responses through volume homeostasis mechanisms

**Atomic cellular components**
- Potassium channel complexes. Genes: KCNK1, KCNMB4
  - [5]: Ion channel regulation critical for astrocytic function

**Required genes (not in input)**
- Genes: AQP4, TRPV4
  - [5]: Core components of osmotic homeostasis in astrocytes

**Program citations**
- [5]: TRPV4/AQP4 complex in astrocytic osmosensing

## Program: Synaptic Organization and Neuronal-Astrocytic Tripartite Synapse
Program organizing and maintaining tripartite synapses wherein astrocytic processes directly contact and regulate neuronal synapses. This program includes synaptic scaffolding proteins, contact site organization factors, and molecules regulating astrocytic influence on synaptic transmission. Astrocytes regulate synaptic transmission, plasticity, and neuronal activity through processes at tripartite synapses.

**Predicted impacts**
- Disrupted synaptic transmission through altered astrocytic regulation
- Loss of astrocytic modulation of synaptic plasticity
- Aberrant neuronal activity patterns promoting seizures
- Impaired astrocytic control of neurotransmitter homeostasis at synapses

**Evidence summary**
Astrocytes form intimate contacts with neuronal synapses through tripartite synapse structures wherein astrocytic processes directly contact and regulate synaptic transmission. This program includes genes encoding synaptic scaffolding proteins and contact site organization factors. CNTNAP4 (contactin-associated protein-like 4) is an immunoglobulin superfamily adhesion molecule involved in synapse organization. DLG2 (discs large MAGUK scaffold protein 2) is a MAGUK scaffolding protein organizing synaptic signaling complexes. ANK3 (ankyrin 3, ankyrin-G) links membrane proteins to the spectrin-actin cytoskeleton at synaptic sites. Recent studies have identified that specific astrocyte populations produce synaptogenic factors linked to tumor-associated seizures, and that astrocyte-mediated regulation of peritumoral neuronal activity is significantly altered in gliomas. Dysregulation of tripartite synapse organization in astrocytomas contributes to aberrant neuronal activity patterns and seizure development.

**Atomic biological processes**
- Synaptic contact and organization. Genes: CNTNAP4, DLG2, ANK3
  - [13]: Synaptogenic factors from astrocytes linked to tumor-associated seizures
- Astrocyte-synapse interactions. Genes: CNTNAP4, SEMA4D
  - [13]: Astrocyte-produced factors regulate peritumoral neuronal activity

**Atomic cellular components**
- Synaptic scaffold complexes. Genes: DLG2, ANK3
  - [13]: Synaptic organization dysregulated in peritumoral region

**Required genes (not in input)**
- Genes: Neuroligin, Neurexin
  - [13]: Essential for synaptic organization

**Program citations**
- [13]: Astrocytic synaptogenic factors and peritumoral neuronal dysfunction

## Program: Extracellular Matrix Remodeling and Perineuronal Net Organization
Program regulating composition, organization, and remodeling of the extracellular matrix through production of matrix components, matrix metalloproteases, and their inhibitors. This program controls mechanical properties of the brain microenvironment and organizes perineuronal nets—specialized ECM structures regulating synaptic plasticity. Aberrant ECM remodeling in astrocytoma promotes invasion, angiogenesis, and altered neural tissue mechanics.

**Predicted impacts**
- Altered tumor microenvironment mechanical properties promoting invasion
- Enhanced angiogenesis through ECM remodeling
- Disrupted perineuronal nets affecting synaptic plasticity
- Increased interstitial pressure and fluid dynamics affecting neural tissue

**Evidence summary**
The extracellular matrix organization program encompasses both production of matrix components and regulated degradation through matrix metalloproteases. ADAMTS4 and ADAMTS18 are secreted metalloproteases involved in ECM remodeling and perineuronal net component degradation. HAPLN2 (hyaluronan and proteoglycan link protein 2) stabilizes interactions between hyaluronic acid and proteoglycans, contributing to perineuronal net organization and stability. Perineuronal nets are specialized ECM structures surrounding neuronal cell bodies and synapses that regulate synaptic plasticity and the closing of critical periods for developmental plasticity. In astrocytomas, aberrant ECM remodeling has been associated with enhanced invasion and tumor progression. Recent studies demonstrate that astrocytes in gliomas produce chemokines and ECM-modifying enzymes supporting tumor progression. The presence of ECM remodeling genes in the astrocytoma list suggests dysregulation of these programs promotes invasion and angiogenesis.

**Atomic biological processes**
- Extracellular matrix component production. Genes: ADAMTS4, ADAMTS18, HAPLN2
  - [17]: Astrocytes express ECM components including CXCL15 supporting tumor progression
- Matrix metalloprotease activity. Genes: ADAMTS4, ADAMTS18
  - [17]: Matrix remodeling in tumor microenvironment supports glioma progression

**Atomic cellular components**
- Perineuronal net structures. Genes: HAPLN2, ADAMTS4, ADAMTS18
  - [1]: ECM organization genes dysregulated in astrocyte transcriptome

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP
  - [17]: Matrix metalloproteases essential for ECM remodeling

**Program citations**
- [17]: ECM remodeling in glioma progression

## Program: Phospholipid Metabolism and Bioactive Lipid Signaling
Program regulating phospholipid metabolism and generation of bioactive lipid mediators that serve as ligands for G protein-coupled receptors and as signaling molecules controlling cell proliferation, migration, and immune responses. This program includes enzymes synthesizing lysophosphatidic acid, phosphatidic acid, and eicosanoids, as well as receptors and binding proteins for these lipids.

**Predicted impacts**
- Enhanced tumor cell migration and invasive capacity
- Increased immune cell recruitment to tumor microenvironment
- Dysregulated cell proliferation through lipid-mediated signaling
- Enhanced angiogenesis through lipid mediator production
- Altered inflammatory responses through prostaglandin dysregulation

**Evidence summary**
The phospholipid metabolism program generates bioactive lipid mediators that profoundly influence cell behavior and immune responses. ENPP2 (ectonucleotide pyrophosphatase/phosphodiesterase 2), also known as autotaxin, catalyzes generation of lysophosphatidic acid (LPA) from lysophosphatidylcholine. LPA acts through G protein-coupled receptors including LPAR1 (lysophosphatidic acid receptor 1) to promote cell migration, proliferation, and survival. PLD1 (phospholipase D1) generates phosphatidic acid (PA), another bioactive signaling lipid. PLAT3 (phospholipase A2, membrane associated 3) releases arachidonic acid and lysophospholipids, substrates for eicosanoid synthesis. PTGDS (prostaglandin D synthase) catalyzes synthesis of prostaglandin D2 (PGD2), a potent inflammatory mediator and metabolic regulator. The ENPP2-LPA-LPAR1 axis is significantly dysregulated in many cancer types, including glioblastoma, where it promotes tumor cell migration, angiogenesis, and immune cell recruitment. The presence of these lipid-metabolizing genes in the astrocytoma gene list suggests that dysregulation of bioactive lipid signaling contributes to tumor progression and immune cell infiltration.

**Atomic biological processes**
- Lysophosphatidic acid synthesis and signaling. Genes: ENPP2, LPAR1, PLAT3
  - [17]: Lipid-mediated signaling promotes glioma cell migration and immune cell recruitment
- Phosphatidic acid generation. Genes: PLD1, PLAT3
  - [17]: Bioactive lipids support tumor cell proliferation and survival
- Prostaglandin synthesis. Genes: PTGDS
  - [1]: Inflammatory pathways dysregulated in astrocyte activation

**Required genes (not in input)**
- Genes: COX2, LTC4S
  - [17]: Inflammatory lipid mediator synthesis

**Program citations**
- [17]: Lipid-mediated signaling in glioma progression

## Bibliography
1. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
2. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
3. Available from: https://www.ncbi.nlm.nih.gov/gene/6663
4. Available from: https://www.ncbi.nlm.nih.gov/gene/18088
5. Available from: https://www.ncbi.nlm.nih.gov/gene/361
6. Kim S-H, Cho Y-S, Jung Y-K. Failure of lysosomal acidification and endomembrane network in neurodegeneration. Experimental &amp; Molecular Medicine [Internet]. 2025Nov18;57(11). Available from: https://www.nature.com/articles/s12276-025-01579-x
7. Available from: https://www.ncbi.nlm.nih.gov/gene/11816
8. Available from: https://www.ncbi.nlm.nih.gov/gene/11820
9. Available from: https://www.ncbi.nlm.nih.gov/gene/14912
10. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
11. Available from: https://www.ncbi.nlm.nih.gov/gene/894
12. Available from: https://www.ncbi.nlm.nih.gov/gene/84504
13. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
14. Almaguer-Mederos LE, Key J, Sen N-E, Canet-Pons J, Döring C, Meierhofer D, et al.. Multiomics approach identifies SERPINB1 as candidate biomarker for spinocerebellar ataxia type 2. Scientific Reports [Internet]. 2025Nov26;15(1). Available from: https://www.nature.com/articles/s41598-025-29070-7
15. Wei X-Y, Zou Z-M, Yao Z-X, Teng S-W, Wei X-Y, Tang W-J, et al.. Neuronal activity-induced GLUT3 plasma translocation supports energy demands for memory acquisition. Communications Biology [Internet]. 2025Nov28;8(1). Available from: https://www.nature.com/articles/s42003-025-09119-z
16. Ye J, Wang H, Peng Y, Wang S, Zheng R, Chen Y, et al.. Noncanonical role of astrocytic mitochondrial Cx43: suppressing IDH3α to sustain glycolytic homeostasis against depression. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08309-1
17. Han Y, Han M, Wang T, Zhang H, Liu H, Zheng Y, et al.. Inhibiting the formation of neutrophil extracellular traps to prevent the recurrence of post-operative glioblastoma. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-65933-3
18. Available from: https://www.ncbi.nlm.nih.gov/gene/65078
19. Available from: http://json-schema.org/draft-07/schema#",
