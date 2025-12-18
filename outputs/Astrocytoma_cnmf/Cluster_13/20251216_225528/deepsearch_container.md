# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and astrocytoma-derived tumor cells
- Disease: Astrocytoma
- Tissue: Brain (intracranial origin)

## Input Genes
KHDRBS2, SMOC1, GULP1, GLCCI1, PTPRO, SH3D19, EYA1, EPCAM-DT, SLC24A3, SATB1-AS1, SYT16, TCF7L1, MTAP, AL139393.1, KCNMB2-AS1, KCNMB2, KCND3, GRIK3, IGF2BP3, KCNQ1, KCNQ1OT1, HIP1, KCTD8, HAPLN1, AC003991.1, ... (200 total)

## Program: MAPK/ERK Pathway Signaling and Proliferation Control
This program encompasses dysregulation of receptor tyrosine kinase signaling (EGFR), downstream kinase cascade amplification (MAP3K1), cell cycle checkpoint disruption through CDK6-mediated G1/S transition, and integration of second messenger signaling through protein kinase C family members. The program collectively drives proliferation and overcomes growth arrest through multiple reinforcing mechanisms.

**Predicted impacts**
- Enhanced growth factor signaling and proliferation
- Bypass of G1/S checkpoint restraint
- Increased replication initiation and DNA synthesis
- Calcium signaling-mediated transcription and survival
- Therapeutic resistance through redundant pathway activation

**Evidence summary**
Astrocytomas, particularly those with BRAF alterations in pediatric low-grade disease or EGFR amplification in high-grade disease, demonstrate dysregulation of multiple MAPK/ERK pathway components. EGFR serves as a classical ligand-activated tyrosine kinase initiating phosphoinositide 3-kinase and mitogen-activated protein kinase cascades. MAP3K1 functions as a kinase kinase kinase amplifying downstream signaling. CDK6 controls G1/S phase transition and overcomes cell cycle checkpoint inhibition through replication stress induction. Protein kinase C family members mediate second messenger signaling downstream of growth factor receptors. The presence of multiple pathway components in the input gene list, in combination with evidence that KIAA1549:BRAF fusion constitutively activates MAPK signaling in pilocytic astrocytomas and EGFR amplification occurs in high-grade gliomas, indicates that MAPK/ERK dysregulation represents a critical driver of astrocytoma proliferation.

**Atomic biological processes**
- Receptor tyrosine kinase signaling. Genes: EGFR
  - [5]: EGFR family receptor tyrosine kinase signaling commonly dysregulated in cancer through amplification or activating mutations, activating downstream phosphoinositide 3-kinase and mitogen-activated protein kinases
  - [6]: EGFR overexpression and amplification frequently reported in cholangiocarcinoma, correlating with advanced disease and reduced survival
- Kinase cascade amplification. Genes: MAP3K1
  - [29]: MAP3K1 expression associated with progression and poor prognosis of hormone receptor-positive, HER2-negative early-stage breast cancer
  - [49]: TOPK activates key signaling pathways such as ERK/RSK/c-Jun through phosphorylation, promoting cancer cell proliferation and migration
- G1/S cell cycle checkpoint control. Genes: CDK6
  - [13]: CDK6 upregulation overcomes G1/S phase cell cycle arrest, associated with increased replication stress and therapeutic resistance
  - [16]: CDK6 encodes cyclin-dependent kinase that plays important roles in progression and regulation of cell cycle
- Second messenger signaling. Genes: PRKCA, PRKD1
  - [14]: PKC regulates intracellular calcium signaling and secretion of apoE from primary human macrophages
  - [17]: PKC-alpha mediates acetylcholine-induced receptor-mediated TRPV4 activation and calcium signaling

**Required genes (not in input)**
- Genes: BRAF, KRAS, PIK3CA, AKT1, ERK1, ERK2, MEK1, MEK2
  - [5]: PIK3CA mutations occur in 36% of EGFR-amplified tumors; AKT amplification occurs in 29.3%
  - [47]: BRAF alterations represent key driver mutations in pediatric gliomas

**Program citations**
- [1]: High frequency of KIAA1549:BRAF fusion in pilocytic astrocytomas
- [5]: EGFR amplification occurs in 3.2–6.7% of triple-negative breast cancers and is associated with poor survival
- [47]: Pediatric gliomas harbor alterations in receptor tyrosine kinases including EGFR and demonstrate MAPK pathway dysregulation
- [50]: Patient-derived tumoroids of pediatric astrocytomas preserve BRAF and KIAA1549::BRAF driver alterations

## Program: Ion Channel Electrophysiology and Calcium Homeostasis
This program encompasses regulation of cellular excitability through voltage-gated potassium channels, calcium influx through high-voltage-activated calcium channels and transient receptor potential channels, and integration of calcium signaling into downstream transcriptional and metabolic processes. The program collectively maintains calcium homeostasis while enabling calcium-dependent proliferative and survival signaling.

**Predicted impacts**
- Altered cellular excitability and membrane potential dynamics
- Enhanced calcium signaling-dependent proliferation and survival
- Integration of calcium signals into MAPK and CREB-mediated transcription
- Metabolic reprogramming through calcium-dependent mitochondrial signaling
- Potential promotion of neuronal-like electrophysiology in transformed cells

**Evidence summary**
The input gene list contains striking enrichment of ion channel genes encoding voltage-gated potassium channels (KCNMB2, KCND3, KCNQ1), high-voltage-activated calcium channels (CACNA1E, CACNA2D1), and transient receptor potential cation channels (TRPC1, TRPC3, TRPC4). These channels collectively mediate cellular excitability and calcium homeostasis. Voltage-gated calcium channels play crucial roles in hippocampal seizure dynamics, suggesting retained neural-like properties in astrocytomas. Calcium influx through these channels activates downstream transcriptional programs including CREB phosphorylation and ERK activation, processes central to proliferation and survival. Recent evidence indicates that TRPC3-mediated calcium signaling shapes endoplasmic reticulum-mitochondria calcium transfer characteristic of tumor-promoting senescence, suggesting that dysregulated calcium homeostasis contributes to astrocytoma growth.

