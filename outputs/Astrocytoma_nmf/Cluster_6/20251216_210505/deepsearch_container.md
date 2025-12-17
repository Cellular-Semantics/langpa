# Gene Program Markdown Report

## Context
- Cell type: Astrocytes, astrocyte progenitors, and malignant astrocytic tumor cells
- Disease: Astrocytoma (including IDH-mutant and IDH-wildtype forms, with focus on high-grade glioma/glioblastoma)
- Tissue: Central nervous system, particularly cerebral cortex and subcortical white matter

## Input Genes
SOX6, FGF12, CADM2, SMOC1, PDE4B, KIF13A, MAML2, FGF14, COL11A1, VCAN, PLAAT1, ALCAM, MEGF11, UST, GRID2, FYN, VCAN-AS1, DNM3, OPCML, DSCAM, OPHN1, MAP2, TNR, ZNF804A, AL512308.1, ... (200 total)

## Program: Synaptic Adhesion and Plasticity
Gene program controlling synaptic structure, neuronal-glial communication, and activity-dependent plasticity through cell adhesion molecules, synaptic scaffolding proteins, and extracellular matrix components. This program includes both pre- and postsynaptic organization and maintenance mechanisms.

**Predicted impacts**
- Altered synaptic connectivity through disrupted adhesion molecule expression
- Enhanced peritumoral neuronal hyperexcitability through compromised synaptic stabilization
- Dysregulated neuron-glia communication affecting trophic support and metabolic coupling
- Impaired activity-dependent synaptic plasticity in peritumoral circuits
- Reduced structural support for dendritic spines and synaptic terminals

**Evidence summary**
Synaptic adhesion molecules and extracellular matrix components undergo coordinated dysregulation in reactive astrocytes and peritumoral neural tissue. Studies of traumatic brain injury reveal marked downregulation of synaptic communication genes in reactive astrocytes[23][29]. In glioma, peritumoral neurons exhibit significant transcriptional alterations in genes controlling synaptic transmission and plasticity[32]. The presence of multiple cadherins, cell adhesion molecules, and extracellular matrix proteins in the gene list indicates widespread disruption of synaptic organization in astrocytoma.

**Atomic biological processes**
- Synapse formation and maturation. Genes: CADM2, LRRTM4, AJAP1
  - [9]: CADM2 (SynCAM2) induces presynaptic terminal formation and mediates homophilic cell adhesion
- Synaptic plasticity and activity-dependent remodeling. Genes: TNR, CADM2, PCDH15
  - [44]: TNR (tenascin R) modulates synaptic plasticity and information storage in neural circuits
- Neuron-glia communication. Genes: NRCAM, ALCAM, CNTN3
  - [23]: Downregulation of genes encoding NRCAM and other adhesion molecules occurs in reactive astrocytes following injury

**Atomic cellular components**
- Adherens junction and cell-cell adhesion. Genes: CADM2, CTNNA3, PCDH15, CDH13, NCAM2
  - [9]: CADM2-mediated adhesion promotes synaptic organization through cell-cell contact
- Extracellular matrix in neural tissue. Genes: TNR, CNTN3, LRRTM4
  - [44]: TNR functions as an extracellular matrix component regulating synaptic plasticity

**Required genes (not in input)**
- Genes: NMDAR subunits (GRIN1, GRIN2A-D), N-cadherin (CDH2), Neuroligin family members (NLGN1-3), PSD-95 family (DLG4, SAP102)
  - [44]: Classical synaptic adhesion components necessary for complete synapse assembly

**Program citations**
- [9]: CADM2 functions in synaptic organization
- [23]: Reactive astrocyte gene expression changes in chronic TBI
- [29]: Comprehensive analysis of astrocytic transcriptional programs in injury
- [32]: Peritumoral neuronal transcriptional alterations in glioma-associated seizures
- [44]: TNR modulates synaptic plasticity

## Program: Glutamatergic Excitatory Signaling
Gene program controlling excitatory glutamatergic synaptic transmission through ionotropic glutamate receptors, glutamate transporters, and associated regulatory proteins. This program represents the molecular basis of glutamate synapses.

**Predicted impacts**
- Enhanced peritumoral neuronal excitability through altered glutamate receptor expression and composition
- Impaired glutamate homeostasis leading to synaptic glutamate accumulation and excitotoxicity
- Altered calcium permeability of AMPA receptors through GluA2 subunit dysregulation
- Increased susceptibility to seizures through enhanced glutamatergic excitation
- Dysregulated long-term potentiation and synaptic plasticity

**Evidence summary**
Glutamatergic dysregulation represents a well-established mechanism in glioma-associated seizures and peritumoral neuronal dysfunction. Glioma cells elevate extracellular glutamate through both direct release and impairment of astrocytic glutamate reuptake[32]. Peritumoral neurons exhibit altered AMPA receptor subunit expression with increased GluA2-lacking, calcium-permeable AMPA receptors, promoting calcium-dependent neuronal damage and hyperexcitability[32]. The convergence of AMPA receptor subunits (GRIA2-4) with glutamate transporter genes indicates coordinated dysregulation of glutamate synapses in astrocytoma.

**Atomic biological processes**
- Postsynaptic glutamate receptor function. Genes: GRIA2, GRIA3, GRIA4, GRID2
  - [32]: AMPA receptor dysregulation occurs in peritumoral neurons in glioma-associated seizure models
- Glutamate clearance and homeostasis. Genes: SLC1A1
  - [32]: Impaired glutamate reuptake contributes to neuronal hyperexcitability in peritumoral regions
- Glutamate-dependent excitotoxicity. Genes: GRIA2, GRIA3, GRIA4, SLC1A1
  - [32]: Excess glutamate elevation through xCT transporter dysfunction drives peritumoral neuronal hyperexcitability

**Atomic cellular components**
- AMPA receptor complex. Genes: GRIA2, GRIA3, GRIA4
  - [32]: AMPA receptor subunit composition changes in peritumoral neurons correlate with altered excitatory postsynaptic currents

