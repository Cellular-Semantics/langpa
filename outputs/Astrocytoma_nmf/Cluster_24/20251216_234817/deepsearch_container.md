# Gene Program Markdown Report

## Context
- Cell type: Tumor-associated macrophages, microglia, and infiltrating myeloid cells
- Disease: Astrocytoma, glioblastoma multiforme
- Tissue: Brain, central nervous system

## Input Genes
C3, APBB1IP, HCLS1, PTPRC, OLR1, CSF2RA, INPP5D, LCP2, CSF1R, LY86, DOCK8, CD53, TBXAS1, IKZF1, TFEC, PLXDC2, CD74, CD84, SAMSN1, LNCAROD, NCKAP1L, AC079015.1, LAPTM5, TLR2, RNASET2, ... (200 total)

## Program: Fc Receptor Signaling and Antibody-Dependent Responses
This program encompasses Fc receptors (FCGR1A, FCGR1B, FCGR2A, FCGR3A) and their intracellular signaling machinery including SYK, LYN, HCK, and adaptor proteins FYB1, CARD11, enabling myeloid cells to recognize and respond to antibody-opsonized targets through antibody-dependent cellular cytotoxicity. The program includes NADPH oxidase components (CYBA, CYBB) for reactive oxygen species production and cytotoxic effector functions.

**Predicted impacts**
- Enhanced recognition of antibody-coated tumor cells
- Activation of antibody-dependent cellular cytotoxicity pathways
- Production of reactive oxygen species and cytotoxic mediators
- Potential therapeutic vulnerability to monoclonal antibody therapy when combined with checkpoint blockade

**Evidence summary**
The complete Fc receptor signaling cascade is represented in the gene list, encompassing all four classical FcγR subtypes and their essential intracellular signaling intermediates. In glioblastoma, these receptors retain capacity for antibody-dependent responses yet are suppressed through immunoregulatory mechanisms. Therapeutic monoclonal antibodies targeting tumor-associated antigens could engage this pathway if immunosuppression is concurrently targeted.

**Atomic biological processes**
- Immunoreceptor tyrosine-based activation motif (ITAM) signaling. Genes: SYK, LYN, HCK, FYB1, CARD11
  - [11]: Describes Fcγ receptor ITAM structure and SYK/LYN coupling
  - [38]: CD86 as co-stimulatory molecule in immune responses
- Antibody recognition and immune complex detection. Genes: FCGR1A, FCGR1B, FCGR2A, FCGR3A
  - [18]: CD274/PD-L1 in immune checkpoint context; immune complex formation
  - [38]: CD86 and costimulation in immune responses
- Oxidative burst and cytotoxic granule exocytosis. Genes: CYBA, CYBB
  - [11]: NADPH oxidase activation downstream of Fc receptors

**Atomic cellular components**
- Fc receptor complex at cell membrane. Genes: FCGR1A, FCGR1B, FCGR2A, FCGR3A
  - [11]: Structure and assembly of Fcγ receptor signaling complexes

**Required genes (not in input)**
- Genes: FcRγ (FCER1G), DAP12 (TYROBP - actually in input), Downstream kinases (ZAP70, BTK)
  - [11]: Essential components of ITAM-mediated signaling

**Program citations**
- [11]: FCGR1 and FCGR2B function in ADCC and immune complex endocytosis
- [18]: CD274 (PD-L1) encoding immune inhibitory ligand
- [38]: CD86 co-stimulation in T cell activation
- [29]: Targeting tumor-associated macrophages via CSF-1R inhibition in GBM
- [63]: TREM2 and TAM polarization in gastric cancer; checkpoint molecules

## Program: CSF-Dependent Myeloid Cell Differentiation and Survival
This program encompasses colony-stimulating factor receptors (CSF1R, CSF2RA, CSF3R) and their signaling machinery (SYK, PI3K pathway components, STAT transcription factors), governing differentiation and survival of distinct myeloid cell lineages. In glioblastoma, CSF1R-dependent macrophage differentiation represents a primary driver of tumor-associated macrophage accumulation and polarization toward immunosuppressive phenotypes.

**Predicted impacts**
- Sustained myeloid cell accumulation within glioblastoma through CSF1R-dependent differentiation
- Polarization toward alternatively activated, immunosuppressive macrophage phenotype
- Resistance to CSF1R inhibitor monotherapy through metabolic adaptation
- Potential synergy between CSF1R inhibition and metabolic targeting agents

**Evidence summary**
CSF1R-dependent differentiation of tumor-associated macrophages is a central driver of glioblastoma progression. The complete signaling machinery downstream of CSF receptor engagement is present in the gene list. CSF1R inhibition shows clinical potential but is limited by metabolic resistance mechanisms that involve oxidative phosphorylation upregulation. Combined targeting of CSF1R with metabolic inhibitors (piperlongumine, vorinostat) shows improved efficacy in preclinical models.

