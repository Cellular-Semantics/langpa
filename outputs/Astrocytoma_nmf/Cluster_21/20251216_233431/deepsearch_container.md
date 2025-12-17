# Gene Program Markdown Report

## Context
- Cell type: astrocyte
- Disease: astrocytoma
- Tissue: brain

## Input Genes
THSD4, STK17B, ADAMTS6, AGMO, AKAP6, IQSEC2, OPHN1, AL355306.2, HEPACAM, KIAA1211, GHR, PLCB1, NHSL1, PARD3B, FMNL3, PARD3, CSGALNACT1, CTDSPL, SLC8A1, RIDA, SNX7, EPHB1, AL589740.1, HIF3A, AKAP13, ... (200 total)

## Program: Glutamate Homeostasis and Excitatory Signaling
Astrocyte-mediated clearance of synaptic glutamate and regulation of extracellular glutamate concentration through high-affinity transporters, coupled with calcium-dependent signaling and ion channel activity that modulates astrocytic physiology and indirectly affects synaptic glutamate handling. This program is critical for protecting neurons from excitotoxicity and maintaining appropriate synaptic transmission strength. Dysregulation of glutamate homeostasis in astrocytoma leads to elevated extracellular glutamate, altered neuronal excitability, and tumor-associated seizures.

**Predicted impacts**
- Impaired glutamate clearance from synaptic cleft and extracellular space
- Elevated extracellular glutamate concentration promoting neuronal excitotoxicity
- Dysregulation of astrocytic calcium signaling impairing astrocyte-neuron communication
- Enhanced neuronal excitability and increased seizure susceptibility in peritumoral cortex
- Loss of astrocytic neuroprotective function

**Evidence summary**
Five genes directly involved in glutamate uptake, ion channel activity, and calcium signaling are present in the input list. In acute phase TBI astrocytes, SLC1A3 and other glutamate handling genes are downregulated, impairing glutamate clearance[1][12]. In gliomas, impaired glutamate reuptake by transformed astrocytes creates a permissive environment for tumor-associated seizures through elevation of extracellular glutamate and altered neuronal excitability[4][32]. The presence of both glutamate transporters (SLC1A3, SLC1A2) and calcium-modulating ion channels (CACNB2, TRPC4, TPCN1, KCNQ5) suggests coordinated dysregulation of glutamate homeostasis and calcium signaling in astrocytoma.

**Atomic biological processes**
- glutamate uptake and reuptake. Genes: SLC1A3, SLC1A2
  - [1]: Differential gene expression analysis revealed significant downregulation of SLC1A3 in acute TBI astrocytes, impairing glutamate termination
  - [8]: SLC1A3 encodes high-affinity glutamate transporter terminating excitatory neurotransmission
  - [10]: SLC1A3 contributes to glutamate homeostasis by regulating astrocytic GLAST expression
- sodium-calcium exchange and ion homeostasis. Genes: SLC8A1, ATP2B2
  - [8]: SLC8A1 sodium-calcium exchanger regulates intracellular calcium dynamics relevant to astrocyte physiology
- calcium signaling and cellular excitability. Genes: CACNB2, TPCN1, TRPC4, KCNQ5, KCNH7, KCNT2
  - [26]: TRPC4 is implicated in regulation of calcium homeostasis in astrocytes
  - [4]: Glioma cells impair local glutamate reuptake through alterations in astrocytic function affecting calcium-dependent processes

**Atomic cellular components**
- plasma membrane glutamate transporters. Genes: SLC1A3, SLC1A2
  - [8]: SLC1A3 encodes high-affinity glutamate transporter
- voltage-gated ion channels. Genes: CACNB2, KCNQ5, KCNH7, KCNT2, KCNIP1
  - [26]: Ion channels regulate astrocytic membrane potential and excitability
- calcium-regulated cellular compartments. Genes: TPCN1, TRPC4, ATP2B2
  - [26]: TRPC4 involved in astrocytic calcium signaling compartments

**Program citations**
- [1]: Comprehensive RNA-seq of astrocytes shows downregulation of Slc1a3 and ion channel genes in reactive astrocytes
- [4]: Glioma cells impair glutamate reuptake and elevate extracellular glutamate through xCT transporter systems and by impairing astrocytic glutamate reuptake
- [12]: Temporal analysis confirms downregulation of SLC1A3 (Slc1a3) and ion channel regulation genes in acute phase astrocytes
- [32]: Neurons in peritumoral cortex of glioma patients form synapses with tumor cells and show altered excitatory properties

## Program: Extracellular Matrix Remodeling and Cell Adhesion
Coordinated synthesis, modification, and degradation of extracellular matrix components that remodel the tumor microenvironment and regulate cell-cell and cell-matrix interactions. This program includes cadherin-mediated adhesion, integrin interactions with ECM proteins, and proteolytic remodeling of matrix by metalloproteinases. Dysregulation of this program promotes astrocytoma cell migration, invasion, and resistance to cell-cell adhesion constraints, while simultaneously altering the biochemical and mechanical properties of the tumor microenvironment.

