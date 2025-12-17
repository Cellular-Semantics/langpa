# Gene Program Markdown Report

## Context
- Cell type: Lymphocytes (CD8+ T cells, CD4+ T cells, NK cells, B cells)
- Disease: Astrocytoma
- Tissue: Brain, central nervous system

## Input Genes
ITGA4, GZMB, LCP1, LCK, KLRC1, JAML, ITK, ITGAL, AC004687.1, INPP5D, IL7R, IL2RG, IKZF3, IKZF1, GZMK, GZMH, GRAP2, LINC00426, GPR174, GNLY, GIMAP7, FYB1, FLI1, EMB, DOCK8, ... (200 total)

## Program: T Cell Receptor Signal Transduction
Complete molecular machinery for TCR recognition of cognate peptide-MHC complexes and initiation of downstream signaling cascades. TCR complex (CD3D, CD3E, CD3G, CD247, TRAC, TRBC1, TRBC2) directly recognizes antigen; Src family kinase LCK and Syk family kinase ZAP70 phosphorylate ITAM motifs and recruit downstream effectors including adaptor proteins and kinases. Signaling integrates through MAPK/ERK, PI3K/AKT, and NF-κB pathways. Signal termination mediated by phosphatases including PTPN22 and PTPN7. In astrocytoma context, TCR signaling intensity and duration determine T cell differentiation fate.

**Predicted impacts**
- Enhanced T cell recognition of tumor-associated antigens presented on MHC molecules
- Sustained proliferation and differentiation of tumor-specific T cell clones upon antigen encounter
- Integration of co-stimulatory and co-inhibitory signals determining T cell developmental fate
- Generation of both long-lived tumor-specific memory T cells and short-lived effector cells
- Activation of transcriptional programs encoding cytotoxic effector molecules and cytokines

**Evidence summary**
The complete TCR signaling cascade is essential for T cell activation and is extensively characterized in both physiological contexts and tumor microenvironments. LCK and ZAP70 represent critical early events in TCR signal initiation, with rapid kinase activation and trans-phosphorylation driving recruitment of downstream effectors. The presence of phosphatases including PTPN22 enables precise tuning of signal intensity, preventing excessive or insufficient immune activation. In astrocytoma microenvironments, integration of TCR signals with co-stimulatory signals and checkpoint molecules determines whether T cells mount productive anti-tumor responses or undergo functional exhaustion and apoptosis.

**Atomic biological processes**
- Antigen recognition and TCR engagement. Genes: CD3D, CD3E, CD3G, CD247, TRAC, TRBC1, TRBC2
  - [8]: CD3 complex structure and ITAM motifs
  - [11]: CD3 delta subunit role in TCR development and signal transduction
- Proximal kinase activation. Genes: LCK, ZAP70
  - [9]: LCK proto-oncogene Src family tyrosine kinase in T cell activation
  - [45]: ZAP70 T cell kinase role in lymphocyte activation
- Signal amplification through phospholipid metabolism. Genes: PIK3CG, PIK3CD, PIK3AP1, PIK3R5
  - [38]: PIK3CG phosphatidylinositol kinase in immune response
  - [40]: PIK3CA catalytic subunit role in cell signaling
- NF-κB pathway activation. Genes: CARD11, BCL10
  - [41]: BCL10 immune signaling adaptor in NF-kappaB activation
  - [44]: CARD11 caspase recruitment domain role in T-cell receptor signaling
- Signal termination and negative feedback. Genes: INPP5D, PTPN22, PTPN7, PTPN6
  - [54]: INPP5D phosphatase role in immune response regulation
  - [67]: PTPN6 protein tyrosine phosphatase in T cell regulation

**Atomic cellular components**
- T cell receptor complex. Genes: CD3D, CD3E, CD3G, CD247
  - [8]: CD3 gamma and delta subunits evolved to optimize TCR activation
  - [11]: CD3 delta subunit part of TCR/CD3 complex
- Src kinase family members. Genes: LCK
  - [9]: LCK proto-oncogene Src family tyrosine kinase
- Signalosome assembly components. Genes: ZAP70, CARD11, BCL10
  - [42]: ZAP70 kinase clustering-dependent signaling switch

**Program citations**
- [8]: CD3 complex and TCR structure
- [11]: CD3D in T cell development and signal transduction
- [30]: PD-1 axis maintaining stem-like CD8+ T cells with active TCR signaling
- [45]: ZAP70 T cell kinase role
- [62]: Guidelines for T cell nomenclature
- [63]: T cell differentiation antigens and cytotoxic function