**Required genes (not in input)**
- Genes: GRIN1, GRIN2A-D (NMDAR subunits), SLC1A2 (astrocytic glutamate transporter EAAT2), GRM1-8 (metabotropic glutamate receptors), Homer proteins (mGluR scaffolding)
  - [32]: Complete glutamate synapse requires additional receptor and transporter components

**Program citations**
- [32]: Comprehensive analysis of peritumoral neuronal dysfunction in glioma-associated seizures with altered glutamate receptor and transporter expression

## Program: Voltage-Gated Ion Channels and Intrinsic Excitability
Gene program controlling neuronal intrinsic excitability through voltage-gated sodium and potassium channels, ATP-gated cation channels, and acid-sensing ion channels. These genes determine the threshold and rate of action potential generation in neurons.

**Predicted impacts**
- Enhanced neuronal excitability through altered sodium channel expression or altered intrinsic properties
- Increased seizure susceptibility in peritumoral tissue through dysregulated action potential generation
- Altered response to extracellular ATP and acidification through ion channel dysregulation
- Enhanced calcium influx through P2RX7 activation contributing to excitotoxicity
- Dysregulated neuronal firing patterns and loss of normal activity regulation

**Evidence summary**
Intrinsic neuronal excitability represents a key determinant of seizure susceptibility in glioma. Peritumoral neurons in glioma models exhibit increased intrinsic excitability with enhanced spontaneous firing rates[32]. SCN1A and SCN3A mutations cause genetic epilepsy syndromes through impaired sodium channel function[34][37]. P2RX7 activation by extracellular ATP contributes to both neuronal excitation and immune cell-mediated inflammation in the tumor microenvironment[38]. The inclusion of multiple ion channel genes indicates coordinated dysregulation of neuronal excitability in astrocytoma.

**Atomic biological processes**
- Action potential generation and propagation. Genes: SCN1A, SCN3A
  - [34]: SCN1A mutations in genetic epilepsy with febrile seizures directly impair action potential generation
- Neuronal repolarization and afterhyperpolarization. Genes: KCNIP4
  - [34]: Potassium channel function controlled by KCNIP interacting proteins regulates repolarization
- ATP-dependent ion channel signaling. Genes: P2RX7, ASIC4
  - [38]: P2RX7 activation by extracellular ATP mediates neuronal and immune cell responses
- pH-sensitive ion channel function. Genes: ASIC4
  - [54]: Tumor microenvironment acidification due to lactate accumulation can activate acid-sensing channels

**Atomic cellular components**
- Voltage-gated sodium channel complex. Genes: SCN1A, SCN3A
  - [34]: SCN1A and SCN3A encode core components of neuronal sodium channels
- Ligand-gated ion channels. Genes: P2RX7, ASIC4
  - [38]: P2RX7 represents ATP-gated cation channel expressed in neurons and immune cells

**Required genes (not in input)**
- Genes: KCNQ family (M-channel genes), HCN genes (hyperpolarization-activated cyclic nucleotide channels), CACNA genes (voltage-gated calcium channels)
  - [32]: Additional ion channels contribute to neuronal excitability control

**Program citations**
- [32]: Peritumoral neurons exhibit altered intrinsic excitability in glioma models
- [34]: SCN1A mutations in genetic epilepsy
- [37]: SCN3A mutations associated with epilepsy
- [38]: P2RX7 channel function in neurons and immune cells
- [54]: Tumor microenvironment acidification from lactate accumulation

## Program: Oligodendrocyte Lineage Development and Myelination
Gene program controlling specification, differentiation, and functional maturation of oligodendrocytes through lineage-restricted transcription factors, adhesion molecules, and myelin protein genes. This program encompasses the developmental transition from OPC to mature myelin-forming oligodendrocyte.

**Predicted impacts**
- Disrupted OPC differentiation leading to arrest in progenitor state or alternative fate transitions
- Enhanced Notch-mediated OPC maintenance potentially blocking myelination in peritumoral regions
- Impaired myelin formation and lipid synthesis affecting axonal conduction velocity and neuronal function
- Altered glial-glial adhesion potentially affecting oligodendrocyte network organization
- Potential transdifferentiation or plasticity of OPCs under tumor-derived signals

**Evidence summary**
Oligodendrocyte development undergoes significant dysregulation in glioma microenvironment. Injury-induced glial responses demonstrate that OPCs undergo transcriptional reprogramming with altered expression of developmental transcription factors[10]. Adult high-grade gliomas arise in a cellular environment containing mature oligodendrocytes and OPCs, both of which can interact with tumor cells through paracrine signaling. Recent studies of diffuse midline gliomas and glioblastomas reveal subsets of tumors with multilineage gene expression patterns including oligodendrocyte-associated genes[2][5]. The convergence of SOX family transcription factors, OLIG1, RBPJ, and myelin genes indicates coordinated dysregulation of oligodendrocyte lineage in astrocytoma.

**Atomic biological processes**
- Oligodendrocyte specification and differentiation. Genes: SOX10, SOX8, SOX5, SOX6, OLIG1, RBPJ
  - [10]: SOX10 functions as a master regulator of oligodendrocyte specification during CNS development
  - [22]: OLIG1 and SOX10 act synergistically to promote oligodendrocyte differentiation
- OPC progenitor maintenance through Notch signaling. Genes: RBPJ
  - [20]: RBPJ-mediated Notch signaling maintains OPC progenitor status and prevents premature differentiation
- Myelin membrane biogenesis and lipid synthesis. Genes: UGT8, BCAS1
  - [10]: UGT8 catalyzes synthesis of galactocerebroside, major myelin lipid component
- Oligodendrocyte-astrocyte interactions. Genes: ALCAM
  - [8]: ALCAM mediates cell-cell adhesion between oligodendrocytes and other glial cells

**Atomic cellular components**
- Oligodendrocyte transcriptional regulatory network. Genes: OLIG1, SOX10, SOX8, SOX5, SOX6
  - [22]: OLIG1 and OLIG2 transcription factors control oligodendrocyte-specific gene expression
- Myelin sheath structure. Genes: UGT8, BCAS1
  - [10]: BCAS1 and UGT8 produce components of myelin membrane

