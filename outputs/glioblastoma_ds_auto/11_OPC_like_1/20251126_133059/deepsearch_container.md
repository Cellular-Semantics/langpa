# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: IDH-wildtype glioblastoma (GBM)
- Tissue: brain

## Input Genes
AFAP1L2, COL4A3, FERMT1, VIPR2, AL512308.1, CALCRL, REPS2, FGF12, CCDC26, OTOGL, ELMO1, PCDH15, COL4A4, THSD4, FA2H, LRRC7, PLPP4, PLA2G4A, AR, LINC00689, TNS3, BCAS1, DLL3, KCNIP3, MIR503HG, ... (109 total)

## Program: Oligodendrocyte differentiation and myelin formation
A developmental transcriptional program that specifies cells toward the oligodendrocyte lineage and promotes myelination. This program includes master transcriptional regulators (MYRF, SOX6), structural myelin proteins (MOG, OMG, BCAS1, CLDN11), and enzymes essential for myelin lipid synthesis (UGT8, FA2H). In GBM context, dysregulation of this program reflects aberrant recapitulation of developmental processes and may be associated with cells occupying an uncommitted developmental state.

**Predicted impacts**
- Dysregulated recapitulation of developmental oligodendrocyte specification in infiltrative tumor regions
- Aberrant myelin lipid synthesis contributing to altered membrane composition and metabolic dependence
- Enhanced stemness and reduced differentiation commitment in infiltrative GBM cells
- Potential metabolic reprogramming toward lipid synthesis over classic oligodendrocyte functions

**Evidence summary**
Multiple genes in this program (MYRF, MOG, SOX6, UGT8, GPR17, CLDN11) are well-established as core regulators of oligodendrocyte differentiation and myelin maintenance. Recent spatial transcriptomics studies show that peritumoral GBM cells adopt oligodendrocyte progenitor cell (OPC)-like states with increased expression of developmental genes including those in this program. The program is particularly relevant to GBM because infiltrative cells show epigenetic signatures mirroring developing OPCs, suggesting neurodevelopmental hijacking of this developmental pathway.

**Atomic biological processes**
- Myelin protein expression and trafficking. Genes: MYRF, MOG, OMG, BCAS1, CLDN11
  - [28]: MYRF is essential transcriptional factor for myelin gene activation including MBP, PLP, MAG, MOG
  - [49]: MOG is late-stage oligodendrocyte marker, important for myelin sheath completion
  - [52]: MOG appears late in oligodendrocyte maturation, serves as marker of mature state
- Myelin lipid biosynthesis. Genes: UGT8, FA2H
  - [27]: UGT8 catalyzes galactosylceramide synthesis, key constituent of myelin sheaths; aberrantly upregulated in aggressive tumors
  - [30]: UGT8 expression associated with tumor aggressiveness and metastatic potential in breast cancer
- Oligodendrocyte progenitor differentiation. Genes: SOX6, GPR17
  - [15]: OLIG2 recruits SETDB1 for transcriptional repression, required for OPC differentiation and myelinogenesis
  - [24]: GPR17 opposes oligodendrocyte maturation, acts as cell-intrinsic timer of myelination

**Atomic cellular components**
- Myelin sheath structure. Genes: MOG, CLDN11, LAMB4
  - [49]: MOG is adhesion molecule providing structural integrity to myelin sheath

**Required genes (not in input)**
- Genes: SOX10, OLIG2, PDGFRA, MBP, PLP, CNP
  - [15]: SOX10 and OLIG2 are master regulators that activate myelin gene networks
  - [25]: MYRF-SOX10 feedback loop essential for myelin maintenance

**Program citations**
- [1]: Spatial transcriptomics reveals OPC-like malignant states in infiltrated brain tissue
- [5]: Peritumoral GBM cells have epigenetic encoding mirroring uncommitted developing OPCs
- [15]: OLIG2-SETDB1 complex essential for OPC differentiation and myelination
- [24]: GPR17 acts as intrinsic timer of myelination through ID protein regulation
- [25]: MYRF and SOX10 compose feedback regulatory loops for myelin development
- [27]: UGT8 catalyzes key myelin lipid synthesis step

## Program: Notch signaling and neural stem cell maintenance
The Notch pathway acts as a critical regulator of neural progenitor self-renewal and inhibition of differentiation in developing CNS. In GBM, elevated Notch signaling through ligands DLL1 and DLL3 maintains cancer stem cell properties and is particularly enriched in infiltrative tumor regions. This program operates downstream of ASCL1 and OLIG2, which are co-expressed transcriptional regulators that determine cellular plasticity and lineage specification in GBM.

**Predicted impacts**
- Enhanced maintenance of tumor-initiating cell populations with stem-like properties
- Resistance to differentiation cues and reduced lineage commitment
- Increased self-renewal capacity enabling recurrence and treatment resistance
- Spatial enrichment in infiltrative regions promoting brain invasion
- Activation of growth factor receptor pathways (EGFR, FGFR) downstream of Notch

**Evidence summary**
DLL1 and DLL3 are well-established Notch ligands that are specifically upregulated in infiltrative GBM regions compared to tumor core. Multiple studies show that higher Notch signaling correlates with worse prognosis and maintains glioma stem cell phenotype. LIN28B functions to repress the tumor-suppressive let-7 miRNA family, thereby maintaining expression of oncogenic factors like MYC and allowing sustained stemness. The program is particularly relevant in GBM because Notch signaling marks the transition from core to infiltrative tumor regions and promotes the acquisition of progenitor-like states.

**Atomic biological processes**
- Notch ligand-receptor interactions. Genes: DLL1, DLL3
  - [1]: Delta-like ligands (DLL1, DLL3) upregulated in infiltrated regions, associated with NPC-like states
  - [13]: DLL1 activation of Notch1 maintains stem cell phenotype of glioma initiating cells
  - [16]: DLL1 most upregulated gene in infiltrated brain tissue; NPC-like marker
