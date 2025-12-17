# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma (including IDH-mutant and IDH-wild-type variants)
- Tissue: Central nervous system (brain)

## Input Genes
SOX6, FGF12, CADM2, SMOC1, PDE4B, KIF13A, MAML2, FGF14, COL11A1, VCAN, PLAAT1, ALCAM, MEGF11, UST, GRID2, FYN, VCAN-AS1, DNM3, OPCML, DSCAM, OPHN1, MAP2, TNR, ZNF804A, AL512308.1, ... (200 total)

## Program: Glial Lineage Specification and Maintenance
This program encompasses transcription factors and regulatory proteins governing astrocyte specification and maintenance of astrocytic identity. SOX family transcription factors (SOX10, SOX8, SOX6) coordinate with RBPJ, a downstream effector of Notch signaling, to promote astrocytic differentiation while suppressing alternative neural cell fates. In astrocytomas, dysregulation of these lineage-specifying factors permits plasticity and escape from differentiation constraints that normally maintain stable astrocytic identity. OLIG1, an oligodendrocyte-specifying factor, participates in mutual antagonism with astrocyte-promoting genes, creating complex lineage decision nodes. The presence of SOX2-OT, a long non-coding RNA regulating SOX2 expression, indicates active regulation of stemness characteristics.

**Predicted impacts**
- Altered lineage commitment and loss of stable astrocytic identity
- Enhanced cellular plasticity enabling transdifferentiation between neural cell fates
- Acquisition of progenitor-like characteristics with enhanced proliferation
- Dysregulated response to differentiation signals and loss of growth constraints

**Evidence summary**
The glial lineage specification program represents a core astrocyte identity maintenance system that becomes dysregulated in astrocytomas to permit enhanced plasticity and proliferation. SOX transcription factors (SOX10, SOX8, SOX6) form the transcriptional core of this program, with SOX10 serving as a master regulator of glial differentiation. These factors interact with RBPJ, which functions downstream of Notch signaling to reinforce astrocytic fate. OLIG1 creates mutual antagonism with astrocyte-promoting genes, permitting lineage plasticity under specific microenvironmental conditions. The presence of SOX2-OT indicates active regulation of neural stemness characteristics. In astrocytomas, dysregulation of this program through altered SOX factor expression or RBPJ signaling abolishes the stable lineage commitment characteristic of normal astrocytes, enabling cellular plasticity that supports tumor evolution and adaptation to different microenvironmental conditions.

**Atomic biological processes**
- Lineage specification and cell fate determination. Genes: SOX10, SOX8, SOX6, RBPJ, OLIG1
  - [6]: SOX8 and SOX9 act redundantly for glial differentiation in neural development
  - [44]: Notch1-RBPJ pathway promotes astrocytic differentiation
- Stemness and progenitor cell maintenance. Genes: SOX2-OT, SOX10, RBPJ
  - [34]: SOX2 expression associated with neural progenitor identity
  - [37]: Ascl1 regulates neuronal versus oligodendrocyte differentiation

**Required genes (not in input)**
- Genes: SOX2, SOX9, STAT3, NFIA, NFIB
  - [6]: SOX2 and SOX9 are critical for neural stem cell and glial differentiation
  - [18]: STAT3 regulates astrocyte differentiation downstream of signaling pathways

**Program citations**
- [6]: SOX genes regulate glial differentiation during neural development
- [18]: Ascl1-mediated astrocyte-to-neuron conversion demonstrates retained plasticity in astrocytes
- [37]: Astrocyte reprogramming potential linked to transcriptional modifications
- [44]: Notch-RBPJ pathway regulates astrocyte differentiation

## Program: Neuronal Differentiation and Glutamatergic Synaptic Function
This program encompasses genes promoting neuronal differentiation, including neuronal transcription factors and neuron-specific genes involved in synaptic transmission. The presence of glutamate ionotropic receptors (GRIA2, GRIA3, GRIA4, GRID2), postsynaptic scaffold proteins (DLGAP1), and auxiliary proteins (NXPH1, LRRTM4) indicates that astrocytomas aberrantly express glutamatergic synaptic machinery. While this may reflect low-level neuronal differentiation, mounting evidence suggests instead that glioma cells co-opt glutamatergic receptor signaling to support proliferation and migration through non-neuronal mechanisms. DISC1 and other neuronal development genes further indicate reactivation of developmental neuronal programs.

**Predicted impacts**
- Aberrant expression of glutamate receptors supporting non-neuronal proliferation signaling
- Altered calcium signaling through ionotropic receptor-mediated cation influx
- Enhanced migration and invasion through co-opted axonal guidance mechanisms
- Dysregulated postsynaptic scaffolding supporting altered cell-cell contacts