**Required genes (not in input)**
- Genes: OLIG2, MBP (myelin basic protein), MOG (myelin oligodendrocyte glycoprotein), MAG (myelin-associated glycoprotein), CNP (cyclic nucleotide phosphodiesterase)
  - [10]: Complete oligodendrocyte differentiation program requires additional transcription factors and myelin proteins
  - [22]: OLIG2 is core component of oligodendrocyte specification

**Program citations**
- [2]: WHO classification of gliomas discusses molecular subtypes with varying glial composition
- [5]: High-grade gliomas exhibit biological heterogeneity
- [8]: ALCAM in glial cell interactions
- [10]: SOX10 in oligodendrocyte development and injury responses
- [20]: OLIG2 and oligodendrocyte development
- [22]: OLIG1 in oligodendrocyte differentiation

## Program: Fibroblast Growth Factor and Morphogenic Signaling
Gene program controlling developmental patterning and morphogenic signaling through FGF ligands, intracellular FGF modulators, Sonic Hedgehog pathway components, and related developmental signaling networks. This program regulates neural progenitor proliferation, migration, and fate specification.

**Predicted impacts**
- Dysregulated neural progenitor proliferation through altered FGF signaling
- Enhanced cellular plasticity through morphogenic pathway activation
- Impaired differentiation signals from Hedgehog pathway dysfunction
- Altered ion channel modulation affecting neuronal excitability
- Reactivation of developmental patterning programs in adult tumor context

**Evidence summary**
Developmental morphogenic pathways become dysregulated in glioblastoma and contribute to tumor plasticity. FGF signaling represents a fundamental pathway controlling neural progenitor behavior during development. FGF12 and FGF14 function as intracellular modulators of FGF receptor signaling, positioning them at the intersection of growth factor and ion channel regulation. While canonical Hedgehog pathway genes (SHH, GLI) are not universally mutated in astrocytoma, PTCH1 appears in the gene list, suggesting pathway dysregulation in at least some samples. Notably, glioblastoma progression involves upregulation of developmental progenitor programs characterized by expression of proneural transcription factors and developmental morphogens[24].

**Atomic biological processes**
- FGF-mediated signaling and ion channel modulation. Genes: FGF12, FGF14
  - [1]: FGF12 and FGF14 function as intracellular modulators of FGF receptor signaling
- Sonic Hedgehog pathway signaling. Genes: PTCH1
  - [42]: PTCH1 receptor mediates Sonic Hedgehog signal transduction
- Neural progenitor proliferation and differentiation. Genes: FGF12, FGF14, PTCH1
  - [24]: Developmental patterning genes control neural progenitor fate decisions

**Atomic cellular components**
- FGF intracellular signaling complex. Genes: FGF12, FGF14
  - [1]: FGF12 and FGF14 interact with FGF receptors and ion channels
- Hedgehog signaling pathway components. Genes: PTCH1
  - [42]: PTCH1 acts as membrane receptor for Hedgehog ligands

**Required genes (not in input)**
- Genes: FGFR1-4 (fibroblast growth factor receptors), SHH (Sonic Hedgehog ligand), SMO (Smoothened, Hedgehog signal transducer), GLI1-3 (Hedgehog effector transcription factors)
  - [42]: Complete Hedgehog pathway requires multiple components

**Program citations**
- [1]: FGF12 and FGF14 functions in CNS
- [24]: Glioblastoma acquisition of developmental plasticity programs
- [42]: PTCH1 in Hedgehog signaling

## Program: Growth Factor Receptors and Receptor Tyrosine Kinase Signaling
Gene program encompassing receptor tyrosine kinases and their immediate effectors that control cell proliferation, survival, and migration. This program includes canonical oncogenic receptors in glioma and their downstream signaling components.

**Predicted impacts**
- Enhanced cell proliferation through PDGFRA-mediated PI3K-AKT and MAPK pathway activation
- Increased cell survival through growth factor-dependent anti-apoptotic signaling
- Enhanced cell migration and invasiveness through FYN-mediated cytoskeletal remodeling
- Altered glial-neuronal communication through ERBB-mediated neuregulin signaling
- Activation of malignant phenotype through constitutive or elevated growth factor receptor signaling

**Evidence summary**
Growth factor receptor signaling represents a central oncogenic mechanism in astrocytoma. PDGFRA mutations and amplifications define a specific subset of glioblastomas with particularly aggressive biology[2][27]. The sequential combination of TERT promoter mutation, TP53 loss-of-function, and PDGFRA activation reliably produces lethal glioblastomas in isogenic neural stem cell models, establishing PDGFRA as a key driver mutation[27]. ERBB3 and ERBB4 mediate neuregulin signaling in glial development and continue to function in adult glial cells, where they regulate responses to growth factors and cytokines[13]. FYN functions as a ubiquitous downstream effector of multiple receptor tyrosine kinases and controls cytoskeletal dynamics, adhesion, and gene expression. The convergence of multiple growth factor receptors in the input gene list indicates dysregulation of proliferative signaling in astrocytoma.

**Atomic biological processes**
- PDGFRA-mediated signal transduction. Genes: PDGFRA
  - [2]: PDGFRA mutations and amplifications occur in 40-50% of glioblastomas and drive aggressive progression
  - [27]: Sequential addition of TERT, TP53, and PDGFRA mutations in neural stem cells produces lethal glioblastomas
- Neuregulin-ERBB3/4 pathway. Genes: ERBB3, ERBB4
  - [13]: ERBB3 and ERBB4 mediate neuregulin signaling in glial development and myelination
- SRC family tyrosine kinase signaling. Genes: FYN
  - [43]: FYN tyrosine kinase functions as downstream effector of multiple receptor tyrosine kinases
- Growth factor-mediated cytoskeletal reorganization. Genes: PDGFRA, FYN, ERBB3, ERBB4
  - [27]: Growth factor receptors control cell migration and invasiveness in glioblastoma

**Atomic cellular components**
- Receptor tyrosine kinase complex. Genes: PDGFRA, ERBB3, ERBB4
  - [2]: PDGFRA functions as membrane receptor for PDGF ligands
- SRC family kinase signaling complex. Genes: FYN
  - [43]: FYN associates with receptor complexes and adaptor proteins

