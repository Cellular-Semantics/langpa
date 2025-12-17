# Gene Program Markdown Report

## Context
- Cell type: glioblastoma cells
- Disease: glioblastoma (GBM)
- Tissue: brain

## Input Genes
POSTN, KIAA1211L, CPNE4, HMGA2, TRPM8, CYTOR, RGS6, RPH3A, CCN4, ADAMTS9-AS1, SPRY1, LEF1, VAT1L, COL22A1, MIR4435-2HG, AC000065.1, CPED1, ARHGAP6, TRPM3, ANGPT1, ALK, CA2, SERPINE1, CHRM3-AS2, ITGA3, ... (118 total)

## Program: Epithelial-Mesenchymal Transition
Coordinated upregulation of mesenchymal transcription factors and downregulation of epithelial adhesion molecules, driving acquisition of migratory and invasive phenotypes in GBM. This program involves transcriptional reprogramming through WNT pathway activation, canonical EMT transcription factors, and matrix remodeling, representing a reversible plastic state induced by microenvironmental cues such as hypoxia and inflammatory signals.

**Predicted impacts**
- Shift from epithelial-like to mesenchymal phenotype with enhanced motility
- Increased expression of invasion-promoting proteases and reduced cell-cell adhesion
- Acquisition of stemness markers and therapeutic resistance
- Enhanced propensity for migration into surrounding brain tissue

**Evidence summary**
EMT is a reversible process in GBM driven by microenvironmental signals (hypoxia, TGF-β, inflammatory cytokines) that involves coordinated transcriptional changes mediated by LEF1 and Wnt signaling, as well as cytoskeletal remodeling through integrin-FAK interactions. Multiple genes in the input list (LEF1, ITGA3, IQGAP2, ARHGAP family members, matrix metalloproteinases) collectively support active EMT programming. The presence of genes encoding cell adhesion molecules, ECM remodelers, and signaling effectors indicates a functionally complete EMT program.

**Atomic biological processes**
- Transcriptional reprogramming via WNT/beta-catenin signaling. Genes: LEF1, WNT16
  - [19]: LEF1 plays key role in stem cell maintenance and EMT process, promoting cell migration and invasion of GBM. HOXA13 promotes glioma progression via Wnt- and TGF-β-induced EMT
  - [22]: WNT3a, WNT5a, WNT7a function as ligands in signaling pathways. WNT5a stimulation induces migration of glioblastoma cells via beta-catenin independent signaling and MMP2 activation
- Focal adhesion and cytoskeletal remodeling. Genes: ITGA3, IQGAP2, RHOJ, ARHGAP26, ARHGAP6, WIPF3
  - [8]: Integrin alpha3 contributes to invasive nature of GSCs via ERK1/2 signaling, promoting glioma migration and invasion through focal adhesion signaling
  - [46]: Tetraspanin CD151 is important in maintaining balance between RhoA and Rac-1 signalling. Integrins are major partners of tetraspanins in controlling cell adhesion and migration
- Matrix metalloproteinase activation and ECM degradation. Genes: ADAM19, ADAMTS9-AS1, SERPINE1, PLAT
  - [14]: EMT in GBM results in increased expression of proteases that increase invasiveness into surrounding normal brain. ZEB proteins suppress E-cadherin and promote invasion
  - [29]: Collagen genes were significantly involved in EMT process of glioma. High expression of collagen genes showed significantly poor prognosis

**Atomic cellular components**
- Cell-cell adhesion molecules. Genes: CDH4
  - [50]: Cadherins are calcium-binding proteins with pivotal role in cell adhesion. Cadherin switch is hallmark of EMT in gliomas, with complex non-binary expression patterns
  - [53]: E- and N-cadherin co-expression identified GBM subgroup with frequent epithelial differentiation and significant survival benefit

**Required genes (not in input)**
- Genes: SNAI1, SNAI2, TWIST1, ZEB1, ZEB2, TGFB1, SMAD2, SMAD3, ERK1/2, NOTCH1
  - [14]: ZEB proteins bind E-cadherin promoter and suppress expression. TGF-β induces EMT through Smad or p38 MAPK pathways. NOTCH signaling involved in EMT in GBM

**Program citations**
- [14]: Glioma cells undergoing EMT acquire potential to initiate metastasis and invasion, highly affected by tumor microenvironment
- [17]: EMT is reversible biological process in epithelial cells, epigenetic mechanisms more crucial than genetic changes
- [9]: Transcriptome changes in glioma NS formation show upregulation of EMT genes, invasion and migration markers

## Program: Calcium-Mediated Proliferation and Survival
Coordinated activation of calcium/calmodulin-dependent signaling pathways that promote GBM cell proliferation, invasion, and therapeutic resistance. Involves calcium-permeable glutamate receptor activation, calcium/calmodulin-dependent protein kinases, and downstream effector pathways including MAPK/ERK and PI3K/AKT signaling. This program couples cellular excitability to oncogenic signaling.

**Predicted impacts**
- Enhanced intracellular calcium dynamics and sustained calcium signaling
- Activation of MAPK/ERK and AKT/mTOR proliferative pathways
- Increased cell proliferation and reduced apoptosis
- Enhanced invasive and migratory capacity of tumor cells
- Coupling of neuronal signaling to glioma survival and growth

**Evidence summary**
Multiple calcium-permeable ion channels and calcium-dependent kinases in the input list collectively support robust calcium-mediated proliferation and survival signaling in GBM. The presence of glutamate receptors (GRM7), GABA receptors (GABBR2), calmodulin-dependent kinases (CAMK2B, CAMK2A), and various ion channels (TRPM8, TRPM3, SLC genes) indicates that this tumor exploits both normal neuronal calcium signaling and aberrant ion transport to enhance malignant properties. CAMK2B has established negative correlation with proliferation, while its knockdown activates pro-proliferative pathways, suggesting the input list captures both oncogenic and suppressive calcium signaling components.

