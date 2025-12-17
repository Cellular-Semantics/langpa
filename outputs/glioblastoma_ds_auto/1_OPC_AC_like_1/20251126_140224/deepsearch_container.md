# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells (GBM cells) and glioma stem-like cells (GSCs)
- Disease: glioblastoma multiforme (WHO grade IV astrocytoma); malignant glioma
- Tissue: brain; central nervous system

## Input Genes
LINC01727, AC117464.1, XYLT1, MMD2, EEPD1, AC013265.1, MYO5B, PLA2G4A, KCNIP1, ITGB4, AC019068.1, UNC5D, MIR3681HG, LINC02125, LINC02246, LRRC4C, LUCAT1, MDGA2, AC077690.1, CTXND1, AL353138.1, CDH18, MN1, AL356737.2, NKAIN3, ... (55 total)

## Program: Extracellular Matrix Remodeling and Invasion
Coordinated remodeling of the glioblastoma extracellular matrix through proteoglycan synthesis, matrix metalloproteinase activity, and adhesion molecule expression. This program enables aggressive invasion through normal brain parenchyma by altering ECM stiffness, composition, and cell-matrix interactions.

**Predicted impacts**
- Enhanced single-cell and collective invasion through brain parenchyma via altered ECM composition and stiffness
- Increased mechanotransductive signaling through CD44-HA and integrin-ECM interactions
- Elevated matrix metalloproteinase activity enabling proteolysis of brain ECM barriers
- Suppression of T cell proliferation through TNC-mediated integrin interactions at tumor-immune interface
- Promotion of glioma stem cell niches through ECM organization mimicking neural stem cell microenvironments
- Enhanced FAK/ERK signaling and MMP9 secretion regulating cell adhesion and migration

**Evidence summary**
Multiple genes in this program demonstrate direct roles in glioma ECM remodeling. ADAMTS5 shows functional necessity for invasion (uncleavable variants fail to enhance invasion), while CD44-HA interactions are shown to activate mechanotransductive signaling independent of classical focal adhesions. ITGB4 upregulation correlates with poor prognosis and immune cell infiltration. The program is particularly well-supported by studies showing altered CS sulfation patterns (CHST8), increased proteoglycan synthesis (XYLT1), and active ECM remodeling (TNR, PLA2G4A). ECM stiffness mediated by TNC correlates with reduced overall survival.

**Atomic biological processes**
- Glycosaminoglycan biosynthesis and modification. Genes: XYLT1, CHST8
  - [45]: XYLT1 initiates GAG biosynthesis; describes crystal structures and substrate specificity for xylosyltransferase
  - [55]: CHST8 and other sulfotransferases alter CS sulfation patterns in glioma, affecting proliferation and invasion
- Matrix proteolysis and remodeling. Genes: ADAMTS5, TNR, PLA2G4A
  - [21]: ADAMTS5 (aggrecanase-2) cleaves BEHAB/brevican; uncleavable variants fail to promote glioma invasion
  - [33]: Glioma cells produce and remodel ECM components including tenascin-C; TNC acts as driver of ECM stiffness
  - [55]: Matrix degradation by ADAMTS proteases regulates glioma invasiveness through multiple sulfation-dependent mechanisms
- Cell-matrix adhesion and mechanotransduction. Genes: CD44, ITGB4, GPC5, RGMA
  - [9]: CD44-HA interactions mediate mechanosensing, adhesion, and invasive motility independent of integrin-based adhesion
  - [11]: ITGB4 upregulation correlates with poor prognosis and associates with tumor-associated fibroblasts
  - [55]: CD44-HA binding activates FAK/ERK signaling and MMP9 secretion; HA-induced activation regulates cell adhesion

**Atomic cellular components**
- Proteoglycans and heparan sulfate proteoglycans. Genes: GPC5, TNR, XYLT1, CHST8
  - [40]: Glypicans act as modulators of Wnt, BMP, FGF, and Shh signaling through heparan sulfate-dependent mechanisms
  - [37]: GPC5 is heparan sulfate proteoglycan with roles in Sonic Hedgehog signaling and neural regulation
  - [33]: Tenascin-C (TNC) expressed by glioma cells; provides scaffold for increased ECM stiffness and mechanosignaling
- Extracellular matrix structural proteins. Genes: TNR, PLA2G4A, CD44
  - [33]: Glioma produces fibronectin, tenascin, laminin, vitronectin; increased GM-ECM density supports malignancy
  - [19]: ECM-derived proteins (COL5A1, COL5A2, FBLN5, TGFBI) have bioactive effects; non-neoplastic ECM antagonizes cancer cells

**Required genes (not in input)**
- Genes: MMP9, MMP2, RECK, TIMP3, FAK, Integrins (α2β1, αvβ1, αvβ3, αvβ6), PKC, SRC, PI3K, PDGFRA, Notch pathway components (JAG1, NOTCH)
  - [33]: Notch pathway activation through TNC-integrin interactions; PDGFRA phosphorylation through CHSY1
  - [55]: FAK upregulation through CSPG4-integrin signaling; MMP9 secretion through HA-CD44-ERK pathway

**Program citations**
- [9]: CD44-HA adhesion and mechanosensing in GBM
- [11]: ITGB4 upregulation and immune microenvironment
- [21]: ADAMTS5-mediated BEHAB/brevican cleavage required for invasion
- [33]: Comprehensive review of glioma ECM remodeling
- [37]: GPC5 in proteoglycan signaling
- [40]: Glypican signaling mechanisms
- [45]: XYLT1 and GAG biosynthesis
- [55]: Detailed mechanisms of CS-GAG sulfation in glioma invasion

## Program: Cell-Cell Adhesion and Migration Plasticity
Dynamic regulation of intercellular adhesion molecules that enables glioblastoma cells to switch between individual and collective migration modes depending on microenvironment. N-cadherin and CD44 mediate differential migration on ECM versus neural cells, supporting both invasion routes through brain tissue.

**Predicted impacts**
- Ability to coordinate collective invasion while maintaining cell-cell contacts
- Context-dependent adhesion: strong adhesion between glioma cells slows migration; adhesion to neural cells accelerates migration
- Regulation of N-cadherin surface levels through catenin availability controls migration plasticity
- Reduced CDH18 expression supports invasiveness and chemotherapy resistance
- Differential cadherin junctional organization between leader and follower cells in migration streams
- Enhanced invasion into brain parenchyma through combination of cell-cell and cell-matrix adhesion

