# Gene Program Markdown Report

## Context
- Cell type: Astrocyte
- Disease: Astrocytoma
- Tissue: Central nervous system (brain)

## Input Genes
ID4, DOCK7, LIFR, ANKFN1, GLIS3, ARHGEF26-AS1, DCLK1, MIR99AHG, ADCY2, SORBS1, RNF19A, PARD3B, GRAMD2B, DCLK2, GFAP, WLS, ABLIM1, TNIK, AC093535.1, BMPR1B, NTRK2, RFX4, PACRG, NKAIN3, LHFPL6, ... (200 total)

## Program: Astrocyte Identity and Reactive Gliosis
Establishes astrocyte lineage commitment and reactive phenotype through coordinated expression of structural proteins, glial fibrillary acidic protein (GFAP), vimentin (VIM), and aldehyde dehydrogenase 1 family member L1 (ALDH1L1) that characterize mature reactive astrocytes. This program encompasses transcriptional control through inhibitors of DNA binding (ID3, ID4) and involves aquaporin-4 (AQP4) for water homeostasis and process dynamics. Reactive astrocytes upregulate GFAP and extend hypertrophic, arborized processes forming glial barriers that insulate injury sites and disease lesions from healthy tissue, representing a coordinated transcriptional reprogramming that both maintains astrocyte identity and drives the transformation from resting to reactive state.

**Predicted impacts**
- Enhanced process morphogenesis and hypertrophic astrocyte transformation
- Establishment of reactive astrocyte transcriptional signature
- Altered water homeostasis and osmotic balance in tumor astrocytes
- Shift from quiescent to activated cellular state with sustained gene expression

**Evidence summary**
GFAP, VIM, and ALDH1L1 comprise the molecular signature of mature reactive astrocytes, a state persistently activated in both injury and disease contexts including astrocytoma. In traumatic brain injury models, astrocyte activation persists for extended periods with sustained GFAP and VIM expression even one year post-injury, suggesting that reactive states become entrenched and difficult to resolve. The transcriptional regulators ID3 and ID4 control whether astrocytes remain proliferative or undergo terminal differentiation, with dysregulation potentially promoting malignant transformation. AQP4 and AQP4-AS1 coordinate astrocyte water homeostasis, a process essential for maintaining osmotic balance during process extension and retraction. In astrocytoma, this program likely establishes and maintains a reactive astrocyte identity while simultaneously preventing differentiation and promoting proliferation through dysregulated ID protein signaling.

**Atomic biological processes**
- Intermediate filament dynamics and astrocyte morphogenesis. Genes: GFAP, VIM, ALDH1L1
  - [2]: GFAP and VIM upregulation characterizes reactive astrocytes with extension of hypertrophic, arborized processes
  - [5]: GFAP, VIM, S100B, and Sox9 expression patterns distinguish reactive astrocyte morphology during TBI recovery
  - [14]: GFAP upregulation and VIM expression mark reactive astrocyte activation across acute to chronic TBI phases
- Transcriptional regulation of astrocyte differentiation and proliferation. Genes: ID3, ID4
  - [3]: ID4 acts as tumor suppressor in myeloid malignancies with potential for similar role in astrocytoma
  - [6]: ID3 modulates cell differentiation and functions as target of p53 with anti-tumor properties
- Water homeostasis and osmotic regulation. Genes: AQP4-AS1
  - [2]: Aquaporin-4 supports astrocyte water homeostasis essential for process dynamics
  - [5]: AQP4-related signaling dysregulated in chronic TBI astrocytes

**Atomic cellular components**
- Intermediate filament cytoskeleton. Genes: GFAP, VIM
  - [2]: GFAP and intermediate filaments form the structural basis of reactive astrocyte processes

**Required genes (not in input)**
- Genes: S100B, SOX9, EAAT1, GLT1
  - [5]: S100B and SOX9 mark astrocyte identity but absent from input list
  - [14]: Core astrocyte markers including S100B essential for reactive gliosis but not in input

**Program citations**
- [2]: Plexin-B1 work demonstrates reactive astrocytes characterized by GFAP upregulation and extended hypertrophic processes
- [5]: Comprehensive transcriptional analysis of astrocytes shows persistent activation from acute to chronic TBI with sustained GFAP, VIM, S100B expression
- [14]: Extended study confirms astrocyte activation persists one year after TBI with maintained reactive phenotype
- [3]: ID4 identified as tumor suppressor with methylation as potential biomarker
- [6]: ID3 functions as anti-tumor factor in various malignancies

## Program: Lipid Metabolism and Apolipoprotein Homeostasis
Regulates lipid synthesis, transport, and metabolism essential for maintaining neuronal health and modulating inflammatory responses. This program centers on apolipoprotein E (APOE) as the primary central nervous system source of lipid distribution, with supporting genes controlling cholesterol efflux (ABCA1), lipid transfer proteins (PLTP), lipoprotein assembly (CLU), and polyunsaturated fatty acid synthesis (FADS2). Astrocytes serve as primary producers of APOE, establishing them as critical regulators of lipid homeostasis affecting neuronal membrane composition, myelin formation, and vulnerability to amyloid-beta accumulation and neurodegeneration. Dysregulation of this program in astrocytoma may impair normal astrocyte-neuron lipid exchange while promoting altered metabolic states supporting tumor growth.

**Predicted impacts**
- Altered amyloid-beta clearance capacity through deficient ApoE lipidation
- Impaired cholesterol efflux and reduced astrocyte-neuron lipid exchange
- Enhanced metabolic adaptations supporting tumor cell growth
- Modified neuroinflammatory responses through altered lipid-mediated signaling