**Atomic biological processes**
- Calcium influx through ionotropic glutamate receptors. Genes: GRM7, GLRA2
  - [38]: GBM cells express elevated levels of AMPAR (alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptors), with Ca2+ influx triggering proliferation and migration. Silencing GluR1 subunit disrupts AMPA-driven signaling and suppresses glioma growth
  - [49]: Glutamatergic and calcium signaling provide positive feedback to promote glioma formation through metabolic reprogramming and genetic switching
  - [52]: GBM tumor-initiating cells express high concentrations of functional calcium-permeable AMPA receptors compared to differentiated tumor cultures
- Calcium/calmodulin-dependent protein kinase signaling. Genes: CAMK2B, CAMK2A, RCAN1
  - [15]: CAMK2B inhibits glioma proliferation, invasion, and migration through Ras/Raf/MEK/ERK pathway. Knockdown leads to activation of this pathway
  - [18]: Ca2+/CaM-dependent kinase family members are overexpressed in cancer and control cell proliferation, migration, invasion and survival
- GABA receptor signaling and neuronal-tumor crosstalk. Genes: GABBR2
  - [38]: GABAergic synaptic activity facilitates glioma growth. GABAA receptor activation has heterogeneous effects - can curb or sustain glioma proliferation depending on receptor subunits and context
- Ion transport and cellular excitability. Genes: TRPM8, TRPM3, CA2, CA10, SLC4A4, SLC24A2, SLC18A1
  - [2]: GJB2 and SCN9A knockdown in patient-derived glioblastoma cells induces transcriptome-wide changes involving neuron projection and proliferation pathways, impairs cell viability and tumor sphere formation

**Atomic cellular components**
- Ion channels and transporters. Genes: TRPM8, TRPM3, CA2, CA10, SLC4A4, SLC24A2, SLC18A1
  - [2]: Ion transport proteins encoding genes are aberrantly activated in GBM as pan-cancer feature defining tumor heterogeneity
- Calcium-binding and buffering proteins. Genes: RCAN1
  - [49]: Calcium commands large network of signaling regulators that determine cell fate. Exaggerated calcium signaling drives transformation and progression via enhanced metabolism and invasion

**Required genes (not in input)**
- Genes: GRIA1, GRIA4, GRIN1, GRIN2A, GRIN2D, GABRA1, mGluR5, CaMKK, PP2B
  - [49]: CaMK2A intimately interacts with most types of GluRs (GRIA1-4, GRIK2, GRIN1, GRIN2A-D) and these are involved in GBM pathology

**Program citations**
- [38]: Dynamic and complex interplay between synaptic communication and brain cancer progression is critical frontier in understanding tumor growth in brain's microenvironment
- [49]: Glutamatergic and calcium signaling may provide positive feedback to promote glioma formation

## Program: Glioma Stem Cell Maintenance
Transcriptional and post-transcriptional regulation of self-renewal capacity, stemness marker expression, and resistance to differentiation in glioblastoma stem cells. This program involves transcription factors that maintain pluripotency-like states, Wnt/Notch signaling, and epigenetic regulation. Glioma stem cells are characterized by high tumorigenicity, self-renewal, invasiveness, and therapy resistance.

**Predicted impacts**
- Sustained self-renewal and clonogenic capacity of GBM stem cells
- Resistance to differentiation and maintenance of pluripotency-like state
- Enhanced tumorigenicity and intracranial tumor formation
- Increased invasiveness and metastatic potential
- Elevated resistance to chemo- and radiotherapy

**Evidence summary**
The input list contains multiple key regulators of GSC stemness, including HMGA2 (highly expressed in neurosphere-enriched cells and associated with enhanced tumorigenicity), EGR1 (orchestrates stemness marker expression through PDGFA signaling), and transcription factors involved in Wnt/Notch pathways (LEF1, WNT16, JAG1). HMGA2 depletion leads to decreased stemness, invasion, and tumorigenicity. EGR1 expression is restricted to proliferating/progenitor cells in GBM tissue. The presence of multiple growth factor signaling components (PDGFD, growth factor receptors) and stemness-associated transcription factors suggests this program is functionally complete and active in the input gene set.

**Atomic biological processes**
- Stemness transcription factor regulation. Genes: EGR1, EGR3, HMGA2, HOPX
  - [20]: EGR1 contributes to stemness marker expression and proliferation by orchestrating PDGFA-dependent growth stimulatory loop. EGR1 regulates SHH, GLI1, GLI2, and PDGFA essential for GSC maintenance and proliferation
  - [23]: EGR3 promotes GBM cell growth and is associated with upregulation of MYC and CDK1, transcription factors associated with enhanced cell proliferation
- Wnt/Notch pathway signaling in stem cell maintenance. Genes: LEF1, WNT16, JAG1
  - [19]: LEF1 plays key role in stem cell maintenance and EMT, promoting cell migration and invasion. ASCL1 maintains GSCs by repressing DKK-1 to promote WNT signaling and GSC survival
  - [25]: TNC is pivotal initiator of enhanced NOTCH signaling and promotes GSC growth through TNC-α2β1-JAG1-NOTCH signaling axis
- Growth factor signaling loops. Genes: EGR1, PDGFD, SOX1-OT
  - [9]: SOX2-dependent activation creates unified basis for processes of intercellular interaction via FGF and TGF-beta/SMAD signaling pathways during NS formation
  - [20]: EGR1 orchestrates PDGFA-dependent growth-stimulatory loop essential for GSC proliferation
- Cell cycle progression and proliferation. Genes: EGR1, EGR3, HMGA2, CAMK2B
  - [23]: EGR3 upregulates MYC and CDK1 to promote GBM cell growth
  - [15]: CAMK2B overexpression leads to ~40% reduction in proliferative capacity of glioma cells

**Atomic cellular components**
- Transcriptional co-activators. Genes: HMGA2, EGR1, HOPX
  - [45]: HMGA2 is a transcriptional modulator that mediates motility and self-renewal in cancer stem cells. High expression in majority of GBM tumors

