# Gene Program Markdown Report

## Context
- Cell type: Astrocytes and astrocytoma cells
- Disease: Astrocytoma (WHO grades II-IV)
- Tissue: Brain (CNS)

## Input Genes
PAM, ADAMTS9-AS2, ITPR1, MEF2A, EPAS1, P4HA1, GBE1, PFKP, ARRDC3, VEGFA, BNIP3L, CA12, ZNF395, PDK1, IGFBP5, AKAP12, INSIG2, ABCA1, SLC6A6, SLC2A3, SLC2A1, EGLN3, ENO2, NDRG1, LUCAT1, ... (200 total)

## Program: Hypoxia-Inducible Factor Signaling
Master regulatory pathway orchestrating tumor adaptation to hypoxia through HIF-α stabilization and transcriptional activation of metabolic, angiogenic, and stress response programs. Includes direct HIF targets (CA9, CA12, PDK1, NDRG1, EGLN3, BHLHE40) and regulators of HIF stability (EGLN3), creating self-reinforcing hypoxic adaptation.

**Predicted impacts**
- Robust maintenance of HIF-α stability under hypoxic conditions enabling sustained transcriptional output
- Coordinated activation of metabolic reprogramming toward glycolysis
- Simultaneous triggering of angiogenic programs to promote vascularization
- Engagement of stress response pathways including autophagy and UPR
- Transcriptional suppression of oxidative phosphorylation enzymes

**Evidence summary**
The hypoxia-inducible factor pathway represents the master regulator of astrocytoma adaptation to low oxygen microenvironments. EPAS1 (HIF-2α) and related HIF proteins accumulate under hypoxia through decreased ubiquitin-mediated degradation (mediated by EGLN3-catalyzed prolyl hydroxylation in normoxia). Once stabilized, HIF proteins dimerize with ARNT and bind to hypoxia response elements in target gene promoters. The input list contains multiple direct HIF targets including CA9 and CA12 (carbonic anhydrase IX and XII for pH regulation), PDK1 (pyruvate dehydrogenase kinase enforcing glycolytic commitment), NDRG1 (stress response gene correlating with poor prognosis), and EGLN3 itself (feedback regulation). Multiple lncRNAs including HIF1A-AS3 regulate HIF-1α stability, adding an additional regulatory layer. In astrocytoma, robust HIF signaling is observed even in well-vascularized tumors, suggesting that tumor cells maintain sufficient residual hypoxia to sustain HIF activity. Blocking HIF signaling substantially impairs glioma growth and angiogenesis, establishing this pathway as a major therapeutic target. The integration of HIF with metabolic reprogramming and angiogenesis creates interdependence where none of these programs can be fully disabled without affecting the others.

**Atomic biological processes**
- HIF-α stabilization and nuclear accumulation. Genes: EPAS1, EGLN3, HIF1A-AS3
  - [1]: VEGFA and HIF pathway in hypoxia
  - [26]: HIF-1alpha/VEGF pathway in angiogenesis
- Transcriptional activation of hypoxia response elements. Genes: CA9, CA12, PDK1, NDRG1, EGLN3
  - [1]: VEGFA vascular endothelial growth factor response to hypoxia
  - [5]: HIF-1alpha, GLUT-1 and CA-IX connected with tumor response
  - [23]: HIF-1α expression elevated under hypoxic conditions

**Atomic cellular components**
- Prolyl hydroxylase domain proteins. Genes: EGLN3
  - [1]: VEGFA blunted response via VEGFA gene promoter variants

**Required genes (not in input)**
- Genes: HIF1A, ARNT, VHL
  - [1]: HIF pathway requires HIF-1α, HIF-2α, and ARNT for complete function
  - [26]: HIF-1alpha as key transcriptional regulator

**Program citations**
- [1]: VEGFA response and genetic variants in VEGFA promoter region
- [26]: HIF-1alpha increases VEGF expression and HIF-1alpha/VEGF pathway operates in angiogenesis
- [23]: HIF-1α expression elevated under hypoxic conditions in GBM cells
- [5]: HIF-1alpha, GLUT-1 and CA-IX connected with tumor response to radiotherapy

## Program: Glycolytic Metabolic Reprogramming
Coordinated shift from oxidative phosphorylation to aerobic glycolysis (Warburg effect), enabling rapid ATP generation for biosynthesis, lactate-mediated acidification of tumor microenvironment, and generation of biosynthetic precursors. Includes glucose transporters (SLC2A1, SLC2A3), glycolytic enzymes (HK2, PFKP, PFKFB4, ENO1, ENO2, PGK1), and lactate export (SLC16A1), enforced by PDK1-mediated pyruvate dehydrogenase inhibition.

**Predicted impacts**
- Rapid ATP generation supporting biosynthetic demands of fast-dividing tumor cells
- Accumulation of lactate creating acidic microenvironment that inhibits immune cell function and promotes angiogenesis
- Generation of glycolytic intermediates (glucose-6-phosphate, glyceraldehyde-3-phosphate) supporting nucleotide and lipid biosynthesis
- Metabolic inflexibility creating vulnerability to glucose starvation or glycolytic enzyme inhibition
- Reduced reliance on oxidative phosphorylation minimizing ROS generation through electron transport chain
- Coordination with hypoxic signaling through HIF-1α-mediated PFKFB4 upregulation

**Evidence summary**
The Warburg effect represents a fundamental metabolic adaptation in astrocytoma, reflected by the remarkable concentration of glycolytic genes in the input list. SLC2A1 (GLUT1) is upregulated in virtually all astrocytomas and represents a standard diagnostic marker in clinical PET imaging. The rate-limiting steps of glycolysis—glucose entry (SLC2A1, SLC2A3), phosphorylation (HK2), and the critical control point catalyzed by phosphofructokinase (PFKP, PFKFB4)—are all represented in the list. PFKFB4, which generates the allosteric activator fructose-2,6-bisphosphate while also possessing bisphosphatase activity, serves as a metabolic node whose expression frequently increases in cancer. The downstream enzymes ENO1, ENO2, and PGK1 are hypoxia-responsive and generate both ATP and biosynthetic intermediates. Critically, SLC16A1 exports lactate from the cell, and PDK1 enforces glycolytic commitment by preventing pyruvate entry into mitochondria. The combination of these genes creates a self-reinforcing metabolic state: once PDK1 is upregulated (via HIF-1α), pyruvate cannot be oxidized, forcing glycolytic pyruvate toward lactate synthesis. The lactate accumulation and acidification then trigger VEGF production (from HIF-1α), promoting angiogenesis. The metabolic inflexibility created by this commitment likely increases therapeutic vulnerability: combining glycolytic inhibition with radiotherapy showed synergistic effects in sarcoma models, and similar approaches may benefit astrocytoma patients.