**Atomic biological processes**
- Potassium channel-mediated membrane potential regulation. Genes: KCNMB2, KCND3, KCNQ1
  - [15]: Voltage-gated calcium channel R-type plays crucial role in hippocampal ictogenesis and seizure generalization
- High-voltage-activated calcium influx. Genes: CACNA1E, CACNA2D1
  - [18]: Alpha-1E subunit of R-type calcium channels belongs to high-voltage activated group involved in modulation of neuronal excitability
- Store-operated and receptor-operated calcium entry. Genes: TRPC1, TRPC3, TRPC4
  - [64]: TRPC1/Orai1 forms complex that mediates calcium influx and nitric oxide production via store-operated calcium channel
  - [67]: TRPC3 shapes ER-mitochondria calcium transfer characterizing tumor-promoting senescence

**Atomic cellular components**
- Voltage-gated potassium channels. Genes: KCNMB2, KCND3, KCNQ1
  - [15]: Voltage-gated calcium channels regulate neuronal excitability
- High-voltage-activated calcium channels. Genes: CACNA1E, CACNA2D1
  - [18]: R-type calcium channels represent high-voltage-activated group
- Transient receptor potential cation channels. Genes: TRPC1, TRPC3, TRPC4
  - [64]: TRPC channels mediate calcium influx through store-operated and receptor-operated mechanisms

**Required genes (not in input)**
- Genes: CREB, ERK1/2, CALMODULIN, RYANODINE_RECEPTOR, IP3_RECEPTOR, SERCA
  - [8]: CREB pathway activation occurs downstream of ERK phosphorylation in response to metabolic changes

**Program citations**
- [8]: Ketogenic diet enhances long-term potentiation and calcium-dependent signaling in Alzheimer disease models
- [15]: Voltage-gated calcium channels regulate neuronal excitability and seizure dynamics
- [60]: Voltage-gated calcium channel disinhibition increases presynaptic calcium and glutamate release
- [64]: TRPC1 forms store-operated calcium channels regulating calcium homeostasis
- [67]: TRPC3 promotes tumorigenesis through altered calcium signaling and metabolic reprogramming

## Program: Synaptic Plasticity and Neurotransmission
This program encompasses expression of synaptic vesicle proteins, ionotropic and metabotropic glutamate receptors, neurotrophic factor signaling, and mechanisms regulating long-term potentiation and synaptic strength. The program reflects retention of functional synaptic machinery potentially dysregulated in astrocytomas.

**Predicted impacts**
- Retention of functional synaptic machinery despite malignant transformation
- Dysregulated glutamate signaling affecting neuronal communication
- Altered long-term potentiation and synaptic plasticity
- Potential aberrant expression of synaptic proteins in tumor-host interactions
- Enhanced responsiveness to neurotrophic signals

**Evidence summary**
The input gene list contains exceptional enrichment of genes encoding components of the synaptic proteome, including synaptic vesicle proteins (SYT16), ionotropic glutamate receptors (GRIK3, GRID2), neurotrophic factor receptors (NTRK3), and neurexin-neuroligin adhesion molecules (NRXN1, NRXN3, NLGN4X). This remarkable enrichment suggests that astrocytomas retain substantial synaptic programming despite their glial origin and malignant transformation. Recent evidence demonstrates that altered glutamate signaling in tauopathy leads to aberrant neuronal communication and disruption of hippocampal memory formation, suggesting that dysregulation of synaptic programs contributes to cognitive decline. Synaptic plasticity mechanisms including long-term potentiation are enhanced by metabolic interventions such as ketogenic diet, suggesting that manipulation of synaptic transmission could represent a therapeutic avenue. The presence of neurexin-neuroligin adhesion systems suggests that astrocytomas may establish aberrant synaptic-like contacts with surrounding neurons, potentially enabling tumor-host communication and escape from normal growth restraints.

**Atomic biological processes**
- Neurotransmitter release and synaptic transmission. Genes: SYT16, GRID2, GRIK3
  - [20]: SYT16 encodes synaptotagmin-16, a synaptic vesicle-associated calcium sensor involved in neurotransmitter release
  - [58]: AMPA and NMDA receptor trafficking and function regulate synaptic transmission and plasticity
- Glutamate receptor signaling. Genes: GRIK3, GRID2
  - [22]: Altered glutamate signaling leads to aberrant neuronal communication and disruption of memory formation
  - [58]: Glutamate ionotropic receptors mediate synaptic transmission through ligand-activated ion channels
- Neurotrophic factor signaling. Genes: NTRK3
  - [27]: NTRK3 serves as receptor for neurotrophic factors and regulates fear memory through hippocampus-dependent mechanisms
  - [30]: NTRK3 plays role in panic disorder by regulating hippocampus-dependent fear memories
- Synaptic organization through neurexin-neuroligin adhesion. Genes: NRXN1, NRXN3, NLGN4X
  - [7]: Neurexins and neuroligins establish pre-postsynaptic connections and organize synaptic structures

**Atomic cellular components**
- Synaptic vesicle proteins. Genes: SYT16
  - [20]: SYT16 associates with synaptic vesicles and regulates neurotransmitter release
- Ionotropic glutamate receptors. Genes: GRIK3, GRID2
  - [24]: GRIK2 belongs to kainate family of glutamate receptors composed of four subunits functioning as ligand-activated ion channels
- Neurexin-neuroligin synaptic adhesion complexes. Genes: NRXN1, NRXN3, NLGN4X
  - [7]: Neurexins and neuroligins mediate pre-postsynaptic cell-cell interactions

**Required genes (not in input)**
- Genes: AMPAR_subunits, NMDAR_subunits, GABA_receptors, SYNAPTOTAGMIN_proteins, SNARE_complex
  - [58]: AMPA and NMDA receptors represent major ionotropic glutamate receptor subtypes regulating synaptic transmission

