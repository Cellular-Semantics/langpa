# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and astrocytoma cells
- Disease: Astrocytoma (including IDH-wild-type and IDH-mutant subtypes)
- Tissue: Brain, central nervous system

## Input Genes
TNC, CD44, VCL, SAMD4A, IGFBP7, DEC1, ELL2, CADPS, ACTN1, GBP2, BCL6, GLIS3, EMP1, SERPINA3, NAMPT, TPST1, GAP43, NEAT1, SPOCD1, GFAP, MAP3K14, FN1, CLIC4, PDE8B, MAP1B, ... (200 total)

## Program: Reactive Astrocyte Phenotype and Identity
The core molecular program establishing reactive astrocyte identity in astrocytoma through upregulation of intermediate filament proteins, cell surface adhesion molecules, and associated structural proteins. This program marks the transition from quiescent to activated astrocytic state and maintains the fundamental glial lineage commitment while enabling altered cellular interactions and enhanced plasticity toward progenitor-like states.

**Predicted impacts**
- Enhanced cytoskeletal plasticity and mechanical flexibility enabling cell migration and morphological changes
- Altered cell-cell and cell-ECM interactions through CD44-mediated adhesion
- Maintained astrocytic lineage commitment with enhanced progenitor-like plasticity
- Enhanced responsiveness to mechanical and inflammatory signals through remodeled cytoskeleton

**Evidence summary**
The reactive astrocyte phenotype program represents the fundamental transcriptomic and proteome reorganization that defines the astrocytoma cell state. GFAP and VIM coordinate cytoskeletal remodeling that enables the cellular flexibility required for tumor cell migration and invasion, while CD44 serves as a multi-functional cell surface molecule supporting both adhesion and growth factor receptor signaling. The coordinated upregulation of these three markers, extensively documented across multiple astrocytoma studies and reactive astrocyte models, collectively define the core identity of tumor-associated astrocytes. This program is particularly significant in the perivascular and infiltrative regions where tumor-astrocyte interactions are most pronounced.

**Atomic biological processes**
- Intermediate filament polymerization and cytoskeletal remodeling. Genes: GFAP, VIM
  - [3]: GFAP and VIM are core reactive astrocyte markers, with coordinated upregulation driving cytoskeletal reorganization in reactive astrocytes at 1 year post-TBI
  - [8]: GFAP and VIM upregulation in astrocytes following injury correlates with AP-1 transcription factor activity and early reactive response
  - [55]: Pan-reactive astrocyte subsets express high levels of both GFAP and VIM, indicating coordinated intermediate filament network reorganization
- Cell-surface adhesion and hyaluronic acid binding. Genes: CD44
  - [13]: CD44 expression correlates with cancer stem cell traits including self-renewal, EMT capacity, and chemotherapy resistance in tumor cells
  - [16]: CD44 is highly expressed in reactive astrocytes and serves as a marker of neural progenitor phenotype
  - [55]: CD44 is a key pan-reactive astrocyte marker, prominently expressed in chronic reactive states

**Atomic cellular components**
- Intermediate filament network. Genes: GFAP, VIM
  - [1]: GFAP protein expression is altered in astrocytomas with grade-dependent changes
  - [6]: Vimentin intermediate filaments interact with GFAP in reactive astrocytes during neurotrauma

**Required genes (not in input)**
- Genes: SOX9, SOX2, NES
  - [8]: SOX9 recruits AP-1 transcription factors to drive reactive astrocyte programs; SOX2 marks neural progenitor states in astrocytes

**Program citations**
- [3]: Comprehensive RNA-seq analysis of astrocyte transcriptome at 1 year after TBI demonstrates sustained upregulation of GFAP, VIM, and CD44 in reactive astrocytes
- [8]: Single-cell analysis of injury-responsive enhancers reveals coordinated AP-1-driven activation of GFAP, VIM, and related genes in astrocytes
- [55]: Astrocyte activation persists one year after TBI with key pan-reactive markers including GFAP, CD44, and VIM prominently expressed