**Atomic biological processes**
- Monocyte to macrophage differentiation via M-CSF signaling. Genes: CSF1R, SYK, PIK3AP1, PIK3R5, RUNX1, IRF8
  - [44]: CSF1 pathway in macrophage differentiation
  - [29]: CSF-1R inhibition targeting TAMs in GBM
- Metabolic reprogramming and oxidative phosphorylation. Genes: PDK4, ACSL1, PPARG
  - [29]: TRAP-seq identifies oxidative phosphorylation as CSF-1R inhibitor resistance mechanism
- Granulocyte and alternative myeloid differentiation. Genes: CSF2RA, CSF3R
  - [44]: GM-CSF and G-CSF receptor signaling in myeloid development

**Atomic cellular components**
- CSF receptor complex and receptor tyrosine kinase signaling. Genes: CSF1R, CSF2RA, CSF3R
  - [44]: Structural and functional aspects of CSF receptors
  - [47]: M-CSF-receptor mediated monocyte differentiation
- PI3K/AKT/mTOR signaling cascade. Genes: PIK3AP1, PIK3R5
  - [65]: SYK-PI3K/AKT/mTOR pathway in myeloid cell polarization

**Required genes (not in input)**
- Genes: STAT3, STAT6, MAPK pathway components, AKT, mTOR
  - [29]: Key signaling nodes in CSF-1R pathway and metabolic adaptation

**Program citations**
- [29]: Comprehensive analysis of CSF-1R inhibitor resistance in GBM through TRAP-seq
- [44]: CSF1 pathway mechanisms in monocyte to macrophage differentiation
- [31]: Pericyte-derived signals influence macrophage polarization
- [65]: TREM2-mediated NF-κB and PI3K/AKT signaling in myeloid cells

## Program: Complement and Scavenger Receptor Pattern Recognition
This program encompasses complement receptors (C3AR1) and scavenger receptors (MSR1, STAB1, OLR1, VSIG4) that recognize pathogen-associated molecular patterns, danger-associated molecular patterns, and altered self-antigens. These receptors mediate myeloid cell recruitment to inflammatory sites and enhance phagocytic clearance of pathogens and dying cells, with implications for tumor cell clearance and immune tolerance.

**Predicted impacts**
- Enhanced recruitment of myeloid cells to tumor regions with complement activation
- Increased phagocytosis of apoptotic cells and tissue debris
- Promotion of immune tolerance through apoptotic cell clearance
- Potential suppression of immunogenic cell death signals in glioblastoma

**Evidence summary**
Complement and scavenger receptor signaling mediates myeloid cell recruitment and clearance functions critical for both immune surveillance and immune tolerance. In glioblastoma, activation of these pathways by dying tumor cells and tumor-associated debris may promote macrophage accumulation while simultaneously suppressing anti-tumor immunity through apoptotic cell recognition. The presence of multiple complement components and scavenger receptors suggests that myeloid cells within astrocytomas are actively engaged in clearing dead cells, a process that may suppress immunogenic danger signals.

**Atomic biological processes**
- Complement cascade activation and C3a chemotaxis. Genes: C3AR1, C1QA, C1QB, C1QC
  - [30]: VEGFA contribution to MDSC differentiation and complement interactions
- Scavenger receptor-mediated ligand recognition. Genes: MSR1, STAB1, OLR1, VSIG4
  - [10]: SIRPA as signal regulatory protein alpha in TAM polarization
- Apoptotic cell recognition and clearance. Genes: MERTK, VSIG4, STAB1
  - [51]: Programmed cell death pathways and immune cell elimination

**Atomic cellular components**
- Complement component C1q complex. Genes: C1QA, C1QB, C1QC
  - [1]: FAS gene and apoptosis regulation
- Pattern recognition receptor family. Genes: MSR1, STAB1, OLR1, C3AR1, VSIG4
  - [10]: SIRPA expression in myeloid cells

**Required genes (not in input)**
- Genes: CR1, CR3 (already includes ITGAM/ITGB2), CD35, Factor H and other complement regulators
  - [30]: Complement component and regulation genes

**Program citations**
- [30]: VEGFA and complement in tumor microenvironment
- [31]: Macrophage polarization and complement regulation in pericyte-poor tumors

## Program: Toll-Like Receptor and Pattern Recognition Innate Immune Signaling
This program encompasses Toll-like receptors (TLR2) and associated signaling machinery (TYROBP/DAP12, TREM2) that detect pathogen-associated and danger-associated molecular patterns. TLR engagement initiates inflammatory cascades through NF-κB and IRF pathway activation, promoting production of pro-inflammatory cytokines including IL-1β and IL-18. TREM2-TYROBP signaling represents an emerging regulator of myeloid cell polarization in both physiological and pathological CNS contexts.