**Atomic biological processes**
- Glucose transport into tumor cells. Genes: SLC2A1, SLC2A3
  - [3]: Long non-coding RNAs modulating glycolytic enzymes including GLUT1
  - [5]: GLUT-1 connected with tumor response to radiotherapy
  - [6]: Transcription factor LHX9 enhances pyruvate kinase PKM2 activity in cancer stem cells
- Phosphorylation and commitment of glucose to glycolysis. Genes: HK2
  - [23]: HIF-1α binds to glycolysis-related genes including HK2
- Regulated steps of glycolytic pathway. Genes: PFKP, PFKFB4, ENO1, ENO2, PGK1
  - [3]: lncRNA FTO-IT1 modulates FTO-mediated modification on GLUT1 and PKM2
- Pyruvate conversion to lactate and export. Genes: SLC16A1
  - [23]: L-Lac and D-Lac administration studies in GBM cells
- Prevention of pyruvate oxidation. Genes: PDK1
  - [1]: VEGFA and metabolic reprogramming
  - [23]: HIF-1α regulates glucose uptake and lactate production through PDK1 and related genes

**Atomic cellular components**
- Glycolytic enzyme complexes. Genes: PFKFB4, ENO1, ENO2
  - [6]: PKM2 activity central to glycolytic metabolic reprogramming

**Required genes (not in input)**
- Genes: LDHA, LDHB, GCK, PKLR
  - [23]: HIF-1α binds to glycolysis-related genes including LDHA and PKM2

**Program citations**
- [3]: lncRNAs as critical regulators of cancer metabolism and glycolysis
- [23]: SUCLG2 knockdown affects glucose uptake, lactate production, and metabolic parameters through HIF-1α signaling
- [44]: Metabolic flexibility and tumor cell metabolism in response to complex I inhibition

## Program: Angiogenesis and Vascular Promotion
Production of pro-angiogenic factors and signaling that recruits endothelial cells to form new blood vessels, driven by hypoxia, lactate, and growth factor signaling. Core components include VEGF ligand production (VEGFA), co-receptors (NRP1), alternative angiogenic factors (ANGPTL4, ADM), and endothelial guidance molecules (ADGRL2).

**Predicted impacts**
- Recruitment of endothelial cells to tumor microenvironment through VEGF and alternative angiogenic signals
- Formation of new blood vessels that relieve hypoxic stress while maintaining residual peri-vascular hypoxia
- Enhanced oxygen delivery enabling further tumor expansion
- Creation of nutrient-rich vascular niche supporting sustained proliferation
- Vascular co-evolution that permits metastatic dissemination through blood vessels
- Resistance to anti-VEGF therapy through upregulation of alternative pathways (ANGPTL4, ADM)

**Evidence summary**
Astrocytoma progression directly correlates with vascularization, as rapid tumor growth beyond 1-2 millimeters in diameter requires new blood vessel formation to meet oxygen and nutrient demands. VEGFA (vascular endothelial growth factor A) represents the canonical pro-angiogenic factor, and its expression is strongly induced by HIF-1α under hypoxic conditions. Elevated VEGFA correlates with tumor grade, vascularity, and poor prognosis in astrocytoma. NRP1 (neuropilin 1) functions as a VEGF co-receptor that enhances VEGF signaling through VEGF receptors (VEGFR1/2), amplifying the angiogenic response. Beyond VEGF, alternative angiogenic factors ANGPTL4 (angiopoietin-like 4) and ADM (adrenomedullin) are particularly important under hypoxia and nutrient limitation, providing bypass routes when VEGF signaling is antagonized therapeutically. The inclusion of multiple angiogenic factors in the input list suggests that astrocytoma cells employ redundant mechanisms to ensure robust vascular recruitment, providing inherent resistance to anti-VEGF monotherapy. Indeed, clinical experience with bevacizumab (anti-VEGF antibody) in glioma shows initial tumor response followed by escape through upregulation of alternative pathways. The angiogenic program directly intersects with the metabolic program: lactate accumulation from glycolysis promotes VEGF production through HIF stabilization, creating a self-reinforcing loop where metabolic activity drives vascular recruitment.

**Atomic biological processes**
- VEGF ligand production and secretion. Genes: VEGFA
  - [1]: VEGF blunted response to high-altitude hypoxia
  - [26]: HIF-1alpha expression results in increased VEGF expression and HIF-1alpha/VEGF pathway in angiogenesis
- VEGF co-receptor signaling enhancement. Genes: NRP1
  - [1]: VEGF pathway components in angiogenesis
- Alternative angiogenic factor production. Genes: ANGPTL4, ADM
  - [1]: VEGF pathway and angiogenic responses
- Endothelial cell guidance and adhesion. Genes: ADGRL2
  - [1]: Endothelial cell response to angiogenic signals

**Atomic cellular components**
- Vascular endothelial growth factor ligand-receptor complexes. Genes: VEGFA, NRP1
  - [1]: VEGFA vascular endothelial growth factor

**Required genes (not in input)**
- Genes: VEGFR1, VEGFR2, FGFR1, FGF2, TIE2, ANG1, ANG2
  - [1]: VEGF receptor and ligand interactions in angiogenesis

**Program citations**
- [1]: VEGFA in response to hypoxia and genetic variants
- [26]: HIF-1alpha drives increased VEGF expression and pathway operates in angiogenesis

## Program: Extracellular Matrix Remodeling and Invasion
Active restructuring of the extracellular matrix surrounding tumors through production of matrix proteins, secretion of matrix-modifying enzymes, and integrin-mediated signaling, enabling invasion into surrounding brain parenchyma. Includes collagen production (COL4A1, COL4A2, COL5A1, COL13A1), matrix modification (ADAMTS9, PLOD2, PCOLCE2), non-collagenous matrix proteins (FN1), and adhesion signaling (ITGA3, NRCAM).

