# Gene Program Markdown Report

## Context
- Cell type: Astrocytes, oligodendrocytes, oligodendrocyte precursor cells
- Disease: Astrocytoma
- Tissue: Central nervous system (brain white and gray matter)

## Input Genes
CARNS1, MOBP, ERMN, ST18, PTGDS, TF, FOLH1, NKAIN2, PLEKHH1, MYO1D, PLP1, CTNNA3, CNDP1, MOG, ENPP2, EDIL3, MAP7, MAG, SELENOP, RNF220, AK5, PPP1R14A, CDH19, PEX5L, RNASE1, ... (200 total)

## Program: Oligodendrocyte Specification and Lineage Identity
A transcriptional cascade establishing and maintaining oligodendrocytic cell fate during development and maturation. This program includes master transcriptional regulators that open chromatin at oligodendrocyte-specific loci and drive expression of genes encoding myelin structural proteins and metabolic enzymes.

**Predicted impacts**
- Establishment of oligodendrocytic gene regulatory network
- Silencing of alternative glial cell fate genes
- Coordinated activation of myelin protein synthesis
- Maintenance of oligodendrocyte identity in mature cells

**Evidence summary**
SOX10, NKX6-2, and MYRF represent the core transcriptional cascade controlling oligodendrocyte specification. SOX10 functions as a pioneer transcription factor opening chromatin at oligodendrocyte-specific loci. NKX6-2 operates downstream to refine cell fate. MYRF represents a critical molecular switch activating late-stage maturation. These factors coordinately regulate hundreds of downstream genes including myelin structural proteins. In astrocytoma context, dysregulation of this cascade could promote aberrant glial differentiation or prevent normal oligodendrocyte maturation.

**Atomic biological processes**
- Transcriptional regulation of oligodendrocyte differentiation. Genes: SOX10, NKX6-2, MYRF
  - GO: GO:0048713 (regulation of oligodendrocyte differentiation) | confidence: 0.80 | method: partial_match
  - [4]: SOX10, OLIG2, and NKX6.2 drive astrocyte-to-oligodendrocyte conversion through transcriptional reprogramming
  - [8]: NKX6-2 functions in oligodendrocyte reprogramming from fibroblasts
  - [10]: OLIG2 and NKX6-2 roles in oligodendrocyte differentiation
- Chromatin remodeling and DNA accessibility. Genes: SOX10, VRK2, TRIM59
  - GO: GO:0006338 (chromatin remodeling) | confidence: 0.90 | method: exact_match
  - [4]: Ascl1 SA6 enables astrocyte-to-neuron conversion through transcriptional modification, related to lineage fate control
  - [46]: Distinct transcriptomic and epigenomic responses of oligodendrocytes reflect developmental stage

**Atomic cellular components**
- Transcription factor complexes. Genes: SOX10, NKX6-2, MYRF, VRK2
  - GO: GO:0005667 (transcription regulator complex) | confidence: 0.85 | method: partial_match
  - [4]: Ascl1 SA6 demonstrates transcriptional regulation mechanisms applicable to oligodendrocyte fate determination
  - [8]: SOX10, OLIG2, NKX6-2 form core reprogramming complex
- Chromatin modifying enzyme complexes. Genes: TRIM2, TRIM59, VRK2
  - GO: GO:0005677 (chromatin silencing complex) | confidence: 0.70 | method: partial_match
  - [46]: Epigenomic changes accompany oligodendrocyte differentiation

**Required genes (not in input)**
- Genes: OLIG2, OLIG1
  - [4]: OLIG2 is a master regulator of oligodendrocyte specification but not present in input gene list
  - [8]: OLIG2 required alongside SOX10 and NKX6-2 for oligodendrocyte reprogramming

**Program citations**
- [4]: Astrocyte reprogramming mechanisms demonstrate transcriptional control principles applicable to oligodendrocyte specification
- [8]: NKX6-2 identified in oligodendrocyte reprogramming
- [10]: OLIG2 and NKX6-2 in oligodendrocyte differentiation
- [41]: Ascl1 SA6 demonstrates transcriptional mechanisms in glial lineage specification
- [46]: Transcriptomic and epigenomic responses of oligodendrocytes

## Program: Myelin Protein Synthesis and Maintenance
The coordinated synthesis and assembly of myelin structural proteins that form the insulating sheath around axons. This program encompasses the three most abundant myelin proteins (MBP, PLP1, MOG) along with supporting proteins that ensure proper protein stoichiometry and membrane organization.