**Required genes (not in input)**
- Genes: SOX2, NESTIN, CD133, NANOG, SHH, GLI1, GLI2, NOTCH1, NICD, TCF4
  - [20]: EGR1 directly regulates stemness markers SOX2, NANOG, SHH, GLI1, GLI2 essential for GSC maintenance

**Program citations**
- [45]: HMGA2 promotes stemness, invasion, and tumorigenicity in GBM. Targeting HMGA2 may be therapeutically beneficial
- [20]: EGR1 expression frequent in GBM and restricted to proliferating/progenitor cells. EGR1 essential for GSC proliferation

## Program: Integrin-Mediated Cell Invasion
Coordinated signaling through integrin receptors and their interaction with extracellular matrix components to promote GBM cell migration, invasion, and adhesion dynamics. Involves integrin clustering, focal adhesion kinase signaling, and activation of downstream kinase cascades that control cytoskeletal organization and enable penetration through tissue barriers.

**Predicted impacts**
- Enhanced migration and invasion through ECM
- Increased focal adhesion dynamics enabling rapid cell motility
- Sustained ERK1/2 signaling promoting invasive phenotype
- Penetration of blood-brain barrier and peritumoral invasion
- Dynamic regulation of cell adhesion-deadhesion cycles

**Evidence summary**
The input list contains ITGA3 (integrin alpha3), which is highly expressed in glioma stem-like cells and associated with invasion via ERK1/2 signaling. ITGA3 overexpression increases migration and invasion while knockdown inhibits these processes. SNED1 mediates cell adhesion through RGD-binding integrins. Multiple Ras/Rho GTPase regulators (RHOJ, ARHGAP26, ARHGAP6) and Rac effectors (IQGAP2, WIPF3) support a functionally complete integrin-mediated invasion program. SPRY genes provide feedback inhibition of RTK pathways downstream of integrin signaling.

**Atomic biological processes**
- Integrin-ECM binding and focal adhesion assembly. Genes: ITGA3, SNED1, IQGAP2
  - [8]: Integrin α3 highly expressed in glioma stem-like cells and localizes in invading cells and cells surrounding vessels. Integrin α3 expression positively correlates with invasion activity
  - [31]: SNED1 mediates cell adhesion via RGD motif through RGD-binding integrins α5β1 and αvβ3
- ERK1/2 pathway activation downstream of integrin signaling. Genes: ITGA3, CAMK2B, SPRY1, SPRY2, SPRY4
  - [8]: Integrin α3 promotes glioma cell invasion via ERK1/2 signaling. MEK/ERK inhibition completely abrogates integrin α3-induced invasion
  - [15]: CAMK2B inhibits Ras/Raf/MEK/ERK pathway. Knockdown activates this pathway promoting proliferation and migration
- Cytoskeletal reorganization and cell polarity. Genes: ITGA3, IQGAP2, RHOJ, ARHGAP26, ARHGAP6, WIPF3
  - [9]: RAS through TIAM1 regulates cytoskeletal organization and cell migration in GBM
  - [46]: Tetraspanin-integrin interactions control cell adhesion and migration through effects on cytoskeleton

**Atomic cellular components**
- Integrin receptors and associated proteins. Genes: ITGA3, SNED1
  - [8]: Integrin α3 is overexpressed in glioma cells and contributes to invasive phenotype
- Focal adhesion kinase and adaptor proteins. Genes: IQGAP2, WIPF3
  - [46]: Tetraspanins regulate focal adhesion assembly and disassembly

**Required genes (not in input)**
- Genes: FAK, SRC, p130CAS, RAC1, ROCK, PAK
  - [8]: FAK acts downstream of integrins and is pivotal mediator of integrin-induced migration

**Program citations**
- [8]: Integrin α3 is prime candidate for anti-invasion therapy for GBM
- [31]: SNED1 is required for neural crest cell migration and necessary for metastatic dissemination of tumor cells

## Program: Extracellular Matrix Remodeling
Coordinated expression and modification of extracellular matrix proteins including collagens, proteoglycans, and matricellular proteins, coupled with protease activity to reshape the tumor microenvironment. This program supports cell adhesion turnover, angiogenesis, immune infiltration, and establishment of a permissive environment for tumor progression and invasion.

**Predicted impacts**
- Enhanced deposition of collagen scaffold around tumor cells
- Increased proteolytic activity remodeling ECM architecture
- Modified heparan sulfate composition affecting growth factor bioavailability
- Creation of permissive microenvironment for tumor cell migration and invasion
- Altered immune cell infiltration through ECM remodeling

**Evidence summary**
The input list contains multiple collagen genes (COL22A1, COL23A1, COL25A1, COL27A1, COL19A1) and matricellular proteins (POSTN, SNED1) known to be dysregulated in GBM. Six collagen genes are established regulators of immunosuppressive microenvironment and EMT in glioma. ADAM19 and ADAMTS9-AS1 mediate protease-based ECM degradation. HS3ST5 modifies heparan sulfate composition affecting signaling. These genes collectively support a functionally complete ECM remodeling program characteristic of aggressive GBM with enhanced invasive capacity.

**Atomic biological processes**
- Collagen deposition and cross-linking. Genes: COL22A1, COL23A1, COL25A1, COL27A1, COL19A1
  - [26]: 6 collagen genes (COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2) regulate immunosuppressive microenvironment of glioma and are involved in EMT process
  - [29]: Collagen is most important component of ECM acting as scaffold for tumor cell adhesion. Identified specific collagen genes correlated with glioma survival
- Matricellular protein expression. Genes: POSTN
  - [25]: TNC is highly expressed in glioma tissue and plays crucial role in cell migration, invasion, angiogenesis, and proliferation. TNC promotes adhesion and migration through integrin binding
  - [12]: Matrisome-high GBM tumors show enrichment of CMPs in vascular and leading edge structures harboring glioma stem cells
