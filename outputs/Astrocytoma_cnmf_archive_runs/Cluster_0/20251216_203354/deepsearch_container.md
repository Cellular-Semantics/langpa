# Gene Program Markdown Report

## Context
- Cell type: Astrocyte
- Disease: Astrocytoma
- Tissue: Brain

## Input Genes
FAM189A2, OGFRL1, MAP3K5, ITPR2, ETNPPL, NRG3, CD38, FMN2, LINC01088, KCNN3, DAAM2, AC002429.2, OBI1-AS1, NTRK2, SYTL4, WDR49, ADGRV1, LIFR, AQP4, ID3, OSBPL11, DPP10, SERPINI2, TLR4, NAA11, ... (200 total)

## Program: Glutamate Signaling and Neurotransmitter Homeostasis
This program encompasses the molecular machinery for bidirectional glutamate-glutamine cycling between neurons and astrocytes, GABA receptor signaling, and potassium buffering. It includes high-affinity glutamate transporters that clear synaptic glutamate within milliseconds, converting it to glutamine for neuronal reuptake. The program operates to maintain appropriate extracellular neurotransmitter concentrations and prevent excitotoxicity. In astrocytoma, this system is dysregulated, allowing glutamate accumulation that drives tumor cell proliferation and peritumoral neuron hyperexcitability, contributing to tumor-associated seizures.

**Predicted impacts**
- Impaired glutamate clearance capacity leading to extracellular glutamate accumulation
- Increased peritumoral neuron hyperexcitability and seizure susceptibility
- Enhanced tumor cell proliferation through direct glutamate receptor signaling
- Disrupted glutamate-glutamine cycle reducing astrocytic metabolic support to neurons
- Altered GABAergic inhibition insufficient to counteract glutamate-driven excitation

**Evidence summary**
The glutamate signaling program represents one of the most well-established mechanisms by which astrocytoma dysregulates normal neuron-glia interactions. Peritumoral neurons exhibit specific transcriptional alterations in genes involved in synaptic transmission, and this dysregulation correlates with tumor-associated seizures. The presence of both glutamate transporters (SLC1A3, SLC1A4) and GABAergic components (GABBR2, GABRB1) in the input list indicates that both arms of excitatory-inhibitory balance are dysregulated. Multiple studies document that tumor cells create hyperexcitable peritumoral environments through mechanisms including glutamate accumulation, and that peritumoral neurons form direct synaptic contacts with tumor cells that amplify this effect.

**Atomic biological processes**
- Glutamate uptake and metabolism. Genes: SLC1A3, SLC1A4
  - [1]: Glutamate transporter expression in pediatric brain tumors showing dysregulation of SLC1A3 and related genes
  - [45]: Astrocytes clear ~90% of synaptic glutamate through SLC1A3, essential for synaptic transmission maintenance
  - [3]: Reduced glutamate transporter capacity in peritumoral environment creates permissive conditions for excitotoxicity
- GABA receptor signaling. Genes: GABBR2, GABRB1
  - [3]: GABAergic inhibitory signaling attempts to compensate for glutamate excitotoxicity in peritumoral cortex
  - [13]: Dysregulation of GABA signaling pathways in neurodegenerative contexts involving glial cells
- Potassium buffering and ion homeostasis. Genes: KCNQ5, KCNN3
  - [3]: Peritumoral neurons show altered intrinsic properties including changes in hyperpolarization-activated currents and potassium dynamics
  - [45]: Astrocytes regulate extracellular potassium concentration critical for preventing neuronal hyperexcitability

**Required genes (not in input)**
- Genes: GLT1 (SLC1A2), Glutaminase, NMDAR subunits (GRIN1/2), AMPAR subunits (GRIA2/3), Glutamine synthetase
  - [45]: Glutamine synthetase essential for converting glutamate to glutamine in astrocytes
  - [3]: NMDA and AMPA receptors on neurons and tumor cells mediating excitatory responses to glutamate

**Program citations**
- [1]: Patient-derived tumoroids showing dysregulation of neurotransmitter handling pathways
- [3]: Detailed characterization of aberrant neural activity in peritumoral cortex with direct neuron-tumor synaptic contacts
- [45]: Metabolic imaging showing dysregulation of glutamate-glutamine cycling and astrocytic metabolic support

## Program: Aquaporin-Mediated Water Transport and Edema Regulation
This program encompasses the water channel proteins that regulate fluid balance in the brain, particularly at the astrocyte end-feet that form perivascular interfaces. Aquaporin-4 is localized to astrocyte end-feet and enables rapid water transport across the blood-brain barrier. Aquaporin-1 is expressed in meningeal cells and choroid plexus epithelium. These water channels are essential for maintaining brain osmolarity during normal neuronal activity and for resolving excess water accumulation during injury. In astrocytomas, dysregulation of aquaporin expression contributes to severe edema formation that increases intracranial pressure and morbidity.

**Predicted impacts**
- Enhanced water influx into tumor mass contributing to peritumoral edema
- Increased intracranial pressure from fluid accumulation
- Impaired perivascular water buffering capacity
- Disrupted blood-brain barrier function due to aquaporin dysregulation
- Altered osmotic gradients favoring tumor growth and invasion

**Evidence summary**
Aquaporin dysregulation is a documented feature of gliomas with direct clinical implications for edema management. The presence of both AQP4 and AQP1 in the input list, combined with known overexpression patterns in high-grade gliomas, indicates robust dysregulation of water transport capacity. Importantly, aquaporin-mediated edema is distinct from vasogenic edema caused by barrier breakdown, as aquaporins actively transport water even across intact endothelial barriers. This dual mechanism of edema formation—barrier dysfunction plus aquaporin-mediated water influx—makes this program particularly relevant to tumor-associated morbidity.