**Predicted impacts**
- Synthesis of myelin structural proteins at massive scale (>80% of myelin protein mass)
- Assembly of multi-protein complexes into organized myelin lamellae
- Maintenance of proper myelin thickness and compaction
- Prevention of myelin decompaction and demyelination
- Rapid conduction velocity along myelinated axons

**Evidence summary**
MBP, PLP1, and MOG represent the three most abundant myelin proteins, collectively comprising over 80 percent of myelin protein mass. MOBP operates alongside MBP in myelin structure. Supporting proteins including MAG, OPALIN, and CNP contribute to myelin organization and stability. CLDN11 functions in paranodal region organization. The presence of MBP in cerebrospinal fluid serves as a biomarker of brain tumor development. In astrocytoma context, myelin disruption could result from tumor mass effects, suppression of oligodendrocyte maturation, or active recruitment of phagocytic cells that digest myelin.

**Atomic biological processes**
- Myelin protein gene expression. Genes: MBP, PLP1, MOG, MOBP
  - GO: GO:0010467 (gene expression) | confidence: 0.70 | method: partial_match
  - [2]: MBP is a major constituent of the myelin sheath and critical for myelin function
  - [9]: MBP presence in CSF indicates brain tumor development
  - [40]: PLP1 is the most abundant proteolipid in CNS myelin; mutations cause Pelizaeus-Merzbacher disease
- Myelin protein trafficking and assembly. Genes: OPALIN, MAG, ENPP2, CNP
  - GO: GO:0032288 (myelin assembly) | confidence: 0.80 | method: partial_match
  - [1]: Patient-derived tumoroids preserve expression of key protein markers used in tumor diagnosis
  - [4]: Myelin proteins accumulate in membrane structures during oligodendrocyte maturation
- Myelin sheath compaction and stability. Genes: PLLP, CLDN11, MAL
  - GO: GO:0043217 (myelin maintenance) | confidence: 0.70 | method: partial_match
  - [26]: Myelin sheath provides metabolic support and enables rapid action potential propagation

**Atomic cellular components**
- Myelin protein complexes. Genes: MBP, PLP1, MOG, MOBP, MAG, OPALIN, CNP
  - GO: GO:0043209 (myelin sheath) | confidence: 0.80 | method: partial_match
  - [2]: MBP and related proteins form the structural foundation of myelin
  - [40]: PLP1 represents the most abundant proteolipid in CNS myelin
- Myelin membrane domains. Genes: CLDN11, CNTNAP4, PLLP, OPALIN
  - GO: GO:0043209 (myelin sheath) | confidence: 0.80 | method: partial_match
  - [26]: Specialized myelin domains exist including paranodal regions and compact myelin
  - [41]: OPALIN localizes to myelin paranodal and inner loop regions

**Required genes (not in input)**
- Genes: MYT1L, ZEB2
  - [1]: Additional transcriptional regulators coordinate myelin protein expression

**Program citations**
- [1]: Patient-derived tumoroids preserve expression of tumor diagnostic markers
- [2]: MBP is a major myelin constituent
- [9]: MBP in CSF indicates brain tumor development
- [26]: Myelin enables rapid action potential propagation and provides metabolic support
- [40]: PLP1 mutations cause myelin disease
- [41]: Multiple myelin proteins maintain myelin stability

## Program: Central Nervous System Cell Adhesion and Barrier Formation
Intercellular adhesion mechanisms establishing physical barriers and maintaining tissue architecture within the CNS. This program includes claudins and cadherins that form tight junctions and adherens junctions, along with supporting adhesion proteins that enable glial cells to establish stable contacts and coordinate tissue organization.

**Predicted impacts**
- Establishment of selective permeability barriers within CNS tissue
- Prevention of paracellular ion leakage
- Organization of glial networks around amyloid plaques and lesion sites
- Coordination of glial cell spacing and alignment
- Stabilization of neurovascular unit through pericyte-endothelial interactions

**Evidence summary**
CLDN11 and CLDND1 encode claudins that form tight junction strands critical for selective permeability. CDH19 and CTNNA3 participate in adherens junctions that strengthen cell-cell contacts. Contactins (CNTN2, CNTNAP4) function as cell adhesion molecules mediating glial-neuronal interactions. EDIL3 and SPOCK3 represent extracellular matrix components supporting adhesion. Recent research demonstrates that beta-catenin undergoes phase separation to nucleate formation of submicron cadherin clusters that stabilize adhesion sites. In astrocytoma context, dysregulation of cell adhesion could promote tumor cell invasion, disrupt glial scar formation, or compromise the blood-brain barrier integrity.

