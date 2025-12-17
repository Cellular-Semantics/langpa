# Gene Program Markdown Report

## Context
- Cell type: Glioblastoma cells (malignant glioma cells)
- Disease: Glioblastoma multiforme (GBM)
- Tissue: brain

## Input Genes
FSTL4, LRFN5, TRPM3, NDST4, PALMD, ADRA1B, PDE1A, CLVS1, SLC17A6, ACVR1C, SLA, EBF1, AC011474.1, FRMPD4, KIT, UNC5D, GCG, TRPC5, CDH9, TARID, LINC01033, AC109492.1, AL596087.2, SHISA6, POSTN, ... (136 total)

## Program: Extracellular Matrix Remodeling and Invasion
Coordinated secretion and degradation of extracellular matrix components to facilitate glioblastoma cell invasion through brain tissue. This program includes collagen synthesis and deposition (COL3A1, COL6A3), matrix metalloproteinase activity (ADAMTS3, PRSS12), ECM-binding proteins (SMOC2, POSTN, TGFBI), and regulatory proteins (GREM2, VWC2L). In GBM, this program promotes escape from the tumor core and infiltration into surrounding brain parenchyma, supporting mesenchymal transition and treatment-resistant phenotypes.

**Predicted impacts**
- Enhanced invasive migration into infiltrated brain tissue
- Acquisition of mesenchymal gene expression signature
- Increased mechanical stiffness of local microenvironment
- Reduced chemotherapy penetration through ECM barrier
- Promotion of bevacizumab-resistant phenotype

**Evidence summary**
Multiple genes in this program are strongly upregulated in GBM, particularly COL6A3 which is enriched in microvascular proliferation regions and mesenchymal GBM subtypes. COL6A3 is selectively enriched in bevacizumab-resistant cells and its deletion reduces invasion and β-catenin signaling. ADAMTS proteases and other ECM-remodeling enzymes are well-established contributors to GBM invasiveness. SMOC2 and TGFBI are emerging mediators of metastatic behavior across multiple cancers. The coordinated expression of these genes suggests active reprogramming of the microenvironment to support rapid proliferation and invasion.

**Atomic biological processes**
- Collagen secretion and deposition. Genes: COL3A1, COL6A3, PAPPA2
  - [9]: GBM cells secrete collagen VI (COL6A3) which stiffens ECM and facilitates invasion through integrin signaling
- Matrix metalloproteinase activity. Genes: ADAMTS3, PRSS12, SERPINI1
  - [55]: ADAM and ADAMTS proteases regulate tissue remodeling through ECM degradation, cell migration, and angiogenesis
- ECM-associated protein binding. Genes: SMOC2, POSTN, TGFBI, VWC2L
  - [56]: SMOC2 is a secreted modular calcium-binding protein involved in ECM remodeling and cell adhesion
  - [59]: SMOC2 regulates cell cycle progression, tissue fibrosis, and cell attachment to extracellular matrix
- Invasion-promoting signaling. Genes: GREM2, RASGEF1B, FGD4
  - [9]: COL6A3 triggers β-catenin signaling and ZEB1 expression in GBM cells, promoting mesenchymal phenotype and invasion

**Atomic cellular components**
- Extracellular matrix structure. Genes: COL3A1, COL6A3, SMOC2, POSTN, EDIL3
  - [9]: GBM-derived collagen VI assembles into ECM fibrillar networks that promote invasion

**Program citations**
- [9]: Core evidence: GBM cells secrete extensive ECM, particularly collagen VI, which facilitates invasion and is associated with bevacizumab resistance
- [55]: ADAM/ADAMTS proteases regulate tissue remodeling through ECM degradation and cell migration
- [57]: LIN28B/TGF-β feedback loop promotes TGFBI expression and cancer cell migration
- [59]: SMOC proteins regulate cell adhesion, tissue fibrosis, and calcification relevant to tumor microenvironment
- [60]: TGFBI is a prognostic marker affecting cancer cell migration and invasion

## Program: Cell Adhesion and Synaptic-Like Junctions
Classical and non-classical cell adhesion molecules that mediate cell-cell contacts and establish specialized junction zones. This program includes classical cadherins (CDH4, CDH9, CDH13, CDH18), contactin-associated proteins (CNTNAP4, CNTN5), and adhesion receptors (LRFN5, TENM2, EFNA5). In GBM, dysregulation of these molecules contributes to loss of normal cell polarity, altered migration dynamics, and altered response to developmental cues that normally restrict proliferation.

**Predicted impacts**
- Altered cell-cell contact dynamics affecting proliferation control
- Loss of normal neuronal polarity cues
- Enhanced migratory behavior through reduced adhesive restraint
- Increased cellular plasticity and phenotypic switching
- Dysregulated response to developmental guidance molecules

**Evidence summary**
Classical cadherins are dynamically expressed during normal neural development with distinct patterns that regulate proliferation and differentiation. In GBM, altered cadherin expression is associated with epithelial-mesenchymal transition (EMT) and increased migration. CNTNAP4 is enriched in dopaminergic neurons and has established roles in GABAergic transmission; its deficiency in neurons leads to altered cell function. TENM2 and latrophilin interactions are critical for synaptic specificity. The presence of multiple cadherin family members and contactin-associated proteins suggests GBM cells aberrantly co-express developmental adhesion programs that normally specify particular neuronal subtypes.

**Atomic biological processes**
- Homotypic cell-cell adhesion. Genes: CDH4, CDH9, CDH13, CDH18
  - [8]: Classical cadherins mediate Ca2+-dependent homotypic cell-cell adhesion and are dynamically expressed during neural development
  - [11]: Classic cadherins (Cdh2, Cdh4, etc.) are involved in neurogenesis, neuron migration, and axon growth with tissue-specific expression patterns