**Evidence summary**
Astrocytomas frequently express neuronal genes despite their glial origin, reflecting either partial neuronal differentiation or pathological co-option of neuronal gene expression programs. The input list includes multiple glutamate ionotropic receptor genes (GRIA2, GRIA3, GRIA4, GRID2) alongside postsynaptic scaffolding proteins (DLGAP1) and auxiliary proteins (NXPH1, LRRTM4) that normally assemble excitatory synapses in neurons. Evidence from glioma studies demonstrates that glioma cells expressing functional glutamate receptors display enhanced proliferation and calcium signaling in response to glutamate, distinct from the synaptic mechanisms in neurons. Additionally, axonal guidance molecules (DCC, SLIT1, EPHB1, SEMA5B, SEMA6D) normally directing neuronal growth cones become dysregulated in astrocytomas, with their altered expression patterns affecting tumor cell migration. The presence of DISC1, a gene implicated in neurodevelopmental processes, further indicates reactivation of developmentally-regulated neuronal programs within tumor cells. Collectively, this program represents a pathological co-option of neuronal gene expression mechanisms to support tumor progression rather than genuine neuronal differentiation.

**Atomic biological processes**
- Glutamate ionotropic receptor signaling and synaptic transmission. Genes: GRIA2, GRIA3, GRIA4, GRID2, DLGAP1, NXPH1, LRRTM4
  - [18]: GRIA2 expression in neurons and regulation of AMPA receptor localization
  - [4]: Glutamate receptor expression in high-grade gliomas
- Axonal guidance and neuronal morphogenesis. Genes: DCC, SLIT1, EPHB1, SEMA5B, SEMA6D, MAP2
  - [18]: DCC-netrin interaction in axonal guidance during neural development
- Synaptic vesicle trafficking and exocytosis. Genes: DNM3, REPS2, SLC1A1
  - [37]: Neurotransmitter release machinery in neurons

**Atomic cellular components**
- Postsynaptic density and synaptic scaffold. Genes: DLGAP1, GRIA2, GRIA3, GRIA4, LRRTM4
  - [18]: DLGAP1 functions as major postsynaptic scaffolding protein at excitatory synapses

**Required genes (not in input)**
- Genes: GRIN1, GRIN2A, GRIN2B, SYN1, SYNAPSIN1
  - [18]: NMDA receptor subunits and synaptic vesicle proteins required for synaptic function

**Program citations**
- [4]: High-grade gliomas display altered glutamate receptor expression and calcium signaling
- [18]: Astrocyte-to-neuron conversion mechanisms and neuronal differentiation pathways
- [37]: Neuronal gene expression in astrocytes during directed reprogramming

## Program: Cell Adhesion and Recognition Molecules
This program governs cell-cell adhesion, cell recognition, and the organization of cell-cell contacts essential for maintaining tissue architecture. The program encompasses classical cadherins (PCDH15, PCDH11X, CDH13), neural cell adhesion molecules (NCAM2, NRCAM, ALCAM, CNTN3), and postsynaptic scaffolding proteins organizing adherens junctions and synaptic contacts (CTNNA3, PKP4). Loss or alteration of adhesion molecule expression frequently occurs in cancers and facilitates enhanced cell migration and invasion. In astrocytomas, dysregulation of this program permits cells to escape normal growth constraints imposed by contact inhibition and enables migration through the brain parenchyma.

**Predicted impacts**
- Loss of contact inhibition and escape from growth constraints
- Enhanced single-cell migration through disrupted cell-cell contacts
- Altered mechanical signaling through diminished adhesion strength
- Dysregulated interaction with infiltrating immune cells

**Evidence summary**
Cell adhesion molecule dysregulation represents a hallmark of malignant transformation, enabling transformed cells to escape growth suppression imposed by contact with neighboring cells and facilitating migration through tissue barriers. The input list includes multiple cadherin family members (PCDH15, PCDH11X, CDH13) and neural adhesion molecules (NCAM2, NRCAM, ALCAM, CNTN3) whose altered expression patterns distinguish tumor cells from normal astrocytes. CTNNA3, encoding catenin alpha-3, links classical cadherins to the actin cytoskeleton and participates in Wnt-beta-catenin signaling, a pathway frequently dysregulated in cancers. PKP4, encoding plakoglobin, functions in desmosomal adhesion and represents another adhesion complex component frequently altered in cancers. TNR, encoding tenascin R, decorates the perineuronal nets surrounding inhibitory neurons and becomes altered in gliomas, affecting interactions between tumor cells and peritumoral neurons. The coordinated dysregulation of multiple adhesion molecule categories within astrocytomas creates a permissive environment for enhanced migration while potentially enabling escape from immune surveillance through altered recognition by infiltrating immune cells.

**Atomic biological processes**
- Classical cadherin-mediated cell-cell adhesion. Genes: PCDH15, PCDH11X, CDH13, CTNNA3
  - [2]: Beta-catenin signaling regulation of adherens junctions
  - [7]: Cadherin-mediated cell-cell adhesion in tumor biology
- Neural cell recognition and synaptic adhesion. Genes: NCAM2, NRCAM, ALCAM, CNTN3, NXPH1
  - [18]: Neural cell adhesion molecules in neurodevelopment and neural tissue organization
- Adherens junction and desmosomal organization. Genes: CTNNA3, PKP4, TNR
  - [7]: PKP4 functions in desmosomal adhesion and cell contact