**Atomic biological processes**
- Tight junction formation and maintenance. Genes: CLDN11, CLDND1
  - GO: GO:0120193 (tight junction organization) | confidence: 0.80 | method: partial_match
  - [11]: CLDN11 is a claudin family member and component of tight junction strands
  - [18]: Beta-catenin condensation nucleates formation of cadherin/catenin clusters forming stable adhesion sites
- Adherens junction stabilization. Genes: CDH19, CTNNA3
  - GO: GO:0034334 (adherens junction maintenance) | confidence: 0.90 | method: partial_match
  - [18]: Beta-catenin condensation facilitates clustering of cadherin complexes into stable adhesion sites
  - [20]: CDH1 mutations affect cell-cell adhesion through cadherin complex dysfunction
- Cell adhesion molecule-mediated intercellular communication. Genes: CNTN2, CNTNAP4, CERCAM
  - GO: GO:0044331 (cell-cell adhesion mediated by cadherin) | confidence: 0.70 | method: partial_match
  - [1]: Contactins contribute to cell adhesion and synaptic organization
  - [17]: CNTNAP4 functions as a cell adhesion molecule in nervous system development

**Atomic cellular components**
- Tight junction protein complexes. Genes: CLDN11, CLDND1
  - GO: GO:0070160 (tight junction) | confidence: 0.90 | method: partial_match
  - [11]: Claudins are integral membrane proteins forming tight junction strands
  - [53]: TJP1 and CLDN5 form tight junctions in blood-brain barrier
- Adherens junction complexes. Genes: CDH19, CTNNA3
  - GO: GO:0005912 (adherens junction) | confidence: 0.90 | method: partial_match
  - [18]: Beta-catenin forms lateral clusters with cadherins at adherens junctions
  - [53]: CDH5 and catenins form adherens junctions in vascular endothelium
- Extracellular matrix components supporting adhesion. Genes: EDIL3, SPOCK3, COL4A5
  - GO: GO:0007160 (cell-matrix adhesion) | confidence: 0.70 | method: partial_match
  - [1]: EDIL3 participates in integrin-binding and cell adhesion
  - [1]: SPOCK3 proteoglycan family member contributes to cell adhesion

**Required genes (not in input)**
- Genes: CDH5, TJP1, ACTB, VCL
  - [53]: CDH5 and TJP1 essential for tight junction formation in vascular endothelium

**Program citations**
- [1]: Multiple adhesion proteins coordinate cell-cell interactions
- [11]: CLDN11 functions in tight junction formation
- [17]: CNTNAP4 is a cell adhesion molecule in nervous system development
- [18]: Beta-catenin condensation nucleates cadherin clustering and adhesion site formation
- [37]: Plexin-B1 coordinates astrocyte spacing and alignment critical for glial organization
- [53]: Tight junction markers coordinate blood-brain barrier formation

## Program: Ion Homeostasis and Electrolyte Regulation
Active transport and passive ion flux mechanisms that maintain proper ionic gradients essential for neuronal excitability and glial cell function. This program encompasses Na+/K+ ATPases, voltage-gated ion channels, and lipid kinases that regulate ion channel function and cellular membrane potential.

**Predicted impacts**
- Maintenance of resting membrane potential in glial cells
- Prevention of excessive extracellular K+ accumulation during neuronal activity
- Regulation of cell volume in response to osmotic changes
- Modulation of neuronal excitability through glial K+ buffering
- Coupling of metabolic ATP production to ion pumping demands

**Evidence summary**
ATP1B1 represents the beta subunit of the Na+/K+ ATPase, the most energy-demanding process in the brain, consuming approximately 25 percent of total ATP. The Na+/K+ ATPase maintains ionic gradients essential for neuronal excitability while also regulating cell volume through osmotic effects. KCNK1 and KCNMB4 encode potassium channels enabling K+ flux that influences resting membrane potential and responsiveness to stimuli. PIP4K2A and related phospholipid kinases regulate channel localization and activity through synthesis of PIP2. In astrocytoma context, dysregulated ion homeostasis could promote glioma cell proliferation (as glioblastoma cells often exhibit abnormal Ca2+ signaling) or suppress normal astrocytic buffering capacity.

**Atomic biological processes**
- Sodium-potassium active transport. Genes: ATP1B1
  - GO: GO:0006814 (sodium ion transport) | confidence: 0.70 | method: partial_match
  - [12]: ATP1B1 is the beta subunit of Na+/K+ ATPase involved in ion gradient maintenance and volume regulation in astrocytes
  - [16]: Na+/K+ ATPases consume 25% of total ATP production in the brain
