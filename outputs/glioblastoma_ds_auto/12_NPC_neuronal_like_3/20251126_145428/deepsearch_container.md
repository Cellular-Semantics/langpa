# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: malignant glioblastoma (GBM)
- Tissue: brain

## Input Genes
GRIN3A, CUX2, LINC02144, LINC00639, CACNA2D3, DLX6-AS1, SYT1, OLFM3, TOX, THRB, SLAIN1, GABRB2, PLCB1, HRK, NYAP2, LINC00581, AL009178.3, MAML3, SLC17A6, LYPD6B, LRTM1, CARMIL1, CNTN2, EBF3, INSYN2B, ... (159 total)

## Program: Glutamate-calcium excitatory signaling
Glioblastoma cells co-opt glutamatergic signaling machinery to enhance intracellular calcium dynamics and promote proliferation through metabotropic and ionotropic glutamate receptors. This program encompasses the release of glutamate from glioma cells via SLC17A6, calcium entry through GRIN3A and CACNA2D3-containing channels, and phosphoinositide signaling through PLCB1. Enhanced calcium-dependent signaling activates downstream kinases and transcription factors that promote tumor growth and invasiveness.

**Predicted impacts**
- Enhanced proliferation and tumor growth through elevated intracellular calcium and downstream PI3K/AKT/mTOR pathway activation
- Increased invasiveness and migration through calcium-dependent cytoskeletal remodeling
- Metabolic reprogramming and genetic switching to accelerate glioma duplication
- Formation of synaptic-like connections between glioma cells and surrounding neurons
- Seizure and neurological symptoms through neuronal hyperexcitability

**Evidence summary**
Multiple lines of evidence demonstrate that glioblastoma cells hijack glutamatergic signaling to promote their own proliferation and invasiveness. GRIN3A encodes an NMDAR subunit whose dysregulation has been implicated in glioma pathology. CACNA2D3 regulates calcium channel surface expression and trafficking, affecting synaptic transmission. SLC17A6 packages glutamate into synaptic vesicles, enabling glioma-neuron communication. PLCB1 mediates calcium-dependent second messenger generation. SYT1 and SYT4 are presynaptic vesicle calcium sensors required for glioma progression. Knockout or knockdown of these genes reduces glioma cell proliferation, expansion, and invasiveness. Enhanced glutamatergic signaling creates feedback loops that promote neuronal hyperexcitability and tumor growth, with glioma-derived glutamate directly stimulating neuronal activity.

**Atomic biological processes**
- Glutamate release and vesicular transport. Genes: SLC17A6, SYT1, SYNPR
  - [1]: Glutamatergic transmission from glioma cells and increased glutamate release through elevated intracellular Ca2+ levels and activation of various glutamatergic receptor subtypes
  - [14]: SLC17A6 encodes vesicular glutamate transporter 2, which transports L-glutamate into synaptic vesicles
- Calcium channel function and calcium signaling. Genes: CACNA2D3, GRIN3A, PLCB1
  - [1]: Enhanced calcium signaling via hyper-activated glutamatergic receptors promotes glioma progression through metabolic reprogramming and increased intracellular Ca2+ levels
  - [3]: CACNA2D3 deletion differentially alters voltage-activated Ca2+ currents and affects synaptic transmission
- Calcium-dependent signaling cascades. Genes: PLCB1, ADCY8
  - [1]: Elevated intracellular Ca2+ activates nitric oxide synthase to produce nitric oxide (NO) that can promote or inhibit tumorigenesis

**Atomic cellular components**
- Synaptic vesicles and release machinery. Genes: SYT1, SYT4, SV2B, SYNPR
  - [7]: Intratumoral synapses between glioblastoma cells require presynaptic genes including syt 1 and syt 4 for vesicle calcium binding and neurotransmitter release
- Voltage-gated ion channels. Genes: CACNA2D3, KCNQ3, KCNK2, KCNH8
  - [3]: CACNA2D3 is an auxiliary subunit of voltage-gated calcium channels that regulates P/Q-type currents

**Required genes (not in input)**
- Genes: GRIN1, GRIN2A, GRIN2B, GRIA1, GRIA2, GRM1, GRM5, CaMK2A, NO synthase
  - [1]: Multiple glutamate receptor subunits (NMDAR, AMPAR, mGluR) and calcium/calmodulin-dependent kinase 2A interact to drive glioma progression

**Program citations**
- [1]: Comprehensive pathway analysis of glutamate-mediated and calcium-related signaling in glioma formation
- [7]: Synaptic components are required for glioblastoma progression; presynaptic genes including syt 1 partially rescue glioma-induced lethality
- [43]: Glioma cells upregulate expression of GABA receptors when in proximity to neurons; glutamate-mediated signaling contributes to feedback loops resulting in glioma-neuron network hyperexcitability
- [46]: Neuronal activity-driven mechanisms influence glioblastoma cell proliferation and invasion through direct synaptic connections

## Program: Neuronal differentiation transcription factor cascade
A hierarchical program of transcription factors and RNA-binding proteins that orchestrates neuronal lineage specification and maturation. Key regulators include CUX2 which controls dendrite and synapse development, RBFOX3 which regulates alternative splicing of neuronal differentiation genes, MYT1L which promotes neuronal conversion and maturation, EBF1/EBF3 which drive neuronal commitment, and CELF4 which translationally regulates synaptic protein synthesis during prenatal corticogenesis. These factors work sequentially to lock in neuronal identity and suppress proliferation, but can be dysregulated in glioma to maintain a more progenitor-like state.

**Predicted impacts**
- Suppression of glioblastoma proliferation through neuronal differentiation programs that enforce cell cycle exit
- Reduction of tumor stem cell properties through activation of neuronal maturation programs
- Altered expression of adhesion molecules and synapse-related proteins through RNA processing changes
- Increased susceptibility to differentiation therapy targeting these transcriptional networks
- Dysregulation of these programs in glioma may maintain a more progenitor-like, proliferative state

**Evidence summary**
The neuronal differentiation program represents a critical checkpoint that opposes glioblastoma tumor growth. CUX2 is a layer-specific transcription factor required for synapse formation and dendritic development; its loss-of-function facilitates seizures and glutamatergic hyperexcitability. RBFOX3 controls Numb alternative splicing to promote neuronal differentiation in postmitotic neurons. MYT1L is a pioneer transcription factor that enhances neuronal conversion from fibroblasts and is necessary for neuronal maturation in vivo; MYT1L loss correlates with microcephaly and reduced brain size. EBF1 and EBF3 are master regulators of neuronal commitment that couple differentiation to cell cycle exit. TOX integrates calcineurin/NFAT signals to control neurogenic determinants. CELF4 is an RNA-binding protein enriched in early synaptogenic compartments that translationally suppresses synaptic proteins and is dysregulated in autism-related neurodevelopmental disorders. Collectively, these factors form a hierarchical cascade that locks cells into a non-proliferative, differentiated neuronal state—a process likely antagonized or bypassed in glioma to maintain proliferative capacity.

