# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: glioblastoma multiforme (GBM)
- Tissue: brain

## Input Genes
FSTL4, LRFN5, TRPM3, NDST4, PALMD, ADRA1B, PDE1A, CLVS1, SLC17A6, ACVR1C, SLA, EBF1, AC011474.1, FRMPD4, KIT, UNC5D, GCG, TRPC5, CDH9, TARID, LINC01033, AC109492.1, AL596087.2, SHISA6, POSTN, ... (136 total)

## Program: Extracellular Matrix Remodeling
This program comprises genes encoding secreted proteins and proteases that modify the glioblastoma microenvironment. The program includes collagen deposition, proteoglycan synthesis, and matrix metalloproteinase regulation. In GBM, dysregulation of this program promotes invasive phenotype, particularly in hypoxic and bevacizumab-resistant tumors. Collagen VI (COL6A3) and collagen III (COL3A1) accumulation stiffens the tumor microenvironment, enhancing β-catenin signaling and mesenchymal marker expression. Periostin (POSTN) expression correlates with glioma grade and poor prognosis. Heparan sulfate proteoglycans (NDST4/HS3ST2) regulate growth factor binding and cell migration. Fibulin-like proteins (FSTL4, FSTL5) promote matrix scaffold formation. Matrix metalloproteinase regulation through FAP and ADAMTS3 enables invasion through brain tissue.

**Predicted impacts**
- Increased tumor stiffness promoting mechanotransduction and β-catenin signaling
- Enhanced migration and invasion through brain tissue via matrix degradation
- Reduced response to anti-angiogenic therapy through altered matrix composition
- Support for tumor-associated immune cell infiltration and M2 macrophage recruitment
- Maintenance of hypoxic microenvironment through altered matrix density

**Evidence summary**
Twelve genes in the input list encode ECM components or regulators directly implicated in GBM progression. COL6A3 is specifically upregulated in bevacizumab-resistant GBM and correlates with mesenchymal transition markers. POSTN expression increases with glioma grade and correlates with poor survival. NDST1/NDST4 regulate heparan sulfate-mediated growth factor signaling. FAP expression in cancer-associated fibroblasts drives ECM remodeling and enhances tumor growth. The convergence of collagen deposition, proteoglycan synthesis, and protease activity creates a pro-invasive microenvironment characteristic of high-grade glioma.

**Atomic biological processes**
- Collagen synthesis and cross-linking. Genes: COL3A1, COL6A3, TGFBI
  - [32]: COL6A3 deletion reduces invasion and β-catenin signaling; COL6A3 upregulated in bevacizumab-resistant GBM cells
  - [35]: Collagen upregulation in GBM associated with basement membrane modifications
- Proteoglycan and glycosaminoglycan synthesis. Genes: NDST4, HS3ST2, POSTN
  - [2]: NDST1 (N-deacetylase/N-sulfotransferase) modulates heparan sulfate patterns regulating growth factor availability and cell migration
- Matrisome protein secretion. Genes: FSTL4, FSTL5, SMOC2, PAPPA2
  - [13]: Fibulin-3 and other ECM proteins promote Notch and NF-κB signaling, enhancing invasion and vascularization
- Matrix metalloproteinase and ADAMTS-mediated remodeling. Genes: FAP, ADAMTS3, SERPINI1
  - [51]: FAP (fibroblast activation protein) has dipeptidyl peptidase and endopeptidase activities that remodel ECM

**Atomic cellular components**
- Collagen fibrils. Genes: COL3A1, COL6A3
  - [32]: COL6A3-rich regions detected in tumor matrix promote invasive phenotype
- Proteoglycan core proteins. Genes: NDST4, POSTN
  - [2]: NDST1 modulates heparan sulfate on proteoglycans affecting FGF and other growth factor signaling

**Required genes (not in input)**
- Genes: MMP2, MMP9, MMP14, ADAMTS1, ADAMTS6, ADAMTS8, ADAMTS9, ADAMTS12, ADAMTS13, ADAMTS14, ADAMTS15, ADAMTS16, ADAMTS17, ADAMTS18, ADAMTS19, ADAMTS20, TIMP1, TIMP2, TIMP3, TIMP4, HYALURONAN_SYNTHASES, VCAN, ACAN, PERLECAN, NIDOGEN1, NIDOGEN2
  - [13]: Matrix metalloproteinases and their inhibitors are critical regulators of ECM degradation in GBM
  - [16]: TIMP proteins regulate MMP activity; hyaluronic acid and proteoglycan core proteins are essential ECM components

**Program citations**
- [13]: Comprehensive ECM characterization in GBM showing Fibulin-3, HA, TN-C, SPARCL1 promote invasion and vascularization
- [16]: Systematic review of ECM modifications in GBM demonstrating ECM as active player in tumor progression
- [32]: GBM cells secrete COL6A3 to facilitate invasion with amplified effects in hypoxia
- [51]: FAP involved in ECM remodeling through both enzymatic and non-enzymatic mechanisms promoting cancer cell migration
- [54]: FAP overexpression activates PI3K and sonic hedgehog pathways affecting cell proliferation and migration

## Program: Cadherin-Mediated Cell Adhesion
This program encompasses classical cadherins and associated adherens junction proteins that mediate homophilic and heterophilic cell-cell adhesion. In GBM, cadherin expression undergoes dynamic changes that facilitate epithelial-to-mesenchymal transition (EMT). E-cadherin (CDH1, not in input) is downregulated in high-grade gliomas through promoter methylation, particularly in microvascular proliferation regions. N-cadherin (not in input) undergoes proteolytic cleavage by ADAM10 at significantly higher rates in GBM than normal brain, with cleavage facilitating migration. The program includes multiple classical cadherins (CDH4, CDH9, CDH13, CDH18) with distinct adhesion patterns and downstream signaling. NEDD4L ubiquitinates Dishevelled proteins to negatively regulate Wnt/β-catenin signaling, a pathway that promotes GBM proliferation and stemness. Cadherin switching and shedding are hallmarks of GBM invasive phenotype.

**Predicted impacts**
- Loss of epithelial adhesion properties and gain of mesenchymal phenotype
- Enhanced cell motility through cadherin shedding and membrane redistribution
- Increased Wnt/β-catenin signaling promoting proliferation and stemness maintenance
- Altered actin cytoskeleton dynamics facilitating 3D invasion
- Heterotypic adhesion with stromal cells promoting local invasion

**Evidence summary**
Five classical cadherins from the input list regulate GBM cell adhesion and EMT. N-cadherin expression increases with glioma grade and correlates with Ki-67 labeling and poor survival. Proteolytic cleavage of N-cadherin by ADAM-10 occurs at high rates in GBM and is prerequisite for cell migration. E-cadherin shows decreased expression in high-grade gliomas (23% of grade IV vs 43% of grade II), with decreased CDH1 promoter methylation correlating with poor progression-free survival. NEDD4L acts as a negative regulator of Wnt signaling by ubiquitinating Dvl2; loss or reduced NEDD4L activity would enhance β-catenin signaling promoting proliferation. GREM2 as a BMP antagonist can modulate Wnt signaling through non-canonical BMP pathways affecting cell fate decisions.

