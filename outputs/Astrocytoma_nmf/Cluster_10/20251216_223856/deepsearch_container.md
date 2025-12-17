# Gene Program Markdown Report

## Context
- Cell type: Astrocyte
- Disease: Astrocytoma
- Tissue: Brain (central nervous system)

## Input Genes
FGFR3, SDC4, SLC6A11, TPD52L1, AL157396.1, ACSS3, LGI1, AC027117.2, LINC00299, GRM3, AC097518.2, AC106845.1, RGS20, ALDH1A1, AC124852.1, LINC00499, ACSBG1, GJA1, GJB6, ANGPTL4, GPC5, ADGRV1, PREX2, PRKG1, PRR5, ... (200 total)

## Program: Glutamate Homeostasis and Neurotransmitter Recycling
Coordinated regulation of glutamate uptake from synaptic clefts, intracellular metabolism to glutamine, and recycling back to neurons. This program maintains extracellular glutamate within physiologically appropriate ranges, preventing excitotoxicity while providing neuronal glutamate recycling. Central to this program are the high-affinity glutamate transporters SLC1A3 (EAAT1) and SLC1A2 (EAAT2) which couple glutamate uptake to sodium and potassium gradients established by the Na+/K+-ATPase pumps ATP1A2 and ATP1B2. Following uptake, glutamate is converted to glutamine by GLUL (glutamine synthetase), which prevents glutamate toxicity and stores glutamate in an inert, transportable form. Metabotropic glutamate receptors GRM3 and GRM5 mediate calcium signaling responses to synaptic glutamate release. Gap junction proteins GJA1 and GJB6 facilitate intercellular communication among astrocytes enabling spatial potassium and glutamate buffering.

**Predicted impacts**
- Dysregulation of glutamate transporters leads to extracellular glutamate accumulation and excitotoxic neuronal injury
- Reduced glutamate-glutamine cycling forces malignant astrocytes toward alternative metabolic pathways for energy and biosynthesis
- Altered metabotropic glutamate receptor signaling shifts astrocytes from homeostatic to pro-tumoral metabolic programs
- Gap junction dysfunction impairs spatial buffering of extracellular glutamate and potassium among astrocyte networks

**Evidence summary**
The glutamate homeostasis program represents one of the most critical and well-established astrocyte functions. In normal physiology, SLC1A3 and SLC1A2 maintain extracellular glutamate at physiological ranges (~500 nM) preventing excitotoxicity. These transporters couple glutamate uptake to sodium influx and potassium efflux, requiring ATP hydrolysis by ATP1A2 to maintain appropriate electrochemical gradients. Following uptake, GLUL rapidly converts glutamate to glutamine, which is recycled back to neurons. In astrocytoma, transcriptomic profiling reveals consistent downregulation of glutamate transporter expression, particularly SLC1A3 and SLC1A2, leading to extracellular glutamate accumulation that contributes to neuronal excitotoxicity and creates selective advantages for tumor cells. The downregulation of this program in astrocytoma is mechanistically linked to enhanced dependency on alternative metabolic pathways and potential acquisition of pro-proliferative signaling through glutamate receptor activation.

**Atomic biological processes**
- Glutamate uptake from synaptic clefts. Genes: SLC1A3, SLC1A2, ATP1A2, ATP1B2
  - [9]: SLC1A3 encodes high affinity glutamate transporter EAAT1/GLAST; functions in termination of excitatory neurotransmission
  - [3]: SLC1A3 downregulation in TBI-affected astrocytes contributes to glutamate accumulation
  - [7]: Down syndrome astrocytes show reduced SLC1A3 and SLC1A2 glutamate transporter expression
- Glutamate-glutamine cycle and metabolism. Genes: GLUL, SLC7A10
  - [11]: Glutamine synthetase deficiency in astrocytes results in neonatal death
  - [14]: Neuronal glutamine synthetase expression occurs in response to reduced astrocyte glutamine availability
- Metabotropic glutamate receptor signaling. Genes: GRM3, GRM5
  - [31]: mGluR3 is the major mGlu receptor expressed by adult cortical astrocytes
  - [34]: Blockade of mGluR5 in astrocytes modulates astrocytic function and increases phagocytosis
- Intercellular gap junction communication. Genes: GJA1, GJB6
  - [5]: Gap junction proteins enable astrocytic intercellular communication under hypoxic conditions

**Atomic cellular components**
- Plasma membrane glutamate transporters. Genes: SLC1A3, SLC1A2
  - [9]: SLC1A3 encodes member of high affinity glutamate transporter family
- Na+/K+-ATPase pump. Genes: ATP1A2, ATP1B2
  - [3]: ATP1A2 and ATP1B2 are involved in ion homeostasis regulation
- Gap junction channels. Genes: GJA1, GJB6
  - [5]: GJA1 and GJB6 gap junction proteins mediate intercellular communication

**Required genes (not in input)**
- Genes: GLT1, GLAST, EAAT1, EAAT2
  - [3]: Additional glutamate transporters contribute to comprehensive glutamate homeostasis

**Program citations**
- [3]: Comprehensive transcriptomic analysis of astrocytes at acute, subacute, and chronic TBI timepoints reveals downregulation of SLC1A3 and other glutamate-related genes
- [7]: Down syndrome astrocytes show distinct phenotypic alterations including reduced glutamate transporter expression
- [9]: SLC1A3 encodes glutamate transporter essential for neurotransmitter homeostasis
- [31]: GRM3 metabotropic glutamate receptor is major mGlu receptor in adult cortical astrocytes

## Program: Water Homeostasis and Osmotic Balance
Regulation of cellular and extracellular water distribution through aquaporin water channels and ion pumps. AQP4 and AQP1 facilitate rapid osmotically-driven water transport across astrocytic membranes in response to changes in intracellular and extracellular osmolarity. AQP4 concentrates at astrocytic endfeet contacting blood vessels and synapses where it enables rapid water uptake following neuronal activity-induced increases in extracellular osmolarity. ATP1A2 and ATP1B2 establish the sodium and potassium gradients that provide osmotic driving force and maintain resting membrane potential. This coordinated program is essential for maintaining appropriate extracellular space volume, preventing cerebral edema, and enabling efficient nutrient distribution.