**Evidence summary**
APOE functions as the master regulator of lipid homeostasis in the CNS, with astrocytes serving as primary producers. The APOE ε4 allele, strongly associated with Alzheimer's disease risk, impairs normal lipid shuttling between astrocytes and neurons, leading to deficient amyloid-beta clearance and exacerbated pro-inflammatory responses. Recent work demonstrates that dysregulation of microRNA-33 increases in AD patients and animal models, with miR-33 dysregulation impairing ABCA1 expression and thereby reducing cholesterol efflux capacity. CRISPR-mediated targeting of miR-33 in astrocytes restores ApoE lipidation and ameliorates amyloid-beta burden both in vitro and in vivo, indicating that lipid metabolism dysregulation directly contributes to neurodegeneration. In astrocytoma context, dysregulation of this program may reflect both tumor cell-autonomous adaptations and impaired capacity to support normal neuronal lipid homeostasis, potentially contributing to peritumoral neurodegeneration and altered immune signaling.

**Atomic biological processes**
- Apolipoprotein E synthesis and lipidation. Genes: APOE
  - [8]: APOE ε4 increases amyloid-β burden through reduced clearance and altered lipid homeostasis
  - [10]: CRISPR targeting of miR-33 restores ApoE lipidation in astrocytes, ameliorating Alzheimer's disease pathology
- Cholesterol efflux and ABCA1-mediated lipid transport. Genes: ABCA1
  - [30]: ABCA1 required for cholesterol efflux and ApoE lipidation; reduced ABCA1 in amyloid-beta-induced reactive astrocytes impairs lipid transport
  - [32]: ABCA1 functions in generating high-density lipoprotein through ApoA-I lipidation
- Lipid transfer and lipoprotein remodeling. Genes: PLTP, CLU
  - [8]: APOE ε4 impairs lipid shuttling between astroglia and neurons through disrupted lipid metabolism
  - [10]: PLTP-mediated lipid transfer essential for maintaining ApoE functionality
- Polyunsaturated fatty acid synthesis. Genes: FADS2
  - [8]: FADS2 catalyzes formation of polyunsaturated fatty acids critical for membrane composition

**Atomic cellular components**
- Lipoprotein particles and lipid transport vesicles. Genes: APOE, ABCA1, PLTP, CLU
  - [10]: CRISPR-mediated miR-33 targeting enables ApoE lipidation and functional lipoprotein assembly

**Required genes (not in input)**
- Genes: APOA1, APOB, LDLR, CETP
  - [10]: Other apolipoproteins and lipid transfer factors participate in CNS lipid homeostasis

**Program citations**
- [8]: Comprehensive analysis of APOE ε4 interaction with tau pathology and astrocyte reactivity
- [10]: Novel CRISPR-based therapeutic approach targeting miR-33 in astrocytes for AD pathology
- [30]: ABCA1 reduction in reactive astrocytes impairs cholesterol efflux capacity

## Program: Glutamate Homeostasis and Ion Regulation
Maintains extracellular glutamate within physiological ranges through coordinated action of glutamate transporters (SLC1A3 encoding EAAT2/GLT-1) and aquaporin-4 (AQP4), supported by ion channel and transporter genes enabling sodium, potassium, and chloride homeostasis. This program couples glutamate uptake to ATP-dependent ion pumping through Na+/K+-ATPase (ATP1B2) and regulates intracellular pH and osmotic balance through sodium-bicarbonate cotransporter (SLC4A4). Dysregulation of glutamate homeostasis in astrocytoma, particularly in peritumoral regions, impairs glutamate clearance capacity and contributes to neuronal excitotoxicity, abnormal network activity, and seizure susceptibility.

**Predicted impacts**
- Impaired glutamate clearance capacity in peritumoral regions
- Dysregulated ion homeostasis supporting pathological neuronal hyperexcitability
- Altered osmotic regulation and water transport dynamics
- Enhanced susceptibility to glutamate-mediated excitotoxicity and seizure generation

**Evidence summary**
SLC1A3 encodes the primary astrocytic glutamate transporter EAAT2/GLT-1, which maintains extracellular glutamate within physiological ranges critical for preventing excitotoxic neuronal injury. Dysregulation of glutamate transport contributes to multiple CNS pathologies including astrocytoma, where peritumoral glioma cells directly impair glutamate reuptake through alterations in transporter expression and function. Recent work demonstrates that glioma cells promote elevation of local glutamate concentration and alter neuronal excitability through both impaired glutamate reuptake and aberrant xCT transporter system activation, establishing glutamate dyshomeostasis as a key mechanism of tumor-associated seizures. Ion homeostasis pathways including potassium channels (KCNQ5, KCNN3) and the Na+/K+-ATPase (ATP1B2) function in generating electrochemical gradients that drive glutamate uptake, suggesting that dysregulation of multiple ion channels collectively impairs glutamate homeostasis. In astrocytoma context, this program likely undergoes comprehensive dysregulation that contributes to peritumoral hyperexcitability and seizure susceptibility.

**Atomic biological processes**
- Glutamate transporter-mediated uptake and recycling. Genes: SLC1A3
  - [15]: SLC1A3 encodes GLT1, the primary astrocytic glutamate transporter regulating extracellular glutamate concentration
  - [17]: SLC1A2 encodes EAAT2, functionally coupled to neuronal protection through glutamate clearance
  - [26]: Glioma cells impair local glutamate reuptake through alterations in transporter function
- Water and osmotic homeostasis coupled to glutamate transport. Genes: AQP4-AS1
  - [2]: AQP4 functions in water homeostasis coupled to glutamate transport dynamics
- Ion homeostasis and electrochemical gradient maintenance. Genes: ATP1B2, SLC4A4, KCNQ5, KCNN3, SLC16A9, SLC14A1
  - [15]: Ion homeostasis through potassium and sodium channels required for glutamate uptake function
  - [26]: Peritumoral hyperexcitability involves dysregulation of ion homeostasis pathways
- pH regulation and intracellular acidification. Genes: SLC4A4
  - [15]: Sodium-bicarbonate cotransporter regulates intracellular pH essential for maintaining astrocyte excitability