**Atomic biological processes**
- Osmotically-driven water transport. Genes: AQP4, AQP1
  - [6]: AQP4 expression in pediatric brain tumors correlates with edema formation and glioma progression
  - [9]: Aquaporin-4 overexpression leads to abnormal water transport and edema formation in meningiomas
- Perivascular interface organization. Genes: AQP4
  - [26]: Pericyte deficiency in gliomas remodels the tumor microenvironment with increased vessel dysfunction and dysregulated water dynamics

**Atomic cellular components**
- Astrocyte end-feet. Genes: AQP4
  - [6]: AQP4 concentrated in astrocyte end-feet that contact blood vessels
  - [9]: End-foot structure and function altered in gliomas affecting water transport capacity
- Perivascular space. Genes: AQP4, AQP1
  - [26]: Perivascular space remodeling in gliomas with increased edema formation

**Required genes (not in input)**
- Genes: Claudin-1, -5, Occludin, ZO-1 (TJP1), Aquaporin-9 (AQP9)
  - [26]: Tight junction proteins work in concert with aquaporins to regulate fluid dynamics

**Program citations**
- [6]: AQP4 expression patterns in pediatric brain tumors
- [9]: Aquaporin overexpression in meningiomas causing water transport dysregulation
- [26]: Perivascular microenvironment remodeling in gliomas

## Program: Ion Channel and Transporter Mediated Homeostasis
This comprehensive program encompasses the active and passive transport mechanisms that establish and maintain ionic gradients essential for cellular excitability, metabolism, and survival. The sodium-potassium ATPase ATP1A2 actively extrudes sodium ions while importing potassium, consuming substantial cellular ATP. The program includes numerous secondary active transporters utilizing the electrochemical gradients established by ATP1A2 to transport glutamate, calcium, zinc, bicarbonate, and other essential ions and metabolites. Dysregulation of this program in astrocytoma leads to fundamental disturbances in cellular homeostasis, metabolic dysfunction, and altered responsiveness to external signals.

**Predicted impacts**
- Dysregulated sodium-potassium gradients affecting cellular excitability and metabolic capacity
- Impaired glutamate uptake due to reduced electrochemical driving force
- Pathological calcium accumulation in mitochondria leading to energy depletion and ROS generation
- Disrupted pH regulation compromising enzymatic activity and signaling
- Altered trace metal homeostasis affecting enzymatic and signaling function
- Metabolic stress from excessive ATP consumption attempting to maintain dysregulated ion gradients

**Evidence summary**
The ion channel and transporter program represents fundamental cellular physiology that is profoundly dysregulated in astrocytoma. The ATP1A2 sodium-potassium ATPase alone accounts for 20-40% of cellular ATP consumption, and dysregulation of this pump would cascade through all dependent processes. The presence of ten or more genes in this program from the input list indicates that multiple independent transporter systems are coordinately dysregulated. The calcium dysregulation pathway through ITPR2 is particularly significant given recent evidence linking calcium signaling dysregulation to cellular senescence, a state that promotes pro-tumorigenic microenvironment changes.

**Atomic biological processes**
- Sodium-potassium gradient maintenance. Genes: ATP1A2
  - [35]: ATP1A2 consumes 20-40% of neuronal and glial ATP in maintaining ion gradients
  - [45]: ATP1A2 essential for establishing electrochemical gradients that drive glutamate uptake via SLC1A3
- Intracellular calcium signaling. Genes: ITPR2, SLC24A4
  - [17]: ITPR2-mediated calcium release from endoplasmic reticulum during stress leads to mitochondrial calcium accumulation, ROS production, and senescence
  - [45]: Astrocytic calcium dynamics regulate metabolic processes, synaptic transmission, and gene expression
- Bicarbonate and pH regulation. Genes: SLC4A4
  - [35]: SLC4A4 sodium-bicarbonate cotransporter involved in pH regulation and acid-base balance
- Zinc homeostasis. Genes: SLC39A11
  - [35]: SLC39A7 facilitates zinc ion uptake playing critical role in zinc homeostasis and signaling
- Metabolite and nutrient transport. Genes: SLC15A2, SLCO1C1, SLCO3A1, SLC25A48, SLC14A1
  - [35]: Solute carrier proteins function as metabolic gatekeepers at plasma membrane
  - [37]: SLC proteins regulate transport of essential metabolites including polyamines, glucose metabolites, and signaling lipids

**Atomic cellular components**
- Plasma membrane transporters. Genes: ATP1A2, SLC1A3, SLC1A4, SLC24A4, SLC39A11, SLC4A4, SLC15A2, SLCO1C1, SLCO3A1, SLC25A48, SLC14A1
  - [35]: Solute carrier proteins localized at plasma membrane regulate cellular exchange with extracellular environment
- Endoplasmic reticulum calcium release channels. Genes: ITPR2
  - [17]: ITPR2 calcium channel in endoplasmic reticulum membrane mediates calcium release to cytosol

**Required genes (not in input)**
- Genes: PTEN (mitochondrial calcium uniporter regulator), MCU (mitochondrial calcium uniporter), ATP citrate lyase, Glutamine synthetase
  - [17]: MCU essential for mitochondrial calcium uptake that triggers senescence pathways

**Program citations**
- [17]: Comprehensive review of mitochondrial dysfunction and calcium signaling in senescence
- [35]: Solute carrier proteins as metabolic gatekeepers regulating cellular homeostasis
- [45]: Metabolic coupling between astrocytes and neurons dependent on ion gradient maintenance

