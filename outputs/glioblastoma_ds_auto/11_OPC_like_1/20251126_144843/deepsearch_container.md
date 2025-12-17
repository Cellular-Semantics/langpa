# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: glioblastoma multiforme (IDH wildtype)
- Tissue: brain

## Input Genes
AFAP1L2, COL4A3, FERMT1, VIPR2, AL512308.1, CALCRL, REPS2, FGF12, CCDC26, OTOGL, ELMO1, PCDH15, COL4A4, THSD4, FA2H, LRRC7, PLPP4, PLA2G4A, AR, LINC00689, TNS3, BCAS1, DLL3, KCNIP3, MIR503HG, ... (109 total)

## Program: Extracellular Matrix Remodeling and Cell Adhesion
This program encompasses genes encoding structural proteins, proteoglycans, and adhesion molecules that compose and remodel the glioblastoma extracellular matrix. The ECM serves as an active mediator of tumor invasion, immune cell infiltration, and therapeutic resistance through dynamic interactions with tumor and stromal cells. Components include collagen crosslinkers, matricellular proteins, and glycoproteins that facilitate cell-cell contact and cell-matrix interactions critical for GBM progression.

**Predicted impacts**
- Enhanced ECM-mediated tumor cell invasion through sinuous brain tissue
- Increased cell-cell contact adhesion promoting collective invasion
- Altered leukocyte infiltration and immune suppression through ECM remodeling
- Sustained proliferative signaling via integrin-ECM crosstalk
- Therapeutic resistance through altered drug penetration in dense ECM

**Evidence summary**
Multiple genes in this program encode ECM components and adhesion molecules known to be dysregulated in glioblastoma. Search results demonstrate that ECM remodeling actively contributes to GBM progression, invasion, and immune evasion. The combination of collagen genes (COL4A3, COL4A4, COL20A1), matricellular proteins (SMOC1, TNR), and adhesion molecules (ALCAM, PCDH15) creates a comprehensive picture of pathological ECM architecture. ADAMTS17 proteolytic activity would facilitate ECM remodeling. Higher ECM density is associated with poor prognosis and restricted immune cell infiltration.

**Atomic biological processes**
- collagen fibril assembly and crosslinking. Genes: COL4A3, COL4A4, COL20A1, ADAMTS17
  - [5]: Systematic review demonstrates fibrillary proteins including collagen as major ECM components involved in GBM invasion and tumor infiltration
  - [34]: Collagen type I homotrimers produced by CAFs promote oncogenic signaling and immunosuppression in tumors
- cell adhesion molecule expression and function. Genes: ALCAM, PCDH15, MEGF11, LRFN5
  - [3]: PTGFRN identified as cell adhesion molecule upregulated in GBM with prognostic significance for cell growth and migration
  - [9]: Cadherin-11 expressed as marker of mesenchymal phenotype in GBM, regulating invasion and migration
- matricellular protein interactions. Genes: SMOC1, TNR, THSD4, LAMB4
  - [5]: Systematic review identifies proteoglycans and glycoproteins as ECM components actively shaping tumor development
  - [25]: SMOC1 identified as tenascin-C interacting protein overexpressed in glioblastomas, capable of counteracting chemo-attractive effects
- integrin-ECM interaction and signaling. Genes: ITGA9, FERMT1
  - [7]: Diamond nanoparticles suppress T98G glioblastoma migration by targeting ECM-integrin interactions through α/β integrin blocking

**Atomic cellular components**
- extracellular matrix scaffold. Genes: COL4A3, COL4A4, COL20A1, TNR, SMOC1
  - [5]: ECM characterized by increased density and tension with aberrant expression of hyaluronic acid, tenascin-C, fibronectin, and proteoglycans
- adhesion complex organization. Genes: ALCAM, PCDH15, LRRC7, TNS3
  - [3]: Cell adhesion molecules involved in ERK, AKT, and mTOR signaling pathways regulating proliferation and migration

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP3, VERSICAN, PERLECAN, NIDOGEN, FIBRONECTIN
  - [5]: MMPs and other degradative enzymes required for ECM remodeling are central to GBM invasion
  - [34]: Extensive ECM proteins discussed as contributing to GBM progression and immune infiltration

**Program citations**
- [5]: Systematic review on ECM modifications in GBM showing active role in tumor development and microenvironment shaping
- [34]: Review on leveraging ECM to increase immunotherapy efficacy through understanding ECM-immune cell interactions
- [7]: Recent study (2025) demonstrating ECM-integrin interactions as therapeutic target in GBM

## Program: Ion Channel-Mediated Cell Motility
This program integrates ion channels and transporters that regulate cellular ion homeostasis, membrane potential, and cell volume dynamics essential for glioblastoma migration and invasion. Potassium, calcium, chloride, and sodium channels modulate cell cycle progression and facilitate the morphological changes necessary for cells to navigate through constrained brain tissue spaces. Dysregulation of these channels contributes to the extensive invasive migration characteristic of GBM.

**Predicted impacts**
- Facilitated cell cycle progression through G1/S and G2/M checkpoints
- Enhanced invasive cell migration through rapid morphological transitions
- Improved survival under metabolic stress through pH buffering
- Increased cell volume dynamics enabling navigation through sinuous extracellular spaces
- Sustained proliferation via ion-dependent signaling amplification

**Evidence summary**
Ion channels are fundamental to GBM's extensive invasive behavior. Multiple genes encode channels (CACNA1E, TRPC4, KCNIP3, ANO3, ANO4) and transporters (SLC8A3, SLC5A4, SLC26A7) that collectively enable the electrophysiological adaptations required for migration. CA10 acidifies the microenvironment, which is known to promote invasion. The literature specifically documents that potassium channel activity facilitates cell cycle checkpoint progression, chloride channels enable cell shrinkage, and calcium channels activate downstream migration machinery. These ion-dependent processes are essential for GBM's characteristic aggressive invasive phenotype.

**Atomic biological processes**
- potassium channel activity and cell cycle regulation. Genes: KCNIP3
  - [4]: K+ channels facilitate progression through G1/S checkpoint via hyperpolarization; iberiotoxin (K+ channel inhibitor) arrests glioma cells in S phase
- calcium influx and signaling. Genes: CACNA1E, TRPC4
  - [4]: Ca2+ input activates gBK channels providing electrochemical driving force for K+ current and water loss facilitating cell shrinkage and migration