**Evidence summary**
This program is strongly supported by evidence showing N-cadherin's paradoxical effects: inhibiting ECM-based migration while promoting neural cell-based migration. CDH18's role in glioma invasiveness is established through multiple studies showing reduced expression increases invasion and resistance. The program highlights cell plasticity through regulated catenin-cadherin interactions that enable context-dependent migration. Surface expression levels correlate with migratory behavior, suggesting dynamic regulation of adhesion strength.

**Atomic biological processes**
- Homotypic cadherin-mediated cell-cell adhesion. Genes: CDH18, INPP4B
  - [23]: N-cadherin inhibits PHGG migration on ECM but stimulates migration on neurons/astrocytes; surface levels regulated by catenins
  - [20]: CDH18 calcium-dependent adhesion protein; lower levels increase glioma invasion/migration
- Heterotypic adhesion to neural cells. Genes: CD44, CDH18, RGMA
  - [23]: N-cadherin homotypic interactions with neural cells ahead of migration front speed overall migration
  - [12]: CD44-mediated adhesion to HA promotes glioma invasiveness through both direct and indirect mechanisms
- Catenin-mediated cadherin regulation. Genes: CDH18, ARC
  - [23]: Catenins regulate N-cadherin surface levels to stimulate or inhibit migration in different environments

**Atomic cellular components**
- Classical cadherins. Genes: CDH18
  - [23]: N-cadherin (CDH2) upregulated in 60-80% of adult glioblastomas; associated with increased mortality
  - [20]: CDH18 expression affects glioma cell resistance and invasiveness
- Cell junctions and adhesion complexes. Genes: CDH18, INPP4B
  - [23]: Distinct N-cadherin junctions form between leader and follower cells during collective migration

**Required genes (not in input)**
- Genes: CDH2 (N-cadherin), α-catenin, β-catenin, p120-catenin, Integrins (laminin and RGD receptors), FAK, SRC family kinases
  - [23]: Catenins reciprocally regulate cadherins; cadherins localize catenins to membrane; catenins regulate cadherin internalization and signaling

**Program citations**
- [12]: CD44 invasion and proliferation reciprocal regulation
- [20]: CDH18 in glioma invasion and chemotherapy resistance
- [23]: N-cadherin differential regulation in pediatric glioma migration

## Program: Ferroptosis Suppression and Redox Defense
Coordinated suppression of ferroptotic cell death through cystine/glutathione biosynthesis and antioxidant mechanisms. SLC7A11-mediated cystine import and PPARGC1α-regulated oxidative phosphorylation work together to maintain cellular redox homeostasis and enable survival under metabolic stress.

**Predicted impacts**
- Enhanced survival under oxidative stress and chemotherapeutic drug exposure through ferroptosis suppression
- Maintenance of elevated intracellular GSH levels supporting antioxidant defenses
- Sustained ATP production through oxidative phosphorylation enabling metabolic adaptation
- Resistance to iron-dependent cell death mechanisms
- Enhanced survival during nutrient deprivation through metabolic flexibility
- Potential resistance to ferroptosis-inducing therapies such as ferroptotic agents

**Evidence summary**
This program is well-established through multiple studies demonstrating that SLC7A11 overexpression directly suppresses ferroptosis while SLC7A11 inhibition induces ferroptotic death. PGC-1α's role in antioxidant defense is complementary, regulating both antioxidant enzyme expression and oxidative phosphorylation. These mechanisms work synergistically: SLC7A11 maintains GSH pools while PPARGC1α supports the mitochondrial energy production and ROS detoxification required for cell survival under stress. The program is particularly relevant in GBM where ferroptosis represents an emerging therapeutic approach.

**Atomic biological processes**
- Cystine/glutathione import and biosynthesis. Genes: SLC7A11
  - [15]: SLC7A11 mediates cystine import via system xc−; cystine converted to cysteine for GSH biosynthesis; SLC7A11 overexpression promotes ferroptosis resistance
  - [18]: SLC7A11/xCT overexpression suppresses ferroptosis; depletion of GSH via SLC7A11 inhibition impairs GPX4 function
- Antioxidant enzyme expression and mitochondrial oxidative metabolism. Genes: PPARGC1A
  - [31]: PGC-1α induces expression of antioxidant enzymes (SOD2, catalase, GPX1) essential for protection against ROS-induced cell death
  - [34]: PGC-1α enhances mitochondrial biogenesis and oxidative phosphorylation; under hypoxic conditions exerts antioxidant effect to shield cancer cells from ROS accumulation
- Lipid peroxidation and ferroptotic cell death prevention. Genes: SLC7A11, PPARGC1A
  - [15]: Ferroptosis induced by excessive lipid peroxidation; SLC7A11 suppresses ferroptosis through GSH-dependent GPX4 function
  - [18]: Depletion of intracellular GSH mediated by reduced cystine import impairs GPX4 function enabling ferroptosis

**Atomic cellular components**
- System xc− cystine/glutamate antiporter. Genes: SLC7A11
  - [15]: System xc− heterodimer consisting of light chain SLC7A11 and heavy chain SLC3A2; SLC7A11 mediates antiporter activity
- Mitochondrial oxidative phosphorylation machinery. Genes: PPARGC1A
  - [31]: PGC-1α regulates mitochondrial biogenesis and activates NRF1/NRF2 controlling β-ATP synthase, cytochrome c, and respiratory chain proteins
- Glutathione peroxidase complex. Genes: SLC7A11, PPARGC1A
  - [15]: GPX4 depends on GSH as cofactor; GSH depletion through SLC7A11 inhibition impairs GPX4 lipid peroxidase function

**Required genes (not in input)**
- Genes: SLC3A2 (heavy chain of system xc−), GPX4 (glutathione peroxidase 4), GSS (glutathione synthase), SOD1/SOD2 (superoxide dismutase), Catalase, GPX1, NRF1, NRF2, PPARα, ERRα
  - [15]: System xc− requires both SLC7A11 and SLC3A2 for function; GPX4 is critical downstream target
  - [31]: PGC-1α activates NRF1/NRF2 and PPARα/ERRα for antioxidant enzyme expression and mitochondrial biogenesis

**Program citations**
- [15]: Comprehensive review of SLC7A11 in ferroptosis and cancer
- [18]: SLC7A11/xCT and ferroptosis in GBM therapy
- [31]: PGC-1α metabolic modulation and antioxidant defense
- [34]: PGC-1α in glioblastoma metabolic reprogramming

## Program: Immune Evasion Through Glycosylation
Dysregulation of sialyltransferase activity leading to altered surface glycosylation patterns that enable immune evasion through reduced antigen presentation, altered checkpoint molecule signaling, and reduced recognition by immune cells. Hypersialylation and aberrant sialylation patterns create an immunosuppressive microenvironment.

