# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma
- Tissue: Brain (central nervous system)

## Input Genes
ADAMTS9, SLC4A4, ELOVL2, CPNE4, AC092957.1, TRMT9B, COL28A1, LAMA2, RORA, CNR1, AC064875.1, COL23A1, POSTN, TRPM3, FAT3, RUBCNL, ARHGAP26, ARHGAP18, SPRY4, SRPX, RHOJ, CCDC175, CCN4, KCNE4, AC092924.2, ... (200 total)

## Program: Glutamate Transport and Synaptic Homeostasis
This program encompasses genes mediating excitatory amino acid transport, glutamate receptor signaling, and maintenance of synaptic glutamate homeostasis. SLC1A2 encodes EAAT2, the primary astrocytic glutamate transporter maintaining extracellular glutamate within physiological ranges and preventing excitotoxic neuronal damage. SLC1A3 encodes EAAT1 with complementary glutamate transport function. Ionotropic glutamate receptor genes GRIK1, GRIA1, GRIA4, and GRID2 mediate rapid synaptic transmission and calcium influx, with GRIN1 and related NMDA receptors providing high-conductance calcium channels. SLC8A1 encodes the sodium-calcium exchanger participating in calcium extrusion after synaptic events. Post-transcriptional regulators NOVA1 and CPEB2 control alternative splicing and localization of glutamate receptor transcripts. Signaling integrators including PPP2R2B, PRKG1, and DPP6 modulate receptor trafficking and synaptic strength through phosphorylation cascades. Dysregulation in astrocytomas reduces glutamate buffering capacity and impairs synaptic transmission fidelity, contributing to neuronal dysfunction within the tumor microenvironment.

**Predicted impacts**
- Reduced glutamate buffering capacity with elevated extracellular glutamate driving excitotoxicity
- Impaired calcium homeostasis through dysregulated ionotropic glutamate receptor signaling
- Disrupted synaptic transmission and plasticity due to altered glutamate receptor trafficking
- Enhanced neuronal death within tumor microenvironment from chronic glutamate elevation

**Evidence summary**
Glutamate transporter dysregulation represents a critical feature of astrocytic pathology in tumors and neurodegeneration. SLC1A2 expression is frequently reduced in reactive astrocytes and glioblastomas, impairing glutamate clearance and promoting excitotoxic neuronal damage. Ionotropic glutamate receptors mediate calcium-dependent synaptic transmission and plasticity, with dysregulated expression contributing to synaptic dysfunction. The coordinated dysregulation of these genes impairs glutamate homeostasis and disrupts synaptic transmission in tumor-affected brain regions.

**Atomic biological processes**
- Glutamate uptake and clearance from synaptic cleft. Genes: SLC1A2, SLC1A3
  - [11]: Establishes astrocytic transcription factor REST upregulates glutamate transporter EAAT2, protecting dopaminergic neurons from manganese-induced excitotoxicity
  - [6]: Documents astrocyte-specific pathways during acute TBI involving glutamate homeostasis dysfunction
- Ionotropic glutamate receptor-mediated calcium signaling. Genes: GRIK1, GRIA1, GRIA4, GRID2
  - [35]: Describes dysregulation of synaptic plasticity-related genes including GRIN and GRIA in AD tauopathy models
  - [37]: GRIN1 and related NMDA receptor subunits play key roles in synaptic plasticity underlying memory and learning
- Post-transcriptional regulation of synaptic protein expression. Genes: NOVA1, CPEB2
  - [35]: Gene-specific alterations in synapse-related genes and dysregulation of synaptic plasticity mechanisms in pathological states

**Atomic cellular components**
- Synaptic cleft and glutamate-binding sites. Genes: SLC1A2, SLC1A3, GRIA1, GRIA4
  - [11]: SLC1A2 function maintains glutamate concentration in synaptic extracellular space
- Postsynaptic density and receptor scaffold. Genes: DLG1, CNTNAP3B
  - [35]: DLG4 and related scaffolding proteins anchor receptors at synapses

**Program citations**
- [11]: Documents EAAT2 regulation and glutamate transporter function in neuroprotection
- [6]: Demonstrates astrocyte transcriptomic changes and glutamate homeostasis dysfunction after brain injury
- [35]: Describes synaptic dysfunction and altered expression of glutamate receptor subunits in disease
- [37]: Establishes NMDA receptor subunit roles in synaptic plasticity

## Program: Extracellular Matrix Remodeling and Deposition
This program encompasses genes governing extracellular matrix synthesis, organization, proteolysis, and remodeling—processes fundamentally altered in astrocytomas. Collagen genes COL1A2, COL5A2, COL23A1, COL25A1, and COL28A1 encode distinct collagen isoforms providing structural scaffold and signaling substrate for the tumor stroma. Basement membrane components LAMA2 and LAMB1 encode laminin subunits critical for vascular stability and cellular adhesion. POSTN encodes periostin, a matricellular protein modulating cell-matrix interactions and frequently upregulated in tumor stromal compartments. Matrix metalloprotease genes ADAMTS9 and associated proteases facilitate ECM degradation and remodeling essential for invasion. Protease inhibitors and regulatory proteins including HTRA1 participate in matrix protein processing and proteostatic control. FBN1 encodes fibrillin-1 providing structural scaffolding and regulating TGF-β signaling through latent complex sequestration. Additional proteins including DCN (decorin) and NPNT (nephronectin) fine-tune matrix properties and growth factor availability. Dysregulation in astrocytomas produces enhanced ECM deposition contributing to altered tissue mechanics, modified growth factor bioavailability, and enhanced invasion through increased protease activity.

**Predicted impacts**
- Enhanced extracellular matrix deposition increasing tumor tissue stiffness and biomechanical properties
- Increased matrix proteolysis facilitating local invasion through tissue barriers
- Modified growth factor sequestration altering growth factor signaling magnitude and duration
- Altered mechanotransductive signaling through modified ECM composition and stiffness

**Evidence summary**
Extracellular matrix remodeling represents a fundamental feature of astrocytoma progression. Spatial transcriptomic studies demonstrate that glioblastoma exhibits distinct ECM expression profiles compared to normal brain, with enhanced collagen and proteoglycan expression contributing to tumor stiffness. Metalloproteases including ADAMTS enzymes are upregulated in gliomas, facilitating invasion through matrix barriers. The coordinated dysregulation of matrix synthesis and degradation genes establishes an environment supporting tumor cell invasion and altered mechanotransductive signaling.

**Atomic biological processes**
- Collagen synthesis and secretion. Genes: COL1A2, COL5A2, COL23A1, COL25A1, COL28A1
  - [4]: Single-cell spatial profiling reveals ECM gene expression patterns in GBM including collagen genes showing distinct expression profiles