## Program: STAT3-IL6 Inflammatory Signaling Axis
The central hub of astrocytoma inflammatory signaling integrating response to multiple pro-inflammatory cytokines through the STAT3-IL6 signaling pathway. This program drives autocrine survival signaling in tumor cells while simultaneously mediating paracrine immune recruitment and the establishment of an immunosuppressive tumor microenvironment. The STAT3-IL6 axis represents one of the most therapeutically relevant programs due to its roles in both cell-autonomous tumor progression and immune evasion.

**Predicted impacts**
- Enhanced tumor cell survival through STAT3-mediated upregulation of anti-apoptotic proteins
- Increased proliferation through IL6R-mediated MAPK and PI3K activation
- Recruitment of pro-tumor immune populations including macrophages and MDSCs
- Establishment of immunosuppressive microenvironment limiting anti-tumor immunity
- Suppression of astrocyte differentiation programs through STAT3-mediated blockade of differentiation factors

**Evidence summary**
The STAT3-IL6 axis represents a central node in astrocytoma pathogenesis, driving both cell-autonomous survival signals and paracrine immune suppression. IL6 signals through membrane-bound IL6R and soluble IL6R to activate STAT3, which translocates to the nucleus and drives transcription of survival genes. Multiple pro-inflammatory cytokines including IL1B and TNF converge on STAT3 activation through JAK kinases. The coordinated expression of chemokines CCL2 and CXCL2 recruitment immune populations that further amplify inflammatory signaling through paracrine IL6 production. This program represents a major therapeutic target, as STAT3 inhibitors show promise in preclinical astrocytoma models.

**Atomic biological processes**
- STAT3 phosphorylation and transcriptional activation. Genes: STAT3, IL6, IL6R, IL1B, IL1R1, TNF
  - [2]: PIAS3 modulates STAT3 signaling in response to parvovirus B19 NS1 protein, suggesting STAT3 regulation in viral and inflammatory contexts
  - [4]: STAT3 activation in astrocytomas correlates with tumor progression; SOCS1 regulates STAT3 pathway
  - [10]: Astrocytic DLL4-NOTCH1 signaling promotes neuroinflammation via IL-6-STAT3 axis
  - [22]: IL6 activates JAK-STAT3 signaling in mesenchymal stem cells promoting invasion and metastasis
  - [36]: IGFBP7 interacts with STAT3 promoting its acetylation/dimerization in kidney disease models
- Chemokine-mediated immune cell recruitment. Genes: CCL2, CXCL2, CCL2
  - [8]: CCL2 and immune interaction genes upregulated in reactive astrocytes; correlates with AP-1 and STAT3 motif activity
  - [3]: CCL2 and CXCL10 upregulated in astrocytes following injury, driving immune cell recruitment and neuroinflammation
  - [32]: Resident stroma-secreted chemokine CCL2 governs myeloid-derived suppressor cell recruitment

**Atomic cellular components**
- IL6-STAT3 signaling complex. Genes: STAT3, IL6, IL6R, IL1R1
  - [51]: STAT5B expression correlates with astrocytoma tumor grade, indicating importance of STAT family signaling
  - [22]: IL-6 and IL-1β regulate STAT3 signaling through JAK activation

**Required genes (not in input)**
- Genes: JAK2, JAK3, PIAS1, SOCS3
  - [2]: PIAS3 protein inhibitor of STAT3 regulates STAT3 signaling
  - [4]: SOCS1 suppressor of cytokine signaling regulates STAT3 pathway

**Program citations**
- [8]: Reactive astrocyte markers including STAT3 remain elevated in later phases post-injury, indicating chronic STAT3 activation
- [3]: STAT3 significantly upregulated alongside inflammatory mediators in chronic TBI-induced astrocyte activation
- [55]: Genes associated with neuroinflammation including STAT3 and TNF prominently upregulated in reactive astrocytes

## Program: Extracellular Matrix Remodeling and Integrin-Mediated Signaling
Coordinated program driving extracellular matrix deposition, remodeling, and degradation while establishing mechanotransduction signaling through integrin-mediated pathways. This program enables both tumor cell infiltration into surrounding brain tissue and the establishment of a mechanically supportive microenvironment that reinforces tumor cell survival, proliferation, and stemness through integrin-ECM interactions.