**Atomic cellular components**
- Adherens junction complex. Genes: CTNNA3, PCDH15, PCDH11X, CDH13, PKP4
  - [2]: Catenin proteins link cadherins to actin cytoskeleton

**Required genes (not in input)**
- Genes: CDH1, CDH2, CTNNB1, APC
  - [2]: Classical cadherins and canonical Wnt-beta-catenin signaling regulate cell adhesion

**Program citations**
- [2]: Beta-catenin and cadherin signaling in tissue organization
- [7]: Patient-derived tumoroids maintain adhesion molecule expression patterns

## Program: Growth Factor Receptor Signaling and Oncogenic Proliferation
This program encompasses dysregulation of growth factor receptors and their downstream signaling effectors driving enhanced proliferation, survival, and migration in astrocytomas. PDGFRA and PDGFC represent core components of the PDGF autocrine signaling loop frequently dysregulated through gene amplification and activating mutations in astrocytomas. ERBB3 and ERBB4, members of the ErbB family of receptor tyrosine kinases, undergo overexpression or activation through dysregulation of upstream regulators including microRNAs. FGF12 and FGF14 encode intracellular FGF variants modulating ion channel function downstream of growth factor stimulation. Together, these components create multiple redundant growth factor signaling inputs supporting tumor cell proliferation.

**Predicted impacts**
- Constitutive activation of PI3K/AKT survival signaling
- Enhanced MAPK/ERK cascade activation supporting proliferation
- Dysregulated calcium signaling through FGF-modulated ion channels
- Increased cell motility and invasion through growth factor-driven cytoskeletal reorganization
- Altered metabolic reprogramming supporting rapid proliferation

**Evidence summary**
Growth factor receptor dysregulation represents one of the most consistent and functionally important alterations in astrocytomas across all molecular subtypes. PDGFRA undergoes frequent amplification and activating mutation in gliomas, with PDGFRA-amplified tumors showing enhanced proliferation and more aggressive clinical behavior. The ligand PDGFC, present in the input list, provides autocrine stimulation of PDGFRA when produced by tumor cells or paracrine stimulation when produced by tumor-associated fibroblasts. PDGFRA engagement triggers multiple downstream signaling pathways including the PI3K/AKT axis supporting survival, the MAPK/ERK cascade promoting proliferation, and phospholipase C activation generating calcium mobilization signals. ERBB3 and ERBB4 undergo dysregulation through multiple mechanisms including direct gene amplification, increased transcription through altered lineage specifier expression, and dysregulation of suppressive microRNAs. FGF12 and FGF14, encoding intracellular FGF variants, modulate ion channel function and cellular excitability downstream of growth factor stimulation, integrating growth factor signaling with ion channel biology. The presence of multiple growth factor receptors within a single program indicates that astrocytomas frequently display simultaneous dysregulation of several growth factor signaling pathways, creating redundancy that impedes single-agent targeted therapy and explains the limited efficacy of monotherapy approaches.

**Atomic biological processes**
- PDGF receptor activation and PDGF autocrine/paracrine signaling. Genes: PDGFRA, PDGFC
  - [9]: PDGFRA dysregulation in glioblastoma supports proliferation and migration
  - [4]: PDGFRA alterations in high-grade gliomas
- ErbB family receptor signaling and HER3/HER4 activation. Genes: ERBB3, ERBB4
  - [5]: ERBB3 overexpression and miR-205 dysregulation in glioblastoma
  - [8]: ERBB4 signaling in neural tissue and cancer
- Intracellular FGF-mediated ion channel modulation. Genes: FGF12, FGF14
  - [13]: FGF receptor activation in cancer biology
  - [15]: FGF signaling in fibroblast growth and cancer

**Required genes (not in input)**
- Genes: PI3K, AKT1, MAPK1, MAPK3, PLCG
  - [4]: Growth factor receptors activate PI3K/AKT and MAPK/ERK pathways in gliomas
  - [9]: PDGFRA activation requires AKT and ERK signaling

**Program citations**
- [4]: Comprehensive characterization of glioma driver alterations including PDGFRA and growth factor pathways
- [5]: ERBB3 dysregulation and microRNA-mediated regulation in glioblastoma
- [7]: Patient-derived tumoroids with PDGFRA and ERBB family alterations
- [9]: PDGFRA-EGFRvIII signaling in glioblastoma requires PDGFRA co-signaling

## Program: Extracellular Matrix Remodeling and Collagen Organization
This program encompasses genes regulating synthesis, deposition, and remodeling of the extracellular matrix, transforming the normal brain ECM into a fibrotic, collagen-rich tumor microenvironment. COL11A1 and COL20A1 encode fibrillar collagens normally restricted to connective tissues but aberrantly expressed in gliomas where they contribute to altered mechanical properties. VCAN and VCAN-AS1 represent versican proteoglycan and its antisense transcript, jointly regulating versican expression, a major brain ECM component enriched in gliomas. UST catalyzes sulfation of glycosaminoglycans modifying proteoglycan function. MMP16, ADAMTS20, and ADAMTS6 represent proteolytic enzymes degrading ECM components. SMOC1 and related ECM modifiers influence ECM structure and growth factor bioavailability.