**Predicted impacts**
- Recognition of microbial and damage-associated patterns within glioblastoma
- Activation of pro-inflammatory transcriptional programs
- Production of IL-1β and IL-18 driving neuroinflammation
- Paradoxical suppression of TLR responses in tumor-associated macrophages (endotoxin tolerance)
- TREM2-mediated polarization toward immunosuppressive macrophage phenotype
- Regulation of macrophage accumulation and survival through TREM2-PI3K/AKT signaling

**Evidence summary**
TLR2 and TREM2 signaling represent central nodes in myeloid cell recognition of environmental danger. In glioblastoma, TREM2 has emerged as a critical regulator of TAM polarization toward immunosuppressive states through activation of NF-κB and PI3K/AKT/mTOR pathways. TREM2+ TAMs drive T cell exhaustion, promote IL-10 and TGF-β production, and represent independent predictors of poor prognosis. Paradoxically, while these pattern recognition receptors can initiate pro-inflammatory responses, tumor-associated macrophages undergo endotoxin tolerance that suppresses TLR-mediated inflammation, potentially maintained through IRAK3-dependent mechanisms. The presence of IRAK3 in the gene list suggests that inhibitory TLR signaling may be a characteristic feature of glioblastoma-associated macrophages.

**Atomic biological processes**
- TLR2-mediated pathogen-associated molecular pattern recognition. Genes: TLR2, CD14, IRAK3, TYROBP
  - [25]: TLR4 and TLR2 in innate immune receptors and disease
  - [6]: TLR signaling in acute TBI astrocyte activation
- TREM2-TYROBP signaling and myeloid cell activation. Genes: TREM2, TYROBP, SYK, PIK3AP1, PIK3R5
  - [12]: TREM2 pathway in microglial activation and hippocampal recognition memory
  - [65]: TREM2-mediated regulation of myeloid cells and SYK-PI3K/AKT/mTOR pathway
  - [63]: TREM2 facilitates gastric cancer progression and M2 macrophage polarization
- Pro-inflammatory cytokine production. Genes: IL1B, IL18, IRAK3
  - [6]: IL-1, IL-6, TNF, and IFN-γ upregulation in acute TBI astrocytes
  - [45]: IL-1, IL-6, TNF, and IFN-γ in chronic TBI astrocyte transcriptome
- Endotoxin tolerance and inhibitory signaling. Genes: IRAK3, RGS1, RGS10
  - [29]: Immune suppression and endotoxin tolerance in TAMs

**Atomic cellular components**
- TLR2 signaling complex at cell membrane. Genes: TLR2, CD14
  - [25]: TLR structure and function
- TREM2-TYROBP signaling complex. Genes: TREM2, TYROBP, SYK
  - [12]: TREM2 and TYROBP association
  - [15]: TYROBP as transmembrane immune signaling adaptor with ITAM

**Required genes (not in input)**
- Genes: MYD88, IRAK1, IRAK4, TRAF6, TAK1, IκBα, p65/RelA, IRF3, IRF7
  - [6]: Key signaling intermediates in TLR pathway

**Program citations**
- [12]: TREM2 pathway in microglial function
- [6]: TLR signaling in TBI-associated astrocyte activation
- [63]: TREM2+ TAMs promote cancer progression and drive T cell exhaustion
- [65]: TREM2-mediated NF-κB signaling and immunosuppressive cytokine secretion

## Program: Chemokine-Mediated Myeloid Cell Recruitment and Polarization
This program encompasses chemokine genes (CCL3, CCL4, CCL3L1, CCL4L2) and their receptors, along with cytokine signaling pathways (IL1B, IL18, IL13RA1, IL4R, IL10RA) that promote myeloid cell migration and determine polarization toward pro-inflammatory versus anti-inflammatory phenotypes. In glioblastoma, this program mediates accumulation of both pro-inflammatory and immunosuppressive myeloid cells within the tumor microenvironment.

**Predicted impacts**
- Sustained recruitment of myeloid cells to glioblastoma microenvironment
- Polarization of macrophages toward M2 immunosuppressive phenotype through IL-4/IL-13 signaling
- Amplification of pro-inflammatory responses through IL-1β and IL-18 autocrine loops
- Suppression of pro-inflammatory responses through IL-10 signaling
- Spatial organization of myeloid cell populations based on chemokine gradients

**Evidence summary**
Chemokines and cytokines orchestrate myeloid cell recruitment and phenotypic programming within glioblastomas. CCL3 and CCL4 are pro-inflammatory chemokines upregulated in acute inflammation but downregulated in chronic pathology, suggesting transition from acute recruitment phase to chronic, suppressed inflammatory state. IL-4 and IL-13 signaling through IL4R and IL13RA1 promotes alternative macrophage polarization, contributing to immunosuppressive TAM phenotype. IL-10 acts as a potent brake on macrophage-mediated pro-inflammatory responses. The presence of this complete chemokine and cytokine signaling program suggests that glioblastoma-derived signals continuously reprogram infiltrating myeloid cells toward immunosuppressive states while simultaneously recruiting additional myeloid cells through chemokine gradients.