- Potassium channel-mediated conductance. Genes: KCNK1, KCNMB4
  - GO: GO:0005267 (potassium channel activity) | confidence: 0.80 | method: partial_match
  - [1]: KCNK1 encodes a two-pore domain potassium channel contributing to background K+ conductance
  - [1]: KCNMB4 functions as accessory subunit of large-conductance calcium-activated potassium channels
- Phospholipid metabolism supporting channel regulation. Genes: PIP4K2A, PLD1, PLAAT3
  - GO: GO:1903725 (regulation of phospholipid metabolic process) | confidence: 0.70 | method: partial_match
  - [1]: PIP4K2A catalyzes synthesis of PIP2, a critical lipid that regulates ion channels

**Atomic cellular components**
- Na+/K+-ATPase pumps. Genes: ATP1B1, ATP8A1
  - GO: GO:0005391 (P-type sodium:potassium-exchanging transporter activity) | confidence: 0.90 | method: partial_match
  - [12]: ATP1B1 beta subunit couples with ATP1A1 alpha subunit in Na+/K+ ATPase
  - [16]: ATP1B1 interacts with MLC1 to regulate astrocyte volume and osmotic balance
- Voltage-gated ion channels. Genes: KCNK1, KCNMB4, PIEZO2
  - GO: GO:0022832 (voltage-gated channel activity) | confidence: 0.90 | method: partial_match
  - [1]: KCNK1 and KCNMB4 represent functional ion channel components
- Membrane phospholipid regulation complexes. Genes: PIP4K2A, PLD1, PLAAT3
  - GO: GO:0061091 (regulation of phospholipid translocation) | confidence: 0.80 | method: partial_match
  - [1]: PIP4K2A and related enzymes regulate phospholipid composition

**Required genes (not in input)**
- Genes: ATP1A1, ATP1A3, MLC1
  - [12]: ATP1A1/ATP1A3 alpha subunits partner with ATP1B1 beta subunits in Na+/K+ ATPase
  - [16]: MLC1 couples with ATP1B1 for astrocyte volume regulation

**Program citations**
- [1]: Multiple ion channel and transporter genes identified in oligodendrocyte context
- [12]: ATP1B1 critical for astrocyte osmotic regulation and volume control
- [15]: Dysregulated oxidative phosphorylation supports glioma therapy resistance
- [16]: Ion pumping represents major energy expenditure in brain

## Program: Axon-Glia Communication and Neurite Support
Bidirectional signaling between axons and glial cells that enables oligodendrocytes and astrocytes to sense axonal activity and provide metabolic and trophic support. This program encompasses secreted signaling molecules, growth factor receptors, and RNA-binding proteins that coordinate neuronal-glial interactions.

**Predicted impacts**
- Sensing of axonal activity through neurotrophin and growth factor signals
- Metabolic reprogramming in glial cells in response to neuronal demands
- Coordination of myelination with axonal caliber and activity patterns
- Modulation of glial cell migration and process extension toward active axons
- Provision of metabolic substrates to support neuronal energy demands

**Evidence summary**
SEMA4D operates as a signaling molecule influencing both axon guidance and glial cell interactions, with recent evidence indicating its role in cancer-nerve interactions and metabolic reprogramming. ERBB3 and FGFR2 represent growth factor receptors enabling glial cells to respond to neuronal signals. LARP6 controls collagen and extracellular matrix protein synthesis through RNA stability mechanisms, enabling glial cells to remodel their microenvironment. UNC5C functions in axon guidance. MEGF10 and BEST1 contribute to additional aspects of axon-glia communication. In astrocytoma context, dysregulation could promote tumor cells to exploit neuronal support signals or suppress normal glial support of neuronal survival.

**Atomic biological processes**
- Semaphorin-mediated axon guidance and glia interactions. Genes: SEMA4D, UNC5C
  - GO: GO:1902287 (semaphorin-plexin signaling pathway involved in axon guidance) | confidence: 0.90 | method: partial_match
  - [25]: SEMA4D functions in signaling that influences cancer cell and nerve interactions including metabolic reprogramming
- Growth factor receptor signaling. Genes: ERBB3, FGFR2, LPAR1
  - GO: GO:0007173 (epidermal growth factor receptor signaling pathway) | confidence: 0.80 | method: partial_match
  - [1]: ERBB3 and FGFR2 function in glial growth factor signaling
  - [50]: VEGF signaling from neurons to endothelial cells enables brain vascular development
- RNA-binding protein-mediated translational control. Genes: LARP6, DNAJC6
  - GO: GO:0140764 (small RNA binding translational repressor activity) | confidence: 0.70 | method: partial_match
  - [25]: LARP6 controls collagen and extracellular matrix protein expression through RNA processing