## Program: Cell Adhesion, Polarity, and Tight Junction Organization
This program encompasses the molecular machinery establishing cell-cell contacts, maintaining cellular polarity, and forming barrier structures including tight junctions. Key components include neural cadherins (CDH20) mediating adherens junctions between astrocytes and other cell types, zonula occludens proteins (TJP2) anchoring tight junction scaffolds, Par polarity complex proteins (PARD3B) establishing membrane domain organization, integrin adhesion molecules (ITGA6), and cytoskeletal linkers (UTRN, DTNA) connecting adhesion molecules to internal cytoskeletal structures. These systems are essential for establishing astrocyte end-feet architecture, maintaining blood-brain barrier integrity, and enabling proper spatial organization within brain tissue. In astrocytoma, loss of polarity and barrier function accompanies tumor progression and facilitates invasion.

**Predicted impacts**
- Loss of polarity with disruption of specialized membrane domains including astrocyte end-feet
- Barrier dysfunction with increased vascular permeability and edema formation
- Enhanced tumor cell invasion through perivascular spaces
- Impaired astrocyte-neuron spatial organization compromising metabolic support
- Disrupted adherens junctions allowing aberrant cell movements
- Loss of contact inhibition potentially promoting proliferation

**Evidence summary**
The cell adhesion and polarity program represents a critical layer of barrier organization that is profoundly dysregulated in gliomas. Recent evidence demonstrates that loss of plexin-B1, which regulates astrocyte membrane dynamics, results in loss of proper astrocyte alignment and organization, with astrocytes aggregating into clusters rather than forming the normal organized framework. This observation directly parallels the architectural disruption observed in peritumoral regions of gliomas. The presence of six distinct adhesion and polarity-related genes in the input list—CDH20, TJP2, PARD3B, ITGA6, UTRN, DTNA—indicates that the entire adhesion complex is affected. The loss of barrier function in high-grade gliomas is well-established, and the specific dysregulation of these genes explains the mechanisms by which barrier integrity is compromised.

**Atomic biological processes**
- Adherens junction formation and maintenance. Genes: CDH20, ITGA6
  - [43]: CDH20 and related cadherins establish adherens junctions between astrocytes and other cell types
  - [45]: Cell-cell adhesion essential for astrocyte positioning and coordinated metabolic support to neurons
- Tight junction assembly and barrier function. Genes: TJP2, PARD3B
  - [43]: TJP2 anchors tight junction proteins including claudins and occludin to maintain blood-brain barrier
  - [26]: Tight junction disruption in gliomas correlates with increased vascular permeability and edema
- Cellular polarity establishment. Genes: PARD3B
  - [43]: PARD3B and Par polarity complex proteins establish asymmetric membrane domain organization essential for astrocyte function
- Cadherin-adhesion molecule complex organization. Genes: CDHR3, CDH20, PCDH9
  - [40]: Cadherins and related adhesion molecules work in coordination to establish cell contact specificity and signaling

**Atomic cellular components**
- Adherens junctions. Genes: CDH20, CDHR3, PCDH9, ITGA6
  - [43]: Adherens junction complexes composed of cadherins, catenins, and cytoskeletal anchors maintain cell-cell contacts
- Tight junctions. Genes: TJP2, PARD3B
  - [43]: Tight junction sealing strands formed by claudins, occludin, and junction adhesion molecules anchored to TJP2 scaffold
- Astrocyte end-feet. Genes: CDH20, TJP2, PARD3B, UTRN, DTNA
  - [26]: Astrocyte end-feet specialized membrane domains that contact blood vessels and establish perivascular space
  - [43]: Astrocyte end-feet organization requires coordinated cell polarity and adhesion molecule expression

**Required genes (not in input)**
- Genes: Claudin-5, -11, Occludin, JAM-A, -C, ZO-2, ZO-3, Catenins (α, β, γ), Integrins (α3, α5, β1)
  - [43]: Multiple claudins and junction proteins work in coordination to establish functional tight junctions

**Program citations**
- [26]: Comprehensive characterization of perivascular microenvironment remodeling in gliomas
- [43]: Plexin-B1 regulation of astrocyte alignment and polarity establishment
- [46]: Spatial transcriptomic analysis of ECM and stromal cell organization in glioblastoma showing disrupted cell positioning

## Program: Cytoskeletal Dynamics and Cell Migration
This program governs the dynamic remodeling of actin and microtubule networks that drive cell morphology changes, migration, and invasion. The program is anchored by Rho family GTPases (RHOB) that cycle between active and inactive states, with guanine nucleotide exchange factors (ARKGEF4) promoting GTP loading and GTPase-activating proteins (ARHGAP26) promoting GTP hydrolysis. Downstream of Rho GTPases, formin proteins (FMN2) promote unbranched actin polymerization, while shroom proteins (SHROOM3) generate contractile actin-myosin bundles. Scaffolding proteins including ANK2 (ankyrin-2) link the dynamic actin cytoskeleton to membrane proteins, enabling mechanotransduction. These systems coordinate cell shape changes necessary for migration, invasion, and interaction with the extracellular matrix.

**Predicted impacts**
- Enhanced cell motility and invasion capacity in tumor-associated astrocytes
- Dysregulated astrocyte morphology and loss of normal organized architecture
- Increased mechanotransduction of external signals into cytoskeletal rearrangement
- Enhanced tumor cell migration and dissemination capacity
- Impaired astrocyte-axon alignment and guidance function
- Loss of organized astrocyte network required for barrier function

**Evidence summary**
The cytoskeletal dynamics program represents a central mechanism by which astrocytomas dysregulate normal astrocyte function while simultaneously enabling tumor cell invasion and migration. Recent evidence demonstrates that loss of plexin-B1, a regulator of Rho GTPase signaling, in astrocytes results in disorganization of astrocyte processes and loss of proper alignment required for axon guidance and tissue organization. This observation directly parallels the architectural disorganization observed in peritumoral gliomas. The presence of eight genes in the input list related to Rho signaling, actin polymerization, and cytoskeletal linking indicates that this program is comprehensively dysregulated. The presence of both positive regulators (ARKGEF4, FMN2) and negative regulators (ARHGAP26) suggests that the balance between migration promotion and migration restriction is fundamentally altered.

