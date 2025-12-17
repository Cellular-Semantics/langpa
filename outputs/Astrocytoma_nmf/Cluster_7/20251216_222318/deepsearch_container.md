# Gene Program Markdown Report

## Context
- Cell type: Astrocyte
- Disease: Astrocytoma
- Tissue: Brain

## Input Genes
CAMK2D, MIR4435-2HG, CDK6, CYTOR, CHRM3, RGS6, KIAA1211L, KLHL4, CDH2, HIVEP3, SPRY4, TRIO, ADAMTS9, WWTR1, SPRED2, VAV3, PLAT, SATB2, CHRM3-AS2, SIPA1L1, GAP43, KCNIP1, PCNX2, GRIA3, ILDR2, ... (200 total)

## Program: Integrin-Mediated Cell Adhesion and Mechanotransduction
This program orchestrates cellular interactions with the extracellular matrix and neighboring cells through integrin heterodimers, focal adhesion complexes, and downstream mechanotransduction signaling. Integrin alpha and beta subunits form heterodimeric complexes that bind extracellular matrix ligands (collagen, laminin, fibronectin) and transduce mechanical tension into biochemical signals that control cell migration, invasion, and gene expression through FAK and YAP/TAZ signaling. Talin proteins directly link integrins to the actin cytoskeleton and sense mechanical forces. Laminin and collagen chains serve as primary ECM ligands. This program is dysregulated in astrocytomas to promote invasion through tumor-infiltrated brain parenchyma and blood vessels.

**Predicted impacts**
- Enhanced focal adhesion assembly and stability in response to ECM stiffness
- Increased cell migration velocity and invasive capacity
- Mechanically-dependent YAP/TAZ nuclear localization and growth-promoting gene expression
- Sustained cell-matrix adhesion enabling invasion through restrictive brain parenchyma

**Evidence summary**
Integrin-mediated mechanotransduction is a critical regulator of cancer cell migration and invasion. The input list contains multiple components of the integrin signaling cascade and ECM composition, suggesting coordinated dysregulation of cell adhesion in astrocytomas. High-grade gliomas exhibit enhanced expression of alpha-3 and alpha-7 integrins and their ligands, enabling invasion. Mechanotransduction through integrin signaling controls FAK activation and YAP nuclear translocation, both pro-tumoral outputs. The presence of multiple ECM component genes (laminin, collagen) alongside integrin subunits and signaling effectors suggests that astrocytomas coordinate cell-autonomous integrin signaling with remodeling of the ECM niche to support invasion and establish supportive microenvironments.

**Atomic biological processes**
- Integrin-mediated cell adhesion. Genes: ITGA3, ITGA7, ITGB8, LAMC1, LAMA2, LAMA4, LIMK1
  - [56]: Describes talin-integrin-actin linkage and mechanotransduction, including paxillin phosphorylation and YAP/TAZ nuclear translocation downstream of integrin signaling
- Focal adhesion assembly and turnover. Genes: ITGA3, ITGA7, ITGB8, LIMK1, ARHGAP26
  - [56]: Discusses FAK activation through paxillin Y118 phosphorylation and focal adhesion complex dynamics
- Mechanotransduction and YAP signaling. Genes: ITGA3, ITGA7, ITGB8, WWTR1, LIMK1
  - [56]: YAP translocation to nucleus as downstream mechanotransduction output regulated by talin rod domain and FAK signaling

**Atomic cellular components**
- Integrin heterodimers. Genes: ITGA3, ITGA7, ITGB8
  - [56]: Integrin heterodimers consisting of alpha and beta subunits activate in response to mechanical tension through talin binding
- Extracellular matrix scaffolds. Genes: LAMC1, LAMA2, LAMA4, COL4A2, COL22A1
  - [56]: Laminin and collagen components of basement membrane and ECM that serve as integrin ligands

**Required genes (not in input)**
- Genes: FAK, Src, Paxillin, Talin
  - [56]: FAK, Src-family kinases, paxillin, and talin proteins are essential focal adhesion components not present in input list but required for integrin mechanotransduction

**Program citations**
- [56]: Primary source demonstrating talin force coupling, FAK-paxillin signaling, and YAP translocation downstream of integrin-talin-actin complexes

## Program: Rho GTPase Signaling and Actin Dynamics
The Rho GTPase signaling program controls actin cytoskeleton dynamics, cell migration, and invasion through a sophisticated network of GEFs (guanine nucleotide exchange factors), GAPs (GTPase-activating proteins), and downstream effectors. RhoA, Rac1, and Cdc42 function as molecular switches toggling between active GTP-bound and inactive GDP-bound states. GEFs promote activation by catalyzing GDP-to-GTP exchange. GAPs inactivate GTPases through GTP hydrolysis. Negative feedback regulators (RGS, Sprouty, Spred) suppress Rho activation downstream of growth factor receptors. Enhanced Rho signaling drives stress fiber formation, cell contractility, and invasion in astrocytomas.

**Predicted impacts**
- Uncontrolled RhoA activation driving excessive stress fiber formation and contractility
- Enhanced cell migration velocity and invasion through ECM
- Suppressed negative feedback through RGS and Sprouty downregulation or mutation
- Dysregulated Rac1/Cdc42 signaling affecting cellular protrusions and directional migration

**Evidence summary**
Rho GTPase signaling is dysregulated in high-grade gliomas to promote migration and invasion. The input list contains multiple GEFs, GAPs, and negative feedback regulators, suggesting a complex regulatory landscape where pro-migration signals (GEFs) may overcome inhibitory signals (GAPs, RGS proteins). Silencing of Drp1 inhibits glioma proliferation and invasion through RHOA/ROCK1 pathway suppression, directly implicating Rho signaling in astrocytoma progression. The presence of multiple negative feedback regulators (RGS, Sprouty, Spred, DUSP6) suggests that dysregulation of these brakes—either through downregulation or mutation—represents a key event in astrocytoma transformation. Enhanced Rho signaling promotes stress fiber formation, cell contractility, and invasion-permissive morphologies.