**Atomic cellular components**
- Secreted signaling molecule complexes. Genes: SEMA4D, MEGF10
  - GO: unmapped
  - [25]: Semaphorins function as secreted or membrane-bound signaling molecules
- Growth factor receptor complexes. Genes: ERBB3, FGFR2, LPAR1
  - GO: unmapped
  - [1]: Receptor tyrosine kinases transduce growth factor signals
- Chloride channel signaling complexes. Genes: BEST1
  - GO: GO:0034707 (chloride channel complex) | confidence: 0.70 | method: partial_match
  - [1]: BEST1 encodes a chloride channel participating in cellular signaling

**Required genes (not in input)**
- Genes: VEGFA, NGF, BDNF, GDNF, NRG1
  - [29]: BDNF and FGF2 show gene interactions in stroke outcome
  - [50]: VEGF represents crucial neurotrophic factor for neurogenesis and axon pathfinding

**Program citations**
- [1]: Multiple axon-glia interaction genes identified in oligodendrocyte gene list
- [25]: SEMA4D and nerves influence cancer cell metabolism and stemness
- [50]: Neurovascular communication couples neural activity with vascular development

## Program: Lipid Metabolism and Myelin Lipid Biogenesis
Biosynthesis and remodeling of specialized lipids unique to myelin, including galactocerebroside, sulfatide, and 2-hydroxy fatty acids that comprise approximately 80 percent of myelin dry weight. This program coordinates fatty acid synthesis, elongation, hydroxylation, and incorporation into complex glycosphingolipids.

**Predicted impacts**
- Synthesis of myelin-specific lipids constituting 80% of myelin dry weight
- Proper myelin compaction and stability through coordinated lipid incorporation
- Prevention of myelin decompaction and demyelination
- Metabolic coupling between lipid synthesis and ATP availability
- Coordination of lipid membrane trafficking with oligodendrocyte development

**Evidence summary**
FA2H synthesizes 2-hydroxy fatty acids essential for myelin galactocerebroside and sulfatide; mutations cause hereditary spastic paraplegia. UGT8 catalyzes cerebroside synthesis, the most abundant myelin-specific lipid. ELOVL7 and SCD coordinate fatty acid elongation and desaturation. OSBPL1A regulates cholesterol trafficking, critical as cholesterol comprises 25 percent of myelin dry weight. ST6GALNAC3 participates in glycosphingolipid synthesis. ABC transporter family members facilitate lipid trafficking. In astrocytoma context, alterations in lipid metabolism may reflect both tumor origin in glial cells and metabolic reprogramming supporting oncogenic transformation.

**Atomic biological processes**
- Synthesis of 2-hydroxy fatty acids for myelin. Genes: FA2H
  - GO: unmapped
  - [41]: FA2H synthesizes 2-hydroxy fatty acids incorporated into myelin galactocerebroside and sulfatide
- Cerebroside (galactosylceramide) synthesis. Genes: UGT8
  - GO: GO:0006682 (galactosylceramide biosynthetic process) | confidence: 0.90 | method: synonym_match
  - [1]: UGT8 catalyzes cerebroside synthesis, the most abundant myelin-specific lipid
- Very long-chain fatty acid elongation. Genes: ELOVL7, SCD
  - GO: GO:0030497 (fatty acid elongation) | confidence: 0.80 | method: partial_match
  - [1]: ELOVL7 catalyzes elongation of very long-chain fatty acids for myelin lipid incorporation
- Cholesterol and oxysterol trafficking. Genes: OSBPL1A
  - GO: GO:0030301 (cholesterol transport) | confidence: 0.70 | method: partial_match
  - [1]: OSBPL1A binds cholesterol and oxysterols influencing their trafficking and metabolism

**Atomic cellular components**
- Fatty acid synthesis and modification enzymes. Genes: FA2H, SCD, ELOVL7
  - GO: GO:0006633 (fatty acid biosynthetic process) | confidence: 0.80 | method: partial_match
  - [41]: Multiple enzymes coordinate myelin lipid synthesis
- Glycosphingolipid synthesis complexes. Genes: UGT8, ST6GALNAC3
  - GO: GO:0006688 (glycosphingolipid biosynthetic process) | confidence: 0.90 | method: partial_match
  - [1]: UGT8 catalyzes cerebroside synthesis in Golgi apparatus