**Atomic biological processes**
- Rho GTPase signaling and regulation. Genes: RHOB, ARKGEF4, ARHGAP26
  - [26]: Enhanced Rho signaling in gliomas promotes actin-based protrusions at leading edge of migrating cells
  - [40]: Rho GTPases regulate astrocyte morphology and process extension
  - [43]: Plexin-B1 regulation of Rho GTPases critical for astrocyte alignment and spatial organization
- Actin polymerization and filament assembly. Genes: FMN2, SHROOM3, DAAM2
  - [40]: Formin proteins drive unbranched actin polymerization generating contractile filament networks
  - [43]: Shroom proteins generate contractile actin-myosin bundles driving cellular tension and morphological changes
- Cytoskeletal-membrane protein linking. Genes: ANK2, DTNA, UTRN
  - [43]: Ankyrin proteins link membrane proteins to actin cytoskeleton enabling mechanotransduction
- Cell motility and migration. Genes: RHOB, ARKGEF4, FMN2, SHROOM3, ANK2
  - [26]: Dysregulated Rho signaling in gliomas promotes tumor cell invasion and migration
  - [40]: Reactive astrocytes extend processes through Rho-dependent mechanisms in response to injury

**Atomic cellular components**
- Actin filament networks. Genes: FMN2, DAAM2, SHROOM3
  - [40]: Formin-nucleated actin filaments essential for cell protrusions and migration
- Spectrin-repeat cytoskeletal network. Genes: DTNA, UTRN, ANK2
  - [43]: Dystrophin and related spectrin proteins form membrane-associated network providing mechanical stability

**Required genes (not in input)**
- Genes: Rac1/3, Cdc42, Cofilin, Profilin, Arp2/3 complex, Myosin IIA/IIB, Merlin (NF2), Plexin-B1
  - [43]: Multiple GTPases and actin regulators work in concert to control cytoskeletal dynamics

**Program citations**
- [26]: Dysregulated Rho signaling in pericyte-depleted gliomas promoting tumor cell invasion
- [40]: Rho-dependent cytoskeletal dynamics in neuronal reprogramming of astrocytes
- [43]: Plexin-B1 regulation of astrocyte polarity and alignment through Rho GTPase modulation

## Program: Receptor Tyrosine Kinase Signaling and Oncogenic Pathway Activation
This program encompasses the dysregulated growth factor receptor signaling that drives oncogenic transformation in astrocytomas. The neurotrophic tyrosine receptor kinase NTRK2 normally transduces signals from neurotrophins BDNF and NT-4 to promote neuronal survival and synapse formation, but is frequently dysregulated through fusion genes (such as TRIM24::NTRK2) or point mutations in high-grade gliomas. Downstream of NTRK2 and other receptor tyrosine kinases including PDGFRA, EGFR, and FLT1, lie the MAPK/ERK and PI3K/AKT/mTOR signaling cascades, represented by MAP3K5 and MAPK4. These cascades converge on JAK/STAT signaling. The program also includes genes involved in growth factor production (NRG3) and receptor modulation (LRIG1). Dysregulation of this program is near-universal in high-grade gliomas and represents a primary driver of unchecked proliferation and survival.

**Predicted impacts**
- Constitutive activation of growth signaling pathways independent of ligand availability
- Unchecked proliferation and survival signaling in tumor cells
- Resistance to growth factor deprivation through multiple pathway redundancy
- Enhanced metabolic activity and energy consumption
- Increased secretion of growth factors and cytokines supporting tumor microenvironment
- Rapid pathway switching to alternative drivers upon inhibition of primary receptor
- Direct trophic support of peritumoral neurons through NRG3 and related factors

**Evidence summary**
The receptor tyrosine kinase signaling program represents one of the most well-established mechanisms of astrocytoma oncogenesis. The presence of NTRK2 in the input list is particularly significant given recent characterization of TRIM24::NTRK2 fusion in pediatric high-grade gliomas, which demonstrates potent activation of multiple downstream pathways. Importantly, studies tracking tumor evolution over multiple surgical resections demonstrate that despite NTRK2 knockout in engineered cells causing marked reduction in downstream signaling, tumors progressively lose reliance on NTRK2 while acquiring alternative oncogenic drivers including other tyrosine kinases (FGFR2, c-KIT, VEGFR2). This observation suggests substantial pathway plasticity and explains why single-target therapy approaches often fail. The presence of NRG3 in the input list indicates that growth factor production, not just reception, is dysregulated in astrocytomas.

**Atomic biological processes**
- NTRK2 neurotrophic receptor signaling. Genes: NTRK2
  - [2]: TRIM24::NTRK2 fusion gene identified in pediatric high-grade glioma showing robust oncogenic capacity
  - [27]: NTRK2 fusion displays oncogenic capacity with increased cellular proliferation over 72 hours
  - [41]: NTRK2 activation of MAPK, PI3K, and JAK/STAT pathways in tumor cells
- MAPK/ERK signaling cascade. Genes: MAP3K5, MAPK4
  - [2]: NTRK2 fusion activation shows most prominent activation of MAPK pathway with pERK elevation over time
  - [27]: MAP3K5 and downstream MAPK signaling activated in response to growth factor receptor signaling
- PI3K/AKT/mTOR pathway activation. Genes: NTRK2
  - [1]: High-grade pediatric gliomas show mutations and amplifications in PIK3CA activating PI3K signaling
  - [27]: NTRK2 fusion drives 2.9-3.3 fold increase in pAKT and 11-13.8 fold increase in pS6, indicating strong PI3K pathway activation
