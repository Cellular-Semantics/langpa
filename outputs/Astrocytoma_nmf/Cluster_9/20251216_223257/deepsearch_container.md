# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and perilesional neurons
- Disease: Astrocytoma/Glioblastoma
- Tissue: Cerebral cortex, white matter

## Input Genes
UNC5D, DAB1, RGS7, ANK3, GRM7, MEG8, LRRC7, SNHG14, GRM5, MEG3, KCNQ3, NRG3, RBFOX1, PPFIA2, GRIN2B, CACNA1C, ATP8A2, PLPPR4, GABRB1, ANKS1B, KCNC2, TENM2, AL024495.1, KIRREL3, CACNA1E, ... (200 total)

## Program: L-type Calcium Channel Signaling and Synaptic Plasticity
CACNA1C, CACNA1D, and CACNA1E encode L-type voltage-gated calcium channels that mediate calcium influx during neuronal activity, coupled to dopamine-dependent plasticity pathways through D1/5 receptor signaling and cAMP-PKA-dependent phosphorylation. These channels trigger dendritic plateau potentials and behavioral timescale synaptic plasticity (BTSP) during spatial learning, and are critical targets for dopamine neuromodulation. In tumor context, glioma-derived factors alter dopaminergic tone and calcium signaling, shifting perilesional neurons toward aberrant excitability through enhanced CaV1.2-mediated calcium entry.

**Predicted impacts**
- Enhanced calcium-dependent dendritic integration in perilesional pyramidal neurons
- Increased susceptibility to paroxysmal depolarizing shifts (PDS) and seizure initiation
- Aberrant structural long-term potentiation driven by tumor-altered calcium dynamics
- Dysregulated experience-dependent plasticity due to altered dopaminergic modulation

**Evidence summary**
CACNA1C, CACNA1D, and CACNA1E collectively form a calcium influx module essential for experience-dependent neural plasticity and learning. In normal physiology, dopamine-dependent phosphorylation of CaV1.2 at Ser1928 enhances working memory performance through enhanced calcium-dependent synaptic plasticity. In astrocytoma, glioma cells alter local dopamine concentrations and glutamate levels, thereby disrupting the normal homeostatic range of calcium signaling. Perilesional neurons in glioma patients exhibit enhanced excitability and altered dendritic morphology characterized by increased spine density, phenomena mechanistically downstream of dysregulated calcium signaling. Computational models confirm that enhanced calcium influx through VGCCs predisposes neurons to paroxysmal depolarizing shifts that reliably predict seizure onset.

**Atomic biological processes**
- Calcium-dependent synaptic plasticity. Genes: CACNA1C, CACNA1D, CACNA1E, CAMK2B
  - [8]: CaV1.2 activation and dopamine-dependent phosphorylation at Ser1928 drives spatial learning through behavioral timescale synaptic plasticity
  - [31]: Rac1-mediated actin polymerization drives structural LTP independently of CaMKII downstream of calcium entry
- Dopamine-dependent neuromodulation of learning. Genes: CACNA1C
  - [8]: D1/5 signaling potentiates L-type currents through PKA-dependent phosphorylation of CaV1.2, enhancing working memory performance

**Atomic cellular components**
- L-type voltage-gated calcium channel complex. Genes: CACNA1C, CACNA1D, CACNA1E
  - [8]: CaV1.2 forms L-type calcium channels in dendritic membranes subject to phosphorylation-dependent modulation
  - [11]: CACNA1C encodes alpha-1 subunit of voltage-dependent calcium channel mediating calcium ion influx

**Required genes (not in input)**
- Genes: DRD1, DRD5, PRKG1, ATP2B, SLC24A
  - [8]: D1/5 dopamine receptors and cAMP-PKA pathway required for CaV1.2 modulation

**Program citations**
- [3]: Perilesional cortex neurons altered in intrinsic properties and dendritic morphology during glioma progression
- [8]: Dopamine-dependent modulation of CaV1.2 through D1/5 signaling and PKA phosphorylation
- [31]: Rac1-mediated structural LTP independent of CaMKII downstream of calcium signaling
- [44]: Glioma cells cause elevation of local glutamate and alter neuronal excitability via altered calcium signaling

## Program: NMDA Receptor-Mediated Glutamate Signaling and Excitotoxicity
GRIN1 and GRIN2B encode subunits of N-methyl-D-aspartate (NMDA) receptors that serve as molecular coincidence detectors gating calcium entry during synaptic activity. GRIN2B-containing receptors display slower kinetics and greater calcium permeability than GRIN2A, and couple to distinct downstream signaling cascades affecting synaptic plasticity and excitotoxicity. In the tumor microenvironment, glioma cells elevate local glutamate concentration through xCT transporter dysregulation and impaired reuptake, causing pathological hyperactivation of NMDA receptors and generation of excessive calcium signals that trigger seizure-like activity.

**Predicted impacts**
- Excessive calcium influx into perilesional neurons through dysregulated NMDA receptor activation
- Generation of paroxysmal depolarizing shifts and seizure-like activity in peritumoral cortex
- Activation of calcium-dependent excitotoxic pathways including proteases, endonucleases, and pro-apoptotic cascades
- Disruption of normal long-term potentiation and depression signaling through altered calcium dynamics

**Evidence summary**
NMDA receptors serve as critical molecular switches that gate calcium entry during coincident pre- and postsynaptic activity, coupling synaptic transmission to plasticity mechanisms essential for learning and memory. GRIN2B-containing receptors have distinctive properties including slower kinetics and greater calcium permeability compared to GRIN2A-containing receptors. In astrocytoma, glioma cells produce glutamate through altered xCT transporter expression and impaired glutamate reuptake capacity, creating a state of chronic glutamate elevation that hyperactivates NMDA receptors. Single-cell RNA-seq from perilesional neurons of TAS patients reveals upregulation of NMDAR-related pathways, and computational models confirm that modest increases in NMDA receptor strength, combined with dendritic perturbations, trigger paroxysmal depolarizing shifts predictive of seizure initiation.

**Atomic biological processes**
- NMDA receptor-mediated calcium influx and synaptic plasticity. Genes: GRIN1, GRIN2B, GRIN2A
  - [9]: GRIN1 and GRIN2B encode N-methyl-D-aspartate receptor subunits gating calcium entry during synaptic activity
  - [12]: GRIN1 encodes critical NMDA receptor subunit in glutamate receptor channel superfamily
- Glutamate excitotoxicity and pathological calcium overload. Genes: GRIN1, GRIN2B
  - [3]: Glioma cells cause elevation of local glutamate concentration and alter neuronal excitability via xCT transporter dysregulation
  - [44]: Glioma cells elevate glutamate and trigger paroxysmal depolarizing shifts through excitotoxic mechanisms

