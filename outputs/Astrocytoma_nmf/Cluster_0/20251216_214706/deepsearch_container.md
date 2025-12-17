# Gene Program Markdown Report

## Context
- Cell type: astrocytes
- Disease: astrocytoma
- Tissue: brain

## Input Genes
FAM189A2, OGFRL1, MAP3K5, ITPR2, ETNPPL, NRG3, CD38, FMN2, LINC01088, KCNN3, DAAM2, AC002429.2, OBI1-AS1, NTRK2, SYTL4, WDR49, ADGRV1, LIFR, AQP4, ID3, OSBPL11, DPP10, SERPINI2, TLR4, NAA11, ... (200 total)

## Program: Ion Homeostasis and Intracellular Calcium Regulation
Astrocytes maintain precise extracellular ion concentrations and intracellular calcium dynamics through coordinated action of aquaporins, ion pumps, channels, and calcium-release machinery. ATP1A2 encodes the Na+/K+-ATPase critical for maintaining electrochemical gradients. AQP4 facilitates rapid water transport across membranes, particularly at perivascular endfeet. KCNN3 and KCNQ5 are potassium channels regulating membrane potential and calcium-dependent processes. ITPR2 gates IP3-mediated calcium release from the endoplasmic reticulum. SLC4A4 encodes the sodium bicarbonate cotransporter supporting pH regulation and osmotic balance. This program is essential for astrocyte volume control, glutamate uptake coupling, and responses to neuronal activity.

**Predicted impacts**
- Rapid astrocyte volume changes enabling process extension and retraction
- Maintenance of extracellular potassium homeostasis critical for neuronal excitability
- Coupling of glutamate uptake to ATP hydrolysis and lactate production
- Blood-brain barrier integrity through perivascular endfeet water transport
- Coordinated calcium signaling regulating astrocyte metabolic state and reactivity
- Disruption of ion homeostasis in tumor-derived astrocytes enabling migration and invasion

**Evidence summary**
Multiple genes from the input list encode key components of astrocyte ion homeostasis machinery. ATP1A2 serves as an energetic hub linking ion pumping to glutamate transport and metabolism. AQP4 is essential for perivascular astrocyte function and BBB maintenance, with distinct isoforms affecting orthogonal array formation. Potassium channels KCNN3 and KCNQ5 regulate membrane potential and calcium-dependent processes. ITPR2 mediates IP3-driven calcium release from ER stores, with dysregulation contributing to senescence and pathological calcium accumulation. SLC4A4 completes the osmotic regulation circuit through bicarbonate transport. In astrocytoma, disrupted ion homeostasis likely facilitates tumor cell migration through enhanced volume plasticity and enables constitutive signaling through altered calcium dynamics.

**Atomic biological processes**
- Sodium-potassium pump function and electrochemical gradient maintenance. Genes: ATP1A2
  - [9]: Describes ATP1A2 role in astrocyte energy consumption and function
  - [32]: Details ATP1A2 coupling to glutamate uptake and metabolism in astrocytes
  - [40]: Discusses astrocytic Na+/K+ ATPase in neurovascular coupling
- Water transport and osmotic regulation. Genes: AQP4, AQP1
  - [3]: Details AQP4 isoforms and orthogonal array formation at astrocyte endfeet
  - [9]: Describes AQP4 roles in blood-brain barrier function and intracellular water transport
  - [43]: Demonstrates AQP4 function in BBB model systems
- Potassium channel-mediated membrane potential control. Genes: KCNN3, KCNQ5, ABCC9
  - [56]: Discusses KCNN3 and related potassium channels in neuronal and glial function
  - [57]: Details potassium channel roles in astrocyte excitability
- IP3-mediated intracellular calcium release. Genes: ITPR2
  - [22]: Describes ITPR2 role in ammonia-induced glutamine synthetase downregulation through Hippo pathway
  - [35]: Details ITPR2-mediated calcium accumulation and senescence induction
  - [40]: Discusses calcium signaling in astrocyte-mediated neurovascular coupling
- Bicarbonate transport and pH regulation. Genes: SLC4A4
  - [40]: Discusses multiple bicarbonate transporters in astrocyte pH control

**Atomic cellular components**
- Aquaporin-water channel complex at astrocytic endfeet. Genes: AQP4, DTNA
  - [3]: Details AQP4-M23 orthogonal array assembly and perivascular localization
  - [9]: Describes perivascular astrocyte endfeet wrapping around capillaries
- Sodium-potassium ATPase pump complex. Genes: ATP1A2
  - [32]: Details ATP1A2 in astrocyte metabolism
  - [40]: Discusses ATPase localization and interactions in neurovascular complexes
- Potassium channel assembly. Genes: KCNN3, KCNQ5
  - [56]: Discusses potassium channel function in cell excitability
- ER-mitochondria calcium transfer zones. Genes: ITPR2
  - [35]: Details mitochondrial-ER contact sites and calcium transfer machinery
  - [64]: Discusses MERCS in calcium homeostasis and senescence

**Required genes (not in input)**
- Genes: SERCA2/ATP2A2 (calcium reuptake into ER), NCX (sodium-calcium exchanger), MCU (mitochondrial calcium uniporter), NKCC1/SLC12A2 (Na-K-2Cl cotransporter)
  - [40]: Discusses multiple calcium handling systems beyond those in input list

**Program citations**
- [3]: Describes AQP4 isoforms and function in astrocytes
- [9]: Comprehensive review of astrocyte ion homeostasis and BBB function
- [32]: Details astrocyte metabolism and ion pump coupling
- [40]: Discusses astrocyte ion homeostasis in neurovascular coupling

## Program: Glutamate Metabolism and Synaptic Homeostasis
Astrocytes participate in the glutamate-glutamine cycle essential for excitatory neurotransmission and neuronal survival. SLC1A3 encodes the primary high-affinity glutamate transporter responsible for synaptic glutamate clearance. SLC1A4 (ASCT2) enables glutamate uptake via cation-independent amino acid exchange. GLUD1 catalyzes bidirectional conversion between glutamate and α-ketoglutarate, linking amino acid metabolism to tricarboxylic acid cycle. Additional transporters including SLC15A2, SLC24A4, SLC14A1, and SLC39A11 enable metabolic flexibility and nutrient sensing. ITPKB regulates inositol phosphate metabolism connected to calcium signaling downstream of glutamate receptor activation. This program directly supports neuronal metabolism, prevents excitotoxicity, and maintains synaptic plasticity.