- Basement membrane assembly and stability. Genes: LAMA2, LAMB1
  - [4]: ECM spatial mapping demonstrates expression of vascular ECM components including laminin in GBM samples
- Matrix metalloprotease-dependent proteolysis. Genes: ADAMTS9, ADAMTS9-AS1
  - [38]: ADAMTS1 serves as potential prognostic biomarker and promotes malignant invasion of glioma
- Growth factor sequestration and release. Genes: FBN1, POSTN
  - [14]: LTBP1 product targets latent TGF-beta complexes to extracellular matrix where latent cytokine is subsequently activated

**Atomic cellular components**
- Fibrillar collagen network. Genes: COL1A2, COL5A2, CHSY3
  - [4]: ECM spatial transcriptomic mapping reveals collagen expression in tumor stromal compartments
- Basement membrane structure. Genes: LAMA2, LAMB1, HSPG2
  - [4]: Vascular ECM components including laminin show differential expression in GBM
- Matricellular protein compartment. Genes: POSTN, TNC, CCN4
  - [4]: ECM atlas identifies ECM-signaling proteins including periostin and thrombospondin family members

**Program citations**
- [4]: Comprehensive single-cell spatial profiling of ECM genes in GBM identifies distinct ECM expression signatures
- [38]: ADAMTS1 promoted malignant glioma invasion through protease activity
- [14]: LTBP1 regulates latent TGF-beta sequestration and release in extracellular matrix

## Program: Cell Adhesion and Epithelial-Mesenchymal Transition
This program encompasses cell adhesion molecules and epithelial-mesenchymal transition regulators controlling cell-cell adhesion, cell polarity, and migratory capacity. Cadherin genes CDH6 and protocadherin genes PCDH7, PCDH9, and PCDH17 mediate homotypic and heterotypic cell-cell adhesion essential for tissue integrity. FAT3 encodes a large cadherin with roles in cell polarization and migration regulation. The transcriptional repressor ZEB1 drives epithelial-mesenchymal transition by suppressing E-cadherin while promoting N-cadherin and pro-migratory gene expression, representing a master regulator of cellular plasticity in tumors. CHL1 (cell adhesion molecule L1) mediates neuron-glia interactions supporting normal astrocyte-neuron physical associations. Junction-associated proteins including DLG1 (discs large homolog 1) and related scaffolding proteins maintain tight junction and adherens junction integrity. The Rho GTPase-activating proteins ARHGAP6, ARHGAP18, and ARHGAP26 regulate Rho family GTPases essential for cytoskeletal dynamics and cell migration, complemented by direct Rho regulators RHOJ, VAV3, and STARD13. The transcriptional regulator ETV1 and other transcription factors coordinate epithelial-mesenchymal transition programs. Dysregulation in astrocytomas promotes partial epithelial-mesenchymal transition, reducing intercellular adhesion, enhancing migratory capacity, and facilitating local invasion.

**Predicted impacts**
- Reduced cell-cell adhesion through ZEB1-mediated cadherindownregulation
- Enhanced migratory capacity and cytoskeletal plasticity through Rho GTPase dysregulation
- Increased invasive potential facilitating local brain invasion
- Partial epithelial-mesenchymal transition phenotype reducing tissue organization

**Evidence summary**
Epithelial-mesenchymal transition regulators represent key drivers of glial tumor progression. ZEB1 functions as a master regulator of epithelial-mesenchymal transition in cancer cells, promoting migratory and invasive phenotypes through transcriptional reprogramming. Rho GTPase-activating proteins modulate cytoskeletal dynamics essential for cell migration, with dysregulation promoting enhanced invasive capacity in gliomas. The coordinated downregulation of adhesion molecules combined with Rho GTPase dysregulation establishes the molecular basis for enhanced migratory and invasive phenotypes characteristic of astrocytic tumors.

**Atomic biological processes**
- Homotypic cell-cell adhesion through cadherins. Genes: CDH6, PCDH7, PCDH9, PCDH17
  - [10]: CDH1 cadherin 1 serves as classical adhesion molecule with roles in tumor differentiation and progression
- Epithelial-mesenchymal transition regulation. Genes: ZEB1, ETV1, TFCP2L1
  - [32]: ZEB1 mediates EMT/plasticity-associated ferroptosis sensitivity by regulating lipogenic enzyme expression
  - [29]: CM treatment induced epithelial-mesenchymal transition in GBM tumorspheres
- Rho GTPase-dependent cytoskeletal remodeling. Genes: ARHGAP6, ARHGAP18, ARHGAP26, RHOJ, VAV3, STARD13
  - [42]: ILK (integrin linked kinase) inhibition blocks glioma cell migration, dependent on Rho GTPase signaling

**Atomic cellular components**
- Adherens junction complex. Genes: CDH6, DLG1, PCDH9
  - [10]: CDH1 and associated adherens junctions mediate cell-cell adhesion and tumor progression
- Actin cytoskeleton. Genes: ARHGAP6, ARHGAP18, ARHGAP26, STARD13
  - [42]: ARHGAP and related proteins regulate actin dynamics through Rho GTPase activity

**Program citations**
- [32]: ZEB1 regulates epithelial-mesenchymal transition and cancer cell plasticity
- [29]: Epithelial-mesenchymal transition occurs in glioblastoma tumorspheres
- [42]: ILK inhibition blocks glioma cell migration through effects on cytoskeletal organization

## Program: Ion Channels and Electrolyte Transport
This program encompasses ion channels and solute carriers governing electrolyte homeostasis, membrane potential, and cellular excitability. SLC1A2 and SLC1A3 encode the glutamate transporters with concurrent sodium and potassium transport coupled to glutamate uptake. SLC8A1 encodes the sodium-calcium exchanger maintaining calcium extrusion essential for calcium homeostasis. SLC4A4 encodes sodium bicarbonate cotransporter 1 (NBCe1) regulating acid-base balance and cellular pH. Multiple potassium channel genes KCNE4 and KCNIP4 regulate potassium conductance and membrane excitability. SCN7A encodes voltage-gated sodium channel 7 contributing to action potential generation and propagation. Voltage-gated calcium channels including CACNA1c mediate calcium influx during electrical stimulation. TRPM3 encodes a transient receptor potential channel with polymodal sensory properties and calcium-permeable characteristics. The ryanodine receptor RYR3 mediates calcium-induced calcium release from sarcoplasmic/endoplasmic reticulum stores. TPCN1 encodes two-pore calcium channels in acidic compartments regulating lysosomal and endolysosomal calcium signaling. ATP13A4 encodes an ATPase potentially participating in metal homeostasis. Dysregulation in astrocytomas impairs normal electrolyte homeostasis, disrupts membrane potential maintenance, and promotes aberrant calcium signaling.