**Predicted impacts**
- Enhanced cell migration and invasion capacity through ECM remodeling
- Loss of tissue architectural constraints through reduced cell-cell adhesion
- Altered mechanical properties of tumor microenvironment affecting mechanotransduction
- Enhanced protease activity degrading basement membranes
- Increased dissemination and infiltration into adjacent neural tissue

**Evidence summary**
Multiple ECM and adhesion genes are present in the input list, coordinating to remodel the tumor microenvironment. Single-cell spatial profiling of glioblastoma demonstrates that ECM signaling pathways are profoundly dysregulated with unique expression profiles in different tumor cell populations[2][29]. The downregulation of classical adhesion molecules like cadherins, combined with upregulation of proteolytic enzymes like ADAMTS family members, creates a permissive environment for tumor cell migration and invasion. The presence of both pro-adhesive molecules (cadherins) and anti-adhesive signals (through protease activity) suggests dynamic control of adhesion appropriate for an invasive tumor phenotype.

**Atomic biological processes**
- cell-cell adhesion through cadherins. Genes: CDH20, CDH11, CDH18, PCDH11X
  - [1]: Downregulation of genes associated with cell junction assembly and adhesion including Cdh19 in acute TBI astrocytes
  - [2]: Single-cell spatial profiling identifies unique ECM expression profiles in glioblastoma including altered cadherin expression
- ECM protein synthesis and organization. Genes: LAMA2, SPOCK1, SPARCL1, P4HA1
  - [2]: ECM signaling pathways are dysregulated in brain pathologies including glioblastoma with profoundly altered expression signatures
- matrix metalloproteinase activity and ECM remodeling. Genes: ADAMTS6
  - [22]: ADAMTS1 metalloprotease decreases cell migration and invasion by modulating matrix dynamics
- integrin signaling and focal adhesion assembly. Genes: FAT3, ANKFN1, CLIP1
  - [44]: Focal adhesions undergo protein complex assembly regulated by integrin-ECM interactions and mechanical tension
  - [18]: Focal adhesion proteins show liquid-liquid phase separation on lipid membranes

**Atomic cellular components**
- cell surface adhesion molecules. Genes: CDH20, CDH11, CDH18, PCDH11X, HEPACAM, FAT3
  - [1]: Cell junction assembly genes downregulated in reactive astrocytes
- secreted extracellular matrix proteins. Genes: LAMA2, SPOCK1, SPARCL1, P4HA1, TTN
  - [2]: ECM components show unique expression profiles across GBM cell populations and spatial regions
- cell polarity and adhesion scaffolds. Genes: PARD3, PARD3B
  - [20]: PARD3 and related proteins organize cell polarity and epithelial architecture

**Program citations**
- [1]: Differential downregulation of cell junction and adhesion genes in reactive astrocytes
- [2]: Single-cell spatial transcriptomics reveals dysregulated ECM signaling in glioblastoma
- [29]: ECM ligand-receptor networks between GBM cells and stromal cells show profound dysregulation

## Program: Synaptic Plasticity and Synapse Pruning
Astrocyte-mediated regulation of synaptic structure, function, and elimination through expression of synaptogenic factors, complement components, and phagocytic receptors. This program includes maintenance of existing synapses through adhesion molecules and growth factors, as well as active elimination of synaptic material through complement-dependent and phagocytosis-dependent pathways. In astrocytoma, dysregulation of this program leads to inappropriate synapse pruning in the peritumoral cortex, loss of synaptic connectivity, and contribution to seizure susceptibility and neuronal dysfunction.

**Predicted impacts**
- Inappropriate elimination of synaptic material in peritumoral cortex
- Loss of functional synaptic connectivity
- Reduced synaptic density around tumor
- Enhanced seizure susceptibility through loss of inhibitory synapses
- Contribution to peritumoral neuronal dysfunction and cognitive decline

**Evidence summary**
Six genes directly participating in synaptic plasticity and pruning are present in the input list. MERTK, a key mediator of synapse pruning, is upregulated in reactive astrocytes both after TBI and in chronic neurodegeneration[1][23]. The presence of both synaptogenic factors (NRXN1, SPON1, C1QL1) and pruning-promoting genes (MERTK) suggests a dysregulated balance favoring pathological synapse elimination in astrocytoma. The documented aberrant neural activity in the peritumoral cortex with enhanced seizure susceptibility is consistent with inappropriate loss of inhibitory synaptic connections through overactive pruning mechanisms.

**Atomic biological processes**
- synapse formation and stabilization. Genes: NRXN1, LSAMP, LRRC4C, C1QL1, SPON1, SPOCK1
  - [1]: Upregulation of genes involved in synaptic structure regulation and neuronal stem cell maintenance in subacute phase
- synapse pruning and phagocytosis. Genes: MERTK, NEDD4
  - [1]: MERTK expression is upregulated in reactive astrocytes and mediates complement-dependent synapse pruning
  - [23]: MERTK, along with C1q components, mediates synapse pruning in reactive astrocytes during neurodegeneration
- protein ubiquitination in synaptic remodeling. Genes: NEDD4, TRIM9
  - [1]: E3 ubiquitin ligases participate in synaptic protein clearance and autophagy-mediated pathways