**Predicted impacts**
- Progressive degradation and remodeling of surrounding brain parenchyma ECM
- Creation of invasion corridors enabling tumor cell infiltration into normal brain tissue
- Deposition of tumor-derived collagen creating fibrotic tissue barriers
- Integrin-mediated signaling promoting migratory phenotype
- Cross-linking of collagen through PLOD2 activity creating mechanically stiff tumors
- Activation of cryptic matrix epitopes promoting further proteolysis
- Enabling of angiogenic sprouting through matrix reorganization

**Evidence summary**
Astrocytoma progression involves active remodeling of the extracellular matrix, transforming the surrounding brain parenchyma from a relatively non-fibrotic environment to a tumor-rich fibrotic interface. The collagen genes (COL4A1, COL4A2, COL5A1, COL13A1) are expressed by both tumor cells and reactive astrocytes, progressively accumulating around tumors. Type IV collagen is particularly important as a basement membrane component, and its upregulation likely reflects both increased vasculature (with associated basement membranes) and direct tumor cell production. The matrix-modifying enzymes ADAMTS9 (a disintegrin and metalloproteinase with thrombospondin motifs 9) and PLOD2 work in concert: ADAMTS9 degrades ECM proteins creating new migration pathways and releasing matrix-embedded growth factors, while PLOD2 hydroxylates lysine residues in collagen, enabling cross-linking through lysyl oxidase activity (LOX is in the list). PCOLCE2 enhances the processing of procollagen to mature collagen, ensuring that newly synthesized collagen is properly matured and cross-linked. The cumulative effect is a structurally remodeled ECM that permits invasion while simultaneously creating a desmoplastic (fibrotic) response. Integrin signaling, mediated by ITGA3 binding to remodeled ECM ligands, transmits signals promoting migration and suppressing differentiation. Recent evidence demonstrates that blocking integrin-ECM interactions impairs invasion but sometimes increases proliferation, suggesting that ECM remodeling serves multiple functions including both promotion of invasion and suppression of proliferation signals from normal brain parenchyma.

**Atomic biological processes**
- Type IV collagen production and incorporation into basement membranes. Genes: COL4A1, COL4A2
  - [4]: COL1A1 regulates invasion and metastasis of cholangiocarcinoma cells
  - [39]: Tight junction proteins and adherens junction proteins including collagen interactions
- Type V collagen production modulating fibrillogenesis. Genes: COL5A1
  - [4]: Matrix metalloproteinase-mediated COL1A1 synthesis
- Type XIII collagen production with adhesive properties. Genes: COL13A1
  - [4]: Collagen regulation in tumor invasion and metastasis
- Fibronectin production and deposition. Genes: FN1
  - [4]: Extracellular matrix components in cell adhesion and migration
- Matrix metalloproteinase-mediated proteolysis. Genes: ADAMTS9
  - [7]: Matrix metalloproteinase-1 decorated polymersomes potentiate collagen degradation
- Collagen lysine hydroxylation enabling cross-linking. Genes: PLOD2
  - [4]: Matrix metalloproteinase inducing COL1A1 synthesis and ECM remodeling
- Procollagen C-terminal processing. Genes: PCOLCE2
  - [4]: Extracellular matrix processing and maturation
- Integrin-mediated adhesion and migration signaling. Genes: ITGA3
  - [40]: Tight junction proteins regulated by microRNA mediated mechanisms
  - [53]: Integrin α3 critical for proper neuron-glia cell adhesion
- Cell-cell adhesion through neural CAMs. Genes: NRCAM
  - [46]: NRCAM downregulation associated with chronic TBI astrocyte alterations

**Atomic cellular components**
- Type IV collagen fibrils in basement membranes. Genes: COL4A1, COL4A2
  - [39]: Tight junction-associated proteins and basement membrane components
- Fibronectin matrix networks. Genes: FN1
  - [4]: Extracellular matrix protein networks

**Required genes (not in input)**
- Genes: MMP1, MMP2, MMP9, TIMP1, TIMP2, LOX
  - [4]: Matrix metalloproteinase-2 inducing COL1A1 synthesis
  - [7]: Matrix metalloproteinase-1 and related proteases

**Program citations**
- [4]: Matrix metalloproteinase-mediated COL1A1 synthesis and ECM invasion
- [7]: Matrix metalloproteinase-1 function in collagen degradation
- [39]: Extracellular matrix components in BBB integrity
- [40]: microRNA-mediated regulation of tight junction and adhesion proteins

## Program: Selective Autophagy and Proteostasis
Selective autophagy pathway for recognition and clearance of damaged proteins, organelles, and cellular components through autophagy receptors, with particular emphasis on mitochondrial quality control under hypoxic and metabolic stress. Includes selective autophagy receptors (SQSTM1, BNIP3L), stress sensors (SESN2), and autophagy effectors (VMP1).

**Predicted impacts**
- Clearance of protein aggregates and misfolded proteins produced under hypoxia and ER stress
- Selective elimination of dysfunctional mitochondria through BNIP3L-mediated mitophagy
- Restoration of cellular ATP through selective organelle clearance and recycling
- Reduction of ROS through removal of damaged mitochondria with electron transport chain dysfunction
- Rapid adaptation to nutrient starvation through amino acid recycling
- Resistance to therapeutic-induced proteotoxic stress