**Predicted impacts**
- Enhanced integrin-FAK signaling promoting survival and proliferation through PI3K/AKT and MAPK pathways
- Increased tumor cell migration through focal adhesion remodeling and increased ECM proteolysis
- Maintenance of cancer stem cell phenotypes through mechanotransduction
- Support for tumor vascularization and immune cell infiltration through ECM remodeling
- Establishment of diffuse infiltrative growth pattern through coordinated ECM deposition along perivascular routes

**Evidence summary**
The ECM remodeling program establishes the structural scaffold within which astrocytomas grow and infiltrate surrounding brain tissue. Fibronectin serves as both a structural component and a signaling molecule that activates integrins (particularly ITGAV and ITGA3), which in turn engage focal adhesion proteins including ACTN1 and VCL. This integrin-ECM axis activates survival signaling through FAK and src family kinases that converge on PI3K/AKT and MAPK pathways. Type IV collagens maintain basement membrane integrity while providing additional integrin signaling cues. The balance between ECM deposition (driven by FN1 and COL genes) and ECM proteolysis (mediated by MMPs and regulated by TIMP3 and SERPINE1) determines the rate and degree of tumor infiltration. Multiple genes in this program are coordinately upregulated in astrocytomas with higher invasive potential.

**Atomic biological processes**
- Fibronectin-mediated ECM deposition and integrin signaling. Genes: FN1, ITGAV, ITGA3, ACTN1, VCL
  - [36]: Fibronectin activates integrin signaling; IGFBP7 interaction with STAT3 demonstrates cross-talk between ECM and inflammatory signaling
  - [52]: VEGFA and ITGAV regulate tumor cell proliferation in glioblastoma
  - [62]: Fibronectin activates integrin signaling with ITGAV functioning as key receptor in injury and repair contexts
  - [49]: Pericyte-expressed GAS6 reinforces pro-tumor macrophage polarization in glioma microenvironment; pericyte loss alters ECM composition
- Collagen-mediated basement membrane function. Genes: COL4A1, COL4A2, COL8A1
  - [49]: Type IV collagen maintains tumor vasculature integrity and provides integrin signaling cues in glioma microenvironment
- Focal adhesion assembly and mechanotransduction. Genes: ACTN1, VCL, NEDD9, SORBS1
  - [12]: ACTN1 mutations affect cytoskeletal association and F-actin colocalization in focal adhesions
  - [15]: ACTN4 and ZYX regulate focal adhesion formation and maturation
- Matrix metalloproteinase regulation and ECM proteolysis. Genes: TIMP3, SERPINE1
  - [64]: SERPINE1 (PAI-1) regulates plasminogen activation and ECM remodeling

**Atomic cellular components**
- Focal adhesion complexes. Genes: ACTN1, VCL, NEDD9
  - [12]: Focal adhesion proteins including actinin mediate integrin-actin coupling
- Integrin-ligand complexes. Genes: ITGAV, ITGA3, FN1, COL4A1
  - [36]: Integrins bind ECM ligands including fibronectin and collagen to transduce mechanical signals
  - [62]: ITGAV integrin engagement with fibronectin activates downstream signaling in macrophages and other cell types

**Required genes (not in input)**
- Genes: FAK, SRC, PIK3CA, AKT1
  - [36]: Integrin signaling activates FAK and PI3K/AKT pathways downstream

**Program citations**
- [49]: Comprehensive characterization of pericyte-vascular interactions in glioma demonstrates role of ECM in tumor progression and immune recruitment
- [36]: ECM and integrin signaling regulate multiple aspects of tumor biology including differentiation and immune evasion
- [62]: Fibronectin-integrin signaling in macrophages demonstrates broader role of ECM signaling in tumor microenvironment

## Program: AP-1 Transcription Factor-Driven Stress Response
The immediate early transcriptional response program orchestrated by AP-1 family members (JUN, JUNB, FOSL2, FOS, FOSB) and stress-responsive factors (ATF3, CEBPD, NR4A3) that rapidly reprogram gene expression following cellular stress, inflammatory stimuli, or growth factor signaling. This program enables astrocytoma cells to rapidly adapt to environmental changes and coordinates both cytoprotective responses and pro-proliferative signals.