- chloride channel-mediated depolarization. Genes: ANO3, ANO4
  - [4]: ClC-3 channels show outwardly rectifying current; overexpression equips GBM cells with improved Cl- transport enabling rapid cell size/shape changes during invasion
- sodium transport and osmotic regulation. Genes: SLC8A3, SLC5A4
  - [4]: Amiloride-sensitive BNaC channels expressed in glioblastoma; Na+ transport couples to osmotic water movement
- pH regulation and acidification. Genes: CA10
  - [27]: CA10 (carbonic anhydrase IX/CAIX) catalyzes CO2 + H2O to HCO3- + H+, extrudes H+ into extracellular space creating acidic TME conducive to invasion

**Atomic cellular components**
- ion channel complexes. Genes: CACNA1E, TRPC4, KCNIP3, ANO3, ANO4
  - [4]: Comprehensive review of potassium, sodium, chloride, and calcium channels in glioblastoma cell cycle and migration
- solute carrier transporters. Genes: SLC8A3, SLC5A4, SLC26A7
  - [13]: Migration-associated transportome identifies SLC transporters involved in GBM cell mobility

**Required genes (not in input)**
- Genes: KCNJ10, KCNQ3, KCNA1, CACNB4, SLC12A5
  - [4]: Other K+, Ca2+, and Cl- channels implicated in GBM but not present in input gene list

**Program citations**
- [4]: Comprehensive 2011 review on ion channels in glioblastoma detailing roles in proliferation, migration, and invasion
- [13]: Recent analysis of migration-associated transportome including SLC transporters in GBM

## Program: Oligodendrocyte Lineage Progenitor Identity
This program comprises genes characterizing oligodendrocyte precursor cells (OPCs) and immature oligodendrocytes, cell types implicated as cells-of-origin for glioblastoma. These genes regulate cell fate determination, developmental progression, and maintenance of progenitor cell characteristics. The aberrant expression of OPC-associated genes in GBM reflects the developmental origin of these tumors and their heterogeneous cellular composition including pre-myelinating states.

**Predicted impacts**
- Maintenance of progenitor cell state and self-renewal capacity
- Impaired terminal differentiation with retention of proliferative phenotype
- Activation of developmental programs associated with GBM stem cells
- Enhanced glioma stemness through aberrant OPC program expression
- Tumor heterogeneity driven by multiple OPC-derived cellular states

**Evidence summary**
The input genes represent key markers and regulators of oligodendrocyte lineage. Recent studies identify OPCs as a cell-of-origin for glioma, and this program captures the developmental genes that maintain this identity. BCAS1 is explicitly identified as an immature oligodendrocyte marker overexpressed in gliomas. MYRF and SOX6 regulate transcriptional programs controlling the OPC-to-oligodendrocyte transition. MOG and OMG are myelin-associated proteins. The co-expression of these genes in GBM reflects the tumor's origins from aberrantly programmed progenitor cells. CLDN11 (claudin-11) is an oligodendrocyte-specific tight junction protein.

**Atomic biological processes**
- oligodendrocyte precursor cell specification and maintenance. Genes: SOX6, MYRF
  - [2]: Olig1 and Olig2 are critical bHLH transcription factors central to oligodendrocyte development
  - [10]: OLIG2 identified as most specific glioblastoma stem cell marker with highest differential expression in GSC-enriched cultures
- myelin gene regulation and terminal differentiation. Genes: MYRF, OMG, MOG
  - [24]: Myrf guides target gene selection of Sox10 during oligodendrocyte differentiation, controlling both differentiation and blocking OPC-specific programs
- immature oligodendrocyte marker expression. Genes: BCAS1, CLDN11
  - [40]: BCAS1 (brain enriched myelin associated protein 1) is novel marker of immature oligodendrocytes and shows expression in diffuse gliomas, particularly oligodendrogliomas and glioblastomas

**Atomic cellular components**
- oligodendrocyte development transcription factor complex. Genes: SOX6, MYRF, EYA1
  - [24]: Sox10 and Myrf function together during oligodendrocyte terminal differentiation, with Myrf redirecting Sox10 from OPC to mature genes
- oligodendrocyte membrane proteins. Genes: BCAS1, MOG, OMG, CLDN11
  - [40]: BCAS1+ cells display morphology and characteristics similar to pre-myelinating oligodendrocytes; co-expression with BLBP marker in stellate cells

**Required genes (not in input)**
- Genes: OLIG2, OLIG1, SOX10, NKX2-2, GPR17
  - [10]: OLIG2 is critical OPC marker and most specific GSC identifier not in input list
  - [24]: SOX10 is essential partner of Myrf in oligodendrocyte development

**Program citations**
- [40]: First comprehensive characterization of BCAS1 expression in diffuse gliomas showing correlation with tumor grade and proliferation
- [24]: Detailed mechanistic study of Myrf-Sox10 cooperation during oligodendrocyte development
- [10]: Identification of OLIG2 as most specific GSC marker demonstrating developmental origin of GBM

## Program: Notch Signaling and Stem Cell Maintenance
This program encompasses genes controlling Notch pathway signaling that maintains glioma stem cell (GSC) self-renewal, stemness capacity, and resistance to differentiation. Delta-like ligands (DLL1, DLL3) and downstream effectors regulate the undifferentiated phenotype characteristic of GSCs. Dysregulation of Notch signaling is associated with poor prognosis and enhanced tumor aggressiveness in glioblastoma.

**Predicted impacts**
- Sustained GSC self-renewal and reduced differentiation capacity
- Enhanced stem cell marker expression including CD133, nestin, SOX2, OCT4
- Increased resistance to apoptosis through Notch-AKT signaling
- Promoted epithelial-to-mesenchymal transition and invasion
- Improved survival under stress conditions through let-7 suppression

**Evidence summary**
This program integrates Notch pathway components with microRNA regulation of stemness. DLL1 and DLL3 are established Notch ligands whose expression correlates with glioma grade and prognosis. Recent literature shows DLL1 acts on differentiated cells within tumors to activate Notch in GSCs, while silencing DLL1 impairs GSC self-renewal. LIN28B is markedly overexpressed in glioblastoma and drives stemness through let-7 suppression. The microRNAs (MIR503HG, MIR217HG) are likely regulatory loci controlling stemness-related pathways. The combination of Notch ligands with LIN28B-mediated miRNA dysregulation creates multiple layers of control maintaining the undifferentiated GSC state.

**Atomic biological processes**
- Delta-like ligand-mediated Notch activation. Genes: DLL1, DLL3
  - [11]: DLL1 activates Notch1 signaling to maintain stem cell phenotype of glioma initiating cells; silencing DLL1 decreases stem cell markers and impairs self-renewal
