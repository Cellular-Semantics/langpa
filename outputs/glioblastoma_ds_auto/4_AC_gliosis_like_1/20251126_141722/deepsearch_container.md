# Gene Program Markdown Report

## Context
- Cell type: Glioblastoma multiforme cells; tumor-associated astrocytes; infiltrating immune cells
- Disease: Glioblastoma multiforme (GBM); malignant glioma
- Tissue: Central nervous system; brain

## Input Genes
AQP1, ANOS1, LIX1, CD38, RASL12, KCNN3, SERPINA3, GFAP, FAM189A2, BBOX1, NPSR1, ITPKB, CFI, LINC01094, ID3, FBLN5, CFAP54, DAAM2, ADAMTS8, GGT5, SLC14A1, RPE65, MASP1, SLCO1C1, AC092131.1, ... (99 total)

## Program: Aquaporin-mediated osmotic water transport and migration
Water channel proteins (AQP1, AQP4) regulate osmotic gradients essential for glioma cell migration and edema formation. AQP4 localizes to leading edges of migrating cells and lamellipodia, facilitating volume changes during invasion through narrow extracellular spaces. Coordinated with ion transporters (KCNN3, ATP1A2, SLC14A1) that maintain ion gradients driving osmotic water flux. Dysregulation contributes to both tumor-associated vasogenic edema and enhanced invasive capability.

**Predicted impacts**
- Enhanced directional cell migration through osmotic volume regulation
- Increased infiltration of tumor cells through brain parenchyma
- Promotion of vasogenic edema formation at tumor-brain interface
- Support for invasive cell membrane protrusions (lamellipodia formation)
- Maintenance of perivascular migration along blood vessel corridors

**Evidence summary**
Multiple lines of evidence demonstrate that aquaporin-mediated water transport is upregulated in gliomas and essential for invasive phenotype. AQP4 shows strong redistribution at tumor cell leading edges, co-localizing with ion channels (KCC1, CLC2) to facilitate coordinated water and ion extrusion that enables cell volume changes required for invasion through narrow extracellular spaces. The coupling of water channels with intermediate-conductance K+ channels (KCNN3) and Na+/K+-ATPase creates osmotic gradients driving migration. This program is specifically dysregulated in glioma compared to normal brain tissue.

**Atomic biological processes**
- osmotic water transport and cell volume regulation. Genes: AQP1, AQP4
  - [1]: AQP4 redistribution and upregulation in glioma cells; high water flux capacity; association with KCl-water extrusion enhancing cell invasion
  - [4]: AQP1 induction by glycolysis; role in tumor edema and cell migration through osmotic gradient mechanisms
- ion channel activity and electrical signaling. Genes: KCNN3, ATP1A2, SLC14A1
  - [25]: KCNN3 (KCa3.1) channels modulate glioma cell infiltration; involved in CXCL12-induced migration
  - [41]: ATP1A2 (Na+/K+-ATPase) consumes 20% of astrocytic ATP; maintains ion gradients essential for cell migration
  - [29]: SLC14A1 (UT-B) expressed in astrocytes; facilitates urea and water transport

**Atomic cellular components**
- plasma membrane water and solute transporters. Genes: AQP1, AQP4, KCNN3, ATP1A2, SLC14A1
  - [1]: AQP4 expression at leading edge of migratory glioma cells; co-localization with CLC2 and KCC1 ion channels

**Program citations**
- [1]: Comprehensive review of AQP4 roles in glioma migration, invasive phenotype, and cell volume changes
- [4]: AQP1 upregulation by glycolysis; localization in perivascular regions supporting invasive phenotype
- [25]: KCNN3 inhibition reduces glioma infiltration and astrogliosis in vivo

## Program: Aerobic glycolysis-dependent nutrient acquisition
Glioblastomas exhibit constitutive aerobic glycolysis despite adequate oxygen (Warburg effect), characterized by upregulation of glycolytic enzymes and glucose transporters. PFKFB3 is the most highly expressed glycolytic regulator in GBM, controlling the rate-limiting step through F-2,6-BP production. This metabolic state is driven by hypoxic microenvironments and genetic alterations (EGFR amplification, PTEN loss). Elevated glycolysis supports both energy production and anabolic biosynthesis, driving tumor cell proliferation and survival. This program is inseparable from invasion, as perivascular glioma cells show peak glycolytic enzyme expression including AQP1, LDH, and cathepsin B.

**Predicted impacts**
- Enhanced ATP production supporting tumor growth and proliferation
- Increased lactate and H+ secretion promoting acidic tumor microenvironment
- Support for anabolic pathways (nucleotide, lipid, amino acid synthesis)
- Hypoxia adaptation and maintenance of hypoxic metabolic state
- Coupling with angiogenic escape mechanisms to overcome anti-VEGF therapy

**Evidence summary**
PFKFB3 emerges as a central node controlling glycolytic flux in GBM. Its expression is induced by hypoxia through multiple mechanisms including O-GlcNAcylation and ERK phosphorylation. PFKFB3 inhibitors (3-PO, PFK15, KAN0438757) significantly reduce GBM cell viability and migration in preclinical models. Combination strategies targeting PFKFB3 with VEGF inhibitors (bevacizumab) show synergistic effects in extending survival and improving drug delivery. The program is further supported by upregulation of AQP1 in perivascular regions showing peak glycolytic enzyme expression, suggesting metabolic zonation within tumors.

**Atomic biological processes**
- glucose uptake and phosphorylation. Genes: PFKFB3
  - [40]: GLUT1 and GLUT3 upregulation in GBM; silencing reduces glioma stem cell tumor sphere formation
- glycolytic pathway flux regulation. Genes: PFKFB3
  - [37]: PFKFB3 O-GlcNAcylation essential for cancer cell division under hypoxia; controls PFKFB3-G3BP2-P27 signaling
  - [40]: PFKFB3 inhibition decreases glycolysis rate and tumor cell proliferation; combination with VEGF inhibitors prolongs survival
- lactate production and extracellular acidification. Genes: AQP1
  - [4]: AQP1 induction correlates with LDH expression in perivascular glioma regions; supports acidification of extracellular milieu

**Atomic cellular components**
- glycolytic enzyme complexes. Genes: PFKFB3
  - [40]: PFKFB3 is rate-limiting enzyme in glycolysis; most highly expressed in GBM