**Atomic biological processes**
- RhoA activation and stress fiber formation. Genes: RHOJ, ARHGEF26, TRIO, DLC1, ARHGAP26, SIPA1L1, VAV3, LIMK1
  - [34]: ROCK1 pathway controls stress fiber formation and cell contractility downstream of RhoA activation, implicated in glioma cell migration and invasion
- Rac1 and Cdc42 activation. Genes: VAV3, TRIO, PREX1, ARHGAP26
  - [7]: SDF-1alpha stimulates CXCR4/PI3K/Rac1 pathway affecting actin dynamics and endothelial permeability; high Rac-1 expression promoted cell migration
- Negative feedback suppression of Rho signaling. Genes: SPRY4, SPRY2, SPRED2, SPRED1, RGS6, RGS17, DUSP6
  - [55]: SPRY2 regulates ERK-MAPK signaling through miR-21-mediated mechanism; sprouty and spred proteins suppress RTK signaling that activates Rho pathways
  - [58]: MYB regulates SPRY2 transcription as negative feedback on MAPK signaling

**Atomic cellular components**
- Rho GTPase exchange factors. Genes: ARHGEF26, TRIO, VAV3, PREX1
  - [7]: GEFs catalyze GDP-to-GTP exchange to activate Rho family GTPases
- Rho GTPase-activating proteins. Genes: DLC1, ARHGAP26, SIPA1L1
  - [12]: DLC1 SAM domain-binding peptides inhibit cancer cell migration by inactivating RhoA through GAP activity
- Actin-binding and cytoskeletal regulators. Genes: LIMK1, SHROOM3, TRIM9
  - [56]: Actin polymerization controlled by cofilin phosphorylation via LIMK and downstream Rho signaling

**Required genes (not in input)**
- Genes: ROCK1, PAK, Cofilin, Paxillin
  - [34]: ROCK1 is the major effector of RhoA-mediated stress fiber formation, essential for the Rho-ROCK pathway in glioma invasion

**Program citations**
- [34]: Silencing Drp1 inhibits glioma proliferation and invasion via RHOA/ROCK1 pathway
- [12]: DLC1 inactivates RhoA to inhibit cancer cell migration
- [7]: Rac1 pathway activated by CXCR4 signaling affects actin dynamics

## Program: Kinase Signaling Cascades and Cell Cycle Progression
The kinase signaling program encompasses cyclin-dependent kinases (CDKs), mitogen-activated protein kinases, calcium/calmodulin-dependent kinases, and receptor tyrosine kinases that collectively control cell cycle progression, survival, proliferation, and differentiation. CDK6 drives G1-to-S phase transition when activated by cyclin D complexes. Calcium-dependent kinases (CAMK2B, CAMK2D) integrate calcium signals to control gene expression and metabolism. Serine-threonine kinases (STK family members) participate in diverse signaling cascades. ALK, a receptor tyrosine kinase, when dysregulated through fusion or amplification, drives constitutive kinase signaling. MAP3K1 sits upstream of MAPK/ERK and JNK cascades. These kinases are frequently dysregulated in astrocytomas to promote uncontrolled proliferation and survival.

**Predicted impacts**
- Accelerated cell cycle progression through G1-S checkpoint
- Enhanced survival signaling through PI3K-Akt-mTOR pathway
- Dysregulation of MAPK/ERK signaling downstream of kinase activation
- Altered calcium signaling affecting metabolism, migration, and differentiation
- Constitutive ALK signaling (if dysregulated) driving proliferation and transformation

**Evidence summary**
Kinase dysregulation is a hallmark of astrocytoma and other cancers. CDK6 is frequently amplified in high-grade gliomas, driving aberrant G1-S progression. CAMK-dependent signaling integrates calcium influx through NMDA and AMPA glutamate receptors (themselves dysregulated in gliomas) to drive proliferation and migration. ALK fusion events, while more common in lung cancers and lymphomas, have been reported in neural tumors and drive constitutive MAPK and PI3K pathway activation. MAP3K1 sits upstream of multiple effector kinases, integrating growth factor and stress signals. The presence of multiple kinases in the input list suggests that astrocytomas employ multiple redundant pathways to overcome cell cycle checkpoints and survival constraints, a common mechanism of cancer progression.

**Atomic biological processes**
- G1-to-S phase transition. Genes: CDK6, CDK14
  - [5]: CDK6 controls G1-to-S phase transition; cyclin-CDK complexes are frequently dysregulated in cancer
- Calcium-dependent signaling and plasticity. Genes: CAMK2B, CAMK2D, TRPM3, GRIN2B, GRIA3
  - [40]: GLUT3 neuronal activity-dependent plasma translocation regulated by PKCε phosphorylation of T232 and S246; PKCε is a calcium-dependent kinase
- Receptor tyrosine kinase signaling. Genes: ALK, FGFR1, MAP3K1
  - [19]: EML4-ALK fusion drives cellular senescence in normal cells and anchorage-independent growth in immortalized cells; ALK promotes MAPK and PI3K pathway activation
- PI3K-Akt-mTOR pathway activation. Genes: PREX1, MAP3K1, STK17A, STK32A, STK32B
  - [13]: KRAS gene silencing inhibits PI3K-Akt-mTOR signaling to regulate breast cancer cell proliferation, EMT, and invasion; this pathway is central to cancer biology

**Atomic cellular components**
- Cyclin-CDK complexes. Genes: CDK6, CDK14
  - [5]: CDKs form catalytic cores of cell cycle checkpoints
- Calcium-calmodulin signaling complexes. Genes: CAMK2B, CAMK2D
  - [40]: Calcium-calmodulin-dependent protein kinases integrate calcium signals

**Required genes (not in input)**
- Genes: Cyclin D1, Cyclin D2, FAK, ERK1/2, Akt
  - [13]: Cyclin-CDK and Akt are essential components of proliferation pathways often dysregulated in cancer

**Program citations**
- [13]: KRAS-mediated PI3K-Akt-mTOR signaling controls cancer proliferation
- [19]: ALK-mediated transformation drives both senescence and growth depending on cellular context
- [40]: CAMK-mediated signaling in neuronal context

