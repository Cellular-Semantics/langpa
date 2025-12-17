# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and neural progenitor cells
- Disease: Astrocytoma (including lower-grade gliomas, anaplastic astrocytoma, and glioblastoma)
- Tissue: Brain (cerebral cortex and other CNS regions)

## Input Genes
THSD7A, RND3, SETBP1, PROX1, MYT1L, NEDD4L, FRMD4A, SILC1, FNBP1L, TOX3, KLHDC8A, PAK3, GPR137C, ELAVL4, PKIA, INSM1, KALRN, KCNH7, AC099792.1, CEMIP2, GRIK2, CACNA2D1, STMN2, SOX11, MIR99AHG, ... (200 total)

## Program: INSM1-Driven Intermediate Progenitor Cell Identity
INSM1 serves as a master transcriptional regulator that locks astrocytoma cells into an intermediate progenitor cell-like state reminiscent of developmental neural progenitor cells that normally give rise to neurons. INSM1 drives expression of downstream transcription factors and effector genes that prevent terminal differentiation while maintaining stem-like self-renewal capacity. This program hijacks developmental transcriptional networks normally governing the transition between radial glia and differentiating neurons, instead using them to sustain malignant progenitor-like identity. Multiple direct and indirect targets of INSM1 are present in the gene list, creating a coordinated transcriptional program that maintains cellular plasticity and stemness.

**Predicted impacts**
- Sustained maintenance of intermediate progenitor cell-like transcriptional state despite malignant transformation
- Prevention of spontaneous neuronal differentiation and associated cell cycle exit
- Enhanced cellular plasticity enabling dynamic phenotypic transitions
- Resistance to differentiation-inducing signals and therapies targeting terminal differentiation
- Elevated expression of stemness-associated genes and self-renewal pathways

**Evidence summary**
INSM1 is highly expressed in human glioblastoma tumors and, during cortical development, in intermediate progenitor cells which give rise to neurons. INSM1 knockdown in both isogenic glioblastoma models and primary tumors disrupts oncogenic gene expression and inhibits in vivo tumorigenicity. SOX11 and SOX4, SoxC family members, target the promoters of genes induced upon neuronal differentiation of adult neural stem cells and are dysregulated in gliomas. EBF1 and EBF3 regulate neuronal differentiation pathways and are included in the gene list. MYT1L encodes a transcription factor essential for neuronal identity that is maintained in transformed cells.

**Atomic biological processes**
- Intermediate progenitor cell identity maintenance. Genes: INSM1, SOX11, SOX4, EBF1, EBF3
  - [8]: INSM1 expression drives intermediate progenitor network and is essential for glioblastoma tumorigenicity; knockdown disrupts oncogenic programs
  - [15]: INSM1 governs neuronal progenitor state critical for glioblastoma plasticity and maintenance of transformed phenotype
- Prevention of terminal neuronal differentiation. Genes: INSM1, ZEB1, CDK6
  - [8]: INSM1 maintains undifferentiated state; knockdown promotes differentiation and reduces tumorigenicity
- Neural stem cell maintenance and self-renewal. Genes: INSM1, SOX11, SOX4, EBF1, EBF3, MYT1L
  - [5]: SoxC transcription factors target promoters of genes induced during neural differentiation and maintain progenitor identity

**Atomic cellular components**
- INSM1-dependent transcriptional complex. Genes: INSM1, SOX11, SOX4, EBF1, EBF3, CDK6
  - [8]: INSM1 forms transcriptional network with other transcription factors regulating progenitor fate

**Required genes (not in input)**
- Genes: ASCL1, NEUROG2, NEUROD1, REST, RCOR1, RCOR2
  - [8]: REST and corepressor complex interact with INSM1 to regulate developmental transcriptional programs

**Program citations**
- [8]: Central role of INSM1 in glioblastoma pathogenesis and plasticity demonstrated through isogenic model systems and primary tumor analysis
- [15]: INSM1 governs neuronal progenitor state that drives glioblastoma functional plasticity
- [5]: SoxC transcription factors regulate neuronal differentiation and are dysregulated in malignancy

