# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: malignant glioblastoma (GBM)
- Tissue: brain

## Input Genes
POSTN, KIAA1211L, CPNE4, HMGA2, TRPM8, CYTOR, RGS6, RPH3A, CCN4, ADAMTS9-AS1, SPRY1, LEF1, VAT1L, COL22A1, MIR4435-2HG, AC000065.1, CPED1, ARHGAP6, TRPM3, ANGPT1, ALK, CA2, SERPINE1, CHRM3-AS2, ITGA3, ... (118 total)

## Program: Extracellular Matrix Remodeling and Invasion
Gene program coordinating degradation and remodeling of the extracellular matrix to promote glioblastoma cell invasion and migration through brain tissue. This program includes collagen deposition, matrix metalloproteinase regulation, and integrin-mediated adhesion dynamics that facilitate the invasive phenotype characteristic of GBM mesenchymal subtypes. The program is particularly enriched in the tumor center where invasive mesenchymal-like cells drive aggressive progression.

**Predicted impacts**
- Enhanced degradation of basement membrane barriers enabling invasion into surrounding brain tissue
- Increased cell motility through integrin-mediated adhesion dynamics
- Promotion of partial epithelial-mesenchymal transition (pEMT) phenotype in glioblastoma cells
- Remodeling of tumor microenvironment to support vascular infiltration and immune cell trafficking
- Enrichment of invasive mesenchymal-like cell populations in tumor center

**Evidence summary**
Multiple genes in this program directly regulate ECM composition and degradation pathways critical for GBM invasion. COL22A1 expression is specifically enriched in mesenchymal-like cells at the GBM center and correlates with increased MMP activity. SERPINE1 is part of established prognostic signatures and promotes both angiogenesis and immune cell infiltration. ITGA3 high expression is an independent predictor of poor survival and knockdown reduces invasion by ~60-70%. SPRY genes regulate RTK signaling which drives invasion. The convergence of multiple collagen genes (COL22A1, COL19A1, COL23A1, COL25A1, COL27A1) with POSTN, SERPINE1, and ITGA3 creates a coordinated program for ECM remodeling that characterizes the aggressive mesenchymal GBM subtype.

**Atomic biological processes**
- extracellular matrix proteolysis. Genes: COL22A1, COL19A1, COL23A1, COL25A1, COL27A1, ADAMTS9-AS1
  - [38]: MMPs including MMP-2 and MMP-9 degrade type IV collagen at basement membranes, facilitating glioblastoma cell invasion. COL22A1 and other collagen genes are substrates.
  - [7]: COL22A1 involved in ECM remodeling with increased MMP-2 and MMP-9 expression driving invasive mesenchymal phenotype in GBM center.
- PAI-1-mediated matrix remodeling and plasmin activation. Genes: SERPINE1, PLAT
  - [12]: SERPINE1 (PAI-1) identified as component of six-gene prognostic signature in glioma with high expression associated with poor survival.
  - [9]: SERPINE1 promotes fibrin deposition, angiogenesis, immune cell infiltration, and is elevated in tumors promoting macrophage transmigration and tumor growth.
- cell-ECM adhesion and migration signaling. Genes: ITGA3, POSTN, CDH4
  - [19]: ITGA3 (integrin alpha-3) knockdown attenuated glioma cell migration, invasion, and adhesion; high expression predicts poor survival.
  - [22]: ITGA3 regulates stemness and invasion of glioblastoma through POU3F2 transcription factor; anti-ITGA3 antibody reduced tumor size.
- focal adhesion and cytoskeletal dynamics. Genes: SPRY4, SPRY1, IQGAP2, ARHGAP26, ARHGAP6, RHOJ
  - [45]: SPRY4 protein regulates cell adhesion and suppresses matrix metalloproteinase activity to inhibit invasion, while IQGAP2 coordinates cytoskeletal remodeling.

**Atomic cellular components**
- extracellular matrix proteins. Genes: COL22A1, COL19A1, COL23A1, COL25A1, COL27A1, POSTN
  - [38]: Matrix metalloproteinases degrade ECM structural components including collagens, proteoglycans, and fibronectin that compose basement membranes and interstitial matrix.
- integrin adhesion complexes. Genes: ITGA3, VAV3, IQGAP2
  - [19]: ITGA3 mediates cell-ECM interactions through integrin complexes that regulate adhesion, migration, and invasion in glioma cells.

**Required genes (not in input)**
- Genes: MMP2, MMP9, MMP14, SNAIL, TWIST1, VIM, FN1, LOX, TIMP1
  - [38]: MMP-2, MMP-9, and MMP-14 are essential for matrix degradation but not present in input gene list; tissue inhibitors like TIMP1 normally constrain MMP activity.
  - [24]: SNAIL and TWIST1 are EMT-inducing transcription factors that coordinate ECM remodeling through upregulation of vimentin and downregulation of E-cadherin.

**Program citations**
- [7]: COL22A1 promotes malignant progression of mesenchymal-like cells in GBM through PI3K pathway activation and ECM remodeling.
- [19]: ITGA3 serves as independent predictor of poor survival in astrocytoma with high expression in grade II-IV glioma cells.
- [21]: EMT-inducing transcription factors correlate with poor prognosis through mechanisms including N-cadherin upregulation and vimentin expression, genes regulated by ECM-interaction pathways.
- [38]: Comprehensive analysis of matrix metalloproteinases in gliomas showing MMP-2 and MMP-9 consistently elevated in aggressive gliomas and associated with increased invasiveness.

## Program: RTK/MAPK Signaling Inhibition and Feedback
Gene program regulating receptor tyrosine kinase (RTK) signaling cascades through negative feedback loops and pathway suppression mechanisms. The SPRY family genes encode classical negative feedback inhibitors of MAPK signaling downstream of growth factor receptors (EGFR, PDGFRA, FGFR). This program is dysregulated in GBM where SPRY expression is often reduced, allowing unopposed RTK signaling that drives proliferation and EMT. RGS proteins provide additional negative feedback on G-protein coupled receptor signaling.

**Predicted impacts**
- Suppression of Ras/MAPK/ERK cascade that promotes GBM proliferation and migration
- Inhibition of PI3K/Akt pathway activation downstream of RTK signaling
- Reduced responsiveness to growth factors (PDGF, FGF, EGF) that activate RTKs
- Decreased EMT-associated transcriptional programs (SNAIL, TWIST upregulation)
- Normalization of cell cycle progression and reduced clonal expansion