**Program citations**
- [8]: Ketogenic diet enhances long-term potentiation and cognitive performance through CREB pathway activation
- [11]: Melatonin regulates hippocampal synaptic plasticity and cognitive function
- [22]: Tau hyperphosphorylation disrupts synaptic function through altered glutamate signaling
- [58]: Synaptic proteome diversity is shaped by glutamate receptor and associated protein levels
- [60]: Dopamine modulation of glutamate release involves calcium-dependent presynaptic mechanisms

## Program: Cell Adhesion and Migration Control
This program encompasses cell-cell adhesion through protocadherins and immunoglobulin-family molecules, Rho GTPase-mediated cytoskeletal dynamics through guanine nucleotide exchange factors, and myosin motor proteins driving cell morphology and migration. The program collectively regulates the balance between cell-cell contact restraint and motility.

**Predicted impacts**
- Dysregulated cell-cell adhesion enabling escape from growth restraint
- Enhanced cell motility and migration through Rho GTPase signaling
- Altered morphology and cytoskeletal dynamics
- Increased invasive capacity through actin polymerization
- Potential disruption of normal tissue architecture

**Evidence summary**
The input gene list contains multiple genes encoding cell-cell adhesion molecules (PCDH11X, PCDH15, NCAM2, NRCAM) that mediate homophilic cell-cell interactions and synaptic development. These molecules are downregulated in tau-associated neurodegeneration, indicating their normal role in maintaining synaptic structure. Guanine nucleotide exchange factors encoded by TRIO regulate Rac1 and Rho GTPases, small GTPases controlling actin cytoskeleton dynamics and cell migration. PAK3 and PAK5 encode p21-activated kinases that mediate Rho GTPase signaling to regulate cell motility and morphogenesis through actin polymerization. Myosin motors (MYO9B, MYO10) translocate along actin filaments to generate force and drive migration. Recent evidence demonstrates that dysregulated Trio GEF1 signaling causes neurodevelopmental disorders through altered axon branching, suggesting that Trio-Rac1 signaling is normally critical for neuronal morphogenesis. The presence of multiple adhesion and migration components suggests that astrocytomas dysregulate the balance between cell-cell contact restraint and motility, enabling escape from normal tissue constraints and promoting invasive behavior.

**Atomic biological processes**
- Homophilic cell-cell adhesion. Genes: PCDH11X, PCDH15, NCAM2, NRCAM
  - [22]: Protocadherins and CAMs mediate cell-cell communication and synaptic development; downregulation occurs in neurodegeneration
- Rho GTPase signaling and actin cytoskeleton dynamics. Genes: TRIO, PAK3, PAK5
  - [23]: Trio GEF regulates Rac1 and Rho GTPases controlling actin cytoskeleton dynamics and cell migration; dysregulated Trio causes neurodevelopmental disorders
- Actin polymerization and cytokinesis. Genes: FNBP1L, MYO9B, MYO10
  - [23]: Formin and myosin proteins regulate actin polymerization and cell morphological changes

**Atomic cellular components**
- Protocadherin and CAM adhesion complexes. Genes: PCDH11X, PCDH15, NCAM2, NRCAM
  - [22]: Cadherins organize cell-cell connections and synaptic structures
- GEF-Rho GTPase signaling complexes. Genes: TRIO
  - [23]: TRIO GEF domains regulate Rac1 and Rho GTPase activity
- Actin filament and myosin motor proteins. Genes: PAK3, PAK5, FNBP1L, MYO9B, MYO10
  - [23]: PAK kinases mediate Rho GTPase signaling to regulate actin polymerization and cell motility

**Required genes (not in input)**
- Genes: RAC1, RHOA, CDC42, COFILIN, ROCK, LIMK
  - [23]: Trio GEF-Rac1 signaling requires downstream RAC1 GTPase and COFILIN for actin dynamics

**Program citations**
- [7]: Slit and Roundabout guidance cues prevent migration of multiple cell types
- [23]: Trio and CRMP2 regulate axon branching through Rac1-GEF signaling; NDD-related mutations in Trio cause branching defects
- [48]: Cofilin activation regulates astrocytoma cell migration and invasion

## Program: Wnt Signaling and Transcriptional Cell Fate Control
This program encompasses Wnt pathway transcriptional regulators, canonical and non-canonical Wnt signaling components, and associated transcription factors controlling cell fate decisions between proliferation and differentiation. The program collectively regulates stemness and differentiation state.

**Predicted impacts**
- Dysregulated balance between Wnt-driven proliferation and differentiation
- Altered stemness and differentiation state
- Enhanced transcriptional plasticity
- Potential maintenance of neural progenitor-like properties
- Increased therapeutic resistance through stemness

**Evidence summary**
The input gene list contains genes encoding key Wnt pathway transcriptional regulators (TCF7L1) and stem cell identity factors (SOX2-OT). TCF7L1 functions as a Wnt pathway repressor that buffers CTNNB1/TCF target gene expression and plays a major role in maintaining embryonic stem cell pluripotency, suggesting its role in regulating the balance between proliferation and differentiation. SOX2 represents a master regulator of neural stem cell identity and is frequently dysregulated in gliomas. Recent evidence demonstrates that β-catenin activation through CTNNB1 mutations is associated with poor outcomes in adrenocortical carcinoma, with more than 50% of poor-outcome patients harboring CTNNB1 or TP53 mutations. Non-canonical Wnt signaling through Wnt5A promotes stemness and metastatic phenotypes in cancer. The presence of Wnt pathway components suggests that astrocytomas dysregulate normal Wnt signaling controlling the balance between neural stem cell maintenance and differentiation, potentially contributing to therapeutic resistance and tumor recurrence.

**Atomic biological processes**
- Wnt pathway transcriptional regulation. Genes: TCF7L1
  - [52]: TCF7L1 functions as Wnt pathway repressor buffering CTNNB1/TCF target gene expression; plays major role in maintaining embryonic stem cell pluripotency
  - [61]: β-catenin activation associated with poor outcome in adrenocortical carcinoma; CTNNB1 mutations occur in >50% of poor-outcome patients