**Atomic biological processes**
- Neuronal cell cycle exit and lineage commitment. Genes: CUX2, MYT1L, EBF1, EBF3, SOX1-OT
  - [2]: CUX2 is expressed in projection neurons during migration and is associated with synaptogenesis and layer specification
  - [15]: MYT1L promotes neuronal maturation and loss of MYT1L leads to precocious IP differentiation and depletion of progenitors
  - [22]: EBF genes are required for coupling neuronal differentiation to cell cycle exit and migration
- Alternative RNA splicing in neuronal differentiation. Genes: RBFOX3, CELF4, SRRM4
  - [9]: Rbfox3 is required for neuronal differentiation through Numb alternative splicing; Rbfox3-full represses exon 12 inclusion in Numb mRNA
  - [50]: CELF4 translationally represses mRNAs encoding synaptic proteins in developing subplate neurons; CELF4 target mRNAs encode risk genes for neurodevelopmental disorders
  - [53]: CELF proteins regulate alternative splicing of transcripts involved in neuronal function, with dysregulation implicated in neurological disorders
- Transcriptional regulation of neuronal genes. Genes: TOX, EBF1, EBF3, RBFOX3
  - [8]: TOX is a transcription factor regulated by calcineurin/Nfat signaling and controls neurogenic determinants including Sox2 and Tbr2
  - [19]: EBF proteins drive expression of neuronal differentiation genes and stabilize neuronal cell commitment through reinforcement of proneural factors

**Atomic cellular components**
- Nuclear transcription factor complexes. Genes: MYT1L, EBF1, EBF3, TOX, CUX2
  - [15]: MYT1L functions as a transcription factor that represses non-neuronal genes while promoting neuronal differentiation
- RNA-binding protein complexes. Genes: RBFOX3, CELF4, SRRM4, RBFOX1
  - [9]: Rbfox3 contains a conserved RNA recognition motif and binds to UGCAUG sequences in target mRNAs
  - [50]: CELF4 is an RNA-binding protein and translational regulator enriched in subplate and deep cortical layers

**Required genes (not in input)**
- Genes: SOX2, SOX3, SOX11, TBR2, NGNR1, DELTA1, NOTCH
  - [8]: TOX downstream targets include Sox2 and Tbr2, key transcription factors in neurogenesis
  - [49]: Sequential binding of SoxB1 and SoxC proteins (Sox2, Sox3, Sox11) drive neurogenesis through common gene enhancers

**Program citations**
- [2]: CUX2 is a novel marker of distinct transient critical histogenetic events during corticogenesis
- [9]: Rbfox3-regulated alternative splicing of Numb promotes neuronal differentiation
- [15]: MYT1L has emerging insights on functions as a transcription factor in neuronal development
- [50]: CELF4 controls mRNA translation underlying synaptic development; CELF4-target mRNAs are encoded by risk genes for adverse neurodevelopmental outcomes

## Program: Axon guidance and cell adhesion
Molecular pathways that direct neuronal axon extension and growth cone navigation through the guidance receptor-ligand interactions and cell adhesion molecules. This program encompasses the Slit-Robo repulsive guidance system via ROBO3 and SLIT1, ephrin-Eph forward and reverse signaling via EPHA3, EPHA5, EPHA7, classical cadherins (CDH2, CDH4, CDH12, CDH18, CDH22), contactin-associated proteins (CNTN2, CNTNAP5), and neurotrophin receptors (ERBB4, NRP1). These molecules regulate axon fasciculation, midline crossing, topographic mapping, and synapse formation. In glioblastoma, dysregulation of these programs facilitates tumor cell migration and invasion along existing neural circuits.

**Predicted impacts**
- Enhanced glioblastoma cell migration and invasion along white matter tracts and established neural circuits
- Aberrant interactions with neuronal axons facilitating formation of neoplastic synapses
- Dysregulation of guidance signaling enabling escape from spatial constraints that normally restrict tumor growth
- Altered angiogenesis through dysregulated NRP1 and FGFR2 signaling promoting tumor vascularization
- Potential enhanced metastatic potential through enhanced migration phenotype

**Evidence summary**
Glioblastoma cells co-opt axon guidance pathways to facilitate their own migration and invasion. ROBO3 mediates repulsive signaling via Slit ligands and controls midline crossing; dysregulation could facilitate tumor cell movement through restricted anatomical zones. SLIT1 is a secreted guidance ligand with repulsive properties. EPHA3, EPHA5, and EPHA7 mediate bidirectional ephrin-Eph signaling that guides axons through topographic mapping and growth cone steering; dysregulation of these signaling cascades could enable aberrant tumor cell navigation. Classical cadherins (CDH2, CDH4, CDH12, CDH18, CDH22) mediate cell-cell adhesion and are subject to strong negative selection in the CNS, suggesting critical roles in neural circuit formation that tumors disrupt. CNTN2 and CNTNAP5 are contactin-associated proteins enriched in myelinated axons that facilitate axon organization and nerve transmission; their dysregulation correlates with neurological disease. ERBB4 is a neuregulin-1 receptor controlling synaptic maturation; glioma cells may usurp this pathway to form ectopic synaptic connections. NRP1 acts as a co-receptor for VEGF and semaphorins, controlling both angiogenesis and axon guidance; dysregulation promotes tumor vascularization and invasion. FGFR2 expression decreases with glioma grade but remains expressed on glioblastoma stem cells, potentially supporting stemness properties.

**Atomic biological processes**
- Slit-Robo repulsive guidance signaling. Genes: ROBO3, SLIT1
  - [39]: Slit-Robo signaling pathway controls midline crossing and axon guidance; Robo3 has distinct functions in pre-crossing versus post-crossing commissural axons
  - [45]: Slit-Robo is a cell signaling protein complex with roles in axon guidance and angiogenesis; Slit2 functions as a repulsive cue via Robo receptors
- Ephrin-Eph bidirectional signaling. Genes: EPHA3, EPHA5, EPHA7
  - [38]: Ephrin-A and ephrin-B transduce distinct reverse signals upon interacting with Eph partners; these reverse signals control axon pathfinding and topographic mapping
  - [41]: Ephrin-A/EphA system signals in forward and reverse directions to guide growth cones; co-adaptation of forward and reverse signaling provides guidance precision