**Atomic biological processes**
- Homophilic cadherin adhesion and sorting. Genes: CDH4, CDH9, CDH13, CDH18
  - [9]: Cadherins mediate cell sorting through homophilic connections; cadherin switch is hallmark of EMT in cancer
- N-cadherin proteolytic cleavage and redistribution. Genes: CDH4, CDH13
  - [9]: N-cadherin cleavage by ADAM-10 at higher rates in GBM than normal brain; cleavage prerequisite for migration
- Wnt/β-catenin signaling regulation. Genes: NEDD4L, GREM2
  - [44]: NEDD4L induces Dvl2 polyubiquitination targeting it for proteasomal degradation, regulating both Wnt/β-catenin and Wnt/PCP signaling
  - [47]: NEDD4-2 ubiquitinates Dvl2; sustained Wnt/β-catenin signaling contributes to renal fibrosis; likely analogous in GBM

**Atomic cellular components**
- Adherens junctions. Genes: CDH4, CDH9, CDH13, CDH18
  - [9]: Cadherins assemble into strong adhesive intercellular junctions with subtype specificities
- Cadherin-catenin-actin cytoskeleton complex. Genes: CDH4, CDH9, CDH13, CDH18, NEDD4L
  - [9]: Interplay between E-cadherin complexes and actin cytoskeleton enables resistance to cell deformation or triggers cellular remodeling

**Required genes (not in input)**
- Genes: CDH1, CDH2, CTNNB1, CTNND1, APC, GSK3B, AXIN1, LEF1, TCF4, ADAM10, FURIN, BACE1, PSEN1, PSEN2
  - [9]: CDH1, CDH2, and associated catenin proteins are essential components of adherens junctions; APC and GSK3B regulate β-catenin degradation
  - [20]: CTNNB1 (β-catenin) is central to Wnt signaling downstream of cadherin complexes

**Program citations**
- [9]: Comprehensive review of cadherin expression and EMT in gliomas with focus on N-cadherin and E-cadherin dynamics
- [20]: N-cadherin-FGFR1 complexes decrease FGFR1 internalization sustaining FGF2-induced proliferation
- [32]: COL6A3 promotes β-catenin signaling; CDH13 deletion reduces invasion

## Program: Calcium Signaling Through Ion Channels
This program comprises genes encoding ion channels and calcium-dependent signaling molecules that regulate intracellular calcium concentrations and downstream effectors. Transient Receptor Potential (TRP) channels including TRPM3, TRPM7, TRPM8, and TRPC5 are dysregulated in glioma cells and drive proliferation, migration, and invasion. TRPC1 channels are essential for chemotactic migration in response to EGF and PDGF through lipid raft-dependent mechanisms. TRPC6 is upregulated in hypoxic GBM cells via Notch signaling and promotes proliferation through calcineurin-NFAT pathway activation. TRPM7 suppression significantly inhibits GBM cell growth and invasion through miR-28-5p-mediated pathways and JAK2/STAT3 signaling. TRPM8 expression correlates with GBM aggressiveness and poor survival. Voltage-gated potassium channels (KCNJ6, KCNC2) maintain resting membrane potential. Anoctamins (ANO4) are calcium-activated chloride channels affecting calcium compartmentalization. Phosphodiesterases (PDE1A, PDE1C) regulate store-operated calcium entry (SOCE) and cAMP signaling affecting cell motility. GABBR2 (GABA B receptor) modulates inhibitory neurotransmitter signaling affecting network-level GBM behavior.

**Predicted impacts**
- Increased intracellular calcium promoting proliferation through calcineurin-NFAT pathway
- Enhanced migratory capacity through TRPC-mediated lipid raft signaling
- Altered response to growth factors (EGF, PDGF) through TRP-mediated chemotaxis
- Maintained hypoxic phenotype through TRPC6-Notch signaling in low-oxygen regions
- Dysregulated cAMP-dependent motility through PDE1C-SOCE coupling
- Modified inhibitory neurotransmitter signaling affecting network-level tumor behavior
- Survival advantage through reduced apoptosis via calcium-dependent survival pathways

**Evidence summary**
Nine genes encoding ion channels and calcium regulators are present in the input list. TRPM3 expression is upregulated in glioma and associated with poor prognosis. TRPM7 suppression significantly inhibits GBM proliferation, migration, and invasion. TRPM8 high expression correlates with shorter overall survival in GBM patients. TRPC5 (TRPC family) promotes migration through EGF/PDGF-mediated activation and lipid raft integrity. PDE1A and PDE1C regulate store-operated calcium entry affecting cell motility and cAMP signaling. KCNJ6 and KCNC2 maintain membrane potential necessary for migration. ANO4 suppresses proliferation in high-calcium conditions. GABBR2 mediates inhibitory signaling affecting network-level tumor behavior. The convergence of multiple calcium-permeable channels creates a cellular environment permissive for GBM growth and invasion.

**Atomic biological processes**
- TRP channel-mediated calcium influx. Genes: TRPM3, TRPC5, TRPM7, TRPM8
  - [4]: TRPM3 upregulated in glioma; TRPM7 suppression inhibits GBM cell growth, proliferation, migration, invasion
  - [52]: TRPC1, TRPC3, TRPC6, TRPV1, TRPV2, TRPM2, TRPM7, TRPM8 implicated in glioma growth and migration
  - [49]: TRP channels non-selective Ca2+-permeable channels regulating glioma proliferation, migration, invasion
- Lipid raft and chemotactic migration. Genes: TRPC5
  - [52]: TRPC1 channel activity and lipid raft integrity required for glioma chemotaxis in response to EGF and PDGF
- Hypoxia-induced calcium signaling. Genes: TRPC5
  - [52]: TRPC6 induced via Notch1 in hypoxic GBM cells; promotes proliferation through calcineurin-NFAT pathway
- Store-operated calcium entry and cAMP regulation. Genes: PDE1A, PDE1C
  - [21]: PDE1C regulates SOCE-dependent cAMP changes and leading-edge protrusions; critical for cell migration
- Potassium channel-mediated membrane potential. Genes: KCNJ6, KCNC2
  - [52]: TRPM8 activation stimulates large-conductance K+ channel activity affecting glioblastoma cell migration
- Calcium-activated chloride channel regulation. Genes: ANO4
  - [42]: ANO1 and ANO4 regulate compartmentalized calcium signals in opposite directions; ANO4 lowers ER Ca2+ stores
  - [39]: ANO4 suppresses cell proliferation in conditions of increased intracellular calcium
- GABA B receptor signaling. Genes: GABBR2
  - [55]: GABBR2 variants cause constitutive activity affecting neuronal inhibition; positive allosteric modulators normalize network activity

**Atomic cellular components**
- Transient Receptor Potential channels. Genes: TRPM3, TRPC5, TRPM7, TRPM8
  - [49]: TRP channels are Ca2+-permeable cation channels (except TRPM4/5) implicated in glioma cell biology
- Voltage-gated potassium channels. Genes: KCNJ6, KCNC2
  - [38]: Voltage-gated potassium channels KCNA1, KCND2, KCNS1 regulate neuronal excitability