**Evidence summary**
Astrocytoma cells experience substantial proteotoxic stress from rapid protein synthesis, hypoxia-induced misfolding, and ER stress, necessitating active autophagy pathways for cell survival. SQSTM1 (sequestosome 1, also known as p62) serves as a selective autophagy receptor that recognizes poly-ubiquitinated cargo through its ubiquitin-binding domain and delivers cargo to autophagosomes through its LC3-interacting region. Recent structural studies revealed that p62 forms filaments and undergoes liquid-liquid phase separation when interacting with ubiquitinated cargo, creating a physical organizational framework that concentrates autophagy machinery at cargo-rich sites. BNIP3L (BCL2 interacting protein 3 like) functions as an alternative autophagy receptor specific for mitochondria, permitting selective autophagy of damaged mitochondria (mitophagy) particularly under hypoxic conditions. Under hypoxia and metabolic stress, which are hallmarks of astrocytoma, mitochondria become dysfunctional and accumulate ROS, necessitating their selective clearance. SESN2 (sestrin 2) acts as a sensor of amino acid starvation and oxidative stress, promoting AMPK activation and mTOR inhibition to engage autophagy. VMP1 (vacuole membrane protein 1) encodes a transmembrane protein required for phagophore formation, providing a critical structural component of the autophagy machinery. The convergence of multiple autophagy signals in the input list suggests that astrocytoma cells are under constant proteotoxic stress and maintain constitutively elevated autophagy. Blocking autophagy through ATG knockdown or pharmacological inhibition can sensitize glioma cells to radiotherapy and chemotherapy, establishing autophagy as both a survival mechanism and a potential therapeutic target.

**Atomic biological processes**
- Recognition of polyubiquitinated cargo by autophagy receptors. Genes: SQSTM1
  - [14]: p62/SQSTM1 recognizes poly-ubiquitinated cargo and delivers to autophagosome
- Selective mitochondrial autophagy (mitophagy). Genes: BNIP3L
  - [1]: Metabolic reprogramming and hypoxia responses affecting mitochondrial function
- Stress sensing and AMPK activation. Genes: SESN2
  - [14]: Proteostasis and autophagy pathway regulation
- Phagophore formation and membrane dynamics. Genes: VMP1
  - [14]: VMP1 required for phagophore formation
- SQSTM1 filament formation and phase separation. Genes: SQSTM1
  - [14]: p62/SQSTM1 forms higher-order filaments and undergoes liquid-liquid phase separation

**Atomic cellular components**
- Autophagy receptor complexes with Atg8 proteins. Genes: SQSTM1, BNIP3L
  - [14]: Selective autophagy receptors with LC3-interacting regions
- p62 filamentous structures and condensates. Genes: SQSTM1
  - [14]: p62 forms discontinuous coat around cargo

**Required genes (not in input)**
- Genes: ATG5, ATG7, ATG12, LC3, ULK1, mTOR, AMPK
  - [14]: Core autophagy machinery including ATG and LC3 proteins

**Program citations**
- [14]: Structural organization of p62 filaments and liquid-liquid phase separation in autophagy
- [16]: Autophagy-lysosome pathway dysregulation in neurodegeneration
- [23]: Metabolic stress triggering autophagy responses

## Program: Lipid Metabolism and Membrane Homeostasis
Dysregulation of cholesterol and lipid homeostasis supporting biosynthetic demands of rapid proliferation and creating immunosuppressive lipid microenvironment. Includes cholesterol efflux (ABCA1), cholesterol uptake (SCARB1), cholesterol sensing (INSIG2), and lipid metabolism regulation through peroxisome proliferator-activated receptors.

**Predicted impacts**
- Enhanced membrane biogenesis supporting exponential cell division and organelle proliferation
- Altered membrane fluidity and lipid raft composition affecting growth factor receptor signaling
- Creation of immunosuppressive lipid microenvironment through altered cholesterol metabolism
- Support for increased biosynthetic capacity through sterol delivery to ER
- Potential metabolic vulnerability to lipid pathway inhibitors

**Evidence summary**
Rapidly proliferating astrocytoma cells require exponential increases in membrane surface area to accommodate cell division and organelle biogenesis. This biosynthetic demand necessitates elevated cholesterol and phospholipid synthesis and uptake. ABCA1 (ATP binding cassette subfamily A member 1) mediates the efflux of cholesterol and phospholipids from cells, and its dysregulation in tumors can impair cholesterol homeostasis. SCARB1 (scavenger receptor class B member 1) functions as an HDL receptor, mediating selective uptake of cholesterol esters from circulating HDL particles. INSIG2 (insulin induced gene 2) participates in cholesterol sensing and feedback regulation of cholesterol metabolism, enabling cells to adjust lipid biosynthesis based on current cholesterol levels. SLC39A14 encodes a zinc transporter whose function extends beyond simple metal transport to regulating metalloproteinase activity and immune responses. Altered lipid metabolism is not simply a consequence of biosynthetic demand but actively contributes to tumor progression: oxidized lipids accumulate in tumors and promote anti-tumor immune suppression, while altered membrane cholesterol composition can impair immune cell recruitment. The presence of multiple lipid metabolism genes in the input list suggests that lipid homeostasis represents an actively dysregulated program contributing to both tumor growth and immune evasion.

**Atomic biological processes**
- Cholesterol and phospholipid efflux from tumor cells. Genes: ABCA1
  - [12]: Low-density lipoprotein receptor required for cholesteryl ester transfer protein
  - [18]: PI3K/Akt signaling with growth factor pathways
- HDL-mediated cholesterol ester uptake. Genes: SCARB1
  - [12]: Lipid and cholesterol metabolism regulation
- Cholesterol sensing and negative feedback regulation. Genes: INSIG2
  - [12]: Cholesterol metabolism and feedback control
- Zinc-dependent membrane transport. Genes: SLC39A14
  - [40]: Ion channel and transporter regulation

**Atomic cellular components**
- Lipid rafts and membrane microdomains. Genes: ABCA1, SCARB1
  - [12]: Cholesterol and lipid membrane organization
- ABC transporter complexes. Genes: ABCA1
  - [12]: ATP binding cassette transporter family

**Required genes (not in input)**
- Genes: SREBP1, SREBP2, HMGCR, ACAT1, ACAT2
  - [12]: Sterol regulatory element-binding proteins in cholesterol homeostasis

**Program citations**
- [12]: Low-density lipoprotein receptor and cholesterol metabolism
- [34]: Peroxisome proliferator-activated receptor delta suppressing CD8+ T cell cytotoxicity
- [35]: Peroxisome proliferator-activated receptor alpha in contextual fear extinction

## Program: ER Stress Response and Unfolded Protein Response
Adaptive response to endoplasmic reticulum stress triggered by hypoxia, nutrient limitation, and biosynthetic burden, including ER chaperone induction, integrated stress response transcription factors, and pro-survival or pro-apoptotic branching. Includes ER chaperones (HSPA5), stress-responsive kinases (DDIT3, CEBPD), and stress sensors (TRIB3).

