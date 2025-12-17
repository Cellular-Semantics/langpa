# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and radial glia progenitors
- Disease: Astrocytoma
- Tissue: Brain (central nervous system)

## Input Genes
DNAH11, EFHC2, SERPINI2, CFAP52, DRC1, ERICH3, C8ORF34, C4ORF47, SLC47A2, CFAP54, SLC9C2, DNAAF1, NAA11, CFAP57, SPAG1, SPAG17, SPATA17, MOK, ARMC2, CFAP61, FANK1, CASC1, NEK11, CFAP46, EFCAB6, ... (200 total)

## Program: Primary Ciliary Axonemal Dyneins and Motor Apparatus
Genes encoding outer dynein arm (ODA), inner dynein arm (IDA), and dynein regulatory complex components that comprise the motor machinery of axonemal microtubules in primary cilia. These proteins convert ATP hydrolysis into mechanical force driving ciliary beating and motility. Dysregulation impairs ciliary-dependent mechanosensing and developmental signaling, disrupting normal developmental constraints on astrocyte proliferation.

**Predicted impacts**
- Impaired primary cilium-dependent developmental signal reception (Hedgehog, Wnt, FGF pathways)
- Disrupted mechanotransduction through ciliary bending
- Altered astrocyte developmental plasticity and progenitor maintenance
- Enhanced susceptibility to uncontrolled proliferation through loss of differentiation signals
- Dysregulated ciliary polarity during asymmetric cell division

**Evidence summary**
The cohort contains at least 15 genes encoding outer dynein arms (DNAH family), inner dynein arm components (DNAI, DNAAF), and radial spoke proteins (DRC, ROPN1L). These proteins form the core structural and regulatory machinery enabling ciliary motility. In radial glia progenitors and astrocytes, primary cilia mediate developmental signal reception and mechanosensingvia Sonic hedgehog, Wnt, and other pathways. Loss or dysregulation of dynein function would impair these ciliary-dependent signaling pathways, disrupting normal developmental constraints that maintain RGP multipotency while limiting proliferation. Recent evidence demonstrates that ciliary dysfunction alters developmental fate specification in RGPs, with downstream consequences for neurogenesis and gliogenesis balance.

**Atomic biological processes**
- ATP hydrolysis-coupled ciliary motility. Genes: DNAH5, DNAH6, DNAH7, DNAH9, DNAH11, DNAH12, DNAI1, DNAAF1, ROPN1L, DRC1, DRC7
  - [1]: GJA1 (connexin) is a component of gap junctions relevant to intercellular communication altered in glioma
  - [3]: BDNF is involved in neural development and survival, with polymorphisms associated with cancer-related pathology
  - [7]: KIF11 localizes to basal bodies of primary cilia and reduction alters cilia dynamics
- Radial spoke and central pair signaling transduction. Genes: ROPN1L, DRC1, DRC7, CFAP46, CFAP47, CFAP52, CFAP54, CFAP57, CFAP61, CFAP69, CFAP70, CFAP73, CFAP100, CFAP206, CFAP221
  - [10]: CEP290 mutations impair protein interaction and localize to centrosomes, compromising cilia formation relevant to developmental timing

**Atomic cellular components**
- Axonemal nine-plus-two microtubule apparatus. Genes: DNAH5, DNAH6, DNAH7, DNAH9, DNAH11, DNAH12, TEKT1, CCDC30, CCDC40
  - [7]: KIF11 localization to primary cilia basal bodies indicates critical role in ciliogenesis

**Required genes (not in input)**
- Genes: CCDC39, CCDC103, LRRC6, SPAG1, HYDIN, CCDC114, DYX1C1
  - [10]: Multiple CCDC and other axonemal proteins required for cilia assembly

**Program citations**
- [1]: GJA1 and gap junction proteins implicated in cell-cell communication altered in glial tumors
- [3]: BDNF role in neural development with implications for tumor biology
- [7]: KIF11 localizes to primary cilia basal bodies
- [10]: CEP290 interactions with NPHP5 relevant to cilia formation

## Program: Centrosome Asymmetry and Asymmetric Cell Division Control
A program governing centrosome organization, pericentriolar material assembly, and asymmetric inheritance of centrosomes during cell division. Includes PCM1, CCDC proteins, CEP83, and associated factors. During asymmetric division of radial glia progenitors, this program determines whether daughter cells inherit mother or daughter centrosomes, thereby directing progenitor versus neuronal fate specification. In astrocytoma, dysregulation would disrupt developmental plasticity and potentially promote symmetric self-renewing divisions.

**Predicted impacts**
- Disrupted specification of progenitor versus differentiating daughter cells during RGP division
- Increased symmetric self-renewing divisions at expense of asymmetric divisions producing differentiating progeny
- Loss of developmental plasticity control mechanisms
- Enhanced proliferation potential through maintenance of progenitor identity in daughter cells
- Altered coupling between centrosome inheritance and polarized endosome trafficking

**Evidence summary**
Recent work identifies PCM1 as a critical regulator of centrosome asymmetry in radial glia progenitors. PCM1 localizes asymmetrically to the mother (posterior) centrosome and facilitates Par-3 assembly on polarized endosomes. Loss of pcm1 increases neuronal (N/N) divisions from 19% to 49% while decreasing progenitor-producing divisions (P/P from 42% to lower levels). This demonstrates that centrosome asymmetry programs directly specify RGP division modes. The program includes multiple CCDC genes (CCDC30, CCDC40, CCDC146, CCDC170) required for PCM assembly, and PARD3B which forms part of the polarization complex. In astrocytoma contexts, dysregulation of this program could promote enhanced self-renewal while disrupting normal differentiation constraints.