**Evidence summary**
The SPRY family genes encode well-characterized negative feedback inhibitors of RTK signaling that are frequently dysregulated in cancer. In glioblastoma, SPRY2 is reported as hyperactive with consequent enhanced ERK signaling. SPRY4 inhibits proliferation, migration, and invasion through Ras-MAPK pathway suppression. CAMK2B represents an alternative pathway for MAPK inhibition and its high expression correlates with better prognosis. RGS proteins (RGS6, RGS20) provide complementary negative feedback on G-protein signaling. This program is significant because GBM TCGA analysis identified RTK/RAS/PI3K pathway activation in 88% of samples, making negative feedback regulators therapeutically relevant. The presence of multiple SPRY and RGS family members suggests coordinated feedback suppression that, when intact, constrains RTK signaling hyperactivation.

**Atomic biological processes**
- RTK negative feedback inhibition. Genes: SPRY1, SPRY2, SPRY4
  - [45]: SPRY4 inhibits activation of Ras-MAPK and PI3K-Akt pathways by binding to SOS1 and disrupting Grb2-Sos1 complex formation, thereby inhibiting FGF and EGF receptor-mediated ERK activation.
  - [48]: SPRY2 essential for regulating RTK signaling; as negative feedback regulator, its hyperactivation leads to ERK signaling enhancement and increased GBM proliferation.
- MAPK pathway inhibition. Genes: CAMK2B, CAMK2A
  - [15]: CAMK2B inhibits glioma proliferation, invasion, and migration through the Ras/Raf/MEK/ERK signaling pathway; CAMK2B overexpression reduced proliferation by ~40% and invasion by 60-70%.
- G-protein coupled receptor signaling modulation. Genes: RGS6, RGS20
  - [45]: RGS proteins serve as negative feedback regulators of heterotrimeric G-protein signaling, constraining proliferative and migratory responses to GPCR ligands.

**Atomic cellular components**
- Ras-MAPK signaling complex. Genes: SPRY1, SPRY2, SPRY4
  - [45]: SPRY proteins physically interact with Grb2-SOS1 complex components to block Ras activation, the initiating step of MAPK cascade.

**Required genes (not in input)**
- Genes: EGFR, PDGFRA, FGFR, RAF, MEK, ERK, GRB2, SOS1
  - [3]: EGFR, PDGFRA, and FGFR are primary targets of SPRY negative feedback; RAF-MEK-ERK cascade is the primary pathway inhibited by SPRY proteins.

**Program citations**
- [3]: EGFR amplification and mutation are most frequent in classical GBM subtype; dysregulation of negative feedback on RTK signaling enables constitutive pathway activation.
- [15]: CAMK2B inhibits glioma proliferation and invasion through Ras/Raf/MEK/ERK signaling pathway; high CAMK2B expression associated with better prognostic outcomes.
- [45]: SPRY4 acts as negative feedback inhibitor of RTK signaling, and loss of SPRY4 expression promotes tumor development in multiple cancer types.
- [48]: SPRY2 as regulator of RTK signaling is essential for GBM cell proliferation and tumorigenicity; hyperactivation consequent to ERK signaling dysregulation.

## Program: Wnt/β-catenin Pathway Activation
Gene program governing canonical Wnt signaling through LEF1 and associated transcriptional regulation. Wnt/β-catenin pathway promotes stemness, migration, angiogenesis, and therapy resistance in glioblastoma. In GBM, this pathway is often overactive particularly in mesenchymal subtypes, allowing cells to recapitulate embryonic developmental programs that result in characteristic proliferation and invasiveness. WNT16 and LEF1 coordinate transcriptional responses downstream of β-catenin stabilization.

**Predicted impacts**
- Enhanced transcription of stemness-maintaining genes and glioma stem cell markers
- Promotion of epithelial-mesenchymal transition through upregulation of EMT-inducing transcription factors
- Increased angiogenesis via VEGF upregulation
- Enhanced cell motility and invasive capacity
- Maintenance of chemotherapy resistance phenotype

**Evidence summary**
WNT/β-catenin signaling is a hallmark of therapeutic challenge in GBM due to its context-dependent role and critical function in healthy tissue homeostasis. The pathway is frequently overactive in GBM, particularly in mesenchymal subtypes. LEF1 functions as a key transcriptional effector downstream of β-catenin. WNT16 as a ligand activates both canonical and non-canonical Wnt pathways. The program is supported by evidence that: (1) canonical Wnt pathway activation promotes stemness in GBM through NSC developmental programs; (2) Wnt signaling regulates VEGF-mediated angiogenesis; (3) non-canonical Wnt pathways promote mesenchymal differentiation and EMT; (4) Wnt pathway inhibitors like WNT974 are under clinical investigation in GBM. However, the input gene list contains limited components of complete Wnt pathway, suggesting partial pathway representation.

**Atomic biological processes**
- canonical Wnt/β-catenin transcriptional activation. Genes: LEF1, WNT16
  - [11]: Wnt/β-catenin pathway comprises extracellular signals (Wnt proteins including WNT16), membrane receptors (Frizzled, LRP5/6), and nuclear transcription factors (TCF/LEF) that activate downstream target genes.
  - [8]: WNT/β-catenin pathway activation in GBM results in upregulation of EMT-TFs such as Twist, Snail, Slug and Zeb1, promoting tumor cell migration and invasion.
- Wnt-induced angiogenesis. Genes: LEF1, WNT16
  - [8]: WNT/β-catenin signaling transcriptionally regulates vascular endothelial growth factor (VEGF), where VEGF gene promoter contains seven TCF binding sites.
- non-canonical Wnt/PCP pathway signaling. Genes: WNT16
  - [8]: WNT5A activation of non-canonical pathways induces formation of lamellipodia and microtubule-organizing center reorientation; mesenchymal tumors with upregulated non-canonical Wnt pathways are more motile and invasive.

**Atomic cellular components**
- TCF/LEF transcriptional complex. Genes: LEF1
  - [11]: LEF (lymphoid enhancer factor) proteins comprise the nuclear segment of Wnt/β-catenin pathway, forming complexes with β-catenin to activate transcription of target genes.

**Required genes (not in input)**
- Genes: WNT3A, WNT1, WNT5A, FZD, LRP5, LRP6, CTNNB1, APC, AXIN, GSK3B, TCF7
  - [8]: Complete Wnt/β-catenin pathway requires Wnt ligands, Frizzled receptors, LRP5/6 co-receptors, destruction complex components (APC, AXIN, GSK3), and additional TCF/LEF transcription factors.

**Program citations**
- [8]: Comprehensive review of WNT signaling pathway involvement in GBM genesis and acquired therapy resistance; WNT system often overactive in GBM allowing recapitulation of embryonic processes.
- [11]: Wnt/β-catenin pathway comprises family of proteins playing critical roles in embryonic development and adult tissue homeostasis; dysregulation drives tumorigenesis.