**Predicted impacts**
- Increased interstitial fluid pressure and altered nutrient diffusion
- Enhanced tumor cell migration through altered ECM physical properties
- Modified growth factor sequestration and bioavailability
- Altered mechanical signaling through collagen-integrin interactions
- Dysregulated neuroimmune interactions through ECM composition changes

**Evidence summary**
Transformation from normal brain parenchyma to astrocytoma involves profound remodeling of the extracellular matrix, transitioning from the relatively protease-poor, hyaluronic acid-rich brain ECM to a collagen-rich, fibrotic tumor microenvironment. COL11A1 and COL20A1, encoding fibrillar collagens normally restricted to connective tissues, become aberrantly expressed in astrocytomas and contribute to altered mechanical properties supporting enhanced cell migration. VCAN, encoding versican, represents one of the most abundant proteoglycans in brain ECM; its elevation in gliomas reflects increased synthesis or altered degradation. VCAN-AS1, the natural antisense transcript to VCAN, likely functions as a competing endogenous RNA that sequesters microRNAs and influences VCAN steady-state expression levels. UST catalyzes sulfation of glycosaminoglycans on proteoglycans, influencing their interaction with growth factors and cell surface receptors. MMP16, a membrane-anchored collagenase, facilitates physical ECM remodeling and tumor cell invasion, while ADAMTS proteases cleave proteoglycans into fragments that may themselves serve as migration-promoting signals. SMOC1 interacts with ECM proteins and growth factors, modifying their bioavailability and signaling capacity. The coordinated dysregulation of these ECM genes transforms the tumor microenvironment from a relatively diffusion-limited, mechanically soft neural tissue into a mechanically stiff, collagen-rich matrix supporting altered cell migration behaviors.

**Atomic biological processes**
- Collagen synthesis and deposition. Genes: COL11A1, COL20A1
  - [3]: COL1A1 effects on vascular wall composition in thoracic aortic aneurysm
- Versican and proteoglycan regulation. Genes: VCAN, VCAN-AS1, UST
  - [1]: Proteoglycan composition of tumor extracellular matrix
- Matrix metalloproteinase-mediated ECM degradation. Genes: MMP16, ADAMTS20, ADAMTS6
  - [1]: Proteolytic remodeling of extracellular matrix in tumors
- ECM-derived growth factor modulation. Genes: SMOC1
  - [1]: SMOC1 regulation of growth factor bioavailability

**Atomic cellular components**
- Fibrillar collagen matrix. Genes: COL11A1, COL20A1
  - [3]: Type I collagen organization in structural tissues
- Proteoglycan and glycosaminoglycan matrix. Genes: VCAN, UST
  - [1]: Versican and other brain ECM proteoglycans

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP1, TIMP2
  - [1]: Matrix metalloproteinases and their inhibitors regulate ECM remodeling

**Program citations**
- [1]: Autophagy-related gene expression and tumor biology
- [3]: Collagen effects on tissue remodeling

## Program: Voltage-Gated Ion Channels and Neuronal Excitability
This program encompasses genes encoding voltage-gated ion channels and regulatory proteins modulating cellular excitability. Astrocytomas aberrantly express neuronal ion channel isoforms including SCN1A and SCN3A (voltage-gated sodium channels), KCNIP4 (potassium channel modulator), and P2RX7 (ATP-gated cation channel). These channels establish cellular membrane potential, repolarization kinetics, and calcium dynamics through voltage-dependent calcium entry. Enhanced ion channel expression in astrocytomas confers neuron-like electrophysiological properties distinct from normal astrocytes, potentially supporting altered migration behaviors and calcium signaling affecting tumor progression.

**Predicted impacts**
- Enhanced sodium-dependent depolarization and action potential generation
- Altered calcium signaling through voltage-dependent calcium entry
- Increased ATP sensitivity and purinergic signaling responsiveness
- Modified membrane potential affecting proliferation and migration
- Enhanced inflammasome activation through P2RX7-mediated ATP sensing

**Evidence summary**
Astrocytomas aberrantly express voltage-gated ion channels normally restricted to neurons, conferring neuron-like electrophysiological properties to tumor cells. SCN1A and SCN3A encode voltage-gated sodium channels with distinct biophysical properties; SCN1A mutations cause genetic epilepsy with febrile seizures, while SCN3A represents a fetal/embryonic isoform normally replaced by mature isoforms during development. Reactivation of SCN3A in astrocytomas reflects developmental dedifferentiation and reacquisition of embryonic electrophysiological characteristics. KCNIP4 encodes a potassium channel interacting protein modulating voltage-gated potassium channels critical for membrane repolarization. P2RX7, encoding the ATP-gated P2X7 receptor, opens a non-selective cation channel in response to extracellular ATP and mediates inflammasome activation in immune cells. Enhanced P2RX7 expression in gliomas supports altered ATP responsiveness and potentially contributes to modified tumor immune microenvironment through altered cytokine production. Collectively, enhanced ion channel expression in astrocytomas confers neuron-like excitability supporting altered migration, calcium signaling, and potential direct effects on proliferation through as-yet-undefined mechanisms.