- Lipid rafts. Genes: TRPC5
  - [52]: Lipid raft integrity required for TRPC1-mediated glioma chemotaxis
- Endoplasmic reticulum calcium stores. Genes: PDE1A, PDE1C, ANO4
  - [21]: ER Ca2+ store depletion activates PDE1C affecting SOCE

**Required genes (not in input)**
- Genes: TRPC1, TRPC3, TRPC4, TRPC6, TRPC7, TRPV1, TRPV2, TRPV4, TRPA1, TRPM2, TRPM4, TRPM5, TRPM6, TRPML1, STIM1, ORAI1, CACNA1D, CACNB4, CAMK2, CALCINEURIN, PKA, PKC
  - [4]: TRPC1, TRPC3, TRPC6 regulate glioma growth and migration; TRPV1, TRPV2 affect survival
  - [52]: STIM1 and ORAI1 mediate store-operated calcium entry essential for TRP channel function

**Program citations**
- [4]: TRPM channels in glioma show dysregulated expression correlating with proliferation, migration, invasion
- [21]: PDE1C regulation of SOCE critical for leading-edge protrusions and cell migration
- [42]: Anoctamins in glioblastoma regulate calcium signaling affecting EGFR targeting and growth
- [49]: Comprehensive review of TRP channels in glioma showing Ca2+-dependent regulation of proliferation
- [52]: TRP channels in brain tumors - TRPM2, TRPM3, TRPM7, TRPM8 regulate multiple aspects of tumorigenesis

## Program: Synaptic Development and Adhesion
This program comprises genes encoding synaptic adhesion molecules, calcium sensors for neurotransmitter release, and axon guidance cues. The program includes contactin-associated protein-like molecules (CNTNAP4, CNTNAP5), contactins (CNTN5), teneurins (TENM2), synaptotagmins (SYT1), and semaphorins (SEMA3C). TENM2 forms nanoclusters at presynaptic active zones and is essential for synaptic connectivity, particularly in hippocampal projections. SYT1 serves as the primary calcium sensor for fast neurotransmitter release and is involved in vesicle recycling. Contactins mediate cell-cell adhesion at synaptic cleft. CNTNAP4 regulates synaptic development and maturation. Semaphorins (SEMA3C) act as axon guidance cues affecting neurite outgrowth and axonal pathfinding. In GBM context, this program may be dysregulated to suppress pro-differentiation signaling or alternatively utilized to support GBM cell-cell interactions and network formation.

**Predicted impacts**
- Altered synaptic connectivity potentially suppressing pro-differentiation signals
- Enhanced cell-cell adhesion through synaptic adhesion molecules
- Modified calcium signaling through synaptotagmin-mediated mechanisms
- Potential maintenance of progenitor-like state through altered axon guidance signals
- Support for neural-like network formation within GBM tumors

**Evidence summary**
Eight genes encoding synaptic development and adhesion proteins are present in the input list. TENM2 is essential for presynaptic connectivity in hippocampal circuits. SYT1 serves as primary calcium sensor for neurotransmitter release. CNTNAP4 and CNTN5 mediate synaptic adhesion. SEMA3C acts as axon guidance molecule promoting attractive and repulsive effects depending on receptor. UNC5C and UNC5D mediate netrin signaling affecting migration and apoptosis. SHISA6 interacts with synaptic proteins. In GBM, dysregulation of this program may suppress pro-differentiation signals that would constrain proliferation, or alternatively, GBM cells may utilize these adhesion molecules for tumor cell-cell interactions.

**Atomic biological processes**
- Presynaptic active zone assembly. Genes: TENM2, SYT1
  - [33]: Tenm3 protein localized to synaptic cleft forming nanoclusters in presynaptic active zones; presynaptic Tenm3 essential for synaptic connectivity
  - [6]: Active zone proteins RIM and ELKS2 organize presynaptic release sites; Synaptotagmin-1 is fast Ca2+ sensor
- Calcium-dependent vesicle fusion and neurotransmitter release. Genes: SYT1
  - [17]: SNARE/Syt1-mediated synaptic vesicle fusion with plasma membrane essential for neurotransmitter release
  - [14]: Synaptotagmin I binds Ca2+ in vitro and serves as Ca2+ sensor for nerve-evoked synaptic transmission
- Synaptic adhesion and connectivity. Genes: TENM2, CNTNAP4, CNTN5
  - [33]: Teneurins function as homophilic adhesion molecules; presynaptic Tenm3/4 deletion causes >50% decrease in synapse density
- Axon guidance and growth cone steering. Genes: SEMA3C, UNC5D, UNC5C
  - [30]: Sema3C and netrin-1 differentially affect axon growth in hippocampus; Sema3C involved in control of septohippocampal projection
  - [27]: Semaphorins act as repulsive or growth-promoting factors; temporal regulation of semaphorin/receptor expression determines function
- Netrin signaling in neuronal migration. Genes: UNC5D, UNC5C
  - [50]: Netrin-1 important attractant and repellant for axon guidance; UNC5D/FLRT signaling regulates radial migration

**Atomic cellular components**
- Presynaptic nanoclusters. Genes: TENM2, SYT1
  - [33]: Tenm3 forms intrinsic nanoclusters at nearly all synaptic junctions in CA1 and subiculum
- Synaptic cleft adhesion complex. Genes: TENM2, CNTNAP4, CNTN5
  - [33]: Teneurins localize to synaptic cleft; presynaptic projections contain Tenm3
- Synaptic vesicle exocytotic machinery. Genes: SYT1
  - [6]: SYT1 is component of synaptic vesicle proteins involved in exocytosis
- Growth cone. Genes: TENM2, SEMA3C
  - [36]: Lasso/TENM2 binds to latrophilin-1 on axonal growth cones inducing axonal attraction

**Required genes (not in input)**
- Genes: TENM1, TENM3, TENM4, NLGN1, NLGN2, NLGN3, NLGN4, NRXN1, NRXN2, NRXN3, LRRTM1, LRRTM2, LRRTM3, LRRTM4, NETRIN1, DCC, ROBO1, ROBO2, FLRT1, FLRT2, FLRT3, LATROPHILIN1, LATROPHILIN2, LATROPHILIN3
  - [33]: Other teneurin family members (TENM1, TENM3, TENM4) and neurexins are essential synaptic adhesion molecules
  - [36]: Latrophilin-1 is required presynaptic receptor for Lasso/TENM2-mediated axonal attraction

**Program citations**
- [33]: Comprehensive characterization of Tenm3 in presynaptic active zones and synaptic connectivity
- [36]: Proteolytically released Lasso/TENM2 induces axonal attraction through latrophilin-1 signaling
- [30]: Sema3C and netrin-1 differentially affect axon growth in hippocampal system
- [50]: Netrin-4 and Unc5 receptors regulate radial neuronal migration