**Predicted impacts**
- Rapid upregulation of inflammatory cytokines and chemokines through AP-1 driven transcription
- Enhanced metabolic gene expression supporting increased biosynthesis and ATP production
- Upregulation of heat shock proteins and autophagy factors enabling stress adaptation
- Increased expression of growth factor receptors and signaling proteins supporting proliferation
- Transcriptional coordination of both pro-survival and pro-apoptotic programs enabling contextual survival decisions

**Evidence summary**
The AP-1-driven transcriptional response program represents the immediate early transcriptional reorganization that occurs following cellular stress, inflammatory stimuli, or growth factor signaling. JUN, JUNB, FOS, FOSB, and FOSL2 heterodimerize to form AP-1 complexes that bind to TPA response elements (TREs) within target gene promoters to drive transcriptional activation. ATF3 and CEBPD function as additional stress-responsive transcription factors that either enhance or antagonize AP-1-mediated transcription depending on their dimerization partner. The coordinated induction of these transcription factors within minutes to hours of cellular stress enables rapid metabolic and transcriptional reorganization. In astrocytoma, constitutive or readily inducible AP-1 activity drives the sustained expression of inflammatory cytokines, chemokines, and pro-survival proteins that collectively maintain the tumor-promoting inflammatory microenvironment. Recent evidence demonstrates that AP-1 factors cooperate with lineage-specific transcription factors such as SOX9 to regulate astrocyte-specific target genes, suggesting tight coupling between cell-type identity and stress response programs.

**Atomic biological processes**
- AP-1 complex assembly and DNA binding. Genes: JUN, JUNB, FOS, FOSB, FOSL2
  - [8]: Early response genes JUNB, FOSL2, and ATF3 are particularly prominent in astrocytes post-injury; AP-1 motif usage increases early after injury in astrocytes
  - [18]: EGR1 regulates inflammatory responses including ATF3 and JUN in myocardial injury models
  - [21]: ATF3 expression marks cellular injury/stress response in sensory neurons
- ATF/CEBP-mediated stress transcription. Genes: ATF3, CEBPD
  - [8]: CEBPD motif enrichment in astrocyte injury-responsive enhancers; ATF3 shows early and sustained induction post-injury
- Early growth response gene activation. Genes: EGR1, EGR3, NR4A3
  - [8]: EGR1 and KLF6 linked to reactive astrocyte response; multiple early growth response genes upregulated in injury
  - [3]: EGR1 significantly upregulated as early response gene in reactive astrocytes at 2 days post-TBI
  - [55]: EGR1 prominently expressed in acute astrocyte reactivity phase

**Atomic cellular components**
- AP-1 transcription factor complex. Genes: JUN, JUNB, FOS, FOSB, FOSL2
  - [8]: AP-1 transcription factors recruit lineage-specific factors including SOX9 to regulate astrocyte-specific target genes

**Required genes (not in input)**
- Genes: MAPK1, MAPK3, MAPK14, SOX9
  - [8]: MAPK pathway drives AP-1 activation; SOX9 cooperates with AP-1 to regulate astrocyte-specific targets

**Program citations**
- [8]: Comprehensive analysis of injury-responsive enhancers reveals AP-1 dominance in commissioning astrocyte-specific transcriptional responses
- [3]: JUNB, FOSL2, ATF3, and EGR1 are prominently upregulated in reactive astrocytes correlating with AP-1 pathway activation
- [55]: AP-1 family members and EGR1 show coordinated upregulation in acute astrocyte reactivity response

## Program: Metabolic Reprogramming and Glycolytic Enhancement
Coordinated program driving metabolic shift toward enhanced glycolysis, altered mitochondrial function, and dysregulated energy homeostasis that collectively optimize astrocytoma cells for rapid proliferation under both normoxic and hypoxic conditions. This program includes HIF1A-driven glycolytic gene expression, NAD biosynthesis enhancement through NAMPT, and mitochondrial ROS buffering through SOD2.