- Classical cadherin-mediated cell adhesion. Genes: CDH2, CDH4, CDH12, CDH18, CDH22
  - [37]: CDH12 regulates neurite outgrowth through cAMP/PKA signaling pathway and Rac1/Cdc42 activity
  - [40]: Classical cadherins comprise a family that regulates tissue morphogenesis through cell-cell adhesion and cytoskeletal dynamics; CDH expression patterns are strongly negatively selected in CNS
- Contactin and neurexin-mediated synaptic adhesion. Genes: CNTN2, CNTNAP5, NXPH1
  - [26]: Contactin 2 (CNTN2) is a cell adhesion molecule involved in axon guidance, neuronal migration, and fasciculation
  - [44]: CNTNAP5 is a neural transmembrane protein enriched in myelinated axons belonging to the neurexin superfamily; its absence causes axon malformation and poor nerve transmission
  - [47]: CNTNAP5 variants are implicated in glaucomatous neurodegeneration and neurodevelopmental disorders through altered regulatory gene networks
- Neurotrophin and growth factor receptor signaling. Genes: ERBB4, NRP1, FGFR2
  - [57]: Neuropilin-1 (NRP1) is a cell-surface receptor for VEGF165 and class 3 semaphorins; it acts as a co-receptor for VEGFR-2 to enhance VEGF activity and promote angiogenesis
  - [58]: ErbB4 is a postsynaptic target of neuregulin-1 that controls glutamatergic synapse maturation and plasticity

**Atomic cellular components**
- Guidance receptor complexes. Genes: ROBO3, EPHA3, EPHA5, EPHA7, ERBB4, NRP1
  - [39]: Robo receptors form complexes with ligands and recruit downstream signaling proteins including RhoGEF
- Axonal adhesion molecules. Genes: CDH2, CDH4, CDH12, CDH18, CDH22, CNTN2, CNTNAP5
  - [40]: Classical cadherins are transmembrane glycoproteins with ectodomains, calcium-binding regions, and conserved cytoplasmic domains

**Required genes (not in input)**
- Genes: SLIT2, SLIT3, ROBO1, ROBO2, EPHB2, EPHB3, EPHB6, SEMAPHORIN3, VEGFA, VEGFR2, PLEXIN
  - [39]: Robo1 and Robo2 work together to mediate repulsion from Slit; Robo3 has opposite activity
  - [57]: NRP1 synergizes with VEGFR-2 to promote angiogenesis; VEGF is essential for normal developmental angiogenesis

**Program citations**
- [39]: The Slit-Robo signalling pathway in nervous system development comprehensive review
- [40]: Classical cadherins evolutionary constraints in primates demonstrates strong negative selection in CNS
- [41]: Ephrin-A/EphA specific co-adaptation as novel topographic mapping mechanism
- [44]: Functional investigation suggests CNTNAP5 involvement in glaucomatous neurodegeneration
- [57]: Neuropilin-1 is required for vascular development and functions as VEGF co-receptor

## Program: GABAergic inhibitory neurotransmission
The inhibitory neurotransmitter system controlling neuronal excitability through GABA receptor signaling. This program encompasses GABAA receptor subunits (GABRB2, GABRA1), the somatostatin receptor 2 (SSTR2), and transcription factors controlling GABAergic interneuron identity (DLX5, DLX6). In the developing brain, GABA initially functions as an excitatory neurotransmitter before the developmental switch to inhibitory function. Dysregulation of GABAergic signaling in glioblastoma can promote tumor growth through altered inhibitory control of neuronal networks and may link to the high incidence of seizures in glioma patients.

**Predicted impacts**
- Dysregulation of inhibitory neurotransmission increasing neuronal hyperexcitability and seizure susceptibility
- Altered GABAergic feedback that normally suppresses tumor growth through paracrine signaling
- Glioma-mediated upregulation of GABA receptors on tumor cells facilitating autocrine/paracrine GABA signaling
- Reduced anxiety-like behavior and altered stress responses through changes in GABAergic circuit function
- Potential therapeutic vulnerability through manipulation of inhibitory tone

**Evidence summary**
GABAergic inhibitory neurotransmission represents a fundamental constraint on neuronal excitability and tumor growth. GABRB2 encodes the β2 subunit of GABAA receptors, which are composed primarily of α1β2γ2 subunits and mediate the fastest inhibitory transmissions in the brain; GABRB2 is highly expressed in gray matter and is subject to positive selection, indicating functional importance. Mutations and altered expression of GABRB2 are associated with epilepsy, autism, and other neuropsychiatric disorders. GABRA1 encodes the α1 subunit, also critical for inhibitory function. Glioblastoma cells have been noted to upregulate GABA receptor expression when in proximity to neurons, enabling them to respond to GABAergic signaling. SSTR2 mediates somatostatin neuropeptide signaling and is upregulated following injury; activation of SSTR2 can contribute to neurodegeneration but also may link to tumor-immune interactions. DLX5 and DLX6 are homeobox transcription factors essential for GABAergic interneuron specification and development; their conditional inactivation specifically in GABAergic neurons reduces anxiety-like behaviors and extends lifespan by 33%, highlighting the profound importance of GABAergic tone on organismal health. Dysregulation of GABAergic signaling in the glioma microenvironment could promote seizures and alter immune surveillance.

**Atomic biological processes**
- GABAergic synapse formation and function. Genes: GABRB2, GABRA1, SSTR2
  - [13]: GABAA receptors participate in excitatory transmission in immature brain and inhibitory transmission in mature brain; GABRB2 is associated with fastest inhibitory transmissions
  - [59]: Somatostatin-expressing GABAergic interneurons elicit layer-specific inhibition of pyramidal cells through prolonged postsynaptic inhibition mediated by somatostatin receptors
- GABAergic interneuron differentiation and identity. Genes: DLX5, DLX6
  - [21]: Dlx6 homeobox transcription factor is required for molecular properties of the striatum and other basal ganglia structures
  - [24]: Dlx5 and Dlx6 encode homeobox transcription factors expressed by developing and mature GABAergic interneurons; their inactivation in GABAergic neurons reduces anxiety-like behavior and extends lifespan

**Atomic cellular components**
- GABA receptor complexes. Genes: GABRB2, GABRA1
  - [13]: GABAA receptors are multisubunit chloride channels; β2 subunits participate in fastest inhibitory transmissions and regulate stress response and pain signals