**Atomic biological processes**
- Chemokine-driven myeloid cell recruitment and migration. Genes: CCL3, CCL4, CCL3L1, CCL4L2
  - [45]: CCL3, CCL4 downregulation in subacute TBI; leukocyte migration pathways
  - [62]: CD8 T cell TNF-α and chemokine expression in inflammatory microenvironments
- M1/M2 macrophage polarization via IL-4 and IL-13 signaling. Genes: IL13RA1, IL4R
  - [13]: Ovine macrophage differentiation and polarization with proteomic characterization
  - [65]: TREM2 and macrophage polarization pathways
- IL-10-mediated immune suppression. Genes: IL10RA
  - [43]: IL-10 signaling and negative immune regulation
- Pro-inflammatory cytokine signaling and inflammatory amplification. Genes: IL1B, IL18
  - [45]: IL-1 and IL-6 signaling in acute and chronic TBI
  - [19]: IL-1β as pro-inflammatory cytokine from activated macrophages

**Atomic cellular components**
- Chemokine receptors on myeloid cell surface.
  - [45]: Chemokine-mediated leukocyte migration
- Cytokine receptor signaling complexes. Genes: IL13RA1, IL4R, IL10RA
  - [13]: M-CSF and GM-CSF receptor signaling in macrophage differentiation

**Required genes (not in input)**
- Genes: CCR1, CCR2, CCR5, CCL2, IL-6, STAT3, STAT6
  - [45]: CCR and STAT family members in macrophage polarization

**Program citations**
- [45]: Chemokine and cytokine signatures in temporal phases of CNS injury
- [13]: Macrophage polarization and cytokine-mediated phenotypic programming
- [62]: TNF-α and IFN-γ production by activated T cells in inflammatory niches

## Program: Integrin and Cell Adhesion Molecule-Mediated Myeloid Cell Trafficking
This program encompasses β2 integrins (ITGAM/CD11b, ITGB2/CD18) and other integrin family members (ITGAX/CD11c), along with adhesion molecule signaling intermediates (LCP2/SLP-76, SKAP2, FYB1) that mediate myeloid cell extravasation from vasculature and interactions with tissue-resident cells. These molecules are essential for breaching the blood-brain barrier and accumulating within glioblastomas.

**Predicted impacts**
- Increased myeloid cell extravasation across tumor vasculature
- Enhanced blood-brain barrier disruption and tumor cell invasion
- Strengthened myeloid cell-endothelial cell and myeloid cell-tumor cell interactions
- Amplification of adhesion signals promoting cell survival and activation
- Positioning of myeloid cells within specific tumor microanatomical compartments

**Evidence summary**
The β2 integrin family, comprised of ITGAM/CD11b and ITGB2/CD18, represents the primary pathway for leukocyte extravasation from the vasculature. In glioblastoma, upregulation of ICAM-1 and VCAM-1 on tumor endothelium, driven by tumor-derived inflammatory mediators, enhances integrin-mediated myeloid cell recruitment. The presence of multiple integrin signaling adaptor proteins (LCP2, SKAP2, FYB1) suggests that integrin engagement within glioblastomas generates robust intracellular signaling that promotes myeloid cell survival, activation, and positioning within tumor microenvironments. Pericyte depletion in glioblastomas results in increased myeloid cell infiltration, suggesting that reduced barrier integrity enhances integrin-mediated extravasation.

**Atomic biological processes**
- Integrin-mediated leukocyte adhesion and extravasation. Genes: ITGAM, ITGB2, ITGAX
  - [34]: ITGB2 in immune cell adhesion and leukocyte adhesion deficiency
  - [27]: ITGA4 (CD49d) in cell adhesion and bone marrow microenvironment
- Adaptor protein-mediated integrin signaling. Genes: LCP2, SKAP2, FYB1
  - [27]: ITGA4 engagement and cell adhesion
- Endothelial cell-myeloid cell interactions. Genes: ITGAM, ITGB2, CD44
  - [35]: ICAM molecules in T cell adhesion to antigen-presenting cells

**Atomic cellular components**
- β2 integrin complex at cell membrane. Genes: ITGAM, ITGB2
  - [34]: Integrin structure and heterodimer formation
- Integrin-associated signaling adaptor proteins. Genes: LCP2, SKAP2, FYB1
  - [27]: Integrin signaling complexes

**Required genes (not in input)**
- Genes: ICAM-1, ICAM-2, VCAM-1, JAM-C, Selectins (L-selectin, E-selectin, P-selectin)
  - [34]: Adhesion molecules and their ligands

**Program citations**
- [31]: Pericyte-dependent control of vascular integrity and immune cell infiltration in gliomas
- [34]: ITGB2 function in immune cell adhesion
- [35]: ICAM molecules in cell-cell adhesion