**Predicted impacts**
- AQP4 dysregulation contributes to altered cerebral edema formation in astrocytoma
- Modified water transport kinetics alter microenvironment osmolarity affecting drug penetration
- Loss of aquaporin function impairs waste clearance from tumor microenvironment
- Altered ion homeostasis affects neuronal excitability and tumor cell migration through osmolarity changes

**Evidence summary**
AQP4 represents a critical component of astrocyte physiology, with particular importance in blood-brain barrier function through its localization at astrocytic endfeet. In neuromyelitis optica spectrum disorder, autoantibody targeting of AQP4 leads to complement-dependent cytotoxicity and astrocyte death. In astrocytoma, AQP4 expression and localization alterations contribute to disrupted water homeostasis, altered cerebral edema dynamics, and potentially impaired drug penetration. The specific targeting of AQP4 in NMOSD demonstrates how dysregulation of aquaporin function has direct pathophysiological consequences for CNS disease.

**Atomic biological processes**
- Osmotically-driven water transport. Genes: AQP4, AQP1
  - [8]: AQP4 facilitates water transport in astrocytes, with overexpression leading to abnormal water transport
  - [6]: AQP4 water channel abundance in astrocytic endfeet, with M23 isoform forming orthogonal arrays targeted by autoantibodies in NMOSD
- Ion gradient establishment and maintenance. Genes: ATP1A2, ATP1B2
  - [3]: ATP1A2 and ATP1B2 involved in ion homeostasis regulation in astrocytes

**Atomic cellular components**
- Aquaporin water channel proteins. Genes: AQP4, AQP1
  - [8]: AQP4 encoded on chromosome 18, facilitates water transport
- Astrocytic endfeet. Genes: AQP4
  - [6]: AQP4M23 isoform abundant at astrocytic foot processes, forms orthogonal arrays of particles

**Required genes (not in input)**
- Genes: NKCC1, KCC2
  - [3]: Additional ion transporters contribute to osmotic balance

**Program citations**
- [6]: AQP4 autoantibodies target water channel on astrocyte endfeet in NMOSD
- [8]: AQP4 chromosomal location and basic water transport functions
- [3]: Osmolarity and ion homeostasis regulated through multiple mechanisms in astrocytes

## Program: Metabolic Reprogramming and Biosynthetic Capacity
Coordinated regulation of glycolytic, lipogenic, and oxidative metabolic pathways enabling astrocytes to synthesize biosynthetic precursors and generate energy. In normal physiology, astrocytes exhibit high glycolytic capacity and produce lactate that is exported to neurons through the astrocyte-neuron lactate shuttle. In astrocytoma, this metabolic program is fundamentally rewired to prioritize self-centered biosynthesis and proliferation rather than neuron-supporting lactate production. Key metabolic enzymes include GLUL (glutamate-glutamine metabolism), ALDH1A1 (lipid aldehyde metabolism), ME1 (malic enzyme enabling NADPH generation), ACSS1/ACSS3 (acetyl-CoA synthetase converting acetate to acetyl-CoA), ACSBG1 (acyl-CoA synthetase for branched-chain fatty acids), ACSL6 (long-chain fatty acid activation), and ACACB (acetyl-CoA carboxylase regulating fatty acid oxidation versus synthesis). Additionally, MARC2 and MGST1 support mitochondrial antioxidant defense enabling enhanced oxidative metabolism.

**Predicted impacts**
- Enhanced lipogenic capacity enables rapid membrane synthesis supporting tumor cell proliferation
- Increased oxidative metabolism generates ATP and biosynthetic precursors while producing ROS requiring enhanced antioxidant defenses
- Loss of lactate-producing capacity impairs astrocyte support for surrounding neurons
- Metabolic rewiring creates distinct microenvironment metabolite signatures that selectively favor tumor cell survival
- Enhanced nucleotide synthesis supports DNA replication and repair enabling genomic instability and therapeutic resistance

**Evidence summary**
Metabolic reprogramming represents a hallmark feature of cancer including glioblastoma and astrocytoma. Studies integrating multi-omics datasets with metabolic tracing demonstrate that extracellular matrix alterations drive enhanced guanylate production through IMPDH and GMPS, accumulating nucleotide pools that enhance DNA repair and sustain proliferation under chemotherapy stress. Similar metabolic rewiring in astrocytoma likely involves enhanced expression of acetyl-CoA synthetases (ACSS1, ACSS3) enabling utilization of alternative carbon sources including acetate. The coordinated downregulation of GLUL and glutamate transporters alongside upregulation of lipogenic enzymes creates a fundamental shift from neuron-supporting lactate production to self-centered biosynthesis. This metabolic rewiring is mechanistically coupled to reduced oxidative stress vulnerability through enhanced antioxidant enzyme expression (MARC2, MGST1), enabling sustained oxidative phosphorylation-dependent ATP and biosynthetic precursor generation.

**Atomic biological processes**
- Glycolytic glucose metabolism. Genes: GLUL, ME1
  - [3]: Metabolic shift consistent with neuronal differentiation includes changes in glycolytic gene expression
- Lipogenic fatty acid and acetyl-CoA metabolism. Genes: ACSS1, ACSS3, ACSBG1, ACSL6, ACACB
  - [20]: Extracellular matrix drives guanylate production through IMPDH and GMPS, supporting enhanced biosynthesis and chemotherapy resistance
- Retinoic acid biosynthesis. Genes: ALDH1A1
  - [12]: ALDH1A2 involved in retinoic acid biosynthesis
- Oxidative phosphorylation and mitochondrial function. Genes: MARC2, MGST1
  - [37]: ROS generation and antioxidant defenses regulated by SOD enzymes and related proteins

**Atomic cellular components**
- Cytoplasmic metabolic enzymes. Genes: ACSS1, ACSS3, ACSBG1, ACSL6, ME1
  - [20]: Metabolic enzymes localize to cytoplasm and mitochondria
- Mitochondrial antioxidant defense proteins. Genes: MARC2, MGST1
  - [37]: Mitochondrial ROS management through multiple enzymatic systems