- Cell fate specification and stemness regulation. Genes: SOX2-OT
  - [21]: SOX2 represents master regulator of neural stem cell identity

**Atomic cellular components**
- Wnt signaling transcription factors. Genes: TCF7L1
  - [52]: TCF7L1 functions as Wnt pathway transcriptional regulator
- Stem cell identity regulators. Genes: SOX2-OT
  - [21]: SOX2 encodes master regulator of neural stem cell pluripotency

**Required genes (not in input)**
- Genes: CTNNB1, LEF1, GSK3B, APC, WNT_ligands
  - [61]: CTNNB1 β-catenin represents core component of canonical Wnt signaling

**Program citations**
- [52]: TCF7L1 buffers Wnt-driven transcription in pluripotent stem cells
- [55]: TCF7L1 regulates embryonic development through Wnt signaling
- [61]: Canonical and non-canonical Wnt signaling regulate stemness and metastatic potential

## Program: Extracellular Matrix Organization and Tumor Microenvironment
This program encompasses proteoglycans and structural proteins organizing extracellular matrix, collagen and basement membrane components, and associated signaling mediating cell-matrix interactions. The program collectively regulates tissue architecture, mechanical signaling, and immune cell infiltration.

**Predicted impacts**
- Altered tissue architecture and mechanical properties
- Enhanced angiogenesis through ECM stiffness modulation
- Modified immune cell infiltration and activation
- Changed cellular differentiation state through mechanotransduction
- Disrupted normal tissue barriers and compartmentalization

**Evidence summary**
The input gene list contains genes encoding critical extracellular matrix components including versican (VCAN), a dynamic regulator of matrix organization; hyaluronan and proteoglycan link protein 1 (HAPLN1), which stabilizes matrix component interactions; and collagen type IV alpha-3 (COL4A3), a basement membrane component. Dysregulation of these proteins by astrocytomas likely contributes to breakdown of normal tissue architecture and altered mechanical signaling. Recent evidence demonstrates that extracellular matrix stiffness modulates angiogenic signaling, with softer substrates promoting pro-angiogenic factor expression while stiffer environments favor anti-angiogenic responses. This suggests that astrocytoma-mediated remodeling of extracellular matrix composition and stiffness could enhance angiogenesis supporting tumor growth. Additionally, the extracellular matrix serves as a critical component of the immune microenvironment, with its composition influencing immune cell infiltration, activation, and trafficking. Dysregulated matrix organization in astrocytomas likely contributes to the immunosuppressive tumor microenvironment characteristic of gliomas.

**Atomic biological processes**
- Extracellular matrix proteoglycan organization. Genes: VCAN, HAPLN1
  - [34]: Versican functions as dynamic regulator of extracellular matrix
  - [62]: HAPLN1 enables hyaluronic acid binding and functions as extracellular matrix structural constituent
- Basement membrane collagen organization. Genes: COL4A3
  - [31]: COL4A3 encodes collagen type IV alpha-3 chain, component of basement membranes
  - [28]: Collagen type IV mutations cause Alport syndrome through disruption of basement membranes
- Mechanotransduction through ECM stiffness. Genes: VCAN, HAPLN1, COL4A3
  - [51]: Extracellular matrix stiffness modulates angiogenic signaling; softer substrates promote pro-angiogenic response while stiffer environments favor anti-angiogenic responses

**Atomic cellular components**
- Proteoglycan and hyaluronic acid binding proteins. Genes: VCAN, HAPLN1
  - [34]: Versican represents major proteoglycan in extracellular matrix
- Type IV collagen basement membrane components. Genes: COL4A3
  - [31]: Collagen type IV represents critical basement membrane structural component

**Required genes (not in input)**
- Genes: MMP2, MMP9, ADAMTS_proteases, TISSUE_INHIBITOR_of_metalloproteinases, INTEGRIN
  - [9]: Matrix metalloproteinases regulate extracellular matrix remodeling

**Program citations**
- [9]: Glioma tumor microenvironment demonstrates profound immunosuppression
- [12]: Glioma tumor microenvironment remodeling represents target for immunotherapy enhancement
- [51]: Extracellular matrix stiffness fundamentally regulates angiogenic factor expression in retinal pigment epithelium

## Program: Post-Transcriptional Gene Regulation and mRNA Stability
This program encompasses m6A methylation-mediated mRNA stability control through IGF2BP3, RNA-binding protein-mediated post-transcriptional regulation through CELF2 and PTBP3, and alternative splicing control. The program collectively enables selective enhancement of pro-tumorigenic factor expression while suppressing tumor suppressors.

**Predicted impacts**
- Enhanced stability and translation of pro-tumorigenic mRNAs
- Selective suppression of tumor suppressor expression
- Dysregulated post-transcriptional control
- Increased invasion and therapeutic resistance
- Altered RNA processing and splicing patterns

**Evidence summary**
The input gene list contains genes encoding critical post-transcriptional regulators including IGF2BP3, an m6A methylation-dependent mRNA stability reader; CELF2, a RNA-binding protein regulating mRNA metabolism; and PTBP3, a polypyrimidine tract binding protein. Recent evidence demonstrates that IGF2BP3 is remarkably upregulated in locally invasive pancreatic ductal adenocarcinoma and indicates worse prognosis. IGF2BP3 recognizes m6A-modified EMP1 mRNAs to prolong their stability, promoting invasion through TGF-β pathway activation. This m6A methylation system represents an emerging layer of post-transcriptional control frequently dysregulated in cancer. RNA-binding proteins including CELF and PTBP families regulate alternative splicing, mRNA stability, and translation efficiency, enabling selective enhancement of pro-tumorigenic factors while suppressing tumor suppressors. The presence of multiple post-transcriptional regulators suggests that astrocytomas dysregulate mRNA metabolism to promote aggressive phenotypes and therapeutic resistance.