**Predicted impacts**
- Reduced T cell recognition through altered MHC glycosylation patterns
- Enhanced macrophage recruitment with reduced anti-tumor phenotype through Siglec-15 engagement
- Resistance to death receptor-mediated apoptosis through sialylation-dependent masking
- Suppression of anti-tumor immune responses through TGF-β secretion
- Reduced binding to galectins that would otherwise trigger apoptosis
- Shift toward immune-excluded or immune-desert phenotypes rather than immune-inflamed

**Evidence summary**
This program is supported by recent evidence showing that 80% of sialyltransferases are differentially expressed between low-invasive and high-invasive GBM cells. Specific sialyltransferases (ST6GAL1, ST3Gal1, ST8SIA variants) have been mechanistically linked to chemotherapy resistance, apoptosis evasion, and immune cell suppression. The sialylation patterns directly correlate with immune infiltration phenotypes and patient outcomes. Aberrant sialylation masks molecular patterns recognized by immune cells while simultaneously engaging inhibitory Siglec receptors that suppress immune responses.

**Atomic biological processes**
- Sialic acid terminal structure synthesis. Genes: ST8SIA1, ST8SIA5
  - [32]: ST6GAL1 α2-6 sialylation protects from apoptosis; ST3Gal1 sialyl-T synthesis linked to poor prognosis and chemotherapy resistance
  - [35]: Sialyltransferases (ST6NAC2/3/5/6, ST8SIA1/2/3/4/5/6, ST3GAL1/4/5/6) differentially expressed in invasive GBM cells
- MHC antigen presentation evasion. Genes: ST8SIA1, ST8SIA5, NLRC5
  - [32]: Sialylation prevents recognition by immune cells; α2-6 sialylation and sTn antigen recognition by Siglec-15 suppresses T cell responses
- Immune checkpoint molecule signaling modulation. Genes: ST8SIA1, ST8SIA5, CD44
  - [32]: Sialylated β1 integrins confer protection against galectin-3-induced apoptosis; sialylation of death receptors FAS prevents internalization
  - [35]: Sialylation patterns affect immune cell infiltration; different phenotypes linked to immune-excluded, immune-desert, or immune-inflamed states

**Atomic cellular components**
- Sialyltransferase enzymes. Genes: ST8SIA1, ST8SIA5
  - [32]: Sialyltransferases include α2-3, α2-6, α2-8 sialyl linkage synthases; each generates specific sialoform modifications
  - [35]: 80% of 20 sialyltransferases differentially expressed between low-invasive and highly-invasive GBM cells
- Siglec and selectin immune receptors. Genes: ST8SIA1, ST8SIA5
  - [32]: Siglec-15 recognizes sTn antigen; engagement by tumor-associated sTn results in enhanced TGF-β secretion and macrophage Siglec-15 suppression of T cells
- Death receptors and survival signaling. Genes: ST8SIA1, ST8SIA5
  - [32]: Sialylation of FAS and TNFR1 prevents receptor internalization and death-inducing signaling complex formation

**Required genes (not in input)**
- Genes: ST6GAL1, ST3Gal1, ST6GalNac1, ST6GalNac2, Siglec-15, FAS, TNFR1, Galectin-3, TGF-β, MHC I and II molecules
  - [32]: ST6GAL1 and ST3Gal1 are key sialyltransferases; Siglec-15 recognizes tumor-associated antigens

**Program citations**
- [32]: Comprehensive review of sialyltransferase roles in cancer immune evasion
- [35]: Sialylation-related gene signatures in lymph node metastasis and immune phenotypes

## Program: Metabolic Reprogramming for Proliferation
Coordinated upregulation of metabolic pathways supporting rapid proliferation through enhanced glycolysis, glutaminolysis, and lipid metabolism. PLA2G4A regulates cell cycle progression through MCM complex activation, while PPARGC1α supports oxidative metabolism enabling tumor cell survival and adaptation.

**Predicted impacts**
- Accelerated G1/S cell cycle transition enabling rapid proliferation
- Enhanced DNA replication through MCM complex upregulation
- Increased ATP production through both glycolytic and oxidative pathways
- Enhanced survival under metabolic stress through metabolic flexibility
- Promotion of cell cycle through mTORC1 pathway activation
- Resistance to metabolic inhibitors targeting single pathways
- Sustained proliferation despite nutrient scarcity through enhanced metabolic efficiency

**Evidence summary**
This program is strongly supported by multiple independent studies. PLA2G4A shows direct functional correlation with proliferation: high expression predicts poor survival, overexpression drives proliferation via G1/S transition, and silencing induces apoptosis. The mechanism involves specific upregulation of MCM2 and MCM5; their knockdown abrogates PLA2 effects. PPARGC1α complements this program by enabling metabolic flexibility and sustained ATP production. The two genes work synergistically: PLA2 drives cell cycle progression while PPARGC1α provides the metabolic fuel.

**Atomic biological processes**
- Phospholipase A2-mediated cell cycle progression. Genes: PLA2G4A
  - [7]: High PLA2 expression correlates with low overall survival; PLA2 overexpression promotes GBM cell proliferation and viability by inducing G1/S cell cycle transition
  - [10]: CENPF interaction with PLA2G4A promotes glioma growth through mTORC1 signaling pathway
- DNA replication initiation through MCM complex regulation. Genes: PLA2G4A
  - [7]: PLA2 increases MCM2 and MCM5 expression; MCM knockdown prevents PLA2-mediated proliferation; PLA2 silencing decreases γ-H2AX indicating reduced DNA replication
- Metabolic flexibility and oxidative phosphorylation. Genes: PPARGC1α
  - [34]: PPARGC1α enhances mitochondrial biogenesis and oxidative phosphorylation, reprogramming metabolism to support cell proliferation, growth, and survival
- Aerobic glycolysis suppression (in certain GBM subtypes). Genes: PPARGC1α
  - [34]: In HCC tumors, PGC-1α promotes OXPHOS and inhibits aerobic glycolysis through PDK1 in PPARγ-dependent manner; may apply to certain GBM subtypes

**Atomic cellular components**
- Minichromosome maintenance (MCM) complex. Genes: PLA2G4A
  - [7]: MCM2 and MCM5 proteins critical for DNA replication initiation; PLA2 upregulates their expression; their knockdown suppresses PLA2-mediated proliferation
- Mitochondrial electron transport chain. Genes: PPARGC1α
  - [31]: PPARGC1α regulates expression of genes encoding respiratory chain proteins including cytochrome c, cytochrome c oxidase subunits, and β-ATP synthase