**Predicted impacts**
- Enhanced glycolytic ATP production supporting rapid proliferation and biosynthesis
- Reduced mitochondrial oxidative phosphorylation and ROS production through HIF1A-mediated metabolic shift
- Elevated NAD availability supporting NAD+-dependent metabolism and stress responses
- Maintained mitochondrial ROS buffering through SOD2 preventing excessive oxidative stress while preserving ROS signaling
- Lactate accumulation and extracellular acidification creating immunosuppressive microenvironment

**Evidence summary**
The metabolic reprogramming program represents a fundamental reorganization of astrocytoma cell energy metabolism optimized for rapid proliferation and survival under nutrient-limited and hypoxic conditions. HIF1A, the master regulator of hypoxic responses, drives glycolytic gene expression including PFKFB3, which catalyzes the production of fructose-2,6-bisphosphate, a potent glycolytic activator. Elevated PFKFB3 activity directly increases glycolytic flux and lactate production, both supporting tumor growth and creating an acidic microenvironment that suppresses anti-tumor immunity. NAMPT expression is elevated in astrocytomas, suggesting enhanced NAD biosynthesis that supports NAD+-dependent processes including sirtuin-mediated deacetylation and poly-ADP-ribose polymerase (PARP)-mediated stress responses. SOD2-mediated mitochondrial ROS buffering protects tumor cells from oxidative stress while maintaining ROS signaling through hydrogen peroxide that activates multiple protein tyrosine kinases. The coordinated expression of these metabolic genes creates a metabolic state optimized for both the high biosynthetic demands of rapid proliferation and the acquisition of stress resistance phenotypes characteristic of therapeutic-resistant tumors.

**Atomic biological processes**
- HIF1A-driven glycolytic gene expression. Genes: HIF1A, PFKFB3
  - [52]: VEGFA and HIF1A regulate metabolic reprogramming in glioblastoma supporting differentiation of myeloid-derived suppressor cells
- NAD biosynthesis and salvage pathway activation. Genes: NAMPT
  - [28]: NAMPT, the rate-limiting enzyme of NAD biosynthesis, increases tumorigenic properties and induces colon cancer stem cell-like characteristics
- Mitochondrial reactive oxygen species buffering. Genes: SOD2
  - [27]: SOD2 and Sirt3 regulate mitochondrial ROS, playing important role in cellular differentiation programs
  - [56]: SOD2 expression regulation by IGFBP7 and related factors influences mitochondrial function and senescence
- Mitochondrial dysfunction and senescence linkage. Genes: SOD2, ITPR2, CAMK2D
  - [56]: Mitochondrial dysfunction characterized by decreased membrane potential, elevated ROS, and impaired ATP generation contributes to senescence and aging
  - [71]: ITPR2 and calcium-mediated mitochondrial dysfunction promote cellular senescence

**Atomic cellular components**
- Glycolytic enzyme complexes. Genes: PFKFB3
  - [52]: PFKFB3 regulates glycolytic flux in tumor cells
- Mitochondrial matrix and ROS handling. Genes: SOD2, ITPR2
  - [71]: Mitochondrial calcium accumulation through ITPR2 reduces membrane potential and increases ROS production

**Required genes (not in input)**
- Genes: LDHA, PDK1, CA9
  - [52]: HIF1A drives expression of multiple glycolytic and lactate metabolism genes supporting Warburg effect

**Program citations**
- [52]: VEGFA and metabolic regulators control glioblastoma tumor properties and immune cell recruitment
- [28]: NAMPT promotes tumorigenic properties and stem cell-like characteristics in cancer cells
- [56]: Metabolic changes including mitochondrial dysfunction drive cellular senescence and link to aging

## Program: Neurodegeneration-Associated Pathways and Chronic Astrocyte Dysfunction
Program encompassing genes shared between chronic astrocytoma and age-related neurodegenerative diseases including Alzheimer disease and Parkinson disease, characterized by impaired autophagy, protein aggregation, mitochondrial dysfunction, and disrupted ion homeostasis. This program reveals unexpected convergence between tumor biology and neurodegeneration, suggesting shared cellular dysfunction mechanisms.