**Atomic cellular components**
- NMDA receptor ion channel complex. Genes: GRIN1, GRIN2B, GRIN2A
  - [9]: NMDA receptor is member of ionotropic glutamate receptor superfamily with critical coincidence detection function
  - [12]: GRIN1 provides critical subunit of NMDA receptor channel superfamily

**Required genes (not in input)**
- Genes: SLC7A3, SLC1A1, SLC1A2, EAAT1, EAAT2
  - [44]: Impaired glutamate reuptake through xCT transporter dysregulation contributes to excitotoxicity

**Program citations**
- [3]: Glioma-derived glutamate triggers aberrant neuronal activity and altered transcriptional profiles in perilesional neurons
- [44]: Glioma cells cause glutamate excitotoxicity and neuronal hyperexcitability through NMDAR activation
- [9]: NMDA receptors as coincidence detectors in synaptic plasticity

## Program: AMPA Receptor Trafficking and Synaptic Strength Regulation
GRIA1 and GRIA2 encode GluA1 and GluA2 subunits of AMPA receptors, while GRIP1 and GRIP2 encode PDZ domain adapter proteins that link AMPA receptors to postsynaptic density scaffolds. GluA1 is dynamically trafficked during long-term potentiation and is primarily calcium-permeable, while GluA2 is more constitutively expressed and calcium-impermeable. The relative abundance of GluA2-containing vs GluA2-lacking AMPA receptors determines calcium permeability and short-term plasticity dynamics. In the tumor context, perilesional neurons undergo remodeling of synaptic composition with changes in AMPA receptor subunit stoichiometry reflecting aberrant homeostatic plasticity.

**Predicted impacts**
- Altered AMPA receptor subunit composition and calcium permeability in perilesional synapses
- Enhanced homeostatic synaptic potentiation through calcium-permeable AMPA receptor insertion
- Increased susceptibility to calcium-dependent excitotoxic cascades through dysregulated receptor trafficking
- Impaired regulation of synaptic strength through disrupted activity-dependent receptor internalization

**Evidence summary**
AMPA receptors mediate the majority of fast excitatory synaptic transmission and undergo activity-dependent trafficking that underlies both long-term potentiation and long-term depression. GluA1-containing AMPA receptors are dynamically trafficked during learning and are primarily calcium-permeable, while GluA2-containing receptors are more constitutively expressed and calcium-impermeable, determining the overall calcium permeability of the synapse. In astrocytoma, chronic dopamine depletion triggers homeostatic synaptic plasticity characterized by postsynaptic insertion of calcium-permeable AMPA receptors, and this compensatory response also occurs in perilesional neurons responding to glioma-derived factors. Perilesional pyramidal neurons from glioma patients with TAS show significantly increased AMPA receptor expression, particularly in the CA1 region, consistent with this homeostatic mechanism.

**Atomic biological processes**
- AMPA receptor activity-dependent trafficking and insertion. Genes: GRIA1, GRIA2, GRIP1, GRIP2, DLG2
  - [15]: GluA1 and GluA2 AMPA receptor subunits dynamically trafficked during long-term potentiation with distinct calcium permeability
  - [60]: GRIA2 encodes AMPA receptor subunit involved in endosomal dynamics and synaptic plasticity
- GluA2 AMPAR endocytosis and synaptic strength decrease. Genes: GRIA2, DPYSL5, NEDD4L
  - [29]: DPYSL5 regulates GluA2 AMPAR endocytosis via phosphorylation during LTD
  - [15]: AMPA receptor internalization through clathrin-mediated endocytosis modulated by neuronal pentraxin 1

**Atomic cellular components**
- AMPA receptor-postsynaptic density linkage complex. Genes: GRIA1, GRIA2, GRIP1, GRIP2, DLG2, DLG4
  - [15]: AMPA receptors anchored to PSD through GRIP adapter proteins and PSD-95 interactions
  - [51]: GRIP1 bridges membrane-proximal PSD layer including AMPA receptors with membrane-distal SHANK complex

**Required genes (not in input)**
- Genes: NSF, GluR2 binding proteins, CaMKII
  - [15]: NSF and associated factors required for AMPA receptor trafficking

**Program citations**
- [15]: Synaptic proteome diversity shaped by AMPA receptor subunit levels and trafficking
- [43]: Chronic dopamine depletion triggers homeostatic synaptic potentiation through AMPA receptor insertion
- [60]: GRIA2 involvement in AMPA receptor trafficking and regulation

## Program: GABAergic Synaptic Transmission and Inhibitory Circuit Assembly
GABRB1, GABRG2, and GABRA2 encode subunits of GABAA receptors, while GABBR2 encodes the B2 subunit of metabotropic GABA-B receptors. These genes collectively organize inhibitory synaptic transmission through effects on postsynaptic chloride influx and hyperpolarization. Gephyrin serves as the postsynaptic scaffold organizing inhibitory receptors at synaptic sites. In normal development, GABAergic interneurons are generated through Ascl1-dependent pathways and migrate to appropriate cortical layers to establish inhibitory circuitry. In astrocytoma, the reactivation of Ascl1-dependent developmental programs in astrocytes can drive conversion toward GABAergic neuronal fates.

**Predicted impacts**
- Dysregulation of E/I balance through altered GABAA and GABAB receptor signaling
- Impaired inhibitory control of perilesional pyramidal neuron activity
- Reactivation of GABAergic interneuron specification programs in astrocyte-derived cells
- Enhanced seizure susceptibility through reduced inhibitory constraint of excitatory networks

**Evidence summary**
GABAergic inhibitory synaptic transmission provides critical constraint on excitatory network activity and maintains normal patterns of neuronal firing. GABAA receptors mediate postsynaptic hyperpolarization through chloride influx, while GABAB receptors act as metabotropic suppressors of presynaptic neurotransmitter release. In normal development, Ascl1 drives the specification of GABAergic interneurons in a developmental-stage and phosphorylation-dependent manner. Remarkably, recent experiments demonstrate that Ascl1SA6 can reprogram lineage-traced astrocytes toward GABAergic neuronal fates, with this conversion driven by distinct transcriptional programs when the transgene is free of miR-124 target sites. In astrocytoma, the disruption of inhibitory transmission through either reduced GABAA receptor expression, altered inhibitory circuit assembly, or enhanced excitatory input would collectively shift the network toward pathological hyperexcitability and seizure generation.

**Atomic biological processes**
- GABA-mediated postsynaptic inhibition and hyperpolarization. Genes: GABRB1, GABRG2, GABRA2, GABBR2
  - [41]: GABAA receptors cluster at postsynaptic sites through gephyrin-mediated organization to mediate inhibitory transmission
  - [51]: Gephyrin serves as organizer of inhibitory synapses similar to PSD-95 role at excitatory synapses