**Required genes (not in input)**
- Genes: PDGF ligands (PDGFA, PDGFB), NRG1 (neuregulin-1 ligand), PI3K catalytic and regulatory subunits, AKT kinase, MAPK/ERK pathway kinases, GAP proteins (GTPase-activating proteins)
  - [2]: Complete growth factor signaling pathway requires additional components
  - [27]: PDGFRA signal transduction requires downstream effectors

**Program citations**
- [2]: PDGFRA in glioblastoma molecular classification
- [13]: ERBB3 in glial development and myelination
- [27]: Triple mutant glioblastoma model with PDGFRA
- [43]: FYN in synaptic plasticity and signal transduction

## Program: Developmental Plasticity and Progenitor Identity
Gene program encompassing transcriptional regulators and signaling components controlling cell fate decisions, maintenance of progenitor-like states, and cellular plasticity. This program enables adoption of alternative cell states and suppression of differentiation signals.

**Predicted impacts**
- Enhanced cellular plasticity allowing adoption of alternative cell states
- Suppressed differentiation and terminal specialization
- Maintained or enhanced proliferative capacity in malignant cells
- Increased stemness and self-renewal capacity
- Altered neuronal vs. glial differentiation balance
- Enhanced tumor heterogeneity through multiple stable cell states

**Evidence summary**
Developmental plasticity drives aggressive glioblastoma progression and tumor heterogeneity. Remarkably, glioblastoma tumors exhibit plasticity through activation of developmental progenitor programs, with evidence that intermediate progenitor-like states promote tumorigenicity[24]. INSM1, a transcription factor normally expressed in intermediate progenitors during cortical development, becomes upregulated in glioblastoma tumors and drives oncogenic gene expression with knockdown of INSM1 suppressing tumorigenicity[24]. While INSM1 itself does not appear in the input list, ZEB2, RBPJ, TOX, and NOVA1 represent related developmental regulators controlling cell fate and plasticity. ZEB2 promotes cancer stem cell maintenance and therapy resistance through EMT activation[31][47]. RBPJ-mediated Notch signaling maintains progenitor identity in neural contexts and likely contributes to tumor cell plasticity[20]. The convergence of these developmental plasticity genes indicates coordinated dysregulation enabling tumor cells to exist in multiple states.

**Atomic biological processes**
- Epithelial-mesenchymal transition (EMT) and plasticity. Genes: ZEB2
  - [31]: ZEB2 controls epithelial-mesenchymal transition and promotes stemness in cancer cells
  - [47]: ZEB2 promotes therapy resistance through EMT activation
- Notch-mediated progenitor maintenance. Genes: RBPJ
  - [20]: RBPJ-mediated Notch signaling maintains progenitor identity through suppression of differentiation
- Transcriptional control of developmental programs. Genes: TOX, ZBTB16
  - [24]: Intermediate progenitor transcription factors like INSM1 drive developmental plasticity in glioblastoma
- Post-transcriptional control of differentiation. Genes: NOVA1
  - [24]: RNA-binding protein NOVA1 regulates alternative splicing of neuronal differentiation genes

**Atomic cellular components**
- EMT transcriptional regulatory complex. Genes: ZEB2
  - [31]: ZEB2 functions as core EMT transcription factor
- Notch signaling effector complexes. Genes: RBPJ
  - [20]: RBPJ serves as central effector of Notch-mediated transcriptional programs
- Neuronal RNA-binding protein complex. Genes: NOVA1
  - [24]: NOVA1 assembles into ribonucleoprotein complexes controlling splicing

**Required genes (not in input)**
- Genes: INSM1 (intermediate progenitor marker), SOX2 (neural progenitor maintenance), TCF/LEF family (Wnt effectors), REST (transcriptional repressor), SNAIL family (EMT regulators)
  - [24]: INSM1 represents key intermediate progenitor transcription factor in glioblastoma

**Program citations**
- [20]: RBPJ in progenitor maintenance
- [24]: Developmental plasticity in glioblastoma pathogenesis, INSM1 function in intermediate progenitors
- [31]: ZEB2 in EMT and cancer stem cells
- [47]: ZEB2 promotes therapy resistance

## Program: Extracellular Matrix Organization and Developmental Signaling
Gene program controlling extracellular matrix composition, matrix-receptor signaling, and ECM-dependent developmental processes. This program influences cell migration, differentiation, and tissue mechanics.

**Predicted impacts**
- Altered ECM stiffness affecting glioma cell migration and tumor cell invasiveness
- Enhanced tumor cell infiltration into surrounding brain parenchyma through ECM remodeling
- Dysregulated glial progenitor differentiation through altered ECM-dependent signaling
- Impaired synaptic organization and neural circuit formation through altered ECM composition
- Changed permeability of peritumoral tissue affecting immune cell infiltration
- Altered guidance cues affecting neuronal migration and axonal outgrowth

**Evidence summary**
ECM composition dynamically influences glioma biology and affects both tumor cells and the peritumoral microenvironment. Tumors exhibit extensive ECM remodeling through altered deposition and degradation of matrix proteins, facilitating tumor cell infiltration into surrounding brain parenchyma[5]. Recent studies demonstrate that ECM composition controls glial progenitor behavior, with specific ECM proteins (Smoc1/2) establishing mesenchymal stem cell quiescence through Wnt pathway inhibition[15]. In the glioma context, altered ECM composition through dysregulated expression of versican, collagen, and semaphorins could influence both tumor cell invasion and surrounding neural progenitor behavior. The convergence of multiple ECM component genes (VCAN, COL11A1, COL20A1) and ECM-binding signaling molecules (SEMA5B, SEMA6D) indicates coordinated dysregulation of the extracellular matrix in astrocytoma.

**Atomic biological processes**
- Proteoglycan synthesis and ECM composition. Genes: VCAN
  - [15]: Smoc2 ECM proteins regulate Wnt pathway activity and stem cell quiescence through ECM composition
- Collagen deposition and ECM mechanics. Genes: COL11A1, COL20A1
  - [5]: ECM composition influences glioma cell migration and invasiveness
- Semaphorin-mediated signaling and guidance. Genes: SEMA5B, SEMA6D
  - [5]: Semaphorins guide neuronal migration and axonal outgrowth during development