**Predicted impacts**
- Prevention of excitotoxicity through rapid synaptic glutamate clearance
- Support of neuronal GABA synthesis through glutamate recycling
- Coupling of glutamate uptake to energy production and lactate generation
- Integration of amino acid availability with metabolic state
- Maintenance of proper excitatory-inhibitory balance at synapses
- Enhanced glutamate uptake enabling metabolic support in astrocytoma supporting tumor-associated neuroinflammation

**Evidence summary**
The glutamate metabolism program is centered on SLC1A3-mediated high-affinity glutamate clearance coupled to metabolic processing through GLUD1 and the glutamate-glutamine cycle. Multiple additional amino acid transporters enable metabolic flexibility and nutrient sensing. In normal astrocytes, this program prevents excitotoxicity and supports neuronal metabolism. In astrocytoma, dysregulation of this program through altered expression of SLC1A3 and metabolic enzymes can either impair anti-tumor glutamate buffering or enhance metabolic support of malignant cells depending on specific molecular context and tumor stage.

**Atomic biological processes**
- High-affinity synaptic glutamate clearance. Genes: SLC1A3
  - [9]: Describes SLC1A3 as primary glutamate transporter in astrocytes
  - [10]: Details SLC1A3 function and genetic variations affecting expression
  - [32]: Discusses glutamate transport in astrocyte metabolism
- Glutamate-glutamine cycle and transamination. Genes: GLUD1, SLC1A3
  - [9]: Comprehensive description of glutamate-glutamine cycle in astrocytes
  - [32]: Details glutamine synthetase and cycle dynamics in astrocyte metabolism
- Amino acid exchange and branched-chain amino acid handling. Genes: SLC1A4, SLC15A2, SLC24A4, SLC14A1, SLC39A11, SLC25A48
  - [9]: Discusses astrocyte amino acid transport and metabolism
  - [32]: Details amino acid transporters in astrocyte metabolic flexibility
- Inositol phosphate metabolism and calcium signaling. Genes: ITPKB
  - [22]: Discusses inositol signaling in astrocyte regulation
  - [40]: Details IP3 signaling in astrocyte calcium dynamics

**Atomic cellular components**
- Synaptic glutamate transporter complex. Genes: SLC1A3
  - [9]: Describes SLC1A3 trafficking and localization to astrocyte processes
- Tricarboxylic acid cycle glutamate oxidation capacity. Genes: GLUD1
  - [32]: Details GLUD1 in TCA cycle and energy metabolism

**Required genes (not in input)**
- Genes: GLUL/GS (glutamine synthetase - essential for glutamine production), GLNS (glutaminase - converts glutamine back to glutamate), GLS2 (glutaminase 2)
  - [9]: Glutamine synthetase and glutaminase are critical components of glutamate-glutamine cycle
  - [22]: Details glutamine synthetase regulation and ammonia sensitivity

**Program citations**
- [9]: Comprehensive discussion of glutamate-glutamine cycle
- [10]: Details SLC1A3 genetics and astrocyte function
- [32]: Integrates glutamate metabolism with astrocyte energetics

## Program: Cytoskeletal Dynamics and Process Motility
Astrocytes maintain highly elaborate branched morphologies with dynamic process extension and retraction through coordinated regulation of actin polymerization and Rho GTPase signaling. Formin family proteins FMN2 and DAAM2 nucleate linear actin filament arrays critical for filopodia and process formation. Rho GTPase regulators ARHGAP26 and ARHGEF4 control Rac1 and Rho activation states governing process growth versus retraction. Structural proteins ASTN2, NEBL, and MAP7 stabilize microtubules and actin bundles. LIMCH1 provides additional actin-binding capacity. SHROOM3 mediates actin bundle organization and cell shape changes. DTNA (dystrophin-associated protein A) anchors cytoskeleton to membrane proteins and ECM. This program enables astrocytes to extend processes to contact neurons and vasculature while maintaining flexibility for migration and morphological adaptation.

**Predicted impacts**
- Dynamic extension and retraction of astrocytic processes enabling rapid response to neuronal activity
- Formation and maintenance of astrocyte-neuron synaptic contacts
- Perivascular endfeet stability and BBB structural integrity
- Coordinated astrocyte alignment in tissue organization
- Actin-based cell migration and invasion in tumor contexts
- Enhanced process plasticity facilitating astrocytoma cell invasion through brain parenchyma

**Evidence summary**
The cytoskeletal dynamics program comprises formin-mediated actin polymerization through FMN2 and DAAM2, Rho GTPase regulation through ARHGAP26 and ARHGEF4, and structural stabilization through SHROOM3, LIMCH1, and NEBL. Recent work demonstrates that loss of Plexin-B1 impairs astrocyte process dynamics, resulting in reduced mobility, abnormal clustering, and altered membrane fragmentation, underscoring the critical role of Rho signaling regulation in maintaining astrocyte morphological plasticity. DTNA provides membrane anchoring. In astrocytoma, enhanced cytoskeletal plasticity likely enables tumor cell invasion through brain parenchyma and supports the morphological heterogeneity characteristic of infiltrating tumors.

**Atomic biological processes**
- Actin polymerization and formin-mediated filament nucleation. Genes: FMN2, DAAM2
  - [56]: Detailed discussion of formins FMN2 and DAAM2 in axon guidance and branching
  - [57]: Discusses actin dynamics in astrocyte process extension
- Rho GTPase regulation and process extension-retraction cycling. Genes: ARHGAP26, ARHGEF4, MCF2L2, RHOB
  - [56]: Comprehensive discussion of Rho GTPase signaling in axon branching
  - [57]: Details Plexin-B1 regulation of Rac1 and astrocyte process dynamics
- Microtubule stabilization and organization. Genes: MAP7, NEBL
  - [56]: Discusses MAP proteins in axon organization
- Actin bundle assembly and cell shape organization. Genes: SHROOM3, LIMCH1
  - [57]: Details SHROOM3 role in actin bundle assembly and astrocyte morphology
- Cytoskeleton-membrane protein anchoring. Genes: DTNA
  - [9]: Discusses dystrophin and associated protein complex at astrocyte endfeet
  - [40]: Details structural anchoring at perivascular endfeet

**Atomic cellular components**
- Linear actin filament arrays and filopodia. Genes: FMN2, DAAM2
  - [56]: Describes formin-nucleated linear actin in filopodia formation
  - [57]: Details process filopodia in astrocyte dynamics