- GABAergic interneuron specification and migration. Genes: MYT1L, RBFOX1, CELF4, SRRM4
  - [2]: Ascl1 drives differentiation toward GABAergic neurons during telencephalic development depending on developmental timing
  - [40]: Ascl1 SA6 robustly induces NPY expression in converted astrocytes toward GABAergic neuronal fate

**Atomic cellular components**
- GABAA receptor-gephyrin postsynaptic scaffold complex. Genes: GABRB1, GABRG2, GABRA2
  - [41]: Gephyrin multivalent scaffolding protein organizes GABAA and glycine receptors at postsynaptic sites
  - [51]: Acute gephyrin degradation leads to concomitant loss of GABAA receptors from postsynaptic membranes

**Required genes (not in input)**
- Genes: GAD1, GAD2, VGAT, SLC32A1
  - [2]: GAD1/2 and VGAT required for GABAergic neuron specification and vesicular GABA transport

**Program citations**
- [2]: Ascl1 drives GABAergic neuron differentiation during telencephalic development
- [40]: Ascl1 SA6-mediated astrocyte reprogramming toward GABAergic fate through NPY expression
- [41]: Gephyrin organization of inhibitory synaptic receptors

## Program: Postsynaptic Density Scaffolding and Synaptic Organization
DLG2, DLG4 (PSD-95), GKAP, and SHANK2 form a hierarchically organized postsynaptic density scaffold complex that anchors neurotransmitter receptors and couples them to downstream signaling cascades. PSD-95 serves as the core MAGUK protein organizing the membrane-proximal layer of the PSD, while GKAP bridges this layer to the membrane-distal SHANK complex. Recent discoveries reveal that GKAP, rather than PSD-95, acts as the primary structural determinant of PSD size, indicating a hierarchical architecture where specific components act as keystones. The involvement of multiple auxiliary proteins including LRRC7 and EDIL3 suggests additional layers of complexity in PSD organization.

**Predicted impacts**
- Dysregulated neurotransmitter receptor clustering and stabilization at synaptic sites
- Altered postsynaptic density size and composition due to perturbed scaffold stoichiometry
- Impaired coupling of synaptic activity to downstream signaling cascades
- Enhanced or reduced synaptic strength through misalignment of receptor anchoring machinery

**Evidence summary**
The postsynaptic density represents one of the most intricate macromolecular complexes in the nervous system, comprising hundreds of proteins organized in hierarchical layers that couple neurotransmitter receptors to the cytoskeleton and signaling machinery. PSD-95 and DLG2 serve as core MAGUK scaffolding proteins that organize the membrane-proximal layer, while GKAP bridges to the membrane-distal SHANK complex. Remarkably, acute degradation experiments reveal that GKAP acts as the primary structural determinant of PSD size, with GKAP degradation causing significant shrinkage and PSD-95 efflux, whereas acute PSD-95 degradation paradoxically does not reduce PSD size and is associated with influx of other PSD molecules into the same postsynaptic sites. This hierarchical organization indicates that dysregulation of specific scaffolding components could selectively alter receptor composition without triggering wholesale synapse loss, a property highly relevant to understanding how tumor-driven perturbations could remodel synaptic properties.

**Atomic biological processes**
- PSD protein hierarchical organization and receptor anchoring. Genes: DLG2, DLG4, GKAP, SHANK2, LRRC7
  - [16]: DLG4 (PSD-95) targets postsynaptic glutamate receptor scaffolding proteins and organizes synaptic components
  - [51]: GKAP acts as primary driver of postsynaptic density organization, with GKAP degradation causing PSD shrinkage
- Activity-dependent PSD remodeling and synaptic plasticity. Genes: DLG2, DLG4, GKAP, SHANK2, CAMK2B
  - [41]: Acute PSD protein degradation reveals roles in synaptic organization independent of overall PSD size
  - [15]: PSD protein stoichiometry determines synaptic strength and receptor composition

**Atomic cellular components**
- Postsynaptic density macro-molecular complex. Genes: DLG2, DLG4, GKAP, SHANK2, LRRC7, EDIL3
  - [41]: PSD comprises hierarchically organized layers linking membrane-proximal receptors to membrane-distal SHANK scaffolds
  - [51]: GKAP bridges membrane-proximal PSD95 layer with membrane-distal SHANK/ProSAPS layer via multivalent interactions

**Required genes (not in input)**
- Genes: SHANK1, SHANK3, Homer proteins, IP3R
  - [51]: SHANK family and Homer proteins required for complete PSD assembly

**Program citations**
- [41]: GKAP as primary structural determinant of PSD size through multivalent interactions
- [51]: Postsynaptic scaffold protein roles revealed by acute degradation
- [16]: PSD-95 scaffolding of glutamate receptors

## Program: Potassium Channel Expression and Action Potential Repolarization
KCNQ3, KCNC2, KCNB2, KCNJ3, KCNMA1, and KCNMB2 collectively encode voltage-gated potassium channels spanning multiple subtypes with distinct roles in action potential repolarization, subthreshold excitability, and burst firing patterns. KCNQ3 encodes a K7 channel involved in M-current regulation of subthreshold excitability and is mutated in neonatal epilepsy. KCNC2 and KCNB2 encode rapidly-inactivating and delayed-rectifier potassium channels respectively. KCNMA1 encodes large-conductance calcium-activated potassium channels (BK channels) while KCNMB2 encodes an auxiliary beta subunit. The coordinated expression of diverse potassium channel types determines the intrinsic firing properties and network excitability of neuronal populations.

**Predicted impacts**
- Dysregulated action potential repolarization and prolonged depolarization in perilesional neurons
- Altered intrinsic firing frequency and burst patterns through changes in potassium channel expression
- Enhanced excitability through reduced outward current during subthreshold and suprathreshold stimulation
- Increased seizure susceptibility through impaired inhibitory control of network activity

**Evidence summary**
Voltage-gated potassium channels are critical determinants of neuronal intrinsic excitability, action potential waveform, and burst firing properties. KCNQ3 mutations cause neonatal epilepsy through reduction of M-current, which normally suppressessubthreshold excitability. KCNC2 and KCNB2 encode fast-inactivating and delayed-rectifier potassium channels respectively, with differential roles in action potential repolarization. KCNMA1 encodes large-conductance calcium-activated potassium channels whose conductance depends on both membrane voltage and intracellular calcium concentration. In perilesional glioma-bearing animals, pyramidal neurons exhibit altered intrinsic properties including changes in resting membrane potential and action potential kinetics during early tumor progression prior to seizure onset. The dysregulation of multiple potassium channel genes would collectively reduce outward current during both subthreshold and action potential-related depolarizations, thereby increasing intrinsic excitability and predisposing networks to aberrant synchronous discharge.

**Atomic biological processes**
- Action potential repolarization and intrinsic excitability. Genes: KCNQ3, KCNC2, KCNB2, KCNMA1, KCNMB2, DPP10
  - [44]: Altered intrinsic properties of perilesional neurons including changes in repolarization kinetics during glioma progression
  - [10]: Potassium channel function determines baseline neuronal activity and firing patterns