**Atomic biological processes**
- Voltage-gated sodium channel function and action potential generation. Genes: SCN1A, SCN3A
  - [10]: SCN1A encodes voltage-gated sodium channel alpha subunit
  - [12]: SCN2A sodium channel in neurological disease
- Potassium channel regulation and membrane potential. Genes: KCNIP4
  - [14]: AKT signaling and ion channel regulation in cellular proliferation
- ATP-gated purinergic signaling and inflammasome activation. Genes: P2RX7
  - [21]: CD47/SIRPA pathway and immune escape in glioblastoma
  - [22]: P2RX7 and immune checkpoint pathways in glioblastoma

**Atomic cellular components**
- Voltage-gated sodium channel complex. Genes: SCN1A, SCN3A
  - [10]: Sodium channel structure and function

**Required genes (not in input)**
- Genes: KCND2, KCND3, KCNH2, HCN1
  - [10]: Multiple voltage-gated potassium channel isoforms regulate neuronal excitability

**Program citations**
- [10]: Sodium channel structure and developmental expression
- [12]: Sodium channel alterations in neurological disease
- [21]: P2RX7 in immune-astrocyte interactions
- [22]: P2RX7 knockout affects glioblastoma proliferation and immune responses

## Program: Receptor Tyrosine Kinase Signaling Through Ras-ERK and PI3K-AKT Cascades
This program encompasses signal transduction molecules downstream of receptor tyrosine kinases, mediating proliferation and survival signals through the classical MAPK/ERK and PI3K/AKT cascades. FYN, a non-receptor tyrosine kinase, amplifies growth factor receptor signaling and supports integrin-dependent migration. PRKCE and related protein kinase C isoforms propagate signals downstream of phospholipase C activation following growth factor stimulation. DGKB and DGKG encode diacylglycerol kinases modulating PKC signaling intensity and duration. Collectively, these components create a complex signal transduction network translating growth factor receptor engagement into proliferation, survival, and migration.

**Predicted impacts**
- Amplified proliferation signaling through enhanced ERK phosphorylation
- Enhanced survival through increased AKT and PKC activation
- Dysregulated integrin signaling supporting migration
- Altered calcium dynamics through PKC-mediated ion channel phosphorylation
- Modified metabolic signaling through mTOR activation

**Evidence summary**
Growth factor receptor engagement initiates complex signal transduction cascades culminating in altered gene expression, cell proliferation, migration, and survival. FYN, a Src family non-receptor tyrosine kinase, functions as a key amplifier of growth factor receptor signaling and as a nodal integration point for multiple signaling inputs including integrin engagement. FYN activity phosphorylates multiple substrates including receptors, adhesion molecules, and downstream kinases, collectively promoting tumor cell migration and invasion. PRKCE, encoding protein kinase C epsilon, represents an unusual PKC isoform with cell-type-specific expression patterns. PKC activation following phospholipase C-mediated DAG generation triggers phosphorylation of numerous effector proteins supporting proliferation and survival. DGKB and DGKG encode diacylglycerol kinases that convert DAG back to phosphatidic acid, thereby regulating the intensity and duration of PKC signaling. Altered DGKB or DGKG expression would shift the balance between sustained and terminated PKC signaling, influencing how astrocytomas respond to growth factor stimulation. The presence of multiple signal transduction components indicates that astrocytomas dysregulate signaling through multiple nodes simultaneously, creating redundancy and complexity in therapeutic targeting.

**Atomic biological processes**
- Src family tyrosine kinase activation and integrin signaling amplification. Genes: FYN
  - [14]: AKT and Wnt signaling pathway integration
- Protein kinase C activation and substrate phosphorylation. Genes: PRKCE
  - [8]: ERBB4 signaling and protein kinase C involvement
- Diacylglycerol metabolism and PKC signal termination. Genes: DGKB, DGKG
  - [8]: Diacylglycerol kinases in signal transduction

**Required genes (not in input)**
- Genes: GRB2, SOS1, RAF1, MEK1, MEK2
  - [4]: Classical MAPK cascade components

**Program citations**
- [8]: ERBB family signaling and downstream effectors
- [14]: AKT signaling in neural cells and proliferation control

## Program: RNA-Binding Proteins and Post-Transcriptional Gene Regulation
This program encompasses RNA-binding proteins and long non-coding RNAs regulating post-transcriptional gene expression through effects on mRNA stability, localization, and translation efficiency. CELF2, RBMS3, KHDRBS2, and KHDRBS3 encode RNA-binding proteins promoting neuronal-specific splicing and mRNA processing. Multiple long non-coding RNAs (LINC00511, LINC02283, LINC00609, LINC01170, CCDC26) function as competing endogenous RNAs that sequester microRNAs and regulate target mRNA stability. This program creates a complex post-transcriptional regulatory landscape permitting rapid reprogramming of gene expression in response to developmental and environmental signals.