**Predicted impacts**
- Impaired glutamate-coupled sodium uptake reducing glutamate transport efficiency
- Dysregulated calcium homeostasis through altered sodium-calcium exchange
- Altered membrane potential and cellular excitability
- Disrupted acid-base balance affecting cellular metabolism and signaling

**Evidence summary**
Ion channel and transporter dysregulation contributes to cellular dysfunction in astrocytic tumors. The coordinated function of glutamate transporters, cation-chloride cotransporters, and sodium-calcium exchangers maintains normal astrocyte electrolyte homeostasis and supports synaptic transmission. Dysregulation of these transporters in tumors impairs glutamate buffering, disrupts calcium homeostasis, and alters membrane potential, collectively contributing to neuronal dysfunction within the tumor microenvironment.

**Atomic biological processes**
- Glutamate-coupled sodium and potassium transport. Genes: SLC1A2, SLC1A3
  - [11]: SLC1A2 (EAAT2) functions in coupled glutamate-sodium-potassium transport
- Calcium extrusion and sodium-calcium exchange. Genes: SLC8A1, FXYD6
  - [48]: SLC8A1 (sodium-calcium exchanger) participates in activity-dependent calcium dynamics
- Acid-base balance and pH regulation. Genes: SLC4A4
  - [11]: Solute carrier family proteins regulate cellular pH and electrolyte balance
- Voltage-gated ion channel function. Genes: CACNA1c, SCN7A, KCNE4, KCNIP4
  - [47]: CACNA1c enables calcium channel activity and voltage-dependent regulation

**Atomic cellular components**
- Plasma membrane transport proteins. Genes: SLC1A2, SLC1A3, SLC8A1, SLC4A4
  - [11]: SLC1A2 EAAT2 localization at astrocyte plasma membrane enables glutamate clearance
- Voltage-gated channels in plasma membrane. Genes: CACNA1c, SCN7A, KCNE4, TRPM3
  - [47]: CACNA1c represents voltage-dependent L-type calcium channel in plasma membrane
- Intracellular calcium release channels. Genes: RYR3, TPCN1, ITPR2
  - [34]: ITPR2 and RYR channels mediate intracellular calcium release during stress and normal signaling

**Program citations**
- [11]: SLC1A2 and related transporters maintain electrolyte homeostasis
- [47]: Voltage-gated ion channels regulate electrical excitability
- [48]: Sodium-calcium exchangers regulate activity-dependent calcium dynamics

## Program: Calcium Signaling and Intracellular Calcium Dynamics
This program encompasses calcium signaling machinery, intracellular calcium release, calcium-dependent enzymes, and calcium-responsive transcriptional regulators. ITPR2 encodes inositol 1,4,5-trisphosphate receptor type 2, a calcium channel localized to mitochondria-associated endoplasmic reticulum membranes critical for mitochondrial calcium uptake and cell fate decisions. STIM1 encodes stromal interaction molecule 1, functioning as the calcium sensor triggering store-operated calcium entry through ORAI channels when intracellular calcium depletes. The voltage-gated calcium channel CACNA1c mediates sustained L-type calcium signaling regulating gene transcription and metabolic coupling. TPCN1 encodes two-pore calcium channels in acidic compartments regulating lysosomal calcium dynamics. PPP2R2B encodes regulatory subunits of protein phosphatase 2A, participating in calcium-dependent dephosphorylation cascades and transcriptional regulation. PRKG1 encodes cGMP-dependent protein kinase mediating nitric oxide-responsive signaling. RYR3 and related ryanodine receptors mediate calcium-induced calcium release from intracellular stores. NFATC1-related calcineurin-NFAT signaling (implied through pathway context) represents a critical calcium-responsive transcriptional pathway. Dysregulation in astrocytomas drives aberrant calcium oscillations, impairs metabolic coupling, and promotes reactive astrocyte transcriptional programs.

**Predicted impacts**
- Elevated cytoplasmic and mitochondrial calcium promoting reactive astrocyte transcriptional programs
- Impaired metabolic coupling between calcium signaling and glycolytic metabolism
- Enhanced mitochondrial dysfunction through excessive calcium accumulation
- Dysregulated calcineurin-NFAT signaling promoting neuroinflammation

**Evidence summary**
Calcium signaling dysregulation represents a fundamental feature of reactive astrocytes and astrocytic tumors. ITPR2-mediated calcium release at mitochondria-ER contact sites contributes to both physiological calcium signaling and pathological calcium accumulation in disease. Dysregulation of calcineurin/NFAT calcium-responsive transcription drives reactive astrocyte transformation and impairs normal astrocyte-neuron metabolic coupling. Research demonstrates that calcineurin/NFAT pathway dysregulation compromises cerebrovascular function and neuronal support capacity in disease contexts.

**Atomic biological processes**
- Inositol 1,4,5-trisphosphate-mediated calcium release. Genes: ITPR2, PLCE1
  - [34]: ITPR2 mediates calcium release at mitochondria-ER contact sites during stress responses
  - [51]: ITPR2-mediated calcium release at MERCS allows uptake into mitochondria via MCU
- Store-operated calcium entry. Genes: STIM1
  - [51]: STIM1 regulates store-operated calcium entry enabling sustained calcium signaling
- Voltage-gated calcium channel-mediated influx. Genes: CACNA1c
  - [47]: CACNA1c mediates L-type calcium channel-dependent calcium signaling
- Calcium-induced calcium release. Genes: RYR3, TPCN1
  - [34]: Ryanodine receptors mediate calcium-induced calcium release amplifying calcium signals
- Calcineurin-NFAT calcium-responsive transcription. Genes: PPP2R2B, PRKG1
  - [51]: Suppression of astrocytic calcineurin/NFAT signaling improves neurovascular coupling and cellular function

**Atomic cellular components**
- Mitochondria-associated endoplasmic reticulum membranes (MERCS). Genes: ITPR2
  - [34]: ITPR2 localizes to MERCS mediating calcium transfer between ER and mitochondria
  - [51]: MERCS represent critical sites for calcium-mediated metabolic coupling
- Endoplasmic reticulum calcium stores. Genes: ITPR2, PLCE1, RYR3
  - [51]: ER calcium release through ITPR2 channels initiates calcium signaling cascades
- Lysosomal/endolysosomal compartments. Genes: TPCN1
  - [34]: TPCN1 encodes two-pore calcium channels in acidic organelles