- Actin bundle networks. Genes: SHROOM3, LIMCH1, NEBL
  - [57]: Discusses SHROOM3-mediated actin bundle organization
- Microtubule cytoskeleton. Genes: MAP7
  - [56]: Details MAP7 role in microtubule organization
- Dystrophin-associated protein complex. Genes: DTNA
  - [9]: Describes DAP complex at astrocyte endfeet

**Required genes (not in input)**
- Genes: Rac1, RhoA, Cdc42 (Rho GTPases - effector targets), Cofilin (actin filament severing), Profilin (actin monomer sequestration), Arp2/3 complex (branched actin nucleation)
  - [56]: Discusses Rac1 activation by Trio as critical for branching
  - [57]: Mentions Rac1 downstream effects on actin dynamics

**Program citations**
- [56]: Comprehensive analysis of formin and Rho signaling in axon branching
- [57]: Detailed study of astrocyte process dynamics and Plexin-B1 regulation

## Program: Cell Adhesion and Extracellular Matrix Interactions
Astrocytes embedded within complex brain extracellular matrix maintain extensive cell-cell and cell-ECM contacts essential for tissue architecture and intercellular signaling. Protocadherin-9 (PCDH9) and cadherin-20 (CDH20) mediate cell-cell adhesion. Integrin ITGA6 binds laminin and other ECM ligands, transducing bidirectional signals governing astrocyte behavior. ADAMTS9 remodels ECM through proteolytic processing. ECM proteins expressed by astrocytes include SPARCL1 (SPARC-like protein 1), LAMA1 (laminin alpha-1), and COL4A5 (collagen type IV alpha-5 chain). The program maintains basement membrane integrity, supports glial scarring responses, and facilitates cell migration through coordinated adhesion modulation.

**Predicted impacts**
- Maintenance of tissue architecture through coordinated cell-cell and cell-ECM contacts
- Bidirectional signaling through integrin-ECM interactions governing cell behavior
- Selective ECM remodeling enabling cell migration while maintaining tissue integrity
- Basement membrane assembly and maintenance at blood-brain barrier
- Astrocyte reactivity-associated ECM changes supporting glial scar formation
- Enhanced ECM remodeling and reduced adhesion in invasive astrocytoma enabling tumor cell migration

**Evidence summary**
The cell adhesion program integrates cadherin-mediated cell-cell contacts (PCDH9, CDH20) with integrin-ECM interactions (ITGA6) and ECM protein production (LAMA1, COL4A5, SPARCL1). ADAMTS9 provides proteolytic ECM remodeling capacity. Recent spatial transcriptomic profiling of glioblastoma reveals substantial alterations in ECM composition compared to lower-grade tumors and normal brain, with differential expression of ECM genes in tumor versus stromal compartments suggesting coordinated remodeling programs during malignant transformation. In astrocytoma, dysregulation of this program through altered adhesion or proteolytic activity facilitates tumor cell invasion while simultaneously disrupting normal astrocyte-ECM interactions that support tissue homeostasis.

**Atomic biological processes**
- Cadherin-mediated cell-cell adhesion. Genes: PCDH9, CDH20, CHL1
  - [40]: Discusses cadherin roles in astrocyte cell-cell interactions
- Integrin-ECM ligand binding and signaling. Genes: ITGA6
  - [40]: Discusses integrin signaling in astrocyte adhesion
  - [46]: Details integrin signaling in pericyte-glioma interactions
- ECM proteolysis and remodeling. Genes: ADAMTS9, HPSE2
  - [6]: Comprehensive spatial transcriptomic analysis of ECM genes in GBM
- Basement membrane protein production. Genes: LAMA1, COL4A5, COL5A3
  - [6]: Discusses ECM protein expression in gliomas
  - [40]: Details basement membrane organization at BBB
  - [43]: Shows basement membrane assembly in 3D BBB models
- SPARC protein expression and ECM organization. Genes: SPARCL1
  - [6]: SPARC-like proteins in ECM remodeling and tumor biology

**Atomic cellular components**
- Cell-cell adhesion complexes. Genes: PCDH9, CDH20
  - [40]: Discusses cadherin and related adhesion protein complexes
- Integrin-focal adhesion complexes. Genes: ITGA6
  - [46]: Details focal adhesion dynamics in glioma cells
- Basement membrane protein networks. Genes: LAMA1, COL4A5, COL5A3, SPARCL1
  - [6]: Describes basement membrane composition and alterations in gliomas
  - [43]: Shows COL4 and related proteins in BBB basement membrane

**Required genes (not in input)**
- Genes: E-cadherin/CDH1 (additional cadherin in some astrocyte contexts), N-cadherin/CDH2 (cadherin in some astrocytes), Laminin beta chains (LAMB1, LAMB3), Nidogen (ECM cross-linking protein), Perlecan (heparan sulfate proteoglycan)
  - [6]: Lists additional ECM proteins altered in gliomas

**Program citations**
- [6]: Comprehensive spatial transcriptomic analysis of ECM in gliomas
- [40]: Discusses astrocyte adhesion and ECM interactions
- [46]: Details integrin signaling in tumor microenvironment

## Program: Gap Junction Communication and Astrocyte Network Integration
Astrocytes form extensive electrical and metabolic coupling networks through gap junction channels containing connexin-43 (encoded by GJA1), enabling synchronized responses to neuronal activity and coordinated regulation of the local microenvironment. GJA1 oligomerizes to form gap junctions permeable to ions and small molecules including ATP, glucose, and amino acids. Gap junction formation and stability are regulated through post-translational modification and transcriptional control. LRIG1 may provide regulatory input to gap junction function through its role in EGFR signaling modulation. The coupled network enables rapid astrocyte responses to heterogeneous inputs and supports metabolic coordination between neighboring cells.

**Predicted impacts**
- Coordinated astrocyte responses to neuronal activity through electrical coupling
- Metabolic support to neighboring astrocytes through ATP and metabolite sharing
- Synchronized calcium signaling across astrocyte networks
- Reduced gap junctional communication in reactive and tumor-associated astrocytes disrupting coordinated responses
- Enhanced tumor cell growth through altered paracrine signaling between tumor and normal astrocytes