## Program: Major Histocompatibility Complex Class II and Antigen Presentation
This program encompasses MHC class II molecules (HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DMB, HLA-DQB1) and co-stimulatory molecules (CD86) essential for CD4+ T cell activation. While tumor-associated macrophages retain the molecular machinery for robust antigen presentation, this capacity is suppressed through tumor-derived immunoregulatory signals in glioblastoma, contributing to T cell exhaustion rather than activation.

**Predicted impacts**
- Retained capacity for antigen presentation despite tumor microenvironment suppression
- Potential enhancement of T cell activation if checkpoint blockade is implemented
- Co-stimulatory capacity through CD86 expression on TAMs
- Paradoxical promotion of T cell exhaustion through continuous low-level antigen presentation without adequate co-stimulation

**Evidence summary**
Glioblastoma-associated macrophages retain robust expression of MHC class II molecules and CD86 co-stimulatory molecules, suggesting retained capacity for antigen presentation. However, in the immunosuppressive tumor microenvironment characterized by high expression of immune checkpoint ligands (PD-L1 on tumor cells and macrophages) and immunosuppressive cytokines (IL-10, TGF-β), antigen presentation events often result in T cell exhaustion rather than activation. The presence of this complete antigen presentation program suggests that blocking checkpoint molecules (PD-L1, PD-L2, B7-H3, B7-H4) concurrent with enhancing co-stimulation (4-1BB, GITR) could unlock anti-tumor immunity in glioblastoma patients.

**Atomic biological processes**
- MHC class II peptide presentation pathway. Genes: HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DMB, HLA-DQB1, CD74
  - [35]: MHC-II compartment and antigen presentation in dendritic cells
  - [46]: Tumor microenvironment and immune landscape of HGGs
- Co-stimulatory molecule signaling. Genes: CD86
  - [35]: CD80 and CD86 as co-stimulatory molecules for T cell activation
  - [38]: CD86 molecule function

**Atomic cellular components**
- MHC class II complex at cell surface. Genes: HLA-DRA, HLA-DRB1, HLA-DPA1, HLA-DPB1, HLA-DQB1, CD74
  - [35]: Structure of MHC class II molecules
- MHC class II compartment in endosomal pathway. Genes: HLA-DMB
  - [35]: MIIC (MHC-II compartment) structure and function

**Required genes (not in input)**
- Genes: CD80, CIITA, Cathepsin L, TAP1, TAP2, HLA-DM
  - [35]: Additional molecules required for MHC class II peptide loading

**Program citations**
- [35]: Comprehensive analysis of antigen presentation pathways in M cells
- [46]: Immune landscape of high-grade gliomas
- [29]: CSF-1R inhibition targeting immunosuppressive macrophages in GBM

## Program: Lipid Mediator Production and Eicosanoid Metabolism
This program encompasses enzymes governing synthesis of lipid-derived inflammatory mediators including leukotrienes (ALOX5, ALOX5AP), prostaglandins (PTGS2), thromboxanes (TBXAS1), and regulatory proteins (LPCAT2, ACSL1). While leukotrienes promote pro-inflammatory myeloid cell responses, prostaglandins including PGE2 function as potent immunosuppressive mediators that enhance macrophage IL-10 production and suppress pro-inflammatory cytokine secretion.

**Predicted impacts**
- Production of leukotriene B4 promoting pro-inflammatory myeloid cell recruitment
- Production of prostaglandin E2 suppressing pro-inflammatory macrophage responses
- Duality of inflammatory and immunosuppressive lipid mediator production within TAMs
- Potential therapeutic target through 5-lipoxygenase or COX-2 inhibition

**Evidence summary**
Tumor-associated macrophages express both pro-inflammatory (5-lipoxygenase) and immunosuppressive (COX-2) lipid mediator synthesis pathways. Leukotriene B4 functions as a potent chemoattractant for myeloid cells, potentially explaining continued recruitment despite immunosuppressive microenvironment. Conversely, PGE2 is a canonical immunosuppressive mediator that enhances IL-10 production and suppresses TNF-α and IL-12 synthesis. This apparent contradiction suggests that glioblastoma-associated macrophages simultaneously produce both recruitment signals (for additional myeloid cells) and suppression signals (for adaptive immunity). Targeting lipid mediator synthesis through 5-lipoxygenase or COX-2 inhibition might reduce immunosuppression while maintaining myeloid cell recruitment, thereby enhancing anti-tumor immunity.

**Atomic biological processes**
- Leukotriene synthesis and pro-inflammatory signaling. Genes: ALOX5, ALOX5AP
  - [54]: ALOX5 (arachidonate 5-lipoxygenase) in leukotriene biosynthesis
- Prostaglandin synthesis and immunosuppressive signaling. Genes: PTGS2
  - [56]: PTGS2 (COX-2) predisposition and arachidonic acid metabolism