**Atomic biological processes**
- m6A methylation-dependent mRNA stability. Genes: IGF2BP3
  - [35]: IGF2BP3 recognizes m6A-modified mRNAs to prolong stability; upregulated in invasive cancer and indicates worse prognosis
  - [39]: IGF2BP3 functions as m6A reader primarily found in nucleolus where it binds insulin-like growth factor II mRNA
- RNA-binding protein-mediated mRNA processing and stability. Genes: CELF2, PTBP3
  - [35]: RNA-binding proteins regulate mRNA stability and translation efficiency

**Atomic cellular components**
- m6A reader proteins. Genes: IGF2BP3
  - [35]: IGF2BP3 represents m6A reader protein recognizing N6-methyladenosine-modified mRNAs
- RNA-binding proteins regulating mRNA metabolism. Genes: CELF2, PTBP3
  - [35]: CELF and PTBP family proteins regulate mRNA alternative splicing and stability

**Required genes (not in input)**
- Genes: METTL3, METTL14, YTHDF1, YTHDF2, HNRNP_proteins
  - [35]: m6A methylation requires METTL3/14 methyltransferases and YTHDF reader proteins

**Program citations**
- [35]: IGF2BP3 functions as invasion driver in pancreatic cancer via EMP1/TGF-β axis

## Program: Metabolic Reprogramming and Stemness Maintenance
This program encompasses transcriptional regulators of metabolic state including PPARα, PRDM16, and SOX2 family factors, long non-coding RNAs regulating stem cell identity, and metabolic enzymes supporting oxidative metabolism and lipid metabolism. The program collectively maintains stem cell-like properties and reprograms metabolism to support rapid growth.

**Predicted impacts**
- Altered metabolic state supporting rapid growth and proliferation
- Maintenance of stem cell-like properties and self-renewal capacity
- Enhanced metabolic plasticity enabling response to nutrient availability
- Increased therapeutic resistance through stemness
- Dysregulated oxidative metabolism and glycolytic dependency

**Evidence summary**
The input gene list contains genes encoding critical metabolic regulators including PRDM16, which controls transcriptional programs regulating differentiation and metabolic state; and SOX2-OT, a long non-coding RNA regulating SOX2 expression and neural stem cell identity. Recent evidence demonstrates that PPARα-dependent mitochondrial functions regulate beta-cell metabolic maturity and function, with PPARα regulating carnitine biosynthesis and oxidative metabolism. SOX2 represents a master regulator of neural stem cell identity and is frequently dysregulated in gliomas. Astrocytomas likely undergo metabolic reprogramming to support rapid growth while potentially retaining some stem cell-like characteristics that enable continued self-renewal and therapeutic resistance. The Warburg effect, wherein tumors preferentially utilize glycolysis over oxidative phosphorylation, represents a hallmark of cancer metabolism. The presence of metabolic regulators and stem cell identity factors suggests that successful astrocytoma transformation requires simultaneous maintenance of neural progenitor-like properties and reprogramming toward metabolic autonomy.

**Atomic biological processes**
- Transcriptional control of metabolic state and differentiation. Genes: PRDM16
  - [63]: PPARα regulates carnitine biosynthesis and oxidative metabolism; PPARα-dependent mitochondrial functions limit metabolic maturity in beta cells
  - [66]: PRDM16 regulates transcriptional programs controlling differentiation and metabolic state
- Stem cell identity and pluripotency control. Genes: SOX2-OT
  - [21]: SOX2 represents master regulator of neural stem cell identity

**Atomic cellular components**
- Transcriptional regulators of metabolic state. Genes: PRDM16
  - [63]: PPARα and estrogen-related receptors regulate beta-cell metabolic maturity and oxidative function
- Stem cell identity transcriptional regulators. Genes: SOX2-OT
  - [21]: SOX2 transcription factor represents critical regulator of neural stem cell identity

**Required genes (not in input)**
- Genes: HIF1A, LDHA, PKM2, GLUT1, SOX2, STAT3
  - [63]: Metabolic reprogramming involves HIF1A-mediated glycolysis and STAT3 signaling

**Program citations**
- [63]: PPARα-dependent mitochondrial functions regulate metabolic maturity and cellular function
- [66]: PRDM16 represents key regulator of cell fate and metabolic state

## Program: Protein Tyrosine Phosphatase Signaling and Kinase Restraint
This program encompasses multiple receptor and non-receptor protein tyrosine phosphatases that dephosphorylate growth factor receptors and signaling proteins, collectively forming a counterbalance to tyrosine kinase signaling. The program regulates the phosphorylation balance controlling proliferation and survival.

**Predicted impacts**
- Restraint of growth factor receptor signaling
- Reduced AKT and MAPK pathway activation
- Enhanced cellular differentiation and reduced proliferation
- Potential loss of function leading to hyperphosphorylation and proliferation
- Altered synaptic plasticity and neural function

**Evidence summary**
The input gene list contains multiple genes encoding receptor and non-receptor protein tyrosine phosphatases (PTPRK, PTPRN2, PTPRZ1, PTPRD, PTPRT) that function to dephosphorylate growth factor receptors and signaling proteins. PTPRK specifically dephosphorylates CD133 tyrosine phosphorylation, regulating AKT signaling and stem cell biology. Recent evidence demonstrates that PTPRK promotes postherpetic neuralgia through activation of DUSP1/p38 MAPK signaling, suggesting complex roles in pain and neuronal signaling. These phosphatases collectively represent a counterbalance to the tyrosine kinase signaling dysregulation central to cancer. Phosphatase inactivation through mutation, deletion, or altered expression represents a complementary mechanism to tyrosine kinase activation in driving tumorigenesis. The presence of multiple phosphatases suggests that astrocytomas may dysregulate the balance between kinase and phosphatase activity, tilting toward enhanced phosphorylation-dependent signaling and proliferation.

**Atomic biological processes**
- Receptor tyrosine kinase dephosphorylation. Genes: PTPRK
  - [43]: PTPRK dephosphorylates CD133 tyrosine phosphorylation, regulating AKT signaling and stem cell biology
  - [41]: PTPRK promotes postherpetic neuralgia through DUSP1/p38 MAPK signaling pathway