- Stemness and self-renewal maintenance. Genes: LIN28B
  - [2]: ASCL1 and OLIG2 mark apex of GBM cellular hierarchy, determine NSC/astrocyte-like and OPC-like states
  - [13]: Notch signaling maintains glioma stem cell self-renewal and inhibits differentiation
  - [45]: LIN28B represses let-7 miRNAs, maintaining stem cell programs and pluripotency factors

**Required genes (not in input)**
- Genes: NOTCH1, NOTCH3, NOTCH4, HES1, HEY1, MAML1
  - [13]: NOTCH1, NOTCH3, NOTCH4 are key receptors; HES1 and HEY1 are downstream effectors

**Program citations**
- [1]: Spatial transcriptomics shows DLL1/DLL3 enriched in NPC-like states of infiltrated tissue
- [2]: ASCL1 and OLIG2 control Notch pathway and determine GBM cell type specification
- [13]: Comprehensive review of Notch signaling in GBM pathogenesis and stem cell maintenance
- [16]: DLL1 is leading gene upregulated in infiltrated regions, marks NPC-like malignant state
- [45]: LIN28-let-7 axis regulates stem cell self-renewal versus differentiation decision
- [48]: LIN28AB drives cancer stem cell maintenance through let-7 repression

## Program: Synaptic adhesion and neuronal crosstalk
GBM cells establish bidirectional communication with neurons through synaptic adhesion molecules and neurotrophic factors. This program includes cell adhesion molecules (ALCAM, LRRC7, MDGA2), guidance molecules (SLIT1, SEMA3E), and neuropeptide receptors (TACR1) that mediate neuron-tumor interactions. Active neuronal activity promotes GBM proliferation through secretion of factors including neuroligin-3 (NLGN3) and activation of growth factor pathways, establishing a tumor microenvironment permissive for GBM growth.

**Predicted impacts**
- Enhanced responsiveness to neuronal activity-dependent paracrine signals
- Increased proliferation in cortical regions with high neuronal density
- Spatial preference for infiltration toward neurons with high synaptic activity
- Establishment of stable neuron-tumor synaptic contacts promoting tumor growth
- Activation of growth factor signaling cascades (PI3K-mTOR) downstream of neuronal ligands
- GBM recurrence in deep brain structures with lower synaptic density but localized neuronal hyperactivity

**Evidence summary**
Active neurons promote GBM growth through secretion of the synaptic protein neuroligin-3 (NLGN3), which activates PI3K-mTOR signaling in tumor cells. NLGN3 expression in human GBM negatively correlates with patient survival. Multiple synaptic adhesion molecules (LRRC7, ALCAM, MDGA2) are involved in formation and maintenance of neuronal circuits and are likely repurposed by tumor cells to establish tumor-neuron contacts. SLIT1 and SEMA3E are axon guidance molecules that may control tumor cell migration relative to neuronal processes. This program is particularly significant in GBM because it explains the spatial patterning of tumor growth relative to neuronal density and the dependence of infiltrative GBM on neuronal stimulation.

**Atomic biological processes**
- Synaptic protein interactions. Genes: LRRC7, ALCAM, MDGA2, LRRC3B
  - [43]: NLGN3 secreted by active neurons promotes HGG proliferation; sufficient and necessary for mitogenic effect
  - [46]: NLGN3 levels higher in cortex; correlates with GBM recurrence in deep brain regions
- Axon guidance and neuronal repulsion. Genes: SLIT1, SEMA3E, KIF21B
  - [33]: Slit proteins (including SLIT1) inhibit leukocyte and potentially cancer cell migration through Robo receptors
  - [36]: Slit-Robo signaling pathway regulates nervous system development and cell migration
- Neuropeptide signaling. Genes: TACR1
  - [57]: TACR1 (tachykinin receptor) stimulates NF-kappaB activation and proinflammatory gene expression
  - [60]: Tachykinins and their receptors contribute to physiological control and disease mechanisms

**Atomic cellular components**
- Perineuronal extracellular matrix. Genes: TNR
  - [51]: TNR (Tenascin-R) endocytosed and recycled near synapses, activity-dependent cycling
  - [54]: ECM protein recycling critical for maintaining synaptic function

**Required genes (not in input)**
- Genes: NLGN1, NLGN3, NRXN1, NRXN2, NRXN3, ROBO1, ROBO2
  - [43]: NLGN3 is primary mitogen; neuroligins interact with neurexins
  - [33]: ROBO1 and ROBO2 are receptors for Slit-mediated migration inhibition

**Program citations**
- [1]: Spatial transcriptomics reveals increased synaptic gene expression in infiltrated regions
- [5]: Peritumoral GBM cells colocalize with neurons; increased synaptic activity and NOTCH signaling
- [43]: Definitive demonstration that active neurons promote HGG proliferation through NLGN3 secretion
- [46]: NLGN3 correlates with GBM recurrence patterns; higher in cortex than deep brain in normal state
- [4]: NLGN-NRXN interactions identified as potential therapeutic targets in glioma

## Program: Ion homeostasis and osmotic cell volume regulation
GBM cells rely on ion channels and water transporters to regulate intracellular osmolarity and cell volume during migration through confined brain parenchyma and at leading edge of invasion. This program includes aquaporins (AQP4), cation channels (ANO3, ANO4, TRPC4, CACNA1E), anion channels, and ion exchangers (SLC8A3, SLC5A4, SLC26A7). Proper ion homeostasis is essential for lamellipodial dynamics, cell shape changes, and migration through narrow extracellular spaces.

**Predicted impacts**
- Enhanced cell volume changes enabling invasion through narrow extracellular spaces
- Rapid osmotic adjustment at tumor cell leading edge during migration
- Dysregulated calcium signaling supporting proliferation and migration
- Contribution to GBM-associated cerebral edema through altered water transport
- Reduced migratory capacity if ion channel function is impaired
- Calcium dysregulation potentially driving metabolic reprogramming

**Evidence summary**
AQP4 is the water channel with highest flux capacity in brain and is strongly upregulated and redistributed across GBM cell surfaces. Multiple studies demonstrate that AQP4 localizes to lamellipodia and is required for efficient cell migration through narrow spaces. Ion channels are essential for osmotic balance during cell volume changes that accompany migration and invasion. ANO3 and ANO4 are calcium-activated channels; dysregulation of calcium signaling through these channels contributes to abnormal proliferation and migration. The program is critical for GBM because cell migration through dense brain tissue requires precise osmotic control and ion homeostasis.