- ECM-dependent progenitor fate control. Genes: VCAN, TNR
  - [15]: ECM proteins (Smoc1/2) establish mesenchymal stem cell quiescence through Wnt inhibition

**Atomic cellular components**
- Chondroitin sulfate proteoglycan matrix. Genes: VCAN
  - [15]: Proteoglycans like versican form major ECM components
- Fibrillar collagen network. Genes: COL11A1, COL20A1
  - [5]: Collagen composition contributes to ECM stiffness and mechanics
- Semaphorin-Plexin signaling complex. Genes: SEMA5B, SEMA6D
  - [5]: Semaphorins signal through Plexin and Neuropilin receptors

**Required genes (not in input)**
- Genes: ADAMTS proteases, MMP (matrix metalloproteinase) family, Integrin family (cell-ECM adhesion), PLXN (Plexin receptors), NRP (Neuropilin receptors)
  - [5]: Complete ECM remodeling pathway requires additional proteases and receptors

**Program citations**
- [5]: High-grade gliomas and ECM remodeling
- [15]: ECM proteins control stem cell quiescence through Wnt pathway

## Program: Metabolic Reprogramming and Lactate Metabolism
Gene program controlling metabolic substrate utilization, lipid metabolism, and lactate-dependent signaling. This program enables metabolic flexibility in tumor cells and influences immune microenvironment composition.

**Predicted impacts**
- Enhanced metabolic flexibility enabling survival under varying oxygen and nutrient conditions
- Increased lactate production and signaling through lactate receptor pathways
- Altered lipid composition affecting membrane properties and signaling
- Impaired immune cell effector function through lactate-mediated immunosuppression
- Dysregulated tumor cell proliferation through altered metabolic signaling
- Regional metabolic heterogeneity between tumor core and periphery

**Evidence summary**
Metabolic reprogramming represents a fundamental feature of glioblastoma biology, enabling tumor cells to rapidly proliferate under conditions of hypoxia and nutrient limitation[54][57]. Lactate accumulates to levels of 10-15 mM in glioblastoma cores, significantly exceeding normal brain tissue, and actively promotes tumor progression through both metabolic effects (fueling oxidative phosphorylation) and signaling effects (activating lactate receptor GPR81/HCAR1)[54]. The tumor core exhibits enhanced glycolytic activity and lactate production due to hypoxia, whereas peripheral tumor regions may more extensively utilize oxidative phosphorylation[54]. This metabolic heterogeneity influences immune cell recruitment and activation, with lactate-enriched microenvironments exhibiting enhanced immunosuppression. The convergence of lipid metabolism genes (SCD5), metabolic signaling kinases (SGK1), and lipid signaling regulators (DGKB) indicates coordinated dysregulation of metabolic flexibility in astrocytoma.

**Atomic biological processes**
- Fatty acid desaturation and lipid synthesis. Genes: SCD5
  - [57]: Cancer cells exhibit altered lipid metabolism supporting rapid growth and membrane synthesis
- Serine/threonine kinase signaling and metabolism. Genes: SGK1
  - [57]: SGK1 regulates cellular metabolism and survival signaling
- Lipid signaling through diacylglycerol metabolism. Genes: DGKB
  - [57]: Diacylglycerol kinase activity regulates MAPK and other lipid signaling pathways
- Lactate-mediated tumor progression. Genes: SCD5, SGK1, DGKB
  - [54]: Lactate from anaerobic glycolysis promotes GBM malignant progression through metabolic reprogramming

**Atomic cellular components**
- Fatty acid desaturase complex. Genes: SCD5
  - [57]: SCD enzymes catalyze saturated to unsaturated fatty acid conversion
- Protein kinase signaling complex. Genes: SGK1
  - [57]: SGK1 functions downstream of PI3K in multiple signaling contexts
- Lipid signaling molecule synthesis. Genes: DGKB
  - [57]: Diacylglycerol kinase enzymes control conversion of DAG to phosphatidic acid

**Required genes (not in input)**
- Genes: GPR81/HCAR1 (lactate receptors), LDHA (lactate dehydrogenase A), HIF-1α (hypoxia-inducible factor), GLUT1 (glucose transporter), PKFM/PFKL (glycolytic enzymes)
  - [54]: Lactate metabolism pathway requires additional glycolytic and signaling components

**Program citations**
- [54]: Comprehensive analysis of lactate metabolism in glioblastoma and SUCLG2 role
- [57]: Cancer cell metabolic reprogramming and dietary interventions

## Program: Immune-Glial Crosstalk and Microglial Function
Gene program controlling immune cell function, microglial activation states, and immune-glial interactions. This program regulates innate immunity in the CNS and shapes the immunosuppressive tumor microenvironment.

**Predicted impacts**
- Enhanced ATP-mediated inflammatory responses through P2RX7 activation
- Dysregulated microglial activation and transition toward immunosuppressive phenotypes
- Impaired anti-tumor immune responses through altered myeloid cell function
- Enhanced tumor cell survival through trophic support from immunosuppressive myeloid cells
- Altered cytokine production affecting tumor microenvironment composition
- Metabolic-immune crosstalk through lactate-mediated immunosuppression

**Evidence summary**
The tumor microenvironment becomes progressively immunosuppressive as glioblastoma develops, with microglia and infiltrating myeloid cells adopting phenotypes that support tumor growth[55][58]. Microglia originate from primitive yolk sac-derived macrophages during embryogenesis and persist throughout life through self-renewal independent of peripheral hematopoietic input[58]. TREM2-expressing myeloid cells exhibit robust immunosuppressive function through IL-10 and TGF-β production, with enhanced TREM2 expression correlating with advanced disease and reduced CD8+ T-cell infiltration[55]. P2RX7, an ATP-gated cation channel expressed in microglia and immune cells, mediates inflammatory responses and cell death; dysregulation of P2RX7 signaling would alter immune responses to tumor cells[35][38]. The relatively limited representation of immune genes in the input list suggests analysis of primarily tumor and glial cell populations rather than immune cells, though immune-glial interactions remain important in interpreting program function.