## Program: Angiogenesis and Vascular Remodeling
Gene program promoting tumor angiogenesis and vascular network formation through growth factor signaling and endothelial-tumor crosstalk. ANGPT1 (angiopoietin-1) and GDF15 (growth differentiation factor-15) coordinate pro-angiogenic signaling. GDF15 is induced by radiation and drives VEGFA expression through MAPK/SP1 pathway in glioblastoma cells. High degree of tumor vascularization through increased VEGF production is a hallmark of GBM progression. Carbonic anhydrases (CA2, CA10) support hypoxia-driven angiogenesis through metabolic regulation.

**Predicted impacts**
- Enhanced secretion of pro-angiogenic factors from both tumor and endothelial cells
- Increased vascular endothelial growth factor (VEGF) expression and signaling
- Promotion of endothelial cell migration and tube formation
- Establishment of abnormal vascular network with enhanced permeability
- Creation of perivascular niche supporting glioblastoma stem cell populations
- Enhanced tumor hypoxia through aberrant vascular architecture

**Evidence summary**
Angiogenesis is a hallmark of GBM biology and therapeutic target. ANGPT1 and GDF15 represent distinct pro-angiogenic signaling mechanisms converging on VEGF regulation. GDF15 is specifically induced by radiation and promotes VEGFA transcription through MAPK1/SP1 signaling, supporting the hypothesis that radiation paradoxically enhances angiogenic responses. ANGPT1 works synergistically with VEGF-A to induce robust angiogenesis. Carbonic anhydrases (CA2, CA10) support the hypoxic tumor microenvironment through pH buffering, which is essential for angiogenic signaling. The high degree of tumor vascularization in GBM results in both abnormal vascular networks and enhanced hypoxia, creating selective pressure for angiogenic gene expression. However, the program in the input gene list is partially represented as it lacks the primary angiogenic ligand VEGFA itself.

**Atomic biological processes**
- angiopoietin-mediated angiogenesis. Genes: ANGPT1
  - [13]: Angiopoietin-1 (ANGPT1) in concert with VEGF-A induces angiogenesis in xenograft models; Angiopoietin-2 mediates tumor angiogenesis in astrocytomas.
- GDF15-mediated VEGF activation and endothelial crosstalk. Genes: GDF15
  - [37]: Radiation promotes GDF15 secretion from brain endothelial cells; GDF15 activates VEGFA promoter in glioblastoma cells via p-MAPK1/SP1 pathway, promoting angiogenesis.
- hypoxia-responsive angiogenesis. Genes: CA2, CA10, ANGPT1
  - [60]: HIF1α and HIF2α regulate angiogenesis under hypoxic conditions through VEGF, PDGF, and angiopoietin upregulation; carbonic anhydrases facilitate metabolic adaptation supporting angiogenesis.

**Atomic cellular components**
- pro-angiogenic growth factor secretion. Genes: ANGPT1, GDF15
  - [13]: GSCs secrete pro-angiogenic factors including angiopoietin and VEGF, with GSCs themselves capable of transdifferentiation into endothelial cells.
- carbonic anhydrase-mediated pH regulation. Genes: CA2, CA10, SLC4A4
  - [25]: SLC4A4 and carbonic anhydrases (CA2, CA10) regulate intracellular pH and buffer extracellular pH changes, supporting metabolic adaptation in tumor microenvironment.

**Required genes (not in input)**
- Genes: VEGFA, VEGFR1, VEGFR2, KDR, FLT1, PDGFA, PDGFB, HIF1A, HIF2A, PECAM1
  - [37]: VEGFA and its receptors KDR/VEGFR2 are primary angiogenic signaling components; HIF1A and HIF2A are master regulators of hypoxia-induced angiogenesis.

**Program citations**
- [3]: High degree of tumor vascularization as result of increased production of pro-angiogenic growth factors, including VEGF, observed in GBM leading to development of bevacizumab treatment.
- [13]: Multiple pro-angiogenic factors secreted by GSCs including angiopoietin and VEGF; hypoxia is most potent stimulator of endothelial cell migration and proliferation in glioblastoma.
- [37]: GDF15 activated by radiation promotes angiogenesis through GBM-endothelial cell crosstalk and VEGFA upregulation via MAPK1/SP1 transcriptional pathway.

## Program: Glioma Stem Cell Maintenance and Self-Renewal
Gene program maintaining stemness properties of glioblastoma stem cells (GSCs) through transcriptional and signaling mechanisms that preserve self-renewal capacity and multipotency. This program includes transcription factors (TFCP2L1, BNC2, EGR1, SOX1-OT) that coordinate expression of stemness markers and suppress differentiation. EGR1 orchestrates a PDGFA-dependent growth-stimulatory loop and activates genes (SHH, GLI1, NANOG) critical for GSC maintenance. The program is dysregulated in GBM to maintain tumor-initiating capacity and therapy resistance.

**Predicted impacts**
- Maintenance of self-renewal capacity and resistance to differentiation cues
- Sustained expression of stemness markers (CD133, SOX2, NANOG, OCT4)
- Preservation of multipotency for differentiation into proneural or mesenchymal lineages
- Enhanced therapy resistance through quiescence and reduced proliferation
- Support for tumor-initiating capacity in serial xenografting experiments

**Evidence summary**
Glioblastoma stem cells are a critical population driving tumor initiation, recurrence, and therapy resistance. EGR1 is expressed in >80% of GBM cases and is specifically enriched in proliferating/progenitor cells. EGR1 orchestrates a positive feedback loop with PDGFA that promotes stemness and is essential for GSC maintenance. TFCP2L1 and SOX1-OT regulate transcriptional programs maintaining pluripotency. BNC2 expression is enriched in the mesenchymal-CSC phenotype. JAG1 as a Notch ligand maintains the Notch-high stem cell population characterized by enhanced tumorigenicity. Multiple studies demonstrate that cells with high expression of these transcription factors exhibit enhanced sphere-forming capacity, tumor-initiating ability, and resistance to differentiation. The program is particularly important given that proneural GSCs are more resistant to temozolomide than differentiated progeny.

**Atomic biological processes**
- transcription factor-mediated stemness maintenance. Genes: EGR1, TFCP2L1, BNC2, SOX1-OT
  - [35]: EGR1 contributes to stemness marker expression and proliferation by orchestrating PDGFA-dependent growth-stimulatory loop; EGR1 directly activates SHH, GLI1, GLI2, and PDGFA expression.
  - [32]: EGR1 plays role in stemness of glioblastoma through SHH/NOTCH1/miR-18a/ERK signaling pathway crucial for regulation of stem cells' self-renewal.