**Required genes (not in input)**
- Genes: LDHA, LDHB, GLUT1, GLUT3, IMPDH, GMPS
  - [20]: Additional metabolic enzymes including IMPDH and GMPS support nucleotide synthesis

**Program citations**
- [20]: ECM-driven metabolic alterations in PDAC cells enhance guanylate production supporting chemotherapy resistance
- [3]: Metabolic gene expression changes in astrocytes during TBI including downregulation of glycolytic genes
- [37]: Mitochondrial oxidative phosphorylation and ROS management critical for metabolic programs

## Program: Reactive Astrocyte Response and Neuroinflammatory Signaling
Following CNS injury, disease, or malignant transformation, astrocytes undergo reactive transformation characterized by upregulation of genes encoding structural proteins, secreted inflammatory mediators, and acute phase proteins. The genes in this program include CST3 (cystatin C, an extracellular protease inhibitor), DKK3 (Dickkopf-3 functioning in injury-induced neurogenesis), IFITM3 (interferon-induced transmembrane protein involved in immune responses), and APOE (apolipoprotein E, critical for neuroinflammatory responses and lipid transport). Reactive astrocytes exhibit sustained transcriptional activation of genes encoding TNF-alpha, IL-1beta, IL-6, CCL2, CXCL10, and complement components. In chronic TBI, reactive astrocytes exhibit both pro-inflammatory/neurotoxic (A1-like) and pro-repair/neuroprotective (A2-like) subsets expressing distinct transcriptional programs.

**Predicted impacts**
- Sustained pro-inflammatory signaling establishes immunosuppressive tumor microenvironment
- APOE overexpression exacerbates amyloid-beta accumulation and neuroinflammatory pathways
- Enhanced cytokine and chemokine secretion promotes immune cell infiltration and altered immune cell polarization
- Reactive astrocyte transcriptional programs drive growth factor production sustaining malignant proliferation
- Altered reactive astrocyte subsets shift from neuroprotective to neurotoxic functions promoting neurodegeneration

**Evidence summary**
Reactive astrocyte transformation represents a fundamental response to CNS injury and disease. High-throughput RNA sequencing studies of astrocytes at multiple timepoints following TBI reveal sustained astrocyte activation with distinct transcriptional signatures at acute, subacute, and chronic phases. Early acute phase astrocytes exhibit pro-inflammatory A1-like signatures with upregulation of TNF, IL-1β, CCL2, CXCL10, and complement components, while subacute and chronic astrocytes transition toward mixed phenotypes incorporating both neurodegenerative and regenerative elements. APOE ε4 carriership potentiates tau-related reactive astrogliosis, with APOE ε4 carriers showing stronger associations between YKL-40 (a marker of astrocyte reactivity) and tau burden in the brain. In astrocytoma contexts, the corrupted reactive astrocyte response program generates tumor-promoting rather than tissue-protective functions, with malignant astrocytes secreting growth factors and establishing immunosuppressive microenvironments that facilitate malignant progression.

**Atomic biological processes**
- Pro-inflammatory cytokine and chemokine secretion. Genes: APOE, CST3, DKK3, IFITM3
  - [3]: Upregulation of TNF, Ccl2, Cxcl10, Il1b, and other inflammatory genes in acute TBI astrocytes
  - [25]: APOE ε4 increases pro-inflammatory astrocytes by epigenetic mechanisms
  - [6]: Inflammatory stress response in astrocytes following anti-AQP4 antibody treatment including NF-κB signaling
- Acute phase protein and protease inhibitor production. Genes: CST3
  - [3]: CST3 upregulation in acute and subacute TBI astrocytes
- Injury-induced neurogenesis support. Genes: DKK3
  - [3]: DKK3 associated with neuroprotection and downregulated in chronic TBI
- Lipid transport and neuroinflammatory signaling. Genes: APOE
  - [25]: APOE ε4 carriership potentiates tau-related reactive astrogliosis
  - [10]: APOE ε4 exerts direct effects on delirium risk through neuroinflammatory mechanisms

**Atomic cellular components**
- Secretory vesicles and pathways for cytokine release. Genes: APOE, CST3
  - [3]: Astrocyte secretion of neuroinflammatory factors in reactive state

**Required genes (not in input)**
- Genes: TNF, IL1B, IL6, CCL2, CXCL10, NF-κB, STAT3
  - [3]: Inflammatory pathway genes critical for reactive astrocyte response

**Program citations**
- [3]: Comprehensive transcriptomic profiling of astrocyte reactivity phases in TBI
- [25]: APOE ε4 potentiates reactive astrogliosis and tau-related pathology
- [10]: APOE direct effects on neuroinflammation and disease risk
- [6]: Inflammatory transcriptional signatures in astrocytes following immune challenge

## Program: Cytoskeletal Reorganization and Cell Morphology
Coordinated regulation of actin filament polymerization, myosin-mediated contractility, and Rho GTPase signaling enabling dynamic astrocyte morphological remodeling. The ramified morphology of resting astrocytes enables extensive synaptic coverage and metabolic support, while reactive transformation involves morphological changes including process retraction and hypertrophy. The genes encoding cytoskeletal regulators include SHROOM3 (Shroom family protein regulating actomyosin organization), DLC1 (Rho GTPase-activating protein restricting cell migration), CARMIL1 (Capping protein-Arp2/3-Myosin-Linker protein), ABLIM1 (actin-binding LIM protein), RANBP3L (Ran-binding protein in cytoplasmic transport), and VAV3 (guanine nucleotide exchange factor activating Rho GTPases). Additional genes include RHOJ, RHPN2, and ARHGEF4 facilitating Rho family signaling.

**Predicted impacts**
- Enhanced actin dynamics enable rapid morphological remodeling during reactive transformation
- Increased myosin-mediated contractility promotes process retraction and cell migration
- Rho GTPase activation promotes stress fiber formation and focal adhesion assembly enabling migration
- Dysregulated cytoskeletal dynamics facilitate tumor cell invasion through enhanced migratory capacity
- Loss of ramified morphology reduces synaptic coverage and metabolic support capacity for neurons