- Glutamate receptor signaling and synaptic responses. Genes: GRIK1
  - [26]: GRIN1-mediated NMDA signaling participates in neuronal responses to glutamate
  - [29]: GRIN1 expression in neuronal networks, downstream of astrocytic glutamate clearance

**Atomic cellular components**
- Glutamate transporter protein complexes. Genes: SLC1A3
  - [15]: SLC1A3/GLT-1 comprises the primary astrocytic glutamate uptake machinery
- Ion channel and transporter assemblies. Genes: KCNQ5, KCNN3, ATP1B2, SLC4A4
  - [15]: Multiple ion channels and transporters coordinate ion homeostasis

**Required genes (not in input)**
- Genes: GLAST, GLT1, KCCN1, KCCN3
  - [15]: GLAST and GLT1 represent functionally distinct glutamate transporters

**Program citations**
- [15]: SLC1A3 and EAAT2 function in glutamate transporter biology
- [17]: Astrocytic transcription factor REST upregulates EAAT2 for neuroprotection
- [26]: Glioma-associated peritumoral hyperexcitability linked to glutamate dyshomeostasis

## Program: Neurotrophic Signaling and Neuronal Support
Establishes astrocyte-mediated neuronal support through expression of neurotrophic factors and their receptors, including brain-derived neurotrophic factor signaling through NTRK2 (TrkB receptor). This program supports neuronal survival, growth, differentiation, and synaptic plasticity through coordinated secretion of trophic factors and receptors for axon guidance molecules including RGMA, SEMA6A, and NRG3. In normal astrocytes, this program maintains neuronal health and facilitates neuronal network function, whereas dysregulation in astrocytoma contributes to aberrant signaling and oncogenic transformation through potential fusion events affecting NTRK2.

**Predicted impacts**
- Enhanced neuronal survival and growth in normal contexts
- Dysregulated NTRK2 signaling supporting tumor cell proliferation through oncogenic fusion events
- Aberrant axon guidance affecting peritumoral circuit organization
- Altered neuronal-glial communication through dysregulated trophic signaling

**Evidence summary**
NTRK2 encodes the TrkB receptor for brain-derived neurotrophic factor, a key neurotrophic factor supporting neuronal survival, plasticity, and synaptic function. In normal astrocytes, NTRK2 signaling participates in supporting neuronal development and function. However, recent work identifies NTRK2 as a participant in oncogenic fusion events in certain astrocytomas, with TRIM24::NTRK2 fusion genes generating constitutively active receptor tyrosine kinases. These fusion proteins activate MAPK, PI3K, and JAK/STAT pathways, driving proliferation of tumor astrocytes. TRIM24::NTRK2 fusion shows highest activation in PI3K pathway signaling and MAPK/PI3K downstream effector pS6, suggesting robust oncogenic signaling. Axon guidance molecules including RGMA and SEMA6A function in restricting axon growth, with dysregulation in astrocytoma potentially contributing to aberrant network organization within peritumoral regions. NRG3 participates in ErbB receptor signaling supporting neuronal development and myelination, with dysregulation likely impairing normal supportive functions.

**Atomic biological processes**
- BDNF signaling through NTRK2/TrkB receptor. Genes: NTRK2
  - [12]: BDNF from microglia regulates neuronal development through TrkB signaling
  - [13]: BDNF supports neuronal development and plasticity through TrkB in multiple brain regions
  - [25]: NTRK2 participates in oncogenic fusion events in astrocytoma, generating constitutively active receptors
- Axon guidance signaling. Genes: RGMA, SEMA6A
  - [26]: RGMA suppresses axon regeneration while SEMA6A serves as neurite outgrowth inhibitor affecting network organization
- Neuregulin signaling and ErbB receptor activation. Genes: NRG3
  - [26]: NRG3 participates in ErbB receptor signaling supporting neuronal development and myelination

**Atomic cellular components**
- Tropomyosin receptor kinase B signaling complexes. Genes: NTRK2
  - [25]: TRIM24::NTRK2 fusion generates constitutively active receptor tyrosine kinase activating MAPK, PI3K, and JAK/STAT pathways

**Required genes (not in input)**
- Genes: BDNF, GDNF, NGF, NTNT3
  - [12]: BDNF represents primary neurotrophin acting through NTRK2
  - [13]: Multiple neurotrophins support neuronal development and survival

**Program citations**
- [25]: NTRK2 fusion events in astrocytoma generating oncogenic drivers
- [26]: Axon guidance molecules dysregulated in tumor contexts
- [12]: BDNF and TrkB signaling in neuronal development

## Program: Cell Adhesion and Polarity Protein Organization
Establishes and maintains cell-cell contacts, tissue organization, and cell polarity through coordinated expression of classical cadherins (CDH11), polarity protein complexes (PARD3, PARD3B), gap junction proteins (GJA1), and focal adhesion components (VCL). This program organizes astrocyte spatial relationships, supports astrocyte-neuron interactions, and enables polarized astrocyte architecture. Dysregulation of polarity proteins in astrocytoma impairs normal astrocyte tiling, disrupts gap junction communication, and facilitates enhanced migratory capacity through loss of adhesive constraints.

**Predicted impacts**
- Impaired cell-cell adhesion and tissue organization in tumor astrocytes
- Disrupted astrocyte-astrocyte communication through gap junction dysfunction
- Loss of cell polarity constraints facilitating enhanced migration and invasion
- Dysregulated mechanotransduction through altered focal adhesion dynamics
- Reduced adhesive constraints supporting malignant transformation