**Atomic cellular components**
- synaptic adhesion molecules. Genes: NRXN1, LSAMP, C1QL1, SPON1
  - [1]: Synaptic adhesion genes involved in synapse maintenance and stabilization
- phagocytic receptor machinery. Genes: MERTK
  - [23]: MERTK mediates phagocytosis in astrocytes for synapse pruning

**Program citations**
- [1]: MERTK and synapse-related genes upregulated in acute and subacute phase astrocytes
- [4]: Neurons in peritumoral cortex show altered synaptic properties and electrophysiological dysfunction
- [23]: MERTK mediates synapse pruning through complement-dependent mechanisms in reactive astrocytes
- [32]: Peritumoral neurons show transcriptomic alterations affecting synaptic transmission and plasticity

## Program: Growth Factor Signaling and Developmental Programs
Activation of growth factor receptor signaling pathways and reactivation of developmental transcription factors that maintain neural progenitor identity and proliferation while blocking terminal differentiation. This program includes receptor tyrosine kinases (FGFR2, IGF1R) that activate PI3K-Akt and MAPK cascades, downstream transcription factors (HES1, HES4, ID4) that regulate progenitor versus differentiation fate, and secreted ligands and modulators (PAPPA, FRY) that affect growth factor bioavailability and signaling dynamics. In astrocytoma, continuous activation of these programs maintains tumor cells in a proliferative, progenitor-like state resistant to differentiation.

**Predicted impacts**
- Enhanced cell proliferation through sustained growth factor signaling
- Maintenance of progenitor-like state resistant to terminal differentiation
- Reduced dependence on specific ligand availability through coordinated pathway activation
- Enhanced expression of self-renewal genes and suppression of differentiation genes
- Increased metabolic demand to support rapid proliferation

**Evidence summary**
Multiple components of growth factor signaling and developmental transcriptional control are present in the input list. FGFR2 is specifically upregulated in chronic phase astrocytes[1], and IGF1R is a canonical growth-promoting receptor with enhanced signaling in cancer. The presence of both receptor-level signaling (FGFR2, IGF1R) and downstream transcriptional regulation (HES1, HES4, ID4, NPAS3) suggests coordinated maintenance of a progenitor program that resists differentiation. Studies of glioblastoma development demonstrate that canonical mutations promote functional plasticity through reactivation of developmental programs[3][28], with INSM1-driven neuronal progenitor networks driving tumor evolution. The presence of multiple components of this developmental program in the input list suggests that astrocytoma maintains active developmental signaling.

**Atomic biological processes**
- fibroblast growth factor receptor signaling. Genes: FGFR2, PAPPA
  - [1]: Fgfr2 expression significantly upregulated in chronic phase astrocytes in neuron-astrocyte interactions
  - [33]: FGFR signaling gradients establish developmental patterns in neural tube formation
- insulin-like growth factor signaling. Genes: IGF1R, PAPPA
  - [9]: IGF1R binds insulin-like growth factor with high affinity and has tyrosine kinase activity promoting cell survival and proliferation
- progenitor maintenance and differentiation control. Genes: HES1, HES4, ID4, NPAS3
  - [3]: Canonical glioblastoma mutations promote functional plasticity through transitions toward a neuronal progenitor network
  - [28]: INSM1-driven transcriptional programs regulate proliferation-differentiation balance in developing brain

**Atomic cellular components**
- receptor tyrosine kinases. Genes: FGFR2, IGF1R
  - [9]: IGF1R and similar RTKs transduce growth signals through receptor-mediated tyrosine kinase activation
- basic helix-loop-helix transcription factors. Genes: HES1, HES4, ID4
  - [3]: Transcriptional programs regulated by developmental factors control progenitor state and differentiation

**Program citations**
- [1]: Fgfr2 upregulated in chronic phase astrocytes in association with neuron-astrocyte interactions
- [3]: Canonical glioblastoma mutations promote functional plasticity through developmental program transitions
- [28]: INSM1 governs neuronal progenitor state driving glioblastoma evolution
- [33]: Growth factor signaling establishes developmental gradients critical for neural development

## Program: Metabolic Reprogramming and Energy Adaptation
Coordinated upregulation of metabolic genes that support rapid proliferation and survival in nutrient-limited tumor microenvironment through enhanced glucose utilization, one-carbon metabolism, and antioxidant defense systems. This program includes glycolytic enzymes, mitochondrial metabolic enzymes, lipid synthesis enzymes, and antioxidant machinery. The metabolic reprogramming allows tumor cells to maintain biosynthetic capacity while surviving in the hypoxic, nutrient-poor tumor core and contributes to chemotherapy resistance.

**Predicted impacts**
- Enhanced nucleotide synthesis supporting rapid DNA replication
- Increased glucose metabolism and lactate production
- Enhanced antioxidant defense reducing reactive oxygen species
- Altered lipid metabolism supporting membrane biogenesis
- Metabolic adaptation to hypoxic microenvironment