**Required genes (not in input)**
- Genes: GLUT1, GLUT3, LDH, HIF1A, LDHA
  - [40]: GLUT1/GLUT3 glucose transporters essential for nutrient uptake; upregulated in GBM
  - [4]: LDH (lactate dehydrogenase) co-induced with AQP1 in perivascular glioma regions

**Program citations**
- [37]: Hypoxia-induced PFKFB3 O-GlcNAcylation maintains cancer cell division
- [40]: Comprehensive review of PFKFB3-targeted therapy approaches in GBM
- [4]: AQP1 induction by glycolysis and perivascular metabolic zonation

## Program: Extracellular matrix remodeling and invasive phenotype
Glioma cells exhibit dynamic ECM remodeling through coordinated synthesis (HAS2, HAS3 driving hyaluronic acid accumulation) and degradation (ADAMTS8, TIMP3, matrix metalloproteinases). CD44 serves as the primary HA receptor, engaging osteopontin (OPN/SPP1) signaling to promote migration, invasion, and stemness. IGFBP7 promotes glioma cell migration through AKT-ERK pathway activation. Increased ECM deposition (particularly brevican/BCAN and other proteoglycans) creates a denser, more resistant tumor microenvironment. HAS2 expression correlates with poor prognosis and GBM subtype (IDH-WT, non-1p/19q codeletion). Loss of ADAMTS8 (an inhibitory protease) contributes to glioma progression.

**Predicted impacts**
- Enhanced tumor cell migration and invasion through remodeled ECM
- Increased stemness and self-renewal via CD44-osteopontin signaling
- Promotion of epithelial-mesenchymal transition (EMT)
- Increased resistance to anti-angiogenic therapy through altered ECM composition
- Support for perivascular migration and vascular co-option
- Enhanced mechanotransduction signaling through integrin-FAK pathways

**Evidence summary**
ECM remodeling represents a core pathological feature of GBM progression. HAS2 upregulation drives excessive hyaluronic acid (HA) accumulation, which promotes migration and invasion through CD44 receptors. CD44+ glioma cells display enhanced interaction with macrophages via osteopontin signaling, creating bidirectional cross-talk between tumor and immune cells. ITGB4 (integrin β4) is specifically upregulated in GBM and predicts poor prognosis, promoting migration through FAK-PI3K/AKT and MAPK activation. IGFBP7 expression correlates with tumor grade and localizes to perivascular regions, supporting invasion along blood vessels. The balance between matrix synthesis and degradation is controlled by ADAMTS proteases and TIMPs; loss of ADAMTS8 (an inhibitory protease) contributes to disease progression.

**Atomic biological processes**
- hyaluronic acid synthesis and accumulation. Genes: HAS2
  - [13]: HAS2 elevated in GBM; promotes proliferation, migration, invasion; associated with poor survival
  - [16]: HAS3 upregulated in GBM; silencing inhibits proliferation, migration, invasion; blocks autophagy flux
- CD44-mediated ECM receptor signaling. Genes: CD44
  - [2]: CD44 expression elevated in GBM; astrocytes upregulate glioma CD44; CD44+ cells interact with M1 macrophages via osteopontin
  - [16]: CD44 antibody blocking inhibits glioma cell proliferation; blocks autophagy and cell cycle
- matrix metalloproteinase regulation. Genes: TIMP3, ADAMTS8, ID4
  - [19]: Id4 suppresses MMP2-mediated invasion by direct inhibition of Twist1; Id4 expression correlates with GBM patient survival
  - [7]: TIMP3 locally balances MMP activity; expression associated with prognosis
- integrin-mediated cell adhesion and migration. Genes: ITGB4
  - [9]: ITGB4 promotes tumor migration and invasion through FAK-PI3K/AKT and MAPK pathways; released from hemidesmosomes in cancer
  - [12]: ITGB4 upregulated in GBM; predicts poor prognosis; interacts with tumor-associated fibroblasts
- IGF binding protein signaling in migration. Genes: IGFBP7
  - [39]: IGFBP7 expression correlates with glioma grade; promotes migration through AKT-ERK pathway; associated with laminin-stained GBM vessels

**Atomic cellular components**
- extracellular matrix proteoglycans and glycosaminoglycans. Genes: BCAN, HAS2, FBLN5, PAPLN
  - [33]: Brevican (BCAN) most abundantly detected proteoglycan in adult and pediatric gliomas
  - [13]: Hyaluronic acid (HA) vital component of ECM; upregulated in GBM; stimulates migration and invasion
- adhesion molecules and integrin receptors. Genes: ITGB4, CD44
  - [9]: ITGB4 (integrin β4) functions as mechanosensor; mediates bidirectional exchange between intracellular and extracellular matrices

**Program citations**
- [13]: HAS2 promotes glioma malignancy and suppresses ferroptosis
- [2]: CD44 as prognostic factor in glioma; interaction with stromal cells in TME
- [12]: ITGB4 upregulation in lower-grade glioma; association with immune infiltration
- [39]: IGFBP7 mediates glioma cell migration through AKT-ERK pathway

## Program: Complement system activation and immune modulation
The complement cascade is activated within gliomas through multiple pathways (classical via C1q, alternative, and lectin pathways via MASP1/MASP2/COLEC12). Complement components C3 and C5 generate potent anaphylatoxins (C3a, C5a) that promote M2 macrophage polarization and immunosuppression. C3a-C3aR signaling in glioma stem cells (GSCs) maintains stemness through STAT-3 and Wnt/SOX2 pathways. CD38 functions as an ectoenzyme converting NAD+ to immunosuppressive adenosine and ADPR. CHI3L2 (YKL40) is secreted by tumor and immune cells, promoting inflammatory responses and inducing CD8+ T cell apoptosis. This program collectively shifts the immune microenvironment toward M2/immunosuppressive phenotypes.

**Predicted impacts**
- Polarization of infiltrating macrophages/microglia toward M2 (immunosuppressive) phenotype
- Maintenance of glioma stem cell phenotype through C3a-STAT3-SOX2 signaling
- Suppression of CD8+ T cell function and promotion of regulatory T cell (Treg) differentiation
- Promotion of tumor angiogenesis through complement-endothelial cell interactions
- Enhanced resistance to complement-mediated lysis via CD46/CD55/CD59 upregulation
- Conversion of adaptive immune responses from Th1 to Th2/immunosuppressive phenotype