## Program: SRRM4-Mediated Neuronal Splicing Regulation
SRRM4 (also known as nSR100) drives tissue-specific alternative splicing patterns that produce neuronal isoforms of genes involved in synaptic transmission, cytoskeletal organization, and signaling. In normal neurons, SRRM4 expression increases during neural development and directs the production of neuronal-specific exons in hundreds of target genes. In astrocytomas, SRRM4 enables production of neuronal isoforms despite the maintenance of undifferentiated progenitor-like transcriptional identity, creating cells with a chimeric phenotype combining progenitor transcription patterns with neuronal protein isoforms. This uncoupling of transcriptional identity from translational output enhances cellular plasticity and enables rapid phenotypic switching.

**Predicted impacts**
- Production of neuronal protein isoforms despite maintenance of progenitor-like transcriptional state
- Enhanced plasticity through decoupling of transcriptional identity from protein isoform repertoire
- Rapid switching between progenitor and neuronal phenotypes through alternative splicing without transcriptional reprogramming
- Adoption of neuronal-like cytoskeletal organization and morphology
- Integration of neuronal signaling responses into undifferentiated tumor cell framework

**Evidence summary**
SRRM4 (serine/arginine repetitive matrix protein 4) is a neuron-specific splicing regulator that drives tissue-specific alternative splicing patterns producing neuronal isoforms. The presence of SRRM4 alongside splicing factor targets (MAP1B, STMN2, TUBB3) and downstream RNA-binding proteins (ELAVL4, RBFOX3, CELF4) indicates that astrocytomas maintain comprehensive neuronal splicing machinery. Recent studies demonstrate that splicing factor expression is tightly regulated during neural development and that dysregulation of splicing factors contributes to neural plasticity in gliomas.

**Atomic biological processes**
- Alternative splicing of neuronal identity genes. Genes: SRRM4, SRRM3, ELAVL4, RBFOX3, CELF4
  - [14]: Ultraconserved regions and splicing regulatory networks control neuronal alternative splicing patterns during brain development
  - [34]: Type I UCRs within protein-coding genes modulate brain development by regulating alternative splicing of genes controlling neural differentiation
- Neuronal isoform production from progenitor-like transcriptional state. Genes: SRRM4, MAP1B, STMN2, TUBB3
  - [14]: Splicing factors control production of neuronal versions of cytoskeletal and development-related proteins

**Atomic cellular components**
- Spliceosome-associated SRRM4 complex. Genes: SRRM4, SRRM3, CELF4
  - [14]: SRRM4 recruits spliceosome machinery to neuronal exons, promoting their inclusion in mature transcripts
- RNA stability regulation apparatus. Genes: ELAVL4, ELAVL2, RBFOX3
  - [14]: ELAV proteins bind AU-rich elements in neuronal transcripts, stabilizing neuronal mRNAs

**Required genes (not in input)**
- Genes: SNRPB, SNRNP70, SF1, SF3B1, U2AF35
  - [14]: Spliceosome components are required for SRRM4-mediated alternative splicing

**Program citations**
- [14]: Splicing factors control neuronal gene expression and are dysregulated in neural development and tumorigenesis
- [34]: Type I ultraconserved regions regulate splicing of developmental genes, suggesting multilayered control of splicing programs

## Program: ROBO-DCC-Mediated Axon Guidance and Tumor Cell Migration
The ROBO (roundabout) and DCC (deleted in colorectal cancer) pathways represent canonical axon guidance mechanisms that are co-opted in astrocytomas to drive tumor cell migration and invasion. During normal development, these pathways guide neuronal migration and axon pathfinding through interpretation of SLIT and NETRIN ligands in the extracellular environment. In astrocytomas, activation of ROBO and DCC signaling promotes tumor cell migration through brain tissue, with DCC functioning in its pro-migratory capacity while potentially evading its pro-apoptotic functions. The presence of multiple ROBO family members (ROBO1, ROBO2, ROBO3) provides pathway redundancy ensuring robust activation of migration programs.

**Predicted impacts**
- Enhanced tumor cell migration and invasion through brain parenchyma
- Responsiveness to SLIT and NETRIN signals in tumor microenvironment
- Pathway redundancy (multiple ROBO family members) ensuring robust migration despite individual gene disruption
- Potential evasion of pro-apoptotic DCC signaling while maintaining pro-migratory functions
- Integration of guidance cues from infiltrating neurons and glia within tumor niche