## Program: Lymphocyte Trafficking and Extravasation
Comprehensive adhesion molecules, chemokine receptors, and accessory proteins enabling lymphocytes to exit secondary lymphoid organs, migrate through blood, cross the blood-brain barrier, and infiltrate astrocytoma parenchyma. Integrins including α4β1 (VLA-4, encoded by ITGA4 and ITGB1) and αLβ2 (LFA-1, encoded by ITGAL and ITGB2) mediate initial rolling and firm adhesion to endothelial cells expressing VCAM-1 and ICAM-1. Chemokine receptors including CXCR4 respond to chemokine gradients produced by tumor cells and stromal cells. This program is essential for transforming systemic anti-tumor immunity into local tumor-infiltrating lymphocyte responses.

**Predicted impacts**
- Efficient recruitment of tumor-specific T cells and NK cells into astrocytomas across the blood-brain barrier
- Positioning of immune cells in close anatomical proximity to tumor cells for surveillance and effector functions
- Formation of stable immunological synapses between lymphocytes and antigen-presenting cells in tumor microenvironment
- Continuous adaptation of lymphocyte trafficking responses to tumor-induced changes in chemokine and adhesion molecule expression
- Establishment of specialized niches within tumors supporting long-lived tumor-specific lymphocytes

**Evidence summary**
Integrins VLA-4 and LFA-1 are well-established as essential mediators of lymphocyte trafficking into peripheral tissues and into the central nervous system. These integrins are redundantly required for efficient T cell infiltration into brain tissues under inflammatory conditions. CXCR4 and its ligand CXCL12 are critical for both recruitment and retention of lymphocytes in specialized tissue microenvironments. Recent spatial transcriptomics studies have demonstrated that plasma cell retention in non-tumor tissue depends on VLA-4 and LFA-1 interactions with stromal fibroblasts expressing their ligands. LSP1 regulates endothelial PECAM-1 expression and facilitates lymphocyte transendothelial migration. In astrocytomas, this trafficking program determines the density and composition of tumor-infiltrating lymphocytes.

**Atomic biological processes**
- Integrin-mediated cell adhesion and extravasation. Genes: ITGA4, ITGAL, ITGA1
  - [1]: SIRPA signal regulatory protein alpha in cell adhesion
  - [10]: Integrin alpha 4 mediates cell adhesion and differentiation
- Chemokine receptor signaling and migration. Genes: CXCR4, RGS1
  - [7]: CXCL12 and integrin signaling in lymphocyte trafficking
- Immunoglobulin superfamily adhesion. Genes: CD2, CD48, CD6
  - [8]: CD3G and CD2 in lymphocyte interactions
- Lymphocyte-specific protein regulation of cell migration. Genes: LSP1
  - [47]: LSP1 regulates lymphocyte cell migration and adhesion
  - [49]: PECAM-1 expression relates to lymphocyte transendothelial migration

**Atomic cellular components**
- Integrin adhesion molecules. Genes: ITGA4, ITGAL, ITGA1
  - [1]: SIRPA integrin-related adhesion
- Chemokine receptor complexes. Genes: CXCR4
  - [7]: Chemokine receptor signaling in lymphocyte networks
- SLAM family immune synaptic molecules. Genes: CD48
  - [7]: SLAMF receptors in lymphocyte compartmentalization

**Program citations**
- [1]: SIRPA adhesion molecule
- [7]: Integrin and chemokine signaling in lymphocyte networks within secondary lymphoid organs and tissues
- [10]: Integrin alpha 4 cell adhesion
- [47]: LSP1 lymphocyte specific protein in cell migration
- [49]: PECAM-1 endothelial adhesion molecule in LSP1 deficiency

## Program: Cytotoxic Granule-Mediated Killing
Complete molecular machinery for perforin-granzyme-mediated direct killing of tumor cells by CD8+ T cells and NK cells. Granules containing multiple serine proteases (granzymes A, B, K, H), the pore-forming protein perforin, and cytotoxic lymphocyte-specific granule proteins are secreted and polarized onto target cell membranes following immune synapse formation. Perforin oligomerizes to create pores allowing granzyme entry into target cell cytoplasm. Intracellular granzymes cleave multiple pro-apoptotic substrates and cause caspase-independent programmed cell death. This represents the primary direct mechanism by which infiltrating CD8+ T cells and NK cells eliminate glioma cells.

**Predicted impacts**
- Direct cytotoxic killing of individual glioma cells engaged with immune cells at tumor-immune interface
- Elimination of tumor cells that have evaded other immune mechanisms including checkpoint-resistant cells
- Generation of tumor cell death signals triggering inflammatory cascades and danger-associated molecular pattern (DAMP) release
- Control of glioma growth rate through continuous cytotoxic assault on malignant cells
- Potential generation of cross-presented tumor antigens amplifying anti-tumor immune responses