- Subthreshold membrane potential regulation and M-current. Genes: KCNQ3
  - [10]: KCNQ family channels regulate subthreshold excitability through M-current generation

**Atomic cellular components**
- Voltage-gated potassium channel complexes at plasma membrane. Genes: KCNQ3, KCNC2, KCNB2, KCNJ3, KCNMA1, KCNMB2
  - [10]: Diverse potassium channel subtypes assembled at plasma membrane with differential subcellular localization

**Required genes (not in input)**
- Genes: Kv subunit-interacting proteins, Accessory subunits

**Program citations**
- [44]: Intrinsic electrophysiological properties of perilesional neurons altered during glioma progression
- [10]: PP2A subunit specificity in regulating Kv1.2 expression and neuronal activity

## Program: Neuronal Transcription Factor Networks and Developmental Cell Fate
MYT1L, INSM1, RBFOX1, CELF4, and SRRM4 collectively comprise a transcriptional and post-transcriptional regulatory network controlling the specification and maintenance of neuronal cell fate. MYT1L represses glial genes while activating neuronal genes. INSM1 drives specification toward intermediate progenitor cell-like states, and is highly expressed in glioblastoma and during normal intermediate progenitor specification. RBFOX1 regulates both alternative splicing and transcriptional networks in neuronal development. CELF4 and SRRM4 are neuronal-specific splicing factors that control the inclusion of neuronal-specific exons in hundreds of genes. The dysregulation of this transcriptional-post-transcriptional axis contributes to both normal neuronal development and to the aberrant cell fate plasticity characteristic of glioblastoma.

**Predicted impacts**
- Reactivation of developmental neuronal specification programs in glioma cells contributing to intermediate progenitor-like state and plasticity
- Dysregulation of neurotrophic signaling pathways through altered RBFOX1-mediated splicing
- Aberrant astrocyte-to-neuron transdifferentiation through ectopic INSM1 or MYT1L expression
- Global disruption of neuronal gene expression patterns through altered splicing factor activity

**Evidence summary**
Transcriptional and post-transcriptional mechanisms collectively establish and maintain neuronal cell identity, distinguishing neuronal from non-neuronal cell types. MYT1L serves as a master regulator that represses glial genes while activating neuronal genes, with overexpression capable of driving neuronal differentiation of non-neuronal cell types. INSM1 has recently been identified as a critical driver of glioblastoma tumorigenicity through its control of an intermediate progenitor cell-like state, with INSM1 knockdown in glioblastoma cells disrupting oncogenic gene expression and reducing in vivo tumorigenicity. RBFOX1 regulates both alternative splicing and transcriptional networks in neuronal development, with loss of function associated with psychiatric disease vulnerability through altered BDNF/TRKB signaling. SRRM4 and other neuronal-specific splicing factors control the inclusion of neuronal exons in hundreds of genes, effectively acting as master regulators of neuronal identity at the post-transcriptional level. In astrocytoma, the reactivation of these developmental programs through ectopic expression or dysregulation of their repressors would contribute to the remarkable cellular plasticity observed in these tumors.

**Atomic biological processes**
- Neuronal gene expression and repression of glial genes. Genes: MYT1L
  - [52]: MYT1L required for neuronal differentiation by repressing glial genes and activating neuronal genes
- Intermediate progenitor cell specification and self-renewal. Genes: INSM1
  - [5]: INSM1 governs neuronal progenitor state driving glioblastoma tumorigenicity with critical role in intermediate progenitor specification
  - [48]: INSM1 highly expressed in glioblastoma and during intermediate progenitor cell generation, knockdown reduces tumorigenicity
- BDNF/TRKB signaling and stress response pathway regulation. Genes: RBFOX1
  - [19]: RBFOX1 regulates BDNF and TrkB alternative splicing to control stress-response and plasticity pathways
- Neuronal-specific alternative splicing and exon inclusion. Genes: SRRM4, RBFOX1, CELF4
  - [52]: SRRM4 neuronal-specific splicing regulator controls inclusion of neuronal exons in hundreds of genes
  - [21]: RBFOX1 regulates RNA splicing and transcriptional networks in human neuronal development

**Atomic cellular components**
- Transcription factor complexes controlling neuronal vs glial cell fate. Genes: MYT1L, INSM1
  - [52]: MYT1L acts as neuronal identity master regulator through transcriptional control
- RNA splicing regulatory complex and neuronal exon inclusion machinery. Genes: SRRM4, RBFOX1, CELF4
  - [52]: SRRM4 as neuronal-specific splicing factor controlling identity at post-transcriptional level

**Required genes (not in input)**
- Genes: NeuroD, Neurogenin3, Pax6, SOX2
  - [5]: SOX2 repression by glioma mutations creates permissive state for INSM1-driven plasticity

**Program citations**
- [5]: INSM1 drives glioblastoma plasticity and tumorigenicity through intermediate progenitor cell state
- [48]: INSM1 knockdown reduces glioma tumorigenicity highlighting developmental program importance
- [52]: MYT1L as neuronal master regulator
- [19]: RBFOX1 in neuronal development and stress response regulation

## Program: Axonal Guidance and Circuit Wiring
DCC, ROBO1, ROBO2, SEMA3C, CNTN5, CHL1, and NTM comprise an axonal guidance system controlling the directional growth of axons and establishment of appropriate neural circuits during development. DCC encodes the deleted in colorectal cancer receptor serving as the primary receptor for netrin-1 guidance cues. ROBO1 and ROBO2 encode roundabout receptors mediating repulsive signaling through slit ligands. SEMA3C encodes a secreted guidance cue. The cell adhesion molecules CNTN5, CHL1, and NTM regulate neurite outgrowth and axonal fasciculation. In the glioma context, tumor cells produce netrin-1 and other guidance cues that exploit these developmental pathways to promote both tumor dissemination and remodeling of perilesional neural circuits.

**Predicted impacts**
- Remodeling of perilesional neural circuit connectivity through exploitation of developmental guidance pathways
- Enhanced glioma cell migration and invasiveness through activation of guidance receptor signaling
- Aberrant axonal pathfinding and circuit assembly in tumor-adjacent tissue
- Altered patterns of axonal innervation from distant regions to perilesional cortex

**Evidence summary**
Axonal guidance molecules represent fundamental determinants of neural circuit connectivity during development, with chemotactic factors like netrins attracting growing axons while repulsive cues like semaphorins and slits constrain their paths. DCC serves as the primary receptor for netrin-1, a secreted guidance cue that attracts commissural axons and promotes interneuron migration during development. Remarkably, glioma cells produce netrin-1 and other chemotactic factors that guide migration of both tumor cells and surrounding neurons, recapitulating physiologic migration patterns of glial progenitor cells that enable rapid dissemination through brain parenchyma. This phenomenon of tumor cells exploiting developmental guidance pathways represents a striking example of how oncogenic transformation reactivates and misuses normal developmental programs. The perilesional cortex exhibits altered patterns of axonal innervation with specific regional changes in synaptic density and connectivity patterns, phenomena suggesting that tumor-derived guidance cues fundamentally reshape perilesional neural architecture.