- Notch pathway-mediated stem cell maintenance. Genes: JAG1
  - [49]: Notch signaling highly active in GSCs where it suppresses differentiation and maintains stem-like properties; Notch activation promotes self-renewal capacity.
  - [52]: Notch signaling regulates metabolic heterogeneity in glioblastoma stem cells; CD133+ (PROM1) and Notch-high cells demonstrate enhanced tumorigenicity and self-renewal.
- developmental gene program recapitulation. Genes: TFCP2L1, SOX1-OT, BNC2
  - [27]: Proneural GSCs predominantly express developmental genes (SLITRK2, DLX1, PDGFRA, OLIG2, NKX2) and stemness-associated genes (SOX11, DCX, HOXA7, EPHA2, PROM1).

**Atomic cellular components**
- transcriptional regulatory complexes. Genes: EGR1, TFCP2L1, BNC2
  - [35]: EGR1 zinc finger transcription factor binds DNA and orchestrates expression of downstream stemness genes through direct promoter binding at SHH, GLI1, GLI2, PDGFA loci.

**Required genes (not in input)**
- Genes: SOX2, NANOG, OCT4, OLIG2, PDGFRA, CD133, NOTCH1, RBPJK, HES1, HES5, SHH, GLI1
  - [35]: EGR1 directly activates SHH, GLI1, GLI2, PDGFA; these downstream targets are essential for maintaining GSC stemness but not present in input gene list.
  - [49]: Notch pathway requires RBPJK, HES1, HES5 as core components; JAG1 alone is insufficient for complete Notch signaling program.

**Program citations**
- [35]: EGR1 expression provided better patient outcome when progression-free survival considered; EGR1 nuclear expression frequent in GBM (82% of cases) and restricted to proliferating/progenitor cells.
- [32]: EGR1 expression notably common in glioblastoma, accounting for over 80% of cases in cohort study; plays role in angiogenesis, cell adhesion, cell survival, and stemness.
- [44]: Progenitor cancer stem cells exhibit enhanced proliferative capacity and contain majority of cycling cells; progenitor GSCs show differential sensitivity to temozolomide compared with differentiated lineages.
- [49]: Notch signaling required for neural stem cell maintenance; blocking Notch pathway reduces GSC proliferation and oncogenicity in vitro and in vivo.

## Program: Calcium Signaling and Ion Homeostasis
Gene program regulating intracellular calcium dynamics and ion channel activity that modulates glioblastoma cell survival, migration, and radioresistance. TRPM8 (transient receptor potential melastatin 8) and TRPM3 are cation channels that regulate calcium influx and cell excitability. CAMK2A and CAMK2B are calcium/calmodulin-dependent protein kinases that transduce calcium signals into phosphorylation cascades controlling proliferation and invasion. SLC24A2 and SLC4A4 regulate sodium-potassium and sodium-bicarbonate transport maintaining ionic gradients.

**Predicted impacts**
- Enhanced intracellular calcium dynamics supporting cell survival and migration
- Increased radioresistance through TRPM8-mediated calcium signaling
- Reduced proliferation and invasion when CAMK2B expression is high
- Maintenance of intracellular pH and ionic balance in tumor microenvironment
- Modulation of calcium-dependent gene expression programs

**Evidence summary**
Calcium signaling represents a critical but understudied regulatory layer in glioblastoma biology. TRPM8 is required for survival and radioresistance of GBM cells and represents a promising therapeutic target. TRPM3 provides complementary calcium influx capacity. CAMK2B suppresses glioma proliferation, invasion, and migration with >40% reduction in proliferation and 60-70% reduction in invasion upon overexpression. CAMK2A/B represent a particularly essential calcium signaling node as deletion of both isoforms is embryonically lethal. The presence of multiple ion transporters (SLC24A2, SLC4A4) suggests that GBM cells actively maintain ionic homeostasis to support the metabolic demands of rapid growth. Carbonic anhydrases (CA2, CA10) enable pH buffering critical for both angiogenic signaling and metabolic adaptation to hypoxia. This program appears particularly important for radioresistance phenotypes.

**Atomic biological processes**
- TRPM channel-mediated calcium signaling. Genes: TRPM8, TRPM3
  - [2]: TRPM8 channels required for survival and radioresistance of human glioblastoma cells; suggests TRPM8 might represent promising therapeutic target.
  - [5]: TRPM8 therapeutic potential in cancer treatment; TRPM8 participates in glioblastoma cancer cell spreading, survival, and radioresistance.
- CAMK-mediated calcium signal transduction. Genes: CAMK2B, CAMK2A
  - [15]: CAMK2B overexpression in glioma cells led to ~40% reduction in proliferative capacity and 60-70% decrease in invasive and migratory abilities; works through Ras/Raf/MEK/ERK pathway.
  - [18]: CAMK2 isoforms (CAMK2A, CAMK2B) are key players in synaptic plasticity; germline deletion of both isoforms is lethal, indicating essential function.
- sodium-potassium and pH homeostasis. Genes: SLC24A2, SLC4A4, CA2, CA10
  - [25]: SLC4A4 plays protective role in glioma progression by regulating metabolic activities and pH homeostasis.

**Atomic cellular components**
- TRP ion channels. Genes: TRPM8, TRPM3
  - [2]: TRPM8 is member of transient receptor potential family of ion channels with cation permeability; TRPM8 expression supports glioblastoma radioresistance.
- calcium/calmodulin-dependent kinase complex. Genes: CAMK2A, CAMK2B
  - [18]: CAMK2 forms holoenzyme of ~12 subunits consisting of both CAMK2A and CAMK2B subunits; subunit composition determines sensitivity for fluctuating calcium levels.
- ionic transporter complexes. Genes: SLC24A2, SLC4A4
  - [25]: SLC4A4 (sodium bicarbonate transporter) and SLC24A2 (sodium/potassium/calcium exchanger) maintain electrochemical gradients supporting metabolic adaptation.

**Required genes (not in input)**
- Genes: CALMODULIN, CaMKIV, CaMKK, IP3R, RYANODINE_RECEPTOR, SERCA
  - [18]: Complete CAMK signaling requires calmodulin as activator, CaMKK as upstream kinase, and calcium release channels (IP3R, ryanodine receptors) as calcium sources.

**Program citations**
- [2]: TRPM8 channels contribute to spreading, survival and radioresistance of human glioblastoma and therefore might represent a promising therapeutic target.
- [5]: Therapeutic potential of TRPM8 channels in cancer treatment; TRPM8 participates in glioblastoma cancer cell spreading, survival and radioresistance.
- [15]: CAMK2B inhibits glioma proliferation, invasion, and migration through Ras/Raf/MEK/ERK signaling pathway; high expression associated with better prognostic outcomes.
- [18]: CAMK2A and CAMK2B germline or adult deletion results in lethality; both Ca2+-dependent and Ca2+-independent activity of CAMK2 essential for neuronal survival.