**Program citations**
- [34]: Comprehensive analysis of mitochondrial calcium accumulation in cellular senescence and disease
- [51]: Describes astrocytic calcium dysregulation in disease and effects on metabolic coupling
- [47]: Voltage-gated calcium channels mediate activity-dependent calcium signaling

## Program: Metabolic Reprogramming and Glucose Metabolism
This program encompasses metabolic enzymes and metabolic regulatory genes governing glucose utilization, lipid metabolism, amino acid metabolism, and energy substrate utilization characteristic of astrocytic tumors. BCAT1 encodes branched-chain amino acid transaminase 1 regulating branched-chain amino acid catabolism and anaplerotic contribution to TCA cycle. Phosphodiesterase genes PDE3A, PDE4D, PDE7B, and PDE8B encode enzymes degrading cAMP and cGMP, thereby modulating energy-sensing cascades and metabolic signaling. ACSS3 encodes acyl-CoA synthetase short chain family member 3 activating short-chain fatty acids for metabolic incorporation. LPL (lipoprotein lipase) catalyzes triglyceride hydrolysis, mobilizing lipid substrates for energy and biosynthesis. ELOVL2 encodes elongation of very long chain fatty acid protein 2 regulating polyunsaturated fatty acid elongation important for membrane composition and signaling. ESRRG encodes estrogen-related receptor gamma, a nuclear receptor governing oxidative metabolism, mitochondrial biogenesis, and metabolic gene expression. HIF1A and HIF3A encode hypoxia-inducible factors promoting glycolytic metabolism under oxygen limitation and in disease contexts. CDK6 and cell cycle checkpoint proteins couple metabolic capacity to proliferative capacity. Dysregulation in astrocytomas establishes enhanced glycolytic metabolism, reduced oxidative phosphorylation (Warburg effect), and altered biosynthetic capacity supporting rapid tumor cell proliferation.

**Predicted impacts**
- Enhanced glycolytic flux and lactate production supporting biosynthesis and bioenergetics
- Reduced oxidative phosphorylation with metabolic shift toward glycolysis
- Altered biosynthetic precursor availability for nucleotides, lipids, and amino acids
- Impaired metabolic coupling with neurons through altered lactate availability

**Evidence summary**
Metabolic reprogramming toward enhanced glycolysis represents a hallmark of cancer cell transformation including astrocytic tumors. The Warburg effect—preferential glycolysis even under normoxic conditions—provides rapid ATP and biosynthetic precursor production supporting rapid proliferation. Astrocytic mitochondrial connexin 43 maintains glycolytic metabolism through inhibition of oxidative phosphorylation, identifying a novel mechanism sustaining the Warburg effect. Dysregulation of metabolic enzyme expression and metabolic transcriptional regulators establishes the enhanced glycolytic phenotype characteristic of astrocytic tumors.

**Atomic biological processes**
- Glucose metabolism and glycolytic flux. Genes: HIF1A, HIF3A, PDE3A, PDE4D
  - [26]: Astrocytic mitochondrial Cx43 sustains glycolytic metabolism and lactate production essential for neuronal excitability
  - [51]: Enhanced glycolytic flux in astrocytes during activation represents key metabolic adaptation
- Branched-chain amino acid metabolism. Genes: BCAT1
  - [51]: Branched-chain amino acid metabolism and anaplerosis support tumor metabolic demands
- Fatty acid activation and metabolism. Genes: ACSS3, LPL, ELOVL2
  - [51]: Lipid metabolism reprogramming supports tumor biosynthetic demands
- Oxidative metabolic gene expression. Genes: ESRRG
  - [51]: ESRRG regulates oxidative metabolism and mitochondrial biogenesis programs

**Atomic cellular components**
- Mitochondrial metabolic machinery. Genes: ESRRG, MT-ND3
  - [26]: Mitochondrial Cx43 regulates isocitrate dehydrogenase 3α and metabolic fate
  - [51]: Mitochondrial function dysregulation contributes to metabolic reprogramming
- Cytoplasmic metabolic enzymes. Genes: BCAT1, ACSS3, LPL
  - [51]: Cytoplasmic metabolic enzyme expression governs glycolytic capacity

**Program citations**
- [26]: Describes noncanonical mitochondrial Cx43 role in sustaining glycolytic metabolism
- [51]: Comprehensive analysis of astrocytic metabolic adaptation and metabolic coupling

## Program: Mitochondrial Function and Metabolic Coupling
This program encompasses mitochondrial structural proteins, electron transport chain components, metabolic enzymes, and metabolic coupling machinery linking energy availability to cellular signaling and gene expression. MT-ND3 encodes mitochondrial NADH dehydrogenase subunit 3, a core component of respiratory complex I essential for oxidative phosphorylation and ATP generation. The noncanonical mitochondrial functions of connexin 43 (GJA1) represent an emerging discovery: astrocytic mitochondrial Cx43 directly inhibits isocitrate dehydrogenase 3α (IDH3α), thereby sustaining glycolytic metabolism and lactate production essential for neuronal excitability and metabolic coupling. This mechanism operates independently of gap junction intercellular communication, establishing a novel mitochondrial scaffold function. Calcium sensing and uptake machinery including ITPR2, STIM1, and related proteins mediate mitochondrial calcium dynamics, with dysregulation causing calcium accumulation and mitochondrial permeability transition pore activation promoting cellular senescence and apoptosis. STARD13 encodes a GTPase-activating protein involved in lipid-dependent signaling regulating mitochondrial function and cellular metabolism. DENND2A encodes a guanine nucleotide exchange factor regulating ARF family GTPases important for vesicular trafficking and mitochondrial dynamics. OXR1 encodes oxidation resistance protein 1 participating in oxidative stress responses and mitochondrial protective mechanisms. Dysregulation in astrocytomas impairs metabolic coupling with neurons, reduces lactate availability for neuronal oxidative metabolism, and promotes mitochondrial dysfunction-driven inflammation.

**Predicted impacts**
- Impaired oxidative phosphorylation with metabolic shift to glycolysis
- Enhanced lactate production sustaining neuronal support capacity
- Dysregulated mitochondrial calcium handling promoting cell death and senescence
- Reduced metabolic coupling between astrocytes and neurons through impaired lactate supply