**Evidence summary**
Cell adhesion and polarity proteins establish and maintain tissue organization through coordinated cell-cell contacts. CDH11, encoding cadherin-11, mediates homophilic adhesion particularly in neural tissues where it supports synaptic organization and astrocyte-neuron interactions. PARD3 and PARD3B encode core components of the PAR (partitioning defective) polarity complex, which establishes cell polarity through asymmetric protein distribution. Recent work reveals striking decline in PAR complex protein expression during malignant transformation, with polarity disruption emerging as an early central molecular event in tumorigenesis and oral squamous cell carcinoma. This suggests that dysregulation of PARD3/PARD3B may similarly drive astrocytoma development and progression by relieving polarity constraints. GJA1 encodes connexin-43, which forms gap junctions enabling direct communication between astrocytes through passage of small molecules and ions. Dysregulation of gap junction function in astrocytoma likely disrupts coordinated astrocyte responses and impairs communication between tumor astrocytes and surrounding tissue. VCL/vinculin functions in focal adhesions linking cytoskeleton to surface adhesion molecules, with changes in vinculin localization reflecting altered mechanotransduction and cell migration capacity.

**Atomic biological processes**
- Cadherin-mediated homophilic cell adhesion. Genes: CDH11
  - [40]: CDH11 mediates homophilic cell-cell adhesion in neurons and astrocytes, supporting tissue organization
- PAR complex polarity protein signaling. Genes: PARD3, PARD3B
  - [40]: PARD3 and PARD3B encode PAR complex components; striking decline in polarity protein expression during malignant transformation
- Gap junction and direct cell-cell communication. Genes: GJA1
  - [2]: GJA1/Cx43 forms gap junctions enabling direct astrocyte-astrocyte communication
  - [38]: GJA1 encodes connexin-43, a component of gap junction intercellular channels
- Focal adhesion assembly and mechanotransduction. Genes: VCL
  - [2]: VCL/vinculin links actin cytoskeleton to membrane-localized adhesion molecules enabling force transduction

**Atomic cellular components**
- Adherens junction and cadherin-catenin complexes. Genes: CDH11
  - [40]: CDH11 participates in adherens junction complexes organizing tissue structure
- PAR polarity complex. Genes: PARD3, PARD3B
  - [40]: PARD3 and PARD3B comprise core components of PAR complex regulating cell polarity
- Gap junction channel structures. Genes: GJA1
  - [38]: GJA1/connexin-43 forms intercellular channel arrays comprising gap junctions
- Focal adhesion plaques. Genes: VCL
  - [2]: VCL localizes to focal adhesions linking cytoskeleton to cell surface

**Required genes (not in input)**
- Genes: CDH2, SCRIBBLE, DLG, CTNNB1
  - [40]: Additional polarity and adhesion proteins including SCRIBBLE and DLG regulate cell polarity

**Program citations**
- [40]: Comprehensive analysis of polarity protein dysregulation during malignant transformation
- [38]: GJA1 functions in gap junction formation and direct cell communication
- [2]: VCL and focal adhesion dynamics in reactive astrocytes

## Program: Cytoskeletal Dynamics and Astrocyte Process Morphology
Coordinates microtubule and actin filament dynamics enabling astrocyte process extension, retraction, and spatial organization through coordinated action of doublecortin-like kinases (DCLK1, DCLK2), Rho family GTPase regulators (DOCK7, ARHGEF26, ARHGEF4), dynein motors (DNAH7), and associated cytoskeletal proteins including talin (TLN2), dystrophin (DMD), and ARP-interacting proteins (ABLIM1). This program maintains astrocyte morphological complexity and plasticity essential for establishing intimate contacts with synapses and vasculature. Dysregulation of cytoskeletal dynamics in astrocytoma impairs normal process organization and enables enhanced migratory and invasive capacity.

**Predicted impacts**
- Enhanced process extension and retraction dynamics
- Altered spatial organization and process alignment relative to neurons
- Increased migratory capacity through dysregulated Rho signaling
- Impaired ability to establish stable synaptic contacts
- Dysregulated mechanotransduction affecting response to microenvironmental cues

**Evidence summary**
Astrocyte processes undergo dynamic extension and retraction enabling elaborate network formation and intimate cellular contacts. DCLK1 and DCLK2 function as microtubule-associated proteins regulating microtubule dynamics and stabilization, promoting formation of stable microtubule arrays supporting process extension. DCLK1 marks immature neurons in neurogenic contexts, suggesting potential roles in regulating progenitor biology within astrocytoma. DOCK7, ARHGEF26, and ARHGEF4 encode guanine nucleotide exchange factors that activate Rho family GTPases (Rac1, Cdc42), master regulators of actin dynamics controlling process extension, retraction, and migration. Recent work demonstrates that Plexin-B1 safeguards astrocyte agility through regulation of astrocytic process dynamics, with Plexin-B1 deficiency promoting astrocyte clustering and misalignment relative to regenerating axons through altered membrane and endocytic dynamics. DNAH7 encodes axonemal dynein motor proteins, with recent evidence suggesting involvement of ciliary biology in astrocyte function and potential tumor suppression. TLN2 and VCL function in focal adhesions linking integrins to actin cytoskeleton, enabling mechanical force transduction and cell migration. DMD encodes dystrophin, which links actin to transmembrane proteins and extracellular matrix through associated protein complexes. Dysregulation of cytoskeletal programs in astrocytoma likely promotes enhanced migratory capacity while impairing normal spatial organization.

**Atomic biological processes**
- Microtubule polymerization and stabilization. Genes: DCLK1, DCLK2
  - [4]: DCLK1 and DCLK2 function as microtubule-associated proteins regulating stability
  - [28]: Microtubule dynamics regulate neural stem cell proliferation and neuronal development
- Rho family GTPase activation and actin dynamics. Genes: DOCK7, ARHGEF26, ARHGEF4
  - [2]: Rho GTPase signaling dynamically regulates astrocyte process plasticity through actin reorganization
- Axonemal motor function and ciliary dynamics. Genes: DNAH7
  - [28]: DNAH7 encodes axonemal dynein participating in ciliary and centrosomal function