## Program: Mesenchymal Differentiation and Epithelial-Mesenchymal Transition
Gene program driving epithelial-mesenchymal transition (EMT) and commitment to mesenchymal phenotype characteristic of aggressive GBM. This program includes transcription factors (BNC2) and signaling molecules that promote loss of epithelial characteristics and acquisition of migratory and invasive properties. The mesenchymal program is enriched in the GBM center where invasive cells cluster, and is associated with poor prognosis. Multiple regulatory mechanisms including Wnt/β-catenin, TGF-β, Notch, and NF-κB pathways converge to drive sustained mesenchymal differentiation.

**Predicted impacts**
- Loss of epithelial cell-cell adhesion and acquisition of migratory capacity
- Downregulation of E-cadherin and upregulation of mesenchymal markers (vimentin, N-cadherin)
- Enhanced ECM remodeling and invasion into surrounding tissue
- Increased angiogenesis through VEGF and angiopoietin production
- Enrichment of tumor-promoting signaling pathways (PI3K/AKT, Wnt/β-catenin, Notch, NF-κB)
- Promotion of therapy resistance and poor clinical prognosis

**Evidence summary**
The mesenchymal GBM subtype represents a distinct transcriptional state enriched at the invasive tumor margin and associated with poor prognosis. BNC2 is a transcriptional co-regulator of mesenchymal identity and is specifically upregulated in mesenchymal-CSC populations. SERPINE1 promotes both EMT and angiogenesis, supporting a mesenchymal-angiogenic phenotype. POSTN, a secreted ECM protein, is characteristic of mesenchymal GBM. The collagen genes (COL22A1, COL19A1, COL23A1, COL25A1, COL27A1) define the ECM remodeling characteristic of mesenchymal differentiation. IRAK2 is part of the NF-κB signaling cascade that drives mesenchymal transcriptional programs. The mesenchymal program is driven by multiple convergent pathways including Wnt/β-catenin, TGF-β, Notch, and NF-κB signaling. Of clinical significance, patients with mesenchymal GBM show elevated expression of immune cell infiltration markers and respond better to immunotherapy despite worse overall prognosis, suggesting therapeutic opportunity.

**Atomic biological processes**
- EMT-inducing transcription factor activity. Genes: BNC2
  - [21]: EMT-inducing transcription factors like TWIST, SNAIL, and ZEB correlate with poor prognosis in glioblastoma; high expression predicts shorter overall survival.
  - [50]: BNC2 and other mesenchymal transcription factors control regulatory networks driving mesenchymal/cancer stem cell phenotype; inversely regulated from immune response modules.
- mesenchymal marker upregulation. Genes: SERPINE1, POSTN
  - [53]: Transposable element-defined clusters show enrichment of mesenchymal signature genes including FN1, SERPINE1, and GFPT2 in cluster 2 associated with mesenchymal phenotype.
  - [26]: MES subtype shows elevated expression of angiogenic factors including VEGF, VEGFR1/2, and PECAM1 (endothelial marker) along with classic mesenchymal markers YKL40 and MET.
- NF-κB pathway-driven mesenchymal transition. Genes: BNC2, IRAK2
  - [43]: NF-κB controls expression of important transcription factors C/EBPβ, STAT3, and TAZ that enhance mesenchymal transition in pre-glioma spheroid cultures.

**Atomic cellular components**
- mesenchymal signature gene expression. Genes: SERPINE1, POSTN, COL22A1, COL19A1, COL23A1, COL25A1, COL27A1
  - [7]: Mesenchymal-like cells from tumor center express genes associated with ECM remodeling (FN1, SERPINE1), angiogenesis (VEGF), and immune infiltration.

**Required genes (not in input)**
- Genes: SNAI1, SNAI2, TWIST1, ZEB1, ZEB2, VIM, FN1, CDH2, STAT3, CEBPB, TAZ, YAP
  - [21]: Classic EMT-inducing transcription factors SNAIL, SLUG, TWIST, and ZEB are master regulators of EMT program but not represented in input gene list.
  - [43]: NF-κB pathway activates downstream transcription factors STAT3, C/EBPβ, and TAZ that are required for complete mesenchymal transition program.

**Program citations**
- [26]: MES-GBM subtype characterized by NF1 gene mutation, NF-κB and AKT pathway activation, elevated YKL40, MET, angiogenic factors, and immune infiltration.
- [43]: Mesenchymal GBM subtype defined by distinct gene expression profile; NF-κB controls expression of transcription factors driving mesenchymal transition and associated with poor prognosis.
- [50]: BNC2 is transcription factor controlling mesenchymal/cancer stem cell transcriptional network; expression patterns inversely correlated with immune response modules.

## Program: Hypoxia Response and Metabolic Adaptation
Gene program coordinating cellular responses to hypoxia and metabolic adaptation in the tumor microenvironment. Carbonic anhydrases (CA2, CA10) buffer pH changes and support glycolytic metabolism under hypoxia. SLC4A4 regulates sodium-bicarbonate transport supporting metabolic homeostasis. This program is activated in response to the hypoxic microenvironment characteristic of GBM tumors, where HIF1α and HIF2α upregulate angiogenic factors (VEGF, PDGF, angiopoietins) and shift metabolism toward glycolysis. The program supports glioblastoma progression by enabling tumor cell survival and invasiveness under low oxygen tension.

**Predicted impacts**
- Maintenance of intracellular pH despite lactic acid accumulation from anaerobic glycolysis
- Support for HIF-driven angiogenic and metabolic gene expression programs
- Enhanced tumor cell survival and radioresistance under hypoxic stress
- Promotion of invasiveness through hypoxia-induced EMT pathways
- Creation of microenvironmental niche supporting glioblastoma stem cell populations in perivascular hypoxic regions

**Evidence summary**
Hypoxia is a defining feature of glioblastoma microenvironment and drives selection of aggressive, treatment-resistant phenotypes. Carbonic anhydrases (CA2, CA10) are essential for pH buffering that enables continued glycolytic metabolism under hypoxic conditions. SLC4A4 provides complementary bicarbonate transport capacity. Hypoxia-driven HIF1α upregulates VEGF, PDGF, and angiopoietins for angiogenesis (represented by GDF15 and ANGPT1 in this gene list). The program is particularly important because hypoxia creates a positive feedback loop: initial hypoxia induces HIF1α, which upregulates VEGF and promotes angiogenesis, but the resulting abnormal vascular architecture perpetuates hypoxia, selecting for tumor cells with enhanced hypoxic adaptation. The presence of multiple carbonic anhydrase genes and the sodium-bicarbonate transporter suggests coordinated pH buffering as a key glioblastoma survival mechanism. Hypoxia-induced expression of these genes correlates with increased radioresistance and poor prognosis.