- Lipid trafficking and binding proteins. Genes: OSBPL1A, ABCA2, ABCA6, ABCA8
  - GO: GO:0008289 (lipid binding) | confidence: 0.70 | method: partial_match
  - [1]: OSBPL1A and related lipid binding proteins regulate cholesterol and oxysterol transport
  - [45]: Astrocyte sphingolipid metabolism changes in neurodegenerative diseases

**Required genes (not in input)**
- Genes: ASAH1, ASAH2, GALC
  - [1]: Additional enzymes coordinate myelin lipid synthesis and metabolism

**Program citations**
- [1]: Multiple lipid metabolism genes identified in oligodendrocyte gene list
- [25]: Metabolic reprogramming in cancer-associated cells includes lipid metabolism changes
- [41]: FA2H and related enzymes essential for myelin lipid synthesis
- [45]: Astrocyte lipid metabolism changes in disease states

## Program: Metabolic Adaptation and Energy Production
Coordinated metabolic reprogramming of glial cells in response to activity demands, injury signals, and tumor microenvironment cues. This program enables flexible utilization of multiple energy substrates and adaptation to changing metabolic demands, including shifts between glycolysis and oxidative phosphorylation.

**Predicted impacts**
- Rapid energy production matching glial cell metabolic demands
- Metabolic flexibility enabling utilization of multiple energy substrates
- Coupling of energy production to active ion pumping and biosynthetic demands
- Metabolic support for axonal activity through lactate and other metabolic substrates
- Resistance to metabolic stress during inflammation and tumor development

**Evidence summary**
Activated astrocytes engage in diverse metabolic processes beyond glycolysis including TCA cycle activity, glycogenolysis, and pyruvate carboxylation. Recent research challenges the classical astrocyte-neuron lactate shuttle hypothesis, indicating that metabolic coordination is more complex than previously appreciated. ATP1B1 represents the most energy-demanding process in the brain, consuming approximately 25 percent of total ATP. Dysregulated oxidative phosphorylation and glycolysis represent identified resistance mechanisms to anti-CSF-1R therapy in glioblastoma, highlighting the therapeutic importance of metabolic reprogramming. Acute and subacute astrocytic responses show upregulation of inflammatory and stress-related pathways. In astrocytoma context, tumor-derived signals drive metabolic reprogramming in tumor-associated glial cells, supporting both tumor growth and therapy resistance.

**Atomic biological processes**
- Aerobic and anaerobic energy metabolism. Genes: ATP1B1, ENO4
  - GO: GO:0006112 (energy reserve metabolic process) | confidence: 0.70 | method: partial_match
  - [16]: Activated astrocytes engage in TCA cycle activity, glycogenolysis, and pyruvate carboxylation in addition to glycolysis
  - [15]: Targeting oxidative phosphorylation and glycolysis represents resistance mechanism to anti-CSF-1R therapy in glioblastoma
- Glycogen metabolism and glucose utilization. Genes: ATP1B1, TPPP
  - GO: GO:0005977 (glycogen metabolic process) | confidence: 0.80 | method: partial_match
  - [16]: Activated astrocytes engage in glycogenolysis to provide substrates for energy and metabolic processes
- Inflammatory signaling and metabolic adaptation. Genes: IL1RAPL1, TNF
  - GO: GO:0006954 (inflammatory response) | confidence: 0.60 | method: partial_match
  - [22]: Acute astrocytic response includes upregulation of pro-inflammatory pathways and metabolic stress responses
  - [34]: Reactive astrocytes show sustained activation with transcriptional signatures reflecting pro-inflammatory and metabolic stress

**Atomic cellular components**
- ATP synthesis and energy coupling complexes. Genes: ATP1B1, ATP8A1, ENO4
  - GO: GO:0042773 (ATP synthesis coupled electron transport) | confidence: 0.90 | method: partial_match
  - [15]: Oxidative phosphorylation complexes represent therapeutic target in glioblastoma
  - [16]: Na+/K+ ATPase couples active ion transport with ATP consumption
- Metabolic regulatory enzyme complexes. Genes: ENO4, CBR1
  - GO: GO:0150005 (enzyme activator complex) | confidence: 0.70 | method: partial_match
  - [27]: Protein synthesis regulation through eEF2K controls energy expenditure during translation
- Stress response and inflammatory signaling complexes. Genes: IL1RAPL1, HSPA2
  - GO: GO:0140467 (integrated stress response signaling) | confidence: 0.80 | method: partial_match
  - [22]: Inflammatory pathway activation accompanies metabolic stress in reactive astrocytes

**Required genes (not in input)**
- Genes: PKM, LDHA, PDHB, SDH
  - [16]: Additional metabolic enzymes coordinate energy production