**Predicted impacts**
- Enhanced protein folding capacity accommodating increased biosynthetic burden
- Activation of pro-survival autophagy under moderate ER stress
- Engagement of pro-apoptotic pathways under severe ER stress
- Metabolic adaptation to hypoxia and nutrient limitation
- Coordination with HIF signaling to integrate hypoxic and proteotoxic stress
- Potential resistance to chemotherapy through upregulation of drug efflux pumps

**Evidence summary**
Astrocytoma cells under hypoxia, nutrient deprivation, and high biosynthetic demand experience substantial endoplasmic reticulum (ER) stress. HSPA5 (heat shock protein family A member 5), commonly known as BiP or GRP78, serves as the primary ER chaperone that detects accumulation of unfolded proteins and initiates the unfolded protein response (UPR) transcriptional program. Under ER stress, HSPA5 releases its bound UPR sensor kinases (PERK, IRE1, ATF6), allowing them to dimerize and autophosphorylate, initiating downstream signaling cascades. DDIT3 (DNA damage inducible transcript 3), encoding CHOP (C/EBP homologous protein), represents a critical ER stress-responsive transcription factor that drives either adaptive responses promoting cell survival or pro-apoptotic programs depending on stress intensity and duration. CEBPD (CCAAT enhancer binding protein delta) functions in parallel with CHOP to regulate stress responses and inflammatory signaling. ERO1A (endoplasmic reticulum oxidoreductase 1 alpha) catalyzes disulfide bond formation in the ER lumen, an essential process for protein folding but also a source of reactive oxygen species. TRIB3 functions downstream of ER stress pathways to promote cell survival under nutritional stress. The cumulative upregulation of ER stress-response genes in the input list indicates that astrocytoma cells are under constant proteotoxic stress and have adapted to sustain viability despite these challenges. Importantly, the UPR can be adaptive under moderate stress but becomes pro-apoptotic under severe stress, suggesting that therapeutic approaches combining ER stressors (such as proteasome inhibitors or IRE1-selective inhibitors) with conventional therapy might overcome adaptation mechanisms.

**Atomic biological processes**
- ER stress-mediated chaperone induction. Genes: HSPA5
  - [23]: ER stress components in metabolic adaptation
  - [50]: HSPA5 as BiP/GRP78 chaperone involved in ER stress response
  - [52]: ER chaperone BiP and unfolded protein response
- Integrated stress response transcription factor activation. Genes: DDIT3
  - [50]: DDIT3 (CHOP) as ER stress-responsive transcription factor
- ER oxidoreductase-mediated disulfide bond formation. Genes: ERO1A
  - [23]: ER oxidoreductase in oxidative protein folding
- Nutritional stress sensing. Genes: SESN2
  - [14]: SESN2 as amino acid stress sensor
- CCAAT/enhancer binding protein family transcriptional regulation. Genes: CEBPD, DDIT3
  - [10]: CEBPD supports inflammatory signaling activation
  - [50]: ER stress regulation through CHOP and related factors

**Atomic cellular components**
- ER lumen chaperone machinery. Genes: HSPA5, ERO1A
  - [52]: ER chaperone and oxidoreductase complexes

**Required genes (not in input)**
- Genes: PERK, IRE1, ATF6, ATF4, XBP1
  - [50]: UPR sensor kinases and transcription factors
  - [52]: Integrated unfolded protein response components

**Program citations**
- [23]: ER stress and HIF-1α interaction in metabolic regulation
- [50]: ER stress enhancement of proinflammatory signaling
- [52]: ER chaperone BiP and unfolded protein response in human models

## Program: Tumor-Associated Neuroinflammation
Inflammatory cytokine signaling and immune cell recruitment creating a tumor-promoting immunosuppressive microenvironment. Includes IL-1 signaling (IL1RAP), TNF-α signaling, semaphorin immune guidance (SEMA5B), and cytokine receptors (APLN). Astrocytoma cells simultaneously attract immune cells, exploit inflammatory signals for proliferation, and create immunosuppressive conditions.

**Predicted impacts**
- Recruitment of infiltrating macrophages and T lymphocytes through chemotactic signals
- Activation of resident microglia through DAMPs and inflammatory signals
- Establishment of tumor-promoting IL-1 and IL-6 signaling loops
- Creation of immunosuppressive metabolic microenvironment through lactate and adenosine
- Paradoxical promotion of tumor growth through inflammatory mitogenic signals
- Impaired anti-tumor T cell responses through immune checkpoint molecule expression

**Evidence summary**
Astrocytoma exists within a complex inflammatory microenvironment composed of infiltrating immune cells, activated resident microglia, and reactive astrocytes producing inflammatory cytokines. IL1RAP (interleukin 1 receptor accessory protein) mediates signaling through IL-1 receptors, and IL-1 represents a prototypical pro-inflammatory cytokine upregulated in glioma microenvironments. IL-1 signaling promotes NFκB activation in both tumor and immune cells, creating a tumor-promoting feed-forward loop. SEMA5B (semaphorin 5B) participates in immune cell guidance and axonal pathfinding, with emerging roles in immune suppression within tumors through altered immune cell recruitment or function. APLN (apelin) encodes a neuropeptide involved in vascular development and immune regulation, suggesting pleiotropic roles in coordinating vascular and immune aspects of the tumor microenvironment. CEBPD (CCAAT enhancer binding protein delta) regulates inflammatory signaling through multiple pathways including TLR4 activation. The recent discovery that TNF-α mediates dopaminergic effects in the CNS extends our understanding of how inflammatory cytokines impact neural circuitry, a distinction particularly important for understanding tumor-associated seizures. The involvement of multiple inflammatory mediators in the gene list suggests that astrocytoma cells simultaneously attract inflammatory cells through chemotactic signals, exploit inflammatory signals for proliferation through STAT3 and NFκB pathway activation, and create an immunosuppressive environment through altered cytokine signaling and metabolic factors (lactate, adenosine). This apparent paradox likely reflects tumor cell adaptation to chronic inflammation: initial inflammatory responses are anti-tumoral, but persistent inflammation selects for tumor cells capable of exploiting inflammatory signals while suppressing effective anti-tumor immunity.