**Evidence summary**
Multiple metabolic genes are present in the input list. MTHFD2 is highly expressed in rapidly proliferating cancer cells and supports one-carbon metabolism critical for nucleotide synthesis. ALDH1L1 is notably the primary marker for mature astrocytes and when altered in astrocytoma may reflect metabolic reprogramming. GCLC supports antioxidant defense through glutathione synthesis. The presence of metabolic genes in the context of astrocytoma suggests that tumor cells maintain active metabolic adaptation to support rapid proliferation and survival in nutrient-limited conditions. Studies of recurrent medulloblastoma show enhanced association with metabolism, stemness, and EMT signatures[30], suggesting that metabolic reprogramming is a general feature of brain tumor progression.

**Atomic biological processes**
- one-carbon metabolism and nucleotide synthesis. Genes: MTHFD2, ALDH1L1
  - [30]: Expression of key metabolic determinants including IDH1, HK2, and related metabolic genes increased in recurrent tumors
- antioxidant defense and glutathione synthesis. Genes: GCLC
  - [31]: NFE2L1 (Nrf1) is key regulator of glucose and lipid metabolism upregulated in stress responses
- lipid signaling and membrane remodeling. Genes: DGKG, PDE3A
  - [16]: PLCB1 is candidate signature gene for proneural subtype high-grade glioma with altered signaling dynamics

**Atomic cellular components**
- mitochondrial metabolic enzymes. Genes: MTHFD2
  - [30]: Mitochondrial genes show altered expression in recurrent tumor populations
- cytoplasmic metabolic enzymes. Genes: ALDH1L1, GCLC

**Program citations**
- [30]: Metabolic genes including IDH1, HK2 elevated in recurrent tumors with enhanced metabolism signatures
- [31]: Metabolic response genes regulated in response to stress and hypoxia

## Program: Transcriptional Regulation and Cell Fate Control
Coordinated activity of multiple transcription factor families that collectively regulate cell fate decisions, progenitor maintenance, and resistance to differentiation. This program includes forkhead transcription factors (FOXP2, FOXO1), basic helix-loop-helix factors (HES1, HES4, ID4), nuclear receptors (ESRRG, RORA), and other transcriptional regulators that cooperatively establish and maintain the tumor cell transcriptional landscape. Dysregulation of this program allows astrocytoma cells to resist normal differentiation signals while maintaining stemness-promoting transcriptional networks.

**Predicted impacts**
- Maintained expression of self-renewal genes
- Suppression of differentiation gene programs
- Altered cell cycle progression and proliferation control
- Resistance to differentiation-promoting signals
- Enhanced stemness and progenitor-like characteristics

**Evidence summary**
Multiple transcriptional regulators are present in the input list, suggesting coordinated transcriptional control at multiple levels. FOXP2, FOXO1, HES1, HES4, and ID4 collectively control progenitor versus differentiation fate decisions in normal neural development. The presence of multiple transcription factors from different families suggests that astrocytoma cells maintain complex transcriptional regulatory networks that suppress differentiation while promoting proliferation. Studies of glioblastoma demonstrate that canonical mutations promote functional plasticity through reactivation of developmental transcriptional programs, with specific transcription factors (INSM1) driving tumor evolution[3][28].

**Atomic biological processes**
- progenitor identity maintenance. Genes: FOXP2, FOXO1, HES1, HES4, ID4, NPAS3
  - [37]: FOXO1 affects medulloblastoma growth through regulation of progenitor state
- transcriptional repression and co-repressor recruitment. Genes: TLE1
  - [1]: Transcriptional control of gene expression programs in developing and reactive astrocytes
- nuclear receptor signaling. Genes: ESRRG, RORA

**Atomic cellular components**
- DNA binding domains of transcription factors. Genes: FOXP2, FOXO1, RFX4
  - [6]: FOXP2 is member of forkhead/winged-helix transcription factor family

**Program citations**
- [3]: Transcriptional programs govern glioblastoma plasticity and progenitor state
- [28]: Transcription factor networks regulate proliferation-differentiation balance in brain development
- [37]: FOXO1 regulates medulloblastoma growth through transcriptional control

## Program: Ion Channel Function and Calcium-Mediated Signaling
Coordinated activity of voltage-gated ion channels, ligand-gated channels, and calcium-handling proteins that regulate astrocyte excitability, membrane potential, and calcium-dependent signaling. This program maintains the ionic microenvironment around neurons and mediates astrocyte responses to neuronal activity. Dysregulation of ion channel function in astrocytoma impairs calcium-dependent glutamate uptake, alters astrocyte-neuron communication, and contributes to neuronal excitability changes and seizure susceptibility.

**Predicted impacts**
- Altered astrocyte membrane potential and excitability
- Impaired calcium-dependent astrocytic functions including glutamate uptake
- Dysregulated astrocyte-neuron signaling
- Enhanced neuronal excitability due to dysfunctional astrocytic support
- Increased seizure susceptibility in peritumoral cortex

**Evidence summary**
Six ion channel genes and two calcium pump genes are present in the input list, representing a comprehensive set of ion channel types involved in astrocyte physiology. TRPC4 is specifically documented as being implicated in calcium homeostasis in astrocytes[26]. The presence of multiple voltage-gated potassium channels (KCNQ5, KCNH7, KCNT2) alongside calcium channels (CACNB2, TPCN1, TRPC4) and calcium pumps (ATP2B2) suggests coordinated regulation of the ionic microenvironment. Dysregulation of astrocytic calcium signaling is documented to impair glutamate uptake and contribute to neuronal excitability changes in the tumor microenvironment[4].