- Adherens junction assembly. Genes: CDH4, CDH9, CDH13, CDH18, LRFN5
  - [8]: Nectins cooperate with cadherins in assembly and maintenance of adherens junctions through interaction with catenins
- Trans-synaptic adhesion complex formation. Genes: TENM2, CNTNAP4, CNTN5, LRFN5, GFRA1
  - [30]: Latrophilin-teneurin complexes form trans-synaptic adhesion structures; TENM2 promotes synapse formation through interactions with adhesion GPCRs
  - [37]: GDNF-GFRα1 complexes support synaptic cell adhesion independently of RET signaling
- Axon guidance and fasciculation. Genes: CDH4, CDH9, EFNA5, SEMA3C
  - [27]: CAMs regulate axon fasciculation through homotypic trans-interactions; cadherins mediate selective axon fasciculation

**Atomic cellular components**
- Adherens junction protein complex. Genes: CDH4, CDH9, CDH13, CDH18, LRFN5
  - [8]: Catenins provide anchorage between cadherins and actin cytoskeleton through α-, β-, and p120-catenin groups
- Contact zones between epithelial/neural cells. Genes: CDH4, CDH9, CDH13, CDH18, CNTNAP4, CNTN5
  - [8]: Nectins and cadherins cooperate in assembly of specialized contact zones called adherens junctions

**Program citations**
- [8]: Cadherins and nectins cooperate in adhesion and regulate neuronal migration and differentiation
- [11]: Classic cadherins show restricted expression patterns in neural tissues during development
- [27]: CAMs regulate axon growth, fasciculation, and synaptic specificity through trans-interactions
- [30]: Latrophilin-teneurin complexes regulate neuronal circuit assembly
- [33]: CNTNAP4 is involved in dopaminergic neuron function and synaptic transmission
- [37]: GDNF-GFRα1 complexes support synaptic cell adhesion

## Program: Growth Factor Receptor Signaling
Receptor tyrosine kinases and associated signaling molecules that drive proliferation, survival, and differentiation in GBM. This program includes FGFR2 (fibroblast growth factor receptor), KIT (stem cell growth factor receptor), GFRA1 (GDNF family receptor alpha-1), and downstream signaling mediators. GBM frequently exhibits aberrant RTK signaling which activates Ras/MAPK and PI3K/AKT/mTOR pathways, driving rapid proliferation and therapy resistance.

**Predicted impacts**
- Enhanced proliferation through Ras/MAPK and PI3K/AKT signaling
- Increased survival signaling and resistance to apoptosis
- Promotion of stemness and self-renewal in cancer stem cells
- Enhanced migration and invasion capabilities
- Reduced responsiveness to differentiation cues

**Evidence summary**
FGFR2 is preferentially expressed on astrocytes in normal brain but its expression decreases with glioma grade, suggesting loss-of-function role in normal astrocytes but potential reprogramming in GBM. FGFR1 is preferentially expressed on glioma stem cells (GSCs) where it regulates stem cell transcription factors (SOX2, OLIG2, ZEB1). KIT is a well-characterized proto-oncogene. GFRA1 is a co-receptor for GDNF signaling supporting neuronal survival. Aberrant RTK signaling is one of the most frequent molecular alterations in GBM, with combined Ras and AKT pathway activation inducing GBM formation in mice.

**Atomic biological processes**
- Fibroblast growth factor receptor signaling. Genes: FGFR2, RASGEF1B, FGD4
  - [26]: FGFR1-3 regulate GBM cell proliferation, migration, invasion, and cancer stemness through multiple pathways
  - [29]: FGFR dysregulation is a major driver of glioma development, and FGFR inhibition is a therapeutic strategy
- Receptor tyrosine kinase transactivation. Genes: KIT, GFRA1, FGFR2, RASGEF1B
  - [19]: RTKs control glioma cell growth, survival, migration, invasion, and angiogenesis through Ras/MAPK and PI3K/AKT pathways
  - [22]: PI3K/AKT/mTOR and Ras/RAF/MEK/ERK pathways are major drivers of GBM proliferation
- GDNF-GFRα signaling axis. Genes: GFRA1
  - [40]: GDNF binds GFRα1 with high affinity to support neuronal survival and neuroprotection
  - [37]: GDNF-GFRα1 complex supports synaptic adhesion and dendritic spine formation

**Atomic cellular components**
- Receptor tyrosine kinase complexes. Genes: FGFR2, KIT, GFRA1
  - [19]: RTKs consist of extracellular ligand-binding domain, transmembrane domain, and intracellular tyrosine kinase domain

**Required genes (not in input)**
- Genes: EGFR, PDGFRA, MET, IGF1R, VEGFR2, KRAS, BRAF, PI3K, AKT, mTOR, MEK, ERK
  - [19]: EGFR, PDGFRA, MET, IGF1R, and VEGFR are major RTKs in GBM; Ras/MAPK and PI3K/AKT are essential downstream pathways
  - [22]: RAF, MEK, ERK are components of Ras/MAPK pathway; PI3K and AKT are components of survival pathway

**Program citations**
- [19]: RTK signaling is among the most frequent molecular alterations in GBM
- [22]: PI3K/AKT and Ras/MAPK pathways are major drivers of GBM progression
- [26]: FGFR1 is a key regulator of tumor growth, invasion, and cancer stemness in GBM
- [29]: FGFR dysregulation in glioma and therapeutic targeting opportunities