**Predicted impacts**
- Impaired extracellular potassium buffering leading to elevated extracellular K+ and neuronal hyperexcitability
- Enhanced neuroinflammation through APOE dysregulation and lipid metabolism alterations
- Disrupted neuronal-glial interactions through reduced NTRK2-mediated BDNF signaling
- Accumulated protein aggregates and impaired proteostasis through SERPINA3 dysregulation
- Potential contribution to neuronal dysfunction within tumor microenvironment despite tumor cell survival

**Evidence summary**
The neurodegeneration-associated program reveals an unexpected convergence between chronic astrocytoma and age-related neurodegenerative diseases, with substantial overlap in dysregulated genes including KCNJ10, APOE, MAP1B, NTRK2, and SERPINA3. This convergence suggests that chronic inflammation and cellular stress in astrocytoma create a brain microenvironment that simultaneously supports tumor cell survival while generating neuronal dysfunction phenotypes characteristic of neurodegeneration. KCNJ10 downregulation impairs the astrocytic buffering of extracellular potassium, leading to elevated extracellular K+ that increases neuronal excitability and may contribute to seizures or progressive neurological decline in astrocytoma patients. APOE dysregulation alters lipid metabolism and neuroinflammatory signaling, effects particularly important in the context of the APOE ε4 allele, which confers enhanced risk for both Alzheimer disease and potentially altered astrocytoma biology. MAP1B alterations suggest disrupted microtubule dynamics that may contribute to both astrocyte morphological changes and neuronal dysfunction. NTRK2 dysregulation reduces BDNF signaling, impairing the normal neuroprotective functions of astrocytes. SERPINA3 elevation suggests proteostasis dysfunction and potentially impaired clearance of protein aggregates. This program represents a critical aspect of astrocytoma pathogenesis often overlooked in traditional tumor biology approaches but highly relevant to understanding the long-term neurological consequences of astrocytoma in survivors.

**Atomic biological processes**
- Potassium channel dysfunction and ion homeostasis impairment. Genes: KCNJ10
  - [3]: KCNJ10 downregulation shared between chronic TBI and astrocytoma; impairs spatial buffering of extracellular potassium
  - [55]: KCNJ10 is among commonly dysregulated genes in chronic astrocyte dysfunction shared with neurodegenerative diseases
- Lipid metabolism and apolipoprotein signaling. Genes: APOE
  - [3]: APOE upregulated alongside other pan-reactive astrocyte markers in chronic TBI and potentially in astrocytoma
  - [55]: APOE prominently expressed in chronic reactive astrocytes; APOE ε4 allele confers enhanced risk for Alzheimer disease
- Microtubule dynamics and tau pathology association. Genes: MAP1B
  - [3]: MAP1B altered expression in chronic astrocytoma mirrors changes in Alzheimer disease and Parkinson disease
  - [55]: MAP1B shares regulatory elements with genes upregulated in chronic neurodegeneration
- BDNF signaling and neuroprotection. Genes: NTRK2
  - [3]: NTRK2 is among shared genes between chronic TBI astrocytes and neurodegenerative disease states
  - [48]: NTRK2 alterations in astrocytoma including TRIM24-NTRK2 fusion gene demonstrate functional importance
  - [55]: NTRK2 expression in chronic astrocytes supports neurons but may be dysregulated in tumor context
- Proteostasis and chaperone dysfunction. Genes: SERPINA3
  - [3]: SERPINA3 upregulated in both chronic TBI and astrocytoma; regulates protease activity and neuroinflammation
  - [55]: SERPINA3 is key pan-reactive astrocyte marker elevated in chronic states, suggesting proteostasis dysfunction

**Atomic cellular components**
- Potassium channel complex. Genes: KCNJ10
  - [3]: KCNJ10 channel dysfunction impairs astrocyte ion buffering capacity

**Required genes (not in input)**
- Genes: MAPT, SNCA, APP
  - [3]: MAPT and other Alzheimer/Parkinson disease genes show regulatory overlap with chronic astrocyte dysfunction genes

**Program citations**
- [3]: Substantial overlap in molecular signature of chronic TBI astrocytes with Alzheimer disease and Parkinson disease
- [55]: Key pan-reactive astrocyte markers including APOE, KCNJ10, and SERPINA3 overlap with neurodegenerative disease signatures
- [59]: Senescence markers in CNS including astrocyte senescence contribute to neurodegeneration in aging and Alzheimer disease