**Evidence summary**
Complement activation represents a critical mechanism of immune evasion in GBM. C3 expression increases with glioma grade, is associated with worse survival, and preferentially localizes to hypoxic tumor regions. C3a/C3aR signaling maintains GSC stemness through STAT-3 and Wnt/SOX2 pathways, while simultaneously promoting M2 macrophage polarization. CD38 functions as an ectoenzyme converting NAD+ to immunosuppressive metabolites; CD38 inhibition with FDA-approved therapeutics extends survival in preclinical models. CHI3L2 (YKL40) is secreted by both tumor and immune cells, directly inducing CD8+ T cell apoptosis. The complement lectin pathway (MASP1, COLEC12) is upregulated in gliomas and provides an alternative route to C3 activation. Gliomas upregulate complement regulators (CD46, CD55, CD59) to resist complement-mediated lysis.

**Atomic biological processes**
- complement classical pathway activation. Genes: C3, MASP1
  - [31]: C1q highly expressed in gliomas; promotes tumor proliferation and invasion; negatively correlates with survival
  - [32]: Glioma cells express complement regulators (CD46, CD55, CD59); resist complement-mediated lysis
- complement lectin pathway activation. Genes: MASP1, COLEC12, CFI
  - [55]: MBL-MASP pathway components (MBL, MASP1, MASP3) highly expressed in glioma cell lines
  - [56]: COLEC12 functions as pattern-recognition molecule; activates complement alternative pathway
- C3a-C3aR signaling in glioma stem cells. Genes: C3
  - [31]: C3a-C3aR interaction activates STAT-3; increases Wnt2b and SOX2 expression; maintains GSC phenotype
  - [34]: Hypoxia-induced C3 expression; C3a promotes M2 macrophage polarization; C3aR antagonism prolongs survival
- CD38-mediated immunosuppression through adenosine production. Genes: CD38
  - [3]: CD38 deficiency attenuates glioma progression; associated with increased cell death and decreased MMP expression
  - [6]: CD38 inhibition important in pre-recurrent GBM; conventional therapies increase CD38 activity in recurrent tumors
- chitinase-like protein immune modulation. Genes: CHI3L2
  - [45]: CHI3L2 induces apoptosis of CD8+ T cells; high expression associated with poor prognosis in glioma
  - [48]: CHI3L1 (YKL40) promotes activation of macrophages; upregulates pro-inflammatory cytokines; increases tumor-infiltrating immune cells

**Atomic cellular components**
- complement cascade proteins. Genes: C3, MASP1, COLEC12, CFI
  - [31]: C1q, C3, C5 components; convertases C3b, C5b
- complement receptor and anaphylatoxin receptor signaling. Genes: C3
  - [31]: C3aR and C5aR (CD88) mediate G-protein coupled receptor signaling
- ectoenzymes and surface receptors. Genes: CD38, CHI3L2
  - [3]: CD38 ectoenzyme uses NAD+ as substrate; generates ADPR and cADPR

**Required genes (not in input)**
- Genes: C5, C1Q, CD46, CD55, CD59, C5AR1
  - [31]: C1q initiates classical pathway; C5 generates C5a for immune cell recruitment
  - [32]: CD46, CD55, CD59 complement membrane regulators highly expressed in gliomas

**Program citations**
- [31]: Complement system in glioblastoma multiforme; C3a maintains GSC phenotype
- [34]: Hypoxia-induced complement C3 promotes M2 macrophage polarization; C3aR antagonism extends survival
- [3]: CD38 deficiency attenuates glioma progression
- [45]: CHI3L2 is prognostic biomarker in glioma; induces CD8+ T cell apoptosis

## Program: Glioma stem cell self-renewal and maintenance
Glioma stem cells (GSCs) reside in perivascular and hypoxic niches where they maintain multipotency and self-renewal capacity. Endothelin-3 (EDN3) and endothelin receptor B (EDNRB) autocrine signaling is essential for GSC maintenance; blocking EDNRB induces apoptosis and impairs tumor-sphere formation. HOPX marks radial progenitor-like cells in glioma. CD44 and osteopontin (OPN) signaling within the perivascular niche promotes stem cell phenotypes and tumor growth. Complement C3a signaling through C3aR maintains GSCs via STAT-3 and Wnt/SOX2 activation. IGFBP7 and growth factor signaling support GSC migration along blood vessels. ID3 and ID4 (inhibitors of differentiation) regulate GSC proliferation and maintain undifferentiated state.

**Predicted impacts**
- Maintenance of undifferentiated GSC phenotype and multipotency
- Enhanced self-renewal capacity and tumor-sphere formation
- Increased resistance to differentiation-inducing signals
- Support for perivascular localization and niche interaction
- Enhanced survival signaling through multiple pathways (EDN, complement, CD44)
- Promotion of tumor recurrence through GSC persistence

**Evidence summary**
Glioma stem cell maintenance depends on coordinated signaling within specialized microenvironmental niches. Autocrine endothelin-3 (EDN3) signaling through EDNRB is both necessary and sufficient for GSC phenotype maintenance; blocking EDNRB induces apoptosis and loss of self-renewal capacity. CD44 expression in GSCs engages osteopontin (OPN) signaling to promote stemness within the perivascular niche. Complement component C3 generated by GSCs activates C3aR to drive STAT-3 and Wnt/SOX-2 pathways that reinforce stemness. HOPX marks a subset of radial progenitor-like GSCs. This program represents a critical mechanism of treatment resistance, as GSCs survive conventional therapies and drive recurrence.

**Atomic biological processes**
- endothelin signaling for stemness maintenance. Genes: EDNRA, EDNRB
  - [15]: Autocrine EDN3/EDNRB signaling essential for GSC maintenance; blockade leads to apoptosis and loss of tumor-sphere formation
  - [18]: Hypoxia upregulates EDN1, EDNRA, EDNRB, and ECE1; hypoxia-ERN1 axis drives endothelin system expression
- CD44-osteopontin perivascular niche signaling. Genes: CD44
  - [2]: OPN-CD44 signaling in glioma perivascular niche promotes cancer stem cell phenotypes; SPP1 (osteopontin) negatively correlates with survival
- complement-mediated GSC maintenance. Genes: C3
  - [31]: Autocrine C3a from GSCs activates C3aR; increases Wnt2b and SOX-2 expression; maintains stemness
  - [34]: C3aR antagonism reduces glioma stem cell self-renewal capability