**Evidence summary**
GJA1 represents the primary connexin in astrocyte gap junctions, forming channels permeable to ions and metabolites that enable astrocyte network integration. Gap junction function is dynamically regulated through post-translational modification and transcriptional control in response to signaling cascades. In reactive astrocytes and potentially in astrocytoma-associated astrocytes, gap junction expression and function are frequently altered, disrupting the coordinated astrocyte network responses essential for normal CNS homeostasis. LRIG1 may modulate this program through indirect effects on growth factor signaling. While specific studies of gap junction dysfunction in astrocytoma are limited, the known loss of gap junctional coupling in reactive glial states suggests this program is dysregulated during malignant transformation.

**Atomic biological processes**
- Connexin-43 gap junction channel assembly and regulation. Genes: GJA1
  - [40]: Discusses GJA1 regulation and dysfunction in disease
  - [62]: Describes GJA1 gap junction composition and function
- Small molecule and ion transfer through gap junctions. Genes: GJA1
  - [40]: Details metabolite transfer through astrocyte gap junctions
  - [62]: Describes gap junction permeability
- Gap junction regulation by kinase phosphorylation. Genes: GJA1
  - [62]: Discusses AKT-dependent GJA1 phosphorylation and internalization
  - [65]: Details mTOR inhibition of gap junction dynamics
- LRIG1-mediated growth factor signaling regulation. Genes: LRIG1
  - [40]: Discusses LRIG1 in astrocyte signaling

**Atomic cellular components**
- Gap junction channels and connexin-43 oligomers. Genes: GJA1
  - [62]: Describes connexin-43 hexamer and higher-order assembly

**Required genes (not in input)**
- Genes: Pannexins (alternative channel proteins), ZO-1 and other PDZ proteins (scaffolding of gap junctions), Src family kinases (phosphorylation of GJA1), PKC (protein kinase C, GJA1 regulation)
  - [40]: Discusses additional regulators of gap junction function

**Program citations**
- [40]: Comprehensive discussion of astrocyte gap junctions
- [62]: Detailed description of connexin-43 biology

## Program: Lipid Metabolism and Apolipoprotein-E Signaling
Astrocytes play central roles in lipid homeostasis and cholesterol delivery to neurons, with astrocyte-derived APOE being the predominant cholesterol carrier in the central nervous system. APOE is synthesized by astrocytes and transported in circulating CSF and parenchymal interstitium. Three common isoforms (ε2, ε3, ε4) differ structurally and influence lipid binding and receptor interactions, with ε4 conferring increased Alzheimer disease risk. LPL catalyzes hydrolysis of triglycerides in circulating lipoproteins. FADS2 enables synthesis of polyunsaturated fatty acids. OSBPL11 and OSBPL3 sense intracellular cholesterol levels and regulate transcriptional control of lipogenic programs. The program links metabolic state to transcriptional control through lipid-activated transcription factors.

**Predicted impacts**
- Maintenance of neuronal lipid homeostasis through APOE-mediated cholesterol delivery
- APOE ε4-associated potentiation of astrocyte-mediated neuroinflammation
- Flexible metabolic adaptation between oxidative phosphorylation and lipogenesis
- Sensing of metabolic state through oxysterol-binding protein interactions
- Enhanced lipid metabolism supporting tumor cell membrane biogenesis in astrocytoma
- Dysregulated APOE signaling contributing to tumor microenvironment remodeling

**Evidence summary**
APOE synthesis by astrocytes provides cholesterol delivery to neurons; the ε4 isoform associates with increased neuroinflammatory responses and Alzheimer disease risk. LPL enables local triglyceride processing. FADS2 supports polyunsaturated fatty acid synthesis critical for membrane composition and signaling. OSBPL11 and OSBPL3 function as lipid sensors regulating transcriptional programs in response to cholesterol availability. Recent evidence reveals that YAP1, through interaction with SREBP1, regulates astrocytic lipogenesis and potentially supports neuroprotection through metabolic adaptation. In astrocytoma, lipid metabolism dysregulation may support tumor cell proliferation through enhanced membrane biogenesis and altered metabolic support from tumor-associated astrocytes, while APOE ε4 status may influence the inflammatory microenvironment surrounding tumors.

**Atomic biological processes**
- Apolipoprotein E synthesis and CSF transport. Genes: APOE
  - [14]: Discusses APOE synthesis by astrocytes and ε4 effects on neuroinflammation
  - [16]: Reviews APOE roles in lipid metabolism and neurodegeneration
- Lipoprotein lipase-mediated triglyceride hydrolysis. Genes: LPL
  - [16]: Discusses LPL in lipid metabolism
  - [32]: Details LPL in astrocyte metabolism
- Polyunsaturated fatty acid synthesis. Genes: FADS2
  - [16]: Discusses FADS2 role in lipid synthesis
- Oxysterol sensing and lipid metabolism regulation. Genes: OSBPL11, OSBPL3
  - [16]: Discusses oxysterol-binding proteins in lipid homeostasis
- YAP1-SREBP1 lipogenesis regulation. Genes: YAP1
  - [24]: Details YAP control of lipid metabolism through SREBP1

**Atomic cellular components**
- Apolipoprotein E particles. Genes: APOE
  - [14]: Describes APOE particle composition and function
- Lipid droplets in astrocytes. Genes: APOE, LPL, OSBPL11, OSBPL3
  - [16]: Discusses astrocyte lipid droplets and their pathological accumulation

**Required genes (not in input)**
- Genes: SREBP2 (sterol regulatory element-binding protein 2), LDLR (low-density lipoprotein receptor), LRP1 (LDL receptor-related protein 1), PCSK9 (LDLR regulator), Apolipoprotein receptors (ApoER2, LDL-RP/LRP1)
  - [14]: Discusses APOE receptor interactions

**Program citations**
- [14]: Comprehensive discussion of APOE ε4 and astrocyte reactivity
- [16]: Reviews lipid metabolism and microglial lipid droplets with implications for astrocyte lipid handling
- [24]: Details YAP-SREBP1 lipogenesis pathway

## Program: Reactive Astrocyte Transformation and Neuroinflammation
In response to injury, infection, or disease, astrocytes undergo reactive transformation characterized by morphological changes, altered gene expression, and pro-inflammatory signaling. This program encompasses surface antigen upregulation (CD44, CD38), pattern recognition receptor signaling (TLR4), inhibition of differentiation (ID3, ID4), and transcriptional control of inflammatory responses (YAP1, RFX4). CD44 serves as a hyaluronic acid receptor upregulated on reactive astrocytes, facilitating immune cell interactions. CD38, a NAD-consuming enzyme, is upregulated in reactive glial cells and contributes to altered metabolic state. TLR4 recognizes pathogen-associated and damage-associated molecular patterns, driving NF-κB-dependent pro-inflammatory signaling. ID3 and ID4 promote proliferation while antagonizing differentiation. YAP1 simultaneously drives both inflammatory responses and metabolic adaptation.