**Evidence summary**
The ROBO-DCC pathway represents well-characterized axon guidance mechanisms dysregulated in gliomas. ROBO1, ROBO2, ROBO3, and DCC are all present in the gene list, indicating that astrocytomas maintain multiple pathways for chemotactic migration. UNC79 and BOC are netrin pathway components that modulate DCC signaling. NRP1 (neuropilin 1) is present and functions as a receptor for semaphorin guidance cues in addition to VEGF signaling. The presence of redundant pathway components suggests that tumor cells have evolved robust mechanisms for interpreting environmental guidance cues to drive invasion.

**Atomic biological processes**
- Chemotactic migration and invasion. Genes: ROBO1, ROBO2, ROBO3, DCC, NRP1
  - [14]: ROBO and DCC pathways guide cell migration during neural development and are dysregulated in glioma invasion
- Response to guidance ligands (SLIT and NETRIN). Genes: ROBO1, ROBO2, ROBO3, DCC, NEO1
  - [34]: Axon guidance molecules create repulsive and attractive cues guiding neuronal migration
- Suppression of pro-apoptotic DCC signaling. Genes: DCC, UNC79, BOC
  - [14]: DCC functions both in survival/migration and in pro-apoptotic pathways depending on NETRIN availability and signaling context

**Atomic cellular components**
- ROBO transmembrane receptor complex. Genes: ROBO1, ROBO2, ROBO3
  - [14]: ROBO proteins function as transmembrane receptors for SLIT guidance molecules
- DCC/NETRIN signaling complex. Genes: DCC, UNC79, BOC
  - [14]: DCC and associated proteins form signaling complex responding to NETRIN ligands

**Required genes (not in input)**
- Genes: SLIT1, SLIT2, SLIT3, NETRIN1, NETRIN3
  - [14]: SLIT and NETRIN ligands are required for ROBO and DCC signaling and are often dysregulated in gliomas

**Program citations**
- [14]: Comprehensive review of axon guidance pathways dysregulated in glioma biology
- [34]: Axon guidance networks control neuronal migration and are co-opted in tumor progression

## Program: Glutamatergic Neurotransmission and Synaptic Plasticity
Astrocytomas maintain comprehensive machinery for glutamatergic synaptic transmission and integration with neural circuits. This program includes vesicular glutamate transporters, ionotropic glutamate receptors, and associated proteins that enable tumor cells to form functional synapses and respond to neuronal activity. The presence of multiple glutamate receptor subunits (GRIA4, GRIK2) and the vesicular transporter SLC17A6 (VGLUT2) suggests that astrocytoma cells adopt neuronal-like electrophysiological properties and can both receive signals from surrounding neurons and potentially influence neuronal function. This neural circuit integration represents a novel mechanism of tumor-microenvironment crosstalk.

**Predicted impacts**
- Formation of functional synapses between glioma cells and surrounding neurons
- Reception of glutamatergic signals from infiltrating neurons and activation of tumor cell signaling cascades
- Potential elevation of intracellular calcium and activation of calcium-dependent oncogenic pathways
- Integration into neural circuits enabling bidirectional communication between tumor and neurons
- Neuronal activity-dependent regulation of tumor cell behavior and survival

**Evidence summary**
SLC17A6 (VGLUT2) is a vesicular glutamate transporter normally restricted to excitatory neurons and is present in the gene list. GRIA4 encodes AMPA receptor subunit GluA4 involved in fast synaptic transmission. GRIK2 encodes kainate receptor subunit GluK2. CACNA2D1 encodes the alpha-2/delta-1 subunit of L-type voltage-gated calcium channels. KCNH7 encodes a potassium channel important for neuronal repolarization. SYT4 and SYT14 encode synaptotagmins involved in vesicle fusion. PCLO encodes piccolo, a presynaptic active zone protein. The presence of this comprehensive synaptic machinery in astrocytomas indicates that tumor cells adopt neuronal-like electrophysiological properties and can form functional synapses.

**Atomic biological processes**
- Glutamate synthesis and packaging into synaptic vesicles. Genes: SLC17A6, SYT4, SYT14, PCLO
  - [14]: Glutamate transporters and synaptic vesicle proteins are essential for glutamatergic neurotransmission
- Ionotropic glutamate receptor signaling. Genes: GRIA4, GRIK2, CACNA2D1, KCNH7
  - [27]: Glutamate receptor dysregulation alters neural communication and synaptic plasticity
  - [30]: GRIA4 AMPA receptor subunit involved in fast synaptic transmission and plasticity