## Program: MAPK/ERK Feedback Suppression and Pathway Regulation
The MAPK/ERK pathway represents one of the central growth-promoting cascades in cancer, driving proliferation, survival, and differentiation. However, this pathway is subject to extensive negative feedback regulation through multiple mechanisms. The input list contains four key negative regulators: SPRY2, SPRY4, SPRED1, and SPRED2, collectively termed sprouty and spred proteins; and DUSP6, a dual-specificity phosphatase that directly dephosphorylates ERK1/2. These negative feedback regulators suppress MAPK/ERK signaling in response to growth factors and stress signals. Dysregulation of these suppressors—through loss of expression, mutations, or epigenetic silencing—combined with upstream kinase activation, creates a permissive environment for sustained MAPK signaling in astrocytomas.

**Predicted impacts**
- Loss or reduction of MAPK/ERK negative feedback allows sustained signaling
- Enhanced proliferation and survival downstream of MAPK/ERK
- Increased transcription of proliferation-associated genes (c-MYC, cyclin D1, etc.)
- Altered differentiation status favoring undifferentiated or progenitor-like phenotypes
- Potential vulnerability to MAPK pathway inhibitors if suppressor downregulation is the primary defect

**Evidence summary**
The presence of multiple MAPK/ERK negative feedback regulators in the input list is striking and suggests that dysregulation of these suppressors represents a key event in astrocytoma pathogenesis. In normal cells, MAPK/ERK signaling triggers negative feedback through sprouty and DUSP upregulation, establishing a 'toggle switch' that prevents excessive signaling. In astrocytomas, downregulation or loss of these suppressors (which can occur through mutations, epigenetic silencing, or transcriptional dysregulation) would allow sustained MAPK signaling even in the absence of continuous growth factor stimulation. This mechanism is complementary to upstream kinase activation (through RAS mutations, BRAF mutations, or RTK amplification) and together they create a robust, redundantly-controlled permissive environment for proliferation.

**Atomic biological processes**
- MAPK/ERK pathway suppression. Genes: SPRY2, SPRY4, SPRED1, SPRED2, DUSP6
  - [55]: SPRY2 regulates ERK-MAPK signaling pathway through miR-21-mediated mechanism during differentiation
  - [58]: SPRY2 is a novel unfolded protein response regulator that may suppress MAPK signaling
- RTK signaling antagonism. Genes: SPRY2, SPRY4, SPRED1, SPRED2
  - [55]: Sprouty proteins antagonize RTK signaling through multiple mechanisms including Grb2 sequestration

**Atomic cellular components**
- Phosphatase complexes. Genes: DUSP6
  - [55]: DUSP6 is a dual-specificity phosphatase that directly inactivates ERK1/2
- Negative feedback regulator complexes. Genes: SPRY2, SPRY4, SPRED1, SPRED2
  - [55]: Sprouty proteins form signaling complexes that suppress RTK-mediated signaling

**Required genes (not in input)**
- Genes: ERK1, ERK2, MEK1, MEK2, RAF
  - [55]: ERK and MEK are essential components of the MAPK cascade regulated by feedback suppressors

**Program citations**
- [55]: SPRY2 regulates MAPK signaling through RTK pathway antagonism
- [58]: MYB directly regulates SPRY2 transcription as negative feedback on MAPK

## Program: Calcium Signaling and Ion Homeostasis
Calcium signaling represents a fundamental communication mechanism in astrocytes, coupling extracellular and intracellular signals to control gene expression, metabolism, migration, and neuron-astrocyte interactions. The input list contains multiple calcium signaling components: inositol 1,4,5-trisphosphate receptors (ITPR2), ryanodine receptors (RYR3), voltage-gated calcium and potassium channels (TRPM3, KCNMA1, KCND2), glutamate receptors that gate calcium influx (GRIN2B, GRIA3, GRIK2), and calcium/calmodulin-dependent kinases (CAMK2B, CAMK2D). Dysregulation of calcium signaling in astrocytomas promotes metabolic reprogramming, migration, and aberrant neuron-tumor interactions.

**Predicted impacts**
- Dysregulated intracellular calcium homeostasis promoting mitochondrial dysfunction
- Altered calcium-dependent gene expression through CAMK and CREB pathways
- Enhanced migration through calcium-dependent cytoskeletal remodeling
- Aberrant calcium signaling promoting metabolic reprogramming
- Aberrant neuron-astrocyte calcium coupling promoting seizures and peritumoral neuronal dysfunction

**Evidence summary**
Calcium signaling is fundamentally dysregulated in astrocytomas. ITPR2, a key component of ER calcium release, drives mitochondrial calcium accumulation and mitochondrial permeability transition pore activation, leading to reduced mitochondrial membrane potential, ROS production, and cell dysfunction. In the context of cancer, dysregulation of calcium signaling can promote metabolic reprogramming (particularly toward glycolysis), affect survival signaling, and enhance migration. The presence of glutamate receptor subunits in astrocytomas is particularly striking, as it suggests that tumor cells may directly respond to synaptic glutamate or even express and release glutamate themselves, creating aberrant calcium-dependent signaling that affects both tumor cells and neighboring neurons. Recent evidence demonstrates that astrocytic mitochondrial connexin-43 directly regulates IDH3α to maintain glycolytic metabolism and lactate production for neuronal energy supply; dysregulation of this coupling in astrocytomas would promote metabolic reprogramming. The calcium signaling program is therefore predicted to promote metabolic reprogramming, migration, and pathological neuron-tumor interactions.

**Atomic biological processes**
- ER calcium release and IP3 signaling. Genes: ITPR2
  - [21]: ITPR2-mediated calcium release from ER leads to mitochondrial calcium uptake via MCU during stress, causing accumulation and reduced ΔΨm; ITPR2 knockdown prevents senescence induction
  - [22]: Chronic hyperglycemia disrupts neuronal function through intracellular calcium imbalance and ER stress
- Mitochondrial calcium handling. Genes: ITPR2, RYR3
  - [21]: Calcium accumulation in mitochondrial matrix activates permeability transition pore (mPTP), causing collapse of ΔΨm and ROS production