## Program: Receptor Tyrosine Kinase Signaling
This program comprises genes encoding receptor tyrosine kinases (RTKs) and their signaling intermediates that drive proliferation, survival, angiogenesis, and migration in GBM. The program includes FGFR2 (fibroblast growth factor receptor), KIT (c-KIT/stem cell factor receptor), and GFRA1 (GDNF co-receptor). RTKs activate downstream MAPK/ERK and PI3K/Akt/mTOR pathways controlling cell cycle progression and survival. FGFR2 mutations and amplifications are detected in GBM; FGFR signaling promotes both proliferation and mesenchymal differentiation. KIT is normally expressed during CNS development in endothelial and mast cell progenitors; KIT overexpression in GBM promotes angiogenesis and contributes to tumor growth. GFRA1 is the co-receptor for GDNF (glial cell line-derived neurotrophic factor), which promotes neuron survival and differentiation; deletion of GFRA1 and nearby genes may contribute to GBM pathogenesis. RTK signaling is also modulated by N-cadherin complexes (CDH2 not in input) that decrease FGFR1 internalization sustaining proliferation.

**Predicted impacts**
- Enhanced proliferation through sustained MAPK/ERK pathway activation
- Improved survival through PI3K/Akt anti-apoptotic signaling
- Increased angiogenesis through KIT-mediated endothelial cell recruitment
- Maintenance of stemness and self-renewal capacity
- Resistance to differentiation signals through continued growth factor signaling

**Evidence summary**
Three RTKs and associated signaling genes are present in the input list. FGFR2 is frequently mutated and amplified in various cancers including GBM; FGFR signaling drives proliferation and survival. KIT is amplified (32%) and mutated (4%) in some GBM subtypes with significantly elevated mRNA and protein expression; c-KIT promotes angiogenesis and tumor growth. GFRA1 deletion analysis in brain tumors suggests loss of GFRα-1 and nearby genes may contribute to GBM pathogenesis. Heparan sulfate proteoglycans (HS3ST2, NDST4) regulate ligand availability and receptor signaling. The convergence of multiple activated RTK signaling cascades creates a proliferative and pro-survival environment characteristic of GBM.

**Atomic biological processes**
- FGFR ligand binding and receptor dimerization. Genes: FGFR2, HS3ST2, NDST4
  - [20]: HSPGs promote formation of 2:2:2 dimer between FGF, FGFR, and HSPGs; essential for sustained signaling
- RTK autophosphorylation and substrate recruitment. Genes: FGFR2, KIT, GFRA1
  - [20]: Phosphorylated tyrosine residues serve as docking sites for downstream signaling molecules like FRS2α
  - [46]: RTK dysregulation through mutations, amplifications, overexpression creates environments conducive to tumor development
- MAPK/ERK pathway activation. Genes: FGFR2, KIT
  - [46]: MAPK pathway activated downstream of RTKs plays central role in regulating proliferation and differentiation
  - [43]: RTKs activate Ras/MAPK and PI3K/Akt/mTOR pathways controlling glioma growth, survival, migration
- PI3K/Akt/mTOR pathway activation. Genes: FGFR2, KIT, GFRA1
  - [46]: PI3K/Akt pathway mobilized for cell survival, growth, metabolism
- RTK internalization and degradation. Genes: FGFR2
  - [20]: N-cadherin-FGFR1 complexes decrease FGFR1 internalization and lysosomal degradation sustaining receptor signaling

**Atomic cellular components**
- Receptor tyrosine kinase complexes. Genes: FGFR2, KIT, GFRA1
  - [43]: RTK heterocomplex formation allows cross-phosphorylation and signal integration
- Growth factor-receptor-heparan sulfate ternary complexes. Genes: FGFR2, HS3ST2, NDST4
  - [20]: HSPGs form 2:2:2 complexes with FGF and FGFR promoting signaling

**Required genes (not in input)**
- Genes: FGF1, FGF2, FGF4, FGF7, FGF8, FGF9, FGF10, FGF18, GDNF, PDGFA, PDGFB, PDGFRA, PDGFRB, IGF1, IGF1R, EGFR, ERBB2, ERBB3, ERBB4, SRC, GRB2, SOS1, HRAS, KRAS, NRAS, RAF1, MAP2K1, MAP2K2, MAPK1, MAPK3, PIK3CA, PIK3R1, AKT1, AKT2, AKT3, MTOR
  - [43]: FGF ligands, GDNF, and other growth factors are required ligands for RTK activation
  - [46]: MAPK and PI3K pathway components are essential downstream effectors of RTKs

**Program citations**
- [20]: Comprehensive review of FGF/FGFR signaling in health and disease including RTK interactions
- [23]: FGFR structure and small molecule inhibitor development; gatekeeper mutations cause kinase inhibitor resistance
- [43]: RTK signaling and targeting in GBM; molecular subtypes with distinct RTK alterations
- [46]: Therapeutic advances in targeting RTKs in cancer; EGFR, PDGFR, FGFR mutations and overexpression in GBM

## Program: Transcriptional Repression of Neural Differentiation
This program comprises transcription factors and RNA-binding proteins that regulate neuronal differentiation, splicing, and transcriptional networks. The program includes MYT1L (myelin transcription factor 1-like), EBF1/EBF2 (early B-cell factors), RBFOX1 (RNA-binding fox-1), CUX2 (cut-like homeobox 2), SRRM4 (serine/arginine repetitive matrix 4), POU6F2, and RUNX1T1. MYT1L directly represses YAP1 expression, reducing GBM cell proliferation and promoting neural differentiation; MYT1L expression inversely correlates with YAP1 expression in GBM. Reduced MYT1L expression associates with GBM progression and poor survival. EBF factors regulate cortical neuron development and are downregulated in GBM. RBFOX1 regulates both splicing and transcriptional networks important for neuronal development; RBFOX1 is implicated in autism and developmental delay with relevance to neural cell fate determination. CUX2 is expressed in cortical development and marks mature neuronal populations. SRRM4 promotes neuronal splicing programs. RUNX1T1 negatively influences transcription through HDAC recruitment. In GBM, suppression of this differentiation program maintains proliferative capacity and stemness.

**Predicted impacts**
- Suppression of neural differentiation through MYT1L inactivation
- Maintenance of proliferative capacity through YAP1-mediated signaling
- Altered splicing of synaptic and adhesion proteins favoring undifferentiated state
- Loss of early differentiation signals through reduced EBF activity
- Enhanced stemness and self-renewal through suppressed differentiation programs

**Evidence summary**
Seven transcription factors and RNA-binding proteins regulating neuronal differentiation are present in the input list. MYT1L expression is significantly lower in GBM compared to normal brain and correlates with improved survival; MYT1L suppresses proliferation and promotes differentiation through YAP1 repression. EBF1 and EBF2 regulate cortical development; their downregulation in GBM supports undifferentiated phenotype. RBFOX1 regulates both splicing and transcriptional networks implicated in autism and developmental delay; RBFOX1 promotes mRNA stability and translation of synaptic and developmental genes. CUX2 marks cortical neuronal populations. SRRM4 drives neuronal splicing programs. RUNX1T1 mediates transcriptional repression through HDAC recruitment. The convergence of suppressed differentiation signals maintains GBM proliferative capacity and stemness.