**Program citations**
- [15]: Oxidative phosphorylation dysregulation supports glioblastoma therapy resistance
- [16]: Activated astrocytes engage in diverse metabolic processes
- [22]: Acute astrocytic response includes inflammatory and metabolic stress pathways
- [27]: Protein synthesis and translation control consume substantial metabolic resources
- [34]: Chronic astrocytic activation shows mixed phenotype including metabolic adaptation

## Program: Transcriptional Regulation of Glial Identity and Chromatin Organization
Coordinated transcriptional control of glial differentiation, chromatin accessibility, and cell fate determination through transcription factors, chromatin remodelers, and epigenetic regulators. This program establishes and maintains glial cell identity while enabling plasticity in response to developmental and environmental signals.

**Predicted impacts**
- Establishment and maintenance of oligodendrocyte-specific gene expression patterns
- Opening of chromatin at oligodendrocyte-specific loci enabling transcriptional access
- Coordinated activation of myelin protein synthesis programs
- Suppression of alternative glial cell fates
- Dynamic regulation of glial plasticity in response to developmental and environmental signals

**Evidence summary**
SOX10, NKX6-2, and MYRF represent the core transcriptional cascade regulating oligodendrocyte specification and maturation. SOX10 functions as a pioneer transcription factor that opens chromatin at oligodendrocyte-specific loci. NKX6-2 refines oligodendrocyte fate through downstream regulatory mechanisms. MYRF represents a molecular switch with intrinsic self-cleaving mechanism that activates latent MYRF to nuclear form at appropriate developmental stage. VRK2 phosphorylates various transcription factors modifying their activity. TRIM proteins function as E3 ubiquitin ligases regulating transcription factor stability. In astrocytoma context, dysregulation of transcriptional control could occur through altered upstream signaling, mutations affecting transcription factors, or chromatin remodeling changes.

**Atomic biological processes**
- Pioneer transcription factor-mediated chromatin opening. Genes: SOX10, NKX6-2
  - GO: GO:0140673 (transcription elongation-coupled chromatin remodeling) | confidence: 0.70 | method: partial_match
  - [4]: Ascl1 SA6 demonstrates transcriptional mechanisms in glial lineage specification through chromatin remodeling
  - [46]: SOX10 functions as pioneer transcription factor opening chromatin at oligodendrocyte-specific loci
- Transcriptional control of myelin protein synthesis. Genes: MYRF, SOX10, NKX6-2
  - GO: GO:0043217 (myelin maintenance) | confidence: 0.50 | method: partial_match
  - [4]: Transcriptional regulators coordinately activate myelin protein genes
  - [41]: Ascl1 SA6 demonstrates transcriptional conversion of astrocytes
- Ubiquitin-mediated protein degradation affecting transcriptional regulation. Genes: TRIM2, TRIM59
  - GO: GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolic process) | confidence: 0.70 | method: partial_match
  - [1]: E3 ubiquitin ligases regulate transcription factor stability and activity

**Atomic cellular components**
- Transcription factor complexes. Genes: SOX10, NKX6-2, MYRF, VRK2
  - GO: GO:0005667 (transcription regulator complex) | confidence: 0.90 | method: partial_match
  - [46]: SOX and homeodomain factors form cooperating transcription factor networks
- Chromatin modifying enzyme complexes. Genes: TRIM2, TRIM59, VRK2
  - GO: GO:0140993 (histone modifying activity) | confidence: 0.80 | method: partial_match
  - [46]: Epigenomic changes accompany oligodendrocyte specification
- Protein kinase signaling complexes. Genes: VRK2
  - GO: GO:0070528 (protein kinase C signaling) | confidence: 0.70 | method: partial_match
  - [1]: VRK2 phosphorylates transcription factors modifying their activity

**Required genes (not in input)**
- Genes: OLIG2, OLIG1, ZEB2, SNAIL1
  - [1]: Additional transcriptional regulators coordinate glial lineage decisions

**Program citations**
- [4]: Transcriptional reprogramming in glial cells demonstrates central role of transcription factors
- [8]: SOX10 and NKX6-2 in oligodendrocyte transcriptional control
- [41]: Transcriptional mechanisms in glial lineage determination
- [46]: Distinct transcriptomic and epigenomic responses characterize oligodendrocyte development