- Glutamate receptor-mediated calcium influx. Genes: GRIN2B, GRIA3, GRIK2
  - [42]: Glioma-derived glutamate acting through neuronal NMDA and AMPA receptors alters neuronal excitability; tumor cells with aberrant glutamate receptor expression may dysregulate calcium
- GPCR-mediated calcium signaling. Genes: CHRM3, P2RY14
  - [2]: Muscarinic M1 receptor mediates cholinergic regulation and calcium signaling in hippocampus
- Calcium-dependent gene expression. Genes: CAMK2B, CAMK2D, CREB5
  - [40]: PKCε phosphorylates GLUT3 in calcium-dependent manner to regulate neuronal glucose uptake; CAMK kinases integrate calcium signals for gene expression

**Atomic cellular components**
- Endoplasmic reticulum calcium channels. Genes: ITPR2
  - [21]: ITPR2 is a calcium channel at ER and MERCS (mitochondria-ER contact sites)
- Ryanodine receptor calcium channels. Genes: RYR3
  - [21]: RYR3 is a calcium-release channel in ER, related to ryanodine receptors
- Voltage-gated ion channels. Genes: TRPM3, KCNMA1, KCND2
  - [40]: Voltage-gated calcium and potassium channels regulate cellular excitability and calcium homeostasis
- Ligand-gated glutamate receptors. Genes: GRIN2B, GRIA3, GRIK2
  - [42]: NMDA and AMPA receptors gate calcium influx in response to synaptic glutamate

**Required genes (not in input)**
- Genes: MCU, NCX, PMCA, STIM1, Connexin-43
  - [21]: MCU (mitochondrial calcium uniporter) is essential for mitochondrial calcium uptake; NCX and PMCA are calcium exchangers; STIM1 couples ER calcium depletion to store-operated calcium entry

**Program citations**
- [21]: ITPR2-mediated calcium signaling and mitochondrial dysfunction in cellular senescence
- [42]: Glioma-derived glutamate acting through neuronal receptors and aberrant astrocyte calcium signaling
- [43]: Astrocytic mitochondrial Cx43 regulates IDH3α and metabolic coupling to neurons

## Program: Synaptic Plasticity and Neuron-Tumor Interaction
A substantial subset of the input gene list encodes proteins classically associated with synaptic function, synaptic plasticity, and neuron-astrocyte interactions. These include growth-associated protein 43 (GAP43), synaptojanin-2 (SYNJ2), neuronal cell adhesion molecules (NRCAM, CHL1, LSAMP), glutamate receptors (GRIA3, GRIN2B, GRIK2), and related signaling proteins. The presence of these synaptic genes in astrocytomas is striking and suggests either that tumors retain developmental neural programs or that they actively dysregulate synaptic genes to manipulate the neuronal microenvironment. High-grade gliomas promote seizures and neuronal dysfunction in peritumoral regions, effects mediated through aberrant astrocyte-neuron communication.

**Predicted impacts**
- Enhanced tumor-derived glutamate release affecting neuronal excitability
- Aberrant astrocyte-neuron calcium coupling promoting seizures
- Dysregulated synaptic plasticity in peritumoral regions
- Altered neuronal function through aberrant cell-cell interactions
- Impaired neuronal integrity potentially reducing anti-tumor immunity

**Evidence summary**
Recent studies have revealed that high-grade gliomas promote aberrant neuronal activity and seizures through multiple mechanisms, including glutamate dysregulation and altered astrocyte-neuron interactions. Glioma cells cause elevation of local glutamate concentration and alter neuronal excitability via the xCT transporter system and glutamate receptor activation. Furthermore, synaptogenic factors produced by specific astrocyte populations have been linked to tumor-associated seizures. The presence of glutamate receptor subunits, cell adhesion molecules, and synaptic proteins in the input astrocytoma gene list suggests that neoplastic astrocytes retain or dysregulate programs of neural development and astrocyte-neuron interaction. This dysregulation may serve tumoral functions by promoting peritumoral neuronal dysfunction, suppressing anti-tumor neuronal activity, or creating a permissive microenvironment for tumor growth. The synaptic program is therefore predicted to dramatically alter neuron-tumor crosstalk, promoting seizures, neuronal dysfunction, and a permissive neuronal microenvironment for tumor progression.

**Atomic biological processes**
- Synaptic plasticity and axonal growth. Genes: GAP43, SYNJ2, DPP6
  - [47]: GAP43 expression pattern correlates with regenerative capacity; reduced expression in Parkinson's disease suggests impaired neuronal growth
  - [45]: GAP-43 plays central role in axonal growth and plasticity; promotes neural regeneration and repair
- Glutamate receptor signaling. Genes: GRIN2B, GRIA3, GRIK2, SLC1A2
  - [42]: Glioma cells cause elevation of local glutamate concentration and alter neuronal excitability via xCT transporter and glutamate receptor activation; astrocytic synaptogenic factors linked to tumor-associated seizures
- Cell-cell adhesion and neuron-astrocyte interaction. Genes: NRCAM, CHL1, LSAMP, CDH2, CDH4, JAG1
  - [39]: Genes involved in neuron-astrocyte interactions (Il33, Clasp2, Fgfr2) significantly upregulated in chronic TBI; NRCAM and CHL1 mediate axon-axon and axon-glia interactions
- Synaptic organization and neuromodulation. Genes: CHRM3, P2RY14, DENND2A, CPNE4
  - [2]: Astrocytes mediate cholinergic regulation of neural function through M1 muscarinic receptor; CHRM3-mediated signaling modulates hippocampal neurogenesis and memory

**Atomic cellular components**
- Synaptic terminals and presynaptic machinery. Genes: SYNJ2, SLC1A2, GRIA3, GRIN2B
  - [42]: Synaptic terminals release glutamate; astrocytes surrounding synapses regulate neurotransmitter reuptake and gliotransmitter release
- Cell adhesion molecules. Genes: NRCAM, CHL1, LSAMP, CDH2, CDH4
  - [39]: CAMs mediate cell-cell interactions between neurons and astrocytes; dysregulation affects synaptic connectivity
- Growth cone structure. Genes: GAP43, DPYSL5
  - [47]: GAP43 is localized to growth cones where it regulates axonal extension