## Program: Ion Channel-Mediated Cellular Signaling
Voltage-gated and ligand-gated ion channels that regulate intracellular calcium, potassium, and chloride dynamics. This program includes NMDA receptors (GRIN2A), GABA receptors (GABBR2, GLRA2), ion channels (TRPM3, TRPC5, KCNC2, KCNJ6), and calcium-dependent enzymes (PDE1A, PDE1C). In GBM, ion channel activity regulates cell proliferation, migration, survival, and response to chemotherapy through calcium signaling and electrical properties.

**Predicted impacts**
- Altered intracellular calcium dynamics affecting proliferation
- Modified excitability and electrical properties of GBM cells
- Dysregulated response to neurotransmitter signals
- Enhanced or reduced drug sensitivity depending on channel status
- Altered cell-cell communication through gap junctions and synaptic-like contacts

**Evidence summary**
TRPM3 shows paradoxical regulation in glioma—initially identified as upregulated but loss of expression correlates with poor prognosis in GBM patients, suggesting loss-of-function tumor suppressor role. TRPM3 expression is significantly downregulated with increasing glioma grade and associated with poor patient survival. GRIN2A (NR2A) mediates synaptic NMDA receptor signaling important for synaptic plasticity. GABAergic and glycinergic systems are important for normal neural function and their dysregulation in GBM may contribute to loss of inhibitory control. Ion channel activity affects cellular calcium levels which regulate proliferation, migration, and survival. TMEM16 proteins are emerging as potential therapeutic targets in GBM through their dual roles as ion channels and phospholipid scramblases.

**Atomic biological processes**
- NMDA receptor-mediated glutamate signaling. Genes: GRIN2A
  - [7]: GRIN2A (NR2A) is a major NMDA receptor subunit involved in synaptic plasticity and cognitive functions
- TRPM ion channel regulation of proliferation. Genes: TRPM3, TRPC5
  - [4]: TRPM3 expression is downregulated in glioma with increasing grade; loss of TRPM3 is a poor prognosis marker in GBM
- GABAergic and glycinergic inhibitory signaling. Genes: GABBR2, GLRA2, CNTNAP4
  - [33]: CNTNAP4 regulates GABAergic synaptic transmission and GABA receptor expression
- Potassium channel regulation of excitability. Genes: KCNC2, KCNJ6, DPP10
  - [49]: DPP10 is a voltage-gated potassium channel associated protein regulating channel surface expression
- Calcium-dependent phosphodiesterase signaling. Genes: PDE1A, PDE1C, CPNE4
  - [43]: Synaptotagmin acts as Ca2+ sensor for neurotransmitter release, highlighting importance of calcium dynamics

**Atomic cellular components**
- Ion channel protein complexes. Genes: TRPM3, TRPC5, KCNC2, KCNJ6, ANO4
  - [44]: TMEM16 proteins function as Ca2+-activated Cl- channels and phospholipid scramblases
- Synaptic vesicle release machinery. Genes: SYT1, SYNPR, RPH3A, SLC17A6
  - [43]: Synaptotagmin is a Ca2+ sensor of synchronized neurotransmitter release at synapses

**Program citations**
- [4]: TRPM3 loss of expression is a poor prognosis marker in GBM; dysregulation closely related to glioma occurrence and development
- [43]: Synaptotagmin is critical calcium sensor for neurotransmitter release; its expression affects exocytosis
- [44]: TMEM16 proteins link Ca2+ signals with cellular electrical activity and are dysregulated in cancer
- [47]: Anoctamins (TMEM16) in brain cancer: calcium-activated chloride channels in EGFR signaling and glioma

## Program: Axon Guidance and Repulsive Signaling
Molecules mediating repulsive and attractive axon guidance cues that direct neuronal migration and process outgrowth. This program includes semaphorins (SEMA3C), ephrin ligands (EFNA5), netrin receptors (UNC5C, UNC5D), and associated signaling molecules (LINGO2, NDNF). In GBM, aberrant expression of guidance molecules contributes to altered cell migration patterns, invasion into surrounding brain tissue, and escape from normal developmental constraints.

**Predicted impacts**
- Altered migration direction and invasive behavior
- Loss of normal developmental constraints on cell movement
- Escape from peri-tumoral zones and infiltration into normal brain
- Reprogramming of guidance molecule responses
- Dysregulation of growth cone dynamics

**Evidence summary**
Semaphorins are classical developmental guidance molecules with established roles in axon guidance through growth cone collapse. In glioma, aberrant expression of semaphorins and their receptors contributes to altered migration. EFNA5 (ephrin-A5) is involved in cell guidance and growth factor signaling. UNC5C and UNC5D are netrin receptors with important roles in radial and tangential neuronal migration. UNC5D shows dynamic developmental expression controlled by transcription factors like FoxG1. These guidance molecules are normally involved in specifying neural circuit connectivity, and their dysregulation in GBM may promote invasion by overriding normal anti-migratory cues.

**Atomic biological processes**
- Semaphorin-mediated repulsion. Genes: SEMA3C, LINGO2
  - [31]: Semaphorins are potent inhibitors of axonal outgrowth; Sema3A induces growth cone collapse and actin depolymerization
  - [34]: Semaphorins mediate axon guidance (attraction or repulsion), cell migration, and cell death with temporal regulation of expression
- Ephrin-Eph signaling in cell guidance. Genes: EFNA5
  - [31]: Ephrin ligands interact with Eph receptors; VEGF and semaphorins can compete for shared receptors like neuropilin