- Focal adhesion assembly and cytoskeleton linkage. Genes: TLN2
  - [2]: TLN2/talin-2 and VCL/vinculin link integrins to actin cytoskeleton in focal adhesions
- Dystrophin-associated protein complex dynamics. Genes: DMD
  - [28]: DMD/dystrophin links actin to transmembrane proteins and extracellular matrix

**Atomic cellular components**
- Microtubule arrays and tubulin oligomers. Genes: DCLK1, DCLK2
  - [4]: DCLK proteins associate with microtubules regulating dynamics
- Actin filament networks and stress fibers. Genes: DOCK7, ARHGEF26, ARHGEF4
  - [2]: Rho GTPases regulate actin polymerization generating dynamic stress fiber networks
- Motor protein complexes. Genes: DNAH7
  - [28]: Dynein motor proteins transport cargo along microtubules
- Focal adhesion plaques. Genes: TLN2, VCL
  - [2]: TLN2 and VCL organize focal adhesion plaques linking to actin cytoskeleton
- Dystrophin-associated protein complexes. Genes: DMD
  - [28]: DMD links sarcolemmal proteins to cytoskeleton through associated proteins

**Required genes (not in input)**
- Genes: RAC1, CDC42, ARPC2, COFILIN
  - [2]: Rho family GTPases and actin depolymerizing factors regulate cytoskeleton dynamics

**Program citations**
- [2]: Plexin-B1 regulation of astrocytic process dynamics and membrane organization
- [28]: Comprehensive analysis of cytoskeletal dynamics in neural stem cells and neurogenesis

## Program: Transcriptional Control of Cell Fate and Proliferation
Regulates cell fate decisions determining astrocyte quiescence, activation, differentiation, or malignant transformation through coordinated action of transcription factors including forkhead box O1 (FOXO1), yes-associated protein 1 (YAP1), inhibitors of DNA binding (ID3, ID4), regulatory factor X proteins (RFX2, RFX4), and HES4. This program couples extracellular signals through signal transduction pathways to changes in gene expression programs controlling proliferation, differentiation, and survival decisions. Dysregulation of transcriptional control in astrocytoma promotes enhanced proliferation while preventing terminal differentiation and apoptosis.

**Predicted impacts**
- Dysregulated proliferation through YAP1 and ID protein signaling
- Impaired autophagy and stress responses through FOXO1 dysregulation
- Loss of differentiation capacity through ID protein overexpression
- Altered ciliogenesis and ciliary signaling through RFX dysregulation
- Enhanced tumor cell survival and reduced apoptosis

**Evidence summary**
FOXO1 functions as a tumor suppressor through multiple mechanisms including autophagy regulation, oxidative stress responses, and metabolic control. Dysregulation of FOXO1 in tumors promotes enhanced proliferation and reduced autophagic capacity. YAP1 serves as major effector of Hippo pathway signaling, a conserved kinase cascade regulating proliferation and differentiation. Loss of Hippo pathway signaling or increased YAP1 promotes proliferation and prevents differentiation, with YAP1 and TAZ showing differential regulatory roles in astrocyte biology. ID3 and ID4 inhibitors of DNA binding prevent differentiation programs while promoting proliferation through sequestration of bHLH transcription factors. ID4 acts as tumor suppressor in myeloid malignancies with methylation-mediated silencing as potential biomarker. RFX transcription factors regulate ciliogenesis and control transitions between proliferation and differentiation, with dysfunction potentially supporting tumorigenesis. HES4 participates in Notch pathway signaling regulating neural cell differentiation. Dysregulation of transcriptional control in astrocytoma collectively promotes proliferation while preventing terminal differentiation and apoptosis.

**Atomic biological processes**
- FOXO-mediated stress response and metabolic regulation. Genes: FOXO1
  - [22]: FOXO1 functions as metabolic regulator and tumor suppressor controlling autophagy and oxidative stress
  - [24]: Foxo1 regulates autophagy and cell survival in response to metabolic and oxidative stress
- Hippo pathway YAP1 signaling and proliferation control. Genes: YAP1
  - [18]: YAP1 and TAZ differentially regulate postnatal cortical progenitor proliferation and astrocyte differentiation
- ID protein regulation of bHLH transcription factors. Genes: ID3, ID4
  - [3]: ID4 acts as tumor suppressor with methylation as potential disease biomarker
  - [6]: ID3 functions as target of p53 with anti-tumor properties
- RFX transcription factor ciliogenesis control. Genes: RFX2, RFX4
  - [41]: RFX transcription factors regulate ciliogenesis and ciliary gene expression in context-specific differentiation
- Notch pathway effector HES4 signaling. Genes: HES4
  - [26]: HES family transcription factors regulate cell differentiation in neural lineages

**Atomic cellular components**
- FOXO transcription factor complexes. Genes: FOXO1
  - [22]: FOXO proteins form dimers and interact with cofactors in nucleus
- YAP1/TEAD transcriptional complexes. Genes: YAP1
  - [18]: YAP1 functions as Hippo pathway effector activating TEAD transcription factors
- ID protein-bHLH heterodimers. Genes: ID3, ID4
  - [3]: ID proteins form non-functional dimers with bHLH factors

**Required genes (not in input)**
- Genes: TEAD1, TEAD4, NOTCH1, JAG1
  - [18]: TEAD factors function as YAP transcriptional partners
  - [41]: Notch pathway components regulate neural cell differentiation

**Program citations**
- [22]: FOXO1 metabolic regulation and tumor suppressor functions
- [18]: YAP1/TAZ differential regulation of astrocyte differentiation
- [3]: ID4 tumor suppressor functions in myeloid malignancies
- [41]: RFX transcription factors in ciliogenesis and cell fate control