**Atomic biological processes**
- MYT1/MYT1L-mediated transcriptional repression of YAP1. Genes: MYT1L
  - [19]: MYT1 and MYT1L reduce proliferation and promote neural differentiation; both repress YAP1 expression
- Early B-cell factor-mediated neuronal development. Genes: EBF1, EBF2
  - [22]: EBF1 and EBF2 involved in dorsal telencephalon development and cortical neuron specification
- RBFOX1-mediated alternative splicing of neuronal genes. Genes: RBFOX1
  - [59]: RBFOX1 regulates alternative splicing of transcription factors, other splicing factors, and synaptic proteins
  - [56]: Cytoplasmic RBFOX1 regulates expression of synaptic and autism-related genes; increased mRNA stability and translation
- RBFOX1-regulated transcriptional networks. Genes: RBFOX1
  - [59]: Downstream alterations in gene expression define transcriptional network involved in neurodevelopmental pathways
- Cortical development transcription factor networks. Genes: CUX2
  - [22]: PAX6, TBR1, EMX2, CUX2, SOX11 sequentially expressed in neocortex; CUX2 downstream target of Notch
- SRRM4-mediated neuronal splicing programs. Genes: SRRM4
  - [22]: SRRM4 promotes neuron-specific splicing patterns during chemical conversion of astrocytes to neurons
- RUNX1T1-mediated transcriptional silencing. Genes: RUNX1T1
  - [45]: RUNX1T1 recruits HDACs and DNMT1 for transcriptional silencing and histone deacetylation

**Atomic cellular components**
- Nuclear transcription factor complexes. Genes: MYT1L, EBF1, EBF2, RBFOX1, CUX2, SRRM4, RUNX1T1
  - [59]: RBFOX1 acts as high-level regulatory factor in neuronal development cascade
- Histone deacetylase complexes. Genes: RUNX1T1
  - [45]: RUNX1T1 recruits HDACs mediating transcriptional repression
- RNA splicing complexes. Genes: RBFOX1, SRRM4
  - [59]: RBFOX1 and SRRM4 component of splicing regulatory networks

**Required genes (not in input)**
- Genes: YAP1, TAZ, NOTCH1, NOTCH2, NOTCH3, NOTCH4, JAG1, JAG2, DLL1, DLL3, DLL4, PAX6, TBR1, EMX1, EMX2, SOX11, NEUROG1, NEUROG2, NEUROD1, NEUROD4, HDAC1, HDAC2, HDAC3, DNMT1, NOVA1, NOVA2
  - [19]: YAP1 and TAZ promote proliferation and mesenchymal transition; repressed by MYT1/MYT1L
  - [59]: NOVA1 and other splicing factors work coordinatively with RBFOX1 on neuronal development

**Program citations**
- [19]: MYT1 and MYT1L correlate with survival; expression limits GBM proliferation
- [22]: Transcription factors in neural development; chemical reprogramming upregulates differentiation-promoting TFs
- [56]: RBFOX1 regulates synaptic and autism-related genes; implicated in neurodevelopmental disease
- [59]: RBFOX1 regulates genome-wide splicing network in neuronal development; high-level regulatory factor

## Program: Neuropeptide and Neurosecretion Pathways
This program comprises genes encoding secreted neuropeptides, hormones, and components of the secretory pathway that package and release bioactive peptides. The program includes SCG2 (secretogranin II), GCG (glucagon), CCK (cholecystokinin), and secretory pathway components including SLC38A11 (amino acid transporter for vesicle loading). SCG2 is a chromogranin/secretogranin family member processed into bioactive peptides EM66 and secretoneurin. SCG2 promotes neuronal differentiation and survival by counteracting nitric oxide-induced toxicity. SCG2 is regulated by REST (repressor element 1 silencing transcription factor) in neural progenitors with non-cell-autonomous differentiation-enhancing activity. SCG2-derived secretoneurin has angiogenic activity and modulates leukocyte transendothelial migration. In reduced SCG2 expression, tumor angiogenesis and aggressive behavior increase. GCG encodes proglucagon processed to GLP-1 and other peptides; GLP-1 neurons show emerging roles in metabolic and stress regulation. CCK encodes cholecystokinin processed to active peptides. In GBM, dysregulation of this program may alter neuroendocrine differentiation capacity and support tumor immune modulation.

**Predicted impacts**
- Enhanced neuronal differentiation through SCG2-mediated non-cell-autonomous signaling
- Increased angiogenesis through secretoneurin-mediated endothelial signaling
- Altered immune cell infiltration through leukocyte migration modulation
- Reduced tumor aggressiveness in conditions of high SCG2 expression
- Potential neuroendocrine differentiation capacity affecting GBM heterogeneity

**Evidence summary**
Four genes involved in neuropeptide synthesis and secretion are present in the input list. SCG2 (secretogranin II) is processed into bioactive peptides with roles in neuronal differentiation, angiogenesis, and immune modulation. Reduced SCG2 expression correlates with enhanced tumor angiogenesis and aggressive behavior in colorectal and bladder cancer; overexpression disrupts HIF-1α stability. SCG2 is regulated by REST in neural progenitors with demonstrated non-cell-autonomous enhancement of neuronal differentiation. GCG encodes glucagon and GLP-1; PPG neurons are distinct populations with specialized functions. CCK modulates presynaptic neurotransmitter signaling. SLC38A11 is a neutral amino acid transporter potentially involved in vesicular cargo loading. Dysregulation of this program in GBM may suppress pro-differentiation signals while supporting neuroendocrine characteristics of certain tumor cells.

**Atomic biological processes**
- Secretogranin II processing and peptide generation. Genes: SCG2
  - [37]: SCG2 is proteolytically processed into bioactive peptides EM66 and secretoneurin
  - [40]: REST regulates SCG2 as major secreted factor with non-cell-autonomous differentiation-enhancing activity
- Neuronal differentiation and survival. Genes: SCG2
  - [37]: SCG2 instrumental in supporting neuronal differentiation and survival by counteracting nitric oxide toxicity
  - [40]: SCG2 required for differentiation of adult hippocampal progenitors
- Angiogenic signaling. Genes: SCG2
  - [37]: SCG2-derived secretoneurin exerts potent angiogenic activity enhancing endothelial cell signaling
- Immune cell migration regulation. Genes: SCG2
  - [37]: Secretoneurin regulates leukocyte transendothelial migration through endothelial calcium signaling
- GLP-1 neuronal signaling. Genes: GCG
  - [25]: GCG-expressing PPG neurons produce GLP-1 and glutamate; GLP-1 release elicits physiological responses
- Cholecystokinin neuropeptide signaling. Genes: CCK
  - [25]: CCK modulates glutamatergic inputs and presynaptic signaling

**Atomic cellular components**
- Secretory vesicles and granules. Genes: SCG2, GCG, CCK
  - [37]: SCG2 involved in packaging and sorting of peptide hormones and neuropeptides into secretory vesicles
- Secretory pathway and vesicular transport. Genes: SCG2, SLC38A11
  - [40]: REST regulates SCG2 secretion affecting neural progenitor cell differentiation