- Neural development and synaptic plasticity regulation. Genes: PTPRN2, PTPRZ1, PTPRD
  - [7]: Receptor tyrosine phosphatases regulate neural development and synaptic plasticity

**Atomic cellular components**
- Receptor protein tyrosine phosphatases. Genes: PTPRK, PTPRN2, PTPRZ1, PTPRD
  - [43]: PTPRK represents receptor protein tyrosine phosphatase
- Non-receptor tyrosine phosphatases. Genes: PTPRT
  - [43]: PTPRT encodes receptor tyrosine phosphatase

**Required genes (not in input)**
- Genes: EGFR, PDGFR, FYN, LCK, PTK2
  - [43]: Receptor tyrosine kinases represent substrates for phosphatase regulation

**Program citations**
- [41]: PTPRK regulates pain signaling through p38 MAPK pathway
- [43]: PTPRK dephosphorylates CD133 to regulate AKT signaling

## Program: Axon Guidance and Neuronal Morphogenesis
This program encompasses repulsive and attractive axon guidance cues including semaphorins, plexin receptors, and downstream signaling including CRMP2, Rac1-GEF, and associated morphogenesis regulators. The program collectively controls neuronal morphology and axonal patterning.

**Predicted impacts**
- Dysregulated axon guidance signaling
- Altered neuronal morphology and branching patterns
- Aberrant filopodial dynamics
- Potential disruption of normal circuit formation
- Enhanced cell-to-cell communication through morphological changes

**Evidence summary**
The input gene list contains genes encoding critical axon guidance components including semaphorin-5A (SEMA5A), a guidance cue involved in neural development that has been implicated as an autism susceptibility gene; plexin-A2 and plexin-A4 (PLXNA2, PLXNA4), transmembrane receptors binding semaphorins; and TRIO, which encodes a GEF regulating Rac1-dependent morphogenesis downstream of semaphorin signaling. Recent evidence demonstrates that pCRMP2-Trio signaling is invoked by Sema3A to mediate axon repulsion through suppression of filopodial motility and branching. Notably, an NDD-related GEF1 loss-of-function mutation in TRIO causes exuberant branching instead of branch suppression, suggesting that TRIO GEF1 signaling is normally critical for neuronal morphogenesis. The presence of these axon guidance components in the astrocytoma gene list suggests retention of developmental signaling pathways that may contribute to either differentiation or aberrant morphogenesis. Astrocytoma cells, despite their glial origin, may express neuronal guidance receptors that influence their morphology and interactions with surrounding neurons.

**Atomic biological processes**
- Repulsive axon guidance signaling. Genes: SEMA5A
  - [23]: Sema3A-signaling stimulates and requires C-terminal phosphorylation of CRMP2 and Rac1 activation to mediate axon repulsion
  - [25]: SEMA5A represents axon guidance cue involved in neural development and implicated as autism susceptibility gene
- Plexin receptor signaling and CRMP2 regulation. Genes: PLXNA2, PLXNA4
  - [23]: CRMP2 associates with Trio and mediates Rac1-GEF signaling downstream of semaphorin to suppress filopodial motility
- Axon branching control through GEF signaling. Genes: TRIO
  - [23]: pCRMP2-Trio GEF1 signaling suppresses axon branching; NDD-related Trio GEF1 mutation causes exuberant branching

**Atomic cellular components**
- Semaphorin guidance ligands. Genes: SEMA5A
  - [25]: Semaphorins represent family of secreted and membrane-bound guidance molecules
- Plexin guidance receptors. Genes: PLXNA2, PLXNA4
  - [23]: Plexins represent transmembrane receptors binding semaphorins

**Required genes (not in input)**
- Genes: RAC1, CRMP2, SEMA3A, PLXNB, EPHRIN
  - [23]: pCRMP2-Trio-Rac1 signaling represents downstream pathway for semaphorin-mediated axon repulsion

**Program citations**
- [7]: Axon guidance receptors control neuronal migration and circuit formation
- [23]: Trio GEF1 signaling regulates axon branching downstream of Sema3A; NDD-associated mutations cause morphogenesis defects
- [25]: Semaphorins represent major axon guidance cues

## Program: Transcriptional Regulation of Development and Cell Fate
This program encompasses developmental transcription factors including members of the homeodomain, nuclear receptor, and bHLH families that control cell fate decisions, glial specification, and differentiation state. The program collectively regulates the balance between progenitor maintenance and terminal differentiation.

**Predicted impacts**
- Dysregulated cell fate decisions between progenitor and terminal differentiation
- Altered glial cell specification and identity
- Modified metabolic and developmental gene expression
- Potential loss of differentiation capacity
- Maintained stemness through altered transcriptional control

**Evidence summary**
The input gene list contains genes encoding developmental transcription factors including EYA1, a transcriptional coactivator involved in development; POU6F2, a POU-family homeobox transcription factor; RORA, a nuclear receptor regulating metabolic pathways; NKD1, a negative regulator of Wnt signaling; and OLIG1, an oligodendrocyte lineage transcription factor. Recent evidence indicates that RORA influences regulation of metabolic pathways and functions as a genetic modifier rescuing retinal degeneration, suggesting pleiotropic developmental and metabolic roles. OLIG1 encodes a critical regulator of glial cell differentiation and specification. The presence of these developmental transcription factors suggests that astrocytomas dysregulate normal developmental programs controlling cell fate decisions, potentially enabling either maintenance of stemness or aberrant differentiation. This program likely works in concert with Wnt signaling (Program 5) and metabolic regulators (Program 8) to maintain balance between proliferation and differentiation.

**Atomic biological processes**
- Developmental transcriptional regulation. Genes: EYA1
  - [28]: EYA1 encodes transcriptional coactivator involved in developmental pathways
- Wnt pathway transcriptional regulation in development. Genes: NKD1
  - [52]: NKD1 encodes negative regulator of Wnt signaling