**Atomic biological processes**
- ATP-mediated immune cell activation. Genes: P2RX7
  - [35]: P2RX7 activation by extracellular ATP triggers inflammatory responses and cell lysis in immune cells
  - [38]: P2RX7 receptor functions as ligand-gated ion channel mediating ATP-dependent immune responses
- Microglial identity and maintenance. Genes: P2RX7
  - [58]: Microglia represent distinct CNS-resident myeloid lineage with conserved transcriptional signature and developmental origins
- Immunosuppressive myeloid cell function. Genes: P2RX7
  - [55]: TREM2-expressing myeloid cells exhibit immunosuppressive phenotype through IL-10 and TGF-β production

**Atomic cellular components**
- P2X7 purinergic receptor complex. Genes: P2RX7
  - [38]: P2RX7 functions as ATP-gated cation channel in microglial and immune cell membranes

**Required genes (not in input)**
- Genes: TREM2 (triggering receptor expressed on myeloid cells 2), IFN-related genes (IFN-α, IFN-γ), IL-10, IL-12, TNF-α (cytokines), CD86, CD80 (immune costimulation), CSF1R (colony-stimulating factor 1 receptor)
  - [55]: Complete immune regulation requires multiple myeloid markers and cytokines
  - [58]: CSF1R signaling essential for microglia maintenance

**Program citations**
- [35]: P2RX7 in immune cell responses
- [38]: P2RX7 purinergic receptor function
- [55]: TREM2-mediated regulation of myeloid cells in tumor microenvironment
- [58]: Microglia evolution and conserved identity across species

## Program: Cell Migration and Neuronal Process Outgrowth
Gene program controlling cell migration, axonal and dendritic growth, and cytoskeletal dynamics through dynamins, actin regulatory proteins, and related genes. This program regulates both tumor cell invasion and peritumoral neuronal morphology.

**Predicted impacts**
- Enhanced glioma cell migration and invasion through improved endocytic and exocytic dynamics
- Altered tumor cell shape and invasive morphology through actin polymerization control
- Peritumoral neuronal morphological alterations including dendritic spine loss and retraction
- Compromised structural integrity of peritumoral neural circuits
- Enhanced seizure susceptibility through reduced synaptic density in peritumoral regions
- Altered neuronal-glial adhesion affecting tissue organization

**Evidence summary**
Glioblastoma cells exhibit highly invasive phenotype requiring dynamic cytoskeletal reorganization and cell-cell adhesion remodeling[5]. Recent mechanistic studies reveal that peritumoral neurons undergo significant morphological changes in glioma models, with altered dendritic spine density and dendritic morphology[32]. These neuronal morphological alterations correlate with transcriptional changes in genes controlling neuronal structure and cytoskeletal dynamics, indicating active remodeling of peritumoral neural architecture in response to tumor growth[32]. DNM3 functions in membrane dynamics during both endocytosis and cell migration. SHROOM4 controls actin-driven cell shape changes critical for cell migration. TRIM9 regulates actin regulatory proteins controlling dendritic spine development and synaptic organization. The convergence of genes controlling both tumor cell migration (DNM3, SHROOM4) and neuronal process outgrowth (TRIM9) indicates coordinated morphological reorganization affecting both malignant cells and peritumoral neurons.

**Atomic biological processes**
- Membrane scission during endocytosis and migration. Genes: DNM3
  - [39]: Dynamin proteins catalyze membrane scission during endocytosis and contribute to cell morphology
- Actin polymerization and cell shape control. Genes: SHROOM4
  - [5]: Actin regulatory proteins like SHROOM control cell shape and migration in development and cancer
- Ubiquitin-dependent cytoskeletal remodeling. Genes: TRIM9
  - [5]: TRIM family ubiquitin ligases regulate cytoskeletal dynamics and dendritic development
- Peritumoral neuronal morphological changes. Genes: DNM3, SHROOM4, TRIM9
  - [32]: Peritumoral neurons undergo significant morphological alterations including dendritic retraction

**Atomic cellular components**
- Dynamin GTPase complex. Genes: DNM3
  - [39]: Dynamins form oligomeric rings catalyzing membrane scission
- Actin nucleation and polymerization complex. Genes: SHROOM4
  - [5]: SHROOM proteins scaffold actin polymerization machinery
- Ubiquitin-proteasome cytoskeletal regulation. Genes: TRIM9
  - [5]: TRIM proteins ubiquitinate actin regulatory proteins

**Required genes (not in input)**
- Genes: Arp2/3 complex components, Formin family proteins, Rho family GTPases (RAC1, CDC42, RHOA), Myosin II, Cofilin
  - [5]: Complete cytoskeletal dynamics requires additional actin regulatory proteins

**Program citations**
- [5]: High-grade gliomas and cellular invasion mechanisms
- [32]: Peritumoral neuronal morphological changes in glioma models
- [39]: Dynamin function in cell migration and endocytosis

## Program: RNA-Binding Protein-Mediated Post-transcriptional Control
Gene program controlling alternative splicing, mRNA localization, translation, and stability through RNA-binding proteins. This program represents a critical level of gene expression regulation particularly important in neurons and neural development.

**Predicted impacts**
- Altered splicing of synaptic genes promoting neuronal hyperexcitability
- Enhanced expression of development-promoting transcripts through altered mRNA stability
- Dysregulated localization and translation of mRNAs controlling cellular differentiation
- Altered expression of calcium-permeable AMPA receptor isoforms through splicing control
- Impaired dendritic local protein synthesis affecting synaptic plasticity
- Enhanced tumor cell plasticity through post-transcriptional control of developmental genes

**Evidence summary**
Post-transcriptional regulation through alternative splicing, mRNA stability, and translational control represents an important level of gene expression control, particularly in neurons where local translation in dendrites controls synaptic strength and plasticity[24]. NOVA1 regulates alternative splicing of transcripts encoding glutamate receptors, GABA receptors, and other synaptic proteins, with altered NOVA1 activity promoting expression of calcium-permeable AMPA receptor isoforms and enhanced neuronal excitability[24]. Dysregulation of RNA-binding protein expression and function has been documented in glioblastoma and other cancers, with altered splicing programs promoting expression of cancer-promoting isoforms. CELF2 regulates mRNA stability and translation of specific transcripts including those encoding developmental transcription factors. KHDRBS and RBMS proteins represent additional RNA-binding proteins controlling post-transcriptional regulation. The convergence of multiple RNA-binding proteins indicates systematic dysregulation of post-transcriptional gene control in astrocytoma.