- Neuropeptide receptor signaling. Genes: SSTR2
  - [56]: Somatostatin receptor 2 (SSTR2) is internalized by endogenous somatostatin following ischemic injury; activation of SSTR2 contributes to postischemic neurodegeneration

**Required genes (not in input)**
- Genes: GABA, GAD1, GAD2, SLC32A1, VGAT, SST
  - [24]: GABAergic interneurons are identified by vesicular GABA transporter (VGAT) and express somatostatin (SST)

**Program citations**
- [13]: GABRB2 is highly expressed in the brain and plays major inhibitory role; associated with multiple neuropsychiatric disorders
- [24]: Dlx5 and Dlx6 inactivation in GABAergic neurons reduces anxiety and extends lifespan by 33%
- [43]: Glioma cells upregulate GABA receptor expression when in proximity to neurons; endogenous GABA may impede tumor growth
- [59]: Somatostatin-expressing interneurons provide layer-specific inhibition through prolonged postsynaptic inhibition

## Program: Synaptic proteins and cytoskeletal dynamics
Molecular machinery controlling axonal microtubule organization, neurofilament structure, and synaptic vesicle dynamics. This program centers on STMN2 (stathmin-2) which binds tubulin heterodimers and regulates microtubule polymerization dynamics, critical for axon maintenance and regeneration. It also includes RhoGTPase signaling (RND3, ARHGAP18) controlling actin dynamics and cell migration, as well as cytoskeletal accessory proteins (DYNC1I1, SPHKAP). In normal neurons, these proteins maintain axon integrity and support neuronal transport; dysregulation in glioblastoma promotes migration and invasion.

**Predicted impacts**
- Enhanced glioblastoma cell migration and invasion through altered microtubule and actin dynamics
- Increased cellular motility and reduced adhesion properties facilitating tumor infiltration
- Dysregulated axonal transport affecting neuronal function and creating opportunities for glioma-neuron interactions
- Potential vulnerability to microtubule-targeting therapies if STMN2 is dysregulated
- Altered neurofilament organization affecting axon caliber and conduction velocity in invaded neurons

**Evidence summary**
Cytoskeletal dynamics control both normal neuronal function and pathological glioblastoma behavior. STMN2 is one of the most abundant mRNAs in human motor neurons and is essential for axon maintenance and regeneration. STMN2 binds directly to α/β tubulin heterodimers and regulates microtubule polymerization dynamics; in motor neurons affected by amyotrophic lateral sclerosis, pathogenic TDP-43 dysfunction causes cryptic splicing of STMN2 mRNA, leading to reduced stathmin-2 protein and axon degeneration. Restoration of stathmin-2 in TDP-43-mutant neurons rescues both neurite outgrowth deficits and axon regeneration capacity. In mature adult axons, stathmin-2 does not affect microtubule number but instead regulates neurofilament spacing and axon diameter, indicating critical roles in axon structural integrity. RND3 and ARHGAP18 are Rho family GTPase modulators controlling actin polymerization and depolymerization, essential for cell migration. FGD5 is a Rho GTP exchange factor. These proteins collectively regulate the cytoskeletal remodeling necessary for both normal neuronal morphogenesis and the enhanced migratory behavior of glioblastoma cells. DYNC1I1 encodes a dynein intermediate chain involved in axonal transport.

**Atomic biological processes**
- Microtubule assembly and tubulin binding. Genes: STMN2
  - [20]: Stathmin-2 (Stmn2) dynamically controls the interaction between stathmin and tubulin; knockdown of Stmn2 in rat hippocampal neurons reduces neurite extension
  - [23]: Stathmin-2 enhances motor axon regeneration after injury through its direct binding to the α/β tubulin dimer; STMN2 is one of the most abundantly expressed mRNAs in human motor neurons
- Rho GTPase signaling and actin dynamics. Genes: RND3, ARHGAP18, FGD5
  - [37]: CDH12 regulates neuronal growth through cAMP/PKA pathway which controls Rac1/Cdc42 activity, key Rho family GTPases controlling actin polymerization
- Axonal transport and motor protein function. Genes: DYNC1I1, STMN2
  - [20]: Dynamic control of Stathmin-tubulin interaction is essential for axonal outgrowth; phosphorylation-resistant Stmn2 increases mitochondrial trafficking through axons

**Atomic cellular components**
- Microtubule cytoskeleton. Genes: STMN2, DYNC1I1
  - [20]: Stmn2 regulates microtubule polymerization through direct interaction with tubulin; loss of Stmn2 causes neurofilament spacing collapse and reduction in axonal diameter
- Actin filament regulators. Genes: RND3, ARHGAP18, FGD5
  - [37]: Rac1/Cdc42 regulate actin polymerization downstream of CDH12 and PKA signaling

**Required genes (not in input)**
- Genes: TUBULIN, COFILIN, ARP2/3, ACTIN
  - [23]: Stathmin-2 directly binds the α/β tubulin dimer and modulates microtubule assembly

**Program citations**
- [20]: New roles for Stathmin-2 in axon integrity; emerging complexity in Stmn2 function
- [23]: Stathmin-2 enhances motor axon regeneration after injury; STMN2 is essential for neuromuscular junction maintenance

## Program: Thrombospondin-mediated synaptogenesis and immune regulation
A recently identified program linking glioblastoma-derived thrombospondin-1 (TSP1/THBS1) to both the promotion of intratumoral synaptic connectivity and the suppression of anti-tumor immunity. TSP1 is a matricellular protein and synaptogenic factor expressed by both astrocytes in non-connected regions and glioblastoma cells in highly functionally connected regions. TSP1 facilitates synapse formation through interactions with receptors and adhesion molecules, simultaneously promoting neuronal hyperexcitability and glutamatergic signaling. TSP1 also recruits anti-inflammatory tumor-associated macrophages and suppresses CD8+ T cell infiltration and activation.

**Predicted impacts**
- Promotion of neoplastic synapse formation between glioblastoma cells and neurons increasing neuronal activity-driven tumor proliferation
- Creation of an immunosuppressive microenvironment through recruitment of anti-inflammatory macrophages and suppression of CD8+ T cell function
- Reduced antitumor immunity in regions of high glioma-neuronal connectivity
- Potential therapeutic vulnerability through TSP1 inhibition to simultaneously reduce synaptic drive and restore anti-tumor immunity