- Calcium-dependent synaptic processes. Genes: CACNA2D1, PCSK2, ADCY8
  - [14]: Calcium signaling regulates synaptic plasticity and dendritic integration

**Atomic cellular components**
- Synaptic vesicle machinery. Genes: SLC17A6, SYT4, SYT14, PCLO, STMN2
  - [14]: Synaptotagmins and piccolo regulate synaptic vesicle docking and release
- Postsynaptic density structure. Genes: GRIA4, GRIK2, NRXN1, CNTN2, CTNNA2
  - [14]: Postsynaptic density contains glutamate receptors, scaffolding proteins, and adhesion molecules

**Required genes (not in input)**
- Genes: PSD95, SAP102, GRIN1, GRIN2A, GRIN2B
  - [27]: NMDA receptors and postsynaptic density scaffolding proteins are required for synaptic function

**Program citations**
- [27]: Glutamate receptor signaling controls neuronal communication and is altered in disease states
- [14]: Synaptic plasticity genes are dysregulated in neural development and tumorigenesis

## Program: Cell Adhesion and Junctional Organization
Astrocytomas maintain comprehensive cell adhesion machinery including cadherins, contactins, neurexins, and ephrin-EphB signaling systems. These adhesion systems serve dual roles: (1) enabling formation of cohesive tumor tissues through organized junctional structures, and (2) facilitating interactions between tumor cells and surrounding neural tissue including neurons and microglia. Classical cadherins and their associated catenins link cells through adherens junctions, while immunoglobulin superfamily adhesion molecules like contactins and neurexins mediate both homophilic cell-cell interactions and interactions with diverse binding partners. The spatial organization of these adhesion molecules likely contributes to the architecture of the tumor microenvironment.

**Predicted impacts**
- Organized tissue architecture within tumors through adherens junction formation
- Heterophilic cell-cell interactions between glioma cells and infiltrating neurons
- Integration of bidirectional ephrin-EphB signaling enabling receptor-ligand crosstalk
- Mechanical stability of tumor tissue through catenin-based cytoskeletal linkage
- Spatially organized interactions with microglial cells and vascular endothelium

**Evidence summary**
CTNNA2 encodes alpha-catenin 2, essential for adherens junction strength. CNTN2 (contactin 2) is an immunoglobulin superfamily adhesion molecule important for neuronal development. NRXN1 (neurexin 1) is a presynaptic adhesion molecule interacting with postsynaptic neuroligins. EPHB2 and EFNB2 encode receptor and ligand for bidirectional ephrin-EphB signaling. KIRREL1 encodes a cell adhesion molecule of the nephrin superfamily. The presence of multiple adhesion system components suggests that astrocytomas maintain organized junctional architecture enabling both internal tissue cohesion and external interactions with the microenvironment.

**Atomic biological processes**
- Adherens junction formation and maintenance. Genes: CTNNA2, CNTN2, NRXN1, EPHB2, EFNB2
  - [14]: Cadherins and catenins form adherens junctions essential for tissue organization
- Immunoglobulin superfamily cell-cell recognition. Genes: CNTN2, NRXN1, KIRREL1
  - [14]: Contactins and neurexins mediate cell-cell interactions through immunoglobulin domains
- Bidirectional ephrin-EphB signaling. Genes: EPHB2, EFNB2, PLXNA2
  - [31]: EphB receptors and ephrin B ligands engage in bidirectional signaling at cell-cell contacts
  - [32]: Ephrin-EphB signaling controls cell migration, morphology, and adhesion

**Atomic cellular components**
- Adherens junction complex. Genes: CTNNA2, CNTN2, EFNB2
  - [14]: Alpha-catenin links cadherins to the actin cytoskeleton, providing mechanical strength to junctions
- Synaptic adhesion complex. Genes: NRXN1, CNTN2, KIRREL1, EPHB2
  - [14]: Neurexins, contactins, and eph receptors form heterophilic adhesion complexes at synapses

**Required genes (not in input)**
- Genes: CDH1, CDH2, NLGN1, NLGN2, NLGN3
  - [14]: Classical cadherins and neuroligins form core adhesion complexes required for neural tissue organization

**Program citations**
- [31]: EphB receptors and ephrin B ligands mediate cell-cell interactions critical for neural development
- [14]: Cell adhesion molecules organize neural tissue architecture and mediate cell-cell communication