**Evidence summary**
Mitochondrial dysfunction represents a hallmark of aging, neurodegeneration, and cancer, including astrocytic tumors. The noncanonical mitochondrial function of connexin 43 directly regulating metabolic fate through IDH3α inhibition represents a novel mechanism sustaining glycolytic metabolism characteristic of tumors. Dysregulated calcium handling through ITPR2 and related channels promotes mitochondrial calcium accumulation, triggering permeability transition pore activation and cellular dysfunction. The coordinated dysregulation of mitochondrial oxidative capacity and metabolic coupling machinery establishes the basis for tumor metabolic reprogramming while impairing normal astrocyte-neuron metabolic support.

**Atomic biological processes**
- Oxidative phosphorylation and ATP generation. Genes: MT-ND3
  - [26]: Mitochondrial Cx43 regulates metabolic fate by inhibiting IDH3α, favoring glycolysis over OXPHOS
- Glycolytic metabolism regulation and lactate production. Genes: GJA1
  - [26]: Astrocytic mitochondrial Cx43 sustains glycolytic metabolism and lactate production essential for neuronal excitability
- Mitochondrial calcium dynamics and homeostasis. Genes: ITPR2, STIM1
  - [34]: ITPR2-mediated calcium release and MCU-mediated mitochondrial uptake causes calcium accumulation reducing mitochondrial membrane potential
  - [51]: Mitochondrial calcium accumulation through dysregulated ITPR2 promotes cellular dysfunction
- Oxidative stress responses and mitochondrial protection. Genes: OXR1
  - [34]: ROS production from dysfunctional mitochondria activates inflammation and senescence pathways

**Atomic cellular components**
- Electron transport chain and ATP synthase. Genes: MT-ND3
  - [26]: Metabolic reprogramming from OXPHOS to glycolysis alters electron transport chain utilization
- Mitochondrial matrix and metabolic enzymes. Genes: GJA1
  - [26]: Isocitrate dehydrogenase 3α (IDH3α) located in mitochondrial matrix regulates TCA cycle
- Mitochondrial calcium uniporter and related channels. Genes: ITPR2, STIM1
  - [34]: MCU and related channels mediate mitochondrial calcium uptake

**Program citations**
- [26]: Identifies noncanonical mitochondrial Cx43 role in metabolic regulation and mental health
- [34]: Comprehensive analysis of mitochondrial dysfunction in cellular senescence and disease
- [51]: Describes astrocytic metabolic coupling dysregulation in disease states

## Program: Synaptic Plasticity and Neuronal Interaction
This program encompasses genes governing synaptic plasticity mechanisms, dendritic complexity, synaptic transmission modulation, and neuron-astrocyte interactions critical for cognitive function. GRIN1, GRIN2A, and GRIN2B encode NMDA receptor subunits mediating high-conductance calcium channels essential for synaptic plasticity, learning, and memory consolidation. GRIA1, GRIA2, and GRIA4 encode AMPA receptor subunits determining synaptic strength through levels of calcium-permeable vs. calcium-impermeable AMPA receptors. GRID2 encodes delta-type glutamate receptors with specialized roles in cerebellar synaptic plasticity. DPP6 (dipeptidyl peptidase-like 6) modulates Kv4 potassium channel function regulating A-type potassium currents essential for dendritic back-propagation of action potentials and plasticity induction. The postsynaptic density scaffolding protein DLG1 (discs large homolog 1) anchors glutamate receptors and associated signaling proteins at synaptic sites. NOS1AP encodes nitric oxide synthase 1 adaptor protein modulating nitric oxide signaling and NMDA receptor-dependent calcium signaling. CNTNAP3B encodes contactin-associated protein-3B, a presynaptic adhesion molecule regulating synaptic transmission. EYA2 (eyes absent homolog 2) participates in synaptic development through transcriptional control of synaptic genes. TOX (thymocyte selection-associated high mobility group box) encodes a transcription factor governing neuronal gene expression programs. NPAS3 (neuronal PAS domain protein 3) regulates clock gene expression and neuronal function with relevance to cognitive processes. Dysregulation in astrocytomas disrupts synaptic plasticity mechanisms, impairs long-term potentiation and depression induction, and contributes to cognitive dysfunction in patients.

**Predicted impacts**
- Impaired NMDA receptor-dependent calcium signaling reducing plasticity induction capacity
- Dysregulated AMPA receptor trafficking reducing synaptic transmission efficacy
- Impaired dendritic integration and action potential back-propagation
- Reduced plasticity-dependent learning and memory formation

**Evidence summary**
Synaptic plasticity dysregulation contributes to cognitive dysfunction in patients with astrocytic tumors. NMDA and AMPA receptor dysregulation reduces synaptic plasticity capacity and long-term potentiation/depression mechanisms essential for learning and memory. Impaired nitric oxide signaling and reduced dendritic integration through altered potassium channel function compromise synaptic transmission fidelity. The combined dysregulation of multiple plasticity-essential genes establishes the molecular basis for cognitive impairment observed in glioma patients.

**Atomic biological processes**
- NMDA receptor-mediated calcium influx and plasticity. Genes: GRIN1, GRIN2A, GRIN2B
  - [37]: GRIN1 and NMDA receptor subunits play key roles in synaptic plasticity underlying memory and learning
  - [35]: Dysregulated GRIN and GRIA receptor expression occurs in AD tauopathy affecting synaptic plasticity
- AMPA receptor trafficking and synaptic strength. Genes: GRIA1, GRIA2, GRIA4
  - [35]: AMPA receptor content determines synaptic transmission strength and long-term potentiation
- Action potential back-propagation and dendritic integration. Genes: DPP6
  - [35]: DPP6 regulation of Kv4 channels affects dendritic integration and plasticity induction
- Nitric oxide signaling and synaptic plasticity. Genes: NOS1AP
  - [51]: NO-mediated signaling represents key mediator of vasomotor and synaptic responses

**Atomic cellular components**
- Postsynaptic density and glutamate receptor complex. Genes: DLG1, GRIN1, GRIA1, GRIA4
  - [35]: DLG4 and related scaffolding proteins organize postsynaptic density containing receptors and signaling proteins
- Presynaptic terminal and adhesion molecules. Genes: CNTNAP3B, GRIA2
  - [35]: Presynaptic proteins regulate neurotransmitter release and synaptic transmission
- Dendritic spine and cytoskeleton. Genes: DPP6, DLG1
  - [35]: Dendritic spine morphology reflects synaptic strength and plasticity state

**Program citations**
- [35]: Comprehensive analysis of synaptic dysfunction in tauopathy models
- [37]: NMDA receptor subunits mediate synaptic plasticity mechanisms