- Fatty acid oxidation machinery. Genes: PPARGC1α
  - [31]: PPARGC1α induces expression of fatty acid transporters CD36 and carnitine palmitoyltransferase I (CPT1); activates PPARα and ERRα for β-oxidation

**Required genes (not in input)**
- Genes: MCM2, MCM5, CDC6, ORC complex proteins, CDK2, Cyclin E, PPARα, ERRα, NRF1, NRF2, PDK1, PPARγ, mTORC1 components
  - [7]: MCM2 and MCM5 are direct targets of PLA2 regulation
  - [10]: mTORC1 pathway is downstream of CENPF-PLA2G4A interaction
  - [34]: PPARGC1α activates PPARα, ERRα, NRF1/2 for metabolic gene expression

**Program citations**
- [7]: PLA2 as oncogene in GBM promoting proliferation and inhibiting apoptosis
- [10]: CENPF-PLA2G4A interaction in GBM growth
- [31]: PGC-1α metabolic regulator in cancer
- [34]: PGC-1α in glioblastoma metabolic reprogramming

## Program: Tumor Microenvironment Immune Regulation
Coordinated manipulation of tumor microenvironment immunity through altered macrophage infiltration, reduced T cell function, and upregulation of immunosuppressive checkpoints. NLRC5 downregulation reduces MHC-I antigen presentation, while myeloid-affiliated transcriptional programs promote M2-like macrophage recruitment.

**Predicted impacts**
- Reduced CD8 T cell activation through decreased MHC class I presentation
- Enhanced recruitment of immunosuppressive M2-like macrophages and myeloid-derived suppressor cells
- Increased PD-L1 expression on tumor-infiltrating macrophages creating checkpoint-mediated immune suppression
- Reduced anti-tumor immune responses despite immune cell infiltration
- Polarization toward immune-excluded or immune-desert phenotypes
- Resistance to checkpoint inhibitor therapies through compensatory mechanisms

**Evidence summary**
This program emerges from multiple converging lines of evidence. NLRC5 is established as necessary and sufficient for MHC class I expression, making its downregulation or silencing a direct mechanism for immune evasion. The mesenchymal GBM subtype (which has poorest survival) exhibits increased immune infiltration paradoxically accompanied by increased immune evasion through acquisition of myeloid-affiliated transcriptional programs. ITGB4 upregulation specifically correlates with immune infiltration patterns and tumor-associated fibroblast interaction. The program integrates transcriptional, epigenetic, and extracellular matrix components to create an immunosuppressive microenvironment despite apparent immune activation.

**Atomic biological processes**
- MHC class I antigen presentation suppression. Genes: NLRC5
  - [27]: NLRC5 is transcriptional regulator orchestrating concerted expression of MHC class I genes, β2-microglobulin, TAP1, and LMP2
  - [30]: NLRC5 necessary and sufficient for IFN-γ-induced MHC class I expression; NLRC5 knockdown impairs MHC class I expression
- Tumor-associated macrophage recruitment and polarization. Genes: GFAP, NLRC5, ITGB4
  - [5]: GBM cells acquire myeloid-affiliated transcriptional programs through epigenetic immunoediting, leading to increased recruitment of tumor-associated macrophages
  - [11]: ITGB4 expression closely related to immune-related genes and specifically interacts with tumor-associated fibroblasts
- Immune checkpoint molecule expression. Genes: GFAP, CD44
  - [5]: Tumor-infiltrating macrophages express significantly higher levels of PD-L1 than microglia; M-MDSCs also express immunosuppressive markers

**Atomic cellular components**
- MHC class I antigen presentation machinery. Genes: NLRC5
  - [27]: NLRC5 regulates promoters of MHC class I genes and induces transcription of related genes involved in antigen presentation
- Macrophage recruitment and differentiation signals. Genes: GFAP, CD44
  - [5]: Epigenetic changes in GBM include activation of myeloid-associated genes and gene programs

**Required genes (not in input)**
- Genes: MHC class I genes (HLA-A, HLA-B, HLA-C), B2M (β2-microglobulin), TAP1, LMP2, IRF1, STAT1, NF-κB, PD-L1/CD274, LAG3-ligand (MHC-II), TGF-β, Colony-stimulating factors (CSF1, CSF2)
  - [27]: NLRC5 regulates complete MHC class I presentation pathway including β2M, TAP1, LMP2
  - [5]: Myeloid programs involve TGF-β and CSF signaling

**Program citations**
- [5]: Epigenetic immunoediting and myeloid program acquisition in GBM
- [11]: ITGB4 and tumor microenvironment immune infiltration
- [27]: NLRC5 as MHC class I transactivator
- [30]: NLRC5 mechanisms in MHC class I-dependent immune responses

## Program: Neural Guidance Cues and Developmental Plasticity
Reactivation of developmental neural guidance pathways in GBM, including Reelin-Disabled signaling, netrin-UNC5 axis, and repulsive guidance molecule signaling. These pathways may support both invasion and plasticity between differentiation states in tumor cells.

**Predicted impacts**
- Enhanced migration plasticity through reactivated developmental guidance pathways
- Potential paradoxical effects: guidance cues may support invasion while simultaneously limiting proliferation
- Integration of extracellular matrix signals through HS-dependent guidance mechanisms
- Possible regulation of glioma stem cell properties through developmental signaling
- Crosstalk between guidance signals and immune cell migration affecting tumor microenvironment
- Potential resistance to standard anti-invasion therapies through redundant guidance mechanisms

**Evidence summary**
This program represents reactivation of developmental neural guidance pathways in GBM. Multiple independent pathway families are represented: Reelin-Dab1, netrin-UNC5, FLRT-Unc5, and RGMa-neogenin. All require heparan sulfate proteoglycans for function, linking this program to ECM remodeling and GAG biosynthesis. Critically, these pathways show functional necessity for developmental cell migration, and their aberrant reactivation in GBM likely contributes to both invasion and plasticity. The program is supported by recent structural and functional evidence defining precise molecular mechanisms of HS-dependent guidance complex formation.

**Atomic biological processes**
- Reelin-Dab1 signaling pathway. Genes: DAB1
  - [14]: Reelin-Disabled-1 signaling regulates neuronal migration; tyrosine phosphorylation of Dab1 recruits SH2 domain-containing proteins and activates multiple cascades
  - [17]: DAB1 is signaling adapter in reelin-mediated pathway, regulating neuron migration and differentiation