- stem cell self-renewal and stemness maintenance. Genes: DLL1, DLL3
  - [11]: Notch1 overexpression associates with low overall survival and undifferentiated aggressive phenotype; higher expression in peritumor GSCs
- microRNA regulation of Notch pathway. Genes: LIN28B, MIR503HG, MIR217HG
  - [11]: miR-18a downregulates DLL3 and strengthens Notch1 signaling via ERK, maintaining GSC self-renewal and stemness via SHH/GLI-1
  - [14]: LIN28B prevents let-7 microRNA biogenesis; let-7 suppresses tumorigenic pathways including those promoting stemness and proliferation
- Notch-mediated EMT and invasion. Genes: DLL1, DLL3
  - [11]: Notch1 overexpression promotes AKT activation inducing nuclear localization of β-catenin and NF-κB; overexpression of Snail, Zeb1, vimentin promotes invasion

**Atomic cellular components**
- Notch signaling receptor and ligand complex. Genes: DLL1, DLL3
  - [11]: DLL1 and DLL3 ligands activate Notch receptors; complex regulation of expression patterns across different GBM subtypes
- microRNA biogenesis and regulation. Genes: LIN28B, MIR503HG, MIR217HG
  - [14]: LIN28B as RNA binding protein prevents let-7 microRNA maturation; let-7 family members decrease genes promoting stemness, proliferation, migration

**Required genes (not in input)**
- Genes: NOTCH1, NOTCH3, HEY1, HES1, let-7 family miRNAs
  - [11]: Notch receptors and downstream effectors required for pathway completion; higher expression of NOTCH1, NOTCH3, HEY1 correlates with higher glioma grade
  - [14]: Let-7 family members directly suppress stemness genes when not blocked by LIN28B

**Program citations**
- [11]: Comprehensive review of Notch signaling in GBM pathogenesis with emphasis on GSC maintenance and poor prognosis correlation
- [14]: Review on LIN28B and let-7 in diffuse midline glioma demonstrating LIN28B overexpression in GBM with poor survival

## Program: Lipid Metabolism and Sphingolipid Remodeling
This program encompasses enzymes and transporters regulating lipid and sphingolipid metabolism, including fatty acid hydroxylation, glycosphingolipid synthesis, and ether lipid degradation. Dysregulated lipid metabolism in GBM contributes to altered membrane composition, enhanced proliferation, migration, and survival signaling. These metabolic alterations create distinct lipid signatures associated with aggressive GBM phenotypes.

**Predicted impacts**
- Altered membrane fluidity and composition supporting enhanced proliferation
- Enhanced ceramide and hexosylceramide accumulation promoting survival signaling
- Increased arachidonic acid mobilization supporting inflammatory and pro-tumoral signals
- Modified glycosaminoglycan synthesis affecting ECM interactions and cell adhesion
- Altered immune cell recognition through lipid antigen modifications

**Evidence summary**
This program identifies dysregulated lipid metabolism in GBM. PLPP4 is specifically highlighted as dramatically elevated in glioma with strong prognostic significance for poor survival, migration, and invasion. FA2H and UGT8 coordinate to produce specific hydroxylated sphingolipids associated with cancer. AGMO regulates ether lipid degradation with emerging evidence linking it to immune responses and cancer. PLA2G4A and PLAAT1 mobilize signaling lipids. UGDH and GFPT2 support glycosaminoglycan synthesis affecting ECM composition. The convergence of multiple lipid metabolic enzymes dysregulation suggests that lipid remodeling is a hallmark of GBM's aggressive phenotype.

**Atomic biological processes**
- fatty acid 2-hydroxylation. Genes: FA2H
  - [17]: FA2H transcript levels predict 2-hydroxyHexCer accumulation in adenocarcinomas; required for accumulation of hydroxylated hexosylceramides in cancers with high UGT8
- glycosphingolipid synthesis and glycosylation. Genes: UGT8, HS6ST2, CHST9
  - [17]: UGT8 (UDP-glycosyltransferase 8) transcript levels increased in cancer subtypes; co-expressed with FA2H for 2-hydroxyHexCer accumulation
- phospholipid phosphatase activity. Genes: PLPP4
  - [26]: PLPP4 dramatically elevated in glioma tissues; high expression correlates with poor overall survival; promotes proliferation, invasion, migration
- ether lipid catabolism. Genes: AGMO
  - [39]: AGMO catalyzes breakdown of alkylglycerols and lyso-alkylglycerophospholipids; expression affects immune activation and cancer development
- phospholipase activity and arachidonic acid mobilization. Genes: PLA2G4A, PLAAT1
  - [29]: Proprotein convertases process immature proteins; various cancer contexts show PLA2G4A involvement in inflammatory signaling
- UDP-sugar metabolism. Genes: UGDH, GFPT2
  - [48]: UGDH involved in glucuronic acid synthesis for glycosaminoglycan production affecting ECM composition and cell-cell interactions

**Atomic cellular components**
- glycosphingolipid biosynthetic enzymes. Genes: FA2H, UGT8, CHST9, HS6ST2
  - [17]: FA2H and UGT8 coordinate to produce 2-hydroxyHexCers with specific accumulation patterns in cancer cells
- phospholipid remodeling enzymes. Genes: PLPP4, PLA2G4A, PLAAT1
  - [26]: PLPP4 expressed in cytoplasm of GBM cells; involved in lipid phosphate metabolism affecting cellular signaling

**Required genes (not in input)**
- Genes: SGPL1, CERT1, SPHK1, ASAH1, CERS
  - [17]: Other sphingolipid metabolic enzymes dysregulated in cancers but not present in input list

**Program citations**
- [26]: PLPP4 as driver of malignant glioma progression with high expression correlating with clinicopathological features and poor survival
- [17]: FA2H and UGT8 transcript levels predicting hydroxylated hexosylceramide accumulation in cancer
- [39]: AGMO as emerging enzyme with roles in immune defense and cancer development

## Program: Cell Migration and Invasion Machinery
This program integrates genes encoding proteins that directly facilitate glioblastoma cell motility, including cell migration regulators, cytoskeletal modulators, and axon guidance pathway components. These genes coordinate dynamic actin remodeling, cell-matrix interactions, and directional migration enabling GBM cells to infiltrate surrounding brain tissue. Dysregulation of this program drives the extensive invasion characteristic of GBM and is associated with therapeutic resistance.