**Atomic biological processes**
- Pericentriolar material assembly and centrosome organization. Genes: CCDC30, CCDC40, CCDC146, CCDC170
  - [33]: PCM1 coordinates centrosome asymmetry with polarized endosome trafficking in radial glia progenitors; loss of pcm1 disrupts endosome dynamics
- Asymmetric centrosome inheritance and segregation. Genes: PARD3B
  - [33]: Mother centrosome preferentially localizes PCM1 and associates with Cep83 during mitosis; differential inheritance specifies progenitor versus differentiated fates

**Atomic cellular components**
- Pericentriolar material (PCM) complex. Genes: CCDC30, CCDC40, CCDC146, CCDC170
  - [33]: PCM1 exists in cloud-like patterns around centrosomes with asymmetric distribution along cell division axis

**Required genes (not in input)**
- Genes: CEP83, CEP76, CEP350, γ-tubulin
  - [33]: PCM1 associates with Cep83 on mother centrosome; other CEPs required for PCM function

**Program citations**
- [33]: PCM1 coordinates centrosome asymmetry with polarized endosome trafficking; loss alters progenitor division modes

## Program: Microtubule Organization and Post-Translational Tubulin Modification
Genes encoding tubulins, tubulin-modifying enzymes (particularly polyglutamylases), and microtubule-associated proteins that regulate microtubule stability, organization, and dynamics. TTLL9 catalyzes polyglutamylation of tubulin, a modification regulating microtubule-motor protein interactions. In RGPs, asymmetric microtubule organization contributes to cell polarity and division mode determination. Dysregulation alters both developmental plasticity and cell cycle checkpoint control.

**Predicted impacts**
- Altered microtubule stability and dynamics affecting spindle formation and cytokinesis
- Disrupted cell polarity establishment and maintenance
- Impaired asymmetric distribution of developmental determinants during mitosis
- Dysregulated intracellular transport of signaling complexes and organelles
- Enhanced cell cycle dysregulation through altered checkpoint control

**Evidence summary**
The cohort includes TUBA1A (alpha-tubulin, the fundamental structural unit of microtubules), TTLL9 (tubulin tyrosine ligase-like 9, catalyzing polyglutamylation), PACRG (parkin co-regulated gene product, a microtubule-associated protein), and multiple TTC genes (tetratricopeptide repeat-containing proteins) that regulate microtubule function. Polyglutamylation of tubulin regulates the binding of motor proteins and other microtubule-associated factors, thereby controlling intracellular transport and organelle positioning. During RGP asymmetric division, microtubules become asymmetrically organized around the mother centrosome, contributing to cell polarity and fate specification. Dysregulation of tubulin modification enzymes or microtubule-associated proteins would impair these developmental processes while potentially disrupting cell cycle checkpoint control.

**Atomic biological processes**
- Tubulin polyglutamylation and post-translational modification. Genes: TTLL9, PACRG
  - [36]: DNA replication fork speed acts as pacer in cortical development, connecting cell cycle dynamics to developmental timing
- Microtubule nucleation and organization from centrosomes. Genes: TUBA1A, TTC26, TTC29, TTC23L, TTC34
  - [33]: Microtubules more abundant around posterior (mother) centrosome during RGP mitosis

**Atomic cellular components**
- Microtubule lattice and associated protein complexes. Genes: TUBA1A, TEKT1, TTLL9, PACRG
  - [36]: Microtubule organization essential for polarized radial glial scaffold formation

**Required genes (not in input)**
- Genes: TUBB2A, TUBB2B, TUBB3, MAP2, MAP1B
  - [36]: Multiple tubulin and MAP proteins required for normal microtubule function

**Program citations**
- [33]: Microtubule organization asymmetry during RGP division
- [36]: Microtubule dynamics essential for cortical development timing

## Program: Endosomal Trafficking and Polarized Transport
Genes governing endosomal compartmentalization, trafficking between endosomal compartments, and asymmetric inheritance of endosomes during cell division. Includes PARD3B, DYNLRB2, and factors facilitating RAB5b-to-RAB11a transitions on specialized endosomes. This program couples centrosome asymmetry to polarized distribution of signaling complexes and developmental determinants, thereby directing cell fate specification in RGPs.

**Predicted impacts**
- Disrupted asymmetric distribution of signaling receptors and developmental determinants
- Impaired ability to maintain distinct signaling states in progenitor versus differentiating daughter cells
- Loss of developmental plasticity through disrupted coupling of endosomal trafficking to fate specification
- Altered growth factor receptor signaling intensity through dysregulated receptor recycling
- Enhanced proliferation through loss of endosomal trafficking-mediated differentiation signals

**Evidence summary**
PCM1 physically associates with Par-3 and Rab-family proteins on specialized directionally-localized (Dld) endosomes during RGP mitosis. These endosomes accumulate in the central zone and carry polarizing factors influencing daughter cell fate. The transition from Rab5b-positive (early endosomal) to Rab11a-positive (recycling endosomal) compartments facilitates asymmetric endosome distribution. PARD3B (Par-3 paralog) and DYNLRB2 (dynein light chain) participate in Par complex assembly and dynein-dependent endosomal transport. Loss of proper endosomal sorting would disrupt the molecular asymmetries distinguishing progenitor from differentiating daughter cells, thereby impairing normal developmental constraints.

**Atomic biological processes**
- Early-to-recycling endosome maturation and transition. Genes: PARD3B, DYNLRB2
  - [33]: PCM1 facilitates transition from Rab5b to Rab11a on recycling endosomes; loss impairs this transition