**Evidence summary**
Thrombospondin-1 emerges as a critical linker between glioma-neuronal circuit remodeling and immune suppression. TSP1 is a multifunctional matricellular protein with roles in synaptogenesis, neuronal development, and immunomodulation. In glioblastoma, TSP1 expression is restricted to highly functionally connected (HFC) regions where glioma cells form numerous synapses with neurons. TSP1 knockout in glioblastoma cells suppresses synaptic gene programs, reduces glutamatergic signaling, and decreases neuronal hyperexcitability. Paradoxically, this same TSP1 knockout restores anti-inflammatory marker gene expression, increases pro-inflammatory macrophage infiltration, and improves CD8+ T cell activation—demonstrating that TSP1 not only drives synaptic plasticity but actively suppresses anti-tumor immunity. Functionally, pharmacological glutamate receptor antagonists (FDA-approved drugs) can reprogram the immune microenvironment toward a less immunosuppressive phenotype. This program represents a critical axis of tumor progression where neuronal activity, immune suppression, and tumor growth are coupled through a single molecular mediator, suggesting novel therapeutic opportunities targeting TSP1 or its signaling pathways.

**Atomic biological processes**
- Synaptogenesis and synaptic potentiation.
  - [46]: Thrombospondin-1 (TSP1) is a tumor-derived synaptogenic factor enriched in highly functionally connected (HFC) intratumoral regions; TSP1 knockout suppresses synaptogenesis and glutamatergic neuronal hyperexcitability
- Immune cell recruitment and polarization.
  - [46]: TSP1 knockout in glioblastoma cells reduces infiltration of anti-inflammatory TAMs and increases infiltration of pro-inflammatory TAMs and CD8+ T-cells; TSP1 knockout alleviates TAM-mediated T-cell suppression

**Atomic cellular components**
- Matricellular thrombospondin-1 complex.
  - [46]: TSP1 is predominantly expressed by glioblastoma cells within highly functionally connected regions and by astrocytes in non-connected regions

**Required genes (not in input)**
- Genes: THBS1, CD36, CD47, VEGF, TGF-β
  - [46]: TSP1 is a multifunctional matricellular protein with multiple receptors and interacting partners

**Program citations**
- [46]: Glioma-neuronal circuit remodeling induces regional immunosuppression mediated by TSP1; TSP1 knockout restores pro-inflammatory immunity and improves survival

## Program: Neuronal activity-sensing signaling cascade
Molecular pathways that integrate neuronal activity and calcium influx to activate intracellular signaling cascades controlling gene expression and cellular responses. This program includes protein kinase C alpha (PRKCA) which transduces both calcium-dependent and phospholipid-dependent signals, adenylyl cyclase 8 (ADCY8) which generates cAMP as a second messenger, and calcium/calmodulin-dependent kinases that link calcium to gene transcription. In glioblastoma, these activity sensors appear to be hyperactive, with neuronal-derived activity signals directly promoting tumor proliferation through enhanced calcium signaling and gene expression.

**Predicted impacts**
- Direct coupling of neuronal activity to glioblastoma proliferation through PKC-dependent signaling
- Enhanced calcium signaling and second messenger generation in response to synaptic inputs
- Activation of transcription factors and gene expression programs promoting tumor growth
- Potential vulnerability to kinase inhibitors targeting PRKCA or ADCY8 pathways

**Evidence summary**
Neuronal activity-sensing pathways directly link excitatory input to glioblastoma proliferation. PRKCA encodes protein kinase C alpha, a serine/threonine kinase that integrates both calcium and phospholipid signals to control gene expression and cellular responses. In bag cell neurons, PKC activation enhances electrical synaptic transmission by increasing junctional conductance and recruiting postsynaptic calcium currents—mechanisms that could facilitate glioma-neuron communication. Notably, gain-of-function mutations in PRKCA have been identified in Alzheimer disease patients and are associated with increased cellular PKC activity; these variants mediate synaptic depression through amyloid-beta signaling, suggesting that dysregulated PKC activity contributes to neurodegeneration. In glioblastoma, enhanced PKC signaling could translate neuronal activity into proliferative signals. ADCY8 encodes adenylyl cyclase 8, which catalyzes the conversion of ATP to cAMP—a critical second messenger linking activity to gene expression. Downstream effectors of cAMP signaling include protein kinase A (PKA) and CREB transcription factor phosphorylation, promoting neuronal growth and differentiation. In glioma, dysregulation of ADCY8-mediated cAMP generation could decouple these protective differentiation programs and instead redirect activity signals toward proliferation.

**Atomic biological processes**
- Protein kinase C-mediated signaling. Genes: PRKCA
  - [25]: Protein kinase C (PKC) is activated during afterdischarges and enhances electrical synaptic transmission by increasing junctional current and postsynaptic responsiveness
  - [28]: Gain-of-function mutations in PRKCA (PKCα) mediate synaptic depression through amyloid-beta; PKCα is required for deleterious synaptic effects of Aβ in Alzheimer disease
- Adenylyl cyclase-cAMP signaling. Genes: ADCY8
  - [37]: cAMP/PKA signaling pathway is activated downstream of CDH12 and controls neuronal growth through CREB phosphorylation and Rac1/Cdc42 activity

**Atomic cellular components**
- Serine/threonine kinase signaling complexes. Genes: PRKCA
  - [25]: PKC activation increases postsynaptic voltage-gated Ca2+ currents that are recruited by modest depolarization

**Required genes (not in input)**
- Genes: CAMK2A, CAMK4, CREB, PKA
  - [1]: CaMK2A intimately interacts with glutamate receptors and mediates downstream signaling in glioma

**Program citations**
- [25]: Protein Kinase C enhances electrical synaptic transmission by modulating junctional and membrane conductances
- [28]: Gain-of-function mutations in PRKCA mediate synaptic depression in Alzheimer disease; PKCα activity contributes to neuronal dysfunction

## Program: Neurofibromatosis and growth factor signaling
Signaling pathways mediated by receptor tyrosine kinases that promote cell proliferation, survival, and angiogenesis. This program includes fibroblast growth factor receptor 2 (FGFR2), which is highly expressed on astrocytes but downregulated with increasing glioma grade; neuropilin-1 (NRP1), which acts as a co-receptor for VEGF and semaphorins; and kit ligand signaling through KITLG. These receptors activate downstream phosphoinositide-3-kinase (PI3K) and mitogen-activated protein kinase (MAPK) cascades that promote tumor growth and angiogenesis.

**Predicted impacts**
- Enhanced glioblastoma angiogenesis through dysregulated VEGF signaling dependent on NRP1 co-receptor function
- Promotion of glioblastoma stem cell properties and therapy resistance through FGFR signaling
- Increased tumor vascularization supporting rapid tumor growth
- Potential therapeutic vulnerability to FGFR and NRP1 inhibition