**Atomic biological processes**
- Water channel-mediated osmotic water transport. Genes: AQP4
  - [55]: AQP4 upregulated in GBM; involved in edema formation and cell migration
  - [58]: AQP4 localizes to lamellipodia; facilitates water influx during cell migration
- Calcium-dependent channel activity. Genes: ANO3, ANO4, CACNA1E, TRPC4
  - [9]: ANO3 mutations disrupt calcium-dependent signaling; calcium pool abnormalities
  - [12]: ANO4 functions as Ca2+-dependent non-selective cation channel
- Ion exchange and transport. Genes: SLC8A3, SLC5A4, SLC26A7
  - [58]: KCl-water extrusion at lamellipodia enhances cell invasion; involves chloride and potassium channels

**Atomic cellular components**
- Leading edge membrane dynamics. Genes: AQP4, ANO3, ANO4
  - [58]: AQP4 polarizes to lamellipodia; increases number and size of lamellipodia in migrating cells

**Required genes (not in input)**
- Genes: KCNC1, KCNC2, CLCN3, CLCN7, CLC2, KCC1
  - [58]: Ion channels and chloride transporters essential for osmotic gradient that drives water movement

**Program citations**
- [55]: AQP4 loss in astrocytes alters GBM edema formation and immune microenvironment
- [58]: Comprehensive review of AQP4 roles in glioma migration and invasion
- [9]: ANO3 mutations demonstrate importance of calcium-dependent channel function
- [12]: ANO4 molecular characterization as calcium-activated cation channel

## Program: Cell cycle progression and proliferation
Cell cycle regulation in GBM is controlled by cyclin-CDK complexes, with cyclin D1 (CCND1) being a proto-oncogene frequently dysregulated in GBM. CCND1 drives progression from G1 to S phase by phosphorylating retinoblastoma protein (pRb). CDCA7L (cell division cycle-associated 7 like) is a c-MYC target that promotes proliferation by upregulating CCND1. Elevated cyclin D1 is associated with poor prognosis, enhanced invasiveness, and reduced apoptosis in GBM.

**Predicted impacts**
- Accelerated progression through G1/S checkpoint in GBM cells
- Enhanced proliferative capacity and increased tumor growth rate
- Increased drug resistance through upregulation of multidrug resistance proteins
- Reduced apoptotic sensitivity to pro-death signals
- Contribution to poor clinical prognosis and shorter survival

**Evidence summary**
CCND1 (cyclin D1) is one of the most frequently dysregulated genes in GBM. Cyclin D1 drives cell cycle progression by forming active complexes with CDK4/6 that phosphorylate pRb, releasing E2F transcription factors. High CCND1 expression correlates with poor prognosis and is associated with enhanced invasiveness and resistance to apoptosis. CDCA7L is a MYC-regulated target that promotes proliferation through CCND1 upregulation. The program is relevant to GBM because GBM cells exhibit constitutive hyperproliferation even in non-permissive microenvironments.

**Atomic biological processes**
- G1/S phase transition. Genes: CCND1
  - [37]: Cyclin D1 knockdown inhibits proliferation, induces apoptosis, attenuates invasion of GBM cells
  - [40]: CDCA7L targets CCND1; knockdown arrests cells at G0/G1 phase
- Proliferation regulation. Genes: CDCA7L
  - [40]: CDCA7L is c-MYC target gene; promotes proliferation through CCND1 regulation
- Apoptosis resistance. Genes: CCND1
  - [37]: Cyclin D1 overexpression increases MDR1 and Bcl-2 expression while decreasing caspase-3

**Required genes (not in input)**
- Genes: CDK4, CDK6, RB1, E2F1, MYC, p21, p27
  - [40]: CCND1 functions through CDK4/6 to phosphorylate Rb and drive proliferation

**Program citations**
- [37]: Comprehensive study of cyclin D1 function in GBM proliferation, apoptosis, and invasion
- [40]: CDCA7L-CCND1 axis demonstrated in GBM; knockdown inhibits proliferation

## Program: Extracellular matrix remodeling and vasculature assembly
The GBM tumor microenvironment is characterized by extensive extracellular matrix (ECM) remodeling and abnormal vasculature. Collagen types I, IV, and XX are abundant in GBM and contribute to tumor stiffness, invasion, and vascular abnormalities. This program includes fibrillar collagens (COL4A3, COL4A4, COL20A1), basement membrane components (LAMB4), ECM glycoproteins (TNR, THSD4), and ECM remodeling enzymes (ADAMTS17, HS6ST2). ECM composition and organization influence cell migration, vascular permeability, and therapeutic resistance.

**Predicted impacts**
- Increased tumor microenvironmental stiffness promoting invasive phenotype
- Enhanced vascular permeability and edema formation
- Creation of hypoxic niches through altered ECM organization and vascular abnormalities
- Promotion of mesenchymal GBM state in regions with elevated collagen
- Reduced drug penetration due to ECM barrier function
- Enhanced cell migration through ECM-rich regions

**Evidence summary**
Type IV collagen (COL4A) expression is markedly increased in GBM compared to normal brain and correlates with grade and malignancy. Multiple spatial transcriptomics and bulk sequencing studies show collagen clustering associated with distinct tumor phenotypes and genetic alterations. TNR is an ECM glycoprotein enriched in perineuronal nets and perisynaptic ECM that undergoes activity-dependent recycling. ADAMTS17 and HS6ST2 participate in ECM remodeling. The program is highly relevant to GBM because ECM composition is a critical determinant of tumor fate, influencing both cell phenotype and therapeutic response.

**Atomic biological processes**
- Type IV collagen biosynthesis and basement membrane assembly. Genes: COL4A3, COL4A4
  - [19]: Collagen type IV is major basement membrane component; distribution changes with glioma grade
  - [22]: COL4A1-2 expression increases with glioma progression; marks high-grade tumors