**Required genes (not in input)**
- Genes: REST, CPE, PC1/PC3, PC2, PDIA2, CHGB, CHGA, VGF, PCSK1, PCSK2, SV2A, VAMP2, STX1, SNAP25, SYN1, SYN2, GLP1R, GIPR, GCGR, CCKAR, CCKBR
  - [40]: REST is master regulator of SCG2 in neural progenitors; endopeptidase PC1/PC3 processes proglucagon and other precursors
  - [37]: Receptors for secretoneurin and other peptides required for downstream effects

**Program citations**
- [37]: SCG2 multifunctional member of granin family with roles in neuronal differentiation, angiogenesis, and immune modulation
- [40]: REST regulates non-cell-autonomous neuronal differentiation via SCG2
- [25]: PPG neurons and GLP-1 signaling in brainstem and other brain regions

## Program: Cyclic Nucleotide Signaling and Cell Motility
This program comprises genes regulating cyclic nucleotide metabolism, calcium signaling coupling, and cell motility through cAMP/cGMP and calcium-dependent pathways. The program includes phosphodiesterases (PDE1A, PDE1C), adrenergic receptors (ADRA1B), and store-operated calcium entry (SOCE) components. PDE1A and PDE1C are calcium/calmodulin-dependent phosphodiesterases with dual specificity for cAMP and cGMP. PDE1C selectively regulates cAMP during SOCE, affecting leading-edge protrusions (LEP) formation critical for cell migration. Inhibition of PDE1C reduces SOCE-dependent ADCY8 activation, decreasing cAMP accumulation and LEP formation. PDE1C couples calcium signals to cAMP dynamics in spatially restricted signalosomes. ADRA1B (α1B-adrenergic receptor) is a G protein-coupled receptor activating PKC and influencing neuronal differentiation and cell migration. In GBM, dysregulation of this program alters cell motility and invasive phenotype.

**Predicted impacts**
- Altered leading-edge protrusion dynamics affecting cell migration speed and direction
- Dysregulated cAMP signaling affecting cell motility and proliferation
- Enhanced SOCE-dependent signaling promoting calcium-driven invasion
- Modified adrenergic receptor signaling affecting neuronal differentiation capacity
- Spatial restriction of calcium-cAMP coupling promoting localized migration signals

**Evidence summary**
Three genes regulating cyclic nucleotide and calcium signaling are present in the input list. PDE1A and PDE1C are calcium/calmodulin-dependent phosphodiesterases with dual cAMP/cGMP specificity. PDE1C selectively regulates SOCE-dependent cAMP dynamics affecting leading-edge protrusion formation and cell migration. PDE1C inhibition reduces SOCE magnitude and rate, decreasing cAMP-dependent motility. PALM2-AKAP2 anchors kinase A and coordinates signalosome assembly. ADRA1B is an α1B-adrenergic receptor affecting cell behavior and differentiation. In GBM, dysregulation of this program through altered PDE1C activity and calcium coupling would modulate invasion and metastatic capacity.

**Atomic biological processes**
- Store-operated calcium entry (SOCE) regulation. Genes: PDE1A, PDE1C
  - [21]: ER Ca2+ store depletion activates PDE1C; PDE1C inhibition reduces SOCE rate and magnitude
- cAMP hydrolysis and signal termination. Genes: PDE1A, PDE1C
  - [21]: PDE1C activation reduces early transient decrease in cAMP during SOCE; enhances cAMP accumulation in latter phase
- Leading-edge protrusion formation. Genes: PDE1C
  - [21]: PDE1C regulates LEP formation critical for cell migration; couples calcium to cAMP signaling
- ADCY-mediated cAMP synthesis. Genes: PDE1A, PDE1C
  - [21]: ADCY8 is dominant source of cAMP for AKAP-based PKA-containing signalosomes regulating LEP formation
- α1B-adrenergic receptor signaling. Genes: ADRA1B
  - [22]: ADRA1B modulates neuronal differentiation and cell behavior

**Atomic cellular components**
- Phosphodiesterase complexes. Genes: PDE1A, PDE1C
  - [21]: PDE1C operates in localized signaling domains at front of polarized cells
- AKAP-based signalosome. Genes: PDE1C, PALM2-AKAP2
  - [21]: AKAP-based PKA-containing signalosomes coordinate PDE1C, ADCY, and calcium signaling
- G protein-coupled receptor complexes. Genes: ADRA1B
  - [20]: FGFR interact with G protein-coupled receptors including adrenergic receptors

**Required genes (not in input)**
- Genes: STIM1, ORAI1, ADCY1, ADCY3, ADCY5, ADCY6, ADCY8, ADCY9, PRKA, PRKC, AKAP1, AKAP2, AKAP3, AKAP4, AKAP5, AKAP6, CALM1, CALM2, CALM3, CAMK2A, CAMK2B, CAMK2D, CAMK4
  - [21]: STIM1 and ORAI1 mediate SOCE; ADCY8 provides cAMP substrate for PDE1C

**Program citations**
- [21]: PDE1C regulates SOCE and SOCE-dependent cAMP changes affecting cell migration
- [22]: Transcriptome changes during neural differentiation include alterations in cAMP signaling components

## Program: RNA-Binding and Post-Transcriptional Control
This program comprises RNA-binding proteins and splicing factors that regulate post-transcriptional gene expression affecting mRNA stability, localization, and translation. The program includes RBFOX1 (RNA-binding fox-1), SRRM4 (serine/arginine repetitive matrix 4), and long non-coding RNAs (lncRNAs). RBFOX1 binds to GCAUG motifs in nascent RNA during splicing and also in 3' UTRs affecting mRNA stability and translation. Cytoplasmic RBFOX1 increases target mRNA stability and translation; cytoplasmic RBFOX1 targets are enriched in cortical development and autism-related genes. RBFOX1 knockout mice show altered synaptic transmission, increased membrane excitability, and seizure predisposition. Reduced RBFOX1 expression correlates with autism and developmental delay. SRRM4 is a neuron-specific splicing regulator. Multiple lncRNAs in the input list (LINC01033, LINC01344, LINC02607, LINC01949, LINC00862, LINC02378, LINC00470, LINC00707, LINC01965) may function as competing endogenous RNAs (ceRNAs) or direct regulators of gene expression. In GBM, dysregulation of RNA-binding protein networks could suppress neuronal differentiation programs.

**Predicted impacts**
- Altered splicing of synaptic and developmental genes affecting differentiation capacity
- Enhanced mRNA stability of proliferation-promoting transcripts
- Disrupted competition between RBFOX1 and miRNAs affecting target mRNA stability
- Dysregulation of autism-related and cortical development gene networks
- Modified translation efficiency of key developmental regulators

**Evidence summary**
Two RNA-binding proteins and multiple long non-coding RNAs are present in the input list. RBFOX1 regulates genome-wide alternative splicing events important for neuronal development; reduced RBFOX1 expression associates with autism and developmental delay. RBFOX1 functions in both nuclear (splicing) and cytoplasmic (mRNA stability/translation) compartments. Cytoplasmic RBFOX1 target mRNAs are enriched in cortical development and autism genes. SRRM4 promotes neuron-specific splicing programs. Multiple lncRNAs (LINC01033, LINC01344, LINC02607, etc.) may function as ceRNAs or direct regulators. In GBM, dysregulation of RBFOX1 and lncRNA networks would suppress pro-differentiation signaling maintaining proliferative state.