**Required genes (not in input)**
- Genes: PSD95, SynGAP, NMDAR, AMPAR, Synapsin
  - [42]: PSD95 and other synaptic scaffold proteins are essential for glutamate receptor signaling and synaptic plasticity

**Program citations**
- [42]: Glioma cells alter peritumoral neuronal excitability through glutamate dysregulation and synaptogenic factors
- [39]: Genes involved in neuron-astrocyte interactions dysregulated in chronic brain injury with parallels to cancer pathology
- [45]: GAP43 role in neural regeneration and plasticity

## Program: Transcriptional Differentiation and Stemness Control
Cellular differentiation represents a fundamental axis controlling cell fate, proliferation, and self-renewal in tissue development and cancer. The input gene list contains multiple transcription factors implicated in stem cell maintenance, neural progenitor identity, and developmental decisions: SATB2 (matrix attachment region-binding protein), LEF1 (lymphoid enhancer-binding factor 1), RUNX1 (runt-related transcription factor), CREB5, LMO2 (LIM domain only 2), MEIS1 (meis homeobox 1), HMGA2 (high-mobility group AT-hook 2), NPAS3 (neuronal PAS domain protein 3), and ENC1 (ectodermal-neural cortex 1). Dysregulation of this transcriptional program is expected to maintain astrocytoma cells in a progenitor-like or stem cell state, preventing terminal differentiation and preserving proliferative capacity.

**Predicted impacts**
- Maintenance of progenitor-like phenotype with reduced terminal differentiation
- Enhanced self-renewal and proliferative capacity
- Preserved stemness markers (SOX2, NESTIN, OLIG2) in astrocytoma cells
- Resistance to differentiation-inducing therapies
- Sustained tumorigenicity and tumor-initiating capacity

**Evidence summary**
High-grade astrocytomas characteristically display reduced expression of mature astrocytic markers (GFAP, glutamine synthetase) and elevated expression of progenitor markers (nestin, SOX2, OLIG2), consistent with a block in differentiation or maintenance of progenitor identity. The input list contains multiple transcription factors known to maintain neural stem cell identity and developmental hierarchies. LEF1 is a key component of Wnt signaling essential for neural progenitor maintenance. MEIS1 and LMO2 function as cofactors for HOXA cluster genes, which establish developmental hierarchies and are frequently dysregulated in acute myeloid leukemia through KMT2A fusion events; similar mechanisms likely operate in neural development. HMGA2 is frequently upregulated in cancers through amplification or t(12;15) translocations and drives undifferentiated and stem-like phenotypes. Dysregulation of this transcriptional program would maintain astrocytoma cells in a more progenitor-like or dedifferentiated state, preventing terminal differentiation and preserving proliferative and self-renewal capacity. This represents a critical adaptation for cancer cell survival, as differentiation typically leads to proliferative arrest and specialized function rather than survival and growth.

**Atomic biological processes**
- Neural stem cell maintenance. Genes: MEIS1, LMO2, LEF1, RUNX1
  - [11]: Flow cytometry shows increased EGFR, SOX2, and CXCR4 expression in neural stem cells including astrocyte progenitor cells after TBI; these markers suggest stem cell maintenance program
  - [24]: HOXA genes (regulated by KMT2A and MEIS1 cofactors) establish developmental hierarchies and stem cell maintenance in hematopoiesis; similar mechanisms likely operate in neural tissue
- Developmental transcriptional regulation. Genes: SATB2, LEF1, RUNX1, MEIS1, LMO2
  - [24]: HOXA genes govern developmental differentiation through integrated regulatory architecture; KMT2A-dependent methylation and MEIS cofactors control lineage commitment
  - [23]: SATB2 acts as potent transcription factor to enhance bone cell differentiation and promote bone regeneration; matrix attachment regions regulate 3D chromatin organization
- Undifferentiated and cancer stem cell phenotype. Genes: HMGA2, CREB5, ENC1, NPAS3
  - [4]: JAB1 promotes breast cancer stemness by stabilizing CUL4B; stemness markers (OCT4, KLF4, NANOG, c-MYC) elevated with JAB1 overexpression and reduced with knockdown
- HMGA2-mediated stemness. Genes: HMGA2, HMGA2-AS1
  - [27]: HMGA2 frequently upregulated in cancers through amplification or fusion events; drives undifferentiated and stem-like phenotypes

**Atomic cellular components**
- Transcription factor complexes. Genes: MEIS1, LMO2, LEF1, RUNX1, SATB2, CREB5
  - [24]: HOXA genes function in complexes with KMT2A, MEIS cofactors, and chromatin remodeling complexes
- Nuclear matrix attachment regions. Genes: SATB2
  - [23]: SATB2 binds nuclear matrix attachment regions and regulates chromatin architecture and gene expression

**Required genes (not in input)**
- Genes: OLIG2, SOX2, NESTIN, KMT2A, PRC2
  - [24]: KMT2A and PRC2 are critical upstream regulators of HOXA gene expression in development

**Program citations**
- [24]: HOXA genes and MEIS cofactors regulate developmental hierarchies and stem cell maintenance
- [23]: SATB2 regulates differentiation decisions in bone tissue
- [4]: Stemness markers dysregulated in cancer cells

## Program: Extracellular Matrix Remodeling and Invasion Program
Cancer cell invasion requires coordinated degradation and remodeling of the extracellular matrix through the action of proteases and their inhibitors, combined with production of matrix components that support migration. The input gene list contains multiple matrix-degrading proteases (ADAMTS9, ADAMTS9-AS1, ADAM19, ADAM12, MMP14), structural matrix proteins (LAMC1, LAMA2, LAMA4, COL4A2, COL22A1, FBN2), and matricellular proteins (POSTN) that regulate cell-matrix interactions. ADAMTS proteases cleave aggrecan, versican, and other ECM components. MMP14 operates at the cell surface to create local zones of ECM degradation enabling invasion. POSTN promotes invasion through non-cell-autonomous immune suppression. Dysregulation of this program drives astrocytoma invasion through restrictive brain parenchyma.