- Thromboxane synthesis. Genes: TBXAS1
  - [56]: TBXAS1 in prostaglandin metabolism
- Fatty acid activation and lipid remodeling. Genes: ACSL1, LPCAT2
  - [56]: Lipid mediator substrate availability

**Atomic cellular components**
- 5-lipoxygenase complex and leukotriene synthesis machinery. Genes: ALOX5, ALOX5AP
  - [54]: ALOX5 and ALOX5AP in leukotriene pathway
- Cyclooxygenase complex and prostaglandin synthesis machinery. Genes: PTGS2, TBXAS1
  - [56]: COX-2 and prostaglandin synthesis

**Required genes (not in input)**
- Genes: LTA4H, PGE2 synthases, 15-LOX, COX-1 (PTGS1)
  - [56]: Additional enzymes in eicosanoid synthesis

**Program citations**
- [54]: ALOX5 in leukotriene synthesis
- [56]: COX-2 and arachidonic acid metabolism in disease

## Program: Rho GTPase Signaling and Actin Cytoskeletal Dynamics
This program encompasses regulators of Rho family small GTPases (VAV1, RAC1) and their guanine nucleotide exchange factors and GTPase-activating proteins (DOCK2, DOCK4, DOCK8, ARHGAP15, ARHGAP25), along with downstream actin polymerization regulators (FMN1). These proteins control cytoskeletal rearrangement essential for myeloid cell migration through tissue, phagocytosis, and immune synapse formation.

**Predicted impacts**
- Enhanced myeloid cell migration toward chemokine gradients within glioblastoma
- Increased phagocytic capacity through actin-dependent pseudopod formation
- Sustained positioning within specific tumor microenvironments through dynamic actin remodeling
- Regulation of migration intensity through GTPase-activating protein-mediated signal suppression

**Evidence summary**
Rho family GTPases, particularly RAC1, represent central regulators of actin cytoskeletal dynamics essential for myeloid cell migration and effector functions. VAV1, a guanine nucleotide exchange factor for RAC1 and CDC42, couples immune receptor signaling to actin polymerization, thereby linking cell activation signals to migration responses. DOCK family proteins represent a distinct family of Rho GTPase exchange factors with particular roles in leukocyte migration; mice lacking DOCK2 display severe impairment of lymphocyte trafficking. The presence of multiple GTPase-activating proteins (ARHGAP15, ARHGAP25) suggests that glioblastoma-associated macrophages maintain dynamic balance between migration-promoting and migration-suppressing signals, potentially enabling rapid responses to spatially localized chemokine gradients within tumors.

**Atomic biological processes**
- Rho GTPase activation and regulation. Genes: VAV1, RAC1, DOCK2, DOCK4, DOCK8, ARHGAP15, ARHGAP25
  - [52]: RAC1 and Rho GTPase signaling in neural crest cell migration
- Actin polymerization and cytoskeletal rearrangement. Genes: FMN1, FMNL1
  - [52]: FMN1 and formin-mediated actin dynamics
- Chemokine-induced migration signaling. Genes: DOCK2, DOCK4, DOCK8, VAV1
  - [52]: DOCK2 in lymphocyte migration

**Atomic cellular components**
- Rho GTPase cycle and nucleotide exchange machinery. Genes: VAV1, DOCK2, DOCK4, DOCK8
  - [52]: GEF-mediated GTPase activation
- Actin nucleation and polymerization apparatus. Genes: FMN1, FMNL1
  - [52]: Formin family in actin dynamics

**Required genes (not in input)**
- Genes: CDC42, RHOA, Arp2/3 complex, Cofilin, Profilin
  - [52]: Additional regulators of actin cytoskeleton

**Program citations**
- [52]: Comprehensive analysis of Rho GTPase signaling in cell migration

## Program: Immunoregulatory Checkpoints and Immune Tolerance Signaling
This program encompasses inhibitory immune checkpoint molecules (LILRB1, LILRB4, SIGLEC8, SIGLEC10, VSIR) and their associated signaling that suppress immune cell activation and promote T cell exhaustion. TREM2 also participates in this program through its role in promoting alternatively activated macrophage polarization and immunosuppression. These molecules collectively define the immunosuppressive capacity of glioblastoma-associated myeloid cells.

**Predicted impacts**
- Suppression of T cell activation through multiple checkpoint mechanisms
- Promotion of regulatory T cell differentiation and exhaustion of CD8+ T cells
- Establishment of immunosuppressive tumor microenvironment dependent on TAM checkpoint molecules
- Therapeutic vulnerability to checkpoint blockade (anti-LILRB, anti-SIGLEC, anti-VSIR)
- Potential combination approaches targeting multiple checkpoint molecules simultaneously