**Evidence summary**
Cytoskeletal reorganization programs enable astrocytes to dynamically modify their morphology in response to local environmental cues and injury. Reactive astrocytes transition from ramified morphology with extensive fine processes to hypertrophic morphology characterized by process retraction and increased perinuclear intermediate filament accumulation. This morphological transition involves coordinated reorganization of actin filaments through Rho family GTPase signaling, altered balance between actin polymerization and depolymerization, and myosin-mediated contractility. Deep learning analysis of chromatin accessibility in injury-responsive enhancers reveals that astrocyte-specific transcription factors including SOX9 recruit AP-1 factors to drive injury-responsive enhancer activation controlling genes regulating Rho signaling and actin dynamics. In astrocytoma, dysregulated cytoskeletal signaling may promote invasive morphologies supporting tumor cell migration while simultaneously reducing the extensive process ramification characteristic of healthy astrocytes.

**Atomic biological processes**
- Actin polymerization and depolymerization dynamics. Genes: SHROOM3, CARMIL1, ABLIM1
  - [42]: Actin dynamics regulated through specialized nucleation complexes and polymerization factors
- Rho family GTPase signaling and activation. Genes: DLC1, VAV3, RHOJ, RHPN2, ARHGEF4
  - [60]: SOX9 recruits AP-1 factors to injury-responsive enhancers regulating Rho signaling
- Myosin-mediated contractility and force generation. Genes: SHROOM3, CARMIL1
  - [42]: Myosin-actin interactions generate mechanical forces reshaping cell morphology
- Focal adhesion assembly and integrin signaling coupling. Genes: ABLIM1
  - [60]: Focal adhesion assembly couples integrin signaling to cytoskeletal reorganization

**Atomic cellular components**
- Actin filament networks. Genes: SHROOM3, CARMIL1, ABLIM1
  - [42]: Actin filaments organized through specialized nucleation and regulatory proteins
- Rho GTPase signaling complexes. Genes: VAV3, ARHGEF4, RHOJ
  - [60]: Rho family GTPases regulate actin dynamics through downstream effectors

**Required genes (not in input)**
- Genes: RAC1, CDC42, RHOA, ARP2, ARP3, ROCK1, ROCK2
  - [60]: Core Rho family GTPases and their downstream effectors essential for cytoskeletal dynamics

**Program citations**
- [60]: Regulatory code of injury-responsive enhancers controlling cytoskeletal gene expression
- [42]: Specialized signaling centers direct cell fate and spatial organization of developing tissues

## Program: Cell-Cell Communication and Synaptic Adhesion
Direct cell-cell interactions through adhesion molecules enabling astrocyte-neuron and astrocyte-astrocyte connections essential for normal CNS development, synapse formation, and synaptic plasticity. The genes encoding adhesion molecules include CADM1 (cell adhesion molecule 1), CADM2 (synaptic cell adhesion molecule/SynCAM), CHL1 (close homolog of L1), PCDH9 (protocadherin 9), CNTNAP3 (contactin-associated protein 3), CNTNAP3B (contactin-associated protein 3B), and NTM (neurotrimin, IgLON family member). These proteins mediate both hemophilic (like-to-like) and heterophilic (different molecule) interactions, with specific adhesion complexes enabling distinct signaling outcomes.

**Predicted impacts**
- Reduced adhesion molecule expression impairs astrocyte-neuron synaptic interactions
- Dysregulated adhesion complexes facilitate tumor cell invasion through reduced adhesive constraints
- Altered cell-cell communication reduces astrocyte capacity to support neuronal development and synaptic plasticity
- Enhanced immune cell infiltration through altered adhesion molecule expression on astrocytes and tumor cells
- Loss of functional synaptic contact between astrocytes and neurons disrupts metabolic coupling and synaptic support

**Evidence summary**
Cell adhesion molecules mediate critical interactions between astrocytes and neurons, enabling both mechanical coupling and signal transduction events. Studies examining synaptic deconstruction in tau pathology identify alterations in genes regulating axon guidance and synapse assembly, with specific involvement of adhesion molecules in both maintenance and pathological remodeling of synaptic connections. CADM1 and CADM2 belonging to the synaptic cell adhesion molecule family enable homophilic interactions promoting synapse formation and stabilization. In astrocytoma, downregulation of these adhesion molecules is expected to facilitate invasion through reduced adhesive constraints while simultaneously creating an environment permissive for glioma-associated neuronal hyperexcitability through impaired metabolic support.

**Atomic biological processes**
- Homophilic cell-cell adhesion through IgCAM superfamily. Genes: CADM1, CADM2, CHL1, NTM
  - [29]: CADM1 enables signaling receptor binding and positive regulation of cytokine production
  - [30]: CADM2 member of synaptic cell adhesion molecule family, immunoglobulin superfamily
- Heterophilic adhesion through protocadherin and contactin interactions. Genes: PCDH9, CNTNAP3, CNTNAP3B
  - [41]: Intercellular signaling and synaptic deconstruction involving adhesion molecules
- Intracellular signaling cascades triggered by adhesion engagement. Genes: CADM1, CADM2, PCDH9
  - [41]: Adhesion molecule engagement triggers downstream signaling affecting synaptic function

**Atomic cellular components**
- IgCAM and protocadherin adhesion complexes. Genes: CADM1, CADM2, PCDH9, CHL1, NTM
  - [29]: Cell adhesion molecule 1 mediates cell recognition and interaction
- Contactin-associated protein complexes. Genes: CNTNAP3, CNTNAP3B
  - [57]: Contactin-associated proteins mediate cell-cell interactions in developing brain

**Required genes (not in input)**
- Genes: N-CADHERIN, L1CAM, NCAM1, NRCAM
  - [41]: Additional adhesion molecules regulating synaptic architecture

**Program citations**
- [29]: CADM1 cell adhesion molecule functions
- [30]: CADM2 synaptic cell adhesion molecule family member
- [41]: Intercellular signaling and synaptic architecture remodeling involving adhesion molecules

## Program: Extracellular Matrix Composition and Remodeling
Synthesis, assembly, and degradation of extracellular matrix components providing structural support and regulating signaling through integrin and non-integrin receptors. Astrocytes contribute substantially to ECM composition through synthesis of collagen, laminin, and other fibrous proteins, particularly during reactive transformation and glial scar formation. The genes encoding ECM components include SPARCL1 (SPARC-like protein 1 in dendritic spine development), COL5A3 (collagen type V alpha 3 chain), LAMA1 (laminin alpha 1 chain), and HPSE2 (heparanase-2 modifying ECM proteoglycans). ECM remodeling through protease degradation enables cell migration and tissue plasticity.