- Netrin-UNC5 repulsive signaling. Genes: UNC5C, UNC5D
  - [32]: UNC-5 mediates repulsive netrin responses; heparin-binding activity of UNC5 is necessary for cell migration and axon guidance
  - [35]: Netrin-1 induces attractive and repulsive signals depending on receptors; UNC5D regulates radial migration with dynamic expression
- Growth cone collapse and actin dynamics. Genes: SEMA3C, FGD4, RASGEF1B
  - [31]: Semaphorins induce actin depolymerization and growth cone collapse; PAK and Rho kinases phosphorylate cofilin

**Atomic cellular components**
- Neuropilin-plexin receptor complexes. Genes: SEMA3C
  - [31]: Semaphorins bind neuropilins; NP-1 mediates both growth cone collapse and axoplasmic transport
- Growth cone cytoskeleton. Genes: SEMA3C, FGD4, RASGEF1B, CPNE4
  - [31]: Growth cone collapse involves actin depolymerization, endocytosis, and vesicular trafficking

**Program citations**
- [31]: Semaphorins and their receptors mediate axon guidance, cell migration, and growth cone collapse
- [32]: UNC5-netrin interactions mediate cell migration and axon guidance through heparin-binding mechanisms
- [34]: Semaphorins have multiple roles in axon guidance, cell migration, and cell death with temporal regulation
- [35]: Netrin and UNC5 signaling regulates migration of specific neuronal populations during development

## Program: RNA Binding and Post-transcriptional Regulation
RNA binding proteins and regulatory mechanisms controlling mRNA stability, localization, and translation. This program includes RBFOX1 (regulates alternative splicing), LIN28B (suppresses let-7 miRNAs and promotes oncogene translation), and SRRM4 (serine/arginine repetitive matrix protein). In GBM, dysregulation of these RNA binding programs drives stemness, proliferation, metabolic reprogramming, and therapy resistance through altered gene expression.

**Predicted impacts**
- Altered splicing of genes encoding adhesion and cytoskeletal proteins
- Derepression of multiple oncogenes through let-7 suppression
- Enhanced de novo lipid synthesis supporting rapid proliferation
- Activation of TGF-β signaling and mesenchymal phenotype
- Increased metabolic flexibility and therapy resistance

**Evidence summary**
LIN28B is overexpressed in diffuse midline glioma (DMG) and other GBM subtypes. LIN28B suppresses let-7 microRNAs, which normally suppress multiple oncogenes promoting stemness, proliferation, migration, and survival. LIN28B also directly binds and enhances translation of SREBP-1 and SCAP mRNAs, promoting de novo fatty acid synthesis critical for cancer cell proliferation. LIN28B expression correlates with tumor grade and poor survival. RBFOX1 regulates alternative splicing of genes required for muscle structure and function; its dysregulation leads to aberrant splicing and protein mislocalization. The coordinated dysregulation of RNA binding proteins in GBM suggests widespread post-transcriptional reprogramming supporting malignant phenotypes.

**Atomic biological processes**
- Alternative splicing regulation. Genes: RBFOX1, SRRM4
  - [14]: Rbfox1 is an RNA-binding protein regulating alternative splicing in multiple tissues; its loss causes aberrant splicing and protein mislocalization
  - [17]: Rbfox1/LASR complex controls alternative pre-mRNA splicing by binding GCAUG and other RNA motifs
- Let-7 microRNA suppression and oncogene derepression. Genes: LIN28B
  - [51]: LIN28B suppresses let-7 family of microRNAs, which normally suppress oncogenes; LIN28B overexpression in DMG promotes stemness and proliferation
- De novo fatty acid synthesis regulation. Genes: LIN28B
  - [54]: Lin28 enhances de novo fatty acid synthesis through post-transcriptional regulation of SREBP-1 and SCAP mRNAs
- TGF-β pathway activation through RNA binding. Genes: LIN28B
  - [57]: LIN28B promotes TGF-β signaling and TGFBI expression through a positive feedback loop

**Atomic cellular components**
- RNA binding protein complexes. Genes: RBFOX1, SRRM4, LIN28B
  - [14]: RBFOX1 regulates splicing of genes encoding myofibrillar and cytoskeletal proteins, and calcium handling proteins

**Program citations**
- [51]: LIN28B is overexpressed in DMG and suppresses let-7 microRNAs, promoting oncogene expression
- [54]: LIN28 proteins enhance de novo fatty acid synthesis through post-transcriptional regulation of SREBP-1
- [57]: LIN28B promotes TGF-β signaling and cell migration through feedback loop involving TGFBI
- [14]: RBFOX1 regulates alternative splicing of multiple genes important for cellular structure and function
- [17]: Rbfox1 complex controls splicing through RNA motif binding

## Program: Transcriptional Control of Neural Differentiation
Transcription factors that specify neuronal identity and regulate differentiation versus proliferation decisions. This program includes EBF family proteins (EBF1, EBF2), MYT1L (myelin transcription factor 1-like), CUX2 (cut-like homeobox 2), RUNX1T1 (runt-related transcription factor), and POU6F2 (POU class 6 homeobox). In GBM, dysregulation or loss of these differentiation-promoting transcription factors maintains stemness and proliferative capacity while blocking maturation.

**Predicted impacts**
- Resistance to terminal differentiation and maturation
- Maintenance of stem cell-like transcriptional signatures
- Continued expression of proliferation-promoting genes
- Loss of normal developmental growth arrest signals
- Dysregulation of glial vs. neuronal cell fate decisions