**Predicted impacts**
- Enhanced directional migration toward chemoattractants and away from repellents
- Sustained actin polymerization dynamics supporting morphological plasticity
- Improved focal adhesion formation and turnover enabling rapid migration
- Increased invasive potential through sinuous brain parenchyma
- Adaptation to hypoxic and acidic microenvironments during migration

**Evidence summary**
Multiple genes in this program directly regulate GBM migration and invasion. ELMO1 is specifically identified in the literature as abundant in invasive tumor areas and central to migration. DOCK10 (dock family guanine nucleotide exchange factor) partners with ELMO1 in cell migration complexes. KIF21B regulates actin dynamics during neuronal migration, a mechanism likely conserved in glioma cells. Focal adhesion regulators (TNS3, FERMT1) control cell-matrix interactions. Axon guidance molecules (SLIT1, SEMA3E) provide directional cues. LHFPL3-AS1 (antisense RNA) may regulate its cognate protein involved in EMT. The convergence of cytoskeletal regulators, focal adhesion proteins, and guidance molecules creates comprehensive control of the migration phenotype.

**Atomic biological processes**
- cell migration and motility regulation. Genes: ELMO1, DOCK10, REPS2, LHFPL3-AS1
  - [16]: ELMO1 specifically abundant in invasive areas of glioblastoma tumors and central for promoting cell migration
  - [31]: LHFPL3 plays role in migration and invasion of GBM; interaction with miRNAs participates in EMT
- axon guidance and chemo-repulsion. Genes: SLIT1, SEMA3E
  - [15]: Slit proteins regulate axon guidance through chemo-repulsive signals; mechanism relevant to glioma cell motility
- actin cytoskeleton dynamics and organization. Genes: KIF21B, LRRC7, TNS3, AFAP1L2
  - [35]: Kif21b directly binds and regulates actin cytoskeleton in migratory neurons; Kif21b-mediated actin regulation influences branching and nucleokinesis during locomotion
- focal adhesion assembly and dynamics. Genes: TNS3, FERMT1
  - [7]: Diamond nanoparticles block α/β integrins impairing early adhesion and reducing T98G cell migration within 48 hours

**Atomic cellular components**
- cell migration regulator proteins. Genes: ELMO1, DOCK10, REPS2
  - [16]: ELMO1-DOCK180 complex central to cytoskeletal reorganization driving cell migration in invasive glioma areas
- actin regulatory complex. Genes: KIF21B, LRRC7, TNS3, AFAP1L2
  - [35]: Actin cytoskeleton regulators including LRRC7 and TNS3 control cell morphodynamics during guided migration
- chemoattractive/chemorepulsive pathway components. Genes: SLIT1, SEMA3E
  - [15]: Slit and semaphorin pathways provide directional cues for migrating cells through chemo-repulsive mechanisms

**Required genes (not in input)**
- Genes: DOCK180, RAC1, CDC42, RHO, ROBO1, ROBO2
  - [16]: DOCK180 partners with ELMO1 in migration complex; Rho family GTPases downstream of ELMO/DOCK signaling
  - [15]: Robo receptors bind Slit ligands to mediate chemo-repulsion

**Program citations**
- [16]: ELMO1 specifically identified in invasive areas of glioblastoma as central for cell migration
- [35]: KIF21b regulates actin cytoskeleton dynamics controlling nucleokinesis and branching during neuronal migration
- [31]: LHFPL3 involvement in GBM migration and invasion with EMT participation

## Program: Growth Factor Receptor Signaling and Proliferation
This program integrates receptor tyrosine kinases, G protein-coupled receptors, and their associated signaling molecules that drive glioblastoma proliferation. These genes regulate growth factor-dependent cell cycle progression, survival signaling, and metabolic reprogramming. Dysregulation of this program through overexpression or constitutive activation drives unchecked GBM proliferation and is associated with aggressive disease and poor prognosis.

**Predicted impacts**
- Sustained proliferation through growth factor-dependent cell cycle progression
- Enhanced survival signaling through multiple receptor pathways
- Increased metabolic flux supporting anabolic cell growth
- Amplified ERK and PI3K-AKT pathway activation
- Therapeutic resistance through receptor redundancy and pathway crosstalk

**Evidence summary**
This program integrates multiple growth-promoting receptor pathways dysregulated in GBM. FGFR4 is explicitly identified as overexpressed in aggressive GBM. AR is overexpressed in glioblastoma with higher expression in GBM vs normal brain, and AR antagonists suppress growth in vitro and in vivo. ERBB3 is highlighted as enriched in CD133+ cancer stem cells. TACR1 (substance P receptor) is consistently overexpressed in GBM cells. FGF12 acts as FGF ligand. VIPR2 (VPAC2) is a GPCR for VIP peptide. GPR17 is implicated as orphan GPCR involved in GBM signaling. CCND1 encodes cyclin D1 critical for G1/S progression. The convergence of receptor tyrosine kinases, GPCRs, and steroid receptors creates multiple independent mitogenic inputs.

**Atomic biological processes**
- receptor tyrosine kinase signaling. Genes: FGF12, VIPR2, ERBB3
  - [8]: FGFR4 overexpression contributes to malignant phenotype of aggressive GBM subgroup; associated with integrin-related therapeutic resistance
  - [23]: ERBB3 (neuregulin receptor) immunoreactivity prominent in CD133+ putative stem cells, suggesting potential therapeutic target
- androgen receptor-mediated proliferation. Genes: AR
  - [21]: AR overexpression in glioblastoma associated with higher grade disease; AR activation influences cell proliferation, migration, invasion; higher AR expression in GBM vs normal brain
- neuropeptide receptor signaling. Genes: TACR1, NRSN1
  - [30]: TACR1 (substance P receptor NK-1) consistently overexpressed in glioblastoma cells; physiological ligand substance P drives downstream signaling
- cell cycle checkpoint progression. Genes: CCND1
  - [50]: CDK inhibitors arrest cell cycle at G1-S and G2-M phases; CDK expression negatively correlates with GBM patient survival

**Atomic cellular components**
- receptor tyrosine kinase complexes. Genes: FGF12, ERBB3
  - [8]: FGFR4 overexpression in GBM activates downstream proliferative and pro-survival pathways
- G protein-coupled receptor complexes. Genes: TACR1, VIPR2, GPR17
  - [30]: TACR1 is GPCR for substance P; GPR17 is orphan GPCR crucial for transducing extracellular signals