**Atomic biological processes**
- Netrin-mediated axonal attraction and DCC signaling. Genes: DCC
  - [34]: Glioma cells produce netrin-1 chemotactic factors that guide both tumor cell migration and neuronal remodeling
- Slit-mediated axonal repulsion and ROBO signaling. Genes: ROBO1, ROBO2
  - [35]: ROBO1 and ROBO2 mediate repulsive axonal guidance through slit ligand interactions
- Cell adhesion-mediated neurite outgrowth and axonal fasciculation. Genes: CNTN5, CHL1, NTM, CNTNAP2
  - [14]: CNTNAP2 member of neurexin superfamily plays essential role in neural development
  - [17]: CNTN2 contactin family protein mediates cell adhesion and neurite interactions

**Atomic cellular components**
- Netrin receptor and signaling complex. Genes: DCC
  - [34]: DCC primary receptor for netrin-1 guidance cues in axonal pathfinding
- Roundabout receptor-slit signaling complex. Genes: ROBO1, ROBO2
  - [35]: ROBO receptors mediate repulsive signaling upon slit ligand binding

**Required genes (not in input)**
- Genes: Netrin-1, Slit ligands, Semaphorin-3 ligands
  - [34]: Guidance ligands produced by glioma cells and perivascular cells

**Program citations**
- [34]: Pericytes and glioma cells produce chemotactic factors exploiting developmental migration programs
- [3]: Perilesional neurons exhibit altered axonal innervation patterns during glioma progression

## Program: Dendritic Spine Cytoskeleton and Structural Plasticity
MYO16, DPYSL5, VAV3, and related cytoskeletal regulatory genes control actin polymerization and microtubule dynamics in dendritic spines. DPYSL5 encodes a dihydropyrimidinase-related protein that inhibits dendritic growth through direct tubulin interaction. MYO16 encodes a myosin involved in actin dynamics and cellular morphology. VAV3 encodes a guanine nucleotide exchange factor for Rho family GTPases including Rac1. The discovery that transient Rac1 activation is sufficient to induce persistent structural long-term potentiation independently of CaMKII identifies Rac1 as a self-sustaining signaling module for dendritic spine growth. In astrocytoma, perilesional neurons exhibit increased dendritic spine density, suggesting that tumor-derived factors enhance Rac1 activation and actin-based spine remodeling.

**Predicted impacts**
- Enhanced dendritic spine formation and enlargement through Rac1-driven actin polymerization
- Increased synaptic multiplicity and synaptic strength through structural spine growth
- Altered microtubule dynamics affecting dendritic growth and stabilization
- Persistent structural remodeling of perilesional neuronal circuits through tumor-driven Rac1 activation

**Evidence summary**
Dendritic spine structure represents the physical substrate for synaptic information storage and transmission, with changes in spine size correlating with synaptic strength and plasticity. Rac1, a small GTPase regulating actin dynamics, serves as a molecular switch whose activation drives transient actin polymerization and persistent spine growth through mechanisms independent of the classical CaMKII-dependent pathway. DPYSL5 and related proteins regulate the opposing process through direct tubulin interaction and inhibition of microtubule polymerization. In astrocytoma, perilesional pyramidal neurons from TAS patients exhibit significantly increased dendritic spine density compared to non-TAS patients, with particularly prominent changes in apical and second-branch dendrites. These structural changes occur alongside transcriptional alterations consistent with enhanced synaptic plasticity, suggesting that tumor-derived factors reactivate developmental plasticity programs normally active during critical periods of brain development.

**Atomic biological processes**
- Rac1-mediated actin polymerization and spine enlargement. Genes: VAV3, MYO16
  - [31]: Transient photoactivation of Rac1 induces persistent structural LTP through actin polymerization independent of CaMKII
- Tubulin-DPYSL5 interaction and microtubule dynamics. Genes: DPYSL5
  - [29]: DPYSL5 inhibits microtubule polymerization and negatively regulates dendritic growth through tubulin interaction
- Dendritic spine formation and stabilization. Genes: MYO16, VAV3, SHANK2, LRRC7
  - [3]: Perilesional neurons exhibit increased dendritic spine density in glioma-bearing animals

**Atomic cellular components**
- Actin-myosin contractile apparatus in dendritic spines. Genes: VAV3, MYO16
  - [31]: Rac1 drives actin polymerization and spine structural changes
- Microtubule-associated protein complexes in dendrites. Genes: DPYSL5
  - [29]: DPYSL5 associates with tubulin and MAP2 to regulate microtubule polymerization

**Required genes (not in input)**
- Genes: Rac1, Cdc42, RhoA, WAVE complex
  - [31]: Rac1 and related Rho GTPases required for actin dynamics

**Program citations**
- [31]: Rac1 as self-sustaining signaling module for structural plasticity
- [3]: Increased dendritic spine density in perilesional neurons of TAS patients

## Program: Neuregulin-ErbB4 Signaling and GABAergic Interneuron Development
NRG1, NRG3, and ERBB4 form a critical signaling axis in development and function of GABAergic interneurons. NRG1 is produced by pyramidal neurons while ERBB4 is expressed on GABAergic interneurons, with this ligand-receptor pair regulating interneuron migration, differentiation, and synaptic integration. The NRG1-ErbB4 pathway has been implicated in schizophrenia and temporal lobe epilepsy. In glioblastoma, neuregulin-1 regulates the conversion of M1/M2 microglia phenotype via ErbB4-dependent inhibition of the NF-κB pathway, and trans-synaptic NRG1-ErbB4 signaling may mediate activity-dependent remodeling of glutamatergic and GABAergic synapses.

**Predicted impacts**
- Altered GABAergic interneuron properties through dysregulated NRG1-ErbB4 signaling
- Enhanced or impaired interneuron migration and circuit assembly in peritumoral regions
- Remodeling of microglia phenotype toward pro-tumoral inflammatory states
- Disrupted activity-dependent synaptic remodeling through altered trans-synaptic signaling

**Evidence summary**
NRG1-ErbB4 signaling represents a key axis in GABAergic interneuron development and function, with NRG1 produced by pyramidal neurons acting on ErbB4 receptors expressed on parvalbumin-expressing interneurons to regulate their migration, differentiation, and synaptic integration. Genetic variants in NRG1 and ERBB4 are associated with schizophrenia and temporal lobe epilepsy, suggesting that dysregulation of this pathway predisposes to both neurodevelopmental and seizure disorders. In the context of glioblastoma, NRG1-ErbB4 signaling extends beyond the neuronal compartment to regulate microglial phenotype, with neuregulin-1 driving the conversion of M1/M2 microglia phenotypes through ErbB4-dependent inhibition of the NF-κB pathway. This dual role of NRG1-ErbB4 signaling in both neuronal and immune cell functions suggests that dysregulation of this pathway in the tumor microenvironment could contribute to both altered perilesional neuronal circuitry and an altered immune microenvironment that favors tumor progression.