- Asymmetric endosome inheritance and polarized distribution. Genes: PARD3B, DYNLRB2
  - [33]: Directionally localized (Dld) endosomes accumulated in central zone during RGP anaphase; differential inheritance to daughter cells

**Atomic cellular components**
- Early endosomal compartment (Rab5b-positive). Genes: PARD3B, DYNLRB2
  - [33]: Rab5b compartments in surrounding cytoplasm; transition to Rab11a in central zone
- Recycling endosomal compartment (Rab11a-positive). Genes: PARD3B, DYNLRB2
  - [33]: Par-3 and PCM1 co-localize with Rab11a in central zone of dividing RGPs

**Required genes (not in input)**
- Genes: RAB5B, RAB11A, DLIC1, PAR3, PAR6
  - [33]: RAB GTPases and PAR complex components required for polarized endosomal trafficking

**Program citations**
- [33]: PCM1 interacts with Par-3, Dlic1, Rab11a, Rab5b on endosomes; physical coupling of centrosome asymmetry to endosomal trafficking

## Program: Transcriptional Control of Glial Differentiation and Neurogenic Fate
Genes encoding transcription factors and chromatin regulators that control the balance between proneural (neurogenic) and pro-gliogenic (glial-promoting) gene expression programs. SOX5 represents a key member specifying glial fates. Dysregulation of this program shifts the balance toward either uncontrolled gliogenic expansion (promoting astrocytoma) or inappropriate neurogenic differentiation. The program responds to developmental signals received through primary cilia and other developmental pathways.

**Predicted impacts**
- Dysregulated balance between neurogenic and gliogenic fate specification in RGPs
- Enhanced astrocytic self-renewal at expense of neuronal differentiation
- Loss of developmental constraints normally limiting RGP proliferation
- Impaired ability to respond to developmental signals specifying differentiation
- Potential acquisition of aberrant glial identity featuring both progenitor and mature astrocyte characteristics

**Evidence summary**
SOX5 (SRY-box transcription factor 5) represents a key regulator of glial fate specification that suppresses oncogenic signaling during glioma development. SOX5 may suppress PDGFB signaling effects during glioma development by regulating p27(Kip1) expression, implying a tumor-suppressive function. Recent research reveals that proneural bHLH transcription factors like ASCL1, when modified to include microRNA-binding sites, shift lineage outcomes from neurogenic toward oligodendrocyte and glutamatergic neuronal fates. This demonstrates that transcriptional fate regulators represent convergence points for multiple post-transcriptional regulatory mechanisms. In astrocytoma, dysregulation of SOX5 and related transcription factors would impair normal glial differentiation programs, potentially trapping RGPs in proliferative states.

**Atomic biological processes**
- Proneural-to-gliogenic transcriptional switching. Genes: SOX5
  - [17]: Ascl1 SA6 (phosphorylation-resistant form) drives GABAergic neuronal differentiation from astrocytes; inclusion of microRNA binding sites redirects toward oligodendrocyte fates
  - [19]: SOX5 may suppress oncogenic PDGFB signaling during glioma development by regulating p27(Kip1)
- Glial cell identity maintenance and astrocytic differentiation. Genes: SOX5
  - [22]: SOX9 regulates astrocyte reactivity and identity; peak-to-gene analysis shows reactive astrocyte genes associated with differentially accessible enhancers

**Atomic cellular components**
- Chromatin-accessible enhancer regions controlling glial differentiation. Genes: SOX5
  - [22]: Glial cell-specific enhancer regions enriched in binding motifs for SOX9, NFI, RFX transcription factors

**Required genes (not in input)**
- Genes: SOX9, OLIG2, OLIG1, ASCL1, NFI, RFX
  - [22]: Multiple SOX family members and proneural factors required for complete glial differentiation programs

**Program citations**
- [17]: Ascl1 phosphorylation and microRNA binding influence lineage fate decisions from astrocytes
- [19]: SOX5 suppresses oncogenic PDGFB signaling in gliomas
- [22]: SOX9 and other glial transcription factors control injury-responsive enhancers in astrocytes

## Program: Growth Factor Signaling and Neurotrophic Receptor Pathways
Genes governing receptor tyrosine kinase signaling, particularly NTRK2 (neurotrophin receptor tyrosine kinase 2) responding to BDNF. This program controls astrocyte proliferation, survival, and differentiation in response to neurotrophic factors. Dysregulation—whether through gene fusion (TRIM24::NTRK2), amplification, or increased ligand availability—drives proliferation through MAPK and PI3K pathway activation, characteristic of astrocytoma.

**Predicted impacts**
- Enhanced astrocyte proliferation through MAPK pathway activation
- Increased cell survival through PI3K/AKT pathway signaling
- Altered metabolic state toward anabolic (growth-promoting) pathways
- Dysregulated response to developmental BDNF signals in tumor microenvironment
- Potential acquisition of pro-invasive phenotypes through STAT3 activation

**Evidence summary**
NTRK2 encodes the high-affinity receptor for brain-derived neurotrophic factor and mediates neuronal survival, growth, and synaptic plasticity. Recent comprehensive characterization of pediatric high-grade gliomas identifies TRIM24::NTRK2 fusion as a recurring oncogenic driver in diffuse intrinsic pontine gliomas and other pediatric CNS tumors. The fusion protein shows constitutive activation (6-fold increased pTRKB), with highest activation of downstream PI3K pathway (pAKT 2.9-3.3-fold) and MAPK/PI3K mediator S6 (11.0-13.8-fold). Over tumor progression, cells become less reliant on TRIM24::NTRK2 while upregulating additional tyrosine kinases (FGFR1-3, FLT1, KIT, MET), demonstrating both initial NTRK2 dependency and subsequent plasticity. Elevated BDNF in tumor microenvironment increases peripheral innervation, suggesting active role of BDNF-NTRK2 signaling in tumor-host interactions.