- steroid receptor signaling. Genes: AR
  - [21]: AR functions as ligand-activated transcription factor and rapid signaling molecule in GBM

**Required genes (not in input)**
- Genes: EGFR, PDGFRA, MET, FGFR1, PI3K, MAPK
  - [45]: EGFR amplification in 40% of GBM; dysregulation of endosomal recycling pathway impacts EGFR density and signaling

**Program citations**
- [21]: AR overexpression in GBM with demonstrated role in proliferation, migration, invasion, and therapeutic resistance
- [8]: FGFR4 overexpression in aggressive GBM subgroup with integrin-related resistance
- [23]: ERBB3 enrichment in CD133+ cancer stem cells as potential therapeutic target

## Program: Mesenchymal Transition and Invasion Program
This program represents genes controlling epithelial-to-mesenchymal transition (EMT) and related developmental plasticity that drives glioblastoma's aggressive phenotype. These genes regulate the shift from adhesive epithelial-like states to migratory mesenchymal-like states, facilitating invasion and therapeutic resistance. Activation of this program is associated with poor prognosis, radiation resistance, and tumor recurrence.

**Predicted impacts**
- Shift from adhesive to migratory phenotype
- Enhanced invasive capability and reduced differentiation
- Acquisition of stem cell characteristics and therapeutic resistance
- Increased survival under stress including hypoxia and acidic conditions
- Promotion of recurrent tumors with more aggressive phenotype

**Evidence summary**
EMT is a hallmark of GBM progression associated with poor prognosis and therapeutic resistance. The literature explicitly demonstrates that glioma cells resistant to irradiation show EMT pathway enrichment, leading to highly invasive recurrence. DISC1 (Disrupted in Schizophrenia 1) has been shown to inhibit glioblastoma cell development through mitochondrial dynamics. NKD1 (naked cuticle homolog 1) inhibits Wnt signaling, with downregulated expression indicating poor prognosis. Multiple long non-coding RNAs (LINC00689, LINC01268, LINC01322) regulate developmental plasticity and cell fate transitions. CA10 acidifies the TME, promoting the mesenchymal state. The program captures the dynamic reprogramming through which GBM acquires invasiveness and stem-like properties.

**Atomic biological processes**
- epithelial-mesenchymal transition. Genes: LINC00689, NKD1, DISC1
  - [48]: EMT is important inducer of cancer stem cell phenotype; glioma cells resistant to irradiation show EMT pathway enrichment leading to highly invasive recurrence
- developmental reprogramming and cell fate plasticity. Genes: LINC00689, LINC01268, LINC01322
  - [1]: GBM transcriptional analysis reveals multiple malignant cell states including glial progenitor-like, neuronal-like and cilia-like; GPC-like state positioned as early progenitor with differentiation potential
- hypoxia-driven phenotypic switching. Genes: CA10, LINC00689
  - [49]: Hypoxia drives shared and distinct transcriptomic changes in invasive glioma stem cell lines; hypoxia drives mesenchymal-like cell state, highly invasive and promotes immune suppression

**Atomic cellular components**
- developmental transcription factor networks. Genes: LINC00689, EYA1, SOX6
  - [1]: Three baseline gene expression programs (BPs) define GBM ecosystems and cellular states; includes assessment of transcription factor activity

**Required genes (not in input)**
- Genes: SNAIL, SLUG, ZEB1, TWIST1, VIMENTIN, N-CADHERIN
  - [48]: Classical EMT transcription factors (SNAIL, SLUG, ZEB1, TWIST) required for phenotypic transition but not in input list

**Program citations**
- [48]: Comprehensive review of EMT in GBM progression showing radiation-associated EMT and acquisition of stem cell markers
- [49]: Hypoxia driving mesenchymal-like phenotype in invasive glioma stem cells with enhanced immune suppression
- [1]: Single-nucleus transcriptomics revealing multiple malignant cell states including developmental plasticity

## Program: Mitochondrial Dynamics and Cellular Metabolism
This program integrates genes controlling mitochondrial function, energetics, and metabolic adaptation essential for GBM's high proliferative and invasive capacity. These genes regulate ATP production, lipid storage, and metabolic plasticity allowing GBM cells to survive under nutrient-poor and hypoxic conditions. Dysregulation of this program supports the Warburg effect and altered metabolic state characteristic of GBM.

**Predicted impacts**
- Enhanced energy production supporting rapid proliferation and migration
- Metabolic flexibility allowing survival under hypoxia and nutrient deprivation
- Lipid accumulation in storage organelles providing energy reserves
- Enhanced radioresistance through altered mitochondrial lipid composition
- Resistance to energy-depleting therapeutic strategies

**Evidence summary**
This program identifies genes controlling metabolic adaptations enabling GBM's aggressive phenotype. DISC1 affects mitochondrial dynamics through Drp1 regulation, impacting cell development. DGKB downregulation and compensatory DGAT1 upregulation confer radioresistance by reducing mitochondrial lipotoxicity, suggesting lipid metabolic remodeling is critical for treatment resistance. PLPP4 promotes proliferation via intracellular calcium influx affecting mitochondrial function. ATP13A5 (P5A ATPase) maintains proton gradients in vesicular compartments critical for proteolytic and metabolic enzyme function. FA2H hydroxylation of fatty acids produces lipids incorporated into membranes affecting mitochondrial composition. Together these genes enable metabolic flexibility supporting GBM's survival under stress.

**Atomic biological processes**
- mitochondrial dynamics and bioenergetics. Genes: DISC1, DGKB
  - [22]: DISC1 affects glioblastoma cell development via mitochondria dynamics partly through downregulation of Drp1
  - [32]: DGKB downregulation and DGAT1 upregulation confer radioresistance by reducing mitochondrial lipotoxicity
- lipid storage and energy metabolism. Genes: DGKB, PLPP4, FA2H
  - [32]: DGKB-DGAT1 axis regulates lipid metabolism affecting mitochondrial stress; DGAT1 upregulation promotes lipid droplet accumulation for energy storage
- proton pump-mediated metabolic stress. Genes: ATP13A5
  - [43]: Vacuolar-type H+ ATPase (v-ATPase) ATP-dependent proton pump critical for endolysosomal acidification; marked ATP consumption causes energy shortage and cytotoxicity

**Atomic cellular components**
- mitochondrial protein import and organization. Genes: DISC1
  - [22]: DISC1 functions in mitochondrial dynamics affecting cell development; downregulation of Drp1 (mitochondrial fission protein) altered by DISC1