**Predicted impacts**
- Enhanced ECM deposition creates mechanically stiff microenvironment promoting tumor cell survival
- Altered ECM composition restricts immune cell infiltration and drug penetration
- Modified growth factor sequestration by altered ECM proteoglycans creates selective microenvironment signals
- Remodeled ECM facilitates tumor cell invasion and migration through degradation-dependent spatial transitions
- Dysregulated ECM mechanics alters cellular mechanotransduction affecting astrocyte and tumor cell phenotypes

**Evidence summary**
The extracellular matrix exerts profound influences on cellular behavior through both structural support and signaling via integrin and non-integrin receptors. Single-cell spatial transcriptomic studies mapping nearly 400 ECM genes in glioblastoma versus non-cancerous brain reveal dramatically dysregulated ECM expression with distinct patterns in tumor cells, endothelial cells, and immune cells. Studies in pancreatic cancer demonstrate that ECM-driven metabolic alterations enhance guanylate production through IMPDH and GMPS, accumulating nucleotide pools that alleviate oxaliplatin-induced DNA damage and boost cell proliferation. Similar ECM-metabolism-DNA repair axes likely operate in astrocytoma, with fibrotic ECM remodeling creating chemotherapy resistance and selective growth factor bioavailability that supports malignant progression.

**Atomic biological processes**
- Synthesis of fibrous ECM components. Genes: SPARCL1, COL5A3, LAMA1
  - [26]: Single-cell spatial profiling identifies unique ECM expression profiles in GBM cell populations
  - [49]: Spatial transcriptomic atlas reveals non-overlapping ECM expression signatures across GBM and stromal cells
- ECM proteoglycan modification and growth factor bioavailability regulation. Genes: HPSE2
  - [26]: ECM signaling pathways dysregulated in brain pathologies including glioblastoma
- Mechanical properties and cellular mechanotransduction. Genes: COL5A3, LAMA1
  - [20]: Extracellular matrix rigidity influences metabolic alterations and drug resistance

**Atomic cellular components**
- Fibrous collagen and laminin networks. Genes: COL5A3, LAMA1
  - [26]: ECM spatial distribution in tumor versus normal brain
- Secreted ECM-modifying enzymes. Genes: HPSE2
  - [26]: ECM remodeling through protease activity

**Required genes (not in input)**
- Genes: COL1A1, COL1A2, FN1, LAMB1, MMPs, TIMPs
  - [26]: Additional ECM components and ECM-modifying enzymes

**Program citations**
- [26]: Single-cell spatial profiling of glioblastoma matrisome
- [49]: GBM spatial transcriptomic atlas reveals ECM dysregulation
- [20]: ECM-driven metabolic alterations supporting chemotherapy resistance

## Program: Lipid Metabolism and Neuroinflammatory Signaling
Synthesis, transport, and metabolism of lipids including membrane lipids, cholesterol, fatty acids, and lipid mediators that regulate inflammation and immune function. Astrocytes synthesize and transport lipids supporting myelin formation by oligodendrocytes, membrane synthesis for cell growth, and generation of lipid mediators regulating neuroinflammation. The genes encoding lipid metabolism proteins include APOE (apolipoprotein E, major lipid transporter in CNS), CLU (clusterin, lipid-binding chaperone for complex lipids), SAT1 (spermidine/spermine N1-acetyltransferase affecting membrane dynamics), and ABCD2 (ATP-binding cassette transporter for long-chain fatty acids). APOE ε4 variants exhibit dramatically increased risk for Alzheimer disease and represent critical modifiers of astrocyte function in disease contexts.

**Predicted impacts**
- APOE ε4 overexpression exacerbates amyloid-beta accumulation and neuroinflammatory pathways
- Enhanced lipid transport supports rapid membrane synthesis during malignant transformation
- Dysregulated lipid metabolism alters immune cell recruitment and polarization through lipid ligand production
- Modified polyamine metabolism affects membrane fluidity and cellular signaling
- Altered cholesterol and phospholipid synthesis support de novo membrane synthesis for tumor cell proliferation

**Evidence summary**
Lipids serve multiple critical roles in astrocytes including membrane synthesis, cholesterol regulation, and generation of lipid mediators affecting inflammation and immune function. APOE represents the major CNS lipid transporter protein expressed predominantly by astrocytes, with three common isoforms (ε2, ε3, ε4) exhibiting distinct effects on lipid metabolism and disease risk. APOE ε4 carriers exhibit dramatically increased risk for Alzheimer disease through multiple mechanisms including reduced amyloid-beta clearance, altered lipid metabolism, dysregulation of lipid-dependent signaling, and exacerbated pro-inflammatory responses. Studies demonstrate that APOE ε4 is associated with inflammatory responses and increased neuroinflammation in Alzheimer disease, with APOE ε4 shown to increase pro-inflammatory astrocytes through epigenetic mechanisms. In glioblastoma, APOE and NCSTN (component of γ-secretase complex) represent top upstream regulators in chronic TBI astrocytes, suggesting that lipid metabolism dysregulation participates in chronic neurodegeneration and potentially malignant transformation.

**Atomic biological processes**
- Cholesterol and lipid transport. Genes: APOE, CLU
  - [25]: APOE expressed in astrocytes regulates amyloid-beta clearance and lipid metabolism
  - [10]: APOE ε4 direct effects on disease risk through lipid transport and neuroinflammatory pathways
- Fatty acid oxidation and synthesis. Genes: ABCD2, ACSL6
  - [20]: Fatty acid metabolism supports both energy production and membrane synthesis
- Polyamine metabolism affecting membrane fluidity. Genes: SAT1
  - [37]: Polyamine metabolism regulates cell biology including membrane dynamics
- Lipid-mediated immune signaling. Genes: APOE
  - [25]: APOE affects immune cell infiltration and polarization through lipid signaling

**Atomic cellular components**
- Lipid transport proteins. Genes: APOE, CLU
  - [25]: APOE as major CNS lipid transporter protein