**Predicted impacts**
- Transition from resting to activated morphological state with process retraction
- Upregulation of pro-inflammatory cytokine and chemokine expression
- Enhanced immune cell recruitment through CD44 hyaluronic acid interactions
- Altered energy metabolism through CD38-mediated NAD+ depletion
- Loss of neuronal support functions in favor of inflammatory responses
- Persistence of reactive phenotype in chronic disease states and astrocytoma
- Potential dual role in both anti-tumor immunity and tumor-promoting inflammation

**Evidence summary**
The reactive astrocyte program involves coordinated upregulation of CD44, CD38, and TLR4 alongside changes in transcriptional control through ID proteins and YAP1. Recent evidence from traumatic brain injury studies reveals that astrocyte reactivity persists for extended periods following injury, with distinct transcriptional signatures associated with different stages of the reactive response. CD44 upregulation facilitates immune cell recruitment, while CD38 NAD+ consumption alters metabolic state. ID3 and ID4 promote continued proliferation characteristic of reactive astrocytes. YAP1 simultaneously drives pro-inflammatory gene expression while supporting metabolic adaptation. In astrocytoma, the reactive astrocyte phenotype likely promotes tumor progression through reduced anti-tumor immune function and metabolic support of tumor cells, while the heterogeneity of reactive states within the tumor microenvironment may create distinct functional domains supporting different aspects of tumor biology.

**Atomic biological processes**
- Hyaluronic acid receptor-mediated immune cell interaction. Genes: CD44
  - [14]: Discusses CD44 upregulation in reactive astrocytes
- NAD+ metabolism and cellular energetics in reactive astrocytes. Genes: CD38
  - [8]: Describes CD38 function in NAD+ consuming reactions
  - [14]: Discusses CD38 upregulation in reactive glial cells
- Pattern recognition receptor signaling through TLR4. Genes: TLR4
  - [7]: Describes TLR4 signaling in immune responses
  - [14]: Discusses TLR4 roles in astrocyte reactivity
- Inhibitor of differentiation protein-mediated proliferation. Genes: ID3, ID4
  - [14]: Discusses ID3 and ID4 in reactive astrocytes
  - [28]: Details ID proteins in glioma stem cells
- YAP1-mediated transcriptional control of inflammatory responses. Genes: YAP1
  - [22]: Discusses YAP1 in reactive astrocyte regulation
  - [24]: Details YAP1 in neuroprotective versus neurotoxic astrocyte states
- RFX4-mediated transcriptional regulation. Genes: RFX4
  - [40]: Discusses transcriptional regulators in astrocyte states

**Required genes (not in input)**
- Genes: GFAP (astrocyte marker, downstream in reactive state), IL-6, TNF-α, IL-1β (pro-inflammatory cytokines), MCP-1/CCL2 (chemokine), iNOS (inducible nitric oxide synthase), MyD88 (TLR4 adaptor), STAT3, NF-κB (downstream of TLR4)
  - [21]: Discusses GFAP as marker and downstream inflammatory gene expression

**Program citations**
- [14]: Comprehensive analysis of astrocyte reactivity markers and APOE effects
- [21]: Details persistent astrocyte activation after TBI

## Program: Calcium Signaling and Metabolic Adaptation
Intracellular calcium serves as a critical second messenger regulating astrocyte metabolic state, gene expression, and synaptic interactions through multiple interconnected calcium-handling systems. ITPR2 gates inositol 1,4,5-trisphosphate-mediated calcium release from ER stores in response to phospholipase C activation downstream of growth factor and neurotransmitter receptors. CACNA2D3 encodes an auxiliary subunit of L-type calcium channels regulating calcium influx. Downstream calcium-responsive effectors including calcineurin and calmodulin-dependent kinases integrate calcium signals with metabolic and transcriptional responses. Recent evidence reveals bidirectional calcium-mitochondrial interactions, with excessive ITPR2-mediated calcium transfer to mitochondria promoting mitochondrial dysfunction and contributing to senescence and neuroinflammation.

**Predicted impacts**
- Coupling of neuronal activity sensing to metabolic adaptation
- Astrocyte lactate production in response to elevated calcium/glutamate uptake
- Calcium-dependent transcriptional control of pro-inflammatory genes
- Mitochondrial calcium overload promoting ROS production and senescence
- Dysregulated calcium signaling in reactive astrocytes contributing to chronic neuroinflammation
- Altered calcium dynamics in astrocytoma supporting metabolic flexibility and tumor cell survival

**Evidence summary**
ITPR2 represents a central calcium-handling component linking growth factor signaling to intracellular calcium dynamics and mitochondrial metabolism. Excessive ITPR2-mediated calcium transfer to mitochondria through ER-mitochondrial contact sites (MERCS) causes mitochondrial calcium accumulation, reduces mitochondrial membrane potential, and elevates ROS production, creating a positive feedback loop promoting senescence and chronic neuroinflammatory states. CACNA2D3 provides auxiliary regulation of L-type calcium channel function. In reactive astrocytes and astrocytoma-associated astrocytes, dysregulated calcium signaling may simultaneously promote pro-inflammatory gene expression while disrupting optimal metabolic function, contributing to both anti-tumor and pro-tumor effects depending on specific context. Evidence that ITPR2 knockdown prevents senescence induction suggests therapeutic potential for modulating this program.

**Atomic biological processes**
- IP3-mediated ER calcium release. Genes: ITPR2
  - [22]: Details ITPR2 function in ammonia-induced metabolic changes
  - [35]: Comprehensive discussion of ITPR2 in calcium handling and senescence
  - [40]: Discusses IP3 signaling in astrocyte calcium dynamics
- Voltage-gated calcium channel regulation. Genes: CACNA2D3
  - [32]: Discusses calcium channels in astrocyte excitability
- Calcineurin-NFAT signaling and calcium-dependent gene expression.
  - [40]: Details calcineurin-NFAT pathway in astrocyte reactivity and neurovascular coupling
- Mitochondrial calcium uptake and oxidative phosphorylation coupling. Genes: ITPR2
  - [35]: Details mitochondrial calcium uniporter function and ROS production
  - [64]: Comprehensive review of mitochondrial calcium in senescence