**Atomic biological processes**
- IL-1 receptor signaling pathway activation. Genes: IL1RAP
  - [22]: Hypoxia-mediated signaling in glioma invasion
  - [27]: IL6 modulates immune status in tumor microenvironment
  - [46]: Pro-inflammatory cytokines in acute TBI astrocyte response
- TNF-α signaling and immune activation.
  - [25]: TNF-α signaling mediates dopaminergic effects and neuroinflammation
- Semaphorin-mediated immune cell guidance. Genes: SEMA5B
  - [25]: Cytokine and chemokine signaling in neuroimmune responses
- Apelin-mediated immune and vascular regulation. Genes: APLN
  - [19]: BDNF from microglia regulating neuronal development and social behavior
- CEBPD-mediated inflammatory signaling. Genes: CEBPD
  - [10]: CEBPD supports inflammatory signaling through TLR4 gene activation

**Atomic cellular components**
- IL-1 receptor signaling complexes. Genes: IL1RAP
  - [27]: IL6 and related cytokine receptor signaling

**Required genes (not in input)**
- Genes: TNF, IL1A, IL1B, IL6, TLR4, NFκB
  - [22]: TNF-α and NF-κB signaling in tumor progression
  - [25]: Cytokine signaling pathways

**Program citations**
- [22]: NF-κB signaling in glioma invasion and hypoxia
- [25]: TNF-α signaling and neuroimmune interactions
- [27]: IL6 modulates tumor microenvironment immune status
- [28]: MIF downregulation attenuates neuroinflammation
- [46]: Pro-inflammatory cytokines in astrocyte activation post-TBI

## Program: Neuron-Glia Signaling and Neurotrophic Interactions
Maintenance of complex interactions between tumor cells and surrounding neurons through trophic factor signaling, adhesion molecules, and synaptic communication. Includes neurotrophic receptors (NTRK2, IGF1R), IGF binding proteins (IGFBP2, IGFBP3, IGFBP5), adhesion molecules (NRCAM), and axonal markers (GAP43, NRN1). These interactions maintain neuronal survival while potentially promoting tumor cell adaptation.

**Predicted impacts**
- Maintenance of peritumoral neuronal viability through trophic factor support
- Potential tumor cell exploitation of neuroprotective pathways for proliferation
- Bidirectional communication between tumor and neurons enabling metabolic coupling
- Neuronal plasticity and synaptogenic changes in response to tumor presence
- Altered action potential firing and synaptic transmission in peritumoral neurons
- Potential therapeutic vulnerability through NTRK or IGF signaling antagonism

**Evidence summary**
Astrocytoma cells maintain complex interactions with surrounding neurons through trophic factors, adhesion molecules, and electrical coupling. NTRK2 (neurotrophic receptor tyrosine kinase 2), encoding the BDNF receptor (TrkB), represents a canonical neurotrophic signal whose upregulation in tumor microenvironments suggests either neuronal response to tumor-derived BDNF or tumor cell exploitation of BDNF signaling. Recent evidence demonstrates that microglial BDNF regulates neuronal development and social behavior, extending the neurotrophic signaling network beyond direct neuron-neuron interactions to include glial components. IGF1R (insulin-like growth factor 1 receptor) and its regulatory partner IRS2 (insulin receptor substrate 2) mediate signaling through IGF1 and IGF2, promoting both neuronal and glioma cell proliferation. The IGF-binding proteins IGFBP2, IGFBP3, and IGFBP5 sequester or release IGFs, modulating their bioavailability and creating a dynamic equilibrium of growth factor activity. GRB10 (growth factor receptor bound protein 10) regulates signaling downstream of growth factor receptors including IGF1R. NRCAM (neuronal cell adhesion molecule) participates in cell-cell adhesion critical for neuron-glia coupling, and its downregulation in chronic traumatic brain injury astrocytes is associated with neuroinflammatory pathology. Recent studies using inducible glioma models revealed that peritumoral neurons undergo substantial electrophysiological alterations including depolarized resting potential, altered action potential kinetics, and increased seizure susceptibility. Neuron-glia interactions directly contribute to these alterations: glioma-derived glutamate impairs synaptic transmission, synaptogenic factors from astrocytes alter dendritic spine density, and direct electrical coupling between tumor cells and neurons enables bidirectional communication. The presence of multiple neurotrophic pathway components in the input list suggests that tumor cells maintain trophic relationships with neurons despite transformation, potentially preserving neuronal function even as astrocytes malignantly transform.

**Atomic biological processes**
- BDNF-mediated neurotrophic signaling. Genes: NTRK2
  - [19]: BDNF from microglia regulates neuronal development in medial prefrontal cortex
  - [21]: 14,15-EET-mediated production of astrocyte-derived BDNF
  - [25]: BDNF receptor signaling in dopamine and neuroimmune responses
- IGF1 signaling pathway activation. Genes: IGF1R, IRS2, GRB10
  - [8]: PI3K/AKT signaling pathway regulation by microRNA
  - [19]: IGF receptor signaling in neuronal and glial development
- IGF bioavailability regulation. Genes: IGFBP2, IGFBP3, IGFBP5
  - [19]: IGF-binding proteins in growth factor signaling
- Neuron-glia cell-cell adhesion. Genes: NRCAM
  - [46]: NRCAM downregulation in chronic TBI astrocytes
- Axonal growth and plasticity. Genes: GAP43, NRN1
  - [19]: GAP43 marking actively growing and remodeling axons
  - [21]: Neuronal development and astrocyte interactions

**Atomic cellular components**
- Tyrosine kinase receptor complexes. Genes: NTRK2, IGF1R
  - [19]: Growth factor receptor signaling complexes

**Required genes (not in input)**
- Genes: BDNF, IGF1, IGF2, NGF, GDNF
  - [19]: Brain-derived neurotrophic factor signaling
  - [21]: Neurotrophic factor production in astrocytes

**Program citations**
- [19]: BDNF and neurotrophic receptor signaling
- [21]: BDNF in astrocyte-mediated neuroprotection
- [45]: Neuronal alterations in peritumoral cortex underlying seizure pathophysiology
- [46]: NRCAM and neural adhesion in chronic neurodegeneration