- Fibrillar collagen deposition. Genes: COL20A1
  - [19]: Collagen clustering identifies distinct tumor microenvironments associated with genetic features
- ECM glycoprotein organization. Genes: TNR
  - [51]: TNR endocytosed and recycled near synapses in activity-dependent manner; essential for neuronal function
- ECM proteolysis and remodeling. Genes: ADAMTS17, HS6ST2
  - [19]: ADAMTS proteases remodel ECM; associated with tumor progression

**Atomic cellular components**
- Basement membrane. Genes: COL4A3, COL4A4, LAMB4
  - [22]: Type IV collagen primary component of basement membrane; critical for BBB function in normal brain
- Vascular matrix. Genes: COL20A1, TNR
  - [1]: MGP and TIMP1 expressed in microvascular proliferation areas; associated with mesenchymal state

**Required genes (not in input)**
- Genes: COL4A1, COL4A2, COL1A1, COL1A2, TIMP1, MMP2, MMP9
  - [22]: COL4A1-2 are major collagen IV components; TIMP1 is key ECM regulator

**Program citations**
- [1]: Spatial transcriptomics identifies collagen-related genes in tumor core and MVP regions
- [19]: Large-scale analysis showing collagens predict genetic features and patient outcomes
- [22]: COL4A family analysis reveals prognostic significance in GBM and LGG
- [51]: Tenascin-R ECM protein recycling mechanism maintains synaptic function

## Program: Integrin-mediated cell adhesion and migration
Cell migration and invasion in GBM are fundamentally dependent on integrin-ECM interactions that link the extracellular matrix to the actin cytoskeleton. Integrins like ITGA9 (α9β1 heterodimer) interact with ECM components including thrombospondin, fibronectin, and VEGF isoforms. FERMT1 (fermitin family homolog 1, also called kindlin-1) is a FERM-domain protein that binds integrin cytoplasmic tails and cooperates with talin to activate integrins. This program coordinates cell adhesion dynamics with cell-matrix signaling to enable migration.

**Predicted impacts**
- Enhanced cell-matrix adhesion enabling stable interactions with ECM during migration
- Increased integrin signaling (β1/β3) promoting proliferation and survival
- Rapid adhesion turnover allowing efficient migration through tissue
- Sustained migratory phenotype through integrin-dependent signaling
- Modulation of cell morphology and actin dynamics at leading edge

**Evidence summary**
Integrin α9β1 is known to regulate cell migration and is involved in angiogenesis and lymphangiogenesis. FERMT1 (kindlin-1) is a critical regulator of integrin activation that binds to integrin cytoplasmic tails and cooperates with talin. Loss of FERMT1 results in reduced integrin activation and impaired cell adhesion and migration. In GBM context, integrin-ECM interactions are essential for tumor cell migration through brain parenchyma and invasion into surrounding tissue.

**Atomic biological processes**
- Integrin activation and adhesion. Genes: FERMT1, ITGA9
  - [8]: FERMT1 (kindlin-1) binds integrin β1 and β3 cytoplasmic tails; contributes to integrin activation
  - [11]: FERMT1 involved in cell adhesion; contributes to integrin activation when coexpressed with talin
- Cell-matrix interaction signaling. Genes: ITGA9
  - [50]: ITGA9 facilitates accelerated cell migration; regulates angiogenesis, lymphangiogenesis, and cancer cell proliferation
- Focal adhesion dynamics. Genes: FERMT1
  - [8]: FERMT1 colocalizes with vinculin and paxillin at focal adhesions in keratinocytes

**Atomic cellular components**
- Focal adhesions. Genes: FERMT1, ITGA9
  - [8]: FERMT1 associates with focal adhesion proteins; loss causes disrupted adhesion and migration

**Required genes (not in input)**
- Genes: TALIN1, TALIN2, PARVIN, FAK, SRC, ACTN
  - [8]: FERMT1 cooperates with talin to activate integrins; FAK and SRC are downstream integrin signaling kinases

**Program citations**
- [8]: FERMT1 loss-of-function causes integrin dysfunction and migration defects
- [50]: ITGA9 epigenetic silencing in breast cancer; hypermethylation reduces expression
- [51]: Integrins critical for ECM remodeling and neuronal function

## Program: Lipid metabolism and myelin-derived nutrient scavenging
GBM, particularly mesenchymal-like (MES) GBM cells, exhibit altered lipid metabolism that enables them to utilize myelin-derived lipids from the tumor microenvironment. Lipid-laden macrophages (LLMs) internalize myelin debris and transfer cholesterol and fatty acids to GBM cells through metabolic symbiosis. This program involves lipid biosynthetic enzymes (PLA2G4A, PLPP4, PLAAT1, DGKB, FA2H) that remodel lipids for membrane synthesis and metabolic signaling. The liver X receptor (LXR) pathway activates macrophage myelin uptake, creating a tumor-macrophage metabolic axis.

**Predicted impacts**
- Enhanced membrane biosynthesis supporting rapid proliferation
- Utilization of exogenous myelin lipids reducing dependence on de novo lipogenesis
- Altered signaling lipid composition modulating proliferation and survival pathways
- Metabolic symbiosis between MES-like GBM cells and lipid-laden macrophages
- Reduced oxidative stress through lipid remodeling
- Enhanced mesenchymal phenotype and invasiveness

**Evidence summary**
Recent studies identify a remarkable metabolic symbiosis between glioblastoma cells and tumor-associated macrophages. Lipid-laden macrophages (LLMs), enriched with GPNMB expression, preferentially interact with mesenchymal-like (MES) GBM cells. LLMs are epigenetically rewired to internalize myelin debris through LXR pathway activation. The myelin-derived cholesterol is transferred to GBM cells where it is incorporated into phospholipids for membrane synthesis, fueling mesenchymal GBM progression. This program represents a critical metabolic adaptation that explains how GBM cells sustain rapid proliferation in lipid-rich but nutrient-poor brain microenvironment.