**Evidence summary**
EBF proteins are highly expressed during neural development and regulate commitment of neural progenitors to neuronal lineages. EBF1 is essential for B-cell development and also plays critical roles in neuronal development and differentiation. EBF proteins regulate expression of transcription factor genes (including nscl-1, emx1, aml1), cell structural proteins, and ion channels. MYT1L is a pioneer transcription factor critical for neuronal differentiation; its loss in mice leads to smaller brains and impaired neuronal maturation. MYT1L is upregulated during neuronal differentiation across multiple CNS regions. Loss of MYT1L leads to precocious intermediate progenitor differentiation and depletion of neural progenitor pools. In GBM, loss or downregulation of these differentiation-promoting transcription factors would maintain cells in proliferative, undifferentiated states resembling neural stem cells or glioma stem cells.

**Atomic biological processes**
- EBF-mediated neuronal differentiation. Genes: EBF1, EBF2
  - [25]: EBF proteins promote neuronal differentiation by stabilizing neuronal cell commitment and regulating expression of neuronal-specific markers
- MYT1L-directed neuronal maturation. Genes: MYT1L
  - [15]: MYT1L represses non-neuronal gene expression and promotes neuronal differentiation; MYT1L loss leads to precocious differentiation and progenitor depletion
- Fibroblast-to-neuron reprogramming. Genes: MYT1L, EBF1, EBF2
  - [15]: MYT1L enhances neuronal transdifferentiation when combined with ASCL1 and BRN2, significantly increasing conversion efficiency
- Transcriptional repression of proliferation programs. Genes: MYT1L, EBF1, EBF2
  - [15]: MYT1L represses cell cycle programs during neural differentiation, possibly through repression of Notch signaling pathway

**Atomic cellular components**
- Transcription factor complexes at promoters. Genes: EBF1, EBF2, MYT1L, CUX2, RUNX1T1, POU6F2
  - [25]: EBF proteins regulate expression of multiple functional classes of genes including transcription factors, structural proteins, and ion channels

**Program citations**
- [15]: MYT1L is critical for neuronal differentiation and maturation; its loss impairs neuronal development
- [25]: EBF proteins drive neuronal differentiation and regulate expression of multiple gene classes

## Program: Glioma Stem Cell Maintenance and Stemness
Programs supporting cancer stem cell (CSC) properties including self-renewal, multipotency, and therapy resistance. This program involves LIN28B-mediated repression of let-7 miRNAs, altered metabolism (MTAP, PIP5K1B), and signaling from growth factor receptors (FGFR2, KIT, GFRA1). GBM stem cells exhibit increased invasive potential and resistance to radiotherapy and chemotherapy, and are thought to be key drivers of tumor recurrence and progression.

**Predicted impacts**
- Self-renewal and multipotency despite differentiation cues
- Increased tumor-initiating capacity
- Enhanced resistance to chemotherapy and radiotherapy
- Promotion of tumor recurrence and progression
- Heterogeneous tumor composition with multiple cell states

**Evidence summary**
Glioma stem cells (GSCs) are a critical component of GBM with elevated invasive potential and therapy resistance. GSCs express high levels of stem cell markers and have capacity for self-renewal and multilineage differentiation. LIN28B overexpression maintains stemness through suppression of let-7 miRNAs. FGFR signaling is particularly important for GSC maintenance, with FGFR1 preferentially expressed on GSCs where it regulates critical stem cell transcription factors. The presence of multiple programs supporting stemness, invasion, and therapy resistance suggests GBM maintains a hierarchy of cancer stem cells driving tumorigenicity.

**Atomic biological processes**
- Let-7-independent stemness maintenance. Genes: LIN28B
  - [51]: LIN28B overexpression in DMG promotes stem-like phenotype with increased resistance to apoptosis and proliferation
- Glioma stem cell marker expression. Genes: EBF1, EBF2, MYT1L
  - [19]: GSCs have similarity to neural stem cells in self-renewal and capacity to differentiate into multiple lineages with high expression of stem cell markers
- Growth factor-driven self-renewal signaling. Genes: FGFR2, KIT, GFRA1
  - [26]: FGFR1 expression in malignant glioma associates with increased migration; FGFR1 is preferentially expressed on GSCs where it regulates stem cell transcription factors
- Enhanced invasion and migration capacity. Genes: COL6A3, ADAMTS3, POSTN, CDH9, CDH18, TENM2
  - [19]: GSCs have elevated invasive potential compared to non-stem tumor cells and are more resistant to therapy

**Program citations**
- [19]: GSCs are promising therapeutic targets with similarity to neural stem cells and elevated invasive potential
- [26]: FGFR1 is preferentially expressed on GSCs and regulates stem cell transcription factors
- [51]: LIN28B overexpression promotes stem-like properties in DMG

## Program: Spatial Gene Expression Heterogeneity
Genes supporting distinct gene expression programs in different tumor microenvironments—tumor core vs. infiltrated brain tissue. This program includes genes upregulated in proneural vs. mesenchymal cores (EBF1, EBF2, CDH genes), genes associated with hypoxic/necrotic regions (HIF-pathway related), and genes enriched in infiltrating cells (AC/OPC/NPC-like state markers). In GBM, spatial heterogeneity reflects both genomic alterations and microenvironmental influences that shape tumor cell behavior.

**Predicted impacts**
- Distinct proliferation and migration strategies in different microenvironments
- Phenotypic plasticity responding to hypoxia and nutrient availability
- Differential therapy response across tumor regions
- Regional heterogeneity in immune infiltration and inflammatory responses
- Spatial segregation of proneural and mesenchymal phenotypes