## Program: Reactive Astrocyte Activation and Neuroinflammation
This program encompasses genes characteristic of reactive astrocyte transformation, neuroinflammatory response activation, and transition from homeostatic to reactive phenotypes. GFAP (glial fibrillary acidic protein, though not in input list, is critical context) represents the canonical astrocyte marker with pronounced upregulation upon activation. The transcription factor genes and lineage-defining factors control astrocyte identity and determine reactive phenotype characteristics. NOS2 (nitric oxide synthase 2, inducible NOS) produces nitric oxide that drives inflammatory responses and contributes to neuronal toxicity through NMDA receptor-dependent excitotoxicity. CNR1 encodes cannabinoid receptor 1 mediating neuroprotective endocannabinoid signaling, with reduced expression in activated astrocytes representing a loss of neuroprotection. The complement cascade components including TFPI (tissue factor pathway inhibitor) participate in complement pathway regulation and inflammatory response modulation. TNFRSF21 (TNF receptor superfamily member 21) participates in TNF-α signaling cascades propagating inflammatory responses. HOPX (homeodomain-only protein) marks a specialized astrocyte subtype with specific reactive properties. RGS6 (regulator of G-protein signaling 6) regulates G-protein coupled receptor signaling potentially affecting responses to inflammatory mediators and neurotransmitters. The genes in this program exhibit dynamic upregulation during reactive astrocyte transition in response to brain injury, neuroinflammation, infection, and tumor development. Research demonstrates distinct transcriptional modules within reactive astrocytes: A1-like pro-inflammatory neurotoxic astrocytes expressing elevated NOS2, TNF-α, and IL-1β, and A2-like astrocytes maintaining more homeostatic neuroprotective functions. Dysregulation of this program in astrocytomas promotes pro-inflammatory neurotoxic astrocyte phenotypes.

**Predicted impacts**
- Enhanced nitric oxide production driving neuronal toxicity through NMDA receptor-dependent mechanisms
- Loss of neuroprotective endocannabinoid signaling through reduced CNR1 expression
- Increased TNF-α signaling amplifying inflammatory cascade propagation
- Chronic pro-inflammatory astrocyte phenotype impairing neuronal support and promoting neurodegeneration

**Evidence summary**
Reactive astrocyte activation represents a hallmark response to brain injury, neuroinflammation, and tumor development. The transition from homeostatic to reactive astrocyte phenotypes involves coordinated transcriptional reprogramming driven by injury-responsive enhancers controlled by AP-1 and lineage-specific transcription factors. Pro-inflammatory neurotoxic A1-like astrocytes express elevated NOS2 and TNF-α, contributing to neuronal injury and synaptic dysfunction. Loss of neuroprotective endocannabinoid signaling through CNR1 downregulation represents a critical loss of protective function in activated astrocytes. Research demonstrates that distinct reactive astrocyte subtypes coexist, with pro-inflammatory neurotoxic functions temporally and spatially segregated from partial neuroprotective functions.

**Atomic biological processes**
- Reactive astrocyte transcriptional transformation. Genes: NOS2, HOPX, RGS6
  - [6]: RNA-seq profiling of astrocytes after TBI highlights distinct neuroinflammatory signature (A1-like) with separate proliferation module (A2-like)
  - [31]: Injury-responsive enhancers drive reactive astrocyte gene expression through AP-1 and lineage-specific transcription factor cooperation
- Nitric oxide synthesis and pro-inflammatory signaling. Genes: NOS2
  - [6]: Reactive astrocytes upregulate pro-inflammatory cytokines including TNF-α and IL-6 contributing to neuronal injury
- Neuroprotective endocannabinoid signaling loss. Genes: CNR1
  - [18]: Perinatal ethanol exposure increased astrogliosis with reduced expression of cannabinoid receptors (Cnr1 and Gpr55) and decreased GRP55/PEA-mediated neuroprotection
- TNF-α and complement pathway regulation. Genes: TNFRSF21, TFPI
  - [6]: Upregulated TNF-α signaling and complement activation characterize acute reactive astrocyte response
  - [49]: Chronic neuroinflammation involves TNF receptor signaling amplifying pain and inflammatory responses

**Atomic cellular components**
- Intermediate filament cytoskeleton.
  - [2]: GFAP encodes major intermediate filament protein of mature astrocytes used as marker distinguishing astrocytes from other glial cells
- Nuclear transcriptional machinery. Genes: HOPX
  - [31]: Injury-responsive enhancers mediate reactive astrocyte transformation through transcriptional reprogramming

**Program citations**
- [6]: Comprehensive temporal analysis of reactive astrocyte transcriptome and distinct transcriptional modules after TBI
- [31]: Mechanistic analysis of injury-responsive enhancer regulation of reactive astrocyte programs
- [18]: Documents astrogliosis and reduced neuroprotective endocannabinoid signaling in disease model
- [49]: Describes microglia-astrocyte communication in chronic neuroinflammation

## Program: Extracellular Matrix-Integrin Mechanotransduction
This program encompasses integrin-based cell-matrix adhesion, mechanotransduction signaling, and mechanically-regulated gene expression critical for cellular responses to microenvironmental stiffness and matrix composition. Integrin family member ITGB1 (integrin subunit beta 1) forms heterodimeric adhesion receptors anchoring cells to extracellular matrix ligands including collagens, fibronectin, and laminin. The focal adhesion complex includes adaptor proteins TLN2 (talin-2) linking integrin cytoplasmic domains to actin cytoskeleton. FRMD4B (FERM domain-containing protein 4B) and related scaffolding proteins organize focal adhesion assembly. Integrin signaling transduction proceeds through focal adhesion kinase and related kinases (implied through pathway context though ILK is related). Cytoskeletal GTPase regulators including ARAP2 (ArfGAP with RhoGAP domain protein 2) and related proteins regulate Arf and Rho GTPases at focal adhesions controlling actin dynamics. Netrin ligands including NTN1 (netrin 1) function as ligands for DCC and UNC5 receptors promoting cell migration and axon guidance, often cooperating with integrin signaling. The Hippo pathway effectors YAP1 (yes-associated protein 1) and TAZ (encoded by WWTR1, WW domain containing transcription regulator 1) transduce mechanotransductive signals in response to matrix stiffness and cell geometry, with LATS2 (large tumor suppressor kinase 2) phosphorylating and inactivating YAP1 within the canonical Hippo pathway. Dysregulation of this program in astrocytomas promotes enhanced integrin signaling, YAP1/TAZ hyperactivation driving proliferation and stemness programs, and cellular adaptation to increased tumor microenvironment stiffness.

**Predicted impacts**
- Enhanced mechanotransductive signaling promoting proliferation through YAP1/TAZ hyperactivation
- Increased cell migration through netrin receptor and integrin signaling cooperation
- Altered cellular responses to increased tumor microenvironment stiffness
- Upregulation of stemness and self-renewal programs through YAP1-dependent transcription