- Netrin-UNC5 repulsive guidance. Genes: UNC5D, GPC5
  - [51]: UNC-5 heparin-binding protein forms stable complex with UNC-6/netrin in presence of heparin; UNC-5-heparin affinity necessary for repulsive guidance
  - [54]: FLRT2/3 ECDs act as repulsive cues for Unc5-positive neurons; Unc5D required for proper neuronal migration in developing cortex
- Repulsive guidance molecule A signaling. Genes: RGMA
  - [57]: RGMa inhibits leukocyte migration through neogenin receptor; RGMa acts as guidance cue for both neurons and immune cells
  - [60]: RGMa regulates cell adhesion, migration, polarity and differentiation with pleiotropic roles in early morphogenesis and immune responses
- Glycosaminoglycan-dependent guidance signaling. Genes: GPC5, XYLT1, CHST8
  - [51]: Heparin/heparan sulfate critically regulates UNC-6-UNC-5 complex formation; HS-binding necessary for netrin-UNC5-mediated guidance
  - [55]: Glypican-1 HS chains regulate glioma cell invasion through PECAM-1 phosphorylation on endothelial cells

**Atomic cellular components**
- Repulsive guidance receptors. Genes: UNC5D, RGMA
  - [51]: UNC-5 IG1-IG2 domain boundary contains positively charged surface for heparin binding
  - [54]: FLRT proteins serve as ligands for Unc5 receptors; diverse Unc5 members show differential FLRT preferences
- Heparan sulfate proteoglycans. Genes: GPC5, XYLT1, CHST8
  - [51]: Heparin/HS necessary for formation of large, stable, rigid UNC-6-UNC-5 complexes
  - [55]: Glypican-1 HS chains mediate shear stress signaling on endothelial cells

**Required genes (not in input)**
- Genes: RELN (Reelin), SH2-domain proteins, UNC-6/Netrin, Neogenin, FLRT2, FLRT3, Unc5A/B/C, Heparan sulfate, SDCBP
  - [14]: Reelin and SH2-containing proteins are upstream of DAB1
  - [51]: UNC-6 and Unc5 are ligand-receptor pairs; heparan sulfate is obligatory cofactor

**Program citations**
- [14]: Reelin-Dab1 signaling in neuronal migration
- [51]: Structural and functional characterization of netrin-UNC5-heparin complexes
- [54]: FLRT-Unc5 as repulsive guidance molecules
- [57]: RGMa as immunomodulatory guidance cue
- [60]: RGMa pleiotropic roles in development and immunity

## Program: Transcriptional and Epigenetic Plasticity Control
Regulation of glioma cell plasticity between differentiation states through altered GFAP isoform expression, long non-coding RNA-mediated epigenetic control, and transcriptional regulatory networks. Alternative splicing and epigenetic modifications enable switching between proneural/stemlike and mesenchymal/differentiated phenotypes.

**Predicted impacts**
- Maintenance of stemlike/proneural state through elevated GFAPδ/α ratio and associated gene programs
- Enhanced proliferation through PRC2-mediated silencing of cell cycle inhibitors
- Reversible switching between proliferative and invasive/migratory states
- Reduced ability to differentiate into mature astrocytes with anti-tumor properties
- Activation of malignant gene programs through MAPK pathway via DUSP4
- Resistance to differentiation therapy approaches
- Enhanced G0/G1 arrest and tumor suppression when epigenetic program is reversed

**Evidence summary**
This program combines two complementary mechanisms: GFAPδ/α ratio as a marker and driver of GBM malignancy, and lncRNA-PRC2 complexes as regulators of cell cycle inhibitor expression. The GFAPδ/α ratio functionally regulates genes involved in malignancy, cell cycle, and cell-ECM interactions; forcing GFAPα expression (lower ratio) impairs proliferation. LUCAT1 demonstrates specific functional dependence on PRC2-mediated silencing of tumor suppressors; its knockdown induces G0/G1 arrest. Together these mechanisms explain how gliomas maintain stemlike properties while resisting differentiation.

**Atomic biological processes**
- GFAP isoform switching and astrocytic differentiation. Genes: GFAP
  - [13]: High GFAPδ/α ratio in grade IV astrocytoma; GFAPδ/α ratio regulates high-malignant genes involved in mitotic cell cycle and cell proliferation
  - [16]: GFAP expression inversely correlates with tumor grade; forced astrocytic differentiation impairs proliferation
- Long non-coding RNA-mediated epigenetic regulation. Genes: LUCAT1
  - [43]: LUCAT1 associates with PRC2 and recruits EZH2; LUCAT1 knockdown increases p21 and p57 expression through epigenetic repression
- Polycomb repressor complex 2-mediated chromatin silencing. Genes: LUCAT1, GFAP
  - [43]: LUCAT1 participates in PRC2-mediated epigenetic regulation of cell cycle inhibitors; similar to HOTAIR-EZH2 mechanism
- MAPK pathway regulation affecting malignancy. Genes: GFAP
  - [13]: GFAPδ/α ratio activates DUSP4 (MAPK phosphatase 2) which regulates ERK and JNK; high DUSP4 expression correlates with worse prognosis

**Atomic cellular components**
- GFAP alternative splice variants. Genes: GFAP
  - [13]: GFAPα and GFAPδ are alternative splice isoforms of GFAP; different ratios characterize differentiation state and malignancy
- Polycomb repressor complex 2 (EZH2). Genes: LUCAT1
  - [43]: lncRNAs bind to EZH2 component of PRC2; EZH2 is suppressor of cancer progression through histone methylation
- Cell cycle inhibitor proteins. Genes: LUCAT1
  - [43]: p21 and p57 are CDK inhibitors controlling G0/G1 arrest; LUCAT1 knockdown epigenetically relieves their repression

**Required genes (not in input)**
- Genes: EZH2, SUZ12, EED (PRC2 components), p21/CDKN1A, p57/CDKN1C, DUSP4, ERK/MAPK, JNK, Histone methyltransferases, Histone deacetylases (HDACs)
  - [13]: PRC2 components required for LUCAT1 function; DUSP4 and MAPK pathway downstream of GFAPδ/α
  - [43]: EZH2 is core PRC2 component; p21/p57 are direct targets

**Program citations**
- [13]: GFAPδ as biomarker and therapeutic target in glioblastoma
- [16]: Astrocytic differentiation impairs glioma proliferation
- [43]: LUCAT1 and PRC2-mediated epigenetic regulation in cancer

## Program: Cytoskeletal Dynamics and Cell Motility
Regulation of dynamic cytoskeletal remodeling supporting migration and invasion through motors, adaptor proteins, and activity-regulated proteins. ARC-mediated plasticity protein function and MYO5B motor protein trafficking coordinate cellular movements enabling collective and individual invasion.