**Atomic biological processes**
- GABAergic interneuron migration and differentiation. Genes: NRG1, NRG3, ERBB4
  - [22]: NRG1-ErbB4 signaling toward parvalbumin-expressing interneurons regulates migration and differentiation
  - [23]: NRG1 intracellular signaling regulates development of interhemispheric callosal axons and interneuron circuits
- Trans-synaptic signaling and activity-dependent synaptic remodeling. Genes: NRG1, ERBB4
  - [20]: NRG1 mediates trans-synaptic signaling and transcytosis with ErbB4
- Microglia phenotype conversion and immune regulation. Genes: NRG1, ERBB4
  - [20]: Neuregulin-1 regulates M1/M2 microglia conversion via ErbB4-dependent NF-κB inhibition

**Atomic cellular components**
- NRG1-ErbB4 receptor signaling complex. Genes: NRG1, NRG3, ERBB4
  - [20]: NRG1 ligand-ERBB4 receptor complex mediates trans-synaptic signaling

**Required genes (not in input)**
- Genes: ErbB2, ErbB3, NRG2
  - [20]: Other ErbB family members and neuregulin ligands may compensate

**Program citations**
- [20]: NRG1-ErbB4 in neuronal and microglial function
- [22]: NRG1-ErbB4 signaling in GABAergic interneuron development

## Program: Protein Phosphatase 2A (PP2A) Compartmentalized Signaling
PPP2R2C encodes a regulatory subunit of protein phosphatase 2A that localizes specifically to the axon initial segment and functionally interacts with the Kv1.2 potassium channel to regulate its expression and neuronal activity during development. PP2A-B55 subfamily represents a newly discovered layer of post-translational regulation revealing specific subcellular targeting of phosphatase activity to functionally critical neuronal compartments. The discovery that Ppp2r2c-OE leads to remarkable potentiation of neuronal activity while baseline activity is maintained by both Ppp2r2a and Ppp2r2c indicates that precise PP2A targeting is essential for normal neuronal excitability.

**Predicted impacts**
- Dysregulated AIS ion channel expression and function through impaired phosphatase targeting
- Altered action potential initiation and propagation through disrupted Kv1.2 regulation
- Enhanced excitability through reduced dephosphorylation of inhibitory channel phosphorylation sites
- Developmental impairment of neuronal activity regulation during critical periods

**Evidence summary**
Protein phosphatase 2A serves critical roles in reversing kinase-mediated phosphorylation across diverse cellular contexts, with recent discoveries revealing that specific PP2A regulatory subunits target the catalytic core to distinct subcellular locations. PPP2R2C represents a newly characterized PP2A subunit that localizes specifically to the axon initial segment, where it functionally interacts with Kv1.2 potassium channels to regulate both their surface expression and the neuronal activity they mediate. The finding that overexpression of Ppp2r2c selectively potentiates neuronal activity while both Ppp2r2a and Ppp2r2c maintain baseline firing indicates that the precise subcellular targeting of PP2A catalytic activity determines its functional output. This compartmentalization principle extends to other protein modifications at the AIS, suggesting that dysregulation of AIS-specific phosphatases could contribute to altered action potential initiation patterns observed in perilesional neurons.

**Atomic biological processes**
- AIS-targeted protein dephosphorylation and ion channel regulation. Genes: PPP2R2C
  - [10]: PPP2R2C localizes to AIS and regulates Kv1.2 channel expression and neuronal activity through dephosphorylation
- Development-dependent modulation of neuronal excitability. Genes: PPP2R2C, ANK3
  - [10]: PP2A-B55 subunits modulate neuronal activity during in vitro development through AIS localization

**Atomic cellular components**
- PP2A-B55 regulatory subunit at axon initial segment. Genes: PPP2R2C
  - [10]: PPP2R2C enrichment at AIS creates specialized signaling microdomain

**Required genes (not in input)**
- Genes: PP2A catalytic subunit, PPP2R1A, PPP2R1B
  - [10]: Catalytic PP2A core required for phosphatase activity

**Program citations**
- [10]: PP2A subunit specificity in AIS function and neuronal activity

## Program: INSM1-Driven Intermediate Progenitor Cell State and Glioma Plasticity
INSM1 encodes a transcription factor that governs a neuronal progenitor state driving glioblastoma plasticity and tumorigenicity. In isogenic glioblastoma models, tumor cell evolution triggers stress-related metabolic changes and transitions toward a neuronal progenitor network driven specifically by INSM1 expression. INSM1 is highly expressed in human glioblastoma tumors and during cortical development in intermediate progenitor cells that give rise to neurons. Critically, INSM1 knockdown disrupts oncogenic gene expression and inhibits in vivo tumorigenicity, highlighting the functional importance of this developmental cell state in glioma pathogenesis. The intermediate progenitor cell state represents a specific developmental stage conferring both proliferative advantage and remarkable plasticity to respond to environmental cues.

**Predicted impacts**
- Maintenance of glioma cell plasticity through reactivation of intermediate progenitor cell developmental state
- Enhanced tumor cell adaptability to microenvironmental challenges including hypoxia and therapeutic stress
- Altered expression of genes controlling proliferation, differentiation, and invasion
- Dysregulation of normal neuronal development pathways through aberrant INSM1 expression

**Evidence summary**
INSM1 has recently emerged as a critical orchestrator of glioblastoma plasticity and tumorigenicity through its control of a neuronal intermediate progenitor cell-like state. In isogenic glioblastoma models engineered with canonical mutations (TERT promoter, TP53, PDGFRA), tumor cell evolution is accompanied by transition toward a gene expression program characteristic of intermediate progenitor cells and specifically driven by INSM1 upregulation. INSM1 is highly expressed in human glioblastoma tumors and during normal development in intermediate progenitor cells that serve as the primary source of neurons in the developing cortex. The functional importance of the INSM1-driven progenitor state is underscored by the finding that INSM1 knockdown in both triple mutant NSCs and primary glioblastoma cells significantly disrupts oncogenic gene expression programs and dramatically reduces in vivo tumorigenicity. This discovery fundamentally reframes our understanding of glioblastoma: rather than being composed of fully dedifferentiated stem cells, these tumors appear to exploit a specific developmental stage—the intermediate progenitor state—that confers both proliferative capacity and plasticity to respond to environmental pressures.