**Atomic biological processes**
- voltage-gated potassium channel activity. Genes: KCNQ5, KCNH7, KCNT2, KCNIP1
  - [26]: TRPC4 regulates calcium homeostasis in astrocytes and participates in astrocytic calcium dynamics
- calcium influx and store-operated calcium entry. Genes: CACNB2, TPCN1, TRPC4
  - [26]: TRPC4 channels implicated in calcium homeostasis in astrocytes
  - [4]: Altered neuronal excitability results from impaired astrocytic function including calcium signaling
- calcium extrusion and ATP-dependent pumps. Genes: ATP2B2

**Atomic cellular components**
- plasma membrane ion channels. Genes: KCNQ5, KCNH7, KCNT2, CACNB2, TRPC4, TPCN1
  - [26]: Ion channels embedded in plasma membrane regulating cellular excitability
- intracellular calcium stores and their regulators. Genes: TPCN1, ATP2B2

**Program citations**
- [4]: Altered neuronal excitability results from impaired astrocytic calcium-dependent functions in glioma
- [26]: TRPC4 channel regulates calcium homeostasis specifically in astrocytes
- [32]: Peritumoral neurons show altered electrophysiological properties

## Program: Hypoxia Response and Metabolic Adaptation
Activation of hypoxia-inducible transcription factors and downstream targets that promote survival and growth in low-oxygen tumor microenvironment. This program includes HIF1A and HIF3A-mediated transcriptional responses that coordinately upregulate glycolysis, angiogenesis, erythropoiesis, and cell survival genes while downregulating oxidative phosphorylation. Recent evidence demonstrates that cycling hypoxia generates specific transcriptional patterns distinct from stable hypoxia through incoherent feedforward loops (IFFLs), suggesting that tumor-specific hypoxic dynamics drive unique adaptive programs.

**Predicted impacts**
- Upregulation of glycolytic enzymes for ATP production under hypoxia
- Enhanced angiogenesis and neovascularization
- Activation of cell survival pathways under metabolic stress
- Metabolic rewiring to favor glucose metabolism and lactate production
- Acquisition of specific transcriptional patterns in cycling (vs stable) hypoxia

**Evidence summary**
HIF1A and HIF3A are both present in the input list, representing the major transcriptional regulators of hypoxic adaptation. Recent characterization of cycling hypoxia in tumors demonstrates that HIF-1 cooperates with p53 and Notch1 to generate hypoxia-specific transcriptional patterns through incoherent feedforward loops (IFFLs)[31]. This finding suggests that the highly dynamic oxygen environment of tumors may drive specific adaptive programs distinct from those under stable hypoxia. The presence of both HIF1A and HIF3A suggests coordinated hypoxic adaptation at multiple regulatory levels.

**Atomic biological processes**
- hypoxia-inducible transcription factor signaling. Genes: HIF1A, HIF3A, RORA
  - [31]: HIF-1 forms incoherent feedforward loops with p53 and Notch1 to generate cycling hypoxia-specific gene expression patterns
- angiogenesis and vessel formation. Genes: HIF1A
  - [40]: VEGFA regulated by HIF family transcription factors in glioma angiogenesis
- metabolic adaptation to low oxygen. Genes: HIF1A, RORA
  - [31]: HIF-1-dependent metabolic rewiring occurs in response to cycling hypoxia

**Atomic cellular components**
- HIF-family transcription factors. Genes: HIF1A, HIF3A
  - [31]: HIF family transcription factors regulate hypoxic adaptive responses

**Program citations**
- [31]: HIF-1 driven IFFLs generate cycling hypoxia-specific gene expression patterns in tumors
- [40]: VEGFA angiogenesis regulated by HIF family transcription factors in gliomas

## Program: Protein Degradation, Ubiquitination, and Cellular Trafficking
Coordinated regulation of proteasomal and autophagy-mediated protein degradation pathways, together with endocytic trafficking machinery, that controls protein levels, clears misfolded proteins, and regulates signaling through selective degradation and spatial redistribution of key signaling proteins. This program includes E3 ubiquitin ligases, proteasomal components, autophagy regulators, and vesicular trafficking machinery. Dysregulation of this program allows selective stabilization of oncogenic proteins while promoting degradation of tumor suppressors, simultaneously facilitating the aberrant trafficking and subcellular localization of signaling proteins.

**Predicted impacts**
- Dysregulated stability of signaling proteins and ion channels
- Altered trafficking and subcellular localization of surface receptors
- Enhanced degradation of tumor suppressor proteins
- Stabilization of oncogenic proteins
- Dysregulated autophagy and clearance of damaged organelles

**Evidence summary**
Multiple ubiquitin ligase genes and trafficking regulators are present in the input list, suggesting that astrocytoma maintains complex proteostatic control networks. NEDD4, RNF150, ZNRF3, MARCH3, and TRIM9 collectively represent multiple families of E3 ubiquitin ligases with diverse substrate specificities. CLIP1 is documented to link endocytic vesicles to microtubules[47]. The presence of both ubiquitination and trafficking machinery suggests coordinated control of protein levels and localization at multiple levels. Dysregulation of this program would allow selective proteolysis of tumor suppressors while stabilizing oncogenic proteins.