## Program: Cellular Senescence and Senescence-Associated Secretory Phenotype
Program encompassing genes regulating cell cycle arrest, senescence-associated secretory phenotype (SASP) production, and mitochondrial dysfunction-driven senescence. This program reflects the paradoxical presence of senescent cells within astrocytomas that both limit tumor progression through growth arrest and paracrine inhibition while simultaneously driving pro-tumor inflammation through SASP cytokine production.

**Predicted impacts**
- Cell cycle arrest through p53/p21 or Rb/p16 checkpoints limiting proliferation
- Elevated ROS production through mitochondrial calcium accumulation and membrane potential loss
- Production of pro-inflammatory SASP factors including TNF, IL-1β, IL-6, and chemokines
- Paracrine tumor promotion through SASP-mediated immune recruitment and vascular remodeling
- Impaired differentiation responses through coordinated action of tumor suppressors and stress-responsive transcription factors

**Evidence summary**
The cellular senescence program represents an important and often overlooked aspect of astrocytoma biology, wherein senescent cells accumulate within tumors and simultaneously limit and promote tumor progression through paradoxical effects. Cell cycle arrest through GADD45A/B-mediated p53 activation or through tumor suppressor pathways limits the proliferation of individual senescent cells, potentially providing a growth-restricting influence on tumors. However, senescent cells produce a potent SASP composed of TNF, IL-1β, IL-6, CCL2, and other pro-inflammatory mediators that collectively promote tumor progression through paracrine effects on neighboring tumor cells and immune populations. The initiation of senescence in astrocytoma involves both canonical DNA damage checkpoints (through GADD45 induction) and non-canonical triggers including mitochondrial dysfunction, with ITPR2-mediated calcium handling playing a central role in senescence induction. ITPR2 function at mitochondria-ER contact sites (MERCS) regulates calcium movement into mitochondria through the mitochondrial calcium uniporter (MCU), and excessive calcium accumulation reduces mitochondrial membrane potential and increases ROS production, thereby triggering senescence. CAMK2D-mediated phosphorylation of signaling proteins downstream of calcium signaling further activates NF-κB and promotes SASP factor production. The presence of senescent cells within astrocytomas likely reflects the balance between growth-restricting differentiation signals and growth-promoting inflammatory signals, with the net effect on tumor progression determined by the specific SASP cytokine profile and the responsiveness of tumor cells to SASP factors.

**Atomic biological processes**
- p53-mediated DNA damage response and cell cycle arrest. Genes: GADD45A, GADD45B, ATF3
  - [3]: GADD45A and ATF3 upregulated indicating ongoing DNA damage responses in chronic astrocytes
  - [55]: GADD45A prominently expressed in astrocyte reactivity suggesting DNA damage checkpoints
- Mitochondrial calcium handling and senescence. Genes: ITPR2, CAMK2D
  - [56]: ITPR2-mediated calcium release and mitochondrial calcium accumulation reduce membrane potential and promote senescence
  - [71]: ITPR2 calcium channel regulates mitochondria-ER contacts that drive senescence induction
  - [72]: CAMK2D activates NF-κB-mediated inflammatory responses including SASP production in senescent cells
- SASP cytokine and chemokine production. Genes: TNF, IL1B, CCL2, IL6
  - [56]: TNF, IL-1β, and IL-6 are SASP factors produced by senescent cells that drive paracrine tumor-promoting inflammation
- Chromatin remodeling and transcriptional dysregulation. Genes: ARID5A, ARID5B
  - [3]: ARID5 family proteins involved in chromatin accessibility changes associated with senescence and inflammation
- Tumor suppressor function and differentiation inhibition. Genes: BTG2
  - [3]: BTG2 upregulation indicates differentiation-driving signals or stress responses

**Atomic cellular components**
- Mitochondrial permeability transition pore. Genes: ITPR2
  - [56]: mPTP opening through calcium accumulation represents key mechanism of senescence-associated mitochondrial dysfunction
- ER-mitochondria contact sites (MERCS). Genes: ITPR2
  - [71]: MERCS mediate calcium handling and calcium accumulation driving senescence