**Predicted impacts**
- Enhanced dynamic reorganization of cytoskeleton in response to microenvironmental cues
- Directed trafficking of membrane proteins required for cell-cell and cell-matrix adhesion
- Rapid adaptation of morphology during collective and individual migration
- Potential RNA transport between tumor cells affecting cooperative behavior
- Calcium-dependent regulation of migration through ion channel and cadherin signaling
- Support for both neural and non-neural interactions through cytoskeletal plasticity

**Evidence summary**
This program combines activity-regulated plasticity proteins with motor proteins supporting physical cell movement. Arc is established as immediate early gene crucial for activity-dependent plasticity, encoding a protein capable of interacting with endocytic machinery and forming virus-like capsids for RNA transport. MYO5B provides molecular motor function for directed trafficking of proteins. While individual genes have limited direct GBM literature, their roles in neuronal plasticity and motility are well-characterized, and their presence in the gene list suggests their reactivation in GBM for enhanced migratory capacity.

**Atomic biological processes**
- Activity-regulated cytoskeletal reorganization. Genes: ARC
  - [25]: Arc/Arg3.1 is immediate early gene induced by neural activity; interacts with dynamin and endophilin in endocytosis; localizes to potentiated synapses
  - [28]: Arc protein forms virus-like capsids; dysfunction implicated in neurological conditions; important for activity-dependent plasticity
- Molecular motor-mediated protein trafficking. Genes: MYO5B
  - [26]: MYO5B is molecular motor trafficking ion transporters to apical membrane; may traffic other membrane proteins
  - [29]: MYO5b deficiency disrupts electric conduction, metabolism, and sarcomere organization affecting cellular function
- Calcium signaling in cell migration. Genes: CDH18, KCNIP1
  - [20]: CDH18 supports calcium-mediated intercellular adhesion; involved in synaptic adhesion and axon growth

**Atomic cellular components**
- Immediate early gene protein. Genes: ARC
  - [28]: Arc protein uniquely forms virus-like capsids that transport RNA between neurons; localizes to endosomal compartments
- Unconventional myosin motor protein. Genes: MYO5B
  - [26]: MYO5B is myosin-5 family member; molecular motor for intracellular vesicle trafficking
- Calcium-sensing protein. Genes: KCNIP1, CDH18
  - [42]: KCNIP1 potentially functions in calcium-dependent signaling affecting cell motility

**Required genes (not in input)**
- Genes: Dynamin, Endophilin, AMPA receptors, GluR1, Kinesin family motors, Rab GTPases, SNARE proteins, Actin regulators (Arp2/3, mDia)
  - [25]: Arc interacts with dynamin/endophilin for AMPA receptor endocytosis

**Program citations**
- [25]: Arc/Arg3.1 in activity-dependent plasticity and synaptic changes
- [26]: MYO5B molecular motor function in protein trafficking
- [28]: Arc protein plasticity functions and virus-like capsid formation

## Program: Signaling Pathway Integration and Crosstalk
Convergence of multiple signaling pathways through phosphoinositide metabolism, histamine signaling, and natriuretic peptide signaling. These pathways integrate extracellular signals to coordinate proliferation, survival, and metabolic adaptations in response to tumor microenvironment.

**Predicted impacts**
- Enhanced PI3K/Wnt crosstalk driving proliferation and survival
- Increased H1R-mediated MAPK activation promoting growth signals
- Modulation of metabolic and hemodynamic responses through natriuretic peptide signaling
- Integration of multiple extracellular signals converging on common effectors
- Context-dependent selection between proliferation (Wnt/β-catenin) and differentiation pathways
- Potential resistance to single-pathway inhibitors through multiple input routes

**Evidence summary**
This program represents convergence of multiple signaling pathways. INPP4B demonstrates functional crosstalk between PI3K and Wnt signaling through phosphoinositide metabolism; its dual nature as oncogene in PIK3CA-mutant cancers shows pathway context-dependence. H1R activation drives proliferation through MAPK pathways; elevated expression correlates with poor survival in multiple cancers. NPR3 represents additional signaling complexity through cGMP-dependent mechanisms. The integration of these diverse pathways suggests tumors utilize multiple overlapping signaling inputs to maintain proliferation despite therapeutic pressure.

**Atomic biological processes**
- Phosphoinositide metabolism and PI3K/Akt signaling. Genes: INPP4B
  - [38]: INPP4B converts PI(3,4)P2 to PI(3)P on late endosomes; facilitates PI3Kα crosstalk with Wnt signaling in ER+ breast cancer
  - [41]: INPP4B regulates PI3K signaling and controls mammary epithelial cell proliferation; loss occurs in aggressive basal-like tumors
- Histamine receptor H1-mediated proliferation. Genes: HRH1
  - [39]: H1R signaling promotes intestinal tumor formation and cell proliferation; H1R-overproducing cells show enhanced ERK and JNK phosphorylation
  - [42]: H1R coupled to Gq protein activating phospholipase C and IP3 signaling; H1R expressed early in developing CNS
- Natriuretic peptide signaling. Genes: NPR3
  - [56]: NPR-A/GC-A and NPR-B/GC-B are transmembrane guanylyl cyclases; NPR-C/NPR3 lacks catalytic activity and controls natriuretic peptide concentrations
  - [59]: Natriuretic peptides regulate blood volume, blood pressure, and metabolic functions through cGMP signaling
- Wnt/β-catenin pathway crosstalk. Genes: INPP4B
  - [38]: INPP4B promotes Wnt/β-catenin signaling through Hrs-dependent degradation of GSK3β on late endosomes

**Atomic cellular components**
- Phosphoinositide lipids and effector proteins. Genes: INPP4B
  - [38]: PI(3,4)P2 and PI(3)P have distinct downstream effectors; Hrs recognizes PI(3)P on late endosomes
- G protein-coupled receptors. Genes: HRH1, NPR3
  - [39]: HRH1 is GPCR coupled to Gq; HRH2 coupled to Gs activating cAMP
  - [56]: NPR-A/B and NPR-C are single membrane-spanning receptors with different signaling properties
- Cyclic nucleotide signaling systems. Genes: HRH1, NPR3
  - [42]: H2R-Gs-cAMP-PKA pathway; H1R-Gq-IP3 pathway represent distinct signaling cascades
  - [56]: cGMP signaling through NPR-A/B and cGMP-binding proteins