**Evidence summary**
Perforin and granzymes are the primary effector molecules of cytotoxic T cell and NK cell killing, with extensive experimental evidence demonstrating their necessity for in vivo tumor control. Granzyme B is particularly abundant and strongly associated with CD8+ T cell terminal differentiation and effector function. Multiple granzymes provide substrate specialization and redundancy, ensuring robust killing even if individual proteases are inhibited. Perforin is absolutely required for efficient in vivo killing, and mutations in perforin cause familial hemophagocytic lymphohistiocytosis characterized by severe immunodeficiency. In high-grade gliomas, high expression of perforin and granzymes in tumor-infiltrating lymphocytes is associated with improved survival outcomes.

**Atomic biological processes**
- Granule priming and secretory pathway. Genes: PRF1, GZMA, GZMB, GZMK, GZMH, GNLY, CTSW
  - [14]: PRF1 perforin cytotoxic protein production
  - [16]: Gzmb granzyme B in cytotoxic T cell function
- Pore formation and membrane disruption. Genes: PRF1
  - [13]: GZMA granzyme A from cytolytic T lymphocytes
  - [14]: PRF1 perforin 1 in NK cell cytotoxicity
- Caspase-independent apoptosis induction. Genes: GZMA, GZMB, GZMK, GZMH
  - [51]: GZMB granzyme B induces apoptosis
  - [66]: GZMB cytotoxic CD8+ T cells promote adverse cardiac remodeling

**Atomic cellular components**
- Cytotoxic granules and secretory vesicles. Genes: GZMA, GZMB, GZMK, GZMH, PRF1, GNLY, CTSW
  - [13]: GZMA in cytolytic granules
  - [16]: Gzmb in granule secretory pathway
- Cytotoxic lymphocyte effector molecules. Genes: PRF1, NKG7
  - [14]: PRF1 pore-forming protein in cytotoxic lymphocytes

**Program citations**
- [13]: GZMA granzyme A cytolytic function
- [14]: PRF1 perforin 1 cytotoxicity
- [16]: Gzmb granzyme B in granule pathway
- [17]: Prf1 perforin pore-forming protein
- [51]: GZMB granzyme B in apoptosis
- [66]: GZMB in cytotoxic CD8 T cells

## Program: Natural Killer Cell Activation and Function
Comprehensive NK cell-specific receptors, adaptors, and effector molecules enabling recognition and killing of transformed cells through both activating receptor-ligand interactions and antibody-dependent cellular cytotoxicity. Natural killer group 2D (NKG2D, encoded by KLRK1) recognizes MHC class I-related chain molecules (MICA and MICB) that are frequently upregulated on transformed cells including gliomas. Inhibitory receptors including NKG2A (encoded by KLRC1, binding HLA-E) and other killer immunoglobulin-like receptors provide 'missing self' recognition. Balance between activation and inhibition determines whether NK cells mount productive anti-tumor responses or remain quiescent.

**Predicted impacts**
- Recognition of MHC class I-deficient and MICA/MICB-expressing glioma cells by NK cells
- Elimination of glioma cells that have downregulated MHC class I as an immune evasion mechanism
- Regulation of NK cell activation by tumor cell-derived ligands and stromal cell signals
- Prevention of NK-cell-mediated damage to healthy brain parenchyma through inhibitory receptor signaling
- Contribution to innate anti-tumor immunity preceding and complementing adaptive immune responses

**Evidence summary**
NKG2D is a major activating receptor for both NK cells and CD8+ T cells, recognizing stress-inducible ligands MICA and MICB that are frequently upregulated on tumors. Inhibitory NK receptors including NKG2A bind MHC-E and related molecules, providing negative regulation that prevents NK cell activation against healthy cells and preserving brain immune tolerance. NK cells with high expression of activating receptors and low expression of inhibitory receptors show enhanced anti-tumor activity in experimental models. In human gliomas, NK cell infiltration is variable and correlates with overall immune response potential and prognosis.

**Atomic biological processes**
- Activating receptor-ligand recognition. Genes: KLRK1, NCR1
  - [22]: KLRC1 killer cell lectin-like receptor in NK cell activity
  - [25]: PRDM1 and NK cell function and development
- Inhibitory receptor signaling. Genes: KLRC1, KLRC2, KLRC4
  - [22]: KLRC1 NKG2A inhibitory NK cell receptor
  - [56]: ETS1 NK cell terminal differentiation