- inhibitor of differentiation transcription factors. Genes: ID3, ID4
  - [22]: ID4 expression in glioblastoma; inhibitor of differentiation protein family involved in cell cycle control and tumorigenesis

**Atomic cellular components**
- perivascular niche microenvironment. Genes: CD44, EDNRA, EDNRB, HOPX
  - [17]: Endothelial-secreted Endocan activates PDGFRA; promotes proliferation and migration; GBM cells in perivascular niche maintain GSC phenotype
- hypoxic microenvironment sensing. Genes: EDNRA, EDNRB, C3
  - [15]: EDN3/EDNRB signaling expressed in response to hypoxia in GSCs

**Program citations**
- [15]: Autocrine endothelin-3/EDNRB signaling maintains glioma stem cells
- [2]: CD44-osteopontin signaling promotes GSC phenotype in perivascular niche
- [31]: Complement C3a maintains GSC phenotype through STAT-3 and Wnt signaling

## Program: Tumor-associated astrocyte and glial cell reprogramming
Peritumoral and tumor-resident astrocytes undergo reactive transformation (gliosis) characterized by GFAP upregulation. Tumor-associated astrocytes (TAAs) display distinct morphology and transcriptomic profiles depending on anatomical location (tumor core, periphery, perivascular niche, border). ALDH1L1 marks gliogenic precursors and mature astrocytes. TAAs enhance glioma cell viability and migration by upregulating CD44 expression in tumor cells through paracrine mechanisms. Reactive astrocytes modulate immune cell recruitment through purinergic signaling (ATP/adenosine metabolism, CD73). This program represents a critical stromal-tumor interaction that supports malignancy.

**Predicted impacts**
- Enhanced glioma cell migration and viability through astrocyte-derived paracrine factors
- Upregulation of stemness-promoting genes (CD44) in adjacent tumor cells
- Promotion of M1 macrophage infiltration and immune cell recruitment
- Increased extracellular adenosine production creating immunosuppressive microenvironment
- Support for perivascular tumor cell positioning and angiogenic cooperation
- Modulation of blood-brain barrier permeability

**Evidence summary**
Tumor-associated astrocytes (TAAs) play a critical supporting role in glioma progression through bidirectional cross-talk with tumor cells and immune cells. Spatial transcriptomics reveals distinct TAA phenotypes in tumor core (perivascular TAAs expressing CD44 and Tenascin-C) versus tumor periphery (morphologically resembling reactive astrocytes). Astrocytes enhance glioma CD44 expression, promoting migration and stemness through paracrine signaling. TAAs display heterogeneous transcriptomic profiles reflecting their adaptive responses to microenvironmental cues. Purinergic signaling through ATP and adenosine creates an immunosuppressive microenvironment. This program highlights the complex three-way interaction between tumor cells, stromal astrocytes, and immune cells.

**Atomic biological processes**
- reactive astrocyte transformation and GFAP upregulation. Genes: GFAP, ALDH1L1
  - [5]: Tumor-associated astrocytes (TAAs) exhibit spatially organized gene expression; distinct phenotypes in tumor core, periphery, and perivascular niches
  - [24]: GFAP expression in white matter fibrous and reactive astrocytes; ALDH1L1 marks gliogenic precursors
- TAA-mediated enhancement of glioma malignancy. Genes: GFAP, CD44
  - [2]: Astrocytes enhance glioma CD44 expression; promote glioma cell migration and viability; coordinate with M1 macrophages via osteopontin signaling
- purinergic signaling in astrocyte-immune cell cross-talk. Genes: GFAP, ATP1A2
  - [38]: ATP released by astrocytes; adenosine (ADO) produced by CD73; A2A receptor activation promotes immunosuppressive A2-like astrocyte phenotype

**Atomic cellular components**
- intermediate filament networks. Genes: GFAP
  - [24]: GFAP cytoskeletal protein; primary marker of astrocyte cell type
- astrocyte metabolic enzymes. Genes: ALDH1L1
  - [21]: ALDH1L1 folate metabolic enzyme; bona fide astrocyte marker; broadly expressed in fibrous and protoplasmic astrocytes

**Program citations**
- [5]: Spatial transcriptomics reveals heterogeneous tumor-associated astrocyte phenotypes
- [2]: Astrocytes enhance glioma CD44 expression and promote malignancy
- [38]: Purinergic signaling modulates astrocyte polarization and tumor growth

## Program: Gap junction communication and chemoresistance
Connexin 43 (GJA1) forms gap junctions enabling intercellular communication but also confers chemoresistance to temozolomide (TMZ) and other chemotherapeutic agents. Cx43 is highly expressed in a subpopulation of GBM; Cx43 mRNA strongly correlates with poor prognosis and chemoresistance. Cx43 activates PI3K (specifically PIK3CB/p110β) signaling independent of its channel function (non-channel function). CD38 ectoenzyme activity may modulate adenosine levels affecting gap junction function. Combining Cx43 inhibition (αCT1 peptide) with PI3K inhibitors (TGX-221, GSK2636771) sensitizes GBM to TMZ.

**Predicted impacts**
- Enhanced intercellular communication enabling collective tumor behavior
- Activation of PI3K/AKT survival signaling independent of chemotherapy
- Increased resistance to temozolomide and other chemotherapeutic agents
- Poor treatment response and shortened progression-free survival
- Maintenance of tumor cell viability despite DNA-damaging therapies

**Evidence summary**
Connexin 43 (GJA1) emerges as a critical determinant of GBM chemoresistance, particularly to temozolomide. Cx43 is highly expressed in a subpopulation of GBM, and its mRNA levels show strong correlation with poor prognosis and treatment resistance. Mechanistically, Cx43 confers chemoresistance through non-channel functions, specifically by activating PI3K (particularly the p110β catalytic isoform). This activation is MGMT-independent, explaining why some MGMT-deficient tumors still show chemoresistance. Combining Cx43 inhibition (using the αCT1 peptide, which has been clinically tested) with selective PIK3CB/p110β inhibitors (TGX-221, GSK2636771) synergistically overcomes TMZ resistance both in vitro and in vivo. This represents a rational combination therapy strategy targeting a fundamental resistance mechanism.

**Atomic biological processes**
- gap junction protein function and intercellular communication. Genes: GJA1
  - [27]: GJA1 (Cx43) forms gap junctions; mRNA levels strongly correlate with poor prognosis and chemoresistance