**Evidence summary**
Growth factor receptor signaling promotes glioblastoma progression through multiple mechanisms. FGFR2 is the primary FGFR expressed on astrocytes in normal brain; however, FGFR2 expression decreases with increasing glioma grade, suggesting that loss of FGFR2 signaling may contribute to malignant progression. Despite reduced overall FGFR2 levels, this receptor remains highly prevalent on glioblastoma stem cell populations in vitro, where it likely supports stemness properties. FGFR1 (not in input list but frequently co-expressed with FGFR2) is preferentially expressed on glioblastoma stem cells where it regulates SOX2, OLIG2, and ZEB1—key transcription factors promoting tumorigenicity and radioresistance. NRP1 is a multifunctional receptor for both VEGF and class 3 semaphorins; it acts as a co-receptor for VEGFR-2 to enhance VEGF signaling and promote developmental angiogenesis. In glioblastoma, NRP1-mediated VEGF signaling drives tumor vascularization and pathological angiogenesis; NRP1 hypomorphism or defective VEGF binding substantially reduces both developmental and tumor-associated neovascularization. KITLG encodes kit ligand, promoting hematopoietic and endothelial cell growth. Together, these receptors create an angiogenic signal hub driving both tumor vascularization and immune cell infiltration.

**Atomic biological processes**
- Fibroblast growth factor receptor signaling. Genes: FGFR2
  - [27]: FGFR1 expression in malignant glioma is associated with increased migration of cancer cells and is a key regulator of tumor growth, invasion, therapy resistance, and cancer stemness
- Vascular endothelial growth factor signaling. Genes: NRP1
  - [57]: NRP1 is a coreceptor for VEGFR-2 that enhances VEGF165 binding and promotes angiogenesis; NRP1 knockout mice display abnormal vascular development
  - [60]: NRP1 hypomorphism combined with defective VEGF binding impairs pathological angiogenesis and reduces tumor growth

**Atomic cellular components**
- Receptor tyrosine kinase complexes. Genes: FGFR2, NRP1
  - [27]: FGFR1-3 are expressed on glioblastoma stem cells where they regulate stem cell transcription factors

**Required genes (not in input)**
- Genes: FGFR1, FGFR3, FGFR4, VEGFA, VEGFR1, VEGFR2, SEMAPHORIN3
  - [27]: FGFR1 is preferentially expressed on glioblastoma stem cells and promotes therapy resistance

**Program citations**
- [27]: Fibroblast Growth Factor Receptor Functions in Glioblastoma comprehensive review
- [57]: Neuropilin-1 is required for vascular development and functions as critical VEGF co-receptor
- [60]: NRP1 hypomorphism combined with defective VEGF binding impairs pathological angiogenesis in retinopathy model

## Program: Long non-coding RNA and RNA processing
Post-transcriptional and epigenetic regulatory mechanisms controlling gene expression through long non-coding RNAs (lncRNAs) and alternative RNA processing. The input list contains multiple long intergenic non-coding RNAs (LINC genes) and intronic transcripts (DLX6-AS1, SOX1-OT, PROX1-AS1) whose functions remain largely uncharacterized but may regulate chromatin structure, transcription factor availability, or mRNA stability. Additionally, genes like SRRM4 (serine/arginine repetitive matrix protein) regulate alternative splicing of neuronal genes. These regulatory layers provide additional points of dysregulation in glioblastoma.

**Predicted impacts**
- Dysregulation of neuronal genes through altered splicing factor activity
- Potential chromatin remodeling and transcriptional dysregulation through lncRNA-mediated mechanisms
- Altered expression of key glioma-related proteins through post-transcriptional regulation
- Potential therapeutic vulnerability through splicing factor inhibition or manipulation

**Evidence summary**
Long non-coding RNAs and alternative RNA processing represent an underexplored layer of gene regulation with likely importance for glioblastoma progression. SRRM4 encodes the serine/arginine repetitive matrix protein 4, a splicing regulator that controls neuronal-specific alternative splicing programs. The input gene list contains 24 long non-coding RNAs (LINC and antisense transcripts) whose functions in glioblastoma remain largely uncharacterized. lncRNAs have been shown to regulate chromatin structure, transcription factor activity, and mRNA stability through diverse mechanisms including RNase P-independent RNA processing, direct transcription factor binding, and assembly of ribonucleoprotein complexes. Some lncRNAs in the list are intronic antisense transcripts (e.g., DLX6-AS1, SOX1-OT, PROX1-AS1) that may regulate the expression of their sense-strand genes through cis-acting mechanisms. MIAT and other lncRNAs have been implicated in cancer development. Given the critical roles of RBFOX3 and CELF4 in neuronal alternative splicing, and the established dysregulation of splicing in neuropsychiatric disorders, dysregulation of RNA processing appears likely to contribute to glioblastoma phenotypes.

**Atomic biological processes**
- Alternative splicing regulation. Genes: SRRM4
  - [9]: SRRM4 regulates alternative pre-mRNA splicing; splicing factors control tissue-specific and developmental gene expression

**Atomic cellular components**
- Long non-coding RNA transcripts. Genes: LINC02144, LINC00639, DLX6-AS1, LINC00581, AL009178.3, SOX1-OT, AC022075.1, AL353138.1, PROX1-AS1, MYCBP2-AS1, MIAT, AC115282.1, NFIA-AS2, MIR548XHG, LINC01550, LINC01122, LINC01102, LINC02428, LINC00707, AC068722.1, AL445623.2, ADAMTS9-AS2, AC090403.1
  - [50]: Long non-coding RNAs and alternative splicing factor expression are dysregulated in neurodevelopmental disorders

**Required genes (not in input)**
- Genes: DICER, DROSHA, RNase P, Mediator complex
  - [50]: RNA-binding proteins and lncRNAs regulate post-transcriptional control of neuronal gene expression

**Program citations**
- [50]: CELF4 and other RNA-binding proteins control alternative splicing underlying synaptic development

## Program: Apoptosis regulation and cell death
Molecular pathways controlling programmed cell death and survival, including p53 family transcription factors and pro- and anti-apoptotic regulators. TP73 encodes the p73 tumor suppressor protein with structural and functional homology to p53; it can induce apoptosis or drive cell cycle arrest depending on context. HRK encodes a pro-apoptotic BH3-only protein. These genes may represent constraints on glioblastoma growth or vulnerabilities in tumor-initiating cells.