**Atomic biological processes**
- E3-mediated ubiquitination and proteasomal degradation. Genes: NEDD4, RNF150, ZNRF3, MARCH3, TRIM9
  - [1]: E3 ubiquitin ligases participate in synaptic protein clearance and modulation of signaling
- endocytic trafficking and vesicular transport. Genes: CLIP1, SNX7
  - [47]: CLIP1 links endocytic vesicles to microtubules facilitating vesicular transport
- surface protein turnover and receptor endocytosis. Genes: MARCH3, NEDD4

**Atomic cellular components**
- E3 ubiquitin ligase complexes. Genes: NEDD4, RNF150, ZNRF3, MARCH3, TRIM9
- endocytic trafficking machinery. Genes: CLIP1, SNX7
  - [47]: CLIP1 protein participates in endocytic vesicle trafficking

**Program citations**
- [1]: E3 ubiquitin ligases modulate signaling through selective protein degradation
- [47]: CLIP1 participates in endocytic vesicle trafficking to degradative compartments

## Program: Cell Migration, Invasion, and Cytoskeletal Remodeling
Coordinated activity of actin-binding proteins, myosin motors, Rho family GTPases, and associated regulators that collectively drive actin cytoskeleton remodeling and enable rapid cell migration and invasion through tissue. This program includes proteins that promote filopodia and lamellipodia formation, as well as negative regulators that provide spatial and temporal control over migration. Dysregulation of this program in astrocytoma promotes enhanced motility, invasion through brain parenchyma, and contributes to the invasive, infiltrative phenotype characteristic of malignant gliomas.

**Predicted impacts**
- Enhanced cell migration and invasion capacity
- Increased filopodia formation facilitating migration
- Reduced migration inhibition from Rho GTPase antagonism
- Enhanced dissemination into adjacent neural tissue
- Infiltrative tumor growth pattern

**Evidence summary**
Multiple actin-regulating genes are present in the input list, representing a comprehensive set of migration and invasion machinery. FRY, MYO10, and ANLN promote actin-based structures involved in cell migration, while ARHGAP24 and ARHGAP31 provide negative regulation. The presence of both pro-migratory (FRY, MYO10, DOCK4) and anti-migratory (ARHGAP) genes suggests dynamic control of migration appropriate for tumor cells that must navigate complex tissue environments. The coordinated dysregulation of adhesion (program 2) and cytoskeletal remodeling would collectively promote the infiltrative phenotype of astrocytomas.

**Atomic biological processes**
- actin polymerization and nucleation. Genes: FRY, FMNL3, ANLN
  - [20]: Actin polymerization and cell migration programs active during development
- myosin-driven cell migration. Genes: MYO10, TPM1
- Rho GTPase signaling and migration control. Genes: DOCK4, ARHGAP24, ARHGAP31
- lamellipodia and filopodia dynamics. Genes: FRY, MYO10, ANLN

**Atomic cellular components**
- actin-binding and bundling proteins. Genes: FRY, ANLN, ADD3, LRRC1, LRRC4C, TPM1
- myosin motors. Genes: MYO10
- Rho GTPase regulators. Genes: DOCK4, ARHGAP24, ARHGAP31

**Program citations**
- [20]: Actin remodeling and migration programs during development

## Program: Receptor Tyrosine Kinase Signaling and Intercellular Communication
Coordinated activity of receptor tyrosine kinases and associated signaling molecules that mediate cell-cell and cell-matrix communication, driving proliferation, survival, and migration signals. This program includes Eph-family receptors and Fgfr/Igf1r already discussed in detail, but also other receptors and their ligands (ephrin, netrin, sema families) that regulate neural cell interactions. In astrocytoma, dysregulation of these communication pathways promotes tumor-neuron crosstalk, enhances tumor cell proliferation, and alters peritumoral neuronal properties.

**Predicted impacts**
- Enhanced neuron-glioma cell communication and synaptic interactions
- Increased neuronal excitability through Eph receptor-mediated signaling
- Dysregulation of developmental guidance signals
- Altered peritumoral neuronal circuit properties
- Enhanced seizure susceptibility through Eph-mediated neuronal excitation

**Evidence summary**
EPHB1 and EPHA5 are present in the input list and represent documented regulators of neuron-astrocyte interactions and neuronal excitability. EphB1 signaling has been characterized to excite neurons through phosphorylation of NMDAR subunits[19], and astrocytic ephrin-B1 controls excitatory-inhibitory balance[21]. In the tumor context, neuron-tumor crosstalk in the peritumoral cortex is documented to involve direct synaptic interactions[4][32], with neurons forming excitatory synapses with surrounding tumor cells. The presence of Eph receptors in both tumor-derived astrocytes and neurons suggests bidirectional communication that could amplify excitatory signals in the peritumoral region.