- Protease secretion and ECM degradation. Genes: ADAM19, ADAMTS9-AS1
  - [57]: ADAM family proteases including ADAM8, ADAM9, ADAM10, ADAM12, ADAM17, ADAM19 are implicated in proliferation, invasion, and angiogenesis in gliomas
- Heparan sulfate proteoglycan modification. Genes: HS3ST5
  - [39]: Heparanase (HPSE) high cells show elevated expression in GBM. HPSE inhibition reduces tumor cell invasion and adhesion. HS modification regulates cell signaling and invasion
  - [42]: Dysregulated heparan sulfate proteoglycan metabolism promotes tumor growth. Targeting proteoglycan metabolism reduces ERK1/2 signaling and tumorigenicity

**Atomic cellular components**
- Collagen molecules. Genes: COL22A1, COL23A1, COL25A1, COL27A1, COL19A1
  - [26]: Multiple collagen genes (COL1A1, COL1A2, COL3A1, COL4A1, COL4A2, COL5A2) identified as candidate key genes for glioma progression
- Matricellular proteins. Genes: POSTN, SNED1
  - [25]: Periostin detected as promoter of TNC incorporation into ECM and to organize ECM architecture
- Glycosaminoglycan biosynthesis. Genes: HS3ST5
  - [39]: HS GAGs determine specificity and affinity of HSPG ligand interactions through sulfation pattern

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP1, TIMP2, TGFB1, VEGF, FIBRONECTIN, LAMININ
  - [29]: ECM comprises numerous proteins including collagen, proteoglycans, laminin, and fibronectin as essential components

**Program citations**
- [26]: Collagen genes could serve as potential therapeutic targets for glioma management
- [12]: Matrisome-high GBM associated with worse prognosis and identified prognostic matrix code defines functional GBM subtypes

## Program: Receptor Tyrosine Kinase Signaling
Coordinated regulation of growth factor signaling through EGFR, PDGFR, ALK, and related receptor tyrosine kinases coupled with feedback inhibition mechanisms. This program drives proliferation, survival, and invasion through MAPK/ERK and PI3K/AKT pathways, with importance for maintaining tumor growth and establishing therapeutic resistance.

**Predicted impacts**
- Enhanced growth factor-driven proliferation via MAPK/ERK activation
- Sustained survival signaling through PI3K/AKT pathways
- Increased invasive and migratory capacity
- Resistance to differentiation and maintenance of stemness
- Therapeutic resistance through redundant signaling pathways

**Evidence summary**
The input list contains multiple key RTK signaling components: FHL2 (EGFR-interacting protein), EGR1 (mediates PDGFA signaling), ALK (receptor tyrosine kinase with established GBM fusions), SPRY genes (feedback inhibitors of RTK signaling), and CAMK2 proteins (negative regulators of Ras/Raf/MEK/ERK). FHL2 interacts directly with EGFR and promotes GBM growth; depletion inhibits proliferation and migration. ALK fusions are present in 12% of gliomas and activate STAT3/ERK pathways. SPRY genes provide essential feedback regulation. This program is functionally complete and represents major driver of GBM proliferation.

**Atomic biological processes**
- EGFR-FHL2 signaling axis. Genes: FHL2, TFCP2L1
  - [21]: FHL2 interacts with EGFR to promote glioblastoma growth. Targeting FHL2 with RNA interference inhibits glioblastoma cell proliferation and migration
  - [24]: FHL2 is four-and-a-half-LIM protein 2 interacting with EGFR to promote GBM growth
- PDGF signaling in stem cell maintenance. Genes: EGR1, PDGFD
  - [20]: EGR1 orchestrates PDGFA-dependent growth-stimulatory loop. PDGFA activation maintains GSC proliferation and stemness
- ALK fusion signaling. Genes: ALK
  - [7]: ALK aberrations detected in 12% of gliomas. ALK fusions promote STAT3 and ERK1/2 pathways. ALK-fused GBM models responsive to ALK inhibitors
- MAPK/ERK pathway activation and feedback inhibition. Genes: SPRY1, SPRY2, SPRY4, CAMK2B, CAMK2A
  - [9]: SPRY4, ERRFI1, RAB31 are EGFR and FGFR signaling feedback regulators found in all analyzed gliomas and can be used for creating therapeutic strategies
  - [15]: CAMK2B suppresses Ras/Raf/MEK/ERK signaling pathway. Knockdown leads to pathway activation promoting proliferation and invasion
- Proprotein convertase inhibition. Genes: PCSK5
  - [51]: PCSK5 upregulated in GBM tissues correlates with advanced stages and worse prognosis. PCSK5 knockdown attenuates EMT properties and reduces p-STAT3 and MMPs expression

**Atomic cellular components**
- Receptor tyrosine kinases. Genes: ALK, FHL2
  - [7]: ALK protein minimally expressed in normal forebrain. ALK fusions present in congenital and pediatric GBMs as primary driver alterations
- MAPK kinase cascades. Genes: SPRY1, SPRY2, SPRY4, CAMK2B
  - [15]: Ras/Raf/MEK/ERK signaling pathway central to GBM proliferation and invasion

**Required genes (not in input)**
- Genes: EGFR, PDGFRA, MET, IGF1R, SHP2, PI3K, AKT, RAF, MEK, ERK
  - [7]: ALK fusions co-occur with other oncogenic drivers like EGFR alterations in adult GBMs

**Program citations**
- [21]: Targeting FHL2 represents novel strategy for EGFR-positive GBM therapy
- [7]: ALK inhibitors show responsiveness in ALK-fused GBM cellular and mouse models including patient-derived cells

## Program: Immune Microenvironment Modulation
Expression of immunomodulatory genes that suppress anti-tumor immune responses and promote immune cell recruitment to create an immunosuppressive tumor microenvironment. Includes genes encoding cytokines, cytokine receptors, immune checkpoint molecules, and factors affecting immune cell differentiation and function.