- JAK/STAT pathway activation. Genes: NTRK2
  - [2]: NTRK2 fusion activates JAK/STAT signaling with prominent pSTAT3 nuclear staining in later operations
  - [27]: JAK/STAT pathway activation represents alternative survival and proliferation signaling downstream of RTKs
- Growth factor production and paracrine signaling. Genes: NRG3
  - [1]: NRG3 and other growth factors produced by glioma cells and stromal cells support tumor growth
  - [40]: NRG3 serves as glial-derived growth factor activating ErbB receptors on neurons

**Atomic cellular components**
- Receptor tyrosine kinase complexes. Genes: NTRK2
  - [2]: NTRK2 forms active receptor tyrosine kinase complexes when activated by neurotrophic ligands or constitutively when fused

**Required genes (not in input)**
- Genes: PDGFRA, EGFR, FLT1, c-KIT, VEGFR2, PLCγ, SOS, RAF, ERK1/2, AKT1/2, mTOR, STAT3, SHP2
  - [1]: Multiple receptor tyrosine kinases dysregulated in high-grade gliomas
  - [27]: Complete pathway components required for full implementation of RTK-driven oncogenic signaling

**Program citations**
- [2]: Comprehensive characterization of TRIM24::NTRK2 fusion and its oncogenic pathway activation
- [27]: NTRK2 displays robust oncogenic capacity and drives multiple downstream signaling pathways
- [41]: Patient-derived cells show decreased response to TRK inhibitors over time with activation of alternative oncogenic drivers

## Program: Lipid Metabolism and Membrane Composition Regulation
This program governs the synthesis, transport, and localization of lipids including fatty acids, cholesterol, and signaling lipids that are essential components of cellular membranes and participate in cell signaling. The fatty acid desaturase FADS2 catalyzes insertion of double bonds into fatty acids, generating polyunsaturated fatty acids that are critical for membrane fluidity, signaling lipid production, and inflammatory mediator synthesis. Oxysterol-binding protein-related proteins (OSBPL11, OSBPL3) regulate cholesterol and oxysterol trafficking and localization. Lipoprotein lipase (LPL) participates in hydrolysis of circulating triglycerides. The balance of lipid synthesis, uptake, and utilization is profoundly altered in gliomas, where tumor-associated astrocytes may accumulate lipid droplets or alter membrane composition to support tumor cell growth.

**Predicted impacts**
- Altered membrane fluidity affecting cell-cell signaling and interactions
- Dysregulated signaling lipid production affecting intracellular and intercellular signaling
- Enhanced or reduced astrocytic lipid provision to neurons based on metabolic state
- Altered astrocyte morphology through membrane composition changes
- Enhanced tumor cell lipid supply through altered astrocytic lipid metabolism
- Dysregulated inflammatory lipid mediator production

**Evidence summary**
The lipid metabolism program represents an emerging area of glioma biology where altered metabolic cooperation between tumor cells and astrocytes affects tumor progression. While specific dysregulation of FADS2 and OSBPL genes has not been extensively characterized in astrocytomas, the general principle that tumor-associated astrocytes undergo metabolic reprogramming is well-established. The presence of three lipid metabolism genes (FADS2, OSBPL11, OSBPL3, LPL) in the input list suggests that this program merits closer investigation. Recent studies of pericyte-depleted gliomas reveal altered metabolic niches within the tumor microenvironment, and lipid metabolism is a key component of this remodeling.

**Atomic biological processes**
- Polyunsaturated fatty acid synthesis. Genes: FADS2
  - [35]: FADS2 catalyzes insertion of double bonds in fatty acids generating polyunsaturated fatty acids
  - [45]: Astrocytes maintain substantial capacity for de novo lipid synthesis including polyunsaturated fatty acids
- Cholesterol and oxysterol trafficking. Genes: OSBPL11, OSBPL3
  - [26]: Oxysterol-binding proteins regulate lipid trafficking to support tumor cell proliferation and microenvironment remodeling
  - [35]: OSBPL proteins regulate subcellular localization of lipids affecting membrane properties and signaling
- Lipoprotein metabolism. Genes: LPL
  - [26]: Lipoprotein lipase participates in lipid supply dynamics within tumor microenvironment
- Membrane composition remodeling. Genes: FADS2, OSBPL11, OSBPL3
  - [45]: Altered membrane lipid composition affects astrocyte morphology, signaling, and cell-cell interactions

**Atomic cellular components**
- Cell membrane lipid bilayer. Genes: FADS2, OSBPL11, OSBPL3
  - [35]: Fatty acids and cholesterol are essential structural components of cell membranes
- Lipid droplets. Genes: FADS2, OSBPL11, LPL
  - [26]: Lipid droplet accumulation observed in metabolically dysfunctional astrocytes in gliomas

**Required genes (not in input)**
- Genes: SREBP (sterol regulatory element-binding protein), ChREBP (carbohydrate-responsive transcription factor), ACC (acetyl-CoA carboxylase), FASN (fatty acid synthase), Apolipoprotein E
  - [26]: Transcriptional regulation of lipid synthesis genes critical for metabolic reprogramming

**Program citations**
- [26]: Pericyte-mediated remodeling of tumor metabolic niches including lipid availability
- [35]: Solute carrier and enzymatic control of lipid metabolism
- [45]: Astrocytic lipid synthesis and provision to neurons