**Predicted impacts**
- Potential activation of apoptosis in glioblastoma cells through p73-mediated pathways
- Vulnerability to differentiation-therapy approaches that induce p73-dependent apoptosis
- Loss of apoptotic constraints during gliomagenesis allowing uncontrolled proliferation

**Evidence summary**
Cell death pathways represent critical anti-tumor mechanisms that are frequently dysregulated in glioblastoma. TP73 encodes the p73 protein, a member of the p53 family of tumor suppressors; p73 can induce both apoptosis and cell cycle arrest depending on its isoform and binding partners. Unlike p53, which is frequently mutated in glioblastoma, TP73 mutations are rare but dysregulation of p73 expression or activity occurs. HRK encodes a pro-apoptotic BH3-only protein that induces mitochondrial outer membrane permeabilization and initiates the intrinsic apoptotic cascade. These genes likely represent either tumor suppressive pathways that are dysregulated in glioma or, conversely, vulnerabilities that could be exploited therapeutically.

**Atomic biological processes**
- p53 family tumor suppressor signaling. Genes: TP73
  - [4]: p53 family proteins including TP73 have roles in neuropsychiatric disorders and development
- Intrinsic apoptotic pathway. Genes: HRK
  - [8]: Cell death and apoptosis are components of neural development regulated by developmental transcription factors

**Atomic cellular components**
- Apoptotic signaling complexes. Genes: TP73, HRK
  - [4]: p73 can activate pro-apoptotic transcription programs or cell cycle arrest

**Required genes (not in input)**
- Genes: TP53, BAX, BAK, BCL2, MDM2
  - [4]: p53 family proteins regulate apoptosis; TP73 shares structural homology with TP53

**Program citations**
- [4]: NMDAR dysfunction and neuropsychiatric disorders involve apoptotic regulation