- Mitochondrial permeability transition and apoptosis.
  - [35]: Discusses mPTP calcium-dependent opening
  - [64]: Details mPTP flickering in senescent cells

**Atomic cellular components**
- IP3 receptor calcium-release channel. Genes: ITPR2
  - [35]: Describes ITPR structure and function
- Voltage-gated L-type calcium channels. Genes: CACNA2D3
  - [32]: Discusses calcium channel subunits
- ER-mitochondria contact sites (MERCS). Genes: ITPR2
  - [35]: Describes MERCS structure and calcium transfer
  - [64]: Details MERCS in senescence

**Required genes (not in input)**
- Genes: PLCB (phospholipase C beta, IP3 generation), MCU (mitochondrial calcium uniporter), NCLX (mitochondrial sodium-calcium exchanger), Calcineurin (calcium-dependent phosphatase), CaMKII (calcium-calmodulin kinase)
  - [40]: Lists calcium-dependent effectors
  - [35]: Discusses mitochondrial calcium transporters

**Program citations**
- [35]: Comprehensive review of mitochondrial dysfunction and ITPR2 calcium signaling
- [40]: Discusses astrocyte calcium signaling in neurovascular coupling
- [64]: Reviews calcium handling in cellular senescence

## Program: Transcriptional Control of Differentiation and Stem Cell Maintenance
The genes ID3, ID4, YAP1, RFX4, and ZNF521 collectively regulate transcriptional programs governing cell proliferation, differentiation state, and maintenance of stem/progenitor cell characteristics. ID proteins function as dominant-negative inhibitors of basic helix-loop-helix transcription factors critical for differentiation; their upregulation maintains proliferative potential while antagonizing terminal differentiation. YAP1 acts as a master regulator of stem cell properties and metabolic flexibility through interaction with TEAD transcription factors and modulation of HIPPO pathway signaling. RFX4 plays roles in neuronal and glial lineage specification. ZNF521 supports stem cell maintenance. This program directly enables the cellular plasticity characteristic of astrocytoma, wherein tumor cells maintain progenitor-like transcriptional states despite expressing some differentiation markers.

**Predicted impacts**
- Maintenance of proliferative potential in progenitor-like astrocytes
- Antagonism of terminal differentiation through ID protein-mediated bHLH inhibition
- YAP1-driven metabolic reprogramming supporting stemness
- Preservation of plasticity enabling lineage transitions in response to microenvironmental signals
- Enhanced tumor cell survival and self-renewal in astrocytoma through sustained stemness
- Resistance to differentiation-based therapies through ID and YAP1 overexpression

**Evidence summary**
Recent glioblastoma studies reveal that tumor progression involves activation of an INSM1-driven intermediate progenitor state, with maintained plasticity enabling transitions between different molecular subtypes. ID proteins antagonize bHLH differentiation factors, maintaining proliferative capacity while reducing differentiation pressure. YAP1 functions as a master regulator of stemness through TEAD interaction, simultaneously promoting metabolic flexibility and survival signaling. The presence of multiple stemness-regulating transcription factors (ID3, ID4, YAP1, RFX4, ZNF521) in the input list suggests that astrocytoma cells maintain access to developmental transcriptional programs normally restricting stemness, enabling the cellular plasticity observed in these tumors. Evidence that YAP1 can simultaneously support neuroprotective functions while driving stemness and metabolic flexibility suggests context-dependent program regulation in tumor versus normal tissue.

**Atomic biological processes**
- bHLH transcription factor antagonism by ID proteins. Genes: ID3, ID4
  - [14]: Discusses ID protein function in reactive astrocytes
  - [28]: Details ID proteins in glioma stem cell maintenance
- YAP1-TEAD transcriptional regulation. Genes: YAP1
  - [22]: Discusses YAP1-TEAD complex in astrocyte gene regulation
  - [24]: Details YAP1 transcriptional targets and neuroprotective effects
- Hippo pathway signaling and YAP1 activation. Genes: YAP1
  - [22]: Details Hippo-YAP pathway regulation of glutamine synthetase
  - [24]: Comprehensive discussion of Hippo-YAP signaling in development and disease
- RFX4-mediated transcriptional regulation of neuronal/glial programs. Genes: RFX4
  - [40]: Mentions RFX4 in transcriptional control
- ZNF521-mediated stem cell maintenance. Genes: ZNF521
  - [40]: Discusses ZNF521 in stem cell regulation

**Required genes (not in input)**
- Genes: TEAD1-4 (TEA domain transcription factors, YAP1 partners), SOX2 (master stem cell regulator), NOTCH1 (developmental signaling), WNT pathway components (β-catenin, TCF/LEF), INSM1 (intermediate progenitor state driver in glioma)
  - [28]: Discusses SOX2 and INSM1 in glioma stem cell biology
  - [24]: Mentions TEAD as YAP1 partner

**Program citations**
- [28]: Details INSM1-driven progenitor state in glioblastoma
- [24]: Comprehensive discussion of YAP1 in development and disease

## Program: Mitochondrial Quality Control and Senescence Prevention
Astrocytes maintain mitochondrial health through quality control mechanisms including selective autophagy (mitophagy) and degradation of damaged organelles. FKBP5, encoding an immunophilin involved in protein folding and stress responses, contributes to cellular stress adaptation. YAP1, while discussed primarily in other contexts, also prevents premature senescence of astrocytes through regulation of CDK6 signaling and metabolic adaptation. Dysregulation of this program occurs through impaired mitophagy, accumulation of dysfunctional mitochondria with elevated ROS production, and persistent DNA damage responses characteristic of cellular senescence. Senescent astrocytes produce pro-inflammatory SASP factors that paradoxically may either oppose or support tumor progression depending on context.

**Predicted impacts**
- Maintenance of healthy mitochondrial population through selective autophagy
- Prevention of ROS accumulation and oxidative damage
- Reduced persistent DNA damage responses and senescence
- Preserved astrocyte metabolic flexibility and support functions
- Reduced SASP-mediated chronic neuroinflammation
- Accumulation of senescent astrocytes in aging brain and chronic disease states contributing to neuroinflammation
- Complex effects of SASP factors in astrocytoma potentially both limiting and promoting tumor progression