**Atomic biological processes**
- BDNF-NTRK2 receptor-mediated signal transduction. Genes: NTRK2
  - [11]: TRIM24::NTRK2 fusion shows 6-fold increased pTRKB activation; highest activation in PI3K pathway (pAKT 2.9-3.3-fold) and downstream S6 (11.0-13.8-fold)
  - [29]: Elevated BDNF in tumor microenvironment increases innervation through TRK2 signaling
- PI3K/AKT and MAPK/ERK signaling cascade activation. Genes: NTRK2
  - [2]: AKT1 serine/threonine kinase mutations associated with multiple cancer types; regulates cell survival and proliferation
  - [11]: TRIM24::NTRK2 activates pERK, pAKT, pSTAT mediators and downstream S6 phosphorylation

**Atomic cellular components**
- NTRK2 receptor and associated signaling complexes. Genes: NTRK2
  - [11]: TRIM24::NTRK2 fusion contains intact tyrosine kinase domain enabling constitutive signaling

**Required genes (not in input)**
- Genes: BDNF, AKT1, PIK3CA, MAP2K1, MAPK1
  - [11]: AKT and MAPK pathway components downstream of NTRK2
  - [29]: BDNF required for NTRK2 signaling activation

**Program citations**
- [11]: TRIM24::NTRK2 fusion demonstrates constitutive tyrosine kinase activation in pediatric gliomas
- [29]: Elevated BDNF in tumor microenvironment mediates innervation through TRK2

## Program: Cell Cycle Checkpoint Control and Tumor Suppression
Genes governing G1/S and G2/M cell cycle checkpoint control, DNA damage response, and apoptosis induction. TP63 (p63 protein) represents a p53 family member implicated in cell identity and differentiation. WEE1 (G2 checkpoint kinase) phosphorylates CDK1 to prevent premature mitotic entry. Dysregulation—particularly through TP53 loss and WEE1 downregulation—permits uncontrolled cell cycle progression characteristic of astrocytoma.

**Predicted impacts**
- Enhanced cell cycle progression through G2/M checkpoint disruption
- Impaired DNA damage response and apoptosis evasion
- Acquisition of chromosomal instability and genomic complexity
- Disrupted developmental differentiation programs controlled by p63 family members
- Increased tumor cell invasiveness through loss of epithelial differentiation constraints

**Evidence summary**
TP63 encodes p63, a p53-related transcription factor implicated in epithelial cell identity and differentiation. The cohort includes TP63 (though TP53 itself is not in the list, TP53 mutations are critical context for astrocytoma). TP53 represents the most frequently mutated gene in astrocytomas, with mutations impairing tumor suppressor function while acquiring gain-of-function properties. The R175H hotspot mutation in TP53 DNA-binding domain results in loss of wild-type tumor suppressor function plus enhanced cell migration and invasion through aberrant transcriptional activation. WEE1 (not directly in list but functionally related to cell cycle programs) phosphorylates CDK1 to maintain G2 arrest, preventing mitotic entry with damaged DNA. Knockdown of WEE1-targeting lncRNAs impairs checkpoint control, allowing cells with unrepaired DNA to enter mitosis. In astrocytoma, loss of TP53 combined with dysregulation of WEE1 and checkpoint control enables uncontrolled proliferation despite genomic damage.

**Atomic biological processes**
- G2/M checkpoint control and CDK1 regulation. Genes: TP63
  - [48]: Knockdown of VIM-AS1 increases cell apoptosis via modulation of WEE1 targeting; WEE1 regulates G2 checkpoint through CDK1 phosphorylation
- DNA damage response and apoptosis induction. Genes: TP63
  - [12]: TP53 R175H mutation shows loss of TP53 function and chromosomal instability; promotes tumor cell invasion
  - [15]: TP53 R213X truncation creates premature termination codon; reported in Li-Fraumeni syndrome

**Atomic cellular components**
- TP53/p63 protein complex and transcriptional regulatory network. Genes: TP63
  - [12]: TP53 mutations at hotspot codons including 175 in DNA binding domain

**Required genes (not in input)**
- Genes: TP53, WEE1, CDK1, CHEK2, ATM
  - [12]: TP53 and checkpoint kinases essential for cell cycle control

**Program citations**
- [12]: TP53 R175H mutation represents hotspot with loss of function and gain of function properties
- [15]: TP53 R213X nonsense mutation reported in Li-Fraumeni syndrome
- [48]: WEE1 regulation through lncRNA-miRNA interactions controls G2 checkpoint

## Program: Metabolic Reprogramming and Glycolytic-to-Oxidative Metabolism Switching
Genes regulating metabolic state, particularly controlling glycolytic versus oxidative phosphorylation balance. SUCLG2 participates in citric acid cycle and lactate metabolism. This program enables the Warburg effect characteristic of astrocytomas—preferential glycolysis generating lactate that accumulates in tumor microenvironment. Dysregulation supports tumor cell proliferation under glucose limitation and shapes immune cell polarization in the tumor microenvironment.