**Atomic biological processes**
- Alternative splicing regulation. Genes: RBFOX1, SRRM4
  - [59]: RBFOX1 regulates wide range of alternative splicing events implicated in neuronal development
  - [56]: RBFOX1 functions as splicing regulator in nucleus; iCLIP-seq shows binding to introns in nascent RNA
- mRNA stability and 3' UTR regulation. Genes: RBFOX1
  - [56]: Cytoplasmic RBFOX1 binds to 3' UTRs increasing target mRNA stability and translation
- miRNA-mediated gene silencing regulation. Genes: RBFOX1
  - [56]: RBFOX1 and miRNA binding sites overlap significantly; RBFOX1 may compete with miRNA binding
- Long non-coding RNA regulation. Genes: LINC01033, LINC01344, LINC02607, LINC01949, LINC00862, LINC02378, LINC00470, LINC00707, LINC01965, MIR3681HG
  - [56]: Multiple lncRNAs implicated in transcriptome control and ceRNA networks

**Atomic cellular components**
- Nuclear splicing complexes. Genes: RBFOX1, SRRM4
  - [59]: RBFOX1 functions as component of nuclear splicing apparatus
- Cytoplasmic mRNP complexes. Genes: RBFOX1
  - [56]: Cytoplasmic RBFOX1 localizes in mRNP complexes affecting mRNA metabolism
- P-bodies. Genes: RBFOX1
  - [3]: m6A-modified mRNAs and RNA-binding proteins colocalize with P-bodies

**Required genes (not in input)**
- Genes: NOVA1, NOVA2, ELAVL1, ELAVL2, ELAVL3, ELAVL4, HNRNPA1, HNRNPA2B1, HNRNPC, HNRNPD, HNRNPL, HNRNPM, HNRNPU, PABPC1, PABPN1, DCP1A, DCP2, XRN1, DICER1, AGO2, GEMIN3, GEMIN4
  - [59]: NOVA1 and other splicing factors work coordinatively with RBFOX1

**Program citations**
- [56]: Cytoplasmic RBFOX1 regulates expression of synaptic and autism-related genes
- [59]: RBFOX1 regulates both splicing and transcriptional networks implicated in neurodevelopment