**Evidence summary**
Glioblastoma-associated macrophages express an extensive suite of inhibitory checkpoint molecules that collectively suppress anti-tumor immunity. LILRB1 and LILRB4 recognize MHC class I molecules and deliver inhibitory signals; elevated LILRB4 expression predicts poor outcomes and reduced anti-tumor immunity. Siglec-14, recently characterized as a regulator of tumor-associated macrophage polarization, recognizes sialic acid-bearing ligands including LGALS3BP produced by tumor cells, thereby promoting protumoral macrophage programming. VSIR represents another emerging checkpoint molecule on alternatively activated macrophages that suppresses T cell responses. TGF-β signaling on glioblastoma-associated macrophages further promotes regulatory T cell differentiation and immune suppression. The cumulative effect of this checkpoint program is creation of a profoundly immunosuppressive microenvironment resistant to standard checkpoint blockade approaches, suggesting that targeting multiple checkpoint pathways simultaneously may be required for therapeutic efficacy.

**Atomic biological processes**
- Leukocyte immunoglobulin-like receptor (LILR) signaling. Genes: LILRB1, LILRB4
  - [50]: BTLA dysregulation in poor outcomes
  - [65]: LILRB4 in TREM2-mediated immunosuppression
- Siglec-mediated immune regulation. Genes: SIGLEC8, SIGLEC10
  - [66]: Siglec-14-LGALS3BP axis in tumor-associated macrophage polarization
- V-domain Ig suppressor signaling. Genes: VSIR
  - [65]: VSIR expression on alternatively activated macrophages
- TGF-β signaling and regulatory T cell differentiation. Genes: TGFBR2
  - [62]: TGF-β in stromal cells driving regulatory T cell development

**Atomic cellular components**
- Inhibitory immune checkpoint receptor complexes. Genes: LILRB1, LILRB4, SIGLEC8, SIGLEC10, VSIR
  - [65]: Checkpoint molecule expression on TAMs

**Required genes (not in input)**
- Genes: PD-L1 (CD274), PD-L2, B7-H3, B7-H4, HVEM, BTLA, TIM-3
  - [65]: Comprehensive checkpoint molecule family

**Program citations**
- [65]: Comprehensive review of TREM2-mediated immune regulation and checkpoint molecules
- [66]: Siglec-14-LGALS3BP axis in CRC and potential application to GBM
- [63]: TREM2 and checkpoint molecules in gastric cancer TAMs

## Program: Phagocytic and Lysosomal Processing Functions
This program encompasses genes governing myeloid cell phagocytic capacity and lysosomal functions essential for clearance of apoptotic cells, pathogens, and tissue debris. MERTK (Mer receptor tyrosine kinase) represents a critical regulator of apoptotic cell recognition, while lysosomal enzymes (CTSB) and trafficking proteins (LAPTM5) facilitate degradation and recycling of internalized material. The coordinated expression of these genes defines a population of tissue-resident macrophages with high phagocytic capacity.

**Predicted impacts**
- Enhanced clearance of apoptotic tumor cells and dying immune cells
- Suppression of immunogenic signals from dead cells through apoptotic cell recognition
- Efficient antigen processing and presentation of internalized antigens
- Immune tolerance promotion through MERTK-mediated apoptotic cell clearance
- Regulation of migration intensity through RGS-mediated suppression of chemokine receptor signaling

**Evidence summary**
MERTK-mediated recognition of apoptotic cells represents a major anti-inflammatory signal on macrophages, promoting IL-10 production and suppressing pro-inflammatory cytokine secretion. In glioblastoma, high rates of cell death generate abundant apoptotic cells that are efficiently cleared by MERTK-expressing macrophages, thereby suppressing immunogenic cell death signals that would otherwise activate anti-tumor immunity. This process paradoxically supports tumor progression by removing death-associated danger signals. The presence of cathepsin B and lysosomal trafficking proteins suggests that glioblastoma-associated macrophages maintain robust degradative capacity for both phagocytosed pathogens and damaged tissues, contributing to tissue remodeling and angiogenic activities within tumors.

**Atomic biological processes**
- Apoptotic cell recognition and phagocytosis. Genes: MERTK
  - [31]: Pericyte-orchestrated tumor-restraining microenvironment; macrophage-mediated clearance
  - [63]: TREM2 and macrophage polarization affecting apoptotic cell clearance
- Lysosomal protein degradation and antigen processing. Genes: CTSB, LAPTM5
  - [51]: Programmed cell death pathways and immune cell elimination
- Regulation of myeloid cell migration and migration suppression. Genes: RGS1, RGS10
  - [43]: RGS proteins as negative regulators of GPCR signaling

**Atomic cellular components**
- Apoptotic cell recognition receptor. Genes: MERTK
  - [31]: MERTK in recognition of phosphatidylserine
- Lysosomal compartment and proteolytic machinery. Genes: CTSB, LAPTM5
  - [51]: Cathepsin enzymes in lysosomal proteolysis