## Program: Metabolic Reprogramming and Bioenergetic Adaptation
Orchestrates metabolic adaptations supporting rapid tumor cell growth and biosynthesis through altered glucose metabolism, lipid synthesis, and energy production. This program includes adenylyl cyclases (ADCY2, ADCY8) regulating cAMP signaling, phosphodiesterases (PDE8A, PDE8B) modulating cAMP dynamics, and multiple genes regulating energy metabolism. Tumor astrocytes likely undergo Warburg effect-like metabolic reprogramming enhancing glycolytic flux while altering oxidative phosphorylation, changes coordinated through dysregulated second messenger signaling.

**Predicted impacts**
- Enhanced glycolytic flux supporting rapid biosynthesis
- Altered energy metabolism and ATP production
- Modified lipid synthesis supporting tumor cell growth
- Dysregulated cAMP signaling affecting metabolic rate

**Evidence summary**
Tumor cells typically undergo metabolic reprogramming toward enhanced glycolysis and altered lipid metabolism to support rapid growth, the Warburg effect. ADCY2 and ADCY8 encode adenylyl cyclases synthesizing cAMP, a second messenger regulating metabolic responses to extracellular signals. PDE8A and PDE8B encode phosphodiesterases degrading cAMP, with dysregulation of adenylyl cyclase and phosphodiesterase expression affecting cAMP signaling dynamics. FADS2 catalyzes polyunsaturated fatty acid synthesis essential for membrane biogenesis and lipid signaling during tumor growth. Dysregulation of metabolic programs likely collectively supports bioenergetic demands of astrocytic tumor growth through coordinated alterations in glucose, lipid, and amino acid metabolism.

**Atomic biological processes**
- cAMP synthesis and second messenger signaling. Genes: ADCY2, ADCY8
  - [26]: Adenylyl cyclases synthesize cAMP regulating metabolic responses to neurotransmitters
- cAMP degradation and signal termination. Genes: PDE8A, PDE8B
  - [14]: Phosphodiesterases terminate cAMP signaling cascades
- Polyunsaturated fatty acid synthesis and membrane biogenesis. Genes: FADS2
  - [8]: FADS2 catalyzes polyunsaturated fatty acid synthesis supporting membrane composition

**Atomic cellular components**
- Adenylyl cyclase catalytic complexes. Genes: ADCY2, ADCY8
  - [26]: ADCY proteins form membrane-associated catalytic complexes

**Required genes (not in input)**
- Genes: LDHA, PKM2, PFKFB3, ACC1
  - [26]: Glycolytic enzymes and lipid synthesis proteins required for metabolic reprogramming

**Program citations**
- [26]: Neurotransmitter signaling through adenylyl cyclase affecting metabolism
- [14]: Phosphodiesterase signaling in astrocyte biology
- [8]: FADS2 in polyunsaturated fatty acid metabolism

## Program: Extracellular Matrix Remodeling and Tissue Interactions
Coordinates dynamic remodeling of extracellular matrix surrounding astrocytes and neurons through expression of matrix components (COL28A1), fibulin-like proteins (EFEMP1, SPARCL1), matrix metalloproteinase inhibitors (TIMP3), and tenascin family proteins (TNC). This program supports matrix assembly during development and plasticity while dysregulation promotes matrix degradation facilitating tumor cell invasion and aberrant tissue interactions.

**Predicted impacts**
- Enhanced matrix degradation through dysregulated TIMP3 function
- Altered matrix composition affecting astrocyte-neuron interactions
- Facilitated tumor cell invasion through permissive matrix environment
- Dysregulated synapse pruning through altered matrix-associated signals

**Evidence summary**
The extracellular matrix undergoes dynamic remodeling during development, plasticity, and in response to injury and disease. EFEMP1 encodes fibulin-3 functioning in extracellular matrix organization and regulating cell migration and adhesion. TIMP3 serves as key inhibitor of matrix metalloproteinases supporting extracellular matrix integrity, with dysregulation promoting matrix degradation and enhanced invasion. In chronic-phase traumatic brain injury, genes involved in synapse pruning including SPARC, MERTK, and complement components are upregulated, suggesting activation of matrix-related pathways associated with neurodegeneration. SPARCL1 encodes SPARC-like protein-1 participating in matrix assembly and tissue remodeling. TNC encodes tenascin-C, a key modulator of cell adhesion and tissue remodeling with particular roles in nervous system development and plasticity. Recent work demonstrates that single-cell spatial transcriptomic analysis reveals changes in extracellular matrix gene expression between normal brain and glioblastoma, suggesting comprehensive dysregulation of matrix programs in astrocytic tumors. Dysregulation of extracellular matrix programs in astrocytoma likely reflects both protective matrix maintenance disruption and pathological matrix degradation associated with tumor invasion.

**Atomic biological processes**
- Matrix metalloproteinase regulation and inhibition. Genes: TIMP3
  - [14]: TIMP3 loss in reactive astrocytes associated with impaired recovery and neurodegenerative processes
- Extracellular matrix protein assembly. Genes: EFEMP1, SPARCL1, TNC
  - [14]: EFEMP1 and SPARCL1 function in extracellular matrix assembly and organization
- Collagen matrix composition and structure. Genes: COL28A1
  - [16]: Extracellular matrix gene expression differs between normal brain and glioblastoma

**Atomic cellular components**
- Extracellular matrix protein complexes. Genes: COL28A1, EFEMP1, SPARCL1, TNC
  - [14]: Matrix proteins interact forming structural scaffold

**Required genes (not in input)**
- Genes: SPARC, MERTK, MMP2, MMP9
  - [14]: SPARC, MERTK, and matrix metalloproteinases regulate matrix remodeling

**Program citations**
- [14]: TIMP3 and matrix genes dysregulated in chronic phase TBI
- [16]: Comprehensive analysis of extracellular matrix genes in glioblastoma