## Bibliography
1. Tingfeng W, Yuntao L, Baohui L, Shenqi Z, Liquan W, Xiaonan Z, et al.. Expression of Ferritin Light Chain (FTL) Is Elevated in Glioblastoma, and FTL Silencing Inhibits Glioblastoma Cell Proliferation via the GADD45/JNK Pathway.. PloS one [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26871431/
2. Argyris S, Ananya R, Anqi X, Soumi K, Xi L, Ylva J, et al.. Heparan sulfate N-deacetylase/N-sulfotransferase-1 regulates glioblastoma cell migration and invasion.. Matrix biology : journal of the International Society for Matrix Biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40796061/
3. Available from: https://eprints.nottingham.ac.uk/60129/1/The%20influence%20of%20N6-methyladenosine%20(m6A)%20RNA%20methylation%20on%20synaptic%20function%20and%20local%20protein%20synthesis.pdf
4. Zhigang C, Han X, Jun L, JiaJia Z, Ruixiang H, Yufei X, et al.. Roles of TRPM channels in glioma.. Cancer biology & therapy [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11062369/
5. Available from: https://portal.research.lu.se/en/publications/heparan-sulfate-n-deacetylasen-sulfotransferase-1-regulates-gliob
6. Available from: https://kaeser.hms.harvard.edu/sites/kaeser.hms.harvard.edu/files/publications/2022/Kershberg%202022%20Elife%20main+SOM%20final.pdf
7. Available from: https://maayanlab.cloud/Harmonizome/gene_set/MYC/CHEA+Transcription+Factor+Targets
8. Caitlin M, Gord F, Richard WT. Unifying Views of Autism Spectrum Disorders: A Consideration of Autoregulatory Feedback Loops.. Neuron [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5757244/
9. Carolina N, Ana SR, Ricardo T, Diogo SC, Joaquim R, Cláudia F, et al.. Cadherin Expression and EMT: A Focus on Gliomas.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533397/
10. A MUBM, A MZ-B-M, Dibya JP. A network-biology approach for identification of key genes and pathways involved in malignant peritoneal mesothelioma.. Genomics & informatics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8261271/
11. Available from: https://aacrjournals.org/cancerres/article/85/2/231/750993/FOXR2-Targets-LHX6-DLX-Neural-Lineages-to-Drive
12. Martins EP, Gonçalves CS, Pojo M, Carvalho R, Ribeiro AS, Miranda‐Gonçalves V, et al.. <i>Cadherin‐3</i> is a novel oncogenic biomarker with prognostic value in glioblastoma. Molecular Oncology [Internet]. 2022Jun10;16(14). Available from: https://febs.onlinelibrary.wiley.com/doi/full/10.1002/1878-0261.13162
13. Enaya M, Hiroaki W. Extracellular matrix in glioblastoma: opportunities for emerging therapeutic approaches.. American journal of cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8414390/
14. Yoshi K. Roles of SNARE proteins and synaptotagmin I in synaptic transmission: studies at the Drosophila neuromuscular synapse.. Neuro-Signals [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/12624525/
15. Mei Y, Si-Lu Y, Stephanie H, Chen L, Monika D, Kirk CH, et al.. Lin28 promotes the proliferative capacity of neural progenitor cells in brain development.. Development (Cambridge, England) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4419280/
16. Salvatore M, Grazia M, Rina DB, Lucia L, Pierpaolo M, Federica F, et al.. The Extracellular Matrix in Glioblastomas: A Glance at Its Structural Modifications in Shaping the Tumoral Microenvironment-A Systematic Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
17. Xiang Y, Cui L, Yao J, Lou X, Wu M, Huo J, et al.. Synaptotagmin-1 serves as a primary Zn2+ sensor to mediate spontaneous neurotransmitter release under pathological conditions. Nature Communications [Internet]. 2025Aug2;16(1). Available from: https://www.nature.com/articles/s41467-025-62496-1
18. Available from: https://journals.biologists.com/dev/article/147/23/dev193631/225966/Neuronal-differentiation-strategies-insights-from
19. Tiffany AM, Izabela K, Arkadi M, Ying Z, Anant S, Roger A, et al.. Myt1 and Myt1l transcription factors limit proliferation in GBM cells by repressing YAP1 expression.. Biochimica et biophysica acta Gene regulatory mechanisms [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/
20. Xie Y, Su N, Yang J, Tan Q, Huang S, Jin M, et al.. FGF/FGFR signaling in health and disease. Signal Transduction and Targeted Therapy [Internet]. 2020Sep2;5(1). Available from: https://www.nature.com/articles/s41392-020-00222-7
21. Paulina B, Nicholas JS, Fabien H, Ariana NJ, M BU, Jodi LM, et al.. Phosphodiesterase 1C integrates store-operated calcium entry and cAMP signaling in leading-edge protrusions of migrating human arterial myocytes.. The Journal of biological chemistry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8095186/
22. Ma N-X, Yin J-C, Chen G. Transcriptome Analysis of Small Molecule–Mediated Astrocyte-to-Neuron Reprogramming. Frontiers in Cell and Developmental Biology [Internet]. 2019May31;7. Available from: https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2019.00082/full
23. Shuyan D, Zhan Z, Zhuchu C, Guangyu X, Yongheng C. Fibroblast Growth Factor Receptors (FGFRs): Structures and Small Molecule Inhibitors.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6627960/
24. Available from: https://www.uniprot.org/uniprotkb/Q61481/entry
25. Available from: https://academic.oup.com/endo/article/166/12/bqaf169/8321651
26. Available from: https://maayanlab.cloud/Harmonizome/gene/GREM2
27. Available from: https://www.ncbi.nlm.nih.gov/books/NBK6446/
28. Available from: https://www.ncbi.nlm.nih.gov/gene/14526
29. Available from: https://www.ncbi.nlm.nih.gov/gene/64388
30. A S, M L, N H, N ES, O N, R N, et al.. Sema3C and netrin-1 differentially affect axon growth in the hippocampal formation.. Molecular and cellular neurosciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/10673323/
31. Available from: https://www.nature.com/articles/6690367
32. Junghwa C, Erika AD, Emily MC, Annabelle F, Manish KA, Sanjay K. Glioma Cells Secrete Collagen VI to Facilitate Invasion.. bioRxiv : the preprint server for biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760023/
33. Zhang X, Lin P-Y, Liakath-Ali K, Südhof TC. Teneurins assemble into presynaptic nanoclusters that promote synapse formation via postsynaptic non-teneurin ligands. Nature Communications [Internet]. 2022Apr28;13(1). Available from: https://www.nature.com/articles/s41467-022-29751-1
34. Available from: https://www.ncbi.nlm.nih.gov/gene/14585
35. Chen X, Zhong X, Zhang F, Zhou X, Yue X, Li X. Molecular mechanisms and therapeutic targets in glioblastoma multiforme: network and single-cell analyses. Scientific Reports [Internet]. 2025Mar27;15(1). Available from: https://www.nature.com/articles/s41598-025-92867-z
36. Nickolai VV, John-Paul S, Vera GL, Jason S, John C, Jennifer KB, et al.. Proteolytically released Lasso/teneurin-2 induces axonal attraction by interacting with latrophilin-1 on axonal growth cones.. eLife [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30457553/
37. Available from: https://maayanlab.cloud/Harmonizome/gene/SCG2
38. Dale JL, Claudia W, Charles E, Bruce AC, Gary A, Steven MP, et al.. Variations in potassium channel genes are associated with breast pain in women prior to breast cancer surgery.. Journal of neurogenetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4035357/
39. Carmela M, Paolo S, Lalarukh HS, Wanfeng Z, Mark G, Luis JVG, et al.. ANO4 (Anoctamin 4) Is a Novel Marker of Zona Glomerulosa That Regulates Stimulated Aldosterone Secretion.. Hypertension (Dallas, Tex : 1979) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6791498/
40. Hyung JK, Ahmet MD, Rebecca W, Tithi DB, Gregory DC, Ari SM, et al.. REST Regulates Non-Cell-Autonomous Neuronal Differentiation and Maturation of Neural Progenitor Cells via Secretogranin II.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4635134/
41. Available from: https://www.ncbi.nlm.nih.gov/books/NBK609910/
42. Brittany D, Lauren U, Emily VF, Terrance GJ. Anoctamins and Calcium Signalling: An Obstacle to EGFR Targeted Therapy in Glioblastoma?. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9740065/
43. Manali T, Jennifer H, Laura AN, Jasmin L, Nina J. Receptor Tyrosine Kinase Signaling and Targeting in Glioblastoma Multiforme.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7918566/
44. Yi D, Yan Z, Chao X, Qing-Hua T, Ye-Guang C. HECT domain-containing E3 ubiquitin ligase NEDD4L negatively regulates Wnt signaling by targeting dishevelled for proteasomal degradation.. The Journal of biological chemistry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3605647/
45. Nan H, Linqing Z, Cheng W, Guoqi S. RUNX1T1 function in cell fate.. Stem cell research & therapy [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9330642/
46. Tomuleasa C, Tigu A-B, Munteanu R, Moldovan C-S, Kegyes D, Onaciu A, et al.. Therapeutic advances of targeting receptor tyrosine kinases in cancer. Signal Transduction and Targeted Therapy [Internet]. 2024Aug14;9(1). Available from: https://www.nature.com/articles/s41392-024-01899-w
47. Manning JA, Shah SS, Nikolic A, Henshall TL, Khew-Goodall Y, Kumar S. The ubiquitin ligase NEDD4-2/NEDD4L regulates both sodium homeostasis and fibrotic signaling to prevent end-stage renal disease. Cell Death &amp; Disease [Internet]. 2021Apr14;12(4). Available from: https://www.nature.com/articles/s41419-021-03688-7
48. Available from: https://www.oncokb.org/gene/RUNX1T1
49. Florence L. Transient Receptor Potential (TRP) Ion Channels Involved in Malignant Glioma Cell Death and Therapeutic Perspectives.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8388852/
50. Yamagishi S, Bando Y, Sato K. Involvement of Netrins and Their Receptors in Neuronal Migration in the Cerebral Cortex. Frontiers in Cell and Developmental Biology [Internet]. 2021Jan15;8. Available from: https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2020.590009/full
51. Allison AF, Louis MW. The role of fibroblast activation protein in health and malignancy.. Cancer metastasis reviews [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7487063/
52. Chinigò G, Castel H, Chever O, Gkika D. TRP Channels in Brain Tumors. Frontiers in Cell and Developmental Biology [Internet]. 2021Apr13;9. Available from: https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.617801/full
53. Available from: https://www.ncbi.nlm.nih.gov/gene/8633
54. Xin L, Gao J, Zheng Z, Chen Y, Lv S, Zhao Z, et al.. Fibroblast Activation Protein-α as a Target in the Bench-to-Bedside Diagnosis and Treatment of Tumors: A Narrative Review. Frontiers in Oncology [Internet]. 2021Aug19;11. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.648187/full
55. Available from: https://academic.oup.com/brain/advance-article/doi/10.1093/brain/awaf356/8263343
56. Ji-Ann L, Andrey D, Chia-Ho L, Mariana F, Neelroop NP, Erik SA, et al.. Cytoplasmic Rbfox1 Regulates the Expression of Synaptic and Autism-Related Genes.. Neuron [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26687839/
57. Available from: https://maayanlab.cloud/Harmonizome/gene/PRSS12
58. Available from: https://www.ncbi.nlm.nih.gov/gene/9568
59. Available from: https://academic.oup.com/hmg/article/21/19/4171/584744
60. Available from: https://www.ncbi.nlm.nih.gov/gene/19142