**Evidence summary**
Mitochondrial quality control represents a critical determinant of astrocyte health, with impaired mitophagy leading to accumulation of dysfunctional organelles, ROS accumulation, and senescence induction. FKBP5 contributes to cellular stress responses and protein folding capacity in response to physiological stress including HPA axis activation. YAP1 actively prevents senescence through CDK6 signaling and metabolic adaptation. In aging brain and chronic neurodegenerative disease, accumulated senescent astrocytes display impaired mitochondrial quality control, producing pro-inflammatory SASP factors that chronically activate local immune cells. In astrocytoma, senescent cell-derived SASP may create a pro-inflammatory microenvironment potentially supporting immune suppression and tumor progression, while in other contexts may limit tumor development. The importance of this program is underscored by recent findings that therapeutic targeting of senescent cells (senolytics) improves age-related cognitive decline.

**Atomic biological processes**
- Mitochondrial selective autophagy (mitophagy).
  - [35]: Comprehensive discussion of PINK1/Parkin-mediated mitophagy
  - [64]: Details S-nitrosylation of Parkin and mitophagy impairment in senescence
- FKBP5-mediated protein folding and stress response. Genes: FKBP5
  - [15]: Details FKBP5 in HPA axis signaling and stress responses
- YAP1-mediated senescence prevention. Genes: YAP1
  - [24]: Describes YAP1 prevention of astrocyte senescence through CDK6
- ROS-mediated DNA damage and persistent DDR.
  - [35]: Details ROS generation and ATM-AKT-mTORC1 signaling cascade
  - [64]: Comprehensive discussion of oxidative stress and senescence
- Senescence-associated secretory phenotype (SASP) production.
  - [35]: Details SASP factors and their production mechanisms
  - [64]: Discusses inflammatory cytokine production by senescent cells

**Atomic cellular components**
- Dysfunctional mitochondria accumulation.
  - [35]: Describes mitochondrial morphological changes and quality loss
  - [64]: Details increased mitochondrial mass in senescent cells

**Required genes (not in input)**
- Genes: PINK1 (mitophagy receptor), Parkin (E3 ubiquitin ligase for mitophagy), p62 (autophagy adaptor), ATM (DNA damage sensor), p53 (senescence inducer), p16, p21 (CDK inhibitors in senescence), mTORC1 (nutrient and energy sensor)
  - [35]: Lists mitophagy and senescence pathway components
  - [64]: Comprehensive pathway listing for mitochondrial dysfunction and senescence

**Program citations**
- [35]: Comprehensive review of mitochondrial dysfunction in senescence
- [64]: Detailed discussion of mitochondrial quality control and senescence

## Program: Growth Factor Signaling and Metabolic Adaptation
Astrocytes respond to multiple growth factor signaling cascades that drive proliferation, survival, and metabolic adaptation. NTRK2 (TrkB) responds to brain-derived neurotrophic factor (BDNF) activation, engaging PI3K-AKT and MAPK signaling cascades. NRG3 (neuregulin-3) signals through ErbB receptor family members including ERBB4. ADCY2 and ADCY8 encode adenylyl cyclases generating cAMP second messengers downstream of Gαs-coupled receptors. ADRA1A encodes alpha-1A adrenergic receptor signaling to phospholipase C and calcium mobilization. PRKG1 encodes protein kinase G activated by cGMP in response to nitric oxide signaling. These pathways collectively integrate growth factor, neurotransmitter, and vasoactive signals to coordinate astrocyte metabolic state with microenvironmental demands.

**Predicted impacts**
- Astrocyte survival and proliferation in response to BDNF-TrkB signaling
- NTRK2 fusion-driven constitutive activation in subset of pediatric astrocytomas
- Metabolic adaptation to growth signals through MAPK and PI3K pathway activation
- cAMP-mediated responses to catecholamine and other Gαs signals
- Integration of multiple growth factor inputs enabling flexible metabolic responses
- Enhanced tumor cell growth through NTRK2 fusion-mediated signaling in specific molecular subtypes
- Vulnerability to targeted kinase inhibitors in NTRK-driven astrocytomas

**Evidence summary**
NTRK2 represents a critical survival and proliferation signal for astrocytes under normal conditions, but becomes pathogenic when constitutively activated through fusion events in certain pediatric astrocytomas. Recent evidence demonstrates that TRIM24::NTRK2 fusion proteins drive oncogenic signaling through both PI3K-AKT and MAPK-ERK pathways, with particularly strong activation of S6 kinase suggesting mTORC1 engagement. NRG3-ERBB4 signaling provides complementary developmental signals. Multiple adenylyl cyclase isoforms (ADCY2, ADCY8) generate cAMP in response to diverse upstream signals including β-adrenergic receptors and other Gαs-coupled receptors, enabling broad metabolic adaptation. ADRA1A signaling through alpha-1A receptors mobilizes calcium and activates phospholipase C. PRKG1 integration of nitric oxide signaling connects astrocyte function to vascular signals. In astrocytoma, dysregulation of this program through NTRK fusion proteins drives constitutive proliferation signals, while enhanced sensitivity to metabolic stress from adenylyl cyclase signaling dysregulation may create therapeutic vulnerabilities.

**Atomic biological processes**
- BDNF-TrkB-PI3K-AKT signaling for survival. Genes: NTRK2
  - [21]: Details NTRK2 downregulation acutely after TBI but upregulation in chronic phase
  - [26]: Describes TRIM24::NTRK2 fusion-driven signaling in astrocytoma
- BDNF-TrkB-MAPK signaling for proliferation. Genes: NTRK2
  - [26]: Details pERK activation through NTRK2 signaling
- Neuregulin-ErbB signaling in astrocyte development. Genes: NRG3, ERBB4
  - [13]: Describes NRG1 and ErbB signaling in nervous system development
  - [26]: Discusses NRG3 in astrocyte signaling
- Adenylyl cyclase-cAMP signaling downstream of Gαs receptors. Genes: ADCY2, ADCY8
  - [14]: Discusses cAMP signaling in astrocyte responses
- α1-adrenergic receptor signaling to PLC and calcium mobilization. Genes: ADRA1A
  - [40]: Discusses noradrenergic signaling in astrocyte responses
- Nitric oxide-cGMP-PKG signaling. Genes: PRKG1
  - [40]: Details nitric oxide and cGMP signaling in neurovascular coupling