**Atomic biological processes**
- Phospholipid metabolism and remodeling. Genes: PLA2G4A, PLPP4, PLAAT1, DGKB
  - [3]: LLMs transfer lipids (cholesterol, phospholipids) from myelin to MES-like GBM cells in LXR/ABCA1-dependent manner
- Fatty acid and sphingolipid metabolism. Genes: FA2H, UGT8
  - [3]: Myelin recycling pathway: LLMs phagocytose myelin, accumulate lipids as droplets; transfer to GBM cells

**Required genes (not in input)**
- Genes: LXR, ABCA1, GPNMB, SREBP, FASN, ACC
  - [3]: LXR activation is key upstream regulator of LLM lipid uptake; ABCA1 transfers lipids

**Program citations**
- [3]: Comprehensive study of lipid-laden macrophages, myelin recycling, and tumor-macrophage metabolic symbiosis

## Program: Growth factor receptor signaling networks
GBM cells exhibit dysregulation of multiple growth factor receptor pathways including EGFR, FGF receptors, and ErbB receptors that drive proliferation, survival, and migration. FGF12 is an intracellular FGF homologous factor (FHF) that modulates intracellular signaling. ERBB3 (HER3) is a neuregulin receptor that heterodimerizes with other ErbB family members to activate PI3K-AKT-mTOR and MAPK pathways. VIPR2 is a G-protein coupled receptor for vasoactive intestinal peptide (VIP) that activates cAMP signaling. These receptors converge on mTOR, AKT, and ERK pathways to promote tumor cell proliferation.

**Predicted impacts**
- Enhanced PI3K-AKT-mTOR signaling promoting anabolic metabolism and proliferation
- Sustained MAPK-ERK activation driving proliferation and survival
- Increased genomic instability through aberrant growth factor signaling
- Cross-talk between multiple growth factor pathways creating redundancy and therapeutic resistance
- Amplification of early response genes and cell cycle progression

**Evidence summary**
Growth factor receptor dysregulation is a hallmark of GBM. ERBB3 (HER3) is expressed in a subset of CD133+ putative cancer stem cells and represents a potential therapeutic target. ErbB receptors signal through multiple pathways including PI3K-AKT and MAPK-ERK to promote proliferation and survival. FGF signaling is involved in neural development and can be dysregulated in GBM. VIPR2 (VIP receptor) and CALCRL couple to G proteins to activate cAMP signaling. The convergence of multiple growth factor pathways on common downstream effectors (mTOR, AKT, ERK) creates pathway redundancy that contributes to therapeutic resistance.

**Atomic biological processes**
- ErbB receptor heterodimerization and activation. Genes: ERBB3
  - [32]: ERBB3 expressed in CD133+ putative cancer stem cells; potential novel therapeutic target
  - [35]: Neuregulin (NRG1)-ErbB signaling regulates myelination and neural development
- FGF signaling and pathway activation. Genes: FGF12
  - [39]: FGF signaling regulates cell proliferation, differentiation, and migration in CNS development
  - [42]: FGF/FGFR signaling dysregulation implicated in cancer progression
- G-protein coupled receptor signaling. Genes: VIPR2, CALCRL
  - [23]: CALCRL (CGRP receptor) signaling involves G-protein coupling and cAMP activation

**Required genes (not in input)**
- Genes: EGFR, FGFR1, FGFR2, FGFR3, NRG1, NRG2, VIP
  - [32]: EGFR amplified in ~40% of GBM; ErbB family shows heterodimerization
  - [42]: FGF ligands bind FGFRs; HSPGs serve as cofactors

**Program citations**
- [32]: ERBB3 expression in CD133+ cancer stem cells; distinct from EGFR distribution
- [35]: Neuregulin-ERBB signaling in nervous system development and myelination
- [39]: FGF signaling in CNS development and organogenesis
- [42]: FGF/FGFR pathway in organ development and disease including cancer

## Program: Lin28-let-7 axis regulating stemness and differentiation
The Lin28-let-7 pathway is a conserved heterochronic regulatory axis that controls the balance between self-renewal and differentiation in stem cells and cancer. LIN28B is an RNA-binding protein that blocks biogenesis of the tumor-suppressive let-7 microRNA family by recruiting Terminal Uridylyl Transferase (ZCCHC11) that polyuridylates and marks pre-let-7 for degradation. By repressing let-7, LIN28B maintains expression of oncogenes including MYC, HMGA2, RAS, and pluripotency factors. This program is particularly relevant in GBM where stemness is associated with treatment resistance and recurrence.

**Predicted impacts**
- Enhanced and sustained expression of oncogenic transcription factors (MYC, HMGA2)
- Maintenance of stemness and resistance to differentiation signals
- Increased chemotherapy and radiation resistance
- Promotion of epithelial-mesenchymal transition (EMT) phenotype
- Enhanced tumor-initiating cell (TIC) properties
- Increased metabolic plasticity enabling adaptation to microenvironmental changes

**Evidence summary**
The Lin28-let-7 axis is a fundamental regulator of stemness in both normal development and cancer. LIN28B is frequently upregulated in cancers and is associated with poor prognosis. LIN28B represses let-7 family miRNAs, allowing derepression of oncogenic targets including MYC, HMGA2, and RAS. Let-7 is a tumor-suppressive miRNA that is downregulated in multiple cancer types. In GBM, LIN28B-mediated stemness maintenance is associated with therapeutic resistance and enhanced tumor-initiating capacity. The axis has been shown to regulate both stemness and metabolic reprogramming in cancer stem cells.

**Atomic biological processes**
- miRNA biogenesis inhibition and let-7 repression. Genes: LIN28B
  - [45]: Lin28 inhibits post-transcriptional maturation of let-7 by recruiting TUTase; blocks Dicer loading of pre-let-7
  - [48]: LIN28A/B repress all let-7 family members; coordinate downregulation of tumor suppressor miRNAs
- Oncogene maintenance through let-7 repression. Genes: LIN28B
  - [45]: Let-7 directly represses MYC, HMGA2, RAS, and other oncogenes; LIN28 maintains these via let-7 inhibition
  - [48]: LIN28A/B establish positive feedback with C-MYC; MYC upregulates LIN28 expression