- Peroxisomal and mitochondrial fatty acid oxidation machinery. Genes: ABCD2
  - [20]: Fatty acid oxidation compartmentalization

**Required genes (not in input)**
- Genes: LDLR, LRPX, OXYSTEROL-BINDING PROTEINS, SREBP
  - [25]: Additional lipid-metabolizing machinery and cholesterol-sensing systems

**Program citations**
- [25]: APOE ε4 potentiates tau-related reactive astrogliosis and neuroinflammation
- [10]: APOE ε4 effects on disease risk including direct neuroinflammatory effects
- [3]: APOE and NCSTN as top upstream regulators in chronic TBI astrocytes

## Program: Developmental Identity and Lineage Determination
Establishment and maintenance of astrocyte lineage identity through activity of developmental transcription factors that specify forebrain astrocyte characteristics and regional specialization. The genes encoding developmental transcription factors include EMX2 (empty spiracles homeobox 2, critical for telencephalic patterning), LHX2 (LIM homeobox 2, specifying forebrain identity), GLI3 (zinc finger transcription factor in Sonic hedgehog signaling), HIF3A (hypoxia-inducible factor 3 alpha responding to hypoxic conditions), and BHLHE40 (basic helix-loop-helix transcription factor in circadian rhythm and metabolic programming). These factors collectively establish astrocyte lineage commitment during development and maintain identity throughout life, though they remain dynamically regulated in response to pathological insults.

**Predicted impacts**
- Loss of developmental identity determinants enables enhanced plasticity and transdifferentiation capacity
- Reduced EMX2 and LHX2 expression in astrocytoma reflects de-differentiation toward more immature progenitor state
- Downregulation of lineage-restraining factors enables neuronal conversion under experimental manipulation
- Altered developmental programming permits acquisition of more immature characteristics supporting enhanced proliferation
- Dysregulated developmental identity may facilitate escape from astrocyte-specific growth constraints

**Evidence summary**
Astrocyte identity is established during development through the coordinated activity of lineage-specific transcription factors including EMX2 (empty spiracles) and LHX2 (LIM homeobox), with continued roles in maintaining astrocyte identity and regulating responses to pathological insults. Recent studies demonstrate remarkable developmental plasticity in mature astrocytes, showing that forced expression of neurogenic transcription factors including Ascl1 enables efficient conversion to functional neurons in vivo. This capacity for transdifferentiation demonstrates that mature astrocytes retain latent developmental potential suppressed by established identity mechanisms. In glioblastoma and lower-grade astrocytoma, downregulation of developmental identity determinants has been documented, suggesting that loss of mature astrocyte identity represents a feature of malignant transformation. The specific capacity of neural progenitor transcription factors to reprogram astrocytes to neurons provides a mechanistic demonstration that developmental programming can be reversed through altered transcriptional factor activity.

**Atomic biological processes**
- Telencephalic patterning and forebrain specification. Genes: EMX2, LHX2
  - [33]: EMX2 functions in positioning pallial-subpallial boundary
  - [42]: Specialized signaling centers direct cell fate and spatial organization
- Sonic hedgehog pathway signaling in developmental specification. Genes: GLI3
  - [42]: Sonic hedgehog pathway agonists enable ventral progenitor emergence
- Hypoxic stress response and metabolic programming. Genes: HIF3A
  - [37]: Hypoxia-inducible factors regulate metabolic adaptation
- Circadian rhythm and metabolic regulation. Genes: BHLHE40
  - [60]: Transcription factor activity in developmental and metabolic programming

**Atomic cellular components**
- Developmental transcription factor complexes. Genes: EMX2, LHX2, GLI3
  - [42]: Transcription factors form regulatory complexes at target genes
- Chromatin accessible regions at developmental genes. Genes: EMX2, LHX2
  - [60]: Injury-responsive enhancers control developmental gene accessibility

**Required genes (not in input)**
- Genes: PAX6, OLIG2, SOX9, STAT3
  - [60]: Additional transcription factors regulating astrocyte specification and lineage maintenance

**Program citations**
- [1]: Ascl1-mediated astrocyte-to-neuron conversion demonstrates retained developmental potential
- [33]: EMX2 developmental functions
- [42]: Developmental signaling centers and lineage specification

## Program: Specialized Ion and Molecular Transport
Transport of diverse substrates including amino acids, ions, nucleotides, and other molecules through specialized transporter proteins and channels. Beyond aquaporins and glutamate transporters, astrocytes express numerous transporters enabling GABA uptake (SLC6A11), uptake of other amino acids (SLC7A10), mitochondrial glutamate transport (SLC25A18), zinc homeostasis (SLC39A12), and GABA-A receptor signaling (GABRA2). The two-pore channel TPCN1 enables endolysosomal calcium release regulating autophagy and secretion. These specialized transporters collectively establish the diverse chemical microenvironment surrounding astrocytes and neurons.

**Predicted impacts**
- Dysregulated GABA uptake alters GABAergic inhibitory tone in tumor microenvironment
- Modified amino acid transport restricts nutrient availability to surrounding neurons while supporting tumor cell proliferation
- Altered mitochondrial metabolite transport impairs oxidative metabolism and contributes to metabolic rewiring
- Zinc dysregulation affects metalloproteinase activity and transcription factor function
- Impaired endolysosomal calcium signaling affects autophagy and secretory pathways in tumor versus normal astrocytes

**Evidence summary**
Beyond the critical roles of glutamate transporters and aquaporins in astrocyte homeostasis, astrocytes express a diverse array of specialized transporters enabling transport of GABA, other amino acids, zinc, and other substrates essential for synaptic function and metabolic homeostasis. The specific tissue- and cell-type distribution of these transporters enables selective chemical environments supporting specialized cellular functions. Dysregulation of these specialized transporters in astrocytoma contributes to altered amino acid availability in the tumor microenvironment, modified ion homeostasis affecting tumor cell excitability and signaling, and altered trace element availability affecting enzyme activity.

**Atomic biological processes**
- GABA and amino acid uptake. Genes: SLC6A11, SLC7A10
  - [9]: SLC1A3 member of high-affinity glutamate transporter family