**Atomic biological processes**
- Alternative splicing of synaptic transcripts. Genes: NOVA1
  - [24]: NOVA1 regulates alternative splicing of glutamate and GABA receptors controlling neuronal excitability
- mRNA stability and translation control. Genes: CELF2, KHDRBS2, KHDRBS3, RBMS3
  - [24]: CELF2 and related CUGBP proteins regulate mRNA stability and translation of specific targets
- Post-transcriptional splicing regulation of developmental genes. Genes: NOVA1, CELF2
  - [24]: NOVA1 regulation of alternative splicing drives developmental transcriptional programs
- mRNA localization and local translation. Genes: NOVA1, KHDRBS2, KHDRBS3
  - [24]: RNA-binding proteins control mRNA localization to dendrites for local protein synthesis

**Atomic cellular components**
- Neuronal RNA-binding protein complex. Genes: NOVA1
  - [24]: NOVA1 assembles into ribonucleoprotein complexes
- mRNA regulatory element-binding protein complex. Genes: CELF2, KHDRBS2, KHDRBS3, RBMS3
  - [24]: CELF, KHDRBS, and RBMS proteins bind specific mRNA regulatory elements

**Required genes (not in input)**
- Genes: RBM5, RBM10 (RNA-binding motif proteins), SRSF family (SR proteins), U2AF (U2 auxiliary factor), snRNPs (small nuclear ribonucleoproteins)
  - [24]: Complete splicing machinery requires additional RNA-binding and catalytic components

**Program citations**
- [24]: NOVA1 in neuronal differentiation and splicing control

## Program: Cell Adhesion and Focal Adhesion Signaling
Gene program controlling cell-cell and cell-matrix adhesion through desmosomes, adherens junctions, and focal adhesions. This program regulates cellular attachment, mechanotransduction, and coordinated adhesion remodeling.

**Predicted impacts**
- Enhanced glioma cell migration through dynamic focal adhesion turnover
- Reduced cell-cell adhesion enabling invasion and single-cell dissemination
- Altered mechanotransduction affecting growth signaling
- Impaired neuronal-neuronal and neuronal-glial adhesion in peritumoral regions
- Compromised tissue integrity in peritumoral tissue
- Enhanced tumor cell-ECM interactions supporting invasion

**Evidence summary**
Cell-cell and cell-matrix adhesion undergoes extensive remodeling in both glioma cells and peritumoral tissue. Glioma cells exhibit enhanced invasion through dynamic remodeling of focal adhesions and reduced expression of stable junctional proteins[5]. Reactive astrocytes undergo significant reorganization of adhesive structures, with documented downregulation of genes involved in cell junctional assembly and adhesion[23]. PKP4 encodes a plakophilin associated with desmosomes; altered desmosomal function affects both cell-cell adhesion and signal transduction. FERMT1 connects integrin signaling to actin cytoskeleton, enabling mechanotransduction and cell migration. TNS3 functions at focal adhesions to regulate integrin signaling and actin polymerization. CTNNA3 (α-catenin) couples cadherin-mediated adhesion to actin cytoskeleton. The convergence of desmosmal and focal adhesion genes indicates coordinated adhesion remodeling at multiple levels.

**Atomic biological processes**
- Desmosomal cell-cell adhesion. Genes: PKP4
  - [23]: Desmosomal proteins maintain cell junctions required for tissue integrity
- Focal adhesion assembly and turnover. Genes: FERMT1, TNS3
  - [15]: Focal adhesion proteins including fermitin regulate integrin signaling and actin polymerization
- Integrin-cytoskeleton coupling. Genes: FERMT1, TNS3, CTNNA3
  - [15]: Focal adhesion proteins connect integrin tails to actin cytoskeleton
- Cell-cell and cell-matrix adhesion remodeling during migration. Genes: PKP4, FERMT1, TNS3, CTNNA3
  - [5]: Dynamic adhesion remodeling enables glioma cell invasion

**Atomic cellular components**
- Desmosomal junction complex. Genes: PKP4
  - [23]: Plakophilins like PKP4 contribute to desmosomal stability
- Focal adhesion complex. Genes: FERMT1, TNS3, CTNNA3
  - [15]: Focal adhesion proteins assemble at sites of integrin-ECM interaction

**Required genes (not in input)**
- Genes: Integrin family members, Talin proteins, Paxillin, FAK (focal adhesion kinase), Vinculin
  - [15]: Complete focal adhesion requires additional scaffold and signaling proteins

**Program citations**
- [5]: Adhesion dynamics in high-grade glioma
- [15]: Focal adhesion protein function
- [23]: Cell junction changes in reactive astrocytes

## Program: Transcriptional and Epigenetic Regulation
Gene program controlling transcription, chromatin remodeling, and epigenetic modifications through transcription factors, histone modifiers, and chromatin remodeling enzymes. This program regulates gene expression at the chromatin level and enables adaptive transcriptional responses.

**Predicted impacts**
- Altered transcriptional programming of both tumor and peritumoral neural cells
- Dysregulated chromatin structure affecting expression of developmental genes
- Enhanced or suppressed expression of differentiation-associated genes
- Altered epigenetic control of cell fate decisions
- Malignant transcriptional programs promoting proliferation and survival
- Aberrant developmental gene reactivation in adult tumor context

**Evidence summary**
Gliomas exhibit distinct epigenetic landscapes compared to normal neural tissue, with widespread alterations in histone modifications and chromatin accessibility[52]. Epigenetic dysregulation through altered activity of chromatin remodelers and histone modifiers represents a common feature of glioblastoma. Notably, diffuse midline gliomas frequently harbor mutations in genes encoding histone H3 variants with K27M mutations causing global alterations in H3K27 trimethylation patterns[52]. While histone H3 mutations are less common in supratentorial astrocytomas, epigenetic dysregulation remains important. RBPJ functions as a central effector of developmental gene regulation through Notch signaling, with disrupted RBPJ function affecting differentiation vs. progenitor balance. ETV1 functions as a transcription factor controlling expression of proliferation and differentiation genes. KAT2B encodes a histone acetyltransferase promoting chromatin opening and transcriptional activation. The convergence of transcriptional and epigenetic regulators indicates systematic dysregulation of chromatin-level gene expression control.