- NK cell costimulatory interactions. Genes: CD244
  - [31]: CD244 2B4 NK cell costimulation

**Atomic cellular components**
- Activating killer cell receptors. Genes: KLRK1, NCR1, HCST
  - [22]: KLRC1 in killer cell lectin-like receptors
- Inhibitory killer cell receptors. Genes: KLRC1, KLRC2, KLRC4, KLRD1
  - [22]: KLRC1 KLRC2 inhibitory NK receptors

**Program citations**
- [22]: KLRC1 NK cell receptor
- [25]: PRDM1 regulatory roles in NK cell development and function
- [31]: CD244 2B4 NK cell function
- [56]: ETS1 transcription factor in NK cell development

## Program: Immune Checkpoint Regulation and T Cell Stemness
Comprehensive checkpoint molecules (PD-1, CTLA-4, TIGIT) and co-stimulatory molecules (ICOS, CD28) regulating T cell activation state and developmental trajectory. Recent evidence reveals that PD-1 (encoded by PDCD1), rather than universally driving exhaustion, maintains stem-like progenitor CD8+ T cells during active antigen presentation by attenuating strong TCR signaling that would drive terminal differentiation. High-PD-1 CD8+ T cells in tumor-draining lymph nodes retain TCF-1 expression, self-renewal capacity, and proliferative potential critical for tumor control. Checkpoint blockade drives these cells toward terminal differentiation or apoptosis, explaining both efficacy and limitations of checkpoint immunotherapy.

**Predicted impacts**
- Maintenance of tumor-specific stem-like CD8+ T cell progenitors during continuous tumor antigen exposure
- Attenuation of TCR signaling intensity to promote stemness over terminal differentiation and exhaustion
- Integration of co-stimulatory signals promoting T cell survival and sustained proliferation
- Coordination of T cell fate decisions with critical checkpoints determining response to checkpoint blockade immunotherapy
- Prevention of unwanted terminal differentiation and apoptosis of most functionally important tumor-specific cells

**Evidence summary**
PD-1 engagement by its ligands PD-L1 and PD-L2 suppresses TCR signaling through recruitment of the phosphatase SHP-2. Remarkably, recent high-resolution spatial analysis in tumor-draining lymph nodes revealed that the most PD-1-high stem-like CD8+ T cells are preferentially enriched in late antigen presentation niches with high TCR affinity and active antigen encounter. These cells maintain high expression of TCF-1, SLAMF6, and other stemness markers despite active TCR signaling. PD-1 blockade drives these cells toward terminal effector differentiation with increased granzyme expression but substantially decreased stemness marker expression. In astrocytoma patients, checkpoint blockade efficacy and acquired resistance correlate with pre-treatment maintenance of stem-like T cell populations.

**Atomic biological processes**
- Inhibitory checkpoint signaling. Genes: PDCD1
  - [30]: PDCD1 PD-1 maintains high-avidity stem-like CD8+ T cells
  - [32]: Pdcd1 programmed cell death 1 protects liver damage
- Co-stimulatory signaling. Genes: ICOS
  - [48]: ICOSL inducible T cell costimulator ligand
  - [50]: ICOS inducible T cell costimulator
- Stem cell-like marker expression and maintenance. Genes: SLAMF6
  - [15]: SLAMF6 marks stem-like progenitor CD8+ T cells

**Atomic cellular components**
- Checkpoint receptor complexes. Genes: PDCD1
  - [30]: PD-1 inhibitory receptor on T cells
- Co-stimulatory receptor complexes. Genes: ICOS
  - [50]: ICOS co-stimulatory receptor

**Program citations**
- [15]: Inhibitory PD-1 axis maintains high-avidity stem-like CD8+ cells
- [21]: Checkpoint blockade and cellular engineering approaches in cancer
- [30]: PD-1 checkpoint inhibition disrupts stem cell maintenance
- [32]: Pdcd1 PD-1 function

## Program: Transcriptional Control of Lymphocyte Differentiation
Master transcription factors determining lymphocyte lineage identity, differentiation state, and effector function capacity. RUNX3 is master regulator of CD8+ T cell identity, driving expression of cytotoxic molecules while repressing CD4 lineage genes. BATF functions as pioneer transcription factor opening chromatin at activation-associated enhancers during T cell differentiation toward effector states. ETS1 regulates NK cell terminal differentiation and cytotoxic potential. IKZF1 and IKZF3 control lymphocyte development and memory T cell formation. Together, these transcription factors orchestrate transcriptional programs transforming naive lymphocytes into activated effectors capable of eliminating tumor cells.