**Atomic biological processes**
- Eph receptor tyrosine kinase activation. Genes: EPHB1, EPHA5
  - [19]: EphB1 receptors regulate synaptic transmission and neuronal excitability through phosphorylation of NMDAR subunits
  - [21]: Astrocytic ephrin-B1 controls excitatory-inhibitory balance in developing hippocampus
- guidance factor signaling. Genes: DCC, SEMA4B
- astrocyte-neuron signaling. Genes: EPHB1, EPHA5
  - [4]: Neuron-tumor crosstalk in peritumoral cortex involves direct synaptic communication

**Atomic cellular components**
- Eph family receptor tyrosine kinases. Genes: EPHB1, EPHA5
  - [19]: EphB receptors are receptor tyrosine kinases activated by ephrin ligands

**Program citations**
- [4]: Neuron-tumor crosstalk involves direct synaptic communication in peritumoral cortex
- [19]: EphB1 receptor signaling regulates neuronal excitability and synaptic transmission
- [21]: Astrocytic ephrin-B1 controls excitatory-inhibitory balance
- [32]: Neuron-tumor interactions alter neuronal electrophysiology

## Program: Neurodegeneration-Associated Processes and Chronic Inflammation
Coordinated upregulation of genes associated with neuronal loss, neuroinflammation, and chronic microglial activation that collectively promote neuronal dysfunction and loss in the peritumoral environment. This program includes phagocytic receptors, complement components, and inflammatory mediators that are upregulated in both reactive astrocytes following CNS injury and in chronic neurodegenerative conditions. In astrocytoma, activation of neurodegeneration-associated programs drives progressive neuronal loss and dysfunction while simultaneously promoting an immunosuppressive microenvironment.

**Predicted impacts**
- Progressive neuronal loss in peritumoral region
- Sustained neuroinflammatory state
- Altered immune cell infiltration and activation
- Compromised synaptic connectivity
- Neurodegeneration-like phenotype despite lack of primary neuronal degenerative disease

**Evidence summary**
Multiple genes associated with neurodegeneration are present in the input list. MERTK and NDRG2 are specifically upregulated in reactive astrocytes during both acute TBI and chronic neurodegeneration[1][23]. The presence of neurodegeneration-associated genes in the astrocytoma context suggests that tumor-derived astrocytes maintain a chronic inflammatory and neurodegenerative phenotype that drives progressive neuronal loss. The temporal analysis of reactive astrocytes reveals that genes associated with chronic neurodegeneration are significantly upregulated specifically in the chronic phase[23], suggesting that sustained astrocyte reactivity creates a neurodegenerative microenvironment.

**Atomic biological processes**
- synapse pruning and neuronal loss. Genes: MERTK, NDRG2
  - [1]: Genes associated with neurodegeneration including Trem2 and Mertk upregulated in chronic phase astrocytes
  - [23]: MERTK, along with C1q and other complement components, mediates synapse pruning in reactive astrocytes and models of chronic neurodegeneration
- immune cell activation and recruitment. Genes: HNMT, TACR1
  - [41]: Glioma tumor microenvironment characterized by profoundly immunosuppressive nature limiting immunotherapy efficacy
- chronic inflammatory signaling. Genes: HNMT
  - [1]: Inflammatory and stress-related pathways enriched in acute and chronic phase astrocytes

**Atomic cellular components**
- phagocytic and complement receptors. Genes: MERTK
  - [23]: MERTK receptors mediate phagocytosis and synapse pruning

**Program citations**
- [1]: Neurodegeneration-associated genes upregulated in chronic phase astrocytes
- [23]: MERTK and other neurodegeneration genes mediate synapse pruning and neuronal loss
- [41]: Glioma microenvironment characterized by immunosuppression

## Program: Transcriptional and Post-Transcriptional Gene Regulation
Coordinated regulation of gene expression at multiple levels through transcriptional control, chromatin remodeling, and post-transcriptional mechanisms including alternative splicing and small RNA-mediated regulation. This program includes long non-coding RNAs (lncRNAs), RNA-binding proteins, and associated regulatory machinery. LncRNAs are increasingly recognized as critical regulators of cancer cell behavior through mechanisms including transcriptional control, alternative splicing modulation, and protein sequestration. Dysregulation of epigenetic and post-transcriptional mechanisms in astrocytoma allows selective gene expression patterns that maintain stemness while suppressing differentiation.

**Predicted impacts**
- Dysregulated gene expression through lncRNA-mediated mechanisms
- Altered alternative splicing patterns
- Selective mRNA stability and translation
- Epigenetic modifications affecting chromatin accessibility
- Context-specific gene expression enabling tumor-specific phenotypes

**Evidence summary**
Eight lncRNA genes are present in the input list, representing a substantial component of post-transcriptional regulation. While the specific functions of many of these lncRNAs in astrocytoma remain to be fully characterized, the presence of multiple lncRNAs suggests that post-transcriptional regulatory mechanisms are integral to the astrocytoma transcriptional landscape. The coordinated dysregulation of multiple lncRNAs alongside transcriptional regulators (programs 6 and 7) suggests multilevel control of gene expression appropriate for maintaining tumor-specific phenotypes.