**Predicted impacts**
- Localized ECM degradation enabling invasion through brain parenchyma
- Enhanced matrix remodeling supporting cell migration and establishment of tumor microenvironment
- Recruitment of tumor-associated macrophages through POSTN-mediated signaling
- Altered matrix stiffness and mechanotransduction signaling
- Enhanced neoangiogenesis through ECM remodeling

**Evidence summary**
The extracellular matrix remodeling program is a critical driver of astrocytoma invasion and microenvironment establishment. ADAMTS proteases and ADAM proteases cleave ECM components, creating degradation products that can either promote or inhibit invasion depending on context. MMP14 operates at the cell surface to create a localized 'degradome' enabling invasion. POSTN, a matricellular protein, was recently demonstrated to promote sarcoma growth and metastasis through recruitment and polarization of tumor-associated macrophages; analysis of human sarcoma data revealed that high POSTN expression correlates with poor prognosis and elevated ECM-related and myeloid cell-associated genes. In astrocytomas, periostin is often upregulated and likely promotes invasion through both direct effects on astrocytoma cells and indirect effects through immune cell recruitment. The synthesis of matrix components (laminin, collagen, fibronectin) by astrocytoma cells supports the establishment of a permissive microenvironment. The coordinated dysregulation of matrix proteases, matrix synthesis, and matricellular signaling creates a robust program of invasion and microenvironment remodeling central to astrocytoma progression.

**Atomic biological processes**
- Extracellular matrix proteolysis. Genes: ADAMTS9, ADAM19, ADAM12, MMP14, POSTN
  - [31]: MMP14 regulates ECM remodeling in melanoma; matrix metallopeptidase 14 controls cell migration and invasion
  - [30]: Periostin promotes sarcoma growth and recruits tumor-associated macrophages; Analysis revealed high POSTN expression correlates with poor prognosis and elevated ECM-related genes
- ECM component synthesis and deposition. Genes: LAMC1, LAMA2, LAMA4, COL4A2, COL22A1, FBN2
  - [30]: Murine sarcoma models with high Postn expression display enhanced expression of ECM genes
- Matricellular protein signaling. Genes: POSTN
  - [32]: Periostin secreted by fibroblasts in idiopathic pulmonary fibrosis promotes tumorigenesis of lung cancer
  - [30]: Recombinant POSTN promotes monocyte migration and differentiation; therapeutic neutralization of POSTN partially recapitulates immunologic remodeling

**Atomic cellular components**
- Membrane-anchored proteases. Genes: MMP14
  - [31]: MMP14 is a transmembrane protease at the cell surface enabling localized ECM remodeling
- Secreted matrix proteases. Genes: ADAMTS9, ADAM19, ADAM12
  - [30]: ADAMTS proteases are secreted and degrade ECM components like versican
- Extracellular matrix structural proteins. Genes: LAMC1, LAMA2, LAMA4, COL4A2, COL22A1
  - [56]: Laminin and collagen form basement membrane and ECM scaffolds

**Required genes (not in input)**
- Genes: TIMP1, TIMP2, TIMP3, TIMP4, Integrin
  - [31]: TIMP proteins inhibit MMPs and ADAMTS proteases; dysregulation or loss promotes invasion

**Program citations**
- [30]: Periostin promotes sarcoma growth and immune cell recruitment, correlating with poor prognosis
- [31]: MMP14 controls ECM remodeling and cell migration

## Program: Metabolic Reprogramming Toward Aerobic Glycolysis and Lipogenesis
Cancer cells characteristically undergo profound metabolic rewiring to support rapid growth while adapting to tissue-specific constraints. Astrocytomas employ aerobic glycolysis (Warburg effect), enhanced glutamine utilization (glutaminolysis), and increased lipid synthesis to generate ATP, biosynthetic precursors, and signaling lipids. The input gene list contains multiple metabolic enzymes: BCAT1 (branched-chain amino acid transaminase 1), GLDC (glycine cleavage system protein H), ACSBG1 (acyl-CoA synthetase butyrate-CoA ligase 1), ACSS3 (acyl-CoA synthetase short-chain family member 3), ELOVL2 (ELOVL fatty acid elongase 2), OSBP2 (oxysterol binding protein 2), and VMP1 (vacuole membrane protein 1). This program is central to the metabolic addiction of astrocytomas and represents a therapeutic vulnerability.

**Predicted impacts**
- Enhanced aerobic glycolysis supporting ATP and NADPH production
- Increased glutamine utilization for anaplerosis and biosynthesis
- Enhanced lipid synthesis supporting rapid membrane production for cell growth
- Altered mitochondrial metabolism with reduced oxidative phosphorylation
- Enhanced tumor growth in glucose-rich brain microenvironment

**Evidence summary**
Metabolic reprogramming is a hallmark of cancer, and astrocytomas are no exception. The Warburg effect (aerobic glycolysis despite adequate oxygen) is characteristic of high-grade gliomas and supports rapid ATP production, NADPH generation for biosynthesis and antioxidant defense, and intermediate precursors for biomass accumulation. The branched-chain amino acid transaminase BCAT1 is frequently upregulated in gliomas and catalyzes the transamination of leucine, isoleucine, and valine to branched-chain alpha-ketoacids, linking amino acid and energy metabolism. The glycine cleavage system (GLDC) converts glycine to one-carbon units and ammonia, supporting folate-mediated biosynthesis. Fatty acid synthesis is enhanced to support rapid membrane production; ACSBG1 and ACSS3 activate short- and medium-chain fatty acids for entry into lipogenic pathways. ELOVL2 elongates polyunsaturated fatty acids for membrane incorporation and signaling lipid synthesis. Recent work has demonstrated that dysregulation of fatty acid metabolism genes (PPARG, ACSL5) by the JAB1/CRL4B complex in breast cancer promotes cell proliferation and invasion. Metabolic dysregulation in astrocytomas would promote adaptation to the brain microenvironment, support rapid growth, and potentially contribute to therapeutic resistance.

**Atomic biological processes**
- Amino acid metabolism and glutamine utilization. Genes: BCAT1, GLDC
  - [9]: In Alzheimer's disease gene networks, a large proportion of core genes (34%) are associated with mitochondrial energy production, followed by 22% with synaptic signaling, indicating metabolic dysregulation; glutamine-fueled anaplerosis identified in the context of altered metabolism