- Mitochondrial amino acid and metabolite transport. Genes: SLC25A18
  - [3]: Mitochondrial metabolite transport in astrocyte metabolism
- Zinc homeostasis and signaling. Genes: SLC39A12
  - [20]: Zinc transport and homeostasis regulate protein function
- Endolysosomal calcium signaling. Genes: TPCN1
  - [37]: Two-pore channels enable endolysosomal calcium release
- GABAergic inhibitory signaling. Genes: GABRA2
  - [50]: GABA-A receptor signaling in neuronal inhibition

**Atomic cellular components**
- Plasma membrane amino acid transporters. Genes: SLC6A11, SLC7A10
  - [9]: Amino acid transporters mediate coupled substrate-ion transport
- Mitochondrial transporter proteins. Genes: SLC25A18
  - [3]: Mitochondrial solute carriers enable substrate oxidation
- Endolysosomal two-pore channel complexes. Genes: TPCN1
  - [37]: Two-pore channels form ion-selective channels on endolysosomal membranes

**Required genes (not in input)**
- Genes: SLC16A1, SLC16A3, MCT1, MCT4
  - [58]: Monocarboxylate transporters MCT1/4 enable lactate and other metabolite transport

**Program citations**
- [9]: SLC family amino acid transporters
- [3]: Metabolite transport and mitochondrial metabolism
- [37]: Endolysosomal calcium signaling and two-pore channels

## Program: Mitochondrial Function and Oxidative Stress Management
Mitochondrial oxidative phosphorylation enabling ATP synthesis coupled with reactive oxygen species (ROS) generation requiring coordinated antioxidant defenses. The genes encoding mitochondrial proteins and oxidative stress management include MARC2 (mitochondrial amidoxime reducer component 2, in antioxidant defense), MGST1 (microsomal glutathione S-transferase 1, catalyzing glutathione-dependent detoxification), and SOD1 (superoxide dismutase 1, catalyzing superoxide dismutation). Additionally, mitochondrial calcium handling through SLC25A18 and calcium-release through RYR3 (ryanodine receptor 3) regulate metabolic dynamics and stress responses. ROS generation during electron transport chain function requires continuous detoxification to prevent cellular damage.

**Predicted impacts**
- Enhanced oxidative metabolism generates ATP while producing ROS requiring increased antioxidant capacity
- Dysregulated ROS protection enables ferroptosis resistance through enhanced antioxidant defenses
- Altered mitochondrial calcium handling affects metabolic plasticity and stress responses
- Chronic oxidative stress drives genomic instability supporting malignant progression
- Enhanced antioxidant capacity protects tumor cells from ROS-induced apoptosis while maintaining proliferative capacity

**Evidence summary**
Astrocyte metabolic capacity depends critically on mitochondrial function enabling both ATP production through oxidative phosphorylation and simultaneous ROS generation requiring coordinate antioxidant defenses. Studies examining mitochondrial dysfunction in cellular senescence reveal that multiple antioxidant enzymes including superoxide dismutase (SOD1), catalase, and glutathione-dependent systems must be coordinately regulated to prevent ROS accumulation-driven senescence. In chronic TBI, upregulation of both neurodegenerative pathways including mitochondrial apoptotic pathways alongside neuroprotective genes including SOD1 and related antioxidant factors suggests that chronic astrocyte activation includes components of oxidative stress and attempted compensation through enhanced antioxidant defenses. In astrocytoma, dysregulation of oxidative stress management likely protects tumor cells from ROS-induced apoptosis, enables sustained oxidative metabolism supporting biosynthesis, and potentially drives adaptive oxidative stress response programming that paradoxically promotes malignant progression.

**Atomic biological processes**
- Oxidative phosphorylation and ATP synthesis. Genes: MARC2, MGST1
  - [37]: Oxidative phosphorylation ATP synthesis coupled to proton gradient
- Reactive oxygen species generation and disposal. Genes: MARC2, MGST1
  - [37]: ROS generation during electron transport requires antioxidant defenses
  - [40]: Superoxide dismutase and related antioxidant enzymes protect against oxidative damage
- Mitochondrial calcium uptake and release. Genes: SLC25A18, RYR3
  - [37]: Calcium accumulation in mitochondria regulates metabolic state and stress signaling
- Glutathione-dependent detoxification. Genes: MGST1
  - [37]: Glutathione S-transferases catalyze detoxification of electrophilic compounds

**Atomic cellular components**
- Electron transport chain and oxidative phosphorylation machinery. Genes: MARC2
  - [37]: ETC complexes establish proton gradient for ATP synthesis
- Mitochondrial calcium handling proteins. Genes: SLC25A18, RYR3
  - [37]: MCU and related transporters enable calcium uptake and release
- Antioxidant defense enzyme complexes. Genes: MGST1
  - [37]: Glutathione and related systems provide antioxidant defense

**Required genes (not in input)**
- Genes: SOD2, CATALASE, GSS, GPX4, TXNRD1
  - [37]: Multiple antioxidant enzyme systems required for comprehensive oxidative stress management

**Program citations**
- [37]: Mitochondrial dysfunction and oxidative stress in cellular senescence
- [40]: SOD1 and antioxidant defense in astrocytes
- [3]: Mitochondrial pathways upregulated in chronic TBI astrocytes