**Predicted impacts**
- Establishment and maintenance of CD8+ T cell identity in face of tumor microenvironment-induced plasticity
- Rapid upregulation of cytotoxic effector genes (granzymes, perforin, NKG7) upon tumor antigen encounter
- Opening of chromatin at activation-associated enhancers enabling rapid transcriptional responses to tumor signals
- Integration of developmental signals with tumor microenvironment cues determining immune response trajectory
- Prevention of inappropriate lineage switching or exhaustion during prolonged tumor antigen exposure

**Evidence summary**
RUNX3 is absolutely required for CD8+ T cell development and function, with RUNX3-deficient mice showing complete loss of mature CD8+ T cells despite intact thymic development. BATF functions as pioneer transcription factor, binding to initially closed chromatin regions and recruiting histone acetylases to establish active chromatin landscapes permissive for effector gene expression. ETS1 is essential for NK cell development, with conditional knockout in NK lineage cells resulting in severe NK cell deficiencies. IKZF1 is critical for early T cell development in thymus, while IKZF3 (Aiolos) functions in B cell development and has recently been identified as key regulator of memory T cell formation and survival.

**Atomic biological processes**
- CD8+ T cell lineage specification. Genes: RUNX3
  - [27]: Runx3 runt related transcription factor regulates CD8 T cell differentiation
- T cell activation and differentiation. Genes: BATF
  - [2]: Comprehensive characterization of epithelioid glioblastoma
  - [15]: BATF mediates epigenetic control of CD8 T cell differentiation
- NK cell terminal differentiation. Genes: ETS1
  - [56]: ETS1 transcription factor important in NK cell development and terminal differentiation
- Memory T cell formation and maintenance. Genes: IKZF1, IKZF3
  - [25]: IKZF3 important for memory T cell formation
  - [29]: IKZF1 transcription factor regulates B lymphocyte proliferation and differentiation

**Atomic cellular components**
- RUNX family transcription factors. Genes: RUNX3
  - [27]: Runx3 runt related transcription factor
- AP-1 family transcription factors. Genes: BATF
  - [15]: BATF basic leucine zipper AP-1 factor
- ETS family transcription factors. Genes: ETS1
  - [56]: ETS1 ETS proto-oncogene transcription factor

**Program citations**
- [25]: Key regulatory roles of PRDM1 in human NK cell development
- [27]: Runx3 runt related transcription factor
- [28]: Gata3 GATA binding protein T cell regulation
- [29]: IKZF1 IKAROS family zinc finger
- [56]: ETS1 transcription factor in NK cell development

## Program: Immune Synapse Assembly and Co-signaling
SLAM family receptors and other cell-cell adhesion molecules mediating formation of immune synapses between T cells and dendritic cells, T cells and B cells, and T cells with tumor cells. SLAMF6 marks stem-like CD8+ T progenitors and mediates signaling critical for maintenance of T cell stemness during active antigen presentation. SLAMF1 and SLAMF7 mediate lymphocyte-dendritic cell and T-B cell cooperation. CD244 (2B4) mediates NK cell co-stimulation through interaction with CD48 on target cells. CD2 binds CD58 on antigen-presenting cells. These interactions provide both adhesive forces maintaining cell-cell contact and bi-directional signaling regulating lymphocyte activation and differentiation.

**Predicted impacts**
- Formation of stable immune synapses enabling prolonged antigen recognition and sustained TCR signaling
- Bi-directional communication between immune cells coordinating multi-cellular anti-tumor responses
- Maintenance of stem-like T cell progenitors through SLAMF6-mediated signaling despite active TCR engagement
- Enhancement of NK cell killing through CD244-CD48 co-stimulatory interactions with tumor and stromal cells
- Facilitation of T-B cell cooperation generating both cellular and humoral anti-tumor immunity

**Evidence summary**
SLAMF6 has been recently identified as definitive marker of stem-like CD8+ T cells in tumor-draining lymph nodes, with high SLAMF6 expression strongly correlating with TCF-1 expression and proliferative capacity. SLAMF receptors function as switchable receptors capable of delivering either activating or inhibitory signals depending on co-receptor engagement and signaling context. CD244 (2B4) enhances NK cell killing through co-engagement with primary activating receptors on both tumor cells and NK cells. The SLAM family represents critical interface for lymphocyte-lymphocyte and lymphocyte-dendritic cell communication enabling coordinated immune responses.

**Atomic biological processes**
- SLAM receptor-mediated signaling. Genes: SLAMF1, SLAMF6, SLAMF7, CD244
  - [7]: Lymphocyte networks in secondary lymphoid organs
  - [15]: SLAMF6+ T SL cells uniquely localized to antigen-draining lymph node