## Program: Transcription Factor-Driven Cellular Plasticity Network
Astrocytomas maintain a sophisticated network of transcription factors governing cellular identity and enabling transitions between distinct cellular states. This program encompasses transcription factors that promote neural progenitor identity (SOX11, SOX4, EBF1, EBF3), neuronal differentiation (MYT1L, FOXP2), epithelial-mesenchymal transition and migratory phenotypes (ZEB1), and developmental patterning (LHX1, PBX1). The coexpression of transcription factors promoting distinct or even opposing cellular fates creates a heterogeneous transcriptional landscape where individual cells or subpopulations can adopt various phenotypic identities. This transcriptional plasticity is fundamental to tumor heterogeneity and therapeutic resistance.

**Predicted impacts**
- Coexistence of distinct transcriptional states within single tumor enabling cellular heterogeneity
- Dynamic transitions between progenitor and differentiated phenotypes without genomic alteration
- Activation of EMT programs promoting invasion while maintaining progenitor core identity
- Resistance to lineage-specific therapies through rapid state switching
- Tumor cell plasticity and adaptation to microenvironmental changes

**Evidence summary**
SOX11 and SOX4 are SoxC family transcription factors regulating neural differentiation. EBF1 and EBF3 are early B-cell factor family transcription factors governing neuronal identity. MYT1L (myelin transcription factor 1-like) is essential for neuronal identity establishment and is sufficient for direct neuronal reprogramming. FOXP2 (forkhead box P2) regulates neural development and synaptogenesis. ZEB1 (zinc finger E-box binding homeobox 1) drives EMT programs and cellular plasticity. LHX1 and PBX1 encode developmental transcription factors specifying neural identities. The constellation of these transcription factors with divergent biological roles indicates that astrocytomas maintain transcriptional landscapes supporting rapid phenotypic switching and cellular heterogeneity.

**Atomic biological processes**
- Neural progenitor cell fate specification. Genes: SOX11, SOX4, EBF1, EBF3, INSM1
  - [5]: SoxC and EBF transcription factors regulate neural progenitor maintenance and differentiation
  - [8]: INSM1 drives progenitor fate in developing brain and in glioblastoma
- Neuronal differentiation and synaptogenesis. Genes: MYT1L, FOXP2, ELAVL4, RBFOX3
  - [21]: FOXP2 regulates synaptic development and neural circuit formation
- Epithelial-mesenchymal transition and migration. Genes: ZEB1, ZNF536, KLF7
  - [33]: ZEB1 drives epithelial-mesenchymal transition and cell lineage plasticity, enabling cellular reprogramming
- Developmental patterning and neural axis formation. Genes: LHX1, PBX1, ONECUT2
  - [14]: LIM-homeodomain transcription factors specify neural cell identities and patterning

**Atomic cellular components**
- Progenitor-specifying transcriptional complex. Genes: SOX11, SOX4, EBF1, EBF3, CDK6
  - [8]: SOX and EBF factors cooperate in transcriptional regulation of progenitor genes
- EMT-inducing transcriptional complex. Genes: ZEB1, SNAIL, TWIST
  - [33]: ZEB1 and related EMT factors form transcriptional repressor complexes silencing epithelial genes

**Required genes (not in input)**
- Genes: SNAIL1, TWIST1, PRRX1, CDH1, RHOA
  - [33]: Core EMT factors cooperate with ZEB1 in driving epithelial-mesenchymal transition

**Program citations**
- [33]: Epigenetic reprogramming and transcriptional control enable cellular lineage plasticity driving therapy resistance
- [8]: Transcriptional networks governing intermediate progenitor identity are dysregulated in glioblastoma

## Program: Long Non-Coding RNA Regulatory Network
Astrocytomas maintain expression of multiple long non-coding RNAs (lncRNAs) that function in chromatin regulation, splicing control, and transcriptional fine-tuning. These lncRNAs include RMST (rhabdomyosarcoma 2 associated transcript), MIAT (myocardial infarction associated transcript), CASC15 (cancer susceptibility candidate 15), MIR137HG (miR-137 host gene), and numerous LINC transcripts (long intergenic non-coding RNAs). lncRNAs regulate gene expression through multiple mechanisms including recruitment of chromatin modifying complexes, interactions with transcription factors, and regulation of RNA processing. The presence of multiple developmentally important lncRNAs suggests that astrocytomas maintain multilayered regulatory networks controlling cell identity and plasticity.