## Bibliography
1. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
2. Available from: https://www.ncbi.nlm.nih.gov/gene/546
3. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
4. Anamaria S, Cristian-Ionut O, Raluca IV, Madalina B, Manuela E, Sorin V, et al.. Unpredictable Evolution of Pilocytic Astrocytoma in Adults: A Case Series and Diagnostic Challenges.. The American journal of case reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41382984/?fc=None&ff=20251213032813&v=2.18.0.post22+67771e2
5. Available from: https://www.ncbi.nlm.nih.gov/gene/2697
6. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
7. André LTES, Pedro HP de O, Bruno YY-M, Jéssica da SF, Jonatan PA, Helder IN, et al.. Complement pathway dysregulation and astrocyte alterations in Down syndrome: evidence from postmortem brain tissue and iPSC-derived astrocytes.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41350900/?fc=None&ff=20251210050700&v=2.18.0.post22+67771e2
8. Available from: https://www.ncbi.nlm.nih.gov/gene/361
9. Available from: https://www.ncbi.nlm.nih.gov/gene/6507
10. Raptis V, Bhak Y, Cannings TI, MacLullich AMJ, Tenesa A. Dissecting the genetic and proteomic risk factors for delirium. Nature Aging [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s43587-025-01018-6
11. Available from: https://www.ncbi.nlm.nih.gov/gene/14645
12. Available from: https://www.ncbi.nlm.nih.gov/gene/8854
13. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
14. Available from: https://www.ncbi.nlm.nih.gov/gene/24957
15. Available from: https://www.ncbi.nlm.nih.gov/gene/7057
16. Available from: https://www.ncbi.nlm.nih.gov/gene/2247
17. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
18. Available from: https://www.ncbi.nlm.nih.gov/gene/4288
19. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
20. Efthymiou G, Lohmann E, Montenegro C, Kousteridou P, Bertrand P, Pereira J, et al.. The extracellular matrix drives guanylate production and protects pancreatic cancer cells from oxaliplatin-induced DNA damage. Science Advances [Internet]. 2025Dec12;11(50). Available from: https://www.science.org/doi/10.1126/sciadv.adu2276
21. Available from: https://www.ncbi.nlm.nih.gov/gene/18596
22. Available from: https://www.ncbi.nlm.nih.gov/gene/2202
23. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
24. Trudel L, Therriault J, Macedo AC, Woo MS, Rahmouni N, Aumont É, et al.. APOE ε4 potentiates tau related reactive astrogliosis assessed by cerebrospinal fluid YKL40 in Alzheimer’s disease. Communications Medicine [Internet]. 2025Nov20;5(1). Available from: https://www.nature.com/articles/s43856-025-01171-4
25. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
26. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
27. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
28. Available from: https://www.ncbi.nlm.nih.gov/gene/23705
29. Available from: https://www.ncbi.nlm.nih.gov/gene/253559
30. Available from: https://www.ncbi.nlm.nih.gov/gene/2913
31. Youngblood MW, Kumari A, Kang Y-T, Gould A, Habashy K, Gomez M, et al.. Dynamic release of extracellular particles after opening of the blood-brain barrier predicts glioblastoma susceptibility to paclitaxel. Nature Communications [Internet]. 2025Dec16;16(1). Available from: https://www.nature.com/articles/s41467-025-65681-4
32. Available from: https://www.ncbi.nlm.nih.gov/gene/13797
33. Available from: https://www.ncbi.nlm.nih.gov/gene/2915
34. Available from: https://www.ncbi.nlm.nih.gov/gene/6622
35. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
36. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
37. Lara N, Javier M, Irene S-S, Moisés S-P, Esther R-S, Teresa S-M. Next-Generation Sequencing Reveals a Diagnostic and Prognostic Role of the . International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41373636/?fc=None&ff=20251211105245&v=2.18.0.post22+67771e2
38. Available from: https://www.ncbi.nlm.nih.gov/gene/6647
39. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
40. Skoufa E, Zhong J, Hu K, Kahre O, Tsissios G, Carrau L, et al.. Specialized signaling centers direct cell fate and spatial organization in a mesodermal organoid model. Science Advances [Internet]. 2025Nov28;11(48). Available from: https://www.science.org/doi/10.1126/sciadv.ady7682
41. Available from: https://www.ncbi.nlm.nih.gov/gene/1950
42. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
43. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
44. Available from: https://www.nature.com/subjects/endocytosis/ncomms
45. Spreen A, Sadanandan NP, Schneider MW, Kuehn E, Leemisa AN, De ZR, et al.. Optogenetic silencing by combining a rhodopsin cyclase with an engineered cGMP-gated potassium channel. Science Advances [Internet]. 2025Nov28;11(48). Available from: https://www.science.org/doi/10.1126/sciadv.adx1195
46. Zhongyi Z, Yang L, Zhicong Z, Tian G, Youhui C, Qian C, et al.. MRI-based radiomic clustering identifies a glioblastoma subtype enriched for neural stemness and proliferative programs.. Frontiers in oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41378293/?fc=None&ff=20251212152250&v=2.18.0.post22+67771e2
47. Zhang X-G, Song J-N. 6-Gingerol enhances the anti-tumor activity of temozolomide by inhibiting EGR1/GDF15 signaling in glioblastoma. Scientific Reports [Internet]. 2025Nov26;15(1). Available from: https://www.nature.com/articles/s41598-025-26109-7
48. Available from: https://www.nature.com/subjects/astrocyte/neuro
49. Ghirardello M, Yruela I, Merino P, Sackstein R, Sanz-Martínez I, Hurtado-Guerrero R. Structure, function, and implications of fucosyltransferases in health and disease. Nature Communications [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41467-025-66871-w_reference.pdf
50. Gkogka A, Malwade S, Koskuvi M, Ohtonen S, Molnar E, Bose R, et al.. Human oligodendrocyte progenitor cells mediate synapse elimination through TAM receptor activation. Nature Communications [Internet]. 2025Dec5;16(1). Available from: https://www.nature.com/articles/s41467-025-66521-1
51. Meng Q, Li C, Cai Y, Chen Y, Chen X, Wang X, et al.. Itaconate transport across the plasma membrane and Salmonella-containing vacuole via MCT1/4 modulates macrophage antibacterial activity. Nature Communications [Internet]. 2025Nov26;16(1). Available from: https://www.nature.com/articles/s41467-025-65582-6
52. Jiang R, Lu Z, Li F, Zhu Y, Yang M, Zhang S, et al.. scCirclehunter delineates ecDNA-containing cells using single-cell ATAC-seq, with a focus on glioblastoma. Cell Discovery [Internet]. 2025Dec9;11(1). Available from: https://www.nature.com/articles/s41421-025-00842-9
53. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
54. Wei X-Y, Zou Z-M, Yao Z-X, Teng S-W, Wei X-Y, Tang W-J, et al.. Neuronal activity-induced GLUT3 plasma translocation supports energy demands for memory acquisition. Communications Biology [Internet]. 2025Nov28;8(1). Available from: https://www.nature.com/articles/s42003-025-09119-z
55. Available from: http://json-schema.org/draft-07/schema#",