**Required genes (not in input)**
- Genes: TAM receptors (AXL, TYRO3), Gas6, Protein S, Cathepsins L, S, K, Lysosomal hydrolases
  - [31]: TAM receptor signaling in macrophage biology

**Program citations**
- [31]: Macrophage-mediated immune tolerance through apoptotic cell clearance
- [51]: Programmed cell death pathways and immune cell fate

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/355
2. 2. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/4684
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/12977
6. 6. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
7. 7. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
8. 8. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/140885
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/14129
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/54209
12. 12. Elkhamary A, Gerner C, Bileck A, Gerner I, Jenner F. Proteomic and morphologic characterization of ovine macrophage differentiation and polarization. Scientific Reports [Internet]. 2025Dec1;. Available from: https://www.nature.com/articles/s41598-025-30269-x
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/14130
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/7305
15. 15. Elkhamary A, Gerner C, Bileck A, Gerner I, Jenner F. Proteomic and morphologic characterization of ovine macrophage differentiation and polarization. Scientific Reports [Internet]. 2025Dec1;. Available from: https://www.nature.com/articles/s41598-025-30269-x_reference.pdf
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/3553
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/10891
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/3552
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/4780
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/3394
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/12505
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/7099
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/6688
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/3676
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/12475
27. 27. Miao C, Ding Z, Wu J, An Q, Shu Y, Jiang H, et al.. Identification and targeting oxidative phosphorylation/glycolysis to overcome anti-CSF-1R therapy resistance in glioblastoma. Cell Death &amp; Disease [Internet]. 2025Dec10;. Available from: https://www.nature.com/articles/s41419-025-08288-3
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
29. 29. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/5290
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/3689
33. 33. Wang D, Lim S, van de WWJ, Lopez-Iglesias C, Okura Y, Teranishi-Ikawa Y, et al.. Human gut M cells resemble dendritic cells and present gluten antigen. Nature [Internet]. 2025Dec10;. Available from: https://www.nature.com/articles/s41586-025-09829-8
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/3684
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=942
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/4312
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/861
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/207
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/16153
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/1435
43. 43. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/1436
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/894
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/151888
47. 47. Lozano-Gil JM, Pedoto A, Conesa-Hernández AM, Ocaña-Esparza M, Mulero V, Tyrkalska SD. Programmed cell death pathways coordinate neutrophil and macrophage clearance in zebrafish and are differentially exploited by Salmonella Typhimurium. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08291-8
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/5879
49. 49. Timothy P, Hosna S, Nazli S, Kate EL, Alexandra JC. Get with the program: regulation of T cell death.. Trends in immunology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41298189/
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/11689
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/5743
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/5788
53. 53. Yang S, Yang Y, Fang Y, Zhou Q, Sun W, Zhang Z, et al.. Targeting tumour-infiltrating B cells: mechanisms and advances in cancer therapy. Cell Death &amp; Disease [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s41419-025-08254-z
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/19264
55. 55. Lu Q, Luo J, Tung C-H, Wang X, Zhao Z. Quantitative profiling of intratumor immune heterogeneity identifies loss of immune diversity as a hallmark of cancer progression. npj Precision Oncology [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41698-025-01223-x_reference.pdf
56. 56. Chen L, Bian Y, Pronk E, van DC, V.D. van TT, Hoogenboezem RM, et al.. An inflammatory T-cell-stromal axis contributes to hematopoietic stem/progenitor cell failure and clonal evolution in human myelodysplastic syndrome. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65802-z
57. 57. Zhang Z, Yu K, Cao Y, Xie P, Wang L, Shen Z, et al.. TREM2 facilitates gastric cancer progression and immune evasion via inhibiting TRIM21-mediated STAT1 degradation in tumor-associated macrophages. Cell Death &amp; Disease [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41419-025-08198-4
58. 58. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
59. 59. Huang Y, Fang W. TREM2-mediated regulation of myeloid cells in the tumor microenvironment: new insights and therapeutic prospects. npj Precision Oncology [Internet]. 2025Nov18;9(1). Available from: https://www.nature.com/articles/s41698-025-01152-9
60. 60. Lin K-Y, Jiang J-K, Lai J-I, Lin S-Y, Ku Y-C, Lin M-H, et al.. Siglec-14-LGALS3BP glycoimmune axis shapes tumor-associated macrophage polarization and confers poor outcome in colorectal cancer. npj Precision Oncology [Internet]. 2025Dec15;9(1). Available from: https://www.nature.com/articles/s41698-025-01169-0
61. 61. Available from: http://json-schema.org/draft-07/schema#",
62. 62. Available from: the specified schema

Let me first understand the gene list and the context:
- Disease: Astrocytoma
- Cell type: Would primarily be astrocytes/glioblastoma cells and the tumor microenvironment
- The gene list includes many immune-related genes (CD14