**Predicted impacts**
- Recruitment and polarization of immunosuppressive myeloid cells
- Reduced anti-tumor T cell and NK cell function
- Enhanced tumor escape from immune surveillance
- Increased expression of immune checkpoint ligands
- Establishment of immunosuppressive tumor microenvironment supporting tumor progression

**Evidence summary**
The input list contains GDF15 (TGF-β superfamily cytokine upregulated in malignant glioma phenotypes), METTL7B (negatively regulates immunity and promotes immunosuppressive microenvironment), and cytokine receptors (IL27RA, IL1RAP). High GDF15 expression predicts poor survival especially in lower-grade glioma and is closely correlated with inflammatory response, infiltrating immune cells, and immune checkpoint molecules. GDF15 downregulates IL-12 receptor on NK cells promoting NK cell dysfunction. METTL7B high expression associated with abundant immunosuppressive cells and upregulation of immune checkpoints. These genes collectively support active immunosuppressive programming in GBM.

**Atomic biological processes**
- Inflammatory cytokine signaling. Genes: GDF15
  - [13]: GDF15 closely related to inflammatory response and infiltrating immune cells. High GDF15 predicted poor survival in LGG. GDF15 regulates IL-12 receptor beta2 on NK cells promoting NK cell dysfunction
  - [16]: GDF15 plays important role in GSC radioresistance. GDF15 expression critical for GSC spheroid formation
- IL-1 and IL-27 receptor signaling. Genes: IL27RA, IL1RAP, IRAK2
  - [37]: Three cytokine receptors expressed on glioblastoma: IL17RE, IL27RA, and IL1RAP
- Immune checkpoint regulation and METTL7B-mediated immunosuppression. Genes: METTL7B
  - [44]: METTL7B is essential regulator of lineage specification in glioblastoma with impact on tumor size and survival
  - [47]: High METTL7B expression associated with abundant immunosuppressive cells and poor prognosis. METTL7B negatively regulates immunity and promotes immunosuppressive microenvironment through upregulation of immune checkpoints and immunosuppressive cytokines
- M2 macrophage polarization and recruitment. Genes: GDF15, METTL7B
  - [12]: M-H matrisome subgroup shows enrichment of transcripts associated with leukocyte migration and activation. Higher CSF1R:CSF1 pair in M-H subgroup consistent with M2 macrophage enrichment

**Atomic cellular components**
- Cytokine and chemokine molecules. Genes: GDF15, PDGFD
  - [13]: GDF15 is cytokine belonging to TGF-β superfamily involved in crucial inflammatory and immune response
- Cytokine receptors. Genes: IL27RA, IL1RAP
  - [37]: IL27RA and IL1RAP are cytokine receptors expressed on glioblastoma

**Required genes (not in input)**
- Genes: IL6, TNFα, IL10, TGFβ, PDL1, PDL2, CTLA4, IDO, ARG1
  - [47]: 31 upregulated immunosuppressive genes and immune checkpoints analyzed in high METTL7B cohort

**Program citations**
- [13]: GDF15 could serve as interesting prognostic biomarker for glioma
- [47]: METTL7B presents clinical prognostic value and METTL7B-related prognostic signature predicts overall survival of glioma patients

## Program: Cuproptosis and Metabolic Reprogramming
Regulation of copper-dependent cell death pathways (cuproptosis) and metabolic shifts supporting tumor aggressiveness. Involves genes regulating copper homeostasis, lipoylation of metabolic enzymes, and mitochondrial function. Recent evidence suggests cuproptosis as alternative tumor suppression mechanism distinct from apoptosis and ferroptosis.

**Predicted impacts**
- Enhanced sensitivity to copper-induced cell death pathways
- Altered mitochondrial metabolism and oxidative stress
- Potential therapeutic vulnerability through cuproptosis induction
- Metabolic reprogramming supporting tumor growth

**Evidence summary**
COL22A1 identified in recent study as cuproptosis-related gene serving as therapeutic target. COL22A1 silencing enhances GBM cuproptosis. Targeting COL22A1 with kaempferol (natural compound from Ginseng) reduces GBM cell proliferation and sensitizes cells to cuproptosis induction. While limited genes from input list directly involved in cuproptosis, COL22A1 represents emerging therapeutic target for exploiting alternative cell death pathways in GBM.

**Atomic biological processes**
- Cuproptosis-related gene expression. Genes: COL22A1
  - [3]: COL22A1 identified as target of kaempferol in cuproptosis pathway. COL22A1 silencing enhances glioblastoma cuproptosis. Kaempferol could decrease proliferation of GBM cells by inhibiting COL22A1 expression
- Metabolic enzyme lipoylation. Genes: COL22A1
  - [3]: Cuproptosis-related prognostic model identified through bioinformatics. Cuproptosis serves important role in tumors with implications for prognosis and treatment

**Required genes (not in input)**
- Genes: SLC31A1, FDX1, LIPT1, DLD, DLAT, PDH
  - [3]: Solute carrier family 31 member 1 selected as potential cuproptosis-related gene in cancer

**Program citations**
- [3]: COL22A1 revealed as cuproptosis-related combined regimen target for GBM with potential therapeutic benefit

## Program: Tetraspanin-Mediated Cell Adhesion
Coordinated regulation of tetraspanin proteins that mediate cell-cell adhesion, cell-ECM interactions, and formation of specialized membrane microdomains. Tetraspanins function as adaptor proteins connecting surface receptors to cytoskeletal and signaling machinery, with roles in tumor heterogeneity and immune microenvironment formation.

**Predicted impacts**
- Enhanced cell-ECM adhesion through integrin-tetraspanin complexes
- Facilitation of EMT through tetraspanin-mediated signaling
- Regulation of immune cell infiltration patterns
- Promotion of cell migration and invasion
- Modulation of tumor microenvironment composition