- Fatty acid and lipid synthesis. Genes: ACSBG1, ACSS3, ELOVL2
  - [4]: JAB1/CRL4B complex represses PPARG and ACSL5 expression, thereby regulating fatty acid metabolism
- Oxysterol and cholesterol metabolism. Genes: OSBP2
  - [21]: Metabolic changes in senescence include alterations in cholesterol and lipid synthesis

**Atomic cellular components**
- Mitochondrial metabolic enzymes. Genes: GLDC, BCAT1
  - [9]: Mitochondrial energy production is altered in AD with implications for cancer metabolic reprogramming
- Lipogenic enzyme complexes. Genes: ACSBG1, ACSS3
  - [4]: ACSL and related acyl-CoA synthetases activate fatty acids for synthesis and oxidation

**Required genes (not in input)**
- Genes: LDHA, PKM2, GLS1, GLUT1, ACC1
  - [9]: LDHA catalyzes lactate production; PKM2 (pyruvate kinase M2) is a key glycolytic enzyme; GLS1 catalyzes glutaminolysis; these are essential for metabolic reprogramming

**Program citations**
- [4]: JAB1 represses PPARG and ACSL5 fatty acid metabolism genes in cancer
- [9]: Metabolic dysregulation in AD with implications for cancer metabolism

## Program: Cell Migration and Directional Guidance
Cell migration requires coordinated regulation of adhesion, cytoskeletal dynamics, and directional sensing through guidance cues. The input list contains genes encoding secreted guidance molecules (SEMA5A, SEMA3A, SEMA3E), migration-associated kinases and scaffolding proteins, and factors that couple chemotactic signals to cytoskeletal dynamics. Semaphorins are secreted or membrane-bound signaling proteins originally discovered as axon guidance cues but now recognized as critical regulators of cell migration in cancer. ETS transcription factors (ETV5, ETV6) regulate migration-associated genes downstream of MAPK signaling. Dysregulation of this program drives astrocytoma cell migration and invasion.

**Predicted impacts**
- Enhanced directional migration in response to guidance cues
- Altered migration velocity and invasive phenotype
- Coupling of kinase signaling to migration machinery
- Dysregulated response to attractant and repellent gradients

**Evidence summary**
Cell migration in astrocytomas is driven by multiple mechanisms, including growth factor gradients, hypoxia, and nutrient depletion. Semaphorins are emerging regulators of cancer cell migration and invasion, working through plexin and neuropilin receptors to trigger both attraction and repulsion depending on the specific semaphorin-receptor pair and cellular context. The presence of multiple semaphorins (SEMA5A, SEMA3A, SEMA3E) in the input list suggests that astrocytomas employ sophisticated guidance signaling to navigate the brain microenvironment. ETS transcription factors, activated downstream of MAPK/ERK signaling, regulate expression of migration-associated genes. Dysregulation of the migration program would enhance astrocytoma cell motility and invasive capacity, enabling infiltration into surrounding brain tissue.

**Atomic biological processes**
- Semaphorin-mediated guidance signaling. Genes: SEMA5A, SEMA3A, SEMA3E
  - [42]: In glioma models, astrocytic-derived factors and semaphorins influence peritumoral neuronal properties; synaptogenic factors linked to tumor progression
- ETS transcription factor signaling. Genes: ETV5, ETV6
  - [55]: ETS transcription factors respond to RTK/MAPK signaling and regulate migration-associated genes
- Migration-associated kinase signaling. Genes: ALK, MAP3K1
  - [19]: ALK-mediated signaling promotes cell migration and anchorage-independent growth

**Atomic cellular components**
- Secreted guidance molecules. Genes: SEMA5A, SEMA3A, SEMA3E
  - [42]: Semaphorins are secreted signaling proteins controlling cell-cell and cell-matrix interactions

**Required genes (not in input)**
- Genes: Plexin, Neuropilin, PAK1, RAC1
  - [42]: Plexin and neuropilin receptors for semaphorins; PAK1 and RAC1 are downstream effectors in migration

**Program citations**
- [42]: Semaphorins and related guidance molecules influence glioma-neuron interactions and migration
- [19]: ALK signaling promotes migration in tumor contexts

## Program: Long Non-Coding RNA Regulatory Network
A substantial portion of the input gene list comprises long non-coding RNAs (lncRNAs) and other non-coding transcripts: MIR4435-2HG, CHRM3-AS2, ADAMTS9-AS1, HMGA2-AS1, PCDH9-AS2, GNG12-AS1, LINC02742, LINC01138, LINC01798, LINC00266-1, and AC-prefixed sequences representing unannotated or novel transcripts. Long non-coding RNAs regulate gene expression at multiple levels, including transcriptional regulation through chromatin remodeling, post-transcriptional splicing and stability, and miRNA sponging. While the specific roles of many lncRNAs in astrocytoma are not yet fully characterized, dysregulation of lncRNA expression is increasingly recognized as a critical feature of cancer biology.

**Predicted impacts**
- Dysregulated transcriptional programs through lncRNA-mediated chromatin remodeling
- Altered post-transcriptional mRNA stability and splicing
- Enhanced miRNA dysregulation through ceRNA networks
- Potentially altered cell fate decisions through lncRNA regulation of differentiation genes

**Evidence summary**
Long non-coding RNAs are emerging as critical regulators of gene expression and cellular phenotypes in cancer. Recent gene co-expression network analysis in Alzheimer's disease, a neurodegenerative condition with overlapping transcriptomic features with brain tumors, identified multiple lncRNAs as disease-specific hub genes associated with altered cytoskeleton organization, mitochondrial function, and neurogenesis. The lncRNA POC1B-AS1, for example, was associated with cytoskeleton organization in Alzheimer's disease networks but with mitochondrial energy production in control networks, suggesting a gain of function related to disease pathology. Similarly, FBXW7-AS1, Lnc-PDE4D-2, and others were functionally assigned only within disease networks. In the context of astrocytomas, dysregulation of lncRNAs likely contributes to the altered transcriptional and post-transcriptional landscapes characteristic of malignant transformation. LncRNAs can regulate gene expression through multiple mechanisms: by serving as scaffolds for chromatin-modifying complexes, by regulating mRNA splicing and stability, or by functioning as competing endogenous RNAs (ceRNAs) that sponge miRNAs away from their mRNA targets. The substantial number of lncRNAs in the input list suggests that lncRNA dysregulation is a significant feature of the astrocytoma transcriptome.