**Required genes (not in input)**
- Genes: BDNF (NTRK2 ligand), NRG1 (ErbB ligand), PI3K, AKT (NTRK2 downstream effectors), MAPK/ERK cascade (NTRK2 downstream), mTORC1 (downstream of AKT), β-adrenergic receptors (ADCY activators), Gαs/Golf (ADCY activators)
  - [26]: Lists signaling pathways downstream of NTRK2

**Program citations**
- [26]: Comprehensive analysis of NTRK2 fusion in astrocytoma
- [21]: Details NTRK2 roles in astrocyte response to injury

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
2. 2. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
3. 3. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/23627
5. 5. Breen KE, Mehta N, Ravichandran V, Mehine M, Gao C, Fiala E, et al.. Paired tumor-normal sequencing provides insights into the CDKN2A-associated tumor spectrum. npj Precision Oncology [Internet]. 2025Nov19;9(1). Available from: https://www.nature.com/articles/s41698-025-01155-6
6. 6. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/21898
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/12494
9. 9. González-Gallego J, Todorov-Völgyi K, Müller SA, Antesberger S, Todorov MI, Malik R, et al.. A fully iPS-cell-derived 3D model of the human blood–brain barrier for exploring neurovascular disease mechanisms and therapeutic interventions. Nature Neuroscience [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41593-025-02123-w
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/6507
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/20655
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/20512
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
14. 14. Trudel L, Therriault J, Macedo AC, Woo MS, Rahmouni N, Aumont É, et al.. APOE ε4 potentiates tau related reactive astrogliosis assessed by cerebrospinal fluid YKL40 in Alzheimer’s disease. Communications Medicine [Internet]. 2025Nov20;5(1). Available from: https://www.nature.com/articles/s43856-025-01171-4
15. 15. Yusuf AM, Ilce BY, Alhaj HA, Hamoudi R. α-synuclein in Parkinson’s disease: a central point of convergence with depression. npj Parkinson's Disease [Internet]. 2025Nov20;11(1). Available from: https://www.nature.com/articles/s41531-025-01167-w
16. 16. Sung S, Kim H-J, Cha SJ, Nahm M, Kim SH, Kwon M-S. Microglial lipid droplets as therapeutic targets in age-related neurodegenerative diseases. npj Aging [Internet]. 2025Nov30;. Available from: https://www.nature.com/articles/s41514-025-00295-0
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/11835
18. 18. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
19. 19. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/18018
21. 21. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
22. 22. Nasu Y, Kishikawa S, Imai M, Yokoyama N, Iida I, Tabeta K, et al.. Ammonia reduces glutamine synthetase expression in astrocytes via activation of Hippo-YAP signaling pathways. Communications Biology [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s42003-025-09191-5
23. 23. Ghirardello M, Yruela I, Merino P, Sackstein R, Sanz-Martínez I, Hurtado-Guerrero R. Structure, function, and implications of fucosyltransferases in health and disease. Nature Communications [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41467-025-66871-w_reference.pdf
24. 24. Jiaojiao W, Chunfang D, Hao Y, Qiuyun T, Qian X, Xiaohuan L, et al.. The YAP/SCAP/SREBP1 Pathway in Astrocytes: A Novel Target for Treating Neonatal Hypoxic-Ischemic Encephalopathy.. Progress in neurobiology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41390137/?fc=None&ff=20251214151330&v=2.18.0.post22+67771e2
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/4323
26. 26. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
28. 28. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
29. 29. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/546
32. 32. Zhang Y, Savvidou M, Liaudanskaya V, Ramanathan V, Bui T, Lindley M, et al.. Multi-modal label-free imaging of cellular metabolism and oxidative stress in 3D brain tissue models. Communications Biology [Internet]. 2025Dec2;8(1). Available from: https://www.nature.com/articles/s42003-025-09122-4
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/4137
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/8678
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/5894
37. 37. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
38. 38. Gkogka A, Malwade S, Koskuvi M, Ohtonen S, Molnar E, Bose R, et al.. Human oligodendrocyte progenitor cells mediate synapse elimination through TAM receptor activation. Nature Communications [Internet]. 2025Dec5;16(1). Available from: https://www.nature.com/articles/s41467-025-66521-1
39. 39. Sims SL, Lu T-H, Weiss BE, Lin R-L, Galopin LB, Wright NA, et al.. Central cytometabolic functional vascular coupling in health and disease. npj Metabolic Health and Disease [Internet]. 2025Dec2;3(1). Available from: https://www.nature.com/articles/s44324-025-00090-1
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/998
41. 41. Martín-Monteagudo C, Sánchez RJ, Adams JM, Puente N, Grandes P, Marsicano G, et al.. An astrocytic ensemble at vHip-NAc synapses modulates cognitive impairments induced by chronic tetrahydrocannabinol exposure. Nature Communications [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s41467-025-67166-w_reference.pdf
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/3399
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/19016
44. 44. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/57591
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/19013
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/207
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
49. 49. Jiang R, Lu Z, Li F, Zhu Y, Yang M, Zhang S, et al.. scCirclehunter delineates ecDNA-containing cells using single-cell ATAC-seq, with a focus on glioblastoma. Cell Discovery [Internet]. 2025Dec9;11(1). Available from: https://www.nature.com/articles/s41421-025-00842-9
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/1385
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/7076
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
53. 53. Fingleton E, Lombardo A, Won S, Chang K, Li Y, Roche KW. Trio and CRMP2 regulate axon branching and Semaphorin3A signaling. Communications Biology [Internet]. 2025Nov25;8(1). Available from: https://www.nature.com/articles/s42003-025-08988-8
54. 54. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
55. 55. Liu T-T, Li H-Y, Gu S-Y, Sun L, Zhang R-W, Zu J-L, et al.. NMDA receptors coordinate brain vascular development via neuron-to-endothelial tip cell crosstalk in zebrafish. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-66543-9
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/13649
57. 57. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
58. 58. David KS, Erin MS, Maeve LS, Maria CV, Sandra M. Differential regulation of p62-ubiquitin conjugates in neurons versus astrocytes during cellular stress.. bioRxiv : the preprint server for biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41332782/
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/56717
60. 60. Sun Y, Liu S, Chen L, Zhou Z, Yin X, Shi Y, et al.. AI-driven discovery of dual antiaging and anti-AD therapeutics via PROTAC target deconvolution of a super-enhancer–regulated axis. Science Advances [Internet]. 2025Nov21;11(47). Available from: https://www.science.org/doi/10.1126/sciadv.adz9283
61. 61. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
62. 62. Available from: http://json-schema.org/draft-07/schema#",