**Predicted impacts**
- Enhanced glycolytic metabolism and lactate production characteristic of Warburg effect
- Tumor cell survival under glucose-limited microenvironmental conditions through lactate utilization
- Altered immune cell polarization through lactate-mediated signaling on macrophages
- Reduced dependence on oxidative phosphorylation despite metabolic inefficiency
- Microenvironmental lactate accumulation reshaping tumor ecosystem

**Evidence summary**
SUCLG2 encodes succinyl-CoA ligase, an enzyme functioning in both the citric acid cycle and fatty acid metabolism. Recent comprehensive analysis demonstrates that SUCLG2 plays a crucial role in regulating lactate metabolism in glioblastoma. SUCLG2 knockdown in glioblastoma cells significantly reduced lactate concentrations within tumor tissue, decreased mitochondrial membrane potential, and reduced proliferation. SUCLG2 knockdown cells showed decreased basal and maximal mitochondrial respiratory capacity with decreased ATP production, accompanied by enhanced glycolytic and glycolytic reserve capacities. Lactate at concentrations of 10-15 mM (achieved in tumor microenvironments) significantly reverses cell viability loss under low-glucose conditions, indicating lactate's critical role in tumor survival. HIF-1α facilitates glucose uptake and lactate production through binding to glycolytic enzyme genes including Glut1, HK2, LDHA, and PKM2. In astrocytoma, dysregulation of SUCLG2 and related metabolic genes promotes glycolytic reprogramming supporting both tumor cell proliferation and immunosuppressive microenvironment effects.

**Atomic biological processes**
- Lactate metabolism and glycolytic reprogramming. Genes: SUCLG2
  - [44]: SUCLG2 knockdown in GBM reduces lactate concentrations; lactate at 10-15 mM significantly reverses viability loss under low-glucose conditions
- Mitochondrial oxidative phosphorylation and ATP production. Genes: SUCLG2
  - [44]: SUCLG2 knockdown decreases basal and maximal mitochondrial respiratory capacity; decreased ATP production
- Hypoxia-inducible factor signaling and metabolic adaptation. Genes: SUCLG2
  - [44]: HIF-1α facilitates glucose uptake and lactate production by binding to glycolysis-related genes (Glut1, HK2, LDHA, PKM2)

**Atomic cellular components**
- Mitochondrial citric acid cycle enzymes and electron transport chain. Genes: SUCLG2
  - [44]: SUCLG2 participates in citric acid cycle; knockdown affects oxidative phosphorylation complex proteins (SDHB, ND1, ATP5A)

**Required genes (not in input)**
- Genes: HIF1A, LDHA, GLUT1, HK2, PKM2, MCT1
  - [44]: Glycolytic enzymes and HIF-1α target genes required for lactate metabolism reprogramming

**Program citations**
- [44]: SUCLG2 regulates lactate metabolism and mitochondrial function in GBM; knockdown reduces lactate and inhibits proliferation

## Program: Long Non-Coding RNA Regulation of Cancer Phenotypes
Genes encoding long non-coding RNAs (lncRNAs) that regulate cancer metabolism, cell proliferation, differentiation, and checkpoint control. The cohort includes multiple LINC genes (large intergenic non-coding RNAs) and lncRNA-associated genes. These transcripts modulate microRNA activity, chromatin accessibility, and signaling pathway engagement to shape astrocytoma phenotypes. Dysregulation of lncRNAs can simultaneously affect metabolic state, proliferation capacity, and drug resistance.

**Predicted impacts**
- Enhanced metabolic reprogramming through lncRNA-mediated glycolytic enzyme regulation
- Dysregulated cell proliferation and differentiation through miRNA sequestration
- Impaired checkpoint control through lncRNA-mediated modulation of WEE1 and related genes
- Enhanced drug resistance through lncRNA-dependent chemotherapy response pathways
- Altered tumor microenvironment composition through lncRNA-dependent immune signaling

**Evidence summary**
The cohort includes multiple long non-coding RNA genes (RMST, LINC00271, LINC00609, LINC00880, LINC00894, LINC01088, LINC01091, LINC01094, LINC01602, LINC02018, LINC02055) that regulate cancer biology. Recent comprehensive review identifies lncRNAs as critical regulators of cancer metabolism, particularly in glycolytic reprogramming supporting tumor growth. lncRNAs influence metabolic adaptation by modulating glycolytic enzymes, transcription factors, and signaling pathways. VIM-AS1 (vimentin antisense RNA) exemplifies lncRNA function: its knockdown inhibits glioma cell proliferation and migration while increasing apoptosis through modulation of WEE1 targeting. lncRNAs also function as competing endogenous RNAs (ceRNAs), sequestering microRNAs and thereby modulating target mRNA expression and protein synthesis. These multifaceted regulatory mechanisms position lncRNAs as both mechanistic drivers and therapeutic targets in astrocytoma, with potential for personalized lncRNA-targeted therapies.

**Atomic biological processes**
- MicroRNA-mediated post-transcriptional gene silencing. Genes: RMST, LINC00271, LINC00609, LINC00880, LINC00894, LINC01088, LINC01091, LINC01094, LINC01602, LINC02018, LINC02055
  - [17]: microRNA-mediated neuronal detargeting through inclusion of miRNA binding sites in transcripts alters lineage trajectories
  - [47]: lncRNAs act as competing endogenous RNAs (ceRNAs), sequestering microRNAs and modulating target gene expression
- Glycolytic reprogramming and metabolic enzyme regulation. Genes: RMST, LINC00271, LINC00609, LINC00880, LINC00894, LINC01088, LINC01091, LINC01094, LINC01602, LINC02018, LINC02055
  - [47]: lncRNAs are critical regulators of cancer metabolism through modulation of glycolytic enzymes and signaling pathways