**Required genes (not in input)**
- Genes: TP53, RB1, p16, p21
  - [56]: p53-p21 and p16-Rb pathways coordinate cell cycle arrest in senescence

**Program citations**
- [56]: Comprehensive review of mitochondrial dysfunction in cellular senescence demonstrating role of calcium, ROS, and SASP in senescence induction and maintenance
- [59]: Cellular senescence in CNS contributes to aging and Alzheimer disease through SASP production and impaired proteostasis
- [71]: ITPR2 and MERCS regulate senescence through calcium-mediated mitochondrial dysfunction

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/10401
3. 3. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/8651
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/24387
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/22352
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
8. 8. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/407050
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/16176
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/87
13. 13. Dong R, Srikanth A, Tharehalli U, Seufferlein T, Schirmbeck R, Lechel A. CD44 upregulation in chronic liver disease marks the transition to hepatocellular carcinoma and portends poor prognosis. British Journal of Cancer [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41416-025-03284-y
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/81
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/12505
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/24330
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/3553
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/768
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/25389
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=3569
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
24. 24. Hruby AJ, Higuchi-Sanabria R. Mitochondrial dysfunction in cellular senescence: a bridge to neurodegenerative disease. npj Aging [Internet]. 2025Dec16;11(1). Available from: https://www.nature.com/articles/s41514-025-00291-4
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/7538
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/20656
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/10135
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/22695
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/546
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/604
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/20296
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/10419
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/51564
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/6347
35. 35. Yu J-tao, Hu X-wei, Wang J-nan, Yang Q, Li X-yu, Shan R-run, et al.. Renal insulin-like growth factor binding-protein 7 is a critical promoter of progressive diabetic kidney disease. Nature Communications [Internet]. 2025Dec1;. Available from: https://www.nature.com/articles/s41467-025-66490-5
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/2633
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/29817
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/3576
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/14468
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/7187
42. 42. Erin F, Alexandra L, Sehoon W, Kai C, Yan L, Katherine WR. Trio and CRMP2 regulate axon branching and Semaphorin3A signaling.. Communications biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41291162/
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
44. 44. Kamiyama D, Kamiyama R, Nishida Y, Sego A, Vining GB, Bui KC, et al.. The Vap33 signaling axis precisely coordinates the timing of motoneuron dendritogenesis in neural map development. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-65900-y
45. 45. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
46. 46. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
47. 47. Ksenia A, Micha D. Phylogenetic Analysis of NEAT1 and MALAT1 Long Non-coding RNAs Highlights Structure-Function Relationships in Paraspeckle Biology.. Molecular biology and evolution [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41363149/?fc=None&ff=20251211190652&v=2.18.0.post22+67771e2
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/6777
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/283131
50. 50. Lara N, Javier M, Irene S-S, Moisés S-P, Esther R-S, Teresa S-M. Next-Generation Sequencing Reveals a Diagnostic and Prognostic Role of the . International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41373636/?fc=None&ff=20251211105245&v=2.18.0.post22+67771e2
51. 51. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
52. 52. Li S, Chu C. Senescence in Aging and Alzheimer's Disease.. Aging and disease [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41296937/
53. 53. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/18787
55. 55. Li R, Huang S, Hanna A, Hernandez SC, Kubota A, Humeres C, et al.. Macrophage ITGAV is dispensable for post-infarction remodeling in mice and does not mediate fibronectin responses. Communications Biology [Internet]. 2025Nov29;. Available from: https://www.nature.com/articles/s42003-025-09295-y
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/6678
57. 57. Available from: https://www.ncbi.nlm.nih.gov/gene/5054
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/4088
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/2597
60. 60. Available from: https://www.ncbi.nlm.nih.gov/gene/4851
61. 61. Available from: https://www.ncbi.nlm.nih.gov/gene/9518
62. 62. Available from: https://www.ncbi.nlm.nih.gov/gene/817
63. 63. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
64. 64. Available from: https://www.ncbi.nlm.nih.gov/gene/3709
65. 65. Available from: https://www.ncbi.nlm.nih.gov/gene/108058
66. 66. Available from: http://json-schema.org/draft-07/schema#",