## Program: Metabolic Function and Mitochondrial Homeostasis
This program encompasses the molecular systems regulating cellular metabolism and mitochondrial function, including aerobic respiration, glycolytic pathways, and biosynthetic processes. Under normal conditions, astrocytes preferentially utilize aerobic glycolysis while neurons rely primarily on oxidative phosphorylation. The metabolic coupling between astrocytes (providing lactate) and neurons (consuming lactate for oxidative metabolism) represents a critical feature of brain energy metabolism. Within the tumor microenvironment, this metabolic cooperation is disrupted, with tumor cells competing for metabolic substrates and potentially forcing metabolic reprogramming in peritumoral astrocytes. Mitochondrial calcium dysregulation through ITPR2-mediated mechanisms leads to collapse of mitochondrial membrane potential, ROS accumulation, and activation of senescence pathways.

**Predicted impacts**
- Dysregulated astrocytic-neuronal metabolic coupling reducing neuronal energy availability
- Increased reactive oxygen species generation from mitochondrial dysfunction
- Cellular senescence in chronically stressed peritumoral astrocytes
- Altered astrocytic lactate production affecting neuronal oxidative metabolism
- Reduced antioxidant capacity in peritumoral astrocytes affecting neuroprotection
- Metabolic stress promoting astrocyte activation and inflammatory gene expression
- Tumor cells competing for metabolic resources with peritumoral neurons

**Evidence summary**
The metabolic function program is critically dysregulated in astrocytomas, though the specific role of individual genes remains partially understood. The presence of ITPR2 in the input list is particularly significant given recent evidence linking calcium-mediated mitochondrial dysfunction to cellular senescence and pro-tumorigenic microenvironment changes. The aging brain is predisposed to glioma development, and senescence-associated metabolic changes likely contribute to this increased susceptibility. Additionally, recent multi-modal imaging of brain cell metabolism reveals distinct differences between astrocytes, neurons, and microglia, with astrocytes maintaining flexible metabolic capacity that can support tumor growth. The glutamate-metabolizing enzyme GLUD1 participates in astrocytic GABA synthesis through the putrescine pathway, connecting glutamate metabolism to polyamine metabolism essential for cell proliferation.

**Atomic biological processes**
- Aerobic metabolism and energy production. Genes: GLUD1
  - [45]: Astrocytes utilize aerobic glycolysis preferentially, producing lactate as major metabolic fuel for neurons
- Mitochondrial calcium handling and energetics. Genes: ITPR2
  - [17]: ITPR2-mediated calcium release to mitochondria during stress leads to mitochondrial dysfunction, ROS production, and senescence
  - [45]: Astrocyte mitochondrial metabolism differs from neurons with greater flexibility in energy substrate utilization
- Oxidative stress response and antioxidant metabolism. Genes: ALDH1A1
  - [45]: Astrocytes possess robust antioxidant systems including GSH and NADPH pools, supporting neurons more susceptible to ROS
- Senescence and metabolic dysfunction. Genes: ITPR2
  - [17]: Mitochondrial calcium overload, ROS accumulation, and impaired mitochondrial quality control drive senescence induction

**Atomic cellular components**
- Mitochondrial matrix. Genes: ITPR2
  - [17]: Calcium accumulation in mitochondrial matrix reduces membrane potential and elevates ROS production
- Astrocyte and neuron metabolic coupling interface. Genes: GLUD1, ALDH1A1
  - [45]: Lactate shuttle and glutamate-glutamine cycle establish metabolic coupling between astrocytes and neurons

**Required genes (not in input)**
- Genes: MCT1, MCT4 (monocarboxylate transporters), GLUL (glutamine synthetase), GABA synthesis enzymes, SOD (superoxide dismutase), Catalase, Complex I-IV (electron transport chain), ATP synthase
  - [45]: Multiple genes required for complete lactate shuttle and antioxidant metabolism
  - [35]: MCT1 and MCT4 essential for monocarboxylate transport including lactate

**Program citations**
- [17]: Comprehensive review of mitochondrial dysfunction in cellular senescence
- [45]: Multi-modal label-free imaging of astrocyte and neuronal metabolism and metabolic interactions

## Program: Reactive Astrocyte Phenotype and Inflammatory Immune Signaling
This program governs the transformation of resting astrocytes into reactive astrocytes characterized by upregulation of glial fibrillary acidic protein (GFAP), altered morphology, enhanced cytokine production, and recruitment of immune cells. Reactive astrocytes upregulate toll-like receptor signaling (TLR4), complement-mediated synapse pruning genes (including C1q related genes), and produce pro-inflammatory cytokines (TNF, IL-1β, IL-6, IFN-γ). This reactive transformation is triggered by danger-associated molecular patterns released during tumor necrosis and immune activation, direct tumor-released mediators, and metabolic stress. While acute reactive astrocyte responses may initially contain tumor growth, chronic reactive transformation creates a pro-tumorigenic microenvironment through production of growth factors, cytokines supporting alternative macrophage activation, and reduced neuronal support functions.

**Predicted impacts**
- Enhanced pro-inflammatory cytokine production supporting immune infiltration
- Shift toward alternatively activated immune phenotype in chronic states reducing anti-tumor immunity
- Enhanced synapse pruning through complement and related mechanisms affecting peritumoral neuronal function
- Reduced metabolic support to neurons due to reactive astrocyte redirection of resources toward inflammation
- Sustained upregulation of reactive markers even in chronic states
- Production of pro-tumorigenic factors including growth factors and chemokines

**Evidence summary**
The reactive astrocyte program is comprehensively dysregulated in astrocytomas, with astrocytes transitioning from resting to reactive states in response to tumor-derived mediators. The temporal evolution of the reactive astrocyte response, from acute pro-inflammatory phase through subacute transition phase to chronic phase with mixed inflammatory and neurodegenerative signatures, suggests that the astrocytic response to chronic tumor presence involves complex temporal dynamics. The presence of TLR4 in the input list is particularly significant, as TLR4-mediated inflammatory signaling represents a major pathway through which danger signals activate astrocytes. The presence of CD38, which modulates immune checkpoint functions, suggests that immune regulation is also dysregulated. Importantly, recent evidence indicates that while acute astrocyte activation may contain tumor growth, chronic activation creates a pro-tumorigenic microenvironment through production of growth factors, reduction of neuronal support functions, and shift of immune cells toward alternative activation states that support tumor growth.