- Immunoglobulin superfamily cell-cell adhesion. Genes: CD2, CD48, CD6
  - [1]: SIRPA signal regulatory protein
  - [8]: CD3G in T cell receptor complex

**Atomic cellular components**
- SLAM family receptor complexes. Genes: SLAMF1, SLAMF6, SLAMF7, CD244
  - [7]: SLAMF and lymphocyte networks
  - [31]: CD244 2B4 in NK cells
- Immune synapse scaffolding. Genes: CD2, CD48, CD6
  - [15]: Immune synapse formation with dendritic cells

**Program citations**
- [7]: Lymphocyte networks and SLAMF signaling
- [15]: SLAMF6 in stem-like CD8 T cell pools
- [30]: SLAMF6 and high-avidity stem-like CD8 cells
- [31]: CD244 2B4 costimulation
- [51]: CD244 in T cell killing

## Program: Phosphatidylinositol Signaling and Lipid Metabolism
Enzymes controlling phosphatidylinositol lipid metabolism serving as molecular platform for plasma membrane signaling complexes and organellar membrane dynamics. Class I and Class II PI3K isoforms (PIK3CG encoding Class IB p110γ, PIK3CD encoding Class IA p110δ) generate phosphatidylinositol-3,4,5-trisphosphate in response to TCR signaling and cytokine receptor engagement. INPP5D (SHIP-1) terminates PI3K signaling through dephosphorylation of this key lipid. These lipid species recruit pleckstrin homology domain-containing proteins including AKT and PDK1 to specific membrane regions, enabling kinase activation and downstream signaling. Dysregulation of this pathway is implicated in lymphocyte dysfunction and lymphoid malignancies.

**Predicted impacts**
- Enhanced PI3K/AKT signaling in response to TCR and cytokine receptor engagement
- Appropriate termination of PI3K signaling preventing excessive uncontrolled lymphocyte activation
- Generation of docking sites for signaling proteins including AKT, Btk, and phospholipase C-gamma
- Control of lymphocyte proliferation, survival, and differentiation through lipid-dependent mechanisms
- Integration of multiple signaling inputs through lipid platform assembly at membranes

**Evidence summary**
Class I PI3K generates PIP3 at plasma membrane and on endosomal membranes, recruiting proteins with pleckstrin homology domains including AKT and PDK1. INPP5D (SHIP-1) is essential for immune homeostasis, with SHIP-1-deficient mice showing severe autoimmunity and enhanced immune activation due to inability to terminate PI3K signaling. PI3K signaling is hyperactivated in certain T cell lymphomas and promotes lymphomagenesis and resistance to checkpoint blockade. In normal T cells, balance between PI3K activation and INPP5D-mediated termination determines magnitude and duration of proliferative signals.

**Atomic biological processes**
- Phosphatidylinositol 3-kinase signaling. Genes: PIK3CG, PIK3CD
  - [38]: PIK3CG phosphatidylinositol 3-kinase in immune response
  - [40]: PIK3CA catalytic subunit phosphorylates inositol lipids
- Phosphatidylinositol phosphatase signaling termination. Genes: INPP5D
  - [54]: INPP5D inositol polyphosphate phosphatase

**Atomic cellular components**
- PI3K catalytic subunits. Genes: PIK3CG, PIK3CD
  - [38]: PIK3CG Class I phosphoinositide 3-kinase
  - [40]: PIK3CA catalytic subunit
- PI3K regulatory subunits and adaptors. Genes: PIK3AP1, PIK3R5
  - [38]: PI3K regulatory subunits

**Program citations**
- [38]: PIK3CG in immune response
- [40]: PIK3CA phosphatidylinositol kinase
- [54]: INPP5D phosphatase in immune regulation

## Program: RhoGTPase Regulation and Actin Dynamics
Rho family GTPases and their regulators (GAPs, GEFs) controlling actin polymerization at immune synapse and during lymphocyte migration through tissue. RAC GTPases regulate assembly of dense actin scaffold at interface between lymphocytes and target cells, essential for stable immune synapse formation, efficient TCR signaling, and directed granule secretion. RHOH provides RAC-independent mechanisms of TCR signaling regulation. ARHGAP family proteins terminate RAC and RHO signaling through GTPase-activating function, providing negative feedback. Balance between RAC activation and ARHGAP-mediated termination determines immune synapse stability and duration.