**Atomic biological processes**
- long non-coding RNA-mediated regulation. Genes: LINC01677, ENTPD1-AS1, POT1-AS1, LINC01748, MIR99AHG, LINC01117, LINC00461, SLC8A1-AS1
- RNA binding and post-transcriptional control. Genes: RBMS3

**Atomic cellular components**
- long non-coding RNA molecules. Genes: LINC01677, ENTPD1-AS1, POT1-AS1, LINC01748, MIR99AHG, LINC01117, LINC00461, SLC8A1-AS1

## Bibliography
1. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
2. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
3. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
4. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
5. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
6. Available from: https://www.ncbi.nlm.nih.gov/gene/93986
7. Available from: https://www.ncbi.nlm.nih.gov/gene/114142
8. Available from: https://www.ncbi.nlm.nih.gov/gene/6507
9. Available from: https://www.ncbi.nlm.nih.gov/gene/3480
10. Available from: https://www.ncbi.nlm.nih.gov/gene/20512
11. Available from: https://www.ncbi.nlm.nih.gov/gene/16001
12. Available from: https://www.ncbi.nlm.nih.gov/gene/57447
13. Available from: https://www.ncbi.nlm.nih.gov/gene/2247
14. Available from: https://www.ncbi.nlm.nih.gov/gene/5728
15. Available from: https://www.ncbi.nlm.nih.gov/gene/23236
16. Available from: https://www.ncbi.nlm.nih.gov/gene/207
17. Available from: https://www.nature.com/subjects/cell-adhesion/ncomms
18. Liu Y, Hu J-J, Cao B, Chen P, Peng B, Yao H, et al.. EphB1-NR2B receptor signaling in glutamatergic neurons of the ventroposteromedial thalamic nucleus regulates emergence from anesthesia. Science Advances [Internet]. 2025Dec5;11(49). Available from: https://www.science.org/doi/10.1126/sciadv.adw7972
19. Murillo-Rincón AP, Seton LWG, Escamilla-Vega E, Damatac A, Fuß J, Fortmann-Grote C, et al.. Positional programs in early murine facial development and their role in human facial shape variability. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-66017-y
20. Available from: https://www.ncbi.nlm.nih.gov/gene/13641
21. Available from: https://www.ncbi.nlm.nih.gov/gene/9510
22. Available from: https://www.ncbi.nlm.nih.gov/gene/8038
23. Available from: https://www.ncbi.nlm.nih.gov/gene/16193
24. Available from: https://www.ncbi.nlm.nih.gov/gene/7223
25. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
26. Veo B, Wang D, DeSisto J, Pierce A, Brunt B, Bompada PC, et al.. Single-cell multi-omics identifies metabolism-linked epigenetic reprogramming as a driver of therapy-resistant medulloblastoma. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65466-9
27. Qiu X, Liu Y, Vera-Licona P, Agmon E, Kshitiz, Suhail Y. Hif-1 responsive IFFLs to explain specific transcriptional responses to cycling hypoxia in cancers. npj Systems Biology and Applications [Internet]. 2025Nov24;11(1). Available from: https://www.nature.com/articles/s41540-025-00612-z
28. Makwana K, Tilley L, Chakravarty P, Thompson J, Baillie-Benson P, Rodriguez-Polo I, et al.. Modelling co-development between the somites and neural tube in human trunk-like structures. Nature Cell Biology [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41556-025-01813-8
29. Available from: https://www.ncbi.nlm.nih.gov/gene/27086
30. Soliman E, de JC, Smith K, Ju J, Willison A, Mills J, et al.. Hematopoietic EphA4 deficiency alters microglial heterogeneity and improves chronic spatial memory after brain injury. Scientific Reports [Internet]. 2025Dec5;. Available from: https://www.nature.com/articles/s41598-025-30648-4
31. Available from: https://www.ncbi.nlm.nih.gov/gene/2321
32. Available from: https://www.ncbi.nlm.nih.gov/gene/2308
33. Available from: https://www.ncbi.nlm.nih.gov/gene/558
34. Available from: https://www.ncbi.nlm.nih.gov/gene/3952
35. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
36. Josip C, Wen-Lu T, Tao J, Zheng Z. Glioma tumor microenvironment and immunotherapy: past, present, and future.. Biomarker research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41272822/
37. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
38. Niovi N, Maria SA, Christiana MN, Panagiotis P. Emerging insights into the immunosuppressive tumor microenvironment and its implications for glioblastoma immunotherapy.. Frontiers in immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41208963/?fc=None&ff=20251116185347&v=2.18.0.post22+67771e2
39. Hanashima A, Kimoto M, Ujihara Y, Hashimoto K, Usui Y, Ohira M, et al.. CCDC141 is a Connectin/Titin and Nesprin-1 binding protein that adapts cardiomyocytes to mechanical stress. Communications Biology [Internet]. 2025Nov26;8(1). Available from: https://www.nature.com/articles/s42003-025-09093-6
40. Available from: https://www.ncbi.nlm.nih.gov/gene/7273
41. Available from: https://www.ncbi.nlm.nih.gov/gene/1432
42. Available from: https://www.ncbi.nlm.nih.gov/gene/6249
43. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