- Metabolic and developmental control through nuclear receptors. Genes: RORA
  - [42]: RORA encodes RAR-related orphan receptor regulating metabolic pathways including steroids and bile acids
  - [44]: RORA functions as genetic modifier rescuing retinal degeneration in mouse models
- Glial cell fate specification. Genes: OLIG1
  - [56]: OLIG1 encodes oligodendrocyte lineage transcription factor regulating glial cell differentiation

**Atomic cellular components**
- Developmental transcription factors. Genes: EYA1, POU6F2
  - [28]: EYA1 functions as transcriptional coactivator
- Nuclear receptors controlling metabolism and development. Genes: RORA
  - [42]: RORA represents nuclear receptor family member
- Glial lineage transcription factors. Genes: OLIG1
  - [56]: OLIG represents oligodendrocyte lineage specification factor

**Required genes (not in input)**
- Genes: PAX6, NeuroD, ASCL1, NGN2, DLX5
  - [56]: Multiple transcription factors cooperatively control neural and glial development

**Program citations**
- [42]: RORA functions in metabolic regulation and developmental pathways
- [44]: RORA represents genetic modifier of retinal degeneration
- [56]: Notch signaling required for nephron formation; OLIG family controls glial specification

## Program: Vesicular Trafficking and Endocytic Receptor Recycling
This program encompasses endocytic machinery including clathrin-coated pit components, small GTPase regulators of vesicular trafficking, dynamin GTPases mediating membrane scission, and downstream vesicle fusion machinery. The program collectively regulates receptor internalization, cellular communication, and cargo trafficking.

**Predicted impacts**
- Altered growth factor receptor trafficking and surface levels
- Modified endocytic pathway efficiency
- Changed cellular communication through altered receptor recycling
- Potential escape from growth factor withdrawal through receptor trafficking dysregulation
- Enhanced or suppressed growth factor signaling through endocytic pathway modulation

**Evidence summary**
The input gene list contains genes encoding critical endocytic and vesicular trafficking components including HIP1 (huntingtin-interacting protein 1), which regulates clathrin-mediated endocytosis; DNM3 (dynamin-3), a GTPase mediating membrane scission during vesicle formation; RAB27B (Ras-related protein), a small GTPase regulating exocytosis; ERC2 (ELKS/Rab6-interacting/CAST family member 2), involved in cytoplasmic vesicle organization. Recent evidence indicates that traffic of GluA2-containing AMPAR involves clathrin-mediated endocytosis and neuronal pentraxin 1, suggesting that endocytic regulation of glutamate receptor levels controls synaptic strength. Dysregulated endocytic trafficking could alter growth factor receptor levels, enabling escape from growth factor withdrawal constraints, or promote invasion through altered cell-cell contact regulation. The presence of multiple endocytic and vesicular trafficking components suggests that astrocytomas dysregulate membrane trafficking systems to modulate growth factor signaling, receptor recycling, and cellular communication.

**Atomic biological processes**
- Clathrin-mediated endocytosis. Genes: HIP1
  - [48]: Endocytic machinery including clathrin regulates receptor trafficking
  - [58]: Traffic of GluA2-containing AMPAR involves clathrin-mediated endocytosis and neuronal pentraxin 1
- GTPase-mediated membrane scission. Genes: DNM3
  - [48]: Dynamin GTPases mediate membrane scission during endocytosis and vesicle formation
- Rab GTPase-mediated vesicular trafficking. Genes: RAB27B
  - [48]: Rab GTPases regulate specific vesicular trafficking routes
- Cytoplasmic vesicle organization and trafficking. Genes: ERC2
  - [48]: ELKS/Rab6-interacting/CAST family members organize cytoplasmic vesicles

**Atomic cellular components**
- Clathrin-coated pit proteins. Genes: HIP1
  - [58]: HIP1 regulates clathrin-mediated endocytosis
- Dynamin GTPase membrane scission machinery. Genes: DNM3
  - [48]: DNM3 encodes dynamin mediating membrane scission
- Rab GTPase vesicular routing proteins. Genes: RAB27B
  - [48]: RAB27B regulates specific vesicular trafficking routes
- Vesicle organization and tethering complex proteins. Genes: ERC2
  - [48]: ERC2 organizes cytoplasmic vesicles

**Required genes (not in input)**
- Genes: AP2, CLATHRIN, AP1, SNAREs, TETHERS
  - [58]: AP2 and clathrin complexes represent core endocytic machinery; SNAREs mediate vesicle fusion