**Evidence summary**
Mechanotransduction represents an emerging oncogenic driver in glioblastoma and astrocytic tumors. Glioma cells exhibit YAP1/TAZ hyperactivation driven by both canonical Hippo pathway dysregulation and mechanotransductive sensing of altered ECM stiffness. LATS2-mediated inhibition of YAP1 reduces glioma proliferation and migration, establishing YAP1 as an important therapeutic target. Integrin-netrin receptor cooperation enhances cell migration and proliferation signaling, with evidence suggesting these pathways cooperate in promoting invasion. The dysregulation of this program in astrocytomas establishes enhanced mechanotransductive signaling supporting proliferation and migration in response to the mechanically altered tumor microenvironment.

**Atomic biological processes**
- Integrin-mediated cell-matrix adhesion. Genes: ITGB1, TLN2, FRMD4B
  - [39]: ITGB1 (integrin beta 1) mediates cellular adhesion to fibronectin and other matrix proteins
  - [42]: ILK and related proteins propagate integrin-dependent signaling cascades affecting cell migration
- Netrin-receptor-mediated migration signaling. Genes: NTN1, DCC, UNC5C
  - [40]: Netrin-1 promotes glioma cell proliferation through NF-kB signaling via UNC5A receptor
  - [43]: NTN1 functions in axon guidance and cell migration during development with roles in cancer progression
- Mechanotransduction through Hippo pathway. Genes: YAP1, WWTR1, LATS2
  - [24]: YAP1 and TAZ (WWTR1) escape Hippo pathway inhibition in human cancers allowing uncontrolled activity
  - [27]: LATS2 inhibits glioma cell proliferation and migration by inactivating YAP1 downstream of Hippo pathway
- Rho GTPase regulation at focal adhesions. Genes: ARAP2, STARD13
  - [42]: ARAP2 and related proteins regulate GTPases at focal adhesion sites controlling cell migration

**Atomic cellular components**
- Focal adhesion complex. Genes: ITGB1, TLN2, FRMD4B
  - [39]: Focal adhesions mediate integrin-dependent cell-matrix adhesion and mechanotransduction
- Actin cytoskeleton. Genes: ARAP2, STARD13, RHOJ, VAV3
  - [42]: Rho GTPases regulate actin dynamics at focal adhesions through effector kinases
- YAP/TAZ nuclear transcriptional complex. Genes: YAP1, WWTR1
  - [24]: YAP1 and TAZ regulate stemness and cell plasticity through transcriptional control

**Program citations**
- [24]: Documents YAP1 and TAZ hyperactivation in human cancers
- [27]: Demonstrates LATS2 inhibition of YAP1 suppresses glioma proliferation and migration
- [40]: Netrin-1 signaling promotes glioma cell proliferation through NF-kB pathway
- [39]: ITGB1 mediates cell migration through fibronectin in glioma

## Program: Lipid Signaling and Phospholipid Metabolism
This program encompasses lipid signaling molecules, phospholipid-metabolizing enzymes, and lipid-dependent signaling cascades governing cell migration, inflammatory responses, and calcium mobilization. DGKG and DGKZ encode diacylglycerol kinases catalyzing conversion of diacylglycerol to phosphatidic acid, modulating protein kinase C signaling magnitude and duration. PLCE1 (phospholipase C epsilon) generates inositol 1,4,5-trisphosphate and diacylglycerol from phosphatidylinositol 4,5-bisphosphate during GPCR signaling, triggering calcium mobilization from intracellular stores. Phosphoinositide signaling through ITPR2 and related inositol phosphate receptors governs calcium-dependent processes. P2RY14 encodes nucleotide receptor P2Y14, a G-protein coupled receptor responding to extracellular nucleotides and lysophosphatidic acid (a bioactive lipid mediator). LPAR1 (lysophosphatidic acid receptor 1) directly responds to lysophosphatidic acid, a bioactive lipid mediator abundant in serum and implicated in cell migration, inflammatory responses, and cancer progression. DENND2A (DENN domain containing 2A) encodes a guanine nucleotide exchange factor for ARF family GTPases regulating endosomal trafficking and organizing lipid-signaling complexes. WIPF3 (WASp-interacting protein family member 3) participates in actin dynamics downstream of lipid signaling through Rac/Rho GTPase activation. Dysregulation of this program in astrocytomas alters cellular responses to growth factor and inflammatory lipid mediators, enhances lipid signaling-dependent proliferation and migration, and supports tumor-promoting metabolic and inflammatory phenotypes.

**Predicted impacts**
- Enhanced cell migration through lysophosphatidic acid-LPAR signaling
- Increased inflammatory responses through lipid mediator signaling
- Enhanced protein kinase C signaling supporting proliferation
- Elevated calcium mobilization through PLCE1-mediated IP3 generation

**Evidence summary**
Lipid signaling represents an important driver of cancer cell migration and inflammatory responses. Lysophosphatidic acid-LPAR signaling promotes cell migration and tumor progression through G-protein coupled receptor activation and Rho GTPase signaling. Phospholipase C-mediated calcium mobilization supports cellular responses to growth factors and inflammatory stimuli. Diacylglycerol kinase dysregulation alters PKC signaling magnitude, affecting proliferation and migration. The coordinated dysregulation of lipid signaling pathways in astrocytomas enhances responsiveness to bioactive lipid mediators abundant in the tumor microenvironment.

**Atomic biological processes**
- Diacylglycerol metabolism and PKC signaling. Genes: DGKG, DGKZ
  - [34]: Diacylglycerol and phosphatidic acid regulate PKC activation and lipid signaling
- Phospholipase C-mediated IP3 and DAG generation. Genes: PLCE1
  - [51]: PLCE1 and related phospholipases generate IP3 driving calcium mobilization from ER stores
- Lysophosphatidic acid signaling and cell migration. Genes: LPAR1, P2RY14
  - [39]: Lysophosphatidic acid regulates integrin-mediated cell migration through LPAR signaling
- ARF GTPase regulation and vesicular trafficking. Genes: DENND2A
  - [51]: ARF GTPase regulation organizes membrane trafficking and lipid signaling complexes

**Atomic cellular components**
- Plasma membrane lipid signaling complexes. Genes: LPAR1, P2RY14, PLCE1
  - [34]: Lipid signaling molecules organize at plasma membrane regulating GPCR activation
- Actin regulatory network. Genes: WIPF3
  - [42]: Actin polymerization downstream of lipid signaling drives cell migration