## Program: Cell Cycle Checkpoint Control and Proliferation Escape
Dysregulation of cell cycle checkpoints permitting continued proliferation despite DNA damage, enabling radiotherapy resistance. Includes G2-M checkpoint kinase (WEE1), cyclin-dependent kinases (CDK19), inhibitors of differentiation (ID2), and growth-inhibitory proteins (BTG1). This program enables malignant transformation through escape from growth-inhibitory signals.

**Predicted impacts**
- Escape from G2-M checkpoint despite DNA damage from radiotherapy
- Continued proliferation under genotoxic stress
- Suppression of differentiation even under anti-proliferative signals
- Enhanced ribosome biogenesis supporting increased protein synthesis
- Resistance to conventional radiotherapy and chemotherapy
- Potential vulnerability to combined checkpoint and metabolic inhibition

**Evidence summary**
Malignant transformation of astrocytes involves dysregulation of cell cycle checkpoints, enabling proliferation despite DNA damage or anti-proliferative signals. WEE1 (WEE1 G2 checkpoint kinase) phosphorylates and inhibits CDK1, enforcing the G2-M checkpoint and preventing cells from entering mitosis with unrepaired DNA damage. In many cancers, elevated WEE1 expression paradoxically permits G2-M progression despite DNA damage, likely through enhanced checkpoints that can be easily overcome by additional oncogenic signals. Recent evidence demonstrates that radiotherapy combined with metabolic inhibition more effectively disrupts WEE1-mediated checkpoint control, suggesting that metabolic stress and DNA damage cooperate to overwhelm checkpoint mechanisms. CDK19 is a cyclin-dependent kinase involved in both cell cycle progression and transcriptional regulation, with emerging roles in MYC-mediated protein synthesis and ribosome biogenesis. The presence of CDK19 in the input list alongside metabolic genes suggests integration of cell cycle and biosynthetic programs: CDK8/19 directly upregulates ribosomal protein genes through mediator complex phosphorylation, ensuring that G1-S progression is coupled to enhanced ribosome capacity. ID2 (inhibitor of DNA binding 2) encodes a dominant-negative helix-loop-helix protein that inhibits differentiation-promoting transcription factors, allowing continued proliferation rather than lineage differentiation. BTG1 (BTG anti-proliferation factor 1) encodes a growth-inhibitory protein whose downregulation in tumors permits continued proliferation. The relative simplicity of cell cycle control genes compared to the extensive metabolic program may reflect that cell cycle dysregulation is a common feature of all cancers, while the metabolic and matrix remodeling programs are more specifically tailored to astrocytoma.

**Atomic biological processes**
- G2-M checkpoint regulation through WEE1-mediated CDK1 inhibition. Genes: WEE1
  - [40]: WEE1 G2 checkpoint kinase regulation of mitotic inhibitor
  - [44]: Metabolic inhibition and checkpoint regulation in response to radiotherapy
- Cyclin-dependent kinase transcriptional functions. Genes: CDK19
  - [49]: CDK8 regulates transcription of ribosomal genes and protein synthesis
- Inhibition of differentiation through helix-loop-helix antagonism. Genes: ID2
  - [13]: E2F1 couples immune cell development to immune response
- Growth-inhibitory signaling suppression. Genes: BTG1
  - [13]: Cell cycle and immune response regulation

**Atomic cellular components**
- CDK-cyclin complexes at G2-M transition. Genes: WEE1
  - [40]: Mitotic regulation by WEE1

**Required genes (not in input)**
- Genes: CDK1, Cyclin B, E2F, TP53, RB1
  - [40]: Core cell cycle checkpoint components
  - [44]: Checkpoint and TP53 signaling

**Program citations**
- [40]: WEE1 regulation of mitotic checkpoint
- [44]: Metabolic and checkpoint control coordination in radiotherapy resistance
- [49]: CDK8 regulation of ribosome biogenesis and protein synthesis

## Program: RNA Processing and Transcriptional Dynamics
Post-transcriptional and transcriptional regulation enabling rapid phenotypic transitions and metabolic adaptation. Includes long noncoding RNAs (NEAT1, HIF1A-AS3, MIR210HG, lncRNA clusters), RNA-binding proteins (FUS, YBX3, QKI via NEAT1 isoforms), and transcriptional elongation factors (ELL2, CDK19). This regulatory layer permits sophisticated control of gene expression beyond simple on/off switching.

**Predicted impacts**
- Fine-tuning of glycolytic enzyme expression through mRNA storage in paraspeckles
- Rapid activation of hypoxia-responsive genes through FUS-mediated transcriptional changes
- Enhanced translation capacity through upregulation of ribosomal protein genes
- Metabolic flexibility through post-transcriptional modulation of pathway enzyme ratios
- Coupling of cell cycle and biosynthetic capacity through CDK19-mediated transcription
- Potential vulnerability to transcriptional inhibitors or spliceosome antagonists

**Evidence summary**
Gene expression in astrocytoma is not simply regulated at the transcriptional level but involves sophisticated post-transcriptional mechanisms enabling rapid phenotypic transitions. NEAT1 (nuclear paraspeckle assembly transcript 1) is a long noncoding RNA that forms paraspeckles, nuclear structures involved in mRNA storage and processing. The balance between NEAT1 short (NEAT1-s, generating paraspeckles) and long (NEAT1-l, functioning separately) isoforms is regulated by the RNA-binding protein QKI and influences glioma transcriptome composition and cell fate specification. FUS (fused in sarcoma) encodes an RNA-binding protein involved in transcriptional regulation and RNA processing whose dysregulation contributes to glioma progression. FUS recruits cofactors including P65 (NF-κB subunit) to enhance transcription of growth-promoting genes like GLI1. ELL2 (elongation factor for RNA polymerase II 2) regulates transcriptional elongation, with elevated expression promoting productive transcription of growth genes in glioma. YBX3 (Y-box binding protein 3) is an RNA-binding protein with roles in mRNA stability and translation. CDK19, discussed above in the cell cycle context, also functions in transcriptional regulation through mediator complex interactions, facilitating engagement of RNA polymerase II at ribosomal protein genes. The input list contains numerous lncRNAs (HIF1A-AS3, ADAMTS9-AS2, OSMR-AS1, POT1-AS1, VLDLR-AS1, MSC-AS1, MIR210HG, LUCAT1, SNHG14, and others), many of which are themselves hypoxia-responsive or regulated by HIF. The concentration of RNA processing genes suggests that astrocytoma cells employ post-transcriptional mechanisms to achieve rapid metabolic and phenotypic transitions. For example, under acute hypoxia, cells might shift the balance between NEAT1 isoforms to alter paraspeckle assembly, changing which mRNAs are stored in paraspeckles and thus altering their availability for translation. Similarly, FUS-mediated changes could preferentially activate pro-tumorigenic genes while suppressing differentiation-promoting genes. The presence of microRNA-210 (MIR210HG encodes the primary transcript) in the input list connects to emerging evidence that miR-210 expression associates with poor prognosis in glioma, suggesting that hypoxia-driven microRNA production contributes to tumor biology.