**Atomic biological processes**
- pH buffering and lactic acid homeostasis. Genes: CA2, CA10, SLC4A4
  - [25]: SLC4A4 (sodium bicarbonate transporter) plays protective role in glioma progression by regulating metabolic activities and pH homeostasis during hypoxic adaptation.
  - [60]: Carbonic anhydrases (CA2, CA10) facilitate proton buffering and CO2 hydration, supporting glycolytic metabolism and maintaining intracellular pH in tumor microenvironment.
- hypoxia-inducible angiogenesis. Genes: ANGPT1, GDF15
  - [60]: Under hypoxia, HIF1α upregulated and activates hypoxia response elements on VEGF-A promoter; HIF1α most potent stimulator of endothelial cell migration and angiogenesis.
- hypoxia-induced radioresistance. Genes: CA2, CA10
  - [57]: Positive feedback circuit comprising p21 and HIF-1α aggravates hypoxia-induced radioresistance by promoting Glut1/LDHA-mediated glycolysis.

**Atomic cellular components**
- glycolytic enzyme complexes. Genes: CA2, CA10
  - [60]: Carbonic anhydrases support aerobic glycolysis through proton buffering; HIF1α upregulates GLUT1 and LDHA to promote glycolytic metabolism under hypoxia.
- bicarbonate transport and pH regulation. Genes: SLC4A4, CA2, CA10
  - [25]: SLC4A4 sodium-bicarbonate cotransporter and carbonic anhydrases work coordinately to regulate intracellular pH and buffer extracellular acidification.

**Required genes (not in input)**
- Genes: HIF1A, HIF2A, VEGFA, PDGFA, GLUT1, LDHA, PKM2, CAIX, PHD2, FIH
  - [60]: Master regulators of hypoxia response (HIF1A, HIF2A) and glycolytic enzymes (GLUT1, LDHA, PKM2) are essential components of metabolic adaptation program not represented in input gene list.

**Program citations**
- [60]: HIF1α and HIF2α regulate distinct aspects of hypoxia response; HIF1α responds acutely to hypoxia while HIF2α regulates tumor response to chronic hypoxia; both upregulate angiogenic factors.
- [57]: Hypoxia-induced radioresistance aggravated by positive feedback circuit of p21 and HIF-1α promoting Glut1/LDHA-mediated glycolysis.
- [25]: SLC4A4 plays protective role in glioma progression by regulating metabolic activities and represents potential therapeutic target.

## Program: Immune Modulation and Inflammatory Signaling
Gene program regulating immune cell recruitment, polarization, and immunosuppressive signaling in the glioblastoma microenvironment. IL1RAP, IL27RA, and IRAK2 coordinate interleukin signaling cascades that modulate innate and adaptive immunity. Neuropeptide receptors (NPY1R, NPR3) and other neuroimmune mediators influence microglial and macrophage phenotype. The program reflects the highly immunosuppressive glioblastoma microenvironment where tumor-associated macrophages (TAMs) and myeloid-derived suppressor cells (MDSCs) promote tumor progression and therapy resistance.

**Predicted impacts**
- Promotion of pro-tumor interleukin signaling (IL-1β, IL-27) supporting macrophage and myeloid-derived suppressor cell activation
- Enhanced NF-κB pathway activity in tumor-associated myeloid cells
- Neuroimmune modulation of microglial polarization toward pro-tumor M2 phenotype
- Recruitment and infiltration of immunosuppressive myeloid populations into tumor microenvironment
- Establishment of immunosuppressive tumor microenvironment limiting T cell infiltration and anti-tumor immunity

**Evidence summary**
The glioblastoma microenvironment is highly immunosuppressive with abundant tumor-associated macrophages (TAMs) that promote tumor progression. IL1RAP serves as accessory protein for IL-1 receptor and IL-1β signaling promotes GSC proliferation through bone marrow-derived monocyte crosstalk. IRAK2 is a kinase directly activated by IL-1R signaling and activates downstream NF-κB pathway, critical for macrophage pro-tumor polarization. IL27RA couples IL-27 cytokine signaling which can promote Th1 responses but also can support regulatory T cell development. Neuropeptide receptors (NPY1R, NPR3, GALR1, NTSR1) represent a less-characterized but potentially important layer of neuro-immune crosstalk in GBM. These receptors modulate cytokine production and immune cell polarization. GABBR2 represents GABA signaling which is known to suppress immune responses. The presence of multiple immune-modulating genes suggests that GBM hijacks neuroimmune signaling to establish an immunosuppressive microenvironment. However, mesenchymal GBM subtypes, which express high levels of immune infiltration markers, may respond better to immunotherapy.

**Atomic biological processes**
- interleukin receptor signaling. Genes: IL1RAP, IRAK2, IL27RA
  - [20]: IL-1β produced by bone marrow-derived monocytes promotes glioma stem-like cell proliferation; IL-1 receptor-associated kinase (IRAK) is downstream of IL-1 signaling.
- NF-κB pathway activation through IL-1 signaling. Genes: IRAK2
  - [20]: IL-1β signaling through IL-1 receptor activates NF-κB pathway in tumor-associated macrophages and microglia, promoting pro-tumor cytokine production.
- neuropeptide-mediated immune modulation. Genes: NPY1R, NPR3, GALR1, NTSR1
  - [45]: Neuropeptide receptors influence tumor microenvironment through neuroimmune interactions; NPY and neuropeptide signaling modulates macrophage polarization and cytokine production.

**Atomic cellular components**
- interleukin receptor complexes. Genes: IL1RAP, IL27RA
  - [20]: IL-1 receptor complex includes IL1RAP as accessory protein; IL-27RA combines with IL-27p28 to form functional IL-27 receptor on T cells and innate lymphoid cells.
- neuropeptide receptor signaling complexes. Genes: NPY1R, NPR3, GALR1, GABBR2, NTSR1
  - [45]: NPY1R and other neuropeptide receptors are G-protein coupled receptors that modulate second messenger signaling in immune cells and tumor microenvironment.

**Required genes (not in input)**
- Genes: IL1B, IL1A, IL27, IL27P28, TNF, IL6, IL10, TGFB1, STAT3, NFKB1, RELA
  - [20]: Pro-tumor cytokines (IL-1β, TNF, IL-6, IL-10, TGF-β) and transcription factors (STAT3, NF-κB) are essential for macrophage polarization but not represented in input gene list.