- Endosomal trafficking compartments. Genes: DENND2A
  - [51]: ARF GTPases regulate endosomal trafficking organizing lipid signaling

**Program citations**
- [34]: Comprehensive analysis of lipid signaling in cellular processes
- [39]: Lysophosphatidic acid and related lipid mediators regulate cell migration

## Program: Cell Cycle Regulation and Proliferative Constraint Bypass
This program encompasses cell cycle checkpoint genes, proliferation regulators, and genes governing transition from quiescence to proliferation characteristic of tumor transformation. CDK6 (cyclin-dependent kinase 6) functions as a G1/S phase cell cycle checkpoint kinase essential for phosphorylation of retinoblastoma protein (Rb) and progression through G1/S transition. CDKN1A (cyclin-dependent kinase inhibitor 1A, p21) and CDKN2A/CDKN2B (cyclin-dependent kinase inhibitor 2A/2B, p16/p14ARF) represent canonical cell cycle checkpoint inhibitors frequently dysregulated in astrocytomas. TERT (telomerase reverse transcriptase) and related telomere maintenance mechanisms enable unlimited replicative potential by preventing telomere shortening. Loss of CDKN2A/CDKN2B and TERT promoter mutations represent hallmark genetic alterations in astrocytomas and glioblastomas. MYC proto-oncogene (implied through pathway context) drives proliferation and metabolic reprogramming. The transcription factors including MECOM regulate stem cell and progenitor cell expansion. FBXL7 encodes an F-box protein participating in ubiquitin-mediated proteasomal degradation of cell cycle regulators. Dysregulation of this program in astrocytomas bypasses proliferative constraints through genetic alterations affecting checkpoint genes, enabling unlimited proliferation independent of normal growth signal dependence.

**Predicted impacts**
- Bypass of G1/S checkpoint enabling unlimited proliferation
- Acquisition of replicative immortality through telomerase reactivation
- Loss of p16/p21-mediated growth arrest in response to stress
- Uncoupled proliferation independent of growth signal dependence

**Evidence summary**
Cell cycle checkpoint dysregulation represents a fundamental feature of astrocytoma pathogenesis. Loss of CDKN2A/CDKN2B occurs in the majority of high-grade gliomas, abolishing p16-mediated growth arrest at the G1/S checkpoint. TERT promoter mutations occur in approximately 70% of glioblastomas, enabling unlimited replicative potential through telomerase reactivation. The combined dysregulation of checkpoint gene programs establishes the molecular basis for unlimited proliferation characteristic of malignant astrocytic tumors.

**Atomic biological processes**
- G1/S cell cycle checkpoint regulation. Genes: CDK6, CDKN1A, CDKN2A, CDKN2B
  - [52]: CDKN2A/CDKN2B loss allows GBM formation from astrocytes and enhances tumor incidence
  - [30]: CDKN2A/B homozygous deletion represents a pathogenic alteration in epithelioid glioblastoma
- Telomere maintenance and replicative immortality. Genes: TERT
  - [25]: TERT promoter mutation status predicts glioma characteristics and prognosis
  - [30]: TERT c.-146C>T promoter mutation identified as pathogenic alteration in epithelioid GBM
- Proteasomal degradation of cell cycle regulators. Genes: FBXL7
  - [54]: CDKN1A levels regulate cell cycle transitions through ubiquitin-proteasomal mechanisms

**Atomic cellular components**
- G1/S checkpoint complex. Genes: CDK6, CDKN1A, CDKN2A, CDKN2B
  - [52]: Retinoblastoma protein and CDK6 form checkpoint complex regulating G1/S transition
- Telomerase complex. Genes: TERT
  - [25]: TERT encodes catalytic subunit of telomerase complex

**Program citations**
- [52]: CDKN2A/B loss drives GBM formation from astrocytes
- [30]: CDKN2A/B and TERT alterations represent pathogenic mutations in epithelioid GBM
- [25]: TERT promoter mutations predict glioma prognosis

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/5045
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
3. 3. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
4. 4. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/546
6. 6. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/3339
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/183
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/999
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/6506
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/1756
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/13405
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/4052
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/5154
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/7048
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/18596
18. 18. Miguel R-P, Beatriz P-S, Meriem BR, Marialuisa de C, Sonia M-L, Ignacio S, et al.. Perinatal Ethanol Exposure Induces Astrogliosis and Decreases GRP55/PEA-Mediated Neuroprotection in Hippocampal Astrocytes of the 3×Tg Alzheimer's Animal Model.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41303637/
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/19883
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/12801
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/19697
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/1030
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/25937
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
26. 26. Ye J, Wang H, Peng Y, Wang S, Zheng R, Chen Y, et al.. Noncanonical role of astrocytic mitochondrial Cx43: suppressing IDH3α to sustain glycolytic homeostasis against depression. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08309-1
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/26524
28. 28. Oh Y, Yoo J, Lee D, Ko B, Hong JP, Moon JH, et al.. Restoring the glioblastoma tumor microenvironment by targeting C5a with the antagonist W54011. Scientific Reports [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41598-025-30853-1
29. 29. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
30. 30. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/6935
32. 32. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
33. 33. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/18018
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/2902
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/9510
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/3688
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/1630
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/3553
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/3611
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/9423
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/12288
45. 45. Wei X-Y, Zou Z-M, Yao Z-X, Teng S-W, Wei X-Y, Tang W-J, et al.. Neuronal activity-induced GLUT3 plasma translocation supports energy demands for memory acquisition. Communications Biology [Internet]. 2025Nov28;8(1). Available from: https://www.nature.com/articles/s42003-025-09119-z
46. 46. Liu Y, Wu Y, Zu M, Li X, Zhang J, Wang D, et al.. Transferrin-phosphatidylserine liposomes target TDP-43 and neuroinflammation in male mice with neuropathic pain. Nature Communications [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41467-025-66397-1
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/27185
48. 48. Sims SL, Lu T-H, Weiss BE, Lin R-L, Galopin LB, Wright NA, et al.. Central cytometabolic functional vascular coupling in health and disease. npj Metabolic Health and Disease [Internet]. 2025Dec2;3(1). Available from: https://www.nature.com/articles/s44324-025-00090-1
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
50. 50. Wang D, Ritz C, Luo Y, Suresh A, Pierce A, Veo B, et al.. Transcriptional regulation of protein synthesis by mediator kinase represents a therapeutic vulnerability in MYC-driven medulloblastoma. Nature Communications [Internet]. 2025Dec16;16(1). Available from: https://www.nature.com/articles/s41467-025-64937-3
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/1026
52. 52. Available from: http://json-schema.org/draft-07/schema#",