- Stem cell self-renewal versus differentiation decision. Genes: LIN28B
  - [45]: Lin28 and let-7 form highly conserved axis that temporally regulates self-renewal and differentiation

**Required genes (not in input)**
- Genes: LIN28A, ZCCHC11, DICER, DROSHA, DGCR8, MYC, HMGA2, KRAS, LET7A, LET7B, LET7C, LET7D, LET7E, LET7F, LET7G, LET7I, LET7MIR
  - [45]: LIN28A/B both inhibit let-7 biogenesis; ZCCHC11 recruits polyuridylation; Dicer required for let-7 processing
  - [48]: Let-7 directly represses MYC, HMGA2, RAS, and other oncogenic targets

**Program citations**
- [45]: Comprehensive review of Lin28-let-7 axis in stem cell biology and cancer
- [48]: LIN28AB drives cancer stem cell maintenance; let-7 acts as barrier to stemness

## Program: Developmental transcriptional regulation and cell fate specification
GBM cells exhibit striking similarity to embryonic neural progenitor cells and recapitulate developmental gene regulatory networks. This program includes key developmental transcription factors (SOX6, EYA1) and regulatory complexes (EYA1-SIX1-BRG1 BAF) that specify cell fate during neural development. SOX6 is part of the SoxD family and promotes neural progenitor maintenance. EYA1 encodes a dual-function protein with both transcriptional activation and protein phosphatase activity; it interacts with SIX1 and chromatin remodeling complexes to specify sensory and neural cell fates. These factors enable developmental plasticity and undifferentiated phenotype in GBM cells.

**Predicted impacts**
- Maintenance of progenitor-like undifferentiated state in GBM cells
- Enhanced developmental plasticity enabling adaptation to microenvironmental cues
- Activation of neural differentiation programs that are repurposed for invasion
- Epigenetic encoding that mirrors developing neural tissue
- Sustained expression of stemness-related transcription factors

**Evidence summary**
GBM cells exhibit remarkable similarity to embryonic neural progenitor cells in their transcriptional architecture and epigenetic landscape. SOX6 maintains neural progenitor pools through positive feedback with SOX2 and prevents precocious differentiation. EYA1 functions as a dual-activity protein with intrinsic phosphatase activity and transcriptional activation capacity. EYA1 interacts with SIX1 and the BRG1-BAF chromatin remodeling complex to specify neural and sensory cell fates during development. Recent spatial transcriptomics shows that infiltrative GBM cells in peritumoral regions have epigenetic profiles and transcriptional programs that closely mirror developing OPCs, including increased NOTCH signaling, synaptic genes, and developmental transcription factors.

**Atomic biological processes**
- Neural progenitor cell maintenance. Genes: SOX6
  - [14]: Sox2 and Sox6 form positive feedback loop maintaining neural progenitor cell (NPC) pool
  - [17]: SOX5 and SOX6 prevent precocious specification and terminal differentiation of OPCs
- Cell fate specification through EYA1-SIX1-BAF complex. Genes: EYA1
  - [31]: EYA1 and SIX1 interact with SWI/SNF BAF complex to induce transcriptional programs
  - [34]: EYA1-SIX1 complexes specify sensory and neuronal cell fates through chromatin remodeling
- Developmental plasticity and lineage commitment. Genes: SOX6, EYA1
  - [5]: Infiltrative GBM cells activate transcriptional programs associated with neurodevelopmental states

**Required genes (not in input)**
- Genes: SOX2, SIX1, SIX5, SMARCA4, BRG1, PAX6
  - [14]: SOX2 partners with SOX6 in feedback loop; essential for NPC maintenance
  - [34]: EYA1 works with SIX1 and chromatin remodeling complexes

**Program citations**
- [5]: Infiltrative GBM cells show epigenetic encoding of developing OPCs with increased invasivity and synaptic activity
- [14]: Sox2-Sox6 positive feedback essential for NPC maintenance
- [17]: SoxD proteins (Sox5, Sox6) regulate OPC development and migration
- [31]: EYA1-SIX1 complex in sensory development and organogenesis
- [34]: EYA1 roles in development spanning eye, ear, kidney, and nervous system