**Evidence summary**
TSPAN18 is present in input list among 18 tetraspanin family members significantly upregulated in GBM. Multiple tetraspanins (TSPAN3/4/6/11/18/24/25/26/29/30) are prognostic factors with high expression associated with poor survival. Tetraspanins promote EMT through enhanced signaling, regulate immune cell infiltration patterns, and mediate integrin-ECM interactions. TSPAN4 knockdown strongly inhibits proliferation, invasion, and migration. Tetraspanins represent emerging therapeutic targets for GBM through dual effects on tumor cells and immune microenvironment.

**Atomic biological processes**
- Tetraspanin-integrin complex formation. Genes: TSPAN18
  - [43]: TSPAN3/4/6/11/12/18/23/24/25/26/27/28/29/30/31 significantly upregulated in GBM. TSPAN-mediated cell adhesion and migration. TSPAN2/4/5/9/11/18/22/25/26/28/32 associated with EMT pathway activation
  - [46]: Tetraspanins are major partners of integrins and interact with wide range of ECM proteins. α3β1-tetraspanin protein complex linked to invasive phenotype via modulation of signaling pathways including MMP-2 activation
- EMT pathway modulation. Genes: TSPAN18
  - [43]: TSPAN2/4/5/9/11/18/22/25/26/28/32 significantly associated with activation of EMT pathway, critical pathway for cancer cell metastasis
- Immune infiltration and tumor microenvironment formation. Genes: TSPAN18
  - [43]: TSPAN family closely associated with immune infiltration of GBM. Cell abundance of resting dendritic cells, M0/M2 macrophages, gamma-delta T cells affected by TSPAN expression

**Atomic cellular components**
- Tetraspanin proteins. Genes: TSPAN18
  - [43]: Tetraspanins are integral membrane proteins forming specialized microdomains. TSPAN4 is independent prognostic factor - knockdown strongly inhibits glioma cell proliferation, invasion, and migration

**Required genes (not in input)**
- Genes: TSPAN1, TSPAN2, TSPAN3, TSPAN4, TSPAN5, TSPAN6, TSPAN8
  - [43]: Comprehensive study analyzed 32 tetraspanin family members with 18 significantly upregulated in GBM

**Program citations**
- [43]: Tetraspanins comprehensively elaborate prognostic value and potential role in GBM pathological mechanisms and tumor microenvironment remodeling

## Program: Transcriptional Regulation of Differentiation
Control of neural differentiation states and lineage specification through transcription factors that balance stem cell maintenance with differentiation. Involves genes regulating neural progenitor fate decisions, astrocytic differentiation, and oligodendrocytic commitment, which determine tumor cell plasticity and phenotypic heterogeneity in GBM.

**Predicted impacts**
- Balanced control of stem cell maintenance versus differentiation
- Phenotypic heterogeneity within tumor cell population
- Plasticity enabling adaptation to environmental stresses
- Modulation of mesenchymal versus proneural differentiation states
- Potential for therapeutic targeting of differentiation pathways

**Evidence summary**
HOPX is transcription factor recently identified as regulator of differentiation and proliferation states in GBM. Knockout of HOPX leads to transition toward mesenchymal-like states with decreased proneural signature activation. HOPX acts as co-effector through interactions with other transcription factors. SOX1-OT (long non-coding RNA) likely involved in neural differentiation pathways. These genes support control of lineage specification and plasticity in GBM, relevant to understanding tumor heterogeneity and phenotypic adaptation.

**Atomic biological processes**
- Lineage specification and differentiation control. Genes: HOPX
  - [32]: HOPX identified as regulator of differentiation and proliferation states in diffusely invading GBM. Knockout of HOPX in GBM led to transition toward mesenchymal-like states with decreased activation of developmental and proneural signatures
- Neural progenitor differentiation. Genes: SOX1-OT, HOPX
  - [9]: SOX2, UBTF, NFE2L2, TCF3, STAT3 identified as common transcriptional factors responsible for upregulation of genes involved in EMT, cancer stemness, invasion and migration of GBM
- Developmental pathway regulation. Genes: HOPX
  - [35]: HOPX recently identified as one of regulators of differentiation and proliferation states in diffusely invading glioblastoma multiforme cells

**Atomic cellular components**
- Transcription factors controlling differentiation. Genes: HOPX, SOX1-OT
  - [32]: HOPX is smallest member of homeodomain protein family lacking DNA-binding domain, acts as co-effector interacting with other transcription factors like SRF and GATA6

**Required genes (not in input)**
- Genes: SOX2, SOX9, OLIG1, OLIG2, NG2, PDGFRA, GFAP
  - [9]: SOX2 identified as common transcriptional factor in all analyzed gliomas controlling genes involved in stemness and differentiation

**Program citations**
- [32]: HOPX has recently been identified as one of regulators of differentiation and proliferation states in GBM