## Program: Inflammatory Response Activation and Immune Signaling
Coordinates astrocyte inflammatory responses through production of alarm signals (IL33), immune cell adhesion receptors (CD44), and complement pathway proteins (MASP1), alongside interferon-stimulated genes (IFI44L) responding to innate immune activation. This program establishes astrocytes as active neuroimmune responders participating in pattern recognition, inflammatory mediator production, and immune cell recruitment. Dysregulation in astrocytoma likely alters balance between tumor-suppressing and tumor-promoting immune responses.

**Predicted impacts**
- Enhanced immune cell recruitment and infiltration
- Dysregulated Th1/Th2 balance through altered IL-33 signaling
- Altered complement activation affecting inflammation and tissue damage
- Modified interferon responses to immune challenges

**Evidence summary**
Astrocytes respond to pathogen and damage signals through inflammatory mediator production establishing them as active participants in neuroimmune responses. IL-33 functions as alarmin signaling through IL1RL1/ST2 receptors promoting Th2 differentiation and innate lymphoid cell responses. Astrocytes produce IL-33 in response to injury, with elevated IL-33 in chronic-phase astrocytes suggesting neuroprotective polarization. CD44 serves as hyaluronic acid receptor functioning in cell-cell and cell-matrix interactions while supporting inflammatory signaling and immune cell recruitment. CD44 shows particularly high expression in cancer stem cells and tumor-promoting macrophages, suggesting roles in both tumor cell biology and immune cell polarization. MASP1 encodes mannan-binding lectin-associated serine protease-1 participating in complement pathway activation, critical for innate immunity. IFI44L encodes interferon-induced protein 44-like functioning downstream of interferon signaling, with comprehensive enrichment of interferon-α and interferon-γ response pathways observed in reactive astrocytes across injury models. In astrocytoma, dysregulation of inflammatory signaling likely reflects complex interactions between tumor-promoting pro-inflammatory and immune-suppressive signaling.

**Atomic biological processes**
- IL-33 alarmin signaling and Th2 response activation. Genes: IL33
  - [35]: IL-33 promotes innate lymphoid cell-dependent IFN-gamma production and Th2 cell differentiation
  - [14]: IL33 genes upregulated in chronic phase astrocytes with neuroprotective implications
- CD44-mediated immune cell recruitment and adhesion. Genes: CD44
  - [34]: CD44 functions in cell-cell and cell-matrix interactions supporting immune cell recruitment
- Complement pathway activation. Genes: MASP1
  - [35]: MASP1 participates in complement pathway activation
- Interferon-stimulated response. Genes: IFI44L
  - [8]: Interferon-α and interferon-γ response pathways enriched in reactive astrocytes
  - [5]: IFN-α and IFN-γ responses highly enriched in acute TBI astrocytes

**Atomic cellular components**
- IL-33 receptor signaling complexes. Genes: IL33
  - [35]: IL-33 binds IL1RL1/ST2 receptor promoting downstream signaling
- CD44-hyaluronic acid interaction surfaces. Genes: CD44
  - [34]: CD44 forms receptor-ligand interactions with hyaluronic acid

**Required genes (not in input)**
- Genes: IL1B, TNF, IL6, IL10
  - [8]: Additional inflammatory cytokines produce comprehensive inflammatory signature

**Program citations**
- [35]: IL-33 and CD44 in immune signaling
- [14]: IL33 upregulation in chronic phase astrocytes
- [8]: Interferon response pathways in astrocyte activation

## Program: Vesicular Trafficking and Membrane Dynamics
Maintains complex endomembrane systems supporting synthesis, trafficking, and secretion of proteins and lipids to distinct cellular compartments through endoplasmic reticulum (ITPR2, ATF6), endosomal dynamics (SNX31), and vesicular transport (STON2) proteins. This program supports astrocyte secretion of gliotransmitters, trophic factors, and inflammatory mediators essential for normal astrocyte function. Dysregulation of vesicular trafficking in astrocytoma impairs coordinated secretory responses and alters cellul ar communication.

**Predicted impacts**
- Dysregulated calcium signaling affecting astrocyte responses
- Impaired secretion of gliotransmitters and trophic factors
- Altered endocytic capacity affecting membrane dynamics
- Disrupted trafficking of surface receptors and transporters

**Evidence summary**
Astrocytes maintain complex endomembrane systems supporting synthesis and trafficking of proteins and lipids to distinct cellular compartments. ITPR2 encodes inositol 1,4,5-trisphosphate receptor 2 participating in calcium signaling and intracellular calcium release from endoplasmic reticulum, a process particularly important in astrocytes functioning as cellular calcium oscillators. ATF6 encodes activating transcription factor 6 functioning in unfolded protein response managing endoplasmic reticulum stress, emerging as important in both normal astrocyte physiology and disease states. SNX31 encodes sorting nexin-31 participating in early endosome dynamics and protein sorting essential for endocytic trafficking. STON2 encodes stonin-2 functioning in clathrin-mediated endocytosis and membrane trafficking. Recent work demonstrates Plexin-B1 safeguards astrocyte agility through regulation of endocytic vesicle dynamics, with Plexin-B1 deficiency promoting astrocyte clustering through altered membrane dynamics and endocytic dysfunction. This suggests dysregulation of vesicular trafficking programs contributes to astrocyte dysfunction in disease states, potentially relevant to astrocytoma.

**Atomic biological processes**
- Calcium signaling and intracellular calcium release. Genes: ITPR2
  - [28]: ITPR2 participates in calcium signaling through ER calcium release
- Unfolded protein response and ER stress management. Genes: ATF6
  - [33]: ATF6 functions in unfolded protein response managing endoplasmic reticulum stress
- Early endosome dynamics and protein sorting. Genes: SNX31
  - [14]: SNX31 participates in early endosome dynamics and protein sorting
- Clathrin-mediated endocytosis. Genes: STON2
  - [14]: STON2 functions in clathrin-mediated endocytosis and membrane trafficking