**Atomic biological processes**
- Chromatin remodeling and transcriptional regulation. Genes: MIR4435-2HG, HMGA2-AS1, LINC02742, LINC01138, LINC01798
  - [9]: In Alzheimer's disease networks, lncRNAs including POC1B-AS1, FBXW7-AS1, Lnc-PDE4D-2, and others were functionally assigned to altered biological processes, suggesting gain of function for these lncRNAs in disease context
- Post-transcriptional regulation and mRNA stability. Genes: CHRM3-AS2, ADAMTS9-AS1, PCDH9-AS2
  - [9]: lncRNAs regulate mRNA stability and splicing; antisense lncRNAs may regulate sense gene expression
- miRNA sponging and ceRNA networks. Genes: MIR4435-2HG, GNG12-AS1, LINC00266-1
  - [9]: lncRNAs function as competing endogenous RNAs (ceRNAs) by sponging miRNAs

**Atomic cellular components**
- lncRNA-chromatin remodeling complexes. Genes: MIR4435-2HG, HMGA2-AS1
  - [9]: lncRNAs recruit chromatin remodeling complexes to regulate gene expression

**Required genes (not in input)**
- Genes: PRC2, Dicer, Drosha, LSD1
  - [9]: PRC2 and histone demethylases (LSD1) are key chromatin regulators recruited by lncRNAs; Dicer and Drosha process miRNAs regulated by lncRNA-ceRNA networks

**Program citations**
- [9]: lncRNA dysregulation in Alzheimer's disease networks with altered functions compared to normal tissue

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/12669
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/154
4. 4. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/207
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/1894
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/5879
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/16449
9. 9. Zebardast F, Riethmüller MPS, Nowick K. Integrative gene co-expression network analysis reveals protein-coding and LncRNA genes associated with Alzheimer’s disease pathology. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-30392-9
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/18128
11. 11. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/10395
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/3480
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/857
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/3265
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/238
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/1050
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/27436
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/12606
21. 21. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
22. 22. Lee H, Han Y, Song J-Y, Kim DG, Chung H, Jung SJ, et al.. Pharmacological activation of SERCA2 reverses ER calcium dysregulation and depression-like behaviors in hyperglycemic mice. Scientific Reports [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41598-025-31293-7_reference.pdf
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/212712
24. 24. Huang W, Zhang F, Zhang Z, Wang Q, Chen S. Dysregulation of HOXA genes in acute myeloid leukemia and targeted therapy. npj Precision Oncology [Internet]. 2025Dec5;9(1). Available from: https://www.nature.com/articles/s41698-025-01200-4
25. 25. Leavey P, Jiang L, Pannullo N, Santiago C, Blackshaw S. Overexpression of Meis factors in late-stage retinal progenitors yields complex effects on temporal patterning and neurogenesis. Scientific Reports [Internet]. 2025Dec3;. Available from: https://www.nature.com/articles/s41598-025-31061-7_reference.pdf
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/23314
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/4602
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/11921
29. 29. Ghirardello M, Yruela I, Merino P, Sackstein R, Sanz-Martínez I, Hurtado-Guerrero R. Structure, function, and implications of fucosyltransferases in health and disease. Nature Communications [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41467-025-66871-w_reference.pdf
30. 30. Jin-Fen X, Kristin I, Emily YK, Annaliese F, Marina TB, Jlenia G. Periostin promotes sarcoma growth by promoting tumor-associated macrophage migration and differentiation.. Cancer research communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41264337/
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/4323
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/10631
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/546
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/6093
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/4851
36. 36. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/998
38. 38. Wei X-Y, Zou Z-M, Yao Z-X, Teng S-W, Wei X-Y, Tang W-J, et al.. Neuronal activity-induced GLUT3 plasma translocation supports energy demands for memory acquisition. Communications Biology [Internet]. 2025Nov28;8(1). Available from: https://www.nature.com/articles/s42003-025-09119-z
39. 39. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
40. 40. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
41. 41. Ye J, Wang H, Peng Y, Wang S, Zheng R, Chen Y, et al.. Noncanonical role of astrocytic mitochondrial Cx43: suppressing IDH3α to sustain glycolytic homeostasis against depression. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08309-1
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
43. 43. Kao Y-C, Huang H-B, Lee C-H. Combined effects of red light and direct-current electric fields on neurite growth in 3D neural cell cultures. Scientific Reports [Internet]. 2025Nov29;. Available from: https://www.nature.com/articles/s41598-025-29835-0_reference.pdf
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/2534
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/2596
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/4868
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/5154
48. 48. Dyer A, Dudley R, Ahuja S, Alsinet C, Poudel P, Bowyer G, et al.. Characterisation of human in vitro tumour-associated macrophage models to define translational relevance. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30224-w
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/5155
50. 50. Yan X, Yang Z, Jiahe W. Engineered macrophages accumulate in solid tumors and locally deliver immune-activating proteins to inhibit tumor progression.. Translational cancer research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41378015/?fc=None&ff=20251211101854&v=2.18.0.post22+67771e2
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/10253
52. 52. Rangarajan S, Espeter L, Drexler HCA, Chrostek-Grashoff A, Grashoff C. Talin force coupling underlies eukaryotic cell-substrate adhesion. Nature Communications [Internet]. 2025Dec6;16(1). Available from: https://www.nature.com/articles/s41467-025-67354-8
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/24064
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/3611
55. 55. da SNL, de MGVRM, Oliveira-Nazareth Y, da SRS, Campello-Costa P. Effects of caffeine on neuroinflammation in anxiety and depression: a systematic review of rodent studies. Translational Psychiatry [Internet]. 2025Nov17;15(1). Available from: https://www.nature.com/articles/s41398-025-03668-x
56. 56. Available from: http://json-schema.org/draft-07/schema#",