- non-channel Cx43-mediated PI3K activation. Genes: GJA1
  - [27]: Cx43 activates PI3K signaling independent of channel function; specifically requires PIK3CB/p110β
- chemoresistance signaling. Genes: GJA1
  - [27]: High Cx43 in MGMT-deficient GBM cells confers TMZ resistance; αCT1 and p110β inhibitors overcome resistance

**Atomic cellular components**
- plasma membrane gap junction protein complexes. Genes: GJA1
  - [30]: Connexin proteins comprise gap junctions; mediate protein-protein interactions and communication
- PI3K signaling complex. Genes: GJA1
  - [27]: Cx43 interacts with PI3K catalytic subunit p110β; activation occurs in Cx43/p110β precipitates

**Required genes (not in input)**
- Genes: PIK3CB, AKT1, PTEN
  - [27]: PI3K/AKT/mTOR cascade activated downstream of Cx43; PTEN loss promotes pathway activation

**Program citations**
- [27]: Connexin 43 confers chemoresistance through PI3K/p110β activation
- [30]: Connexin 43 drives GBM cancer stem cell phenotypes

## Program: Pericyte recruitment and vascular stability
Pericytes (mural cells) are recruited to glioma vasculature through PDGF-B/PDGFR-β signaling. Pericytes play paradoxical roles: structurally supporting vessel formation but also promoting treatment resistance. NG2 (a pericyte marker not in input list) isoforms in proliferative perivascular pericytes promote early angiogenesis and vasculogenic mimicry. PDGFRB signaling activates PI3K, promoting pericyte recruitment to hypoxic tumor regions. Two pericyte subtypes exist: Type-1 (non-contributing to new vessel formation; can differentiate to tumor-associated fibroblasts) and Type-2 (pro-angiogenic). Hypoxia induces HIF-1α-mediated PDGF-β expression in endothelial cells, recruiting pericytes. Anti-VEGF therapies lead to increased pericyte vessel coverage, promoting vascular stabilization and therapy resistance.

**Predicted impacts**
- Enhanced tumor vascular network formation and stabilization
- Recruitment of pericytes to hypoxic tumor regions
- Support for glioma stem cell maintenance in perivascular niche
- Increased resistance to anti-angiogenic therapies (bevacizumab)
- Promotion of vascular invasion and infiltration
- Development of abnormal vascular patterns with atypical pericyte coverage

**Evidence summary**
Pericytes play a multifaceted role in gBM vascular biology and treatment resistance. PDGF-B/PDGFR-β signaling is the primary mechanism recruiting pericytes to tumor vasculature, particularly in hypoxic regions. Hypoxia-inducible factor-1α (HIF-1α) upregulates PDGF-β expression in endothelial cells, creating a hypoxia-driven recruitment loop. Pericytes produce pro-angiogenic factors (VEGF, TGF-β, hepatocyte growth factor) and maintain vascular integrity through Ang-1/Tie-2 signaling. Importantly, anti-VEGF therapies paradoxically increase pericyte vessel coverage, promoting vascular stabilization and therapy resistance. Two functionally distinct pericyte subtypes have been characterized: Type-1 pericytes can differentiate to tumor-associated fibroblasts and contribute to ECM; Type-2 pericytes directly induce angiogenesis and are recruited specifically to sites of active tumor neovascularization.

**Atomic biological processes**
- PDGF-B/PDGFR-β mediated pericyte recruitment. Genes: PDGFRB
  - [14]: Hypoxia induces HIF-1α-mediated PDGF-β expression in endothelial cells; promotes PDGFR-β signaling in pericytes and migration
- pericyte-endothelial cell paracrine signaling. Genes: PDGFRB
  - [14]: Pericytes produce TGF-β, VEGF, HGF; create paracrine loop with endothelial cells via Ang-1/Tie-2 signaling
- resistance to anti-VEGF therapy. Genes: PDGFRB
  - [14]: Anti-VEGF therapy initially reduces endothelial cell density but leads to increased pericyte vessel coverage and vascular stabilization

**Atomic cellular components**
- perivascular pericyte niche. Genes: PDGFRB
  - [14]: Pericytes recruited to hypoxic regions; establish critical interactions with endothelial cells modulating vascular stability
- PDGFR-β signaling platform. Genes: PDGFRB
  - [14]: PDGFR-β mediates PI3K activation and pericyte migration toward newly formed immature microvessels

**Required genes (not in input)**
- Genes: PDGFB, NG2, VEGFR2, VEGFA, TGF-BETA1, HIF1A
  - [14]: PDGF-B secreted by endothelial cells; NG2 expressed by proliferative pericytes; VEGF-A and TGF-β produced by pericytes

**Program citations**
- [14]: Pericytes in glioblastoma: hidden regulators of tumor vasculature and treatment resistance

## Program: Immune cell infiltration and M2 macrophage polarization
Multiple genes in this list promote M1-to-M2 macrophage polarization and creation of an immunosuppressive tumor microenvironment. CHI3L2 (YKL40) is secreted by tumor cells and immune cells (particularly macrophages), promoting M2-like activation. COLEC12 (C-type lectin) functions as a scavenger receptor upregulated on M2 macrophages. ZFP36L2 correlates with immune infiltration and is positively associated with M2 macrophage markers. Complement components (C3, C3a) promote M2 polarization through C3aR signaling on macrophages. NMB (neuromedin B) expression correlates with immune infiltration and improved GBM survival. OSMR and other cytokine receptors on myeloid cells support immune cell recruitment and polarization.

**Predicted impacts**
- Recruitment and infiltration of macrophages/microglia into tumor microenvironment
- Shift of macrophage phenotype from pro-inflammatory (M1) to immunosuppressive (M2) state
- Increased expression of immunosuppressive cytokines (IL-10, TGF-β)
- Enhanced T cell exhaustion and impaired anti-tumor immunity
- Support for tumor angiogenesis and invasive phenotype
- Creation of permissive microenvironment for GSC maintenance