**Predicted impacts**
- Altered mRNA stability promoting expression of proliferation genes
- Dysregulated isoform selection affecting protein function and localization
- Enhanced translation of specific target mRNAs through ribosome recruitment
- Modified microRNA availability affecting multiple downstream target genes
- Rapid transcriptome remodeling without requirement for transcription factor alteration

**Evidence summary**
Post-transcriptional gene regulation represents an underappreciated but critical mechanism through which astrocytomas reprogram their transcriptomes to support tumor progression. CELF2 (CUGBP Elav-like family member 2) binds to AU-rich sequences in 3' untranslated regions, regulating mRNA stability and translation efficiency. In normal neurons, CELF2 promotes expression of neuronal differentiation genes while suppressing proliferation-associated genes. Dysregulation of CELF2 in astrocytomas could shift mRNA stability patterns to favor proliferation genes. RBMS3, KHDRBS2, and KHDRBS3 similarly regulate neuronal-specific gene expression through effects on mRNA processing and localization. NOVA1 encodes an RNA-binding protein regulating neuron-specific alternative splicing, with particular importance in regulating GABA receptor isoform selection and glycine receptor function. The presence of multiple long non-coding RNAs (LINC00511, LINC02283, LINC00609, LINC01170, CCDC26) suggests that astrocytomas exploit lncRNA-mediated microRNA sequestration to dysregulate target gene expression. These lncRNAs function as competing endogenous RNAs that bind to microRNAs and reduce their availability to suppress target mRNAs, effectively increasing target mRNA expression levels. CCDC26 represents a glioma susceptibility locus identified through genome-wide association studies, with genetic variants in CCDC26 increasing astrocytoma risk, likely through effects on its lncRNA function.

**Atomic biological processes**
- RNA-binding protein-mediated mRNA stability control. Genes: CELF2, RBMS3, KHDRBS2, KHDRBS3
  - [18]: CELF2 regulation of neuronal gene expression
  - [37]: RNA-binding proteins in astrocyte differentiation
- Alternative splicing and isoform selection. Genes: CELF2, RBMS3, KHDRBS2, KHDRBS3, NOVA1
  - [18]: RNA-binding proteins regulate neuronal-specific splicing
- MicroRNA sequestration and competing endogenous RNA function. Genes: LINC00511, LINC02283, LINC00609, LINC01170, CCDC26
  - [1]: Long non-coding RNAs in tumor biology

**Required genes (not in input)**
- Genes: ELAVL1, ELAVL2, ELAVL3, ELAVL4
  - [18]: ELAV family RNA-binding proteins regulate neuronal gene expression

**Program citations**
- [1]: Molecular alterations in tumor-intrinsic biology including post-transcriptional regulation
- [18]: Post-transcriptional modulation affecting cellular reprogramming
- [37]: RNA-binding proteins in astrocyte and neuron differentiation

## Program: Tumor Suppression and Differentiation-Promoting Pathways
This program encompasses genes functioning to suppress proliferation, promote differentiation, and maintain growth constraints in normal astrocytes. ZBTB16 encodes a transcriptional repressor promoting differentiation while suppressing proliferation in various cell types. PTCH1 functions as the Sonic Hedgehog receptor and possesses growth-suppressive functions through both classical Hedgehog pathway antagonism and non-canonical mechanisms. SOX5 promotes differentiated versus progenitor-like phenotypes in certain neural contexts. RBPJ, discussed previously in the context of lineage specification, additionally functions downstream of Notch signaling to promote astrocytic differentiation. Dysregulation of this program through loss of expression or function of these genes enables enhanced proliferation and reduced differentiation in astrocytomas.

**Predicted impacts**
- Loss of cell cycle arrest mechanisms
- Enhanced proliferation through suppression of differentiation-promoting signals
- Reduced expression of mature astrocytic markers
- Increased stemness and progenitor-like characteristics
- Impaired response to external differentiation signals

**Evidence summary**
Maintenance of stable astrocytic differentiation requires active suppression of proliferation through multiple tumor suppressor mechanisms and differentiation-promoting pathways. ZBTB16, encoding a zinc finger and BTB domain-containing protein also known as PLZF (promyelocytic leukemia zinc finger), functions as a transcriptional repressor of proliferation genes in various cell types. ZBTB16 expression typically promotes differentiation and apoptosis while suppressing proliferation; downregulation of ZBTB16 in cancers removes these growth constraints and enables enhanced proliferation. PTCH1 encodes the Sonic Hedgehog receptor and possesses dual roles in both pathway-dependent and -independent growth suppression. Beyond its function in Hedgehog pathway antagonism, PTCH1 influences cell cycle progression and apoptosis through non-canonical mechanisms. Loss of PTCH1 function in various cancers contributes to enhanced proliferation and altered differentiation. SOX5, unlike the lineage-specifying SOX10 and SOX8 discussed earlier, promotes differentiation and more restricted cell fate decisions in certain neural contexts. RBPJ, downstream of Notch signaling, promotes astrocytic differentiation; its dysregulation would accordingly promote plasticity and enhanced proliferation. The coordinated dysregulation of this program in astrocytomas removes multiple growth constraints simultaneously, explaining why even tumors lacking mutations in classical tumor suppressors like TP53 display enhanced proliferation.