**Atomic biological processes**
- Intermediate progenitor cell specification and self-renewal. Genes: INSM1
  - [5]: INSM1 governs neuronal progenitor state driving glioblastoma cell evolution and plasticity
  - [48]: INSM1 drives transition toward neuronal progenitor network in glioblastoma with high expression in human tumors
- Tumor cell plasticity and response to environmental pressures. Genes: INSM1
  - [5]: INSM1 knockdown in glioblastoma cells disrupts oncogenic gene expression and inhibits tumorigenicity
- Stress-related metabolic reprogramming. Genes: INSM1
  - [5]: Tumor cell evolution triggers stress-related metabolic changes coordinated with INSM1-driven plasticity

**Atomic cellular components**
- INSM1 transcription factor complex. Genes: INSM1
  - [5]: INSM1 operates as transcription factor governing neuronal progenitor programs

**Required genes (not in input)**
- Genes: E2F6, histone acetylation machinery
  - [5]: E2F6 regulates INSM1 expression through histone acetylation-dependent mechanisms

**Program citations**
- [5]: INSM1 governs neuronal progenitor state driving glioblastoma tumorigenicity
- [48]: INSM1 highly expressed in glioblastoma and intermediate progenitor cells

## Program: Astrocyte Activation and Perilesional Neuroinflammation
GFAP expression, though not explicitly in the input list, reflects a broader astrocytic program relevant to understanding neuroinflammation in the glioma microenvironment. Recent high-throughput RNA sequencing of astrocytes following traumatic brain injury reveals sustained activation across acute, subacute, and chronic phases, with transcriptional signatures evolving from early pro-inflammatory profiles to mixed phenotypes featuring both neurodegenerative and regenerative elements. Multiple genes in the input list including neurotrophic factors (BDNF-related signaling through RBFOX1) and inflammatory mediators contribute to astrocyte-neuron interactions. In astrocytoma, astrocytic activation through exposure to glioma-derived factors creates a perilesional microenvironment characterized by altered neurotrophic support and inflammatory signaling that directly affects perilesional neuronal excitability and plasticity.

**Predicted impacts**
- Altered neurotrophic support for perilesional neurons through dysregulated astrocyte BDNF production
- Enhanced inflammatory microenvironment through astrocyte-derived cytokine production
- Impaired blood-brain barrier integrity through reactive astrogliosis
- Dual contribution to both neurodegeneration and attempted repair through mixed astrocyte phenotypes

**Evidence summary**
Astrocytes, the most abundant glial cells in the central nervous system, are integral to maintaining neuronal homeostasis, regulating blood-brain barrier integrity, and modulating synaptic function. Following central nervous system injury, astrocytes undergo reactive transformation characterized by morphological, molecular, and functional changes. Recent high-throughput RNA sequencing reveals that astrocyte transcriptional signatures evolve across injury phases, with acute profiles dominated by pro-inflammatory responses that transition to mixed phenotypes featuring both neurodegenerative and regenerative elements by chronic timepoints. Critically, a subset of astrocytes maintains neurogenic potential and continues to express neural stem cell markers even at one year post-injury, suggesting ongoing neuroplasticity and regenerative capacity. In astrocytoma, resident astrocytes are exposed to tumor-derived factors that drive their transformation into activated states characterized by altered production of neurotrophic factors and inflammatory mediators, thereby creating a microenvironment that simultaneously promotes tumor growth while affecting perilesional neuronal function and survival.

**Atomic biological processes**
- Reactive astrogliosis and pro-inflammatory cytokine production. Genes: RBFOX1
  - [24]: Astrocyte activation reveals distinct neuroinflammatory signatures evolving from pro-inflammatory to mixed neurodegenerative-regenerative phenotypes
  - [55]: Astrocytes maintain temporally distinct, phase-specific transcriptional trajectories following injury
- Synaptogenic and neuroprotective astrocyte function. Genes: RBFOX1
  - [24]: Astrocytes express compensatory neuroprotective genes including BDNF and other neurotrophic factors
- Astrocyte-derived regenerative programs and neurogenesis support. Genes: RBFOX1
  - [24]: Subset of astrocytes retain neurogenic potential and express neural stem cell maintenance markers

**Atomic cellular components**
- Astrocyte-neuron signaling axis and neurotrophic support. Genes: RBFOX1
  - [24]: Astrocytes integral to maintaining neuronal homeostasis and regulating synaptic function

**Required genes (not in input)**
- Genes: GFAP, IL6, TNF, IL1B, CXCL10
  - [24]: GFAP and inflammatory cytokines produced by activated astrocytes

**Program citations**
- [24]: Astrocyte activation and temporally distinct phenotypic transitions
- [55]: Sustained astrocyte activation with mixed degenerative and regenerative programs

## Program: Metabolic Reprogramming and Oxidative Phosphorylation in Glioma
While explicit metabolic enzyme genes are limited in the input list, the broader metabolic dysregulation in glioblastoma drives both tumor cell plasticity and therapeutic resistance. Recent translatome profiling identifies oxidative phosphorylation and glycolysis dysregulation as key resistance mechanisms in glioma, particularly relevant to understanding why anti-CSF-1R therapies targeting tumor-associated macrophages and microglia fail clinically. The fact that targeting oxidative phosphorylation/glycolysis with piperlongumine or vorinostat significantly improves survival when combined with standard therapy suggests metabolic reprogramming is not merely a consequence of transformation but rather a critical enabler of tumor plasticity and therapeutic resistance. Multiple genes in the input list including kinases and phosphatases could modulate metabolic state of both tumor cells and perilesional neurons.

**Predicted impacts**
- Enhanced metabolic flexibility enabling tumor cell adaptation to changing microenvironmental conditions
- Resistance to metabolic stress including hypoxia and nutrient depletion
- Altered energy substrate preference affecting both tumor cell and immune cell function
- Dysregulated mitochondrial function contributing to altered calcium handling and excitability

**Evidence summary**
Glioblastoma cells exhibit profound alterations in metabolic programming, including increased oxidative phosphorylation and dysregulated glycolysis that together support both rapid proliferation and cellular plasticity. Recent translatome profiling studies identify oxidative phosphorylation and glycolysis dysregulation as key mechanisms of resistance to anti-CSF-1R therapies, with triple combination therapy targeting these metabolic pathways significantly improving survival in preclinical glioma models. The finding that pharmacologic inhibitors of HDAC enzymes or polyphenols that enhance oxidative metabolism can synergize with standard chemotherapy suggests that metabolic reprogramming is not merely a consequence of transformation but rather a critical enabler of tumor cell plasticity and therapeutic resistance. This metabolic remodeling extends beyond tumor cells to affect the function of immune cells in the microenvironment, with macrophages and microglia showing altered metabolic profiles that support pro-tumoral polarization states.

**Atomic biological processes**
- Oxidative phosphorylation and ATP production dysregulation.
  - [37]: Oxidative phosphorylation dysregulation identified as key resistance mechanism in glioblastoma