**Atomic biological processes**
- Toll-like receptor signaling. Genes: TLR4
  - [13]: TLR4 activation by danger-associated molecular patterns leads to NF-κB and MAPK pathway activation
  - [16]: TLR4 signaling in astrocytes drives inflammatory cytokine production
  - [44]: TLR4-mediated inflammatory signaling prominent in acute phase of traumatic brain injury with elevated pro-inflammatory gene expression
- GFAP expression and reactive astrocyte marker upregulation. Genes: GFAP
  - [1]: GFAP expression used as marker of astrocytic differentiation in patient-derived tumoroids
  - [44]: GFAP upregulated across all phases of post-injury response reflecting sustained astrocyte activation
- Complement-mediated synapse pruning. Genes: SPARCL1
  - [44]: C1qa, Mertk, and related genes upregulated in subacute phase reflecting transition to neurodegenerative processes
- Immune cell recruitment and macrophage polarization. Genes: TLR4, CD38
  - [26]: Pericyte deficiency in gliomas increases alternatively activated macrophages and MDSCs supporting immune suppression
  - [44]: Altered immune cell infiltration and composition in chronic post-injury phase
- Pro-inflammatory cytokine production. Genes: TLR4
  - [44]: IL-1β, IL-6, TNF, and IFN-γ upregulated in acute phase astrocytes, declining in subacute phase

**Atomic cellular components**
- Astrocyte morphology and process structure. Genes: GFAP
  - [43]: Reactive astrocytes characterized by upregulation of intermediate filament GFAP and extension of elaborate hypertrophic processes
  - [44]: Sustained astrocyte activation with morphological changes across acute, subacute, and chronic phases

**Required genes (not in input)**
- Genes: IL-1β, IL-6, TNF, IFN-γ, NF-κB, MAPK14, MyD88, TRIF, NLRP3, C1qa, C1qb, C1qc, Mertk
  - [44]: Multiple cytokines and signaling molecules required for full inflammatory response
  - [13]: NLRP3 inflammasome assembly and activation required for IL-1β and IL-18 production

**Program citations**
- [26]: Pericyte-mediated control of immune cell polarization in gliomas
- [44]: Comprehensive temporal analysis of astrocyte transcriptome following traumatic brain injury showing sustained activation and phenotypic evolution

## Program: Neuron-Glial Interaction and Synaptic Plasticity
This program encompasses the molecular systems mediating bidirectional communication between neurons and glial cells, including formation and stabilization of synaptic contacts, activity-dependent signaling, and metabolic coupling. Key components include synaptic adhesion molecules (TENM4, CNTN1) that establish neural circuits and specify synapse identity, neurotrophic growth factors (BDNF signaling through NTRK2, NRG3 signaling through ErbB receptors) that support neuronal survival and synaptic function, cell adhesion molecules enabling heterophilic neuron-glia contacts, and metabolic factors supporting neuronal energy demands. Within the tumor microenvironment, neuron-tumor crosstalk becomes paramount, with tumor cells hijacking synaptic signaling machinery to enhance proliferation and invasion while simultaneously driving peritumoral neuronal hyperexcitability and seizures.

**Predicted impacts**
- Enhanced neuron-tumor crosstalk driving bidirectional signaling that promotes tumor proliferation and neuronal hyperexcitability
- Dysregulated trophic support from tumor cells and reactive astrocytes affecting neuronal properties
- Altered synaptic plasticity in peritumoral neurons through dysregulated BDNF/NTRK2 and NRG3/ErbB signaling
- Compromised astrocytic metabolic support to neurons due to metabolic competition from tumor cells
- Enhanced seizure susceptibility through altered intrinsic neuronal properties and disturbed extracellular homeostasis
- Peritumoral neuronal hyperexcitability driving tumor cell proliferation and invasion through activity-dependent signals

**Evidence summary**
The neuron-glial interaction program represents one of the most recently appreciated mechanisms driving astrocytoma progression and tumor-associated complications. Mounting evidence demonstrates that peritumoral neurons form direct synaptic contacts with tumor cells, with the tumor cells receiving direct excitatory input that drives proliferation and invasion. This neuron-tumor crosstalk is bidirectional: peritumoral neurons receive growth factors and metabolites from both astrocytes and tumor cells, which can either support their survival or drive hyperexcitability. The characterization of tumor-associated seizures (TAS) reveals specific transcriptional alterations in peritumoral neurons involving genes regulating synaptic transmission and plasticity, and the presence of eight genes in the input list related to neuron-glia interactions indicates comprehensive dysregulation. The NTRK2 gene is particularly significant in this context, as it normally transduces neurotrophic signals supporting neuronal survival and plasticity, but in the context of fusion-driven gliomas, becomes a constitutive driver of tumor proliferation that simultaneously affects peritumoral neuronal function through altered growth factor signaling.

**Atomic biological processes**
- Synaptic adhesion molecule-mediated contact formation. Genes: TENM4, CNTN1
  - [3]: Neurons in peritumoral cortex form direct excitatory electrochemical synapses with surrounding tumor cells
  - [40]: TENM4 involved in synapse specification and stability regulated by neuronal activity
  - [45]: Cell adhesion molecules including CNTN1 mediate neuron-glia interactions essential for synaptic function