**Atomic biological processes**
- Transcriptional repression of proliferation genes. Genes: ZBTB16
  - [1]: Prognostic and therapeutic relevance of biomarkers in gliomas
- Hedgehog pathway antagonism and growth suppression. Genes: PTCH1
  - [41]: NOTCH3 signaling and related developmental pathways
- Differentiation promotion and stemness suppression. Genes: SOX5, RBPJ
  - [18]: SOX factors regulate differentiation versus stemness balance

**Required genes (not in input)**
- Genes: TP53, RB1, PTEN
  - [4]: Classical tumor suppressors altered in high-grade gliomas

**Program citations**
- [1]: Prognostic relevance of tumor suppression pathways
- [41]: NOTCH signaling and developmental pathways in astrocytes

## Program: Neuroinflammation and Tumor Microenvironment Remodeling
This program encompasses genes orchestrating neuroinflammatory responses and immune cell recruitment that paradoxically support tumor progression despite their inflammatory nature. NF-kappaB1, TNF, and IL6 drive pro-inflammatory cytokine production creating a chronically inflamed tumor microenvironment. NOTCH3 signaling in astrocytes promotes microglial activation and IL-6 production. SIRPA engagement by CD47 on tumor cells delivers inhibitory signals to myeloid cells, suppressing immune responses. The coordinated dysregulation of neuroinflammatory genes creates an immunosuppressive, protumoral microenvironment supporting tumor progression.

**Predicted impacts**
- Enhanced recruitment of immunosuppressive myeloid-derived suppressor cells
- Expansion of regulatory T cells through IL-6 and TGF-beta signaling
- Reduced cytotoxic T-cell infiltration through checkpoint pathway activation
- Promotion of alternative activated macrophages with pro-tumoral functions
- Enhanced vascular permeability and immune cell infiltration into tumors

**Evidence summary**
Paradoxically, chronic neuroinflammation within astrocytomas typically supports rather than suppresses tumor progression through recruitment and polarization of immunosuppressive cell types. NFKB1, encoding the p50/p105 component of NF-kappaB, serves as a central hub integrating inflammatory signals from multiple sources. TNF and IL6, major pro-inflammatory cytokines, are produced by both tumor cells and infiltrating immune cells and promote NF-kappaB activation in a positive feedback loop. TNF signaling through TNFR1 simultaneously promotes NF-kappaB activation and programmed cell death receptor signaling; in astrocytomas, the proliferation-promoting effects typically predominate over apoptotic signals. IL6 functions as a critical driver of STAT3 activation and promotes immunosuppression through expansion of myeloid-derived suppressor cells and regulatory T cells. NOTCH3, encoding Notch receptor 3, influences microglial activation state through astrocytic DLL4-NOTCH signaling that promotes IL-6 production and neuroinflammation. SIRPA represents a signal regulatory protein expressed on myeloid cells that delivers inhibitory signals upon CD47 engagement, reducing phagocytic activity and promoting immune tolerance. The coordinated dysregulation of this program creates a chronically inflamed yet paradoxically immunosuppressive microenvironment that supports tumor progression through multiple mechanisms including growth factor production by infiltrating immune cells, physical insulation of tumor cells from cytotoxic lymphocytes, and angiogenic signaling.

**Atomic biological processes**
- NF-kappaB-mediated pro-inflammatory cytokine production. Genes: NFKB1, TNF, IL6
  - [16]: mTOR/NF-kappaB pathway in neuroinflammation
  - [29]: NF-kappaB mediates glioblastoma growth through IL-1beta
- Notch-mediated microglial activation and IL-6-STAT3 signaling. Genes: NOTCH3
  - [41]: NOTCH3 signaling promotes neuroinflammation
  - [44]: Astrocytic DLL4-NOTCH1 signaling axis
- Immune checkpoint signaling and myeloid cell inhibition. Genes: SIRPA
  - [21]: CD47/SIRPA immune escape pathway
  - [22]: CD274 (PD-L1) immune checkpoint expression in glioblastoma

**Required genes (not in input)**
- Genes: IL1B, TGF-beta, STAT3, MERTK
  - [20]: Neuroinflammatory mediators in brain injury

**Program citations**
- [16]: Neuroinflammatory pathways in brain pathology
- [21]: Signal regulatory protein pathways in immune escape
- [29]: NF-kappaB pathway in glioblastoma progression

## Program: Developmental Plasticity, Progenitor Identity, and Self-Renewal
This program encompasses genes maintaining progenitor-like characteristics and developmental plasticity within astrocytomas, enabling enhanced self-renewal and reduced commitment to terminal differentiation. SOX2-OT and SOX2-regulated genes maintain neural progenitor identity. NES, encoding nestin, serves as a marker of neural progenitor cells. DOCK10 and related migration-promoting genes enable progenitor-like migratory capacity. The activation of developmental plasticity programs in astrocytomas enables enhanced proliferation and adaptation to changing microenvironmental conditions while maintaining escape from terminal differentiation.