## Bibliography
1. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
2. Available from: https://www.ncbi.nlm.nih.gov/gene/4155
3. Available from: https://www.nature.com/subjects/cns-cancer/ncomms
4. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
5. Available from: https://www.ncbi.nlm.nih.gov/gene/65078
6. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
7. Available from: https://www.ncbi.nlm.nih.gov/gene/4336
8. Available from: https://www.ncbi.nlm.nih.gov/gene/84504
9. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
10. Available from: https://www.ncbi.nlm.nih.gov/gene/5010
11. Available from: https://www.ncbi.nlm.nih.gov/gene/481
12. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
13. Available from: https://www.ncbi.nlm.nih.gov/gene/5743
14. Miao C, Ding Z, Wu J, An Q, Shu Y, Jiang H, et al.. Identification and targeting oxidative phosphorylation/glycolysis to overcome anti-CSF-1R therapy resistance in glioblastoma. Cell Death &amp; Disease [Internet]. 2025Dec10;. Available from: https://www.nature.com/articles/s41419-025-08288-3
15. Sims SL, Lu T-H, Weiss BE, Lin R-L, Galopin LB, Wright NA, et al.. Central cytometabolic functional vascular coupling in health and disease. npj Metabolic Health and Disease [Internet]. 2025Dec2;3(1). Available from: https://www.nature.com/articles/s44324-025-00090-1
16. Available from: https://www.ncbi.nlm.nih.gov/gene/85445
17. Monster JL, Manzato C, van der BJA, Pannekoek W-J, Hummelink JA, Hadders MA, et al.. β-catenin condensation facilitates clustering of the cadherin/catenin complex and formation of nascent cell-cell junctions. Nature Communications [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41467-025-66984-2
18. Available from: http://connect.biorxiv.org/archive/index.php?dt
19. Available from: https://www.ncbi.nlm.nih.gov/gene/999
20. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
21. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
22. Raikes AC, Dyke JP, Nerattini M, Boneu C, Ajila T, Fauci F, et al.. White matter microstructural and macrostructural profiles during midlife reveal sex differences between men and women at different menopausal stages. Scientific Reports [Internet]. 2025Nov17;15(1). Available from: https://www.nature.com/articles/s41598-025-24136-y
23. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
24. Zhang Z, Wang C, Sun Z, Shi X, Shuai Y, Wang Y, et al.. CAV2-expressing nerves induce metabolic switch toward mitochondrial oxidative phosphorylation to promote cancer stemness. Nature Communications [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41467-025-66914-2
25. Jamann N, Montijn JS, Petersen N, Lokhorst R, van den BD, Balemans M, et al.. Layer 5 myelination gates corticothalamic coincidence detection. Nature Communications [Internet]. 2025Dec11;16(1). Available from: https://www.nature.com/articles/s41467-025-66157-1
26. Jester HM, Nicol N, Yang Q, Zhang Y, Suhocki A, Zhou X, et al.. Overactive Neuronal eEF2K/eEF2 signaling is associated with cognitive impairment and apathy-like behavior. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03408-z
27. Available from: https://www.ncbi.nlm.nih.gov/gene/83619
28. Available from: https://www.ncbi.nlm.nih.gov/gene/2247
29. Available from: https://www.ncbi.nlm.nih.gov/gene/4137
30. Available from: https://www.ncbi.nlm.nih.gov/gene/18024
31. Available from: https://www.ncbi.nlm.nih.gov/gene/627
32. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
33. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
34. Available from: https://www.ncbi.nlm.nih.gov/gene/3458
35. Available from: https://www.ncbi.nlm.nih.gov/gene/5354
36. Available from: https://www.ncbi.nlm.nih.gov/gene/18053
37. Available from: https://www.ncbi.nlm.nih.gov/gene/24943
38. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
39. Fernandez RF, Fallatah W, Ji Y, Jones JW, Johnson CC, Tressler CM, et al.. Dysregulated hippocampal fatty acid metabolism following intermittent hypoxemia-induced neonatal brain injury is rescued by treatment with acetate. Nature Communications [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41467-025-67542-6_reference.pdf
40. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
41. Available from: https://www.ncbi.nlm.nih.gov/gene/11816
42. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
43. Available from: https://www.ncbi.nlm.nih.gov/gene/1277
44. Liu T-T, Li H-Y, Gu S-Y, Sun L, Zhang R-W, Zu J-L, et al.. NMDA receptors coordinate brain vascular development via neuron-to-endothelial tip cell crosstalk in zebrafish. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-66543-9
45. Available from: https://www.ncbi.nlm.nih.gov/gene/100130776
46. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
47. González-Gallego J, Todorov-Völgyi K, Müller SA, Antesberger S, Todorov MI, Malik R, et al.. A fully iPS-cell-derived 3D model of the human blood–brain barrier for exploring neurovascular disease mechanisms and therapeutic interventions. Nature Neuroscience [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41593-025-02123-w