- Transcription factor and chromatin accessibility modulation. Genes: RMST, LINC00271, LINC00609, LINC00880, LINC00894, LINC01088, LINC01091, LINC01094, LINC01602, LINC02018, LINC02055
  - [47]: lncRNAs influence transcription factor activity and chromatin accessibility at target loci

**Atomic cellular components**
- lncRNA-microRNA-mRNA regulatory networks. Genes: RMST, LINC00271, LINC00609, LINC00880, LINC00894, LINC01088, LINC01091, LINC01094, LINC01602, LINC02018, LINC02055
  - [47]: lncRNAs function as competing endogenous RNAs modulating microRNA activity

**Required genes (not in input)**
- Genes: DICER1, DROSHA, AGO2, LIN28
  - [47]: microRNA processing and RISC machinery required for lncRNA-miRNA-mRNA regulatory networks

**Program citations**
- [47]: lncRNAs regulate cancer metabolism through glycolytic enzyme and transcription factor modulation
- [48]: VIM-AS1 lncRNA modulates WEE1 to control cell proliferation and checkpoint function in gliomas

## Program: Astrocyte Activation and Reactive Gliosis Program
Genes controlling astrocyte activation responses, including acute pro-inflammatory, subacute transitional, and chronic neurodegenerative states. This program orchestrates how astrocytes respond to injury, infection, or tumor-associated signals. In astrocytoma contexts, dysregulation of astrocyte activation programs could either promote tumor progression (through immunosuppression and altered metabolic support) or impair anti-tumor responses (through loss of normal homeostatic astrocyte functions).

**Predicted impacts**
- Altered astrocyte contribution to tumor microenvironment through dysregulated activation states
- Enhanced or impaired pro-inflammatory responses affecting immune cell recruitment
- Disrupted neuroprotective astrocytic functions in chronic tumor settings
- Potential locking of tumor-associated astrocytes in particular activation states
- Altered metabolic support to tumor cells through activation state-dependent metabolite provision

**Evidence summary**
Recent comprehensive RNA-sequencing of astrocytes isolated at acute, subacute, and chronic timepoints following traumatic brain injury reveals dynamically evolving astrocyte transcriptomes. Acute activation (2 days post-injury) features a distinct pro-inflammatory signature with 2,588 differentially regulated transcripts (P adj < 0.05). Upregulated genes include pro-inflammatory cytokines (TNF, IL-1β, IL-17rc), chemokines (CCL2, CXCL10), and immediate early genes (Junb, Egr1). At 2 weeks (subacute phase), most acute inflammatory genes showed reduced expression while astrocytes upregulated regulatory and homeostatic pathways including synaptic regulation, axonogenesis, and neuronal stem cell maintenance. Chronic-phase astrocytes (1 year post-injury) maintained low-level pro-inflammatory signaling but prominently upregulated neurodegenerative pathways including mitochondrial and neuronal apoptotic pathways. Notably, chronic-phase astrocytes showed increased Ndrg1 (highly expressed in brain tumors including astrocytoma and glioblastoma) and decreased Rbpj (whose deletion promotes neurogenesis), suggesting persistent stress and aberrant activation. While this program is insufficiently represented by genes from the input list, understanding astrocyte activation dynamics is critical to comprehending how astrocytomas co-opt or dysregulate normal astrocytic responses.

**Atomic biological processes**
- Pro-inflammatory transcriptional activation and cytokine production.
  - [39]: Acute astrocyte activation features pro-inflammatory transcriptome with upregulation of TNF, IL-1β, IL-17rc, Ccl2, Cxcl10 and immediate early genes Junb, Egr1
- Transition from inflammation to neurodegeneration.
  - [39]: Subacute phase shows persistent low-level pro-inflammatory signaling; upregulation of regulatory and homeostatic pathways
- Synaptic pruning and neuronal apoptotic pathways.
  - [39]: Subacute and chronic phases feature upregulation of synapse pruning mediators (Sparc, Mertk, C1q) and neuronal apoptotic pathways

**Atomic cellular components**
- Astrocytic activation state-specific gene expression signatures.
  - [39]: Distinct transcriptional signatures associated with A1-like (pro-inflammatory) and A2-like (pro-healing) astrocyte states

**Required genes (not in input)**
- Genes: TNF, IL1B, IL17RC, CCL2, CXCL10, GFAP, VIM, S100B, AQP4
  - [39]: Multiple inflammatory cytokines, chemokines, and astrocytic markers essential for characterizing activation states

**Program citations**
- [39]: Comprehensive RNA-seq of astrocytes reveals dynamically evolving activation states from acute to chronic phases

## Program: Cell Adhesion and Extracellular Matrix Interactions
Genes governing cell adhesion, extracellular matrix composition, and cellular interactions within the tumor microenvironment. This program determines how astrocytic tumor cells interface with pericytes, endothelial cells, immune cells, and the surrounding ECM. Dysregulation alters invasion, angiogenesis, immune suppression, and blood-brain barrier integrity characteristic of astrocytoma.

**Predicted impacts**
- Dysregulated tumor-stromal interactions affecting pericyte coverage and blood-brain barrier integrity
- Enhanced tumor cell invasion through altered ECM signaling
- Increased immune suppression through altered pericyte-immune cell interactions
- Enhanced angiogenesis and abnormal vasculature characteristic of astrocytoma
- Altered spatial organization of tumor microenvironment into distinct niches