**Evidence summary**
Immune cell polarization toward M2 (immunosuppressive) phenotypes is a hallmark of GBM progression. CHI3L2 (YKL40) is secreted by tumor and immune cells and promotes M2 macrophage activation while inducing CD8+ T cell apoptosis, explaining the dual pro-tumor effects. COLEC12 functions as a scavenger receptor on M2 macrophages, recognizing patterns that promote immunosuppression. Complement C3a potently drives M3 macrophage polarization through C3aR signaling. ZFP36L2 high expression correlates with immune infiltration and poor prognosis, with enrichment of M1 macrophage markers in non-responders. Interestingly, NMB shows the opposite pattern—high NMB expression predicts better survival and is associated with enhanced immune infiltration, suggesting heterogeneity in immune responses. This program illustrates how tumors co-opt immune cells to create an immunosuppressive microenvironment.

**Atomic biological processes**
- M2 macrophage polarization and activation. Genes: C3, CHI3L2, COLEC12, ZFP36L2
  - [34]: C3a induces M2 polarization of cultured microglia and macrophages in C3aR-dependent fashion
  - [59]: Scavenger immunosuppressive program in myeloid cells includes MRC1, MSR1, CD163, LYVE1, COLEC12
- immune infiltration and lymphocyte recruitment. Genes: ZFP36L2, NMB
  - [20]: ZFP36L2 high expression significantly positively correlated with immune infiltration and immune checkpoint PD-L1
  - [51]: NMB expression correlated with tumor-infiltrating lymphocytes; associated with better survival

**Atomic cellular components**
- macrophage scavenger receptors and pattern recognition. Genes: COLEC12, CHI3L2
  - [59]: COLEC12 functions as pattern-recognition scavenger receptor; expressed on M2 macrophages

**Program citations**
- [45]: CHI3L2 is prognostic biomarker correlated with immune infiltrates in glioma
- [20]: ZFP36L2 expression positively correlated with immune infiltration and poor prognosis
- [34]: Hypoxia-induced C3 promotes M2 macrophage polarization
- [51]: NMB expression associated with immune infiltration and improved GBM survival

## Program: Metabolic reprogramming and hypoxia adaptation
Gliomas undergo profound metabolic rewiring to survive hypoxic microenvironments and aggressive selection pressures. Hypoxia-inducible factor-1α (HIF-1α) is a master regulator activating genes for glycolysis, angiogenesis, and stemness. PFKFB3 is the most highly expressed glycolytic enzyme and undergoes post-translational modifications (O-GlcNAcylation, phosphorylation) in response to hypoxia. HAS2 and HAS3 (hyaluronic acid synthases) are upregulated under hypoxia and glycolytic conditions. Endothelin signaling (EDNRA/EDNRB) is hypoxia-responsive and promotes both metabolic adaptation and GSC stemness. This program bridges metabolic, signaling, and stemness programs, reflecting the integrated nature of GBM adaptation.

**Predicted impacts**
- Coordinated upregulation of glycolytic pathway under hypoxia
- Maintenance of tumor cell viability in oxygen-deprived regions
- Enhanced stemness signaling through hypoxia-responsive pathways
- Increased ECM synthesis supporting tumor architecture
- Metabolic adaptation supporting rapid proliferation and invasion
- Coupling of metabolic and stemness programs through HIF-1α and endothelin signaling

**Evidence summary**
Metabolic reprogramming and hypoxia adaptation represent integrated processes in GBM driven by HIF-1α and complementary signaling pathways. PFKFB3 emerges as a central hub, with its expression and activity controlled by multiple post-translational modifications in response to hypoxia. O-GlcNAcylation of PFKFB3 by OGT (triggered by glucose availability during glycolysis) promotes nuclear translocation and cell cycle progression, while ERK phosphorylation causes cytoplasmic retention—these represent mutually exclusive regulatory mechanisms. Endothelin signaling (EDNRA/EDNRB) represents a hypoxia-responsive pathway coupling metabolic adaptation with GSC stemness maintenance. HAS2 upregulation under hypoxia drives excessive hyaluronic acid synthesis, creating a denser, more resistant ECM. This program illustrates how GBM coordinates multiple survival mechanisms in response to hostile microenvironmental conditions.

**Atomic biological processes**
- hypoxia-induced gene expression and HIF-1α signaling. Genes: EDNRA, EDNRB
  - [18]: Hypoxia upregulates EDN1, EDNRA, EDNRB expression through HIF-1α and ERN1-dependent mechanisms
- hypoxia-dependent glycolytic enzyme expression. Genes: PFKFB3
  - [37]: Hypoxia induces PFKFB3 expression and O-GlcNAcylation; maintains cancer cell division under hypoxic stress
- hypoxia-responsive ECM synthesis. Genes: HAS2
  - [13]: HAS2 (hyaluronic acid synthase) highly expressed in GBM; expression drives tumor progression

**Atomic cellular components**
- post-translational modification sites in metabolic enzymes. Genes: PFKFB3
  - [37]: PFKFB3 undergoes O-GlcNAcylation at Ser172 by OGT; alternatively phosphorylated by ERK; mutually exclusive modifications regulate nuclear translocation

**Required genes (not in input)**
- Genes: HIF1A, EGFR, PTEN, TP53
  - [37]: HIF-1α is master regulator of hypoxic adaptation; PFKFB3 induction is HIF-1α-dependent

**Program citations**
- [37]: Hypoxia-induced PFKFB3 O-GlcNAcylation and metabolic reprogramming
- [13]: HAS2 facilitates glioma malignancy under various metabolic conditions
- [18]: Hypoxia-dependent endothelin system expression