**Predicted impacts**
- Enhanced self-renewal and reduced terminal differentiation
- Increased proliferation rate through escape from differentiation-imposed growth constraints
- Enhanced migration capacity through reactivation of developmental migration machinery
- Maintained responsiveness to stemness-promoting signaling (Wnt, Notch, FGF)
- Acquisition of multipotency enabling differentiation into multiple neural cell types

**Evidence summary**
Astrocytomas frequently display characteristics of neural progenitor cells, including enhanced self-renewal, reduced terminal differentiation, and heightened responsiveness to proliferation signals. SOX2, a master regulator of neural stem cell and progenitor identity, maintains stemness through transcriptional regulation of genes supporting self-renewal while suppressing differentiation-promoting genes. SOX2-OT, a long non-coding RNA transcribed from the SOX2 locus, regulates SOX2 expression levels through mechanisms involving microRNA sequestration. NES, encoding nestin, represents a classical intermediate filament protein expressed in neural progenitor cells but downregulated during differentiation; reactivation of NES in astrocytomas indicates partial reversion to an embryonic, progenitor-like state. DOCK10, encoding dedicator of cytokinesis 10, participates in Cdc42-mediated cell migration through effects on actin cytoskeleton reorganization. During normal neural development, neural progenitor cells migrate extensively along radial glia and between germinal zones; reactivation of progenitor-associated migration machinery in astrocytomas enables enhanced single-cell migration through brain parenchyma, a critical prerequisite for invasive tumor growth. The coordinated activation of stemness and migration programs in astrocytomas creates cells with both enhanced proliferative capacity (through reduced differentiation constraints) and enhanced migratory potential (through reactivation of developmental migration machinery), collectively supporting aggressive tumor progression.

**Atomic biological processes**
- Neural progenitor self-renewal and stemness maintenance. Genes: SOX2-OT, NES
  - [18]: SOX2 regulation of neural stem cell identity
  - [34]: SOX2 and cell-type-specific transcriptomic signatures
  - [37]: Neural progenitor characteristics in reprogrammed cells
- Progenitor cell migration and developmental motility. Genes: DOCK10
  - [18]: Neural progenitor cell migration during development

**Atomic cellular components**
- Intermediate filament cytoskeleton. Genes: NES
  - [39]: Nestin as intermediate filament protein in neural cells

**Required genes (not in input)**
- Genes: SOX2, PAX6, NOTCH1, JAG1
  - [18]: Notch-Jagged signaling in neural progenitor maintenance
  - [34]: SOX2 and PAX6 in neural progenitor specification

**Program citations**
- [18]: Neural progenitor characteristics in reprogrammed astrocytes
- [34]: SOX2 and neural stem cell markers in cell type-specific analysis
- [37]: SOX2-regulated neural progenitor programs
- [39]: Nestin expression in neural progenitor and stem cells

## Bibliography
1. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
2. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
3. Available from: https://www.ncbi.nlm.nih.gov/gene/1277
4. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
5. Available from: https://www.ncbi.nlm.nih.gov/gene/2065
6. Available from: https://www.ncbi.nlm.nih.gov/gene/20682
7. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
8. Available from: https://www.ncbi.nlm.nih.gov/gene/2066
9. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
10. Available from: https://www.ncbi.nlm.nih.gov/gene/6323
11. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
12. Available from: https://www.ncbi.nlm.nih.gov/gene/6326
13. Available from: https://www.ncbi.nlm.nih.gov/gene/2260
14. Available from: https://www.ncbi.nlm.nih.gov/gene/207
15. Available from: https://www.ncbi.nlm.nih.gov/gene/2247
16. Available from: https://www.ncbi.nlm.nih.gov/gene/18033
17. Philipp K, Jacob SY, Maarten MJW, Tommaso S, Nico T, Alba C, et al.. A prognostic classification system for extent of resection in IDH-mutant grade 2 glioma: an international, multicentre, retrospective cohort study with external validation by the RANO resect group.. The Lancet Oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41308678/
18. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
19. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
20. Available from: https://www.ncbi.nlm.nih.gov/gene/140885
21. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
22. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
23. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
24. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
25. Available from: https://www.ncbi.nlm.nih.gov/gene/9839
26. Available from: https://www.ncbi.nlm.nih.gov/gene/22601
27. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
28. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
29. Available from: https://www.ncbi.nlm.nih.gov/gene/25937
30. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
31. H HJ, S ZZ, S L. [Molecular subtype-driven surgical concepts and clinical application in gliomas].. Zhonghua wai ke za zhi [Chinese journal of surgery] [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41292395/
32. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
33. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
34. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
35. Available from: https://www.ncbi.nlm.nih.gov/gene/10763
36. Available from: https://www.ncbi.nlm.nih.gov/gene/2064
37. Available from: https://www.ncbi.nlm.nih.gov/gene/4854
38. Available from: https://www.ncbi.nlm.nih.gov/gene/5175
39. Available from: https://www.ncbi.nlm.nih.gov/gene/18128
40. Available from: https://www.ncbi.nlm.nih.gov/gene/177
41. Available from: their known roles in astrocyte development