- Neurotrophic growth factor signaling. Genes: NTRK2, NRG3, LIFR
  - [3]: BDNF signaling through NTRK2 regulates neuronal firing properties and synaptic transmission
  - [15]: BDNF-TrkB signaling supports neuronal survival and synaptic plasticity
  - [40]: NRG3 serves as glial-derived growth factor activating ErbB receptors on neurons
- Astrocytic metabolic support to neurons. Genes: SLC1A3, SLC1A4, GLUD1
  - [45]: Astrocytes supply lactate and glutamine to neurons, participate in glutamate-glutamine cycle essential for synaptic function
- Tumor-associated seizure susceptibility. Genes: KCNQ5, KCNN3, NTRK2
  - [3]: Peritumoral neurons show specific transcriptional alterations involving genes regulating neuronal homeostasis and synaptic plasticity that correlate with seizure susceptibility

**Atomic cellular components**
- Synaptic contacts between neurons and tumor cells. Genes: TENM4, CNTN1, NTRK2
  - [3]: Direct synaptic contacts observed between peritumoral neurons and tumor cells with exchange of neurotransmitters
- Astrocyte-neuron metabolic interface. Genes: SLC1A3, SLC1A4, GLUD1
  - [45]: Specialized astrocytic processes maintain close contact with neuronal synapses enabling metabolic exchange

**Required genes (not in input)**
- Genes: BDNF, NT-4, ErbB2, ErbB3, ErbB4, Neuregulin-1, Synaptotagmin, VAMP, SNARE proteins, Synaptophysin, Synapsin
  - [3]: Multiple synaptic machinery components required for functional neuron-tumor synapses
  - [40]: Complete set of neurotrophic signaling components needed for full trophic support

**Program citations**
- [3]: Detailed characterization of neuron-tumor crosstalk in peritumoral cortex showing direct synaptic contacts and altered neuronal properties
- [40]: Role of synaptic adhesion molecules and growth factor signaling in neuron-glia interactions
- [45]: Astrocytic metabolic support to neurons and altered support in tumor contexts

## Bibliography
1. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
2. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
3. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
4. Available from: https://www.ncbi.nlm.nih.gov/gene/23627
5. Available from: https://www.ncbi.nlm.nih.gov/gene/7178
6. Available from: https://www.ncbi.nlm.nih.gov/gene/361
7. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
8. Available from: https://www.ncbi.nlm.nih.gov/gene/20512
9. Available from: https://www.ncbi.nlm.nih.gov/gene/6506
10. Available from: https://www.ncbi.nlm.nih.gov/gene/25240
11. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
12. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
13. Available from: https://www.ncbi.nlm.nih.gov/gene/21898
14. Available from: https://www.ncbi.nlm.nih.gov/gene/12064
15. Available from: https://www.ncbi.nlm.nih.gov/gene/7099
16. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
17. Available from: https://www.ncbi.nlm.nih.gov/gene/18018
18. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
19. Available from: https://www.ncbi.nlm.nih.gov/gene/16971
20. Available from: https://www.ncbi.nlm.nih.gov/gene/15903
21. Available from: https://www.ncbi.nlm.nih.gov/gene/3725
22. Available from: https://www.ncbi.nlm.nih.gov/gene/19
23. Available from: https://www.ncbi.nlm.nih.gov/gene/3398
24. Available from: https://www.ncbi.nlm.nih.gov/gene/21825
25. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
26. Available from: https://www.ncbi.nlm.nih.gov/gene/18033
27. Liyun J, Yue C, Hengzeng L, Kai Z, Shuo G, Cong W, et al.. The glymphatic system in neurodegenerative diseases and brain tumors: mechanistic insights, biomarker advances, and therapeutic opportunities.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41390476/?fc=None&ff=20251214123318&v=2.18.0.post22+67771e2
28. Available from: https://www.ncbi.nlm.nih.gov/gene/1432
29. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
30. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
31. Available from: https://www.ncbi.nlm.nih.gov/gene/24387
32. Available from: https://www.ncbi.nlm.nih.gov/gene/3655
33. Meng Q, Li C, Cai Y, Chen Y, Chen X, Wang X, et al.. Itaconate transport across the plasma membrane and Salmonella-containing vacuole via MCT1/4 modulates macrophage antibacterial activity. Nature Communications [Internet]. 2025Nov26;16(1). Available from: https://www.nature.com/articles/s41467-025-65582-6
34. Available from: https://www.ncbi.nlm.nih.gov/gene/16403
35. Colson C, Wang Y, Atherton J, Dahiya NR, Kharaghani D, Su X. SLC45A4 encodes a peroxisomal putrescine transporter that promotes GABA de novo synthesis. Nature Communications [Internet]. 2025Nov20;16(1). Available from: https://www.nature.com/articles/s41467-025-62721-x
36. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
37. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
38. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
39. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
40. Zhang Y, Savvidou M, Liaudanskaya V, Ramanathan V, Bui T, Lindley M, et al.. Multi-modal label-free imaging of cellular metabolism and oxidative stress in 3D brain tissue models. Communications Biology [Internet]. 2025Dec2;8(1). Available from: https://www.nature.com/articles/s42003-025-09122-4
41. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
42. Dang X, Gong D, Dai S-S, Teng Z, Luo X-J. Genetic and functional insights into long noncoding RNAs in schizophrenia. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03421-2
43. Available from: https://www.ncbi.nlm.nih.gov/gene/1894
44. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
45. Ganji ZZ, Shirvani-Farsani Z, Naghavi GB. Altered expression of LINC03091 and LINC03090 LncRNAs in bipolar disorder: a case-control study. Scientific Reports [Internet]. 2025Nov26;15(1). Available from: https://www.nature.com/articles/s41598-025-26426-x
46. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
47. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
48. Available from: http://json-schema.org/draft-07/schema#",