- lipid metabolism and storage organelles. Genes: DGKB, PLPP4, FA2H
  - [32]: DGKB and related enzymes regulate triglyceride synthesis affecting lipid droplet formation and energy buffering
- proton gradient maintenance. Genes: ATP13A5
  - [43]: v-ATPase maintains acidic endolysosomal environment; inhibition with bafilomycin A1 abrogates lysosomal-enlarged vacuole formation

**Required genes (not in input)**
- Genes: DRP1, OPA1, DGAT1, CPT1, ACAD
  - [22]: DRP1 (dynamin-related protein 1) is downstream target of DISC1 affecting mitochondrial fission
  - [32]: DGAT1 upregulated compensatory to DGKB downregulation in radioresistant GBM

**Program citations**
- [32]: DGKB-DGAT1 axis demonstrating lipid metabolism control of radioresistance through mitochondrial lipotoxicity
- [22]: DISC1 role in mitochondrial dynamics affecting GBM cell development

## Program: Proteolytic Processing and Proteasomal Activity
This program comprises genes encoding proteases and proteasomal components that regulate protein processing, cellular remodeling, and quality control in glioblastoma. These enzymes process pro-proteins into active forms, degrade regulatory proteins, and remodel the microenvironment. Dysregulation of proteolytic activity contributes to GBM invasion, immune evasion, and therapeutic resistance.

**Predicted impacts**
- Enhanced ECM remodeling supporting invasion and migration
- Processing of pro-inflammatory mediators affecting microenvironment
- Immune evasion through altered antigen processing
- Increased therapeutic resistance through protease-mediated drug degradation
- Amplified growth factor signaling through pro-growth factor activation

**Evidence summary**
This program identifies proteolytic enzymes dysregulated in GBM. PCSK2 (proprotein convertase subtilisin/kexin type 2) is part of the proprotein convertase family; literature demonstrates that PC inhibitors decrease GBM cell viability more effectively than temozolomide and can reactivate macrophages to be cytotoxic. PRSS12 is identified as a prognostic marker in glioblastoma. TMPRSS9 is a membrane-anchored serine protease. Together these genes enable proteolytic remodeling of the GBM microenvironment and immune regulation.

**Atomic biological processes**
- proprotein convertase-mediated processing. Genes: PCSK2
  - [29]: Proprotein convertases (PCSK) cleave proproteins at paired basic residues converting them to bioactive proteins; PC inhibitor decreases glioma cell viability at lower dose than temozolomide
- serine protease activity. Genes: PRSS12, TMPRSS9
  - [41]: PRSS12 is prognostic marker in glioblastoma multiforme; serine protease involved in ECM remodeling
- macrophage-mediated tumor immunity reactivation. Genes: PCSK2
  - [29]: PC inhibitor reactivates macrophages to be cytotoxic within tumor environment; dual role as anti-glioma and anti-tumoral macrophage reactivation drug

**Atomic cellular components**
- serine protease complexes. Genes: PRSS12, TMPRSS9
  - [41]: PRSS12 and TMPRSS9 are serine proteases involved in ECM degradation and cellular remodeling

**Required genes (not in input)**
- Genes: PC1/3, FURIN, PCSK5, PCSK7, ADAMTS
  - [29]: Other proprotein convertases (PC1/3, furin) also involved in glioma pathogenesis but not in input list

**Program citations**
- [29]: Proprotein convertase inhibitor demonstrates dual anti-glioma and macrophage reactivation activity
- [41]: PRSS12 prognostic marker in glioblastoma multiforme

## Program: Signal Transduction Modulation and cAMP/Calcium Signaling
This program encompasses genes regulating intracellular signal transduction, including phosphodiesterases, calcium signaling proteins, and kinase regulators that modulate cellular responses to growth factors, neuropeptides, and stress. These genes fine-tune signaling intensity and duration controlling proliferation, differentiation, and survival. Dysregulation of signal transduction creates sustained pro-tumoral signaling.

**Predicted impacts**
- Sustained proliferative signaling through reduced second messenger turnover
- Enhanced growth factor responsiveness through cAMP/calcium modulation
- Increased invasive capacity through kinase-dependent cytoskeletal remodeling
- Altered differentiation responses through calcium signaling dysregulation
- Therapeutic resistance through signaling pathway redundancy

**Evidence summary**
This program identifies signal transduction regulators dysregulated in GBM. PDE4A and PDE7B degrade cAMP and cGMP, controlling signal duration and intensity. PRKG2 (protein kinase G2) is cGMP-dependent kinase involved in calcium signaling. CALCRL (calcitonin receptor-like receptor) participates in GPCR signaling. ARPP21 is a kinase regulator involved in phosphorylation dynamics. Together these genes create multiple layers of signal modulation affecting GBM proliferation and invasion.

**Atomic biological processes**
- phosphodiesterase-mediated cAMP and cGMP degradation. Genes: PDE4A, PDE7B, PRKG2
  - [20]: cAMP signaling pathway and related effectors impact cancer incidence and development; phosphodiesterases regulate second messenger levels
- calcium/calmodulin-dependent signaling. Genes: CALCRL, PRKG2
  - [4]: Ca2+ signaling critical for ion channel activation and cell cycle progression; calmodulin-dependent processes regulate glioma migration
- kinase regulation and phosphorylation dynamics. Genes: ARPP21
  - [50]: CDK inhibitor AT7519 arrests cell cycle at G1 and G2 phases by targeting CDK1/2 and their phosphorylation

**Atomic cellular components**
- phosphodiesterase enzyme complexes. Genes: PDE4A, PDE7B
  - [20]: PDE family enzymes degrade cAMP and cGMP regulating signaling intensity and duration
- calcium regulatory proteins. Genes: CALCRL, PRKG2
  - [4]: Calmodulin and calcium-binding proteins regulate glioma cell migration and invasion

**Required genes (not in input)**
- Genes: GNAS, ADCY, GPCR downstream effectors, CaMKII
  - [20]: G protein-coupled receptor signaling machinery required for cAMP pathway completion

**Program citations**
- [20]: Review on cAMP signaling in cancer showing impact on incidence and development

## Program: Endosomal Recycling and Receptor Trafficking
This program integrates genes regulating endosomal membrane trafficking and receptor recycling that control cell surface receptor density and signaling duration. These genes mediate the balance between receptor recycling to the cell surface (sustaining signaling) versus degradation in lysosomes (attenuating signaling). Dysregulation of endosomal recycling in GBM promotes sustained growth factor signaling and therapeutic resistance.