- Glycolytic reprogramming and Warburg effect.
  - [37]: Glycolysis dysregulation contributes to glioma resistance mechanisms
- Metabolic plasticity enabling therapeutic resistance.
  - [37]: Targeting metabolic dysregulation with HDAC inhibitors or polyphenols improves therapeutic response

**Required genes (not in input)**
- Genes: HIF1A, LDHA, PKM, MTOR, AKT1
  - [37]: HIF1A and glycolytic enzymes dysregulated in glioma

**Program citations**
- [37]: Oxidative phosphorylation and glycolysis dysregulation in glioma resistance

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/546
2. 2. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
3. 3. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
5. 5. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/51299
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/627
8. 8. Man KNM, Rougé SLS, Berumen RA, Jacobi AA, Weiner JC, Naderi SY, et al.. Stimulation of Ca
                    <sup>2+</sup>
                    channel Ca
                    <sub>V</sub>
                    1.2 activity by dopamine signaling augments spatial working memory. Science Signaling [Internet]. 2025Dec9;18(916). Available from: https://www.science.org/doi/10.1126/scisignal.adp7760
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/2904
10. 10. Anderson AP, Kim S, Melton AJ, Ding X, Zhang W, Saltzman AB, et al.. A distinct PP2A subunit regulates local protein phosphorylation at the axon initial segment. Nature Communications [Internet]. 2025Dec3;16(1). Available from: https://www.nature.com/articles/s41467-025-66120-0
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/775
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/2902
13. 13. Lee Y-K, Xiao C, Zhou X, Wang L, McReynolds M, Wu Z, et al.. Bipolar and schizophrenia risk gene AKAP11 encodes an autophagy receptor coupling the regulation of PKA kinase network homeostasis to synaptic transmission. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-66356-w
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/26047
15. 15. Reig-Viader R, del C-BD, Burgas-Pau A, Arco-Alonso D, Zerpa-Rios O, Ramos-Vicente D, et al.. Synaptic proteome diversity is shaped by the levels of glutamate receptors and their regulatory proteins. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65490-9
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/1742
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/6900
18. 18. Hsu T-T, Chen C-P, Lin M-H, Hung T-E, Haung T-N, Wang C-Y, et al.. Shared and divergent alteration of whole-brain connectivity and sensory deficits in multiple autism mouse models. Molecular Psychiatry [Internet]. 2025Nov20;. Available from: https://www.nature.com/articles/s41380-025-03340-2
19. 19. Leggieri A, García-González J, Hosseinian S, Ashdown P, Anagianni S, Wang X, et al.. rbfox1 LoF mutants show disrupted bdnf/trkb2 and crhb/nr3c2 expression and increased cortisol levels during development coupled with signs of allostatic overload in adulthood. Translational Psychiatry [Internet]. 2025Nov19;15(1). Available from: https://www.nature.com/articles/s41398-025-03703-x
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/2066
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/54715
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
23. 23. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
24. 24. Wang Y, Jing L, Qi J, Wang Y, Song Y, Chen A, et al.. NeuroDepth: an ultra long whole brain reachable multi-channel probe for real-time precise functional localization of deep human brain tumor margins. Microsystems &amp; Nanoengineering [Internet]. 2025Dec11;11(1). Available from: https://www.nature.com/articles/s41378-025-01097-w
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/13869
26. 26. Available from: https://www.nature.com/subjects/cns-cancer/ncomms
27. 27. Desprez F, Remize S, François-Moutal L, Ung DC, Dangoumau A, Marouillat S, et al.. Missense variants in DPYSL5 associated with neurodevelopmental disorders and brain malformations cause impaired neuronal maturation in vitro. Molecular Psychiatry [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s41380-025-03364-8
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
29. 29. Takeo S, Chisato S, Yasunori H. Transient Photoactivation of Rac1 Induces Persistent Structural LTP Independent of CaMKII in Hippocampal Dendritic Spines.. eNeuro [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41249054/
30. 30. Jeet BS, Bartomeu P-A, Jenny S, Hadi M, Constanze IS, Anna F, et al.. Activity-dependent extracellular proteolytic cascade cleaves the ECM component brevican to promote structural plasticity.. EMBO reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41261283/
31. 31. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/319504
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/429
34. 34. Miao C, Ding Z, Wu J, An Q, Shu Y, Jiang H, et al.. Identification and targeting oxidative phosphorylation/glycolysis to overcome anti-CSF-1R therapy resistance in glioblastoma. Cell Death &amp; Disease [Internet]. 2025Dec10;. Available from: https://www.nature.com/articles/s41419-025-08288-3
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/17967
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/17172
37. 37. Elbaum-Mendelson L, Yuan W, Seiler JP-H, Blom N, Chan Y-C, Baig AH, et al.. Revealing acute consequences of rapid degradation of synaptic fusion proteins at individual synapses using Auxin-Inducible Degron 2 technology. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08996-8
38. 38. Peng T, Ying Z, Xingyu J, Yangping L, Li K, Feng W, et al.. A non-coding RNA risk pathway in schizophrenia: miR-137 enhances the lncRNA GOMAFU through a pathological transcription network.. Translational psychiatry [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41253765/
39. 39. Uzay B, Zhang KJ, Monteggia LM, Kavalali ET. Dopaminergic tone inhibits spontaneous glutamate release and augments homeostatic synaptic plasticity. Molecular Psychiatry [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41380-025-03374-6
40. 40. Trudel L, Therriault J, Macedo AC, Woo MS, Rahmouni N, Aumont É, et al.. APOE ε4 potentiates tau related reactive astrogliosis assessed by cerebrospinal fluid YKL40 in Alzheimer’s disease. Communications Medicine [Internet]. 2025Nov20;5(1). Available from: https://www.nature.com/articles/s43856-025-01171-4
41. 41. Fernandez RF, Fallatah W, Ji Y, Jones JW, Johnson CC, Tressler CM, et al.. Dysregulated hippocampal fatty acid metabolism following intermittent hypoxemia-induced neonatal brain injury is rescued by treatment with acetate. Nature Communications [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41467-025-67542-6_reference.pdf
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/4661
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/23040
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/283120
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/57441
48. 48. Darko-Boateng A, Afriyie E, Morgenstern TJ, Shanmugam SK, Zou X, Laloudakis YD, et al.. Ion channel inhibition by targeted recruitment of NEDD4-2 with divalent nanobodies. Nature Communications [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41467-025-67068-x
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/2891
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
51. 51. Giovannini S, Fiorilli C, Moriconi V, Shi Y, Candi E, Melino G, et al.. The role of HECT-type E3 ubiquitin ligases in DNA damage response and repair. Cell Death Discovery [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41420-025-02911-0
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/14812
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
54. 54. Available from: http://json-schema.org/draft-07/schema#",