**Evidence summary**
The cohort includes genes encoding adhesion molecules and ECM-interacting proteins (PLEKHA5, PLEKHA7 encoding pleckstrin homology domain containing proteins; PTPRQ encoding protein tyrosine phosphatase receptor Q). Recent spatial transcriptomic studies reveal that glioblastomas contain nearly 400 differentially expressed ECM genes compared to normal brain, with distinct expression patterns in different tumor cell populations and stromal cells. Vascular endothelial cells and microglia/macrophages show largely non-overlapping ECM expression signatures, creating spatially distinct microenvironmental niches. Critically, pericytes orchestrate tumor-restraining microenvironments: pericyte depletion through genetic engineering results in both accelerated tumor progression and significantly shortened survival. Pericyte-deficient tumors show dysregulated vessel growth, reduced blood-brain barrier patency, increased tumor cell vessel co-option, altered endothelial cell signaling, and increased abundance of immune-suppressive macrophages expressing IL4-induced markers (Retnla, Ccl24, Mrc1, Arg1, Klf4). This demonstrates that ECM-mediated interactions between tumor cells and stromal components fundamentally shape astrocytoma progression.

**Atomic biological processes**
- Cell-cell adhesion and contact-dependent signaling. Genes: PLEKHA5, PLEKHA7, PTPRQ
  - [24]: Pericyte-astrocyte interactions dampen immune cell polarization; pericyte depletion results in increased abundance of immune-suppressive macrophages
  - [40]: Pericytes orchestrate tumor-restraining microenvironment; depletion accelerates tumor progression
- Extracellular matrix composition and remodeling. Genes: PLEKHA5, PLEKHA7, PTPRQ
  - [42]: Spatial transcriptomics reveals nearly 400 ECM genes dysregulated in GBM; differential ECM expression in vascular endothelial cells and microglia/macrophages

**Atomic cellular components**
- Cell adhesion molecule complexes and focal adhesions. Genes: PLEKHA5, PLEKHA7, PTPRQ
  - [24]: Pericyte-endothelial cell interactions altered by pericyte depletion; dysregulated vessel growth and BBB integrity
- Extracellular matrix protein networks and spatial organization. Genes: PLEKHA5, PLEKHA7, PTPRQ
  - [42]: Spatial heterogeneity in ECM composition creates distinct tumor microenvironmental niches

**Required genes (not in input)**
- Genes: CDH1, CDH2, ICAM1, NCAM1, LAMININ, COLLAGEN, FIBRONECTIN
  - [42]: Classical cell adhesion molecules and ECM proteins required for microenvironment interactions

**Program citations**
- [24]: Pericytes suppress immune polarization toward suppressive phenotypes; depletion accelerates tumor progression
- [40]: Pericyte depletion results in dysregulated vasculature and increased immune suppression
- [42]: Spatial transcriptomics reveals ECM heterogeneity and distinct stromal-tumor niches

## Program: Developmental Plasticity and Multicellular Progenitor Fate Specification
An integrative meta-program unifying the centrosome asymmetry, endosomal trafficking, microtubule organization, transcriptional control, and ciliary signaling programs described above. This program collectively determines whether RGPs self-renew symmetrically or undergo asymmetric division producing differentiated progeny. In normal development, this program maintains developmental plasticity while constraining proliferation. In astrocytoma, dysregulation unlocks proliferative potential while eliminating differentiation constraints, driving malignant transformation.

**Predicted impacts**
- Fundamental alteration of RGP proliferative capacity and differentiation potential
- Loss of developmental constraints normally limiting progenitor expansion
- Acquisition of symmetric self-renewing phenotype characteristic of cancer stem cells
- Enhanced susceptibility to oncogenic transformation through loss of developmental plasticity controls
- Potential acquisition of multipotent progenitor characteristics in tumor cells
- Disrupted developmental timing creating temporal dysregulation of proliferation and differentiation

**Evidence summary**
The collective evidence from multiple interconnected programs demonstrates that developmental plasticity in radial glia progenitors depends on proper functioning of an integrated system including centrosome asymmetry (PCM1, CCDC proteins), endosomal trafficking (PARD3B, DYNLRB2), microtubule organization (TUBA1A, TTLL9, PACRG), ciliary signaling (DNAH, DNAI, radial spoke proteins), and transcriptional control (SOX5). Loss or dysregulation of multiple components simultaneously would fundamentally alter RGP biology, potentially unlocking proliferative potential while simultaneously eliminating developmental constraints that normally drive differentiation. The evidence that pcm1 loss increases differentiating divisions (N/N) suggests that acute loss of centrosome asymmetry programs initially promotes differentiation. However, if such dysregulation occurs in RGPs that have simultaneously acquired TP53 loss or other oncogenic mutations preventing differentiation, the result would be proliferation-prone cells resistant to developmental signals—precisely the phenotype of astrocytoma. This integrative program likely represents the fundamental developmental plasticity mechanism that becomes dysregulated during astrocytoma initiation and that astrocytomas retain to enable adaptive plasticity during progression.

**Atomic biological processes**
- Asymmetric cell division and progenitor-differentiation fate specification. Genes: CCDC30, CCDC40, CCDC146, CCDC170, PARD3B, DYNLRB2, SOX5, TUBA1A, TTLL9, PACRG
  - [33]: PCM1-mediated centrosome asymmetry controls RGP division mode distribution (P/P vs. P/N vs. N/N); loss of pcm1 increases N/N divisions from 19% to 49%
  - [22]: Injury-responsive enhancers govern glial cell transcriptional reprogramming; unique and shared programs in different glial types