**Program citations**
- [48]: Endocytic machinery regulates receptor trafficking and signaling
- [58]: AMPAR trafficking involves clathrin-mediated endocytosis and regulates synaptic strength

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/1028
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/546
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/12577
5. 5. Wisniewski DJ, Voeller D, Addissie YA, Deshmukh SK, Wu S, Lustberg MB, et al.. EGFR amplification and PI3K pathway mutations identify a subset of breast cancers that synergistically respond to EGFR and PI3K inhibition. Oncogene [Internet]. 2025Nov25;. Available from: https://www.nature.com/articles/s41388-025-03634-3
6. 6. Sayinta A, Duangdara J, Sumphanapai T, Rangnoi K, Boonsri B, Supradit K, et al.. Identification of internalizing ScFvs for EGFR inhibition and apoptosis induction in cholangiocarcinoma cells. Scientific Reports [Internet]. 2025Nov19;15(1). Available from: https://www.nature.com/articles/s41598-025-24324-w
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/6091
8. 8. Jacopo DL, Jennifer MR, Alfredo EP, Giuseppe P, Zeyu Z, Lee-Way J, et al.. A ketogenic diet improves memory in females in the APOE4 mouse model of Alzheimer's disease.. GeroScience [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41283974/
9. 9. Ana HLN, Ana PS do P, Rafael SP, Áquila RCS, Rafaela RV, Luiza CDS de S, et al.. Microglial Inflammatory Response in the Glioblastoma Microenvironment in Preclinical Models.. Molecular neurobiology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41307720/
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/9353
11. 11. Leila K-Z, Samaneh A, Maryam Z. Hippocampal synaptic plasticity impairment and melatonin synthesis reduction in cognitive decline of a rodent model of Alzheimer's disease-like pathology.. Pflugers Archiv : European journal of physiology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41366569/?fc=None&ff=20251211205400&v=2.18.0.post22+67771e2
12. 12. Josip C, Wen-Lu T, Tao J, Zheng Z. Glioma tumor microenvironment and immunotherapy: past, present, and future.. Biomarker research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41272822/
13. 13. He W, Demas DM, Kraikivski P, Shajahan-Haq AN, Baumann WT. WEE1 inhibition delays resistance to CDK4/6 inhibitor and antiestrogen treatment in ER+ MCF7 cells. npj Systems Biology and Applications [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41540-025-00604-z
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/5578
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/12290
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/12571
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/18750
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/777
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/20358
20. 20. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
22. 22. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
23. 23. Fingleton E, Lombardo A, Won S, Chang K, Li Y, Roche KW. Trio and CRMP2 regulate axon branching and Semaphorin3A signaling. Communications Biology [Internet]. 2025Nov25;8(1). Available from: https://www.nature.com/articles/s42003-025-08988-8
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/2898
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/9037
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/26401
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/4916
28. 28. Winston W-SF, Maggie L-YY, Pensi PHL, Cheuk-Chun S, Shuk-Ching C, Kai-Ming C. A case of concurrent Alport syndrome and Nail-patella syndrome posing diagnostic challenge without genetic testing.. BMC nephrology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41299396/
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/4214
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/18213
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/1285
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/23345
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/16971
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/1462
35. 35. Long L, Yu Z, Yuxi H, Xiaohong Z, Hongxing F, Lin C, et al.. IGF2BP3 regulates EMP1 stability in an m. Cell death & disease [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41285728/
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/77053
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/53353
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=13003
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/10643
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/5138
41. 41. Yong Z, Hongli Z, Zhijian W, Mengye Z, Xuexue Z, Daying Z. PTPRK promotes resiniferatoxin-induced postherpetic neuralgia via activating DUSP1/p38 MAPK signaling pathway in dorsal root ganglia.. Scientific reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41253902/
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/19883
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/5796
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=6095
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/100130776
46. 46. Braun T, Afgin N, Sapozhnikov L, Sivan E, Bergmann A, Baena-Lopez LA, et al.. Apoptosis-resistant cells drive compensatory proliferation via cell-autonomous and non-autonomous functions of the initiator caspase Dronc. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-65996-2
47. 47. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/1072
49. 49. Mengyu Z, Min Z, Mengrui L, Xinru W, Qipan F, Shengjie W, et al.. The Roles of TOPK in Tumorigenesis and Development: Structure, Mechanisms, Pathways, and Therapeutic Implications.. International journal of biological sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41362722/?fc=None&ff=20251209230910&v=2.18.0.post22+67771e2
50. 50. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
51. 51. Wolfram L, Schwämmle M, Gimpel C, Merle DA, Tang J, Clark SJ, et al.. Extracellular matrix stiffness modulates angiogenic properties of the retinal pigment epithelium. Scientific Reports [Internet]. 2025Nov18;15(1). Available from: https://www.nature.com/articles/s41598-025-27140-4
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/83439
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/13388
54. 54. Zhaoping T, Binyue S, Lu C, Hong D, Yaqin D, Yunyun L, et al.. Inflammation-driven mechanisms in endometrial cancer: pathways from inflammatory microenvironment remodeling to immune escape.. Frontiers in immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41383623/?fc=None&ff=20251212152406&v=2.18.0.post22+67771e2
55. 55. Available from: https://www.ncbi.nlm.nih.gov/gene/21415
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/18128
57. 57. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
58. 58. Reig-Viader R, del C-BD, Burgas-Pau A, Arco-Alonso D, Zerpa-Rios O, Ramos-Vicente D, et al.. Synaptic proteome diversity is shaped by the levels of glutamate receptors and their regulatory proteins. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65490-9
59. 59. Syrtveit AA, Ingebriktsen LM, Tegnander AF, Akslen LA, Wik E, Hoivik EA. Tumor necrosis associates with aggressive breast cancer features, increased hypoxia signaling and reduced patient survival. Scientific Reports [Internet]. 2025Nov27;. Available from: https://www.nature.com/articles/s41598-025-29905-3
60. 60. Uzay B, Zhang KJ, Monteggia LM, Kavalali ET. Dopaminergic tone inhibits spontaneous glutamate release and augments homeostatic synaptic plasticity. Molecular Psychiatry [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41380-025-03374-6
61. 61. Shapiro I, Debaix H, Kräuchi C, Abate A, Bornstein SR, Nölting S, et al.. (Non)canonical Wnt signaling, cytoarchitecture and stemness: new insights from primary nonmetastatic, primary metastatic, regional and distant metastatic models of adrenocortical carcinoma. Experimental &amp; Molecular Medicine [Internet]. 2025Nov28;57(11). Available from: https://www.nature.com/articles/s12276-025-01507-z
62. 62. Available from: https://www.ncbi.nlm.nih.gov/gene/1404
63. 63. Lietzke AC, Walker EM, Bealer E, Crumley K, King J, Stendahl AM, et al.. Limitations in PPARα-dependent mitochondrial programming restrain the differentiation of human stem cell-derived β cells. Nature Communications [Internet]. 2025Dec10;16(1). Available from: https://www.nature.com/articles/s41467-025-66022-1
64. 64. Available from: https://www.ncbi.nlm.nih.gov/gene/7220
65. 65. Available from: https://www.ncbi.nlm.nih.gov/gene/12950
66. 66. Available from: https://www.ncbi.nlm.nih.gov/gene/63976
67. 67. Available from: https://www.ncbi.nlm.nih.gov/gene/7222
68. 68. Available from: http://json-schema.org/draft-07/schema#",