**Predicted impacts**
- Dynamic control of chromatin accessibility enabling rapid transcriptional switching
- Regulation of neuronal alternative splicing programs through lncRNA-splicing factor interactions
- Fine-tuning of developmental gene expression through miRNA host gene regulation
- Enhanced cellular plasticity through multilayered lncRNA-mediated regulatory networks
- Epigenetic memory of cellular state transitions through lncRNA-dependent chromatin modifications

**Evidence summary**
RMST is upregulated during neural differentiation and regulates chromatin accessibility. MIAT (myocardial infarction associated transcript) has been implicated in alternative splicing regulation and neural development. CASC15 (cancer susceptibility candidate 15) overlaps with the primary transcript for miR-15c and miR-16-2 and is dysregulated in gliomas. MIR137HG is the host gene for miR-137, a microRNA implicated in neurogenesis and tumor suppression. Multiple LINC RNAs (LINC01102, LINC01122, LINC01619, LINC01748, LINC02487, LINC02488, etc.) are present in the gene list, indicating widespread expression of intergenic lncRNAs. Recent research demonstrates that lncRNAs overlapping ultraconserved regions are differentially expressed in glioblastoma and correlate with patient survival.

**Atomic biological processes**
- Chromatin remodeling and epigenetic control. Genes: RMST, MIAT, CASC15
  - [14]: lncRNAs regulate chromatin accessibility and histone modifications controlling gene expression
- Alternative splicing regulation through lncRNA interactions. Genes: RMST, MIAT, SRRM4
  - [34]: lncRNAs interact with splicing factors to modulate alternative splicing patterns
- miRNA biogenesis and regulation. Genes: MIR137HG, MIR99AHG
  - [14]: Host genes for miRNAs contain regulatory sequences controlling miRNA expression

**Atomic cellular components**
- lncRNA-chromatin complex. Genes: RMST, MIAT, CASC15
  - [14]: lncRNAs recruit chromatin remodeling complexes to specific genomic loci

**Required genes (not in input)**
- Genes: PRC2, DNMT1, HDAC1, HDAC2
  - [14]: Polycomb complex and histone deacetylases interact with lncRNAs for chromatin remodeling

**Program citations**
- [14]: ncUCR genes including lncRNAs are predominantly expressed in brain tissues and dysregulated in gliomas

## Program: Rho GTPase Signaling and Cytoskeletal Dynamics
Astrocytomas maintain sophisticated signaling networks downstream of Rho family GTPases that regulate cytoskeletal organization, cell morphology, and migration. PAK (p21-activated kinase) proteins including PAK3 and PAK5, alongside RND3 (RhoE), function as key effectors of Rho GTPase signaling. These proteins regulate actin dynamics, focal adhesion assembly, and cell-cell junctions. The presence of GTPase regulatory proteins (FGD4, RAPGEF5) indicates active GTPase signaling. Rho GTPase signaling is particularly important in enabling the morphological plasticity that allows astrocytoma cells to transition between migratory and stationary phenotypes.

**Predicted impacts**
- Dynamic cytoskeletal reorganization enabling cell morphology changes between migratory and stationary states
- Enhanced focal adhesion turnover facilitating cell migration and invasion
- Regulation of cell-cell junctions enabling transitions between epithelial-like and mesenchymal-like phenotypes
- Morphological plasticity supporting tumor cell adaptation to microenvironmental constraints
- Integration of guidance signals (SLIT, NETRIN, semaphorins) into cytoskeletal responses

**Evidence summary**
PAK3 and PAK5 are members of the p21-activated kinase family that function as downstream effectors of Rho family GTPases. RND3 (also known as RhoE) is a GTPase that regulates Rho-dependent actin dynamics and is involved in astrocyte-to-neuron reprogramming. FGD4 encodes a Rac-specific guanine nucleotide exchange factor (GEF). RAPGEF5 encodes a Rap GEF regulating integrin signaling. The presence of multiple Rho GTPase pathway components indicates active signaling supporting cytoskeletal plasticity and cellular migration.

**Atomic biological processes**
- Actin cytoskeleton reorganization and cell morphology. Genes: PAK3, PAK5, RND3, FGD4
  - [3]: RND3 regulates actin cytoskeleton during astrocyte-to-neuron conversion and morphological changes