## Bibliography
1. Available from: https://patents.google.com/patent/US20210363525A1/en
2. Alexander TB, Hyun-Kee M, Masroor B, Hongyu Z, Alexander F, Weifan D, et al.. Pan-cancer ion transport signature reveals functional regulators of glioblastoma aggression.. The EMBO journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10897389/
3. Yi C, Ye Z, Huilan Y, Qiang L, Rui S, Ji S, et al.. Targeting the cuproptosis‑associated gene COL22A1 in glioblastoma using EMD‑1204831 and kaempferol.. International journal of oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12068844/
4. Available from: https://isomirtar.hse.ru
5. Available from: https://ouci.dntb.gov.ua/en/works/4YdZYqP7/
6. Hongchao X, Beilin Z, Yinggui Y, Zihuang L, Pan Z, Weiqing W, et al.. LncRNA MIR4435-2HG potentiates the proliferation and invasion of glioblastoma cells via modulating miR-1224-5p/TGFBR2 axis.. Journal of cellular and molecular medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/32319715/
7. Anne-Florence B, Ross G, Maya SG, Guadalupe G, Seth M, Jared KW, et al.. ALK Amplification and Rearrangements Are Recurrent Targetable Events in Congenital and Adult Glioblastoma.. Clinical cancer research : an official journal of the American Association for Cancer Research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36780194/
8. M N, E N, N F, Y Y, T T, Y H, et al.. Integrin α3 is overexpressed in glioma stem-like cells and promotes invasion.. British journal of cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3694230/
9. Natalia SV, Elena VK, Maya AD, Yulya IS, Nikita DZ, Alisa BA, et al.. Transcriptome Changes in Glioma Cells Cultivated under Conditions of Neurosphere Formation.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9563256/
10. Available from: https://patents.google.com/patent/WO2021216460A1/en
11. Available from: https://patents.google.com/patent/US20170088898A1/en
12. Monika V, Zeynep D, Zheng Y, Elisabeth KK, Meric K, Kisan T, et al.. A prognostic matrix code defines functional glioblastoma phenotypes and niches.. bioRxiv : the preprint server for biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10274725/
13. Longbin G, Yulei C, Shushu H, Lianxuan G, Nan T, Rongping L, et al.. GDF15 expression in glioma is associated with malignant progression, immune microenvironment, and serves as a prognostic factor.. CNS neuroscience & therapeutics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8673705/
14. Yasuo I. Epithelial-mesenchymal transition in glioblastoma progression.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4774466/
15. Shiyang Z, Jingchen L, Qianxu J, Siyu Z, Hongshan Y, Yizheng W, et al.. CAMK2B Impacts the Proliferation, Invasion, and Migration of Glioma Cells via the Ras/Raf/MEK/ERK Signaling Pathway.. Oncology research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12493989/
16. Alexandre B-R, Yvan N, Caroline D, Valérie G-A, Elizabeth C-J-M, Catherine S. Overexpression of Growth Differentiation Factor 15 in Glioblastoma Stem Cells Promotes Their Radioresistance.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10778311/
17. Yasuo I. Epithelial-mesenchymal transition in glioblastoma progression.. Oncology letters [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26998052/
18. Joshua SB, Kathryn AS. The Multi-Functional Calcium/Calmodulin Stimulated Protein Kinase (CaMK) Family: Emerging Targets for Anti-Cancer Therapeutic Intervention.. Pharmaceuticals (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6469190/
19. Mariachiara Z, Patricia G, Sihana Z, Marzia C, Patrizia DI, Francesco C, et al.. The Role of Wnt Signal in Glioblastoma Development and Progression: A Possible New Pharmacological Target for the Therapy of This Tumor.. Genes [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5852601/
20. Nathalie S, Laurent T, Aurélie B, Hélène H, Samah R, Fabrice L, et al.. A Positive Feed-forward Loop Associating EGR1 and PDGFA Promotes Proliferation and Self-renewal in Glioblastoma Stem Cells.. The Journal of biological chemistry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4865916/
21. Lili S, Qing L, Ming L. Targeting FHL2 for EGFRvIII-positive glioblastoma.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6298400/
22. McCord M, Mukouyama Y-suke, Gilbert MR, Jackson S. Targeting WNT Signaling for Multifaceted Glioblastoma Therapy. Frontiers in Cellular Neuroscience [Internet]. 2017Oct13;11. Available from: https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2017.00318/full
23. Chia-Wei C, Yi-Chin C, Yin-Cheng H, Yi-Chuan C. EGR3 Promotes Glioblastoma Cell Growth with Upregulation of MYC and CDK1.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40649712/
24. Lili S, Shuye Y, Hui X, Yanwen Z, Juntang L, Meiyan W, et al.. FHL2 interacts with EGFR to promote glioblastoma growth.. Oncogene [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8691187/
25. Fu Z, Zhu G, Luo C, Chen Z, Dou Z, Chen Y, et al.. Matricellular protein tenascin C: Implications in glioma progression, gliomagenesis, and treatment. Frontiers in Oncology [Internet]. 2022Aug12;12. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.971462/full
26. Lucas CB, Gabriel CM, Manoela H, Valéria PF. Identification of established and novel extracellular matrix components in glioblastoma as targets for angiogenesis and prognosis.. Neurogenetics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/38775886/
27. Rui M, Dong H, Kaitao Z, Yang L, Xiaomei Z, Yi C, et al.. VAV3 regulates glioblastoma cell proliferation, migration, invasion and cancer stem‑like cell self‑renewal.. Molecular medicine reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10073803/
28. Nicole B, Andreas F. Role of tenascins in the ECM of gliomas.. Cell adhesion & migration [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4422794/
29. Wen Y, Hecheng Z, Jun T, Zhaoqi X, Quanwei Z, Yudong C, et al.. Identification of collagen genes related to immune infiltration and epithelial-mesenchymal transition in glioma.. Cancer cell international [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8147444/
30. Rui M, Dong H, Kaitao Z, Yang L, Xiaomei Z, Yi C, et al.. VAV3 regulates glioblastoma cell proliferation, migration, invasion and cancer stem‑like cell self‑renewal.. Molecular medicine reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36960857/
31. Dharma P, Nandini K, Alexandra N. The novel ECM protein SNED1 mediates cell adhesion via the RGD-binding integrins α5β1 and αvβ3.. Journal of cell science [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/39713860/
32. Fabian M, Miljana N, Alexander B, Tim S, Susanne L, Nikolaus G, et al.. Beyond Tumor Suppression: The Multifaceted Functions of HOPX in Tissue Differentiation, Metabolism, and Immunity.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12608687/
33. Margot CD, Eric HM, Timothy RR, Ezequiel MF de V, Runbo G, Anna ML, et al.. RGS6 negatively regulates inhibitory G protein signaling in dopamine neurons and positively regulates binge-like alcohol consumption in mice.. British journal of pharmacology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36929333/
34. Zhendong L, Ruotian Z, Zhenying S, Jiawei Y, Penglei Y, Xin C, et al.. Identification of hub genes and small-molecule compounds in medulloblastoma by integrated bioinformatic analyses.. PeerJ [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7164431/
35. Doroszko M, Stockgard R, Uppman I, Heinold J, Voukelatou F, Mangukiya HB, et al.. The invasion phenotypes of glioblastoma depend on plastic and reprogrammable cell states. Nature Communications [Internet]. 2025Jul19;16(1). Available from: https://www.nature.com/articles/s41467-025-61999-1
36. Zhang Y, Zhao Y, Song X, Luo H, Sun J, Han C, et al.. Modulation of Stem Cells as Therapeutics for Severe Mental Disorders and Cognitive Impairments. Frontiers in Psychiatry [Internet]. 2020Apr30;11. Available from: https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2020.00080/pdf
37. Orentas RJ, Yang JJ, Wen X, Wei JS, Mackall CL, Khan J. Identification of Cell Surface Proteins as Potential Immunotherapy Targets in 12 Pediatric Cancers. Frontiers in Oncology [Internet]. 2012;2. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2012.00194/full
38. Jayanta M, Jason TH. Neurotransmitter power plays: the synaptic communication nexus shaping brain cancer.. Acta neuropathologica communications [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12042361/
39. Vy MT, Anna W, Andrew M, Katharine C, Olle RL, Jane RE, et al.. Heparan Sulfate Glycosaminoglycans in Glioblastoma Promote Tumor Invasion.. Molecular cancer research : MCR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6059807/
40. Artem DB, Laila MP, David C, Craig PW, Andrea DT, Nancy WL, et al.. Sox2 promotes malignancy in glioblastoma by regulating plasticity and astrocytic differentiation.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4094829/
41. Ingvild LG, Keagan D, Kristian M, Maike K, Nicola PM, Hinako K, et al.. Postnatal persistence of hippocampal Cajal-Retzius cells has a crucial role in the establishment of the hippocampal circuit.. Development (Cambridge, England) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10820737/
42. Available from: https://elifesciences.org/articles/69734
43. Li Y-C, Wu Y, Chen G, Zhu L-Z, Luo X, Nie Q-Q, et al.. Tetraspanins predict the prognosis and characterize the tumor immune microenvironment of glioblastoma. Scientific Reports [Internet]. 2023Aug16;13(1). Available from: https://www.nature.com/articles/s41598-023-40425-w
44. Myrianni C, James N, Xinyu Z, Eleni M, Sara L, Gabriel R, et al.. Lineage specification in glioblastoma is regulated by METTL7B.. Cell reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/38848215/
45. Harpreet K, Sabeen ZA, Lauren H, Marianne H-C, Isabella T, Xing-Gang M, et al.. The transcriptional modulator HMGA2 promotes stemness and tumorigenicity in glioblastoma.. Cancer letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
46. S D, E DW, M WP, A GF. Tetraspanins as regulators of the tumour microenvironment: implications for metastasis and therapeutic strategies.. British journal of pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4290697/
47. Chen X, Li C, Li Y, Wu S, Liu W, Lin T, et al.. Characterization of METTL7B to Evaluate TME and Predict Prognosis by Integrative Analysis of Multi-Omics Data in Glioma. Frontiers in Molecular Biosciences [Internet]. 2021Sep17;8. Available from: https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2021.727481/full
48. Available from: https://www.oncotarget.com/article/9744/text/
49. Zhe P, Kuo-Chieh L, Amber K, Gabriell E, Hoau-Yan W. Pathway analysis of glutamate-mediated, calcium-related signaling in glioma progression.. Biochemical pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
50. Carolina N, Ana SR, Ricardo T, Diogo SC, Joaquim R, Cláudia F, et al.. Cadherin Expression and EMT: A Focus on Gliomas.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533397/
51. Huiyuan G, Xiaomin Y, Lijun A, Wangming Z, Xiaohua L, Liping S, et al.. PCSK5 downregulation promotes the inhibitory effect of andrographolide on glioblastoma through regulating STAT3.. Molecular and cellular biochemistry [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/38553549/
52. Oh MC, Kim JM, Safaee M, Kaur G, Sun MZ, Kaur R, et al.. Overexpression of Calcium-Permeable Glutamate Receptors in Glioblastoma Derived Brain Tumor Initiating Cells. PLoS ONE [Internet]. 2012Oct23;7(10). Available from: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0047846
53. Carolina N, Ana SR, Rita C, Nuno M, Joaquim R, Claudia CF, et al.. Cadherin Expression Profiles Define Glioblastoma Differentiation and Patient Prognosis.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240393/
54. Rose M, Duhamel M, Aboulouard S, Kobeissy F, Tierny D, Fournier I, et al.. Therapeutic anti-glioma effect of the combined action of PCSK inhibitor with the anti-tumoral factors secreted by Poly (I:C)-stimulated macrophages. Cancer Gene Therapy [Internet]. 2021Jan5;29(1). Available from: https://www.nature.com/articles/s41417-020-00286-1
55. Available from: https://www.nature.com/articles/bjc201473
56. Chao F, Lei D, Cun W, Chuanwen F, Yongyang Y, Lie Y, et al.. Secretogranin II impairs tumor growth and angiogenesis by promoting degradation of hypoxia-inducible factor-1α in colorectal cancer.. Molecular oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8637574/
57. Marta Ł-Z, Maciej D, Barbara M. A Disintegrin and Metalloproteinase (ADAM) Family: Their Significance in Malignant Tumors of the Central Nervous System (CNS).. International journal of molecular sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8508774/
58. Mitsutoshi N, Kelsey LD, Satoko N, Jared AN, Michael EB. Ephrin-B3 ligand promotes glioma invasion through activation of Rac1.. Cancer research [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/16951161/
59. Available from: https://www.nature.com/articles/6604565
60. Available from: https://academic.oup.com/jnen/article/69/3/215/2917144