**Predicted impacts**
- Sustained EGFR and other RTK signaling through increased cell surface density
- Enhanced proliferative signaling via ERK and Akt pathway amplification
- Reduced responsiveness to growth factor withdrawal
- Therapeutic resistance to receptor-targeting drugs through increased surface density
- Increased invasive capacity via sustained signaling

**Evidence summary**
This program identifies dysregulation of receptor trafficking in GBM. Recent systematic analysis reveals that endosomal recycling regulators are dysregulated in glioblastoma, creating an 8-gene prognostic signature predictive of outcome. Upregulation of recycling shifts the balance toward sustained signaling rather than degradation, particularly important for EGFR which is amplified or mutated in 40-60% of GBMs. MYRIP (myosin VIIa-regulated intracellular transport) participates in endosomal recycling dynamics. ATP13A5 (P5A ATPase) maintains pH gradients in vesicular compartments critical for recycling function. This program explains sustained proliferative signaling characteristic of GBM.

**Atomic biological processes**
- endosomal recycling pathway regulation. Genes: MYRIP, ATP13A5
  - [45]: Endosomal recycling regulators dysregulated in glioblastoma; upregulation shifts balance between recycling and degradation toward recycling, amplifying RTK signaling
- receptor trafficking and subcellular localization. Genes: MYRIP
  - [45]: 40-60% of GBMs carry EGFR mutations/amplifications; upregulated endosomal recycling increases EGFR at cell surface, sustained proliferative signaling

**Atomic cellular components**
- recycling endosome components. Genes: MYRIP, ATP13A5
  - [45]: Regulators of endosomal recycling pathway components dysregulated in glioblastoma

**Required genes (not in input)**
- Genes: RAB4, RAB10, RAB11, EPS15, KIF5A, EHD2
  - [45]: Key endosomal recycling regulators identified in systematic analysis but not present in input gene list; dysregulation associated with GBM grade and prognosis

**Program citations**
- [45]: Systematic computational analysis of endosomal recycling pathway in glioblastoma identifying dysregulated regulators and prognostic signature