**Predicted impacts**
- Rapid actin polymerization at immune synapses enabling stable lymphocyte-tumor cell contacts and TCR signaling
- Facilitation of granule polarization and directional secretion of cytotoxic mediators toward target cells
- Enhanced lymphocyte migration through dense brain tissue toward glioma cells
- Adaptation of actin dynamics to changing immune synapse formation requirements during prolonged activation
- Prevention of excessive actin dynamics that could disrupt synapse stability or cellular integrity

**Evidence summary**
RAC GTPases are essential for immune synapse formation and TCR signaling, with RAC-deficient T cells showing severe impairment in TCR-induced calcium flux and IL-2 production. RHOH regulates LAT complex assembly independent of RAC, providing redundancy in TCR signaling and ensuring robust responses to antigen. The ARHGAP family proteins provide negative feedback on Rho GTPase signaling, with dysregulation implicated in immunodeficiencies and autoimmune diseases. Actin dynamics are particularly important in central nervous system where lymphocytes must navigate through dense, highly structured brain parenchyma and maintain synapses on glioma cells.

**Atomic biological processes**
- Actin polymerization at immune synapse. Genes: RAC2, RHOH
  - [34]: RAC1 Rac family small GTPase in cell migration
  - [37]: Astrocyte activation and immune signaling pathways
- Lymphocyte migration through brain tissue. Genes: RAC2, ARHGAP15, ARHGAP25, ARHGAP30
  - [34]: RAC GTPase regulation of cell migration
- GTPase-activating protein signaling. Genes: ARHGAP15, ARHGAP25, ARHGAP30
  - [34]: RAC1 GTPase function

**Atomic cellular components**
- Rho family GTPases. Genes: RAC2, RHOH
  - [34]: RAC1 small GTPase
- RhoGTPase-activating proteins. Genes: ARHGAP15, ARHGAP25, ARHGAP30
  - [34]: ARHGAP proteins regulate GTPases
- Actin regulatory proteins. Genes: CORO1A, CYTIP
  - [37]: Cytoskeletal dynamics in cell migration

**Program citations**
- [34]: RAC1 and ARHGAP regulation
- [37]: Astrocyte activation and cell signaling
- [55]: Ets1 transcription factor in immune regulation

## Program: Cytokine Receptor Signaling and Lymphocyte Survival
Receptors for interleukins critical for lymphocyte development, expansion, and survival, including IL-2, IL-7, IL-15, IL-18. IL2RB and IL2RG form part of high-affinity IL-2 receptor promoting T cell proliferation and activation. IL7R signaling is essential for maintenance of naive T cell pools and memory T cell survival through homeostatic proliferation. IL18R1 enables response to IL-18, pro-inflammatory cytokine promoting IFN-γ production in T cells and NK cells. Collectively, these signaling pathways provide survival and expansion signals that counterbalance terminal differentiation, enabling long-lived anti-tumor immunity.

**Predicted impacts**
- IL-2-driven clonal expansion of tumor-specific T cells following antigen encounter in draining lymph nodes
- IL-7-mediated homeostatic survival of long-lived memory T cells in tumor microenvironment and peripheral tissues
- IL-18-driven IFN-γ production amplifying local inflammatory and anti-tumor responses
- Integration of cytokine signals with TCR signals determining T cell fate toward expansion versus terminal differentiation
- Prevention of lymphocyte apoptosis and maintenance of prolonged anti-tumor immunity

**Evidence summary**
IL-2 is critical autocrine and paracrine T cell growth factor promoting both proliferation and terminal differentiation, with balance determined by co-signals and transcription factor activity. IL-7 is constitutively produced by stromal cells and absolutely essential for T cell survival through STAT5 activation, with IL-7 deficiency causing severe T cell lymphopenia. IL-18 synergizes with IL-12 to promote Th1 differentiation and IFN-γ production by both CD4+ and CD8+ T cells and NK cells. In tumors, availability of these cytokines influences sustainability of anti-tumor immune responses and development of durable memory immunity.

**Atomic biological processes**
- IL-2 receptor signaling and T cell proliferation. Genes: IL2RB, IL2RG
  - [20]: IL2RA interleukin 2 receptor alpha
  - [25]: Interleukin signaling in NK cell expansion
- IL-7 receptor signaling and memory T cell survival. Genes: IL7R
  - [20]: IL2RA interleukin receptor complex
- IL-18 receptor signaling and IFN-γ production. Genes: IL18R1
  - [46]: IL18 interleukin 18 proinflammatory cytokine

**Atomic cellular components**
- IL-2 receptor complex. Genes: IL2RB, IL2RG
  - [20]: IL2RA IL2RB IL2RG receptor chains
- IL-7 receptor complex. Genes: IL7R
  - [20]: IL7R interleukin 7 receptor