- Endocytic vesicle dynamics and membrane plasticity. Genes: SNX31, STON2
  - [2]: Plexin-B1 safeguards astrocyte agility through regulation of endocytic vesicle dynamics

**Atomic cellular components**
- Inositol 1,4,5-trisphosphate receptor calcium channels. Genes: ITPR2
  - [28]: ITPR2 forms calcium release channels in ER membrane
- Early endosome compartments. Genes: SNX31
  - [14]: SNX31 localizes to early endosomes organizing protein sorting

**Required genes (not in input)**
- Genes: RAB5, EEA1, LAMP1
  - [2]: Early endosomal and lysosomal proteins regulate trafficking

**Program citations**
- [2]: Plexin-B1 regulation of endocytic vesicle dynamics in astrocytes
- [28]: Calcium signaling and endosomal dynamics in neural cells

## Program: Synaptic Plasticity and Synapse-Associated Processes
Establishes astrocyte relationships with synapses through secretion of synaptogenic factors, neurotransmitter metabolism, and support for synaptic transmission. This program includes exocytosis regulation (CADPS), vesicular transport (SYTL4), and actin dynamics (FMN2) enabling astrocytic contributions to synaptic function and plasticity.

**Predicted impacts**
- Impaired gliotransmitter and trophic factor release
- Dysregulated synaptic contact formation and maintenance
- Altered astrocytic support for synaptic transmission
- Enhanced synaptic dysfunction and neurodegeneration in peritumoral regions

**Evidence summary**
Astrocytes establish intimate relationships with synapses supporting synaptic transmission through neurotransmitter uptake, metabolic support, and secretion of synaptogenic factors. CADPS encodes calcium-dependent secretion activator functioning in regulated exocytosis of neuropeptides and neurotrophic factors essential for astrocytic support of synaptic transmission. SYTL4 encodes synaptotagmin-like-4 participating in vesicular trafficking and calcium-regulated secretion of gliotransmitters. FMN2 encodes formin homology 2 domain-containing protein 2 participating in actin dynamics and filopodium formation, processes important in establishing astrocyte-synaptic contacts. In astrocytoma context, dysregulation of this program likely impairs astrocytic support of synaptic transmission contributing to neuronal dysfunction and seizure susceptibility.

**Atomic biological processes**
- Regulated exocytosis of neuropeptides and trophic factors. Genes: CADPS
  - [26]: CADPS functions in calcium-dependent secretion activation of neuropeptides
- Vesicular trafficking and calcium-regulated secretion. Genes: SYTL4
  - [26]: SYTL4 participates in vesicular trafficking and calcium-regulated secretion
- Filopodium formation and synaptic contact establishment. Genes: FMN2
  - [26]: FMN2 participates in actin dynamics and filopodium formation

**Atomic cellular components**
- Secretory vesicle pools and SNARE complexes. Genes: CADPS, SYTL4
  - [26]: CADPS and SYTL4 organize secretory vesicles

**Required genes (not in input)**
- Genes: VAMP2, SNAP25, STX1
  - [26]: SNARE proteins mediate secretory vesicle fusion

**Program citations**
- [26]: CADPS, SYTL4, and FMN2 in astrocytic secretion and synapse interactions

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/177
2. 2. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/3400
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/13193
5. 5. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/3399
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/22352
8. 8. Trudel L, Therriault J, Macedo AC, Woo MS, Rahmouni N, Aumont É, et al.. APOE ε4 potentiates tau related reactive astrogliosis assessed by cerebrospinal fluid YKL40 in Alzheimer’s disease. Communications Medicine [Internet]. 2025Nov20;5(1). Available from: https://www.nature.com/articles/s43856-025-01171-4
9. 9. Soliman E, de JC, Smith K, Ju J, Willison A, Mills J, et al.. Hematopoietic EphA4 deficiency alters microglial heterogeneity and improves chronic spatial memory after brain injury. Scientific Reports [Internet]. 2025Dec5;. Available from: https://www.nature.com/articles/s41598-025-30648-4_reference.pdf
10. 10. Boyoung K, Minju Y, Moonsu P, Hongji R, Junhang P, Hyerin Y, et al.. CRISPR editing of miR-33 restores ApoE lipidation and amyloid-β metabolism in ApoE4 sporadic Alzheimer's disease.. Brain : a journal of neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41288387/
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/11820
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/627
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/12064
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/20512
15. 15. Arpan D, Santiago AF, Ali P, John EM, Marisol DLF-G, Sumod S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma.. Communications biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41366031/?fc=None&ff=20251210103937&v=2.18.0.post22+67771e2
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/6506
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/22601
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/596
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/578
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/2308
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/3756
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/56458
24. 24. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
25. 25. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
27. 27. Tao L, Teng L, Ge M, Wang Y, Hu C, Chen J, et al.. Slc22a17 governs postnatal neurogenesis by maintaining the iron homeostasis in hippocampus. Nature Communications [Internet]. 2025Dec15;16(1). Available from: https://www.nature.com/articles/s41467-025-66108-w
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/14810
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/19
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/23604
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/11303
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/22926
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/12505
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/90865
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=12505
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/3458
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
38. 38. Ghose S, Chaudry UR, Chakravarty S, Sarangi S, Biswas NK, Baral R, et al.. Integrated profiling reveals polarity protein dysregulation during oral cancer progression. Scientific Reports [Internet]. 2025Dec3;15(1). Available from: https://www.nature.com/articles/s41598-025-27447-2
39. 39. Pérez-Posada A, García-Castro H, Emili E, Guixeras-Fontana A, Vanni V, Salamanca-Diaz D, et al.. Multimodal single cell analyses reveal gene networks of planarian stem cell differentiation. Nature Communications [Internet]. 2025Nov27;16(1). Available from: https://www.nature.com/articles/s41467-025-65712-0
40. 40. Available from: http://json-schema.org/draft-07/schema#",