## Bibliography
1. Nomura M, Spitzer A, Johnson KC, Garofano L, Nehar-belaid D, Galili DN, et al.. The multilayered transcriptional architecture of glioblastoma ecosystems. Nature Genetics [Internet]. 2025May;57(5). Available from: https://www.nature.com/articles/s41588-025-02167-5
2. Tian Y, Wang Z, Yang F, Zhang W, Li J, Yang L, et al.. Olig1/2 Orchestrates Progenitor Cell Fates during Mammalian Cortical Gliogenesis and Gliomagenesis. Nature Communications [Internet]. 2025Nov5;16(1). Available from: https://www.nature.com/articles/s41467-025-64753-9
3. Uchurappa M, Tapan KB, Kumaravel S. Integrative analysis of cell adhesion molecules in glioblastoma identified prostaglandin F2 receptor inhibitor (PTGFRN) as an essential gene.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9188228/
4. Remco JM. Ion channels in glioblastoma.. ISRN neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
5. Salvatore M, Grazia M, Rina DB, Lucia L, Pierpaolo M, Federica F, et al.. The Extracellular Matrix in Glioblastomas: A Glance at Its Structural Modifications in Shaping the Tumoral Microenvironment-A Systematic Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
6. Available from: https://maayanlab.cloud/Harmonizome/gene_set/MEWO/COSMIC+Cell+Line+Gene+Mutation+Profiles
7. Katarzyna Z, Barbara W, Malwina S-Ł, Marta K, Sławomir J, Agnieszka O, et al.. Diamond Nanoparticles Suppress Migration of T98G Glioblastoma Cells by Targeting ECM-Integrin Interactions and Intracellular Signaling, Leading to Extensive Proteome Alterations.. Nanotechnology, science and applications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41210309/
8. Lisa G, Carola NJ, Sonja K, Sushilla van S, Bernhard E, Christine P, et al.. Fibroblast growth factor receptor 4 promotes glioblastoma progression: a central role of integrin-mediated cell invasiveness.. Acta neuropathologica communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/35484633/
9. Harpreet K, Polly JP-M, Susan MB-G, Amber EK-F, James PB, Andrew ES, et al.. Cadherin-11, a marker of the mesenchymal phenotype, regulates glioblastoma cell migration and survival in vivo.. Molecular cancer research : MCR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3307867/
10. Anne-Laure T, Christelle B, Sandrine R, Sébastien S, Christine D, Pieter D, et al.. Identification of OLIG2 as the most specific glioblastoma stem cell marker starting from comparative analysis of data from similar DNA chip microarray platforms.. Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/25384509/
11. Riccardo B, Angela B. Role of Notch Signaling Pathway in Glioblastoma Pathogenesis.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
12. Ryo U, Kazunari Y, Yutaka K, Takeshi K, Masahiro T. Expression of a transcriptional factor, SOX6, in human gliomas.. Brain tumor pathology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/15696967/
13. Samir V, Mirko HHS. Migration-Associated Transportome and Therapeutic Potential in Glioblastoma Multiforme (GBM).. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10340178/
14. Truman K, Tina H, Jin Q, Shejuan A, Noah B, Scott C, et al.. LIN28B and Let-7 in Diffuse Midline Glioma: A Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10296230/
15. Available from: https://www.ncbi.nlm.nih.gov/books/NBK470001/
16. Signe RM, Derya A, Thomas U, Hans SP, Kirsten G, Helle B, et al.. DNA Methylation Levels of the ELMO Gene Promoter CpG Islands in Human Glioblastomas.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5877540/
17. Anne-Marie L, Olivier C, Timothy AC, Giuleta J, Andréanne G, Yohan B, et al.. High FA2H and UGT8 transcript levels predict hydroxylated hexosylceramide accumulation in lung adenocarcinoma.. Journal of lipid research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/31409741/
18. Weiwei C, Xia L, Youqin J, Daguang N, Longfei Y, Jixiang W, et al.. Pancancer analysis of the correlations of HS6ST2 with prognosis, tumor immunity, and drug resistance.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628205/
19. Available from: https://patents.google.com/patent/JP7162406B1/en
20. Muhammad BA, Abdullah AAA, Salman UI, Joon-Seok L, Young-Sup L. cAMP Signaling in Cancer: A PKA-CREB and EPAC-Centric Approach.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9266045/
21. Zhang C, Zhao N, Khan R, Hung M-yang, Zhang C, Wang S, et al.. The prognostic significance of androgen receptor expression in gliomas. Scientific Reports [Internet]. 2024Sep27;14(1). Available from: https://www.nature.com/articles/s41598-024-72284-4
22. Xingchun G, Yajing M, Na G, Zhifang H, Fengrui H, Dou L, et al.. Disrupted in schizophrenia 1 (DISC1) inhibits glioblastoma development by regulating mitochondria dynamics.. Oncotarget [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/27852062/
23. Véronique D-T, Ivan B, Sophie V, Anne L, Claude-Alain M, Francis C, et al.. Differential distribution of erbB receptors in human glioblastoma multiforme: expression of erbB3 in CD133-positive putative cancer stem cells.. Journal of neuropathology and experimental neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3173752/
24. Jessica A, Elisabeth S, Matthias W, Olga E, Franziska F, Michael W. Myrf guides target gene selection of transcription factor Sox10 during oligodendroglial development.. Nucleic acids research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7026603/
25. Florence B, Sabrina R, Daniela Z, Enrico M, Daniel H, Marianne B-L, et al.. SMOC1 is a tenascin-C interacting protein over-expressed in brain tumors.. Matrix biology : journal of the International Society for Matrix Biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/21349332/
26. Wenxiu T, Ping W, Zhimei W, Huimin Q, Junhong D, Hongmei W. Phospholipid Phosphatase 4 as a Driver of Malignant Glioma and Pancreatic Adenocarcinoma.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8669803/
27. Martin AP, Marsha JM, Eva-Maria S, Annette L, Fabian P, Alexander B. Function of carbonic anhydrase IX in glioblastoma multiforme.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3480266/
28. Satyanarayana R, Chaitanya SS, Suresh KI, Thiyagarajan R, Chandrabose S, Abass KS, et al.. GPR17 in Glioblastoma: Structure, Ligand Interactions, and Therapeutic Targeting. ACS Omega [Internet]. 2025Sep29;10(40). Available from: https://pubs.acs.org/doi/10.1021/acsomega.5c04079
29. Mélanie R, Marie D, Soulaimane A, Firas K, Emilie LR, Annie D, et al.. The Role of a Proprotein Convertase Inhibitor in Reactivation of Tumor-Associated Macrophages and Inhibition of Glioma Growth.. Molecular therapy oncolytics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7152595/
30. Available from: https://www.ncbi.nlm.nih.gov/gene/6869
31. Zhixiao L, Rongjun Q, Jiadong Z, Xiwen S. MiR-218-5p targets LHFPL3 to regulate proliferation, migration, and epithelial-mesenchymal transitions of human glioma cells.. Bioscience reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6395304/
32. Hyunkoo K, Haksoo L, Kyeongmin K, Eunguk S, Byeongsoo K, JiHoon K, et al.. DGKB mediates radioresistance by regulating DGAT1-dependent lipotoxicity in glioblastoma.. Cell reports Medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9873821/
33. Rosemary L, Chiara C, Jianing C, Kalpit S, Eleonora M, Nektarios KM, et al.. PDGF-R inhibition induces glioblastoma cell differentiation via DUSP1/p38. Oncogene [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9076540/
34. Jimena C, Lauren B, Jared TA, Jason M, Catalina L-C. Understanding the glioblastoma tumor microenvironment: leveraging the extracellular matrix to increase immunotherapy efficacy.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
35. José RA, Laure A, Peggy T, Roxane B, Claire B, Ludovic R, et al.. The kinesin Kif21b regulates radial migration of cortical projection neurons through a non-canonical function on actin cytoskeleton.. Cell reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37418324/
36. Mei C, Qingming S. Extracranial metastasis of glioblastoma with genomic analysis: a case report and review of the literature.. Translational cancer research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36093544/
37. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=131544
38. Lijun L, Ruiying G, Weizhong H, Fang Z, Ruixia W. Clinical Significance of NKD Inhibitor of WNT Signaling Pathway 1 (NKD1) in Glioblastoma.. Genetics research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36969985/
39. Sabrina S, Markus AK, Ernst RW, Katrin W. The Emerging Physiological Role of AGMO 10 Years after Its Gene Identification.. Life (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7911779/
40. Raquel M-G, María JU-N, Patricia G-T, Ricardo P-A, Gaspar R, Pedro P-B, et al.. BCAS1 defines a heterogeneous cell population in diffuse gliomas.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10812236/
41. Available from: https://www.proteinatlas.org/ENSG00000164099-PRSS12
42. Available from: https://maayanlab.cloud/Harmonizome/gene_set/MITF/CHEA+Transcription+Factor+Targets
43. Dongoh K, Lars GJH, Martin H, Patrik E. Glioblastoma cytotoxicity conferred through dual disruption of endolysosomal homeostasis by Vacquinol-1.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8577523/
44. Rama RM, Sreelatha G, Kiranmai A, Bharathi G, Christopher SG, Jasti SR. Knockdown of cathepsin B and uPAR inhibits CD151 and α3β1 integrin-mediated cell adhesion and invasion in glioma.. Molecular carcinogenesis [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3525767/
45. Luke JJ, Andrew JL. A systematic computational analysis of the endosomal recycling pathway in glioblastoma.. Biochemistry and biophysics reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11024495/
46. Alberto V, Nadia T, Gandino M, Fabrizio G, Massimiliano C, Orazio P, et al.. Different states of stemness of glioblastoma stem cells sustain glioblastoma subtypes indicating novel clinical biomarkers and high-efficacy customized therapies.. Journal of experimental & clinical cancer research : CR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10512479/
47. Matthew DS, Rui PG, Lixin W, Jungeun K, Lauren KR, Shambhavi S, et al.. Premalignant Oligodendrocyte Precursor Cells Stall in a Heterogeneous State of Replication Stress Prior to Gliomagenesis.. Cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8137536/
48. Yasuo I. Epithelial-mesenchymal transition in glioblastoma progression.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4774466/
49. Itamar F, Aleli S, Verónica P de la C, Tamara M-G, Javier ANC, Rubén F, et al.. Von Hippel-Lindau/Hypoxia Inducible Factor Axis in Glioblastoma.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12564729/
50. Wenpeng Z, Liang Z, Yaya Z, Zhengye J, Hanwen L, Yuanyuan X, et al.. The CDK inhibitor AT7519 inhibits human glioblastoma cell growth by inducing apoptosis, pyroptosis and cell cycle arrest.. Cell death & disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9829897/