- Focal adhesion assembly and turnover. Genes: PAK3, PAK5, RAPGEF5
  - [14]: PAK-mediated phosphorylation regulates focal adhesion dynamics and cell migration
- Cell-cell junction dynamics. Genes: RND3, PAK3, CTNNA2
  - [3]: RND3 signaling modulates cell-cell adhesion during developmental transitions

**Atomic cellular components**
- PAK kinase signaling complex. Genes: PAK3, PAK5, FGD4
  - [10]: PAK proteins interact with GTPases and scaffold proteins regulating downstream signaling
- Focal adhesion maturation machinery. Genes: PAK3, PAK5, RAPGEF5, CTNNA2
  - [14]: Focal adhesions contain integrin-binding proteins and actin regulators

**Required genes (not in input)**
- Genes: RAC1, CDC42, RHOA, LIMK1, COFILIN
  - [3]: Rho family GTPases and their direct effectors are upstream of PAK and RND3 signaling

**Program citations**
- [3]: RND3 mediates cytoskeletal changes during astrocyte-to-neuron conversion through Rho pathway modulation
- [10]: PAK proteins regulate actin dynamics and cell morphology through GTPase-dependent signaling

## Bibliography
1. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
2. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
3. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
4. Available from: https://www.ncbi.nlm.nih.gov/gene/20677
5. Available from: https://www.ncbi.nlm.nih.gov/gene/20666
6. Zhang Z, Wang C, Sun Z, Shi X, Shuai Y, Wang Y, et al.. CAV2-expressing nerves induce metabolic switch toward mitochondrial oxidative phosphorylation to promote cancer stemness. Nature Communications [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41467-025-66914-2
7. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
8. Tao L, Teng L, Ge M, Wang Y, Hu C, Chen J, et al.. Slc22a17 governs postnatal neurogenesis by maintaining the iron homeostasis in hippocampus. Nature Communications [Internet]. 2025Dec15;16(1). Available from: https://www.nature.com/articles/s41467-025-66108-w
9. Available from: https://www.ncbi.nlm.nih.gov/gene/10298
10. Darko-Boateng A, Afriyie E, Morgenstern TJ, Shanmugam SK, Zou X, Laloudakis YD, et al.. Ion channel inhibition by targeted recruitment of NEDD4-2 with divalent nanobodies. Nature Communications [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41467-025-67068-x
11. Available from: https://www.ncbi.nlm.nih.gov/gene/23327
12. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
13. Bai Y, Zhang X, Wang X, Wang M, Shen T. Characterizing and decoding ultraconserved regions uncovers their regulatory significance in human brain development and disorders. Communications Biology [Internet]. 2025Nov27;8(1). Available from: https://www.nature.com/articles/s42003-025-09115-3
14. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
15. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
16. Available from: https://www.ncbi.nlm.nih.gov/gene/8829
17. Available from: https://www.ncbi.nlm.nih.gov/gene/18186
18. Available from: https://www.ncbi.nlm.nih.gov/gene/93986
19. Available from: https://www.ncbi.nlm.nih.gov/gene/114142
20. Available from: https://www.ncbi.nlm.nih.gov/gene/12571
21. Available from: https://www.ncbi.nlm.nih.gov/gene/5071
22. Ma L, Huang Y, Han M, Wang B, Guo X, Wang Z, et al.. ZFP612 controls neuropathic pain through epigenetic repression of Il1rl1 within the silencer–promoter loop in primary sensory neurons of male mice. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-65935-1
23. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
24. Available from: https://www.ncbi.nlm.nih.gov/gene/146713
25. Available from: https://www.ncbi.nlm.nih.gov/gene/2893
26. Available from: https://www.ncbi.nlm.nih.gov/gene/2048
27. Available from: https://www.ncbi.nlm.nih.gov/gene/1948
28. Veo B, Wang D, DeSisto J, Pierce A, Brunt B, Bompada PC, et al.. Single-cell multi-omics identifies metabolism-linked epigenetic reprogramming as a driver of therapy-resistant medulloblastoma. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65466-9
29. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
30. Liu Z, Lim S-H, Jung S. Targeting tumor metabolic flexibility enhances radiotherapeutic efficacy via mitochondrial complex I Inhibition in an intracranial S180 sarcoma mouse model. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-29326-2
31. Available from: https://www.ncbi.nlm.nih.gov/gene/10419
32. Available from: http://json-schema.org/draft-07/schema#",