- Developmental signal integration through primary cilia. Genes: DNAH5, DNAH6, DNAH7, DNAH9, DNAH11, DNAH12, DNAI1, DNAAF1, ROPN1L, DRC1, DRC7, CFAP46, CFAP47, CFAP52, CFAP54, CFAP57, CFAP61
  - [33]: Primary cilia seed by mother centrosome; ciliary dynamics regulate developmental signal reception
  - [36]: Ciliary activities essential for polarized radial glial scaffold formation
- Developmental timing and cell cycle pace setting. Genes: TUBA1A, TTLL9
  - [36]: DNA replication fork speed acts as pacer controlling developmental timing in cortical neurogenesis

**Atomic cellular components**
- Integrated asymmetric cell division apparatus. Genes: CCDC30, CCDC40, CCDC146, CCDC170, PARD3B, DYNLRB2, TUBA1A, TTLL9, PACRG
  - [33]: PCM1-Par-3 complexes on Dld endosomes; asymmetric microtubule organization around centrosomes; differential centrosome inheritance
- Developmental signal transduction complexes. Genes: SOX5
  - [22]: Injury-responsive enhancers contain binding sites for lineage-specific and stimulus-induced transcription factors

**Required genes (not in input)**
- Genes: NOTCH1, JAG1, DLL1, HES1, NGN2, BDNF, GDNF
  - [22]: Notch signaling and developmental neurotrophic factors required for complete developmental plasticity control
  - [36]: Multiple developmental signaling pathways coordinate timing and fate specification

**Program citations**
- [33]: PCM1 integrates centrosome asymmetry with endosomal trafficking and cell fate specification in RGPs
- [22]: Injury-responsive enhancers coordinate glial cell transcriptional programs reflecting cell-type identity
- [36]: DNA replication dynamics pace developmental timing in cortical development

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
2. Available from: https://www.ncbi.nlm.nih.gov/gene/207
3. Available from: https://www.ncbi.nlm.nih.gov/gene/627
4. Available from: https://www.ncbi.nlm.nih.gov/gene/4763
5. Available from: https://www.ncbi.nlm.nih.gov/gene/5817
6. Available from: https://www.ncbi.nlm.nih.gov/gene/5133
7. Available from: https://www.ncbi.nlm.nih.gov/gene/3832
8. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
9. Available from: https://www.ncbi.nlm.nih.gov/gene/4867
10. Available from: https://www.ncbi.nlm.nih.gov/gene/80184
11. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
12. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
13. Philipp K, Jacob SY, Maarten MJW, Tommaso S, Nico T, Alba C, et al.. A prognostic classification system for extent of resection in IDH-mutant grade 2 glioma: an international, multicentre, retrospective cohort study with external validation by the RANO resect group.. The Lancet Oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41308678/
14. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
15. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/43590/
16. Lara N, Javier M, Irene S-S, Moisés S-P, Esther R-S, Teresa S-M. Next-Generation Sequencing Reveals a Diagnostic and Prognostic Role of the . International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41373636/?fc=None&ff=20251211105245&v=2.18.0.post22+67771e2
17. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
18. Available from: https://www.ncbi.nlm.nih.gov/gene/7161
19. Available from: https://www.ncbi.nlm.nih.gov/gene/6660
20. Available from: https://www.ncbi.nlm.nih.gov/gene/4582
21. Pietramale AN, Bame X, Doty ME, Schwarz KE, Hill RA. Mitochondria are absent from microglial processes performing surveillance, chemotaxis, and phagocytic engulfment. Nature Communications [Internet]. 2025Dec12;16(1). Available from: https://www.nature.com/articles/s41467-025-66708-6
22. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
23. Available from: https://www.ncbi.nlm.nih.gov/gene/3064
24. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
25. Han Y, Han M, Wang T, Zhang H, Liu H, Zheng Y, et al.. Inhibiting the formation of neutrophil extracellular traps to prevent the recurrence of post-operative glioblastoma. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-65933-3
26. Available from: https://www.ncbi.nlm.nih.gov/gene/6103
27. Available from: https://www.ncbi.nlm.nih.gov/gene/4804
28. Available from: https://www.ncbi.nlm.nih.gov/gene/57096
29. Available from: https://www.ncbi.nlm.nih.gov/gene/24842
30. Available from: https://www.ncbi.nlm.nih.gov/gene/12803
31. Zhao X, Mouilleau V, Wang Y, Solak AC, Garcia JQ, Chen X, et al.. PCM1 coordinates centrosome asymmetry with polarized endosome dynamics to regulate daughter cell fate. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-65756-2
32. Available from: https://www.ncbi.nlm.nih.gov/gene/1270
33. Wang J, Kong Y, Li X, Chen D, Xiang K, Tan Y, et al.. DNA replication fork speed acts as a pacer in cortical neurogenesis. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65269-y
34. Available from: https://www.ncbi.nlm.nih.gov/gene/4313
35. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
36. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
37. Christina P, Olympia A, Konstantina C, Anastasios K, Sofia D, Martina S, et al.. Dysregulated proteostasis in p.A53T-α-Synuclein astrocytes aggravates Lewy-like neuropathology in a Parkinson's disease iPSC model.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41248289/
38. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
39. Available from: https://www.ncbi.nlm.nih.gov/gene/991
40. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z
41. Ren Y, Zhang Z, Lei X, Shi L. Long non-coding RNAs in cancer glycolysis and metabolism: mechanisms and translational opportunities. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08289-2
42. Available from: https://www.ncbi.nlm.nih.gov/gene/7465
43. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z_reference.pdf
44. Available from: http://json-schema.org/draft-07/schema#",