- IL-18 receptor complex. Genes: IL18R1
  - [46]: IL18R1 interleukin 18 receptor subunit

**Program citations**
- [20]: IL2RA IL7R IL2RG interleukin receptors
- [25]: IL cytokines in NK cell expansion and function
- [46]: IL18 proinflammatory cytokine

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/140885
2. 2. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
3. 3. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
5. 5. Li W, Xiang S, Liu K, Wang Y, Li Q, OuYang Q, et al.. CSDE1 depletion inhibits tumor progression through enhancing B-cell infiltration in NSCLC. Cell Death &amp; Disease [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41419-025-08282-9
6. 6. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
7. 7. Gridley J, Pak D, Kumari A, Shupak J, Holland B, Shi Y, et al.. iHALT unlocks liver functionality as a surrogate secondary lymphoid organ. Nature [Internet]. 2025Nov26;. Available from: https://www.nature.com/articles/s41586-025-09803-4
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/917
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/3932
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/16401
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/915
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/16818
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/3001
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/5551
15. 15. Hor JL, Schrom EC, Wong-Rolle A, Vistain L, Shang W, Dong Q, et al.. Inhibitory PD-1 axis maintains high-avidity stem-like CD8+ T cells. Nature [Internet]. 2025Nov26;. Available from: https://www.nature.com/articles/s41586-025-09440-x
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/14938
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/18646
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/925
19. 19. de los RKI, Jayewickreme R, Lee MJ, Wilk AJ, Blomkalns AL, Nadeau KC, et al.. Interferon-mediated NK cell activation increases cytolytic activity against T follicular helper cells and limits antibody response to SARS-CoV-2. Nature Immunology [Internet]. 2025Nov21;26(12). Available from: https://www.nature.com/articles/s41590-025-02341-1
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/3559
21. 21. Kang X, Cheemalamarri SK, Yin Q. Organoid: a promising solution to current challenges in cancer immunotherapy. npj Biomedical Innovations [Internet]. 2025Dec12;2(1). Available from: https://www.nature.com/articles/s44385-025-00051-9
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/3821
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/6352
24. 24. Masopust D, Awasthi A, Bosselut R, Brooks DG, Buggert M, Chamoto K, et al.. Guidelines for T cell nomenclature. Nature Reviews Immunology [Internet]. 2025Nov18;. Available from: https://www.nature.com/articles/s41577-025-01238-2
25. 25. Liu X, Shi Y, Zhang J, Shetty K, Chew K, Küçük C, et al.. Key regulatory roles of PRDM1 in human NK-cell differentiation and activation. Leukemia [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s41375-025-02815-z
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/22806
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/12399
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/14462
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/10320
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/18566
31. 31. Chen L, Bian Y, Pronk E, van DC, V.D. van TT, Hoogenboezem RM, et al.. An inflammatory T-cell-stromal axis contributes to hematopoietic stem/progenitor cell failure and clonal evolution in human myelodysplastic syndrome. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65802-z
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/5879
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/5788
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/19264
35. 35. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/5294
37. 37. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/5290
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/8915
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/22637
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/3458
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/84433
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/7535
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/3606
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/4046
46. 46. Ian S, Alessia P, Sara S, Nausicaa C, Deepika P, Foteini C, et al.. ICOSL: more than a trigger of ICOS function.. Cell communication and signaling : CCS [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41299676/
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/18613
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/29851
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/3002
50. 50. Pogorelyy MV, Kirk AM, Adhikari S, Minervina AA, Sundararaman B, Vegesana K, et al.. TIRTL-seq: deep, quantitative and affordable paired TCR repertoire sequencing. Nature Methods [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s41592-025-02907-9
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/14939
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/3635
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/23871
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/2113
55. 55. Available from: https://www.ncbi.nlm.nih.gov/gene/8651
56. 56. Ibáñez-Molero S, Veldman J, Simon NJ, Traets JJH, George A, Hoefakker K, et al.. Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. Nature [Internet]. 2025Nov19;. Available from: https://www.nature.com/articles/s41586-025-09754-w
57. 57. Lu Q, Luo J, Tung C-H, Wang X, Zhao Z. Quantitative profiling of intratumor immune heterogeneity identifies loss of immune diversity as a hallmark of cancer progression. npj Precision Oncology [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41698-025-01223-x_reference.pdf
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/5996
60. 60. Available from: https://www.ncbi.nlm.nih.gov/gene/5777
61. 61. Available from: https://www.ncbi.nlm.nih.gov/gene/14678
62. 62. Available from: http://json-schema.org/draft-07/schema#",