**Evidence summary**
Recent spatial transcriptomics studies reveal that GBM exhibits substantial transcriptional heterogeneity organized by microenvironment. In the tumor core, cells express genes associated with proneural or mesenchymal subtypes. In infiltrated brain tissue, these differences diminish and cells instead upregulate genes associated with immature neural cell states (AC/NPC/OPC-like). Necrotic and microvascular proliferation (MVP) regions show distinct hypoxia-induced gene expression. COL6A3 is particularly enriched in mesenchymal cores and MVP regions. Notch signaling components and glial differentiation genes are increased in infiltrated tissue. This spatial heterogeneity likely reflects both genomic alterations and microenvironmental plasticity, with tumor cells adapting their gene expression programs to local conditions.

**Atomic biological processes**
- Mesenchymal state gene expression. Genes: COL6A3, TGFBI, POSTN, ADAMTS3, CDH9, CDH18
  - [3]: Malignant cells in tumor core express genes associated with MES-like states; MES-like signatures decrease in invasive cells while AC/OPC/NPC-like states increase in infiltrated tissue
  - [9]: COL6A3 is strongly enriched in mesenchymal GBM relative to proneural and classical subtypes
- Proneural and oligodendrocytic-like state maintenance. Genes: EBF1, EBF2, MYT1L
  - [3]: Proneural tumors express genes associated with neurodevelopmental pathways; these cells increase expression of AC/OPC/NPC-like genes in infiltrated regions
- Hypoxia-induced gene expression. Genes: POSTN, TGFBI, CDH9, ADAMTS3
  - [3]: Pseudopalisading cells surrounding necrosis show upregulation of genes induced by hypoxia; MVP regions show downregulation of EGFR but upregulation of mesenchymal markers
  - [6]: Tumor cells respond to hypoxic conditions by upregulating HIFs which activate gene expression of downstream targets for cell survival
- Notch and glial differentiation signaling. Genes: CDH9, CDH18, CDH4, EFNA5, SEMA3C
  - [3]: Malignant cells in infiltrated tissue increase expression of genes related to notch signaling and glial cell differentiation

**Program citations**
- [3]: Spatial transcriptomics reveals distinct gene expression in tumor core vs. infiltrated tissue with shifts in malignant cell composition
- [6]: Hypoxic conditions in GBM activate HIF signaling and alter cell survival and metabolic programs
- [9]: COL6A3 enrichment in mesenchymal GBM and MVP regions correlates with aggression

## Program: Metabolic Reprogramming and Lipid Synthesis
Genes supporting altered metabolic states in GBM including enhanced glycolysis, de novo lipid synthesis, and alternative nutrient utilization. LIN28B drives fatty acid synthesis through SREBP-1 pathway; MTAP and associated genes support purine metabolism; metabolic enzymes support rapid biomass accumulation. In GBM, metabolic reprogramming enables rapid proliferation and supports therapy resistance through ER stress evasion and lipid-dependent membrane expansion.

**Predicted impacts**
- Enhanced de novo lipid synthesis supporting rapid membrane expansion
- Increased biomass production enabling rapid proliferation
- Altered cellular stress responses and ER homeostasis
- Metabolic flexibility supporting survival under nutrient restriction
- Enhanced therapy resistance through metabolic adaptation

**Evidence summary**
LIN28B-mediated regulation of SREBP-1 promotes de novo fatty acid synthesis, which is critical for cancer cell proliferation and survival. This metabolic reprogramming supports rapid membrane biogenesis and supports ER stress evasion. Glioma cells increase glucose uptake and utilize multiple nutrient sources for biomass production. MTAP involvement in purine metabolism and SREBP-1 pathway suggests coordination of nucleotide and lipid synthesis. The presence of multiple metabolic regulatory genes suggests comprehensive reprogramming of cellular metabolism to support rapid proliferation and survival under adverse conditions.

**Atomic biological processes**
- De novo fatty acid and lipid synthesis. Genes: LIN28B, MTAP, PIP5K1B
  - [54]: Lin28 enhances de novo fatty acid synthesis through post-transcriptional regulation of SREBP-1, SCAP, and fatty acid synthetic enzymes
  - [57]: LIN28B promotes expression of TGF-β pathway genes which regulate ECM and metabolic processes
- ER stress response and lipid homeostasis. Genes: LIN28B
  - [54]: Lin28-mediated enhancement of fatty acid synthesis protects cells from ER stress through altered lipid composition
- Glucose and nutrient uptake. Genes: SLC38A11
  - [6]: Glioma cells increase uptake of glucose and other nutrients to support aggressive biomass production in GBM

**Atomic cellular components**
- Lipid droplets and ER membranes. Genes: LIN28B, MTAP
  - [54]: Lin28 regulates lipid accumulation in lipid droplets and affects ER stress through lipid metabolism

**Program citations**
- [54]: Lin28 proteins enhance de novo fatty acid synthesis through SREBP-1 pathway
- [57]: LIN28B promotes TGF-β signaling affecting metabolic processes
- [6]: GBM cells exhibit metabolic reprogramming with increased nutrient uptake