## Bibliography
1. Zhe P, Kuo-Chieh L, Amber K, Gabriell E, Hoau-Yan W. Pathway analysis of glutamate-mediated, calcium-related signaling in glioma progression.. Biochemical pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
2. Terezija M, Ivica K, Mladen-Roko R, Željka K. Adult Upper Cortical Layer Specific Transcription Factor CUX2 Is Expressed in Transient Subplate and Marginal Zone Neurons of the Developing Human Brain.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7922267/
3. Stephani F, Scheuer V, Eckrich T, Blum K, Wang W, Obermair GJ, et al.. Deletion of the Ca2+ Channel Subunit α2δ3 Differentially Affects Cav2.1 and Cav2.2 Currents in Cultured Spiral Ganglion Neurons Before and After the Onset of Hearing. Frontiers in Cellular Neuroscience [Internet]. 2019Jun26;13. Available from: https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2019.00278/full
4. Zhang W, Ross PJ, Ellis J, Salter MW. Targeting NMDA receptors in neuropsychiatric disorders by drug screening on human neurons derived from pluripotent stem cells. Translational Psychiatry [Internet]. 2022Jun9;12(1). Available from: https://www.nature.com/articles/s41398-022-02010-z
5. Suzuki T, Tatsukawa T, Sudo G, Delandre C, Pai YJ, Miyamoto H, et al.. CUX2 deficiency causes facilitation of excitatory synaptic transmission onto hippocampus and increased seizure susceptibility to kainate. Scientific Reports [Internet]. 2022May17;12(1). Available from: https://www.nature.com/articles/s41598-022-10715-w
6. Nicholas JS, Jessica CN, Elelbin AO, Andrew HM, Dima KH, Zoë AS, et al.. cacna2d3, a voltage-gated calcium channel subunit, functions in vertebrate habituation learning and the startle sensitivity threshold.. PloS one [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9282658/
7. María L-P, Mamen HG-M, Irene G-R, Sergio C-T. Synaptic components are required for glioblastoma progression in Drosophila.. PLoS genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9352205/
8. Benedetta A, Antonio M de JD, Sara BA, Elisabeth B, Simone M, Andreas D, et al.. Tox: a multifunctional transcription factor and novel regulator of mammalian corticogenesis.. The EMBO journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4388598/
9. Available from: https://rupress.org/jcb/article/200/4/443/37219/Rbfox3-regulated-alternative-splicing-of-Numb
10. Tagliatti E, Bello OD, Mendonça PRF, Kotzadimitriou D, Nicholson E, Coleman J, et al.. Synaptotagmin 1 oligomers clamp and regulate different modes of neurotransmitter release. Proceedings of the National Academy of Sciences [Internet]. 2020Feb3;117(7). Available from: https://www.pnas.org/doi/10.1073/pnas.1920403117
11. Niu H, Wang H. TOX regulates T lymphocytes differentiation and its function in tumor. Frontiers in Immunology [Internet]. 2023Mar9;14. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.990419/full
12. Available from: https://www.ncbi.nlm.nih.gov/gene/146713
13. Available from: https://en.wikipedia.org/wiki/GABRB2
14. Available from: https://www.ncbi.nlm.nih.gov/gene/57084
15. Chen J, Yen A, Florian CP, Dougherty JD. MYT1L in the making: emerging insights on functions of a neurodevelopmental disorder gene. Translational Psychiatry [Internet]. 2022Jul22;12(1). Available from: https://www.nature.com/articles/s41398-022-02058-x
16. Available from: https://www.ncbi.nlm.nih.gov/gene/2561
17. Available from: https://www.uniprot.org/uniprotkb/Q9P2U8/entry
18. Available from: https://www.ncbi.nlm.nih.gov/gene/23040
19. Yangsook SG, Monica LV. EBF factors drive expression of multiple classes of target genes governing neuronal development.. Neural development [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3113313/
20. Emma JCT-S, Daniel WS. Microtubules, Membranes, and Movement: New Roles for Stathmin-2 in Axon Integrity.. Journal of neuroscience research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11407747/
21. Bei W, Thomas L, John LRR. Dlx6 regulates molecular properties of the striatum and central nucleus of the amygdala.. The Journal of comparative neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4019376/
22. Available from: https://journals.biologists.com/dev/article/130/24/6013/42188/Ebf-gene-function-is-required-for-coupling
23. Beccari MS, Arnold-Garcia O, Baughn MW, Artates JW, McAlonis-Downes M, Lim J, et al.. Stathmin-2 enhances motor axon regeneration after injury independent of its binding to tubulin. Proceedings of the National Academy of Sciences [Internet]. 2025May20;122(21). Available from: https://www.pnas.org/doi/10.1073/pnas.2502294122
24. Camille de L, Eglantine H, Gladys A, Anastasia F, Rim H, Cécile V, et al.. Aging [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6756896/
25. Christopher CB, Yueling G, Neil SM. Protein Kinase C Enhances Electrical Synaptic Transmission by Acting on Junctional and Postsynaptic Ca. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/29440551/
26. Available from: https://www.rcsb.org/structure/9ba4
27. Ana J-P, Florian AS. Fibroblast Growth Factor Receptor Functions in Glioblastoma.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6678715/
28. Available from: https://newtonlab.ucsd.edu/documents/Alfonsoetal.2016_000.pdf
29. Maria S, George K, Stefanos-Ioannis K, Niki K, Kostas T, Domna K. Neuronal, but not glial, Contactin 2 negatively regulates axon regeneration in the injured adult optic nerve.. The European journal of neuroscience [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33469963/
30. Deshors P, Kheil Z, Ligat L, Gouazé-Andersson V, Cohen-Jonathan ME. FGFR inhibition as a new therapeutic strategy to sensitize glioblastoma stem cells to tumor treating fields. Cell Death Discovery [Internet]. 2025Jun4;11(1). Available from: https://www.nature.com/articles/s41420-025-02542-5
31. Hakeem OL, David EK. SLC18: Vesicular neurotransmitter transporters for monoamines and acetylcholine.. Molecular aspects of medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3727660/
32. Benjamin D, Ritchie H, Agnes L, Christian JH, Richard MG, David JA. The transcription factor NFIA controls the onset of gliogenesis in the developing spinal cord.. Neuron [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/17178400/
33. Available from: https://www.ncbi.nlm.nih.gov/gene/23236
34. Available from: https://en.wikipedia.org/wiki/Vesicular_monoamine_transporter_1
35. Available from: https://www.jci.org/articles/view/127492
36. Available from: https://www.uniprot.org/uniprotkb/Q9NQ66/entry
37. Beibei G, Mengwei Q, Shuai H, Run Z, Wenxue Z, Yufang Z, et al.. Cadherin-12 Regulates Neurite Outgrowth Through the PKA/Rac1/Cdc42 Pathway in Cortical Neurons.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8606577/
38. Nan-Jie X, Mark H. Ephrin reverse signaling in axon guidance and synaptogenesis.. Seminars in cell & developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3288821/
39. Nicole S, Evelyn CA, Carlos O. The Slit-Robo signalling pathway in nervous system development: a comparative perspective from vertebrates and invertebrates.. Open biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12308364/
40. Max P, Fredy R-V, Marc C, Juan LB. Classical cadherins evolutionary constraints in primates is associated with their expression in the central nervous system.. PloS one [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11581309/
41. Available from: https://elifesciences.org/articles/25533
42. Available from: https://www.uniprot.org/uniprotkb/Q9Z2I4/entry
43. Pratibha S, Ashley A, Jiyong L, Vinay KP. Tumor microenvironment in glioblastoma: Current and emerging concepts.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10034917/
44. Sudipta C, Jyotishman S, Shantanu SR, Sukanya M, Sayani B, Sankhadip D, et al.. Functional investigation suggests CNTNAP5 involvement in glaucomatous neurodegeneration obtained from a GWAS in primary angle closure glaucoma.. PLoS genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11651621/
45. Available from: https://en.wikipedia.org/wiki/Slit-Robo
46. Nejo T, Krishna S, Yamamichi A, Lakshmanachetty S, Jimenez C, Lee KY, et al.. Glioma-neuronal circuit remodeling induces regional immunosuppression. Nature Communications [Internet]. 2025May22;16(1). Available from: https://www.nature.com/articles/s41467-025-60074-z
47. Alistair TP, Elena B, Maretha V de J, Ghazala M, Thomas SS, Fiorella M, et al.. Characterization of a family with rare deletions in CNTNAP5 and DOCK4 suggests novel risk loci for autism and dyslexia.. Biological psychiatry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2941017/
48. Available from: https://www.ncbi.nlm.nih.gov/gene/9353
49. Maria B, Daniel R, Cécile Z, Susanne K, Rickard S, Jonas M. Sequentially acting Sox transcription factors in neural lineage development.. Genes & development [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3243056/
50. Salamon I, Park Y, Miškić T, Kopić J, Matteson P, Page NF, et al.. Celf4 controls mRNA translation underlying synaptic development in the prenatal mammalian neocortex. Nature Communications [Internet]. 2023Sep27;14(1). Available from: https://www.nature.com/articles/s41467-023-41730-8
51. Available from: https://genesdev.cshlp.org/content/25/23/2423.full.pdf
52. Andrea NL. CUG-BP, Elav-like family (CELF)-mediated alternative splicing regulation in the brain during health and disease.. Molecular and cellular neurosciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3650117/
53. Gassmann M, Casagranda F, Orioli D, Simon H, Lai C, Klein R, et al.. Aberrant neural and cardiac development in mice lacking the ErbB4 neuregulin receptor. Nature [Internet]. 1995Nov1;378(6555). Available from: https://www.nature.com/articles/378390a0
54. Ralf KS, Chun Z, Stefan S, Matthias E, Golo K, Jeremy PA, et al.. Somatostatin receptor 2 is activated in cortical neurons and contributes to neurodegeneration after focal ischemia.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6730368/
55. Lee P, Goishi K, Davidson AJ, Mannix R, Zon L, Klagsbrun M. Neuropilin-1 is required for vascular development and is a mediator of VEGF-dependent angiogenesis in zebrafish. Proceedings of the National Academy of Sciences [Internet]. 2002Jul25;99(16). Available from: https://www.pnas.org/doi/10.1073/pnas.162366299
56. Bo L, Ran-Sook W, Lin M, Roberto M. The neuregulin-1 receptor erbB4 controls glutamatergic synapse maturation and plasticity.. Neuron [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/17521571/
57. Kecskés M, Henn-Mike N, Agócs-Laboda Á, Szőcs S, Petykó Z, Varga C. Somatostatin expressing GABAergic interneurons in the medial entorhinal cortex preferentially inhibit layerIII-V pyramidal cells. Communications Biology [Internet]. 2020Dec10;3(1). Available from: https://www.nature.com/articles/s42003-020-01496-x
58. Alessandro F, Birger H, Marwa M, Maiko Y, Alice P, Laura D, et al.. Neuropilin 1 (NRP1) hypomorphism combined with defective VEGF-A binding reveals novel roles for NRP1 in developmental and pathological angiogenesis.. Development (Cambridge, England) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3899814/
59. Available from: http://json-schema.org/draft-07/schema#"