## Bibliography
1. Dylan SLH, Vilde P, Nicolai SB, Ane YS, Tobias OS, Aušrinė A, et al.. Glioblastoma cells increase expression of notch signaling and synaptic genes within infiltrated brain tissue.. Nature communications [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11385527/
2. Myers BL, Brayer KJ, Paez-Beltran LE, Villicana E, Keith MS, Suzuki H, et al.. Transcription factors ASCL1 and OLIG2 drive glioblastoma initiation and co-regulate tumor cell types and migration. Nature Communications [Internet]. 2024Nov28;15(1). Available from: https://www.nature.com/articles/s41467-024-54750-9
3. Lizhi P, Fei Z, Peiwen C. Lipid-Laden Macrophages Recycle Myelin to Feed Glioblastoma.. Cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12165008/
4. Nomura M, Spitzer A, Johnson KC, Garofano L, Nehar-belaid D, Galili DN, et al.. The multilayered transcriptional architecture of glioblastoma ecosystems. Nature Genetics [Internet]. 2025May;57(5). Available from: https://www.nature.com/articles/s41588-025-02167-5
5. Yiyan W, Benson ZW, Yosef E, Joan BYK, Pengcheng Y, Xuyao L, et al.. Neurodevelopmental hijacking of oligodendrocyte lineage programs drives glioblastoma infiltration.. Developmental cell [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40381621/
6. Clements M, Tang W, Florjanic BZ, Simpson RH, Oria R, Volteras D, et al.. Axonal injury is a targetable driver of glioblastoma progression. Nature [Internet]. 2025Aug20;646(8084). Available from: https://www.nature.com/articles/s41586-025-09411-2
7. Shin J-B, Gillespie PG. Unraveling cadherin 23's role in development and mechanotransduction. Proceedings of the National Academy of Sciences [Internet]. 2009Mar31;106(13). Available from: https://www.pnas.org/doi/10.1073/pnas.0902008106
8. Joey EL-C, Maddy P, Akio T, Siegfried U, Andrew PS, Sethuraman G, et al.. Loss-of-function FERMT1 mutations in kindler syndrome implicate a role for fermitin family homolog-1 in integrin activation.. The American journal of pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2751540/
9. Gavin C, Vincent P, Kira MH, Jose B, Una-Marie S, Elisavet P, et al.. Mutations in ANO3 cause dominant craniocervical dystonia: ion channel implicated in pathogenesis.. American journal of human genetics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3516598/
10. Andrea L, Piotr K, Yoshiyuki K, Ulrich M, Jeffrey RH. Development and regeneration of sensory transduction in auditory hair cells requires functional interaction between cadherin-23 and protocadherin-15.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2949085/
11. Available from: https://www.uniprot.org/uniprotkb/Q9BQL6/entry
12. Reichhart N, Schöberl S, Keckeis S, Alfaar AS, Roubeix C, Cordes M, et al.. Anoctamin-4 is a bona fide Ca2+-dependent non-selective cation channel. Scientific Reports [Internet]. 2019Feb19;9(1). Available from: https://www.nature.com/articles/s41598-018-37287-y
13. Riccardo B, Angela B. Role of Notch Signaling Pathway in Glioblastoma Pathogenesis.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
14. Lee KE, Seo J, Shin J, Ji EH, Roh J, Kim JY, et al.. Positive feedback loop between
            <i>Sox2</i>
            and
            <i>Sox6</i>
            inhibits neuronal differentiation in the developing central nervous system. Proceedings of the National Academy of Sciences [Internet]. 2014Feb5;111(7). Available from: https://www.pnas.org/doi/10.1073/pnas.1308758111
15. Zhang K, Chen S, Yang Q, Guo S, Chen Q, Liu Z, et al.. The Oligodendrocyte Transcription Factor 2 OLIG2 regulates transcriptional repression during myelinogenesis in rodents. Nature Communications [Internet]. 2022Mar17;13(1). Available from: https://www.nature.com/articles/s41467-022-29068-z
16. Harwood DSL, Pedersen V, Bager NS, Schmidt AY, Stannius TO, Areškevičiūtė A, et al.. Glioblastoma cells increase expression of notch signaling and synaptic genes within infiltrated brain tissue. Nature Communications [Internet]. 2024Sep9;15(1). Available from: https://www.nature.com/articles/s41467-024-52167-y
17. Tina B, Yvonne Z, Anja S, Lina L, Petra L, Michael W, et al.. Transcription factors Sox5 and Sox6 exert direct and indirect influences on oligodendroglial migration in spinal cord and forebrain.. Glia [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/26345464/
18. Available from: https://www.ncbi.nlm.nih.gov/gene/10215
19. Guo KS, Brodsky AS. Tumor collagens predict genetic features and patient outcomes. npj Genomic Medicine [Internet]. 2023Jul6;8(1). Available from: https://www.nature.com/articles/s41525-023-00358-9
20. Salvador S, Sara MH, Doan O, Mikhail GD, M ID, Javier G-M. Upregulation of the neuropeptide receptor calcitonin receptor-like in the spinal cord via MLL2 in a mouse model of paclitaxel-induced peripheral neuropathy.. Molecular pain [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11795615/
21. Lu C, Dong L, Zhou H, Li Q, Huang G, Bai S jun, et al.. G-Protein-Coupled Receptor Gpr17 Regulates Oligodendrocyte Differentiation in Response to Lysolecithin-Induced Demyelination. Scientific Reports [Internet]. 2018Mar14;8(1). Available from: https://www.nature.com/articles/s41598-018-22452-0
22. Aijun L, Jiankun Z, Na T, Liping W, Ying L, Zefeng T, et al.. Prognostic significance and multivariate modeling of COL4A family genes and HMGA2 in glioma.. Frontiers in pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12062008/
23. Davis RB, Ding S, Nielsen NR, Pawlak JB, Blakeney ES, Caron KM. Calcitonin-Receptor-Like Receptor Signaling Governs Intestinal Lymphatic Innervation and Lipid Uptake. ACS Pharmacology &amp; Translational Science [Internet]. 2019Jan29;2(2). Available from: https://pubs.acs.org/doi/10.1021/acsptsci.8b00061
24. Ying C, Heng W, Shuzong W, Hisami K, Jianrong L, Feng Y, et al.. The oligodendrocyte-specific G protein-coupled receptor GPR17 is a cell-intrinsic timer of myelination.. Nature neuroscience [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/19838178/
25. Hao H, Fang Z, Shiyou Z, Mengsheng Q. MYRF: A Mysterious Membrane-Bound Transcription Factor Involved in Myelin Development and Human Diseases.. Neuroscience bulletin [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8192642/
26. Breitenbucher A, Welsh C, Robers M. Spinal Glioblastoma Mimicking Myelin Oligodendrocyte Glycoprotein Antibody Disease Transverse Myelitis (P13-5.021). Neurology [Internet]. 2023Apr25;100(17_supplement_2). Available from: https://www.neurology.org/doi/10.1212/WNL.0000000000201978
27. Available from: https://maayanlab.cloud/Harmonizome/gene/UGT8
28. Available from: https://en.wikipedia.org/wiki/Myelin_regulatory_factor
29. Moein A, MaryAnn M, David P, Eoin PF, Richard P, Amy K. Myelin oligodendrocyte glycoprotein (MOG) antibodies in a patient with glioblastoma: Red flags for false positivity.. Journal of neuroimmunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34695769/
30. Available from: https://www.nature.com/articles/6605750
31. Pin-Xian X. The EYA-SO/SIX complex in development and disease.. Pediatric nephrology (Berlin, Germany) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6592036/
32. Véronique D-T, Ivan B, Sophie V, Anne L, Claude-Alain M, Francis C, et al.. Differential distribution of erbB receptors in human glioblastoma multiforme: expression of erbB3 in CD133-positive putative cancer stem cells.. Journal of neuropathology and experimental neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3173752/
33. J YW, L F, H TP, N H, L W, H T, et al.. The neuronal repellent Slit inhibits leukocyte chemotaxis induced by chemotactic factors.. Nature [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2072862/
34. Available from: https://portlandpress.com/biochemsoctrans/article/49/3/1397/229138/The-Eyes-Absent-proteins-in-development-and-in
35. Lin M, Klaus-Armin N. Neuregulin-ERBB signaling in the nervous system and neuropsychiatric diseases.. Neuron [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4189115/
36. Sanhueza N, Avilés EC, Oliva C. The Slit–Robo signalling pathway in nervous system development: a comparative perspective from vertebrates and invertebrates. Open Biology [Internet]. 2025Jul;15(7). Available from: https://royalsocietypublishing.org/doi/10.1098/rsob.250026
37. Junyu W, Qi W, Yong C, Zhen YL, Wei Z, Chun LW, et al.. Knockdown of cyclin D1 inhibits proliferation, induces apoptosis, and attenuates the invasive capacity of human glioblastoma cells.. Journal of neuro-oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/21912938/
38. S MW, P TT, S BO, S EG, S V, D R, et al.. The status of voltage-dependent calcium channels in alpha 1E knock-out mice.. The Journal of neuroscience : the official journal of the Society for Neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6773068/
39. David MO, Nobuyuki I. The Fibroblast Growth Factor signaling pathway.. Wiley interdisciplinary reviews Developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4393358/
40. Ji Q, Ma J-W, Liu R, Li X, Shen F, Huang L, et al.. CDCA7L promotes glioma proliferation by targeting CCND1 and predicts an unfavorable prognosis. Molecular Medicine Reports [Internet]. 2019Jun5;. Available from: https://www.spandidos-publications.com/10.3892/mmr.2019.10349
41. Carvill GL. Calcium Channel Dysfunction in Epilepsy: Gain of <i>CACNA1E</i>. Epilepsy Currents [Internet]. 2019May;19(3). Available from: https://journals.sagepub.com/doi/abs/10.1177/1535759719845324
42. Xie Y, Su N, Yang J, Tan Q, Huang S, Jin M, et al.. FGF/FGFR signaling in health and disease. Signal Transduction and Targeted Therapy [Internet]. 2020Sep2;5(1). Available from: https://www.nature.com/articles/s41392-020-00222-7
43. Humsa SV, Tessa BJ, Viola C, Alyssa N, Yujie T, Surya N, et al.. Neuronal Activity Promotes Glioma Growth through Neuroligin-3 Secretion.. Cell [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4447122/
44. Available from: https://genesdev.cshlp.org/content/suppl/2006/04/17/gad.381706.DC1/BrackenSuppTable3.pdf
45. Liem HN, Hao Z. Lin28 and let-7 in cell metabolism and cancer.. Translational pediatrics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4729067/
46. Liu R, Qin X, Zhuang Y, Zhang Y, Liao H, Tang J, et al.. Glioblastoma recurrence correlates with <scp>NLGN</scp>3 levels. Cancer Medicine [Internet]. 2018May18;7(7). Available from: https://onlinelibrary.wiley.com/doi/full/10.1002/cam4.1538
47. Available from: https://www.kegg.jp/kegg-bin/get_htext?htext=ko00001.keg&query=myc
48. Balzeau J, Menezes MR, Cao S, Hagan JP. The LIN28/let-7 Pathway in Cancer. Frontiers in Genetics [Internet]. 2017Mar28;8. Available from: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2017.00031/full
49. Available from: https://en.wikipedia.org/wiki/Myelin_oligodendrocyte_glycoprotein
50. Luydmila AM, Tatiana YP, Aleksandr GK, Dina L, Pavel VV, Valentina IR, et al.. Integrin alpha9 (ITGA9) expression and epigenetic silencing in human breast tumors.. Cell adhesion & migration [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3218606/
51. Dankovich TM, Kaushik R, Olsthoorn LHM, Petersen GC, Giro PE, Kluever V, et al.. Extracellular matrix remodeling through endocytosis and resurfacing of Tenascin-R. Nature Communications [Internet]. 2021Dec8;12(1). Available from: https://www.nature.com/articles/s41467-021-27462-7
52. N JS, S F, C L, B PM, A KC, D AC. Myelin-oligodendrocyte glycoprotein (MOG) is a surface marker of oligodendrocyte maturation.. Journal of neuroimmunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/2649509/
53. Mostovich LA, Prudnikova TY, Kondratov AG, Loginova D, Vavilov PV, Rykova VI, et al.. Integrin alpha9 (ITGA9) expression and epigenetic silencing in human breast tumors. Cell Adhesion &amp; Migration [Internet]. 2011Sep;5(5). Available from: https://www.tandfonline.com/doi/abs/10.4161/cam.5.5.17949
54. Tal MD, Rahul K, Linda HMO, Gabriel CP, Philipp EG, Verena K, et al.. Extracellular matrix remodeling through endocytosis and resurfacing of Tenascin-R.. Nature communications [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/34880248/
55. Available from: https://academic.oup.com/neuro-oncology/article/27/Supplement_5/v462/8319745
56. Caihong L, Dongkai C, Peng L. Androgen receptor dynamics in prostate cancer: from disease progression to treatment resistance.. Frontiers in oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11850250/
57. Ronald W, Xiaoyan Z, Gary WH. Tachykinin-1 receptor stimulates proinflammatory gene expression in lung epithelial cells through activation of NF-kappaB via a G(q)-dependent pathway.. American journal of physiology Lung cellular and molecular physiology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/17041011/
58. Yu-Long L, Xun W, Jia-Cheng L, Xiao-Chi M, Bo Z. The potential roles of aquaporin 4 in malignant gliomas.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5458289/
59. Michmerhuizen AR, Spratt DE, Pierce LJ, Speers CW. ARe we there yet? Understanding androgen receptor signaling in breast cancer. npj Breast Cancer [Internet]. 2020Sep25;6(1). Available from: https://www.nature.com/articles/s41523-020-00190-9
60. Martin SS, Bengt von M, Pierangelo G, Charalabos P, Nigel WB. Tachykinins and their receptors: contributions to physiological control and the mechanisms of disease.. Physiological reviews [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3929113/