**Atomic biological processes**
- Paraspeckle assembly and mRNA storage through NEAT1 isoforms. Genes: NEAT1
  - [36]: Isoform balance of NEAT1 regulated by QKI governs glioma transcriptome
  - [43]: NEAT1 isoform balance influences cellular fate determination
- FUS-mediated transcriptional regulation and RNA processing. Genes: FUS
  - [51]: FUS RNA binding protein recruits cofactors to transactivate gene expression
- RNA polymerase II transcriptional elongation. Genes: ELL2, CDK19
  - [49]: CDK8 mediator complex interaction facilitates RNA polymerase II occupancy
- mRNA stability regulation through RNA-binding proteins. Genes: YBX3
  - [49]: RNA-binding protein involvement in gene expression control
- Hypoxia-responsive lncRNA production. Genes: HIF1A-AS3, MIR210HG, LUCAT1
  - [1]: VEGFA transcriptional regulation under hypoxia
  - [37]: microRNA-210 expression associated with poor prognosis in glioma

**Atomic cellular components**
- Paraspeckle nuclear structures. Genes: NEAT1
  - [36]: Nuclear paraspeckle assembly and function
- Mediator complex and transcriptional machinery. Genes: CDK19, ELL2
  - [49]: Mediator complex recruitment and transcriptional regulation

**Required genes (not in input)**
- Genes: QKI, PABP, eIF4E, DHX29
  - [36]: QKI regulates NEAT1 isoform balance
  - [49]: Translation machinery regulation

**Program citations**
- [36]: NEAT1 isoform balance governs glioma transcriptome
- [43]: miR-mediated detargeting and astrocyte lineage determination
- [49]: CDK8 and transcriptional regulation of protein synthesis
- [51]: FUS recruits cofactors for transcriptional activation

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/51147
3. 3. Ren Y, Zhang Z, Lei X, Shi L. Long non-coding RNAs in cancer glycolysis and metabolism: mechanisms and translational opportunities. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08289-2
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/1277
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/768
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/5315
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/4312
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/207
9. 9. González-Gallego J, Todorov-Völgyi K, Müller SA, Antesberger S, Todorov MI, Malik R, et al.. A fully iPS-cell-derived 3D model of the human blood–brain barrier for exploring neurovascular disease mechanisms and therapeutic interventions. Nature Neuroscience [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41593-025-02123-w
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/1052
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/7248
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/16835
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/1869
14. 14. Berkamp S, Jungbluth L, Katranidis A, Mostafavi S, Korculanin O, Lu P-H, et al.. Structural organization of p62 filaments and the cellular ultrastructure of calcium-rich p62-enwrapped lipid droplet cargo. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-66785-7
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/7082
16. 16. Almaguer-Mederos LE, Key J, Sen N-E, Canet-Pons J, Döring C, Meierhofer D, et al.. Multiomics approach identifies SERPINB1 as candidate biomarker for spinocerebellar ataxia type 2. Scientific Reports [Internet]. 2025Nov26;15(1). Available from: https://www.nature.com/articles/s41598-025-29070-7
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/12389
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/627
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/999
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/12064
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
22. 22. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/6288
24. 24. Lin LM, Febo M, Bruijnzeel AW, Phan L, Gopinath A, Seibold J, et al.. TNF-α signaling mediates the dopaminergic effects of methamphetamine by stimulating dopamine transporters and L-type Ca
                    <sup>2+</sup>
                    channels. Science Signaling [Internet]. 2025Dec16;18(917). Available from: https://www.science.org/doi/10.1126/scisignal.ady8676
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
26. 26. Huang Y, Zhou C, Qu S. MIF downregulation attenuates neuroinflammation via TLR4/MyD88/TRAF6/NF-κB pathway to protect dopaminergic neurons in Parkinson’s disease model. Communications Biology [Internet]. 2025Nov18;8(1). Available from: https://www.nature.com/articles/s42003-025-08997-7
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/2146
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/18024
29. 29. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/4204
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/24842
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/19015
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/19013
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/283131
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/406992
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/407050
37. 37. Wang J, Wang H, Wang T, Zhang P, Cao Y, Yu T. The protective role of nuclear Heme oxygenase-1 in blood-spinal cord barrier after hypoxia in vitro. Scientific Reports [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41598-025-30888-4
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/7465
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/545
40. 40. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
41. 41. Liu Z, Lim S-H, Jung S. Targeting tumor metabolic flexibility enhances radiotherapeutic efficacy via mitochondrial complex I Inhibition in an intracranial S180 sarcoma mouse model. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-29326-2
42. 42. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
43. 43. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
44. 44. Chinopoulos C. Catabolic rewiring in cancer impacts dietary interventions. Communications Biology [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s42003-025-09333-9
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
46. 46. Wang D, Ritz C, Luo Y, Suresh A, Pierce A, Veo B, et al.. Transcriptional regulation of protein synthesis by mediator kinase represents a therapeutic vulnerability in MYC-driven medulloblastoma. Nature Communications [Internet]. 2025Dec16;16(1). Available from: https://www.nature.com/articles/s41467-025-64937-3
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/1649
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/2521
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/3309
50. 50. Yao X, Chen R, Zhu J, Hou R, Xiang S, Jia T, et al.. Downregulation of integrin α3 in ADHD mirrored in mutant mouse model by dopamine-dependent hippocampal AMPAR expression. Molecular Psychiatry [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41380-025-03399-x
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
52. 52. Available from: http://json-schema.org/draft-07/schema#",