**Program citations**
- [20]: Tumor-associated macrophages (TAMs) promote glioma stem-like cell proliferation; IL-1β production by bone marrow-derived monocytes enhances GSC proliferation through IL-1 receptor signaling.
- [23]: Study confirmed importance of immune-related genes and immune infiltrates in predicting GBM patient prognosis; immune microenvironment critical component of GBM biology.

## Bibliography
1. Available from: https://maayanlab.cloud/Harmonizome/gene_set/glucose+metabolism+disease/GWASdb+SNP-Disease+Associations
2. Dominik K, Stephanie CF, Lukas K, Efe CS, Marita E, Lena E, et al.. TRPM8 is required for survival and radioresistance of glioblastoma cells.. Oncotarget [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/29221175/
3. Marsel K, Airat G, Yanis B, Karam K, Manuel F, Firat K, et al.. Signaling pathways and therapeutic approaches in glioblastoma multiforme (Review).. International journal of oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9084550/
4. Available from: https://patents.google.com/patent/US20210363525A1/en
5. Ochoa SV, Casas Z, Albarracín SL, Sutachan JJ, Torres YP. Therapeutic potential of TRPM8 channels in cancer treatment. Frontiers in Pharmacology [Internet]. 2023Mar22;14. Available from: https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2023.1098448/epub
6. Nomura M, Spitzer A, Johnson KC, Garofano L, Nehar-belaid D, Galili DN, et al.. The multilayered transcriptional architecture of glioblastoma ecosystems. Nature Genetics [Internet]. 2025May;57(5). Available from: https://www.nature.com/articles/s41588-025-02167-5
7. Guangyuan C, Zhonghua F, Xulin H, Zhaoli S. Malignant progression of MES-like cells mediated by COL22A1 in the spatial heterogeneity of glioblastoma.. Discover oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12500492/
8. Michael L, Nam-Gu H, Santosh K, Elmar N. WNT Signaling as a Therapeutic Target for Glioblastoma.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8395085/
9. Yunting Z, Maree JW, Gerardo MV, Frank AM, Paul TM, Cynthia SW. Molecular Evidence for Altered Angiogenesis in Neuroinflammation-Associated Schizophrenia and Bipolar Disorder Implicate an Abnormal Midbrain Blood-Brain Barrier.. Schizophrenia bulletin [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12236309/
10. Tian J, Zhao J, Xu Z, Liu B, Pu J, Li H, et al.. Bioinformatics analysis to identify key invasion related genes and construct a prognostic model for glioblastoma. Scientific Reports [Internet]. 2025Mar28;15(1). Available from: https://www.nature.com/articles/s41598-025-95067-x.pdf
11. Liu J, Xiao Q, Xiao J, Niu C, Li Y, Zhang X, et al.. Wnt/β-catenin signalling: function, biological mechanisms, and therapeutic opportunities. Signal Transduction and Targeted Therapy [Internet]. 2022Jan3;7(1). Available from: https://www.nature.com/articles/s41392-021-00762-6
12. Ping L, Lingyan H, Nan T, Xuchen Q. The evaluation of six genes combined value in glioma diagnosis and prognosis.. Journal of cancer research and clinical oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11797574/
13. Manali T, Jennifer H, Laura AN, Jasmin L, Nina J. Receptor Tyrosine Kinase Signaling and Targeting in Glioblastoma Multiforme.. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7918566/
14. Rafael B, Matheus D, Osvaldo M, Jurandir MRF, Rafael R, Marcelo ACF, et al.. Gene Expression of GABA. Brain sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969028/
15. Shiyang Z, Jingchen L, Qianxu J, Siyu Z, Hongshan Y, Yizheng W, et al.. CAMK2B Impacts the Proliferation, Invasion, and Migration of Glioma Cells via the Ras/Raf/MEK/ERK Signaling Pathway.. Oncology research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12493989/
16. Available from: https://brieflands.com/journals/jjcmb/articles/119223
17. Yang T, Maleeha AQ, Kevin RB, Nicholas M, Jason M, Sheila KS, et al.. Identification of five important genes to predict glioblastoma subtypes.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8577514/
18. Martijn JK, Martina PO, Nils ZB, Jolet E van de B, Minetta E-H, Enzo N, et al.. CAMK2-Dependent Signaling in Neurons Is Essential for Survival.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6616294/
19. Available from: https://www.remedypublications.com/open-access/integrin-alpha3-itga3-as-a-prognostic-marker-and-potential-therapeutic-9197.pdf
20. Zhihong C, Dolores H. Immune Microenvironment in Glioblastoma Subtypes.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5951930/
21. Available from: https://ecancer.org/en/news/27138-from-molecular-pathways-to-potential-treatments-targeting-epithelialmesenchymal-transition-in-glioblastoma
22. Junchao Y, Leilei W. Integrin α3 Mediates Stemness and Invasion of Glioblastoma by Regulating POU3F2.. Current protein & peptide science [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36843258/
23. Ping L, Yi C, He Z, Guihuai W. Predictive Analyses of Prognostic-Related Immune Genes and Immune Infiltrates for Glioblastoma.. Diagnostics (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7151008/
24. Jae KM, Seung AC, Seung-Ki K, Kyu-Chang W, Sung-Hye P. Snail plays an oncogenic role in glioblastoma by promoting epithelial mesenchymal transition.. International journal of clinical and experimental pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4069885/
25. Available from: https://academic.oup.com/neuro-oncology/article-abstract/25/Supplement_5/v27/7406476
26. Can X, Pengyu H, Xiang L, Menglin X, Ziqi Z, Ziru L, et al.. Comprehensive understanding of glioblastoma molecular phenotypes: classification, characteristics, and transition.. Cancer biology & medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11131044/
27. Alberto V, Nadia T, Gandino M, Fabrizio G, Massimiliano C, Orazio P, et al.. Different states of stemness of glioblastoma stem cells sustain glioblastoma subtypes indicating novel clinical biomarkers and high-efficacy customized therapies.. Journal of experimental & clinical cancer research : CR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10512479/
28. Zhiwei X, Jiwei W, Zide W, Junzhi L, Jiangli Z, Xuchen L, et al.. SLC25A32 promotes malignant progression of glioblastoma by activating PI3K-AKT signaling pathway.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10294537/
29. Singh S, Dey D, Barik D, Mohapatra I, Kim S, Sharma M, et al.. Glioblastoma at the crossroads: current understanding and future therapeutic horizons. Signal Transduction and Targeted Therapy [Internet]. 2025Jul9;10(1). Available from: https://www.nature.com/articles/s41392-025-02299-4
30. Christoph PB, Praveen K, Katharina M, Petra L, Valentin B, Ines A, et al.. The cancer stem cell subtype determines immune infiltration of glioblastoma.. Stem cells and development [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3464079/
31. Hongchao X, Beilin Z, Yinggui Y, Zihuang L, Pan Z, Weiqing W, et al.. LncRNA MIR4435-2HG potentiates the proliferation and invasion of glioblastoma cells via modulating miR-1224-5p/TGFBR2 axis.. Journal of cellular and molecular medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/32319715/
32. Saleh R, Esma'il A, Seyed EM, Maedeh B, Mohammad B. Early growth response 1 transcription factor and its context-dependent functions in glioblastoma.. Contemporary oncology (Poznan, Poland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480913/
33. Clara T, Johanna M, Hanane C, Soumyabrata G, Mathilde S, Amel B, et al.. DNA damage repair kinase DNA-PK and cGAS synergize to induce cancer-related inflammation in glioblastoma.. The EMBO journal [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36574362/
34. Available from: https://aacrjournals.org/mcr/article/16/10/1470/89825/LINC00152-Promotes-Invasion-through-a-3-Hairpin
35. Nathalie S, Laurent T, Aurélie B, Hélène H, Samah R, Fabrice L, et al.. A Positive Feed-forward Loop Associating EGR1 and PDGFA Promotes Proliferation and Self-renewal in Glioblastoma Stem Cells.. The Journal of biological chemistry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4865916/
36. Available from: https://www.igmm.cnrs.fr/wp-content/uploads/2025/09/EMBJ-42-e111961.pdf
37. Park H, Nam K-S, Lee H-J, Kim KS. Ionizing Radiation-Induced GDF15 Promotes Angiogenesis in Human Glioblastoma Models by Promoting VEGFA Expression Through p-MAPK1/SP1 Signaling. Frontiers in Oncology [Internet]. 2022Feb25;12. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.801230/full
38. Ella EA, Alexandra MD, Alireza S. Matrix Metalloproteinases in Glioma: Drivers of Invasion and Therapeutic Targets.. Biotech (Basel (Switzerland)) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12015896/
39. Bianca LM, Kathryn JB, Luis EP-B, Estrella V, Matthew SK, Hideaki S, et al.. Transcription factors ASCL1 and OLIG2 drive glioblastoma initiation and co-regulate tumor cell types and migration.. Nature communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/39609428/
40. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
41. Fu Y, Zhou Y, Wang K, Li Z, Kong W. Extracellular Matrix Interactome in Modulating Vascular Homeostasis and Remodeling. Circulation Research [Internet]. 2024Mar29;134(7). Available from: https://www.ahajournals.org/doi/10.1161/CIRCRESAHA.123.324055
42. Idoia G, Juncal A, Jelena MV, Paula A, Leire M-C, Sergio T-B, et al.. Oncogenic activity of SOX1 in glioblastoma.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5397861/
43. Couturier CP, Ayyadhury S, Le PU, Nadaf J, Monlong J, Riva G, et al.. Single-cell RNA-seq reveals that glioblastoma recapitulates a normal neurodevelopmental hierarchy. Nature Communications [Internet]. 2020Jul8;11(1). Available from: https://www.nature.com/articles/s41467-020-17186-5
44. Hao P, Renjie X, Yong Z. Role of SPRY4 in health and disease.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11056578/
45. Jinan B, Gaetano F, Gabi H. The landscape of the mesenchymal signature in brain tumours.. Brain : a journal of neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6485274/
46. Alba L, Luis GG-B, Julia LG-A, Conrado M-C, Maria AM-T. Neural Stem Cells as Potential Glioblastoma Cells of Origin.. Life (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10145968/
47. Jong-Whi P, Guido W, Carles U, Barbara F, Tullio F, Stephan G, et al.. Sprouty2 enhances the tumorigenic potential of glioblastoma cells.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6280149/
48. Riccardo B, Angela B. Role of Notch Signaling Pathway in Glioblastoma Pathogenesis.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
49. da SWA, Palma PVB, Sicchieri RD, Villacis RAR, Mandarano LRM, Oliveira TMG, et al.. Transcription Factor Networks derived from Breast Cancer Stem Cells control the immune response in the Basal subtype. Scientific Reports [Internet]. 2017Jun6;7(1). Available from: https://www.nature.com/articles/s41598-017-02761-6
50. Isabella W, Silvia T, Hideaki N, Urban D, Federica S, Fabien G, et al.. PECAM-1 Stabilizes Blood-Brain Barrier Integrity and Favors Paracellular T-Cell Diapedesis Across the Blood-Brain Barrier During Neuroinflammation.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6460670/
51. Available from: https://www.oncotarget.com/article/18117/text/
52. Mattia DP, Yusuke S, Owen PL, Nikos T. Transposable element dynamics in glioblastoma stem cells: insights from locus-specific quantification.. Mobile DNA [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12403600/
53. Sabrina D, Martina L, Olga TB, Martina G, Simona F, Muhlis A, et al.. Blood-brain barrier permeability increases with the differentiation of glioblastoma cells in vitro.. Fluids and barriers of the CNS [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11529439/
54. Zhixing W, Wanjun T, Jiangang Y, Boqin Q, Wei H, Xiaozhong P. Integrated Analysis of RNA-Binding Proteins in Glioma.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7226056/
55. Shirin I, Jasmine L, Miller H, Daniel JF, Robyn W, Aaron F, et al.. Glial progenitors as targets for transformation in glioma.. Advances in cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4270964/
56. Jin X, Kuang Y, Li L, Li H, Zhao T, He Y, et al.. A positive feedback circuit comprising p21 and HIF‐1α aggravates hypoxia‐induced radioresistance of glioblastoma by promoting Glut1/LDHA‐mediated glycolysis. The FASEB Journal [Internet]. 2022Feb24;36(3). Available from: https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fj.202101736R
57. Xu W, Jiang L, Chengkai Z, Xiudong G, Xingang L, Wang J, et al.. Old players and new insights: unraveling the role of RNA-binding proteins in brain tumors.. Theranostics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12036871/
58. Tian Y, Wang Z, Yang F, Zhang W, Li J, Yang L, et al.. Olig1/2 Orchestrates Progenitor Cell Fates during Mammalian Cortical Gliogenesis and Gliomagenesis. Nature Communications [Internet]. 2025Nov5;16(1). Available from: https://www.nature.com/articles/s41467-025-64753-9
59. Emir B, Hakija B, Amina D-K, Samra KV, Semir H, Alma M-A, et al.. Understanding the Significance of Hypoxia-Inducible Factors (HIFs) in Glioblastoma: A Systematic Review.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11171068/