## Bibliography
1. Tingfeng W, Yuntao L, Baohui L, Shenqi Z, Liquan W, Xiaonan Z, et al.. Expression of Ferritin Light Chain (FTL) Is Elevated in Glioblastoma, and FTL Silencing Inhibits Glioblastoma Cell Proliferation via the GADD45/JNK Pathway.. PloS one [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26871431/
2. Available from: https://patents.google.com/patent/WO2018204764A1/en
3. Harwood DSL, Pedersen V, Bager NS, Schmidt AY, Stannius TO, Areškevičiūtė A, et al.. Glioblastoma cells increase expression of notch signaling and synaptic genes within infiltrated brain tissue. Nature Communications [Internet]. 2024Sep9;15(1). Available from: https://www.nature.com/articles/s41467-024-52167-y
4. Zhigang C, Han X, Jun L, JiaJia Z, Ruixiang H, Yufei X, et al.. Roles of TRPM channels in glioma.. Cancer biology & therapy [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11062369/
5. Available from: https://discover.nci.nih.gov/cellminerdata/html/VARIANT_PROTEIN_AFFECTING_LIST.html
6. Pratibha S, Ashley A, Jiyong L, Vinay KP. Tumor microenvironment in glioblastoma: Current and emerging concepts.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10034917/
7. Paul JH, David MB. GRIN2A (NR2A): a gene contributing to glutamatergic involvement in schizophrenia.. Molecular psychiatry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10730418/
8. David de A-D, Isabel M-W, Jaime F-B, Cristina G-S. Stick around: Cell-Cell Adhesion Molecules during Neocortical Development.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7826847/
9. Junghwa C, Erika AD, Emily MC, Annabelle F, Manish KA, Sanjay K. Glioma Cells Secrete Collagen VI to Facilitate Invasion.. bioRxiv : the preprint server for biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760023/
10. Available from: https://www.ncbi.nlm.nih.gov/gene/14811
11. Lin J, Wang C, Redies C. Restricted expression of classic cadherins in the spinal cord of the chicken embryo. Frontiers in Neuroanatomy [Internet]. 2014Mar31;8. Available from: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2014.00018/full
12. Day ZI, Roberts-Thomson S, Nouri YJ, Dalton NS, Wang SS, Davenport A, et al.. Defining the extracellular matrix for targeted immunotherapy in adult and pediatric brain cancer. npj Precision Oncology [Internet]. 2025Jun14;9(1). Available from: https://www.nature.com/articles/s41698-025-00956-z
13. Calabresi P, Mechelli A, Natale G, Volpicelli-Daley L, Di LG, Ghiglieri V. Alpha-synuclein in Parkinson’s disease and other synucleinopathies: from overt neurodegeneration back to early synaptic dysfunction. Cell Death &amp; Disease [Internet]. 2023Mar1;14(3). Available from: https://www.nature.com/articles/s41419-023-05672-9
14. Simona P, Jimena G, Adan D-A, Mark K, Ravi KS, Amy H, et al.. The RNA-binding protein Rbfox1 regulates splicing required for skeletal muscle structure and function.. Human molecular genetics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/25575511/
15. Chen J, Yen A, Florian CP, Dougherty JD. MYT1L in the making: emerging insights on functions of a neurodevelopmental disorder gene. Translational Psychiatry [Internet]. 2022Jul22;12(1). Available from: https://www.nature.com/articles/s41398-022-02058-x
16. Jacqueline B. The Synaptic Function of α-Synuclein.. Journal of Parkinson's disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4927875/
17. Available from: https://genesdev.cshlp.org/content/39/5-6/364.full
18. Available from: https://www.uniprot.org/uniprotkb/Q9UL68/entry
19. Manali T, Jennifer H, Laura AN, Jasmin L, Nina J. Receptor Tyrosine Kinase Signaling and Targeting in Glioblastoma Multiforme.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7918566/
20. Available from: https://www.ncbi.nlm.nih.gov/gene/140919
21. Zheng Z, Zong Y, Ma Y, Tian Y, Pang Y, Zhang C, et al.. Glucagon-like peptide-1 receptor: mechanisms and advances in therapy. Signal Transduction and Targeted Therapy [Internet]. 2024Sep18;9(1). Available from: https://www.nature.com/articles/s41392-024-01931-z
22. Available from: https://www.nature.com/articles/sigtrans201740
23. Available from: https://www.uniprot.org/uniprotkb/Q9P2U8/entry
24. Available from: https://www.ncbi.nlm.nih.gov/gene/2641
25. Yangsook SG, Monica LV. EBF factors drive expression of multiple classes of target genes governing neuronal development.. Neural development [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3113313/
26. Ana J-P, Florian AS. Fibroblast Growth Factor Receptor Functions in Glioblastoma.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6678715/
27. Trevor M, Fabienne EP. To Stick or Not to Stick: The Multiple Roles of Cell Adhesion Molecules in Neural Circuit Assembly.. Frontiers in neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9096351/
28. Available from: https://aacrjournals.org/mcr/article/7/12/1893/90355/Emerging-Roles-of-the-EBF-Family-of-Transcription
29. Deshors P, Kheil Z, Ligat L, Gouazé-Andersson V, Cohen-Jonathan ME. FGFR inhibition as a new therapeutic strategy to sensitize glioblastoma stem cells to tumor treating fields. Cell Death Discovery [Internet]. 2025Jun4;11(1). Available from: https://www.nature.com/articles/s41420-025-02542-5
30. Burbach JPH, Meijer DH. Latrophilin’s Social Protein Network. Frontiers in Neuroscience [Internet]. 2019Jun26;13. Available from: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.00643/full
31. Yoshio G, Takaaki I, Yukio S, Fumio N. Semaphorins as signals for cell repulsion and invasion.. The Journal of clinical investigation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC150952/
32. Priest JM, Nichols EL, Smock RG, Hopkins JB, Mendoza JL, Meijers R, et al.. Structural insights into the formation of repulsive netrin guidance complexes. Science Advances [Internet]. 2024Feb16;10(7). Available from: https://www.science.org/doi/10.1126/sciadv.adj8083
33. Wenlong Z, Miaomiao Z, Weiye L, Junwei G, Feng G, Yuanquan L, et al.. CNTNAP4 deficiency in dopaminergic neurons initiates parkinsonian phenotypes.. Theranostics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7053186/
34. Available from: https://www.ncbi.nlm.nih.gov/books/NBK6446/
35. Satoru Y, Yuki B, Kohji S. Involvement of Netrins and Their Receptors in Neuronal Migration in the Cerebral Cortex.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7843923/
36. Zhang W, Ding L, Chen H, Zhang M, Ma R, Zheng S, et al.. Cntnap4 partial deficiency exacerbates α-synuclein pathology through astrocyte–microglia C3-C3aR pathway. Cell Death &amp; Disease [Internet]. 2023Apr22;14(4). Available from: https://www.nature.com/articles/s41419-023-05807-y
37. Houghton FM, Adams SE, Ríos AS, Masino L, Purkiss AG, Briggs DC, et al.. Architecture and regulation of a GDNF-GFRα1 synaptic adhesion assembly. Nature Communications [Internet]. 2023Nov20;14(1). Available from: https://www.nature.com/articles/s41467-023-43148-8
38. Available from: https://en.wikipedia.org/wiki/Fas_ligand
39. Available from: https://www.ncbi.nlm.nih.gov/gene/23327
40. A S, B JH, L O, M M. Glial cell line neurotrophic factor-family receptor alpha-1 is present in central neurons with distinct phenotypes.. Neuroscience [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/12535958/
41. Andreas S, Philipp JJ, Shigekazu N. The many roles of FAS receptor signaling in the immune system.. Immunity [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2956119/
42. Available from: https://www.cellsignal.com/products/primary-antibodies/nedd4l-antibody/4013
43. Gábor N, Jun HK, Zhiping PP, Ulf M, Jens R, Thomas CS, et al.. Different effects on fast exocytosis induced by synaptotagmin 1 and 2 isoforms and abundance but not by phosphorylation.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6674391/
44. Zeqi H, Zoya I, Zhe Z, Xiaoqiang C, Ayesha M, Jianquan L, et al.. TMEM16 proteins: Ca. International journal of molecular medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11315658/
45. Jantina M, Sharad K. NEDD1: function in microtubule nucleation, spindle assembly and beyond.. The international journal of biochemistry & cell biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/17005434/
46. Xiang Y, Cui L, Yao J, Lou X, Wu M, Huo J, et al.. Synaptotagmin-1 serves as a primary Zn2+ sensor to mediate spontaneous neurotransmitter release under pathological conditions. Nature Communications [Internet]. 2025Aug2;16(1). Available from: https://www.nature.com/articles/s41467-025-62496-1
47. Brittany D, Lauren U, Emily VF, Terrance GJ. Anoctamins and Calcium Signalling: An Obstacle to EGFR Targeted Therapy in Glioblastoma?. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9740065/
48. Jodi K, Raymundo A-A, Bernardo G, Sabine P. Microtubule nucleation for spindle assembly: one molecule at a time.. Trends in biochemical sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10789498/
49. Tong C, Wei-Ping G, Catherine AA. Dipeptidyl peptidase 10 (DPP10(789)): a voltage gated potassium channel associated protein is abnormally expressed in Alzheimer's and other neurodegenerative diseases.. BioMed research international [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/25025038/
50. Lifang M, Kogo T, Gareth T, Da-Ting L, Richard LH. GRIP1 and 2 regulate activity-dependent AMPA receptor recycling via exocyst complex interactions.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2973854/
51. Truman K, Tina H, Jin Q, Shejuan A, Noah B, Scott C, et al.. LIN28B and Let-7 in Diffuse Midline Glioma: A Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10296230/
52. Available from: https://en.wikipedia.org/wiki/DPP10
53. Available from: https://www.uniprot.org/uniprotkb/Q9C0E4/entry
54. Zhang Y, Li C, Hu C, Wu Q, Cai Y, Xing S, et al.. Lin28 enhances
                    <i>de novo</i>
                    fatty acid synthesis to promote cancer progression via
                    <scp>SREBP</scp>
                    ‐1. EMBO reports [Internet]. 2019Aug5;20(10). Available from: https://www.embopress.org/doi/10.15252/embr.201948115
55. Zhaoni W, Wanshan L, Shixing C, Xiao XT. Role of ADAM and ADAMTS proteases in pathological tissue remodeling.. Cell death discovery [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10710407/
56. Christian V, Silke G, Mats P, Patrik M, Ursula H. Characterization of SMOC-2, a modular extracellular calcium-binding protein.. The Biochemical journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC1223551/
57. Puthdee N, Sriswasdi S, Pisitkun T, Ratanasirintrawoot S, Israsena N, Tangkijvanich P. The LIN28B/TGF-β/TGFBI feedback loop promotes cell migration and tumour initiation potential in cholangiocarcinoma. Cancer Gene Therapy [Internet]. 2021Sep21;29(5). Available from: https://www.nature.com/articles/s41417-021-00387-5
58. Available from: https://maayanlab.cloud/Harmonizome/gene/ADAMTS3
59. Qiang G, Hsiao-Pei M, Jian Z. Secreted modular calcium-binding proteins in pathophysiological processes and embryonic development.. Chinese medical journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6831058/
60. Hao W, Yin-Hai X, Yi G. Novel prognostic marker TGFBI affects the migration and invasion function of ovarian cancer cells and activates the integrin αvβ3-PI3K-Akt signaling pathway.. Journal of ovarian research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10885438/