**Required genes (not in input)**
- Genes: PI3K catalytic subunit, AKT, PTEN, GSK3β, β-catenin, Wnt, Frizzled, TCF/LEF, Phospholipase C, IP3 receptor, PKC, Guanylate cyclase, PKG, Phosphodiesterases
  - [38]: PI3K, AKT, and Wnt pathway components are downstream effectors of INPP4B
  - [39]: PLC and IP3 are downstream of H1R; ERK/JNK are downstream effectors

**Program citations**
- [38]: INPP4B in PI3K-Wnt signaling crosstalk
- [39]: H1R signaling in tumor formation and proliferation
- [41]: INPP4B regulation of PI3K signaling
- [42]: Histamine signaling in neural development
- [56]: Natriuretic peptide receptor signaling

## Bibliography
1. Zhang H, li yuhao, Lu H. Correlation of BUB1 and BUB1B with the development and prognosis of endometrial cancer. Scientific Reports [Internet]. 2024Jul24;14(1). Available from: https://www.nature.com/articles/s41598-024-67528-2
2. Yu-Ting S, Robert C, Herui W, Hua S, Qi Z, Li-Yuan C, et al.. Novel Targeting of Transcription and Metabolism in Glioblastoma.. Clinical cancer research : an official journal of the American Association for Cancer Research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8108069/
3. Artem DB, Laila MP, David C, Craig PW, Andrea DT, Nancy WL, et al.. Sox2 promotes malignancy in glioblastoma by regulating plasticity and astrocytic differentiation.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4094829/
4. Available from: https://www.genecards.org/cgi-bin/carddisp.pl?gene=LINC01727
5. Available from: https://discovery.ucl.ac.uk/id/eprint/10126313/1/1-s2.0-S0092867421003512-main.pdf
6. Available from: https://kups.ub.uni-koeln.de/12158/1/Goranci-PhD-thesis.pdf
7. Haiyun Z, Hanwei Z, Hongliang W, Zhongbo Y, Kai H, Minhong Y. High PLA2 level is correlated with glioblastoma progression via regulating DNA replication.. Journal of cellular and molecular medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8899163/
8. Yizhou H, Irene Y, Ping C, Li L, Sampsa H, Tuula AN, et al.. Netrin-4 promotes glioblastoma cell proliferation through integrin β4 signaling.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323899/
9. Available from: https://aacrjournals.org/mcr/article/12/10/1416/135686/CD44-Mediated-Adhesion-to-Hyaluronic-Acid
10. Junhong L, Moxuan Z, Qiang S, Xinglan L, Fei D, Yanhao C, et al.. CENPF interaction with PLA2G4A promotes glioma growth by modulating mTORC1 and NF-κB pathways.. Cancer cell international [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11871623/
11. Chen P, Ma T, Yan T, Song Z, Liu C, Pan C, et al.. ITGB4 upregulation is associated with progression of lower grade glioma. Scientific Reports [Internet]. 2024Jan3;14(1). Available from: https://www.nature.com/articles/s41598-023-49801-y
12. Akihiro I, Takanori O, Masahiro N, Yoshihiro O, Kosuke K, Hajime Y, et al.. A Narrative Review on CD44's Role in Glioblastoma Invasion, Proliferation, and Tumor Recurrence.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
13. Roxana R, George EDP, Radu MG, Felix MB. GFAPδ: A Promising Biomarker and Therapeutic Target in Glioblastoma.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8971704/
14. Zhihua G, Roseline G. Reelin-Disabled-1 signaling in neuronal migration: splicing takes the stage.. Cellular and molecular life sciences : CMLS [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/23052211/
15. Pranavi K, Li Z, Boyi G. Cystine transporter SLC7A11/xCT in cancer: ferroptosis, nutrient dependency, and cancer therapy.. Protein & cell [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8310547/
16. Available from: https://aacrjournals.org/mct/article/22/2/274/716253/Transcription-Factor-Forced-Astrocytic
17. Available from: https://www.uniprot.org/uniprotkb/O75553/entry
18. Singh S, Mohapatra I, Barik D, Zheng H, Kim S, Sharma M, et al.. Harnessing ferroptosis to transform glioblastoma therapy and surmount treatment resistance. Cell Death Discovery [Internet]. 2025Oct7;11(1). Available from: https://www.nature.com/articles/s41420-025-02744-x
19. Available from: https://www.oncotarget.com/article/28203/text/
20. Xiaoxuan T, Shanxing D, Jie Q, Ruilan Z, Jing L, Limei Z, et al.. Calcium-dependent adhesion protein CDH18, a potential biomarker for prognosis in uterine corpus endometrial carcinoma.. Frontiers in molecular biosciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11864935/
21. Mariano SV, Susan H, Russell TM. BEHAB/brevican requires ADAMTS-mediated proteolytic cleavage to promote glioma invasion.. Journal of neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
22. Massimiliano M, Antonio D, Simona C, Francesco R, Valentina M, Silvia V, et al.. Identification of a novel set of genes reflecting different in vivo invasive patterns of human GBM cells.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3502598/
23. Available from: https://rupress.org/jcb/article/223/6/e202401057/276615/N-cadherin-dynamically-regulates-pediatric-glioma
24. Held‐Feindt J, Paredes EB, Blömer U, Seidenbecher C, Stark AM, Mehdorn HM, et al.. Matrix‐degrading proteases ADAMTS4 and ADAMTS5 (disintegrins and metalloproteinases with thrombospondin motifs 4 and 5) are expressed in human glioblastomas. International Journal of Cancer [Internet]. 2005Oct26;118(1). Available from: https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.21258
25. Jonathan EP, Vicki JP, Jason S, Kevin P, Melissa SM, Kathie AO, et al.. The activity-regulated cytoskeletal-associated protein (Arc/Arg3.1) is required for memory consolidation of pavlovian fear conditioning in the lateral amygdala.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6671728/
26. Sarah AD, Kristen AE, Jessica D, Rachel S, Izumi K, Evan K, et al.. Myosin 5b is required for proper localization of the intermicrovillar adhesion complex in the intestinal brush border.. American journal of physiology Gastrointestinal and liver physiology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9639760/
27. Meissner TB, Li A, Biswas A, Lee K-H, Liu Y-J, Bayir E, et al.. NLR family member NLRC5 is a transcriptional regulator of MHC class I genes. Proceedings of the National Academy of Sciences [Internet]. 2010Jul16;107(31). Available from: https://www.pnas.org/doi/10.1073/pnas.1008684107
28. Available from: https://en.wikipedia.org/wiki/Activity-regulated_cytoskeleton-associated_protein
29. Available from: https://academic.oup.com/eurheartj/article/46/25/2455/8118993
30. Koichi SK, Peter J van den E. NLRC5: a key regulator of MHC class I-dependent immune responses.. Nature reviews Immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/23175229/
31. Frederic B, Lisa K. The metabolic modulator PGC-1α in cancer.. American journal of cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6405967/
32. Marjolaine H, Pushpita S, Quentin H, Stephan von G. The Distinct Roles of Sialyltransferases in Cancer Biology and Onco-Immunology.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8718907/
33. Ruolun W, Jiasheng Z, Brandon B, Xianzhi L. Glioma actively orchestrate a self-advantageous extracellular matrix to promote recurrence and progression.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308147/
34. Wang Y, Peng J, Yang D, Xing Z, Jiang B, Ding X, et al.. From metabolism to malignancy: the multifaceted role of PGC1α in cancer. Frontiers in Oncology [Internet]. 2024May7;14. Available from: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1383809/full
35. Shao Y, Yu M, Zhang L, Zhou L, Yan X, Feng B, et al.. In-depth analysis of lymph node metastasis-related sialylated protein profiling and their clinical and biological significance in colorectal cancer using mass spectrometry and multi-omics technologies. Scientific Reports [Internet]. 2024Nov18;14(1). Available from: https://www.nature.com/articles/s41598-024-79893-z
36. Day ZI, Roberts-Thomson S, Nouri YJ, Dalton NS, Wang SS, Davenport A, et al.. Defining the extracellular matrix for targeted immunotherapy in adult and pediatric brain cancer. npj Precision Oncology [Internet]. 2025Jun14;9(1). Available from: https://www.nature.com/articles/s41698-025-00956-z
37. Available from: https://maayanlab.cloud/Harmonizome/gene/GPC5
38. Rodgers SJ, Ooms LM, Oorschot VMJ, Schittenhelm RB, Nguyen EV, Hamila SA, et al.. INPP4B promotes PI3Kα-dependent late endosome formation and Wnt/β-catenin signaling in breast cancer. Nature Communications [Internet]. 2021May25;12(1). Available from: https://www.nature.com/articles/s41467-021-23241-6
39. Zhongcheng S, Robert SF, Melinda AE, Chunxu G, Anne H, Angela M, et al.. Distinct roles of histamine H1- and H2-receptor signaling pathways in inflammation-associated colonic tumorigenesis.. American journal of physiology Gastrointestinal and liver physiology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6383385/
40. A F, F M, R D. Fine-tuning of cell signaling by glypicans.. Cellular and molecular life sciences : CMLS [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11114805/
41. Clare GF, Lisa MO, Miriel H, Jessica V, Sandra AO, Ewan KM, et al.. Inositol polyphosphate 4-phosphatase II regulates PI3K/Akt signaling and is lost in human basal-like breast cancers.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3009830/
42. Carthy E, Ellender T. Histamine, Neuroinflammation and Neurodevelopment: A Review. Frontiers in Neuroscience [Internet]. 2021Jul14;15. Available from: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.680214/full
43. Yue S, Shi-Dai J, Quan Z, Liang H, Jing F, Xi-Yi L, et al.. Long non-coding RNA LUCAT1 is associated with poor prognosis in human non-small lung cancer and regulates cell proliferation via epigenetically repressing p21 and p57 expression.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5438651/
44. Available from: https://www.ncbi.nlm.nih.gov/gene/161357
45. Taieb M, Ghannoum D, Barré L, Ouzzine M. Xylosyltransferase I mediates the synthesis of proteoglycans with long glycosaminoglycan chains and controls chondrocyte hypertrophy and collagen fibers organization of in the growth plate. Cell Death &amp; Disease [Internet]. 2023Jun9;14(6). Available from: https://www.nature.com/articles/s41419-023-05875-0
46. Qinfan Y, Cuili W, Yucheng W, Xiuyuan Z, Hong J, Dajin C. The integrated comprehension of lncRNA HOXA-AS3 implication on human diseases.. Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9568475/
47. Available from: https://www.uniprot.org/uniprotkb/Q7Z553/entry
48. David CB, Erhard H. Structural Basis for the Initiation of Glycosaminoglycan Biosynthesis by Human Xylosyltransferase 1.. Structure (London, England : 1993) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5992326/
49. Tomoyuki I, Yoko M, Tetsuya Y, Miyuki T, Fumiaki S, Jeffrey RJ, et al.. Monoallelic mutations in MMD2 cause autosomal dominant aggressive periodontitis.. The Journal of experimental medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40663042/
50. Jessica MP, Ev LN, Robert GS, Jesse BH, Juan LM, Rob M, et al.. Structural insights into the formation of repulsive netrin guidance complexes.. Science advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10871540/
51. Tomoyuki I, Yoko M, Tetsuya Y, Miyuki T, Fumiaki S, Jeffrey RJ, et al.. Monoallelic mutations in MMD2 cause autosomal dominant aggressive periodontitis.. The Journal of experimental medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12262042/
52. Available from: https://www.proteinatlas.org/ENSG00000122547-EEPD1
53. Satoru Y, Falko H, Katsuhiko H, Daniel DT, Manuela S, Elena K, et al.. FLRT2 and FLRT3 act as repulsive guidance cues for Unc5-positive neurons.. The EMBO journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3160250/
54. Chaitanya T, Lohitash K. Glycomaterials to Investigate the Functional Role of Aberrant Glycosylation in Glioblastoma.. Advanced healthcare materials [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9048137/
55. Available from: https://academic.oup.com/edrv/article/27/1/47/2355165
56. Mirakaj V, Brown S, Laucher S, Steinl C, Klein G, Köhler D, et al.. Repulsive guidance molecule-A (RGM-A) inhibits leukocyte migration and mitigates inflammation. Proceedings of the National Academy of Sciences [Internet]. 2011Apr5;108(16). Available from: https://www.pnas.org/doi/10.1073/pnas.1015605108
57. Meghan TL, Kallie EW, Gregory S, Wujun Z, Leidong M, Qun Z, et al.. Surfen-mediated blockade of extratumoral chondroitin sulfate glycosaminoglycans inhibits glioblastoma invasion.. FASEB journal : official publication of the Federation of American Societies for Experimental Biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6902699/
58. Lincoln RP, Sarah A-H, Deborah MD. Natriuretic peptides, their receptors, and cyclic guanosine monophosphate-dependent signaling functions.. Endocrine reviews [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/16291870/
59. Brian K, Grace JL. Repulsive guidance molecule A (RGMa): a molecule for all seasons.. Cell adhesion & migration [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3499317/
60. Available from: http://json-schema.org/draft-07/schema#"