**Atomic biological processes**
- Notch-mediated transcriptional regulation. Genes: RBPJ
  - [20]: RBPJ serves as central effector of Notch signaling controlling developmental transcription
- ETS family transcription factor signaling. Genes: ETV1
  - [5]: ETV1 encodes ETS transcription factor regulating proliferation and differentiation
- Histone acetyltransferase activity and chromatin opening. Genes: KAT2B
  - [5]: KAT2B acetyltransferase promotes transcriptional activation through histone acetylation
- Transcriptional reprogramming during tumor progression. Genes: RBPJ, ETV1, KAT2B
  - [24]: Glioblastoma progression involves transcriptional transition toward developmental progenitor programs

**Atomic cellular components**
- Notch transcriptional regulatory complex. Genes: RBPJ
  - [20]: RBPJ assembles CSL complex mediating Notch-dependent transcription
- Histone acetyltransferase complex. Genes: KAT2B
  - [5]: KAT proteins assemble with coactivator complexes controlling chromatin state
- ETS transcription factor protein family. Genes: ETV1
  - [5]: ETV1 functions as ETS family transcription factor binding ETS DNA sequences

**Required genes (not in input)**
- Genes: Histone deacetylases (HDAC family), Polycomb repressive complexes (EZH2, EED, SUZ12), Chromatin remodeling ATPases (BAF complexes), Mediator complex components, BRD4
  - [52]: Complete epigenetic regulation requires balanced activation and repression machinery

**Program citations**
- [5]: Transcriptional control in high-grade gliomas
- [20]: RBPJ in transcriptional regulation
- [24]: Transcriptional reprogramming in glioblastoma
- [52]: Epigenetic dysregulation and H3K27M mutations in diffuse midline glioma

## Bibliography
1. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
2. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
3. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/12355/
4. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
5. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
6. Available from: https://www.ncbi.nlm.nih.gov/gene/546
7. Available from: https://www.ncbi.nlm.nih.gov/gene/20682
8. Gkogka A, Malwade S, Koskuvi M, Ohtonen S, Molnar E, Bose R, et al.. Human oligodendrocyte progenitor cells mediate synapse elimination through TAM receptor activation. Nature Communications [Internet]. 2025Dec5;16(1). Available from: https://www.nature.com/articles/s41467-025-66521-1
9. Available from: https://www.ncbi.nlm.nih.gov/gene/23705
10. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
11. Available from: https://www.ncbi.nlm.nih.gov/gene/4133
12. Available from: https://www.ncbi.nlm.nih.gov/gene/25595
13. Available from: https://www.ncbi.nlm.nih.gov/gene/13867
14. Available from: https://www.ncbi.nlm.nih.gov/gene/627
15. Chen Z, Cai M, Wang Y, Li X, He Y, Pu H, et al.. Autocrine ECM molecules establish MSC quiescence during incisor development by disrupting WNT ligand trafficking process. Nature Communications [Internet]. 2025Nov27;16(1). Available from: https://www.nature.com/articles/s41467-025-65705-z
16. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
17. Available from: https://www.ncbi.nlm.nih.gov/gene/4803
18. Available from: https://www.nature.com/subjects/mesenchymal-stem-cells/ncomms
19. Available from: https://www.ncbi.nlm.nih.gov/gene/5154
20. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
21. Available from: https://www.ncbi.nlm.nih.gov/gene/5155
22. Available from: https://www.ncbi.nlm.nih.gov/gene/116448
23. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
24. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
25. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
26. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
27. Patrick AD, Matthew I, Xuan Q, Colin M, Devi A, Diane DM, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model.. Nature communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41354838/
28. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
29. Available from: https://www.ncbi.nlm.nih.gov/gene/11096
30. Available from: https://www.ncbi.nlm.nih.gov/gene/9839
31. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
32. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
33. Available from: https://www.ncbi.nlm.nih.gov/gene/6323
34. Available from: https://www.ncbi.nlm.nih.gov/gene/18439
35. Available from: https://www.ncbi.nlm.nih.gov/gene/1756
36. Available from: https://www.ncbi.nlm.nih.gov/gene/6328
37. Available from: https://www.ncbi.nlm.nih.gov/gene/5027
38. Available from: https://www.ncbi.nlm.nih.gov/gene/13405
39. Available from: https://www.ncbi.nlm.nih.gov/gene/29499
40. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
41. Available from: https://www.ncbi.nlm.nih.gov/gene/19206
42. Available from: https://www.ncbi.nlm.nih.gov/gene/2534
43. Available from: https://www.ncbi.nlm.nih.gov/gene/21960
44. Available from: https://www.ncbi.nlm.nih.gov/gene/25150
45. Available from: https://www.ncbi.nlm.nih.gov/gene/3371
46. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
47. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
48. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
49. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
50. Yuan Y, Yue Q, Wang Y, Du Z, Wang X, Yan F, et al.. AI-augmented intraoperative decision-making workflows in diffuse midline glioma biopsy using cryosection pathology. Nature Communications [Internet]. 2025Nov26;. Available from: https://www.nature.com/articles/s41467-025-66853-y
51. Available from: https://www.ncbi.nlm.nih.gov/gene/6469
52. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
53. Huang Y, Fang W. TREM2-mediated regulation of myeloid cells in the tumor microenvironment: new insights and therapeutic prospects. npj Precision Oncology [Internet]. 2025Nov18;9(1). Available from: https://www.nature.com/articles/s41698-025-01152-9
54. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
55. Chinopoulos C. Catabolic rewiring in cancer impacts dietary interventions. Communications Biology [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s42003-025-09333-9
56. Shimizu T, Prinz M. Microglia across evolution: from conserved origins to functional divergence. Cellular &amp; Molecular Immunology [Internet]. 2025Nov21;22(12). Available from: https://www.nature.com/articles/s41423-025-01368-6
57. Available from: http://json-schema.org/draft-07/schema#",