## Bibliography
1. Available from: https://www.oncotarget.com/article/16017/text/
2. Zhanxin D, Yaqing W, Jiaqi L, Shaowei G, Xiaoying C, Yu Y, et al.. Association of glioma CD44 expression with glial dynamics in the tumour microenvironment and patient prognosis.. Computational and structural biotechnology journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9508470/
3. Ayelet L, Eran B, Hananya V, Frances EL, Reuven S, Lior M. CD38 deficiency in the tumor microenvironment attenuates glioma progression and modulates features of tumor-associated microglia/macrophages.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3408254/
4. Yasuhiko H, Nancy AE, Martin AP, Edward HO, Marsha JM. Regulation and function of aquaporin-1 in glioma cells.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC1993862/
5. Mitrajit G, Paulina P-K, Szymon B, Karol J, Katarzyna P, Paulina S, et al.. Identification and characterization of tumor-associated astrocyte subpopulations and their interactions with the tumor microenvironment in experimental glioblastomas.. PLoS biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12539703/
6. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7651462/
7. Anand-Apte B, Bao L, Smith R, Zetter B, Iwata K, Olsen BR, et al.. A review of tissue inhibitor of metalloproteinases-3 (TIMP-3) and experimental analysis of its effect on primary tumor growth. Biochemistry and Cell Biology [Internet]. 1996Dec1;74(6). Available from: https://cdnsciencepub.com/doi/10.1139/o96-090
8. Rong R, Zuowei L, Qiong F. A disintegrin-like and metalloproteinase 15 facilitates glioblastoma proliferation and metastasis through activation of the protease-activated receptor 1.. CytoJournal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12010881/
9. Guichen H, Minfeng Z, Damin L, Jinxiao L, Qian T, Chutong X, et al.. The mechanism of ITGB4 in tumor migration and invasion.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335651/
10. Jinkun H, Yajun J, Fubing H, Peng S. Comprehensive analysis of expression, prognosis and immune infiltration for TIMPs in glioblastoma.. BMC neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34781885/
11. Baosheng Z, Yong L, Guangshuo M, Xiuyu W, Binge C, Hongwei L, et al.. ADAMTS8 inhibits glioma development in vitro and in vivo.. Folia neuropathologica [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37587889/
12. Chen P, Ma T, Yan T, Song Z, Liu C, Pan C, et al.. ITGB4 upregulation is associated with progression of lower grade glioma. Scientific Reports [Internet]. 2024Jan3;14(1). Available from: https://www.nature.com/articles/s41598-023-49801-y
13. Zhiyuan L, Kuo Y, Kaile C, Jinlai L, Kexiang D, Peng Z. HAS2 facilitates glioma cell malignancy and suppresses ferroptosis in an FZD7-dependent manner.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11309948/
14. Irene S-S, María P-S, Javier M, Lara N, Esther R-S, Teresa S-M. Pericytes in Glioblastoma: Hidden Regulators of Tumor Vasculature and Therapy Resistance.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11718950/
15. Yue L, Fei Y, Kazunari Y, Jonathan LT, Yibei Z, David HN, et al.. Autocrine endothelin-3/endothelin receptor B signaling maintains cellular and molecular properties of glioblastoma stem cells.. Molecular cancer research : MCR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3245317/
16. Yan T, Chen X, Zhan H, Yao P, Wang N, Yang H, et al.. Interfering with hyaluronic acid metabolism suppresses glioma cell proliferation by regulating autophagy. Cell Death &amp; Disease [Internet]. 2021May13;12(5). Available from: https://www.nature.com/articles/s41419-021-03747-z
17. Bastola S, Pavlyukov MS, Sharma N, Ghochani Y, Nakano MA, Muthukrishnan SD, et al.. Endothelial-secreted Endocan activates PDGFRA and regulates vascularity and spatial phenotype in glioblastoma. Nature Communications [Internet]. 2025Jan7;16(1). Available from: https://www.nature.com/articles/s41467-024-55487-1
18. Dmytro OM, Daria OT, Olena OR, Yuliia MV, Yuliia OL, Myroslava YS, et al.. Hypoxic regulation of EDN1, EDNRA, EDNRB, and ECE1 gene expressions in ERN1 knockdown U87 glioma cells.. Endocrine regulations [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/31734650/
19. G JR, M AI. Id4 suppresses MMP2-mediated invasion of glioblastoma-derived cells by direct inactivation of Twist1 function.. Oncogene [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/24413082/
20. Min Z, Jinquan L, Cheng C. High expression of ZFP36L2 correlates with the prognosis and immune infiltration in lower-grade glioma.. Frontiers in genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9334557/
21. Anna VM, Stacey MG, Lesley SC, Hui-Hsin T, Alice TM, Kevin WK, et al.. Expression profiling of Aldh1l1-precursors in the developing spinal cord reveals glial lineage-specific genes and direct Sox9-Nfe2l1 interactions.. Glia [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3909648/
22. Weifin Z, Elisabeth JR, Daniel PH, Norio A. Increased inhibitor of differentiation 4 (id4) expression in glioblastoma: a tissue microarray study.. Journal of Cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2931346/
23. Sáenz-Narciso B, Bell SE, Matheson LS, Venigalla RKC, Turner M. ZFP36-family RNA-binding proteins in regulatory T cells reinforce immune homeostasis. Nature Communications [Internet]. 2025May6;16(1). Available from: https://www.nature.com/articles/s41467-025-58993-y
24. Clavreul S, Dumas L, Loulier K. Astrocyte development in the cerebral cortex: Complexity of their origin, genesis, and maturation. Frontiers in Neuroscience [Internet]. 2022Sep13;16. Available from: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.916055/full
25. Available from: https://www.nature.com/articles/cddis2013279
26. Ruida H, Mehrdad A, Baoxue Y, Jeff MS, Xiangbo K, Guangping C. Identification of a Novel UT-B Urea Transporter in Human Urothelial Cancer.. Frontiers in physiology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5409228/
27. Pridham KJ, Shah F, Hutchings KR, Sheng KL, Guo S, Liu M, et al.. Connexin 43 confers chemoresistance through activating PI3K. Oncogenesis [Internet]. 2022Jan12;11(1). Available from: https://www.nature.com/articles/s41389-022-00378-7
28. Luigi C, Bernard F, Fabio F. Expression and Role of the Intermediate-Conductance Calcium-Activated Potassium Channel KCa3.1 in Glioblastoma.. Journal of signal transduction [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3362965/
29. Huang B, Wang H, Zhong D, Meng J, Li M, Yang B, et al.. Expression of Urea Transporter B in Normal and Injured Brain. Frontiers in Neuroanatomy [Internet]. 2021May28;15. Available from: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2021.591726/full
30. Erin EM-H, Nicole H, Ellen SH, Ashley PJ, Aymerick G, Sophia G, et al.. Connexin 43 drives glioblastoma cancer stem cell phenotypes through a WNK lysine-deficient protein kinase 1-c-MYC signaling axis.. Cell reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40946315/
31. T AMB van der V, J MK, D AMM, R TA van W, L A, P M van H, et al.. The complement system in glioblastoma multiforme.. Acta neuropathologica communications [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6134703/
32. A M, S J, J H, T T, S M. Expression of complement membrane regulators membrane cofactor protein (CD46), decay accelerating factor (CD55), and protectin (CD59) in human malignant gliomas.. The American journal of pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC1861510/
33. Day ZI, Roberts-Thomson S, Nouri YJ, Dalton NS, Wang SS, Davenport A, et al.. Defining the extracellular matrix for targeted immunotherapy in adult and pediatric brain cancer. npj Precision Oncology [Internet]. 2025Jun14;9(1). Available from: https://www.nature.com/articles/s41698-025-00956-z
34. Available from: https://insight.jci.org/articles/view/179854
35. Kolev M, Das M, Gerber M, Baver S, Deschatelets P, Markiewski MM. Inside-Out of Complement in Cancer. Frontiers in Immunology [Internet]. 2022Jul1;13. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.931273/full
36. Available from: https://www.ncbi.nlm.nih.gov/gene/63827
37. Lei Y, Chen T, Li Y, Shang M, Zhang Y, Jin Y, et al.. O-GlcNAcylation of PFKFB3 is required for tumor cell proliferation under hypoxia. Oncogenesis [Internet]. 2020Feb14;9(2). Available from: https://www.nature.com/articles/s41389-020-0208-1
38. Gabriela ND, Dominique SR, Elizandra B. Adenosinergic Signaling as a Key Modulator of the Glioma Microenvironment and Reactive Astrocytes.. Frontiers in neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8766410/
39. Wei J, Cunli X, Simona C, Chaya B, Tom M. Insulin-like growth factor binding protein 7 mediates glioma cell growth and migration.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2586684/
40. Yang L, Li S, Yu L, Leng J, Li N. Targeting glycolysis: exploring a new frontier in glioblastoma therapy. Frontiers in Immunology [Internet]. 2025Jan14;15. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1522392/full
41. I AS, M E. Energetic demands of the Na+/K+ ATPase in mammalian astrocytes.. Glia [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/9298845/
42. Liu Z, Ji H, Fu W, Ma S, Zhao H, Wang F, et al.. IGFBPs were associated with stemness, inflammation, extracellular matrix remodeling and poor prognosis of low-grade glioma. Frontiers in Endocrinology [Internet]. 2022Aug3;13. Available from: https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2022.943300/full
43. Tsunoda T, Riku M, Yamada N, Tsuchiya H, Tomita T, Suzuki M, et al.. <i>ENTREP/FAM189A2</i>
                    encodes a new ITCH ubiquitin ligase activator that is downregulated in breast cancer. EMBO reports [Internet]. 2021Dec20;23(2). Available from: https://www.embopress.org/doi/10.15252/embr.202051182
44. Casey WM, Branch C, Tiffany VK, Rozzy F, Todd AW, Joseph HS, et al.. CFAP54 is required for proper ciliary motility and assembly of the central pair apparatus in mice.. Molecular biology of the cell [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4569307/
45. Liling L, Yuanzhong Y, Hao D, Jiahua H, Lu S, Wanming H, et al.. CHI3L2 Is a Novel Prognostic Biomarker and Correlated With Immune Infiltrates in Gliomas.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8084183/
46. Available from: https://v22.proteinatlas.org/ENSG00000135063-FAM189A2
47. Siling L, Mia XT, Jeremy S, Jiami G, E SA. The essential role of primary cilia in cerebral cortical development and disorders.. Current topics in developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740521/
48. Ming-Cheng C, Chun-Tang C, Ping-Fang C, Ying-Cheng C. The Role of Chitinase-3-like Protein-1 (YKL40) in the Therapy of Cancer and Other Chronic-Inflammation-Related Diseases.. Pharmaceuticals (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10976000/
49. Hongsheng X, Hailiang Z, Chong M, Xing M, Ming S, Kai L, et al.. Epidermal growth factor receptor in glioblastoma.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5494611/
50. Clovis O da F, Rafael L, Débora F, Cerli RG, Thereza Q-S. Ras pathway activation in gliomas: a strategic target for intranasal administration of perillyl alcohol.. Archivum immunologiae et therapiae experimentalis [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2778682/
51. Li S, Li S, Li Q, Liu F, Liao W, Yu L, et al.. Increased Neuromedin B is Associated with a Favorable Prognosis in Glioblastoma. Frontiers in Bioscience-Landmark [Internet]. 2023Mar16;28(3). Available from: https://article.imrpress.com/journal/FBL/28/3/10.31083/j.fbl2803054/a47bb4b76a1c75c038a24fbc148290c6.pdf
52. Zhenyi A, Ozlem A, Tina Z, Qi-Wen F, William AW. Epidermal growth factor receptor and EGFRvIII in glioblastoma: signaling pathways and targeted therapies.. Oncogene [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5860944/
53. Available from: https://aacrjournals.org/cancerres/article/79/16/4026/638334/Identification-of-Novel-RAS-Signaling-Therapeutic
54. Suqin L, Shihuan L, Qingjie L, Fei L, Wenli L, Liangzhu Y, et al.. Increased Neuromedin B is Associated with a Favorable Prognosis in Glioblastoma.. Frontiers in bioscience (Landmark edition) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37005748/
55. Zhu H, Yu X, Zhang S, Shu K. Targeting the Complement Pathway in Malignant Glioma Microenvironments. Frontiers in Cell and Developmental Biology [Internet]. 2021Apr1;9. Available from: https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.657472/full
56. Xiangfei S, Qiang Z, Ping S, Xiaohan L, Xiaodong G, Kuntang S. COLEC12 Promotes Tumor Progression and Is Correlated With Poor Prognosis in Gastric Cancer.. Technology in cancer research & treatment [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10734338/
57. Jordan Z, Marco B, Philip DK, Gregory PT. Advances and therapeutic opportunities in visual cycle modulation.. Progress in retinal and eye research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12147667/
58. Mikio K, Misao M, Yuichi E, Steffen T, Teizo F. Expression of H-ficolin/Hakata antigen, mannose-binding lectin-associated serine protease (MASP)-1 and MASP-3 by human glioma cell line T98G.. International immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/12502731/
59. Miller TE, El FCA, Couturier CP, Chen Z, D’Antonio JP, Verga J, et al.. Programs, origins and immunomodulatory functions of myeloid cells in glioma. Nature [Internet]. 2025Feb26;640(8060). Available from: https://www.nature.com/articles/s41586-025-08633-8
60. Postnikova OA, William S, Uppal S, Bernstein SL, Poliakov E, Rogozin IB, et al.. Regulation of RPE65 expression in human retinal pigment epithelium cells. Scientific Reports [Internet]. 2025Jul25;15(1). Available from: https://www.nature.com/articles/s41598-025-12926-3
