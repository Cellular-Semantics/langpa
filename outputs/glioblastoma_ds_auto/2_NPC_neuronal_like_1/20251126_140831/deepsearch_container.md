# Gene Program Markdown Report

## Context
- Cell type: malignant glioma cells, including glioblastoma (GBM) and glioma stem cells (GSCs)
- Disease: glioblastoma multiforme (GBM), malignant glioma
- Tissue: brain, including diffuse midline glioma (DMG) and hemispheric high-grade glioma

## Input Genes
CFAP43, NEGR1, DNAH12, LRRC2, VAT1L, ZNF804B, RBMS3, SLC14A1, GABRA5, ZBBX, ADAMTS18, CFAP52, GRM1, MAP3K19, FHAD1, TCTEX1D1, DNAAF1, DCDC2, AC005165.1, COL21A1, PKHD1, ZNF521, EPB41L4B, ERICH3, PLAGL1, ... (94 total)

## Program: Motile Cilia-Axoneme Assembly Dysregulation
Multiple genes encoding cilia- and flagella-associated proteins (CFAP) and dynein arm components coordinate the assembly and function of axonemal structures. In glioblastoma, dysregulation of this program through mutations in CFAP43, CFAP52, CFAP47, CFAP206, CFAP73, CFAP221, CFAP157, CFAP61, CFAP100, combined with DNAH5, DNAAF1, DRC1, and RSPH1 mutations, impairs ependymal and neural cilia motility. This impairment disrupts cerebrospinal fluid flow and ventricular homeostasis, contributing to hydrocephalus phenotypes observed in familial GBM cases and affecting neural stem cell niche signaling. The primary cilium also serves as a signaling hub for Hedgehog, Wnt, and other developmental pathways critical for neural progenitor maintenance. DCDC2 localization to primary cilia and its interaction with intraflagellar transport (IFT) machinery further implicates cilia dysfunction in neural developmental defects that may predispose to glioma. In GBM cells themselves, primary cilia presence correlates with hedgehog pathway activation and stem-like properties in VHL wild-type tumors, suggesting cilia-dependent signaling drives GSC biology.

**Predicted impacts**
- Impaired cerebrospinal fluid circulation and ventricular enlargement in normal physiology, contributing to hydrocephalus phenotypes in genetic glioma predisposition
- Disrupted sonic hedgehog signaling dependent on primary cilium function, affecting neural stem cell maintenance and GSC properties
- Altered Wnt and other developmental pathway signaling through compromised primary cilia platform
- In GBM context: maintenance of high ciliation rate in VHL-wt tumors correlates with hedgehog pathway addiction and poor progression-free survival
- Dysregulated intraflagellar transport affecting delivery of signaling receptors and effectors to ciliary compartment

**Evidence summary**
Strong evidence from multiple sources establishes that mutations in this cluster of cilia-associated genes cause primary ciliary dyskinesia and hydrocephalus through disrupted axoneme structure and motility. DNAH5 is mutated in 28-53% of PCD families with outer dynein arm defects[1][2]. CFAP43 nonsense mutations segregate with normal-pressure hydrocephalus in familial cases, with knockout mice exhibiting dilated ventricles and ciliary abnormalities[1]. DNAAF1 mutations identified in neural tube defect patients disrupt cytoplasmic preassembly of dynein complexes[3]. DCDC2 localizes to primary cilia and regulates ciliary signaling[39]. Recent evidence demonstrates that primary cilia in VHL-wt renal cancer correlate with hedgehog pathway activation and poor prognosis[45]. In glioblastoma context, primary cilia have been implicated as oncogenic signaling platforms in DMG and are required for hedgehog-dependent GSC properties[48]. The convergence of multiple CFAP, dynein, and IFT genes in this input list with their established roles in ciliary dysfunction suggests this program is highly relevant to both genetic predisposition to glioma (through developmental alterations) and glioma progression (through altered stem cell signaling).

**Atomic biological processes**
- Outer dynein arm assembly and function. Genes: DNAH5, CFAP43, DNAAF1
  - [1]: DNAH5 heavy chain mutations cause outer dynein arm defects in PCD and are responsible for 28% of PCD cases with ODA defects
  - [2]: CFAP43 mutations identified in NPH family with ciliary abnormalities and outer dynein arm defects in knockout mice
- Inner dynein arm assembly and preassembly. Genes: DNAAF1, CFAP47, CFAP206
  - [3]: DNAAF1 mutations disrupted cytoplasmic preassembly of dynein-arm complexes including inner dynein arms
  - [4]: C11orf70 and IFT74 mutations linked to PCD phenotypes affecting IDA stability and assembly
- Radial spoke and central pair apparatus. Genes: DRC1, RSPH1, TTC29
  - [2]: CFAP43 mutations in hydrocephalus associated with ciliary abnormalities including axonemal structure defects
- Intraflagellar transport machinery. Genes: DCDC2, CFAP100
  - [4]: IFT74 exon 2 deletion causes defective motile cilia and links IFT dysfunction to primary ciliopathy phenotypes
  - [39]: DCDC2 is actively transported in cilia in IFT-dependent manner, affecting ciliary architecture

**Atomic cellular components**
- Axonemal microtubule doublets and dynein arms. Genes: DNAH5, CFAP43, DNAAF1, CFAP52, DRC1
  - [2]: Axonemal ultrastructure alterations observed with CFAP43 mutations
  - [1]: Outer dynein arms attached to peripheral A-microtubules mediate ciliary motility
- Primary cilium structure and signaling compartment. Genes: DCDC2, CFAP43, PKHD1
  - [39]: DCDC2 localizes to primary cilium and regulates ciliary length and morphology
  - [45]: Primary cilia in VHL-wt ccRCC maintain high incidence and correlate with hedgehog pathway activation
  - [48]: Primary cilia required for hedgehog signaling and glioma stem cell formation

**Required genes (not in input)**
- Genes: DNAI1, IFT88, IFT172, IFT81, IFT140, DYNC2LI1, KIF3A, CEP290, MKS1, IFT74, WDR19, IFT57, DYNCLI1, PLK4, CPAP, OFD1
  - [3]: IFT172, IFT88, CEP290 identified as ciliary genes associated with neural tube defects
  - [4]: IFT74, WDR19, IFT complexes essential for cilia assembly and function
  - [39]: KIF3A kinesin-2 subunit required for intraflagellar transport

**Program citations**
- [1]: DNAH5 mutations cause PCD with outer dynein arm defects and are frequent (~28-53%) in PCD families
- [2]: CFAP43 nonsense mutations cause familial hydrocephalus with ciliary abnormalities demonstrated by electron microscopy and knockout mouse model
- [3]: DNAAF1 rare mutations in neural tube defects disrupt dynein-arm preassembly and are associated with NTC defects
- [4]: IFT74 and IFT-related genes link primary and motile ciliopathy phenotypes
- [39]: DCDC2 localizes to primary cilium, regulates ciliary length, and activates/represses Shh/Wnt signaling
- [45]: Primary cilia in VHL-wt ccRCC correlate with hedgehog pathway activation and poor progression-free survival
- [48]: Primary cilia required for hedgehog signaling and glioma stem cell formation in brain tumors

## Program: Extracellular Matrix Remodeling and Stiffness
The gene program involving type V and other collagen genes (COL21A1, COL13A1, COL23A1, COL26A1), along with extracellular matrix regulators like POSTN (periostin), ADAMTS18 (ADAMTS metalloproteinase), and THBS1 (thrombospondin-1), coordinately remodel the glioblastoma microenvironment. GBM cells orchestrate ECM composition, density, and mechanical stiffness through upregulation of collagen synthesis, crosslinking, and deposition. Type V collagen (COL5A1) has been identified as a driver of GBM malignancy through the COL5A1-PPRC1-ESM1 axis, activating epithelial-mesenchymal transition-related genes and actin filament remodeling. Increased ECM stiffness (from 0.08 kPa to 119 kPa in experimental systems) produces 5-fold increases in phosphorylated EGFR and 2-fold increases in phosphorylated Akt, broadly activating PI3K-EGFR signaling in GBM tumor cells. The GM-ECM acts as a physical barrier protecting residual glioma cells from adjuvant therapy by preventing drug penetration and immune cell infiltration, while simultaneously promoting glioma stem cell stemness through integrin-ECM signaling and metabolic pathway support. Hyaluronic acid and tenascin-C enrichment in ECM correlates with worse prognosis and shorter survival. POSTN and THBS1 participate in this remodeling either as pro-tumorigenic molecules or as context-dependent regulators depending on cellular source and signaling context.

**Predicted impacts**
- Increased ECM density and stiffness activates PI3K-EGFR signaling, promoting GBM cell proliferation 5-fold at high stiffness
- Physical barrier formation shields residual GBM cells from chemotherapy and immune cell infiltration post-treatment
- Enhanced GSC adherence, stemness maintenance, and self-renewal capacity through integrin-collagen signaling
- Promotion of epithelial-mesenchymal transition phenotype in GBM cells through COL5A1-PPRC1-ESM1 axis
- Altered metabolic adaptation including hypoxia through ECM-mediated barriers to vascular perfusion
- Regulation of angiogenesis - THBS1 as context-dependent inhibitor vs. immune cell-derived pro-tumorigenic factor
- Enhanced migration and invasion through integrin αvβ3 and CDC42/F-actin/YAP-1 pathway activation
- Therapy resistance - increased ECM accumulation impedes drug penetration and immune cell access to tumor cells

**Evidence summary**
Comprehensive evidence demonstrates that glioblastoma cells actively orchestrate ECM remodeling into a tumor-promoting, therapy-resistant microenvironment. COL5A1-driven EMT and the COL5A1-PPRC1-ESM1 axis represent a validated therapeutic target in GBM[19]. Type I collagen and fibronectin enrichment in GM-ECM promotes GSC stemness through Integrin αvβ3 signaling and CDC42/F-actin/YAP-1 pathways[22]. Increased ECM stiffness (119 kPa vs. 0.08 kPa) produces 5-fold increases in pEGFR and 2-fold in pAkt, broadly activating EGFR signaling for proliferation[22]. Hyaluronic acid and tenascin-C abundance in patient samples correlates with poor prognosis and survival[22]. THBS1 plays dual roles - as angiogenesis inhibitor but also as immune cell-secreted pro-tumorigenic factor that regulates T-cell dysfunction[9][12]. The physical barrier formed by dense ECM actively protects residual glioma cells from therapy while neither T cells nor dendritic cells can penetrate dense fibrils[22]. ADAMTS18 and other matrix proteases regulate ECM composition dynamically. The presence of multiple collagen genes (COL21A1, COL13A1, COL23A1, COL26A1) along with POSTN, THBS1, and ADAMTS18 in the input list strongly supports this program's relevance to GBM progression and therapy resistance.

**Atomic biological processes**
- De novo collagen synthesis and deposition. Genes: COL21A1, COL13A1, COL23A1, COL26A1
  - [19]: COL5A1 plays pivotal role in GBM malignancy through collagen deposition and ECM remodeling
  - [22]: Residual glioma cells create and remodel ECM to be more abundant, dense and stiffer through increased collagen expression
- Extracellular matrix crosslinking and stabilization. Genes: ADAMTS18
  - [22]: ECM stiffness increases through collagen accumulation, with elevated stiffness promoting EGFR/PI3K signaling
- ECM-receptor signaling and mechanotransduction. Genes: COL21A1, COL13A1, COL23A1, COL26A1, POSTN
  - [19]: COL5A1 activates PPRC1 and downstream ESM1, promoting actin filament reorganization and EMT
  - [22]: Type I collagen/fibronectin enriched in GM-ECM promotes GSC adherence and proliferation through integrin signaling
- Angiogenesis inhibition and vascular normalization. Genes: THBS1, POSTN
  - [9]: THBS1 identified as angiogenesis inhibitor, with decreased expression associated with cancer progression
  - [12]: THBS1 and THBS2 enhance proliferation, adhesion, migration and invasion of cancer cells while regulating vascular network

**Atomic cellular components**
- Type V collagen fibers. Genes: COL21A1, COL23A1, COL26A1
  - [19]: COL5A1 encodes type V collagen alpha 1 chain, a key component of fibrous collagen in ECM
- Hyaluronic acid and proteoglycan matrix. Genes: POSTN
  - [22]: HA and tenascin-C enrichment in glioma ECM correlates with poor prognosis and disease progression
- Extracellular vesicles and ECM-associated proteins. Genes: THBS1
  - [9]: THBS1 component of extracellular vesicles released by immune cells mediates tumor cell killing

**Required genes (not in input)**
- Genes: COL1A1, COL1A2, COL4A1, COL4A2, FN1, LOXL2, LOXL4, MMPs, MMP-2, MMP-9, TIMP1, TIMP2, VTN, FBN1, SPARC, OPN/SPP1, TIMP3
  - [22]: Col I, Col IV, fibronectin major components of glioma ECM; MMPs regulate ECM remodeling
  - [19]: MMP-2 and MMP-9 expression regulated by COL5A1; essential for ECM remodeling and invasion
  - [11]: OPN/SPP1 expressed by glioblastoma-associated microglia and promotes tumor progression

**Program citations**
- [19]: COL5A1-PPRC1-ESM1 axis drives GBM malignancy through EMT and metastasis; therapeutically targetable
- [22]: Comprehensive review of glioma ECM remodeling in therapy resistance; dense ECM creates physical barrier and immunosuppressive microenvironment
- [9]: THBS1 dual roles in angiogenesis and immune regulation; identified as cancer-promoting or suppressing depending on context
- [12]: THBS1 and THBS2 enhance cancer cell proliferation, adhesion, migration while regulating angiogenesis
- [11]: OPN (SPP1) involved in DNA damage repair in GBM, role of ECM proteins in therapy resistance

## Program: GABAergic Neuron-to-Glioma Synaptic Communication
A recently discovered program of functional, tumor-promoting GABAergic synapses formed between GABAergic interneurons and H3K27M-altered diffuse midline glioma (DMG) cells, mediated by GABA-A receptors. The input genes GABRA5, GABRG3 (encoding α5 and γ3 GABA-A receptor subunits), along with KCNJ3 (encoding GIRK1, a G-protein-gated potassium channel), GRM1 and GRM4 (metabotropic glutamate receptors), and CDH7 (cadherin-7 for cell adhesion) coordinate a depolarizing GABAergic input on DMG cells. In normal development, GABAergic signaling hyperpolarizes neurons through Cl- efflux; however, DMG cells express elevated NKCC1 chloride transporter, resulting in elevated intracellular chloride concentration [Cl-]i. This reversal of the chloride gradient converts GABAergic input into depolarizing current, activating voltage-gated calcium channels (CACNA2D1 encodes auxiliary subunit α2δ-1) and promoting tumor cell proliferation and migration. The GABA-A receptor subunits α3, β3, γ1, γ2 are highly expressed in H3K27M+ DMGs but minimally in IDH wild-type hemispheric GBMs, establishing tumor subtype-specific vulnerability. GRM4 antagonism or knockout improves antitumor immunity by promoting CD8+ T cell, CD4+ T cell, and NK cell activation through cAMP/CREB-mediated interferon-γ production. ADCY8 (adenylyl cyclase 8) couples Ca2+ and cAMP signaling, modulating neuronal activity-dependent plasticity. This program links aberrant neural circuit signaling to glioma progression in a molecular subtype-specific manner.

**Predicted impacts**
- In H3K27M+ DMGs: depolarizing GABAergic currents directly promote tumor cell proliferation and migration through NKCC1-mediated chloride reversal
- Distinction from normal GBM physiology: lorazepam effective only in DMGs, not IDH-WT hemispheric GBMs, providing tumor subtype-specific therapeutic opportunity
- In non-DMG context: GRM4 antagonism promotes antitumor immunity through CD8+ T cell and NK cell activation via cAMP/CREB-IFN-γ axis
- Calcium influx through voltage-gated calcium channels following depolarization activates downstream proliferation and survival signaling
- Potential compensatory metabotropic glutamate receptor signaling through GRM1/4 for cell survival in glioma context
- Synaptic communication between normal neurons and tumor cells creates a novel mechanism of tumor progression distinct from paracrine secretion
- Restoration of hyperpolarizing GABA signaling through NKCC1 inhibition or chloride channel modulation could impair DMG progression

**Evidence summary**
Recently published evidence from Nature identifies functional, growth-promoting GABAergic neuron-to-glioma synapses specifically in H3K27M-altered diffuse midline gliomas[10]. Whole-cell patch-clamp electrophysiology confirms depolarizing GABAergic currents in DMG cells (-49±4.9 mV) but not hemispheric IDH-WT GBM cells (-61.3±7.9 mV)[10]. DMG cells broadly express GABA-A receptor subunits α3, β3, γ1, γ2 and postsynaptic protein components (gephyrin, ARHGEF9, NLGN2) at much higher levels than IDH-WT GBM[10]. The depolarizing phenotype depends on DMG-specific NKCC1 transporter function creating elevated [Cl-]i[10]. Lorazepam selectively blocks growth-promoting effects in DMGs but not IDH-WT GBM, establishing molecular subtype specificity[10]. Optogenetically-driven GABAergic input in vivo promotes DMG growth, confirming functional relevance[10]. In contrast, GRM4 deletion/antagonism improves antitumor immunity across multiple tumor models through enhanced CD8+ T cell, CD4+ T cell, and NK cell activation via cAMP/CREB-mediated IFN-γ production[32]. mGluR1 stimulation promotes survival in GBM through PI3K-Akt/mTOR[35]. The convergence of GABRA5, GABRG3, KCNJ3, GRM1, GRM4, CDH7, and CACNA2D1 in the input list, combined with recent mechanistic discoveries, indicates this program represents a critical and actionable pathway in H3K27M+ DMG biology and potentially immune evasion in other GBM subtypes.

**Atomic biological processes**
- GABAergic postsynaptic receptor assembly and localization. Genes: GABRA5, GABRG3
  - [10]: H3K27M+ DMG cells express GABA-A receptor subunits α3, β3, γ1, γ2, gephyrin, ARHGEF9, NLGN2 - components of GABAergic postsynaptic compartments
- Synaptic current generation and ion homeostasis. Genes: KCNJ3, CACNA2D1
  - [10]: GABAergic input produces depolarizing currents in H3K27M+ DMG cells due to NKCC1-mediated elevated [Cl-]i; depolarization of -49±4.9 mV vs -61.3±7.9 mV in IDH-WT GBM
- Metabotropic glutamate receptor signaling and immune modulation. Genes: GRM1, GRM4, ADCY8
  - [32]: GRM4 perturbation promotes antitumor immunity; GRM4 loss activates NK, CD4+, CD8+ T cells through cAMP/CREB pathway producing IFN-γ
  - [35]: mGluR1 stimulation promotes GBM cell survival through PI3K-Akt/mTOR pathway; multiple mGluR family members regulate glioma progression
- Cell adhesion and synaptic scaffold assembly. Genes: CDH7
  - [10]: Gephyrin (GPHN), ARHGEF9, NLGN2 associated with GABAergic postsynaptic compartments; CDH7 potential synaptic adhesion molecule
- Lorazepam-sensitive GABAergic current blockade. Genes: GABRA5, GABRG3
  - [10]: Lorazepam blocks GABAergic depolarizing currents in H3K27M+ DMG cells but not hemispheric GBM, confirming receptor-mediated mechanism

**Atomic cellular components**
- GABAergic postsynaptic membrane specialization. Genes: GABRA5, GABRG3
  - [10]: Clustering of GABA-A receptors, gephyrin, and associated proteins at postsynaptic membrane in DMG cells
- G-protein-gated potassium channel complex. Genes: KCNJ3
  - [56]: GIRK1 (KCNJ3) forms heteromultimeric GIRK channels coupled to GPCRs; essential for GPCR-mediated hyperpolarization
- Voltage-gated calcium channel complex. Genes: CACNA2D1
  - [55]: α2δ-1 (CACNA2D1) auxiliary subunit increases trafficking of α1 pore-forming subunit to plasma membrane

**Required genes (not in input)**
- Genes: GABRA1, GABRA2, GABRA3, GABRB1, GABRB2, GABRG1, GABRG2, GEPHYRIN, NLGN2, ARHGEF9, NKCC1, GAD65, GAD67, VGAT, Netrin-G1, Latrophilin-3
  - [10]: Additional GABA-A receptor subunits, gephyrin, NLGN2, ARHGEF9 required for GABAergic postsynaptic specialization; NKCC1 essential for chloride homeostasis reversal in DMG
  - [34]: IL-6R and GABA signaling pathway interactions in GBM immune evasion

**Program citations**
- [10]: First demonstration of functional GABAergic neuron-to-glioma synapses in H3K27M+ DMGs; depolarizing currents promote tumor growth via NKCC1
- [32]: GRM4 deletion promotes antitumor immunity through CD8+ T cell and NK cell activation via cAMP/CREB-IFN-γ axis
- [35]: mGluR1 and other metabotropic glutamate receptors regulate glioma survival and progression through multiple pathways
- [56]: KCNJ3/GIRK1 G-protein-gated potassium channels bridge GPCR activation to cellular hyperpolarization
- [55]: CACNA2D1 α2δ-1 subunit overexpression related to GBM malignancy through enhanced calcium channel trafficking

## Program: Glioma Stem Cell Self-Renewal and Differentiation
A program coordinating cancer stem cell maintenance, controlled by genes including ZNF521, ZNF804B, CHD5, BMP6, SATB1-AS1, and PLAGL1, that regulates the balance between GSC self-renewal and differentiation. ZNF117 was recently identified as a genetic regulator controlling GSC differentiation toward oligodendroglial lineage; downregulation of ZNF117 significantly reduced stem cell frequency and promoted differentiation through Notch signaling modulation[52]. ZNF521 and related zinc finger proteins act as chromatin-level regulators of stemness programs. BMP6, a bone morphogenetic protein, acts as a tumor suppressor in GBM by promoting GSC differentiation into non-proliferative astrocyte-like cells, while inhibiting Wnt and Notch pathways that maintain stemness[25]. BMP signaling defines a quiescent GSC population that is relatively resistant to radiation and temozolomide chemotherapy but lacks proliferative capacity, creating a cellular reservoir for tumor recurrence[28]. CHD5, a chromodomain helicase and tumor suppressor downregulated in GBM, plays roles in neural development and gene expression regulation; CHD5 low expression associates with worse prognosis[21][24]. SATB1-AS1, an antisense RNA, may regulate SATB1 (special AT-rich sequence-binding protein), which acts as a chromatin organizer whose phosphorylated form correlates with GBM progression[20][23]. PLAGL1 encodes a zinc finger protein involved in imprinting and developmental regulation potentially relevant to stem cell control. This program mechanistically explains how GSCs resist standard therapies: BMP pathway activation confers relative quiescence and therapy resistance despite increasing DNA repair capacity (MGMT upregulation and ATM activation)[28], while Notch and Wnt pathways maintain proliferative potential and stemness.

**Predicted impacts**
- ZNF117 downregulation or pharmacological targeting promotes GSC differentiation, reducing stem cell frequency and increasing sensitivity to standard chemotherapy
- BMP6 activation induces quiescence without impairing stemness, creating therapy-resistant but non-proliferative GSC reservoir
- Increased MGMT and ATM expression in BMP-activated GSCs confers enhanced DNA damage resistance and chemo-radiotherapy resistance
- CHD5 tumor suppressor function impaired in GBM; restoration could restore differentiation capacity and reduce stemness
- SATB1 chromatin remodeling activity regulates invasive and proliferative phenotypes in GBM through HDAC1 interaction
- Combination of BMP differentiation therapy plus temozolomide improves therapeutic outcome over monotherapy
- Notch and Wnt pathway antagonism through BMP signaling restricts GSC self-renewal capacity
- GSC plasticity maintained through multiple regulatory nodes (ZNF, BMP, SATB1, CHD5) allowing adaptation to microenvironmental changes

**Evidence summary**
Recent studies establish the importance of stemness regulation in GBM therapy resistance. ZNF117 was identified as a genetic regulator of GSC differentiation through Notch signaling, with downregulation significantly reducing stem cell frequency in vitro and extending survival of tumor-bearing mice to >100 days[52]. ZNF117 downregulation sensitized GSCs to temozolomide, and combination therapy proved more effective than monotherapy[52]. BMP signaling defines a distinct quiescent GSC population marked by elevated ID1 expression that is relatively resistant to radiation and temozolomide despite low proliferation rates[28]. BMP4 treatment increases MGMT and ATM phosphorylation in GSCs, enhancing DNA repair[28]. Analysis of patient biopsies shows selection for pSmad1+ (BMP-signaling) cells following chemoradiation[28]. CHD5 low expression is associated with worse prognosis in GBM and LGG; CHD5 knockdown promotes proliferation and migration[21][24]. SATB1 phosphorylation status correlates with GBM progression and invasiveness through HDAC1-dependent mechanisms[20]. BMP2 and BMP4 antagonize Wnt and Notch pathways maintaining CSC stemness[25]. The presence of ZNF521, ZNF804B, CHD5, BMP6, SATB1-AS1, and PLAGL1 in the input list, combined with recent mechanistic discoveries linking each to GSC biology, strongly supports this program's central role in GBM stem cell control and therapy resistance.

**Atomic biological processes**
- Zinc finger transcription factor-mediated stemness regulation. Genes: ZNF521, ZNF804B, PLAGL1
  - [52]: ZNF117 downregulation significantly reduces GSC stem cell frequency and promotes differentiation through Notch signaling
  - [21]: CHD5 chromodomain helicase regulates gene expression and has tumor suppressor function in neural development
- BMP-SMAD signaling axis in GSC differentiation. Genes: BMP6
  - [25]: BMP4 reduces GSC self-renewal and promotes astrocytic differentiation; BMPs inhibit Notch and Wnt signaling
  - [28]: BMP pathway activation demarcates slow-cycling, long-term label-retaining quiescent GSC population with enhanced DNA repair
- Chromatin remodeling and gene regulation. Genes: CHD5, SATB1-AS1
  - [21]: CHD5 knockdown promoted proliferation and migration; CHD5 low expression associated with worse prognosis in GBM
  - [20]: SATB1 chromatin organizer; phospho-SATB1 interacts with HDAC1 to regulate gene expression and GBM cell phenotype
- Notch signaling modulation in stemness. Genes: ZNF521, BMP6
  - [52]: ZNF117 controls GSC differentiation through interaction with JAG2 and Notch signaling regulation
  - [25]: BMPs inhibit Notch signaling, restricting GSC proliferation and promoting differentiation
- DNA damage response and therapy resistance. Genes: CHD5, BMP6
  - [28]: BMP4 treatment increases MGMT and ATM phosphorylation in GSCs, enhancing DNA repair and temozolomide/radiation resistance
  - [52]: ZNF117-mediated GSC differentiation sensitizes GBM to temozolomide chemotherapy

**Atomic cellular components**
- Chromatin regulatory complexes. Genes: CHD5, SATB1-AS1
  - [21]: CHD5 chromodomain helicase DNA binding protein; SATB1 acts as chromatin organizer
- BMP receptor signaling complexes. Genes: BMP6
  - [25]: BMP ligands bind type I and type II serine/threonine kinase receptors; SMAD1/5/8 phosphorylation and translocation initiates signaling
- Transcriptional regulatory complexes. Genes: ZNF521, ZNF804B, SATB1-AS1
  - [20]: Phospho-SATB1 interacts with HDAC1; ZNF proteins form zinc finger transcription factor complexes

**Required genes (not in input)**
- Genes: ZNF117, SOX2, NESTIN, OLIG2, JAG2, NOTCH1, NOTCH3, WNT3, WNT7B, TCF3, SMAD1, SMAD4, ID1, ID3, HDAC1, BMP2, BMP4, BMPR1A, BMPR1B, ALK2, ALK3, MGMT, ATM, p53
  - [52]: ZNF117, SOX2, NESTIN, OLIG2 core GSC markers; JAG2, Notch pathway essential for stemness
  - [28]: SMAD1/4, ID1/3, BMPR essential for BMP signaling; MGMT, ATM DNA repair genes activated by BMP
  - [25]: BMP2, BMP4, BMPRs, TCF/LEF, WNT antagonism essential components

**Program citations**
- [52]: ZNF117 controls GSC differentiation; downregulation extends survival and sensitizes to temozolomide
- [28]: BMP signaling defines quiescent GSCs with enhanced DNA repair and therapy resistance; BMP4 increases MGMT and ATM
- [21]: CHD5 knockdown promotes GBM proliferation and migration; low expression associated with worse prognosis
- [20]: Phospho-SATB1 associates with GBM progression through HDAC1 interaction
- [25]: BMP signaling inhibits Notch and Wnt; promotes GSC differentiation and sensitizes to chemotherapy

## Program: Immune Evasion and T-Cell Exhaustion
Multiple genes coordinate suppression of antitumor immunity in GBM through several mechanisms. IL6R (interleukin-6 receptor) enables IL-6-STAT3 signaling that promotes T-cell exhaustion and immune suppression[31][34]. BANK1 (B cell scaffold protein with ankyrin repeats) modulates B cell and immune signaling through interactions with tyrosine kinases and toll-like receptors[33]. THBS1 (thrombospondin-1) limitsantitumor immunity through CD47-dependent regulation and differentially regulates sensitivity of malignant cells to genotoxic stress[9]. In the glioblastoma microenvironment, IL-6 is overexpressed, correlating with tumor grade and poor survival[31]. IL-6 signaling through gp130 recruits and activates the JAK-STAT3 pathway, which promotes anti-apoptotic signaling (Bcl-2, Bcl-xL, Mcl-1) and inhibits T-cell effector functions[31]. IL-10-producing myeloid cells (characterized by HMOX1+ phenotype) drive T-cell exhaustion through IL-10-STAT3-BLIMP-1 axis[50]. Hypoxia (common in GBM) elevates HIF-1α and HIF-2α, which promote T-cell exhaustion by depriving glucose availability and forcing alternative metabolic pathways (OXPHOS, one-carbon metabolism) that impair T-cell effector function[51][53]. HMOX1+ mesenchymal-like tumor regions spatially localize with exhausted T cells[50]. The program explains why standard immunotherapy approaches fail: the glioma microenvironment actively generates and maintains an exhausted T-cell state through IL-6, IL-10, hypoxia, and metabolic competition. Recent studies show JAK/STAT pathway inhibition rescues T-cell functionality both in ex vivo and in vivo models[50].

**Predicted impacts**
- IL-6-STAT3 signaling activation suppresses T-cell effector functions and promotes anti-apoptotic signaling in both GBM cells and immune cells
- IL-10-producing myeloid cells spatially localized to mesenchymal tumor regions establish local immunosuppressive microenvironment
- Glucose deprivation in hypoxic tumor core forces T-cells to repress glycolysis-dependent functions (IFN-γ production, proliferation)
- THBS1-CD47 axis limits macrophage and NK cell cytotoxicity through 'don't eat me' signaling
- BANK1 modulation of BCR and TLR signaling affects both B cell and dendritic cell responses
- Persistent antigen exposure combined with hypoxia and IL-10 drives irreversible T-cell exhaustion phenotype
- JAK/STAT3 pathway inhibition can rescue T-cell functionality and restore antitumor immunity
- Standard checkpoint inhibitors ineffective without addressing underlying IL-6/IL-10/hypoxia-driven exhaustion mechanisms

**Evidence summary**
The glioblastoma microenvironment actively suppresses antitumor immunity through multiple reinforcing mechanisms. IL-6 mRNA expression significantly correlates with glioma grade and is markedly elevated in GBM vs. lower-grade gliomas, with high IL-6 correlating with shortened survival[31]. IL-6-STAT3 signaling promotes anti-apoptotic protein expression (Bcl-2, Bcl-xL, Mcl-1) and inhibits T-cell differentiation[31]. Recent spatially-resolved transcriptomics and scRNAseq studies identified HMOX1+ myeloid cells as drivers of CD8+ T-cell exhaustion through IL-10-STAT3-BLIMP-1 axis; these cells are spatially enriched in mesenchymal tumor regions[50]. JAK/STAT pathway inhibition rescued T-cell functionality in both ex vivo neocortical GBM models and in vivo[50]. Hypoxia in GBM activates HIF-1α/HIF-2α, which suppress glucose utilization in T-cells and promote exhaustion through multiple non-HIF mechanisms[51][53]. Glucose competition between metabolically active GBM tumors and infiltrating T-cells impairs T-cell effector functions[53]. THBS1 acts as angiogenesis inhibitor but also suppresses immunity through CD47 engagement[9]. BANK1 modulates immune signaling through BCR, CD40, and TLR pathways[33]. The convergence of IL6R with immune exhaustion evidence, combined with THBS1 and BANK1 involvement in immune regulation, strongly establishes this program's central role in GBM's immunosuppressive microenvironment. The presence of these genes in the input list, along with recent mechanistic studies, indicates multiple targetable nodes in this program.

**Atomic biological processes**
- IL-6-STAT3 signaling cascade. Genes: IL6R
  - [31]: IL-6 activates JAK-STAT3 pathway; IL-6 mRNA expression significantly greater in GBM than lower-grade gliomas and correlates with poor survival
  - [34]: IL-6 activates STAT-3 signaling in GBM cells; IL-6 trans-signaling promotes pro-inflammatory responses
- IL-10-STAT3-BLIMP-1 axis driving T-cell exhaustion. Genes: IL6R
  - [50]: HMOX1+ myeloid cells produce IL-10; IL-10-STAT3-BLIMP-1 signaling axis drives CD8+ T-cell exhaustion in glioblastoma
  - [53]: IL-10 and TGF-β signaling in exhausted T-cells; chronic antigen stimulation drives exhaustion
- B cell receptor signaling and immune checkpoint regulation. Genes: BANK1
  - [33]: BANK1 binds Src family kinases Lyn and Blk; modulates BCR signaling, CD40 signaling, TLR signaling affecting immune responses
- CD47-mediated 'don't eat me' signaling. Genes: THBS1
  - [9]: THBS1 limits antitumor immunity through CD47-dependent regulation of innate and adaptive immune cells
- Glucose deprivation and metabolic exhaustion. Genes: IL6R
  - [53]: Hypoxia and glucose deprivation force T-cells to reprogram metabolism toward OXPHOS or autophagy, impairing effector function and promoting exhaustion
  - [50]: Exhausted T-cells have compromised ability to utilize aerobic glycolysis; glucose competition between tumor and immune cells
- Hypoxia-mediated HIF-STAT3 cross-talk. Genes: IL6R
  - [51]: HIF-1α and HIF-2α stabilized in hypoxic GBM microenvironment; promote T-cell exhaustion through multiple mechanisms
  - [53]: Hypoxia drives T-cell exhaustion beyond HIF-1α axis; involves both hypoxia and chronic antigen stimulation

**Atomic cellular components**
- IL-6 receptor complex (IL-6R, gp130). Genes: IL6R
  - [34]: IL-6R expressed in leukocytes and hepatocytes; gp130 expressed in all nucleated cells; trans-signaling through soluble IL-6R
- B cell scaffold complex (BANK1-LYN-BLK). Genes: BANK1
  - [33]: BANK1 acts as adaptor/scaffold connecting Src family kinase LYN/BLK to signaling substrates and receptors
- Immune checkpoint ligands (CD47). Genes: THBS1
  - [9]: THBS1 regulates CD47; affects innate immune cell activation

**Required genes (not in input)**
- Genes: IL6, IL10, TGF-β, PD-L1, PD-L2, LAG-3, TIM-3, CTLA-4, STAT3, JAK1, JAK2, HIF-1α, HIF-2α, BLIMP-1 (PRDM1), gp130, HMOX1, ARG1, IDO1, CD47, SIRP-α, GLUT1, LDHA, ENO1, LDLR, VEGF, PDGF
  - [31]: IL-6, IL-10, TGF-β core cytokines; STAT3, JAK kinases essential for signaling
  - [50]: PD-1, CTLA-4, LAG-3, TIM-3 exhaustion markers; BLIMP-1 transcriptional repressor of effector function
  - [51]: HIF-1α, HIF-2α, VEGF, PDGF hypoxia response genes
  - [53]: GLUT1, LDHA, ENO1 glycolytic enzymes; metabolic competition for glucose

**Program citations**
- [31]: IL-6 mRNA expression elevated in GBM, correlates with grade and poor prognosis; IL-6-STAT3 promotes T-cell exhaustion
- [34]: IL-6 signaling in glioblastoma; trans-signaling mechanism and autocrine/paracrine effects
- [50]: HMOX1+ myeloid cells drive T-cell exhaustion through IL-10-STAT3-BLIMP-1; JAK/STAT inhibition rescues function
- [51]: HIF signaling in GBM angiogenesis and immune evasion; hypoxia-mediated therapy resistance
- [53]: Hypoxia and glucose deprivation drive T-cell exhaustion through metabolic reprogramming
- [9]: THBS1 dual roles in angiogenesis and immune suppression through CD47 engagement
- [33]: BANK1 scaffold function in BCR, CD40, TLR signaling

## Program: Calcium Signaling and Neuronal Activity Coupling
A program coupling neuronal/synaptic activity to cellular responses through calcium-dependent signaling, coordinated by genes including ADCY8 (adenylyl cyclase 8), KCNJ3 (GIRK potassium channels), CACNA2D1 (calcium channel auxiliary subunit), and potentially GRM1/4 (metabotropic glutamate receptors). ADCY1 and ADCY8 are the only Ca2+-stimulated adenylyl cyclases in the brain[30]. ADCY8 is regulated exclusively by Ca2+ (EC50 ~500-800 nM), inactive in resting neurons but activated during stimulation, whereas ADCY1 is partially constitutively activated at basal Ca2+ (EC50 ~100 nM) and additionally regulated by GPCRs[30]. ADCY1 and ADCY8 show distinct functions in regulating synaptic plasticity: ADCY1 required for both initial and reversal memory formation, whereas ADCY8 required only for reversal memory[30]. KCNJ3/GIRK1 channels are coupled to GPCRs and translate receptor activation into membrane hyperpolarization through potassium efflux, modulating neuronal excitability and synaptic transmission[56]. CACNA2D1 α2δ-1 increases voltage-gated calcium channel trafficking and function; its overexpression is related to GBM malignancy and promotes proliferation and migration through TLR-4-NF-κB-Sp1 signaling[55]. In glioma context, aberrant calcium signaling through these components promotes tumor cell proliferation and migration, potentially mimicking or interacting with neuron-like activity patterns observed in GBM. This program links neuronal activity patterns to glioma progression through molecular mechanisms normally involved in synaptic plasticity and learning.

**Predicted impacts**
- Activity-dependent cAMP production through ADCY8 modulates synaptic transmission, learning, and memory formation
- ADCY1 required for both initial and reversal memory; ADCY8 specialized for reversal learning, suggesting distinct roles in cognitive flexibility
- KCNJ3-mediated hyperpolarization opposes excitation; dysfunction or downregulation would enhance excitability and calcium influx
- Enhanced voltage-gated calcium channel trafficking through CACNA2D1 overexpression increases intracellular calcium and promotes proliferation/migration signaling
- TLR-4-mediated CACNA2D1 upregulation in GBM links inflammatory signaling to calcium channel availability
- Aberrant calcium signaling in GBM may mimic or exploit normal neuronal activity-dependent processes for tumor progression
- Calcium-cAMP coupling through ADCY8 modulates diverse downstream effects (PKA, EPAC, MAPK pathways)
- Potential therapeutic targeting of aberrant calcium signaling in GBM through calcium channel antagonists or ADCY inhibitors

**Evidence summary**
ADCY1 and ADCY8 are the exclusive Ca2+-stimulated adenylyl cyclases in the brain, with distinct biochemical properties and functional roles[30]. ADCY8 has higher EC50 for Ca2+ (~500-800 nM) compared to ADCY1 (~100 nM), leading to differential activation dynamics in resting vs. stimulated neurons[30]. In hippocampus, ADCY1 contributes ~50% of Ca2+-stimulated cAMP production while ADCY8 contributes ~30%, establishing ADCY1 as the primary stimulus-response element[30]. ADCY1-knockout mice show protocol-dependent deficits in LTP and impaired both initial and reversal memory formation, while ADCY8-knockout mice show normal LTP but specifically impaired reversal memory[30]. KCNJ3/GIRK1 is the primary G-protein-gated potassium channel in brain, coupling GPCR activation to membrane hyperpolarization through Ca2+-independent and Ca2+-dependent mechanisms[56]. CACNA2D1 α2δ-1 overexpression associates with increased GBM malignancy; TLR-4 activation increases CACNA2D1 expression through NF-κB/Sp1 signaling, promoting GBM proliferation and migration[55]. AC8 associates dynamically with lipid rafts and actin cytoskeleton, directly orchestrating its microenvironment through cAMP production[27]. The convergence of ADCY8, KCNJ3, and CACNA2D1 in the input list, combined with their distinct roles in neural activity, synaptic plasticity, and calcium signaling, indicates this program represents a link between neuronal physiology and glioma progression.

**Atomic biological processes**
- Ca2+-stimulated cAMP production. Genes: ADCY8
  - [30]: ADCY1 and ADCY8 exclusively account for Ca2+-stimulated adenylyl cyclase activity in brain; differential Ca2+ sensitivities (100 nM vs 500-800 nM)
- Long-term potentiation and synaptic plasticity. Genes: ADCY8, KCNJ3
  - [30]: ADCY1 required for LTP formation; ADCY8 required for reversal memory but shows normal LTP following HFS
- GPCR-mediated membrane hyperpolarization. Genes: KCNJ3
  - [56]: GIRK1 (KCNJ3) couples GPCRs to potassium efflux and membrane hyperpolarization; essential for parasympathetic cardiac regulation and neuronal inhibition
- Voltage-gated calcium channel trafficking and function. Genes: CACNA2D1
  - [55]: CACNA2D1 α2δ-1 increases trafficking of α1 pore-forming subunit to plasma membrane; overexpression in GBM promotes proliferation/migration
- TLR-4-mediated calcium channel regulation. Genes: CACNA2D1
  - [55]: TLR-4 activation increases CACNA2D1 expression through NF-κB/Sp1 pathway; elevated α2δ-1 promotes GBM proliferation and migration

**Atomic cellular components**
- Adenylyl cyclase complex. Genes: ADCY8
  - [27]: AC8 associates with lipid rafts and actin cytoskeleton; directly controls its micro-environment through cAMP production
  - [30]: ADCY8 Ca2+-stimulated enzyme; represents one of two sole Ca2+-stimulated ACs in brain
- G-protein-gated inwardly rectifying potassium channel complex. Genes: KCNJ3
  - [56]: GIRK1 (KCNJ3) heterodimerizes with other GIRK subunits; couples to opioid, cannabinoid, GABA-B receptors
- Voltage-gated calcium channel complex (Cav channel). Genes: CACNA2D1
  - [55]: CACNA2D1 α2δ-1 auxiliary subunit; increases trafficking and stabilization of pore-forming α1 subunit

**Required genes (not in input)**
- Genes: ADCY1, CALM, CALMODULIN-BINDING, CaMKII, CaMKIV, CREB, PKA, EPAC, GIRK2, GIRK3, GIRK4, GPCR-family, M2-receptors, Opioid-receptors, Cannabinoid-receptors, GABA-B-receptors, Gq-protein, Gi/o-proteins
  - [30]: ADCY1, CaMKII, CaMKIV, CREB required for LTP and memory; PKA, EPAC downstream effectors
  - [56]: GIRK2, GIRK3, GIRK4 form heteromultimeric complexes with GIRK1; Gi/o-proteins mediate GPCR coupling
  - [27]: Calmodulin, actin cytoskeleton proteins required for AC8 function

**Program citations**
- [30]: ADCY1/ADCY8 sole Ca2+-stimulated ACs in brain; distinct functions in synaptic plasticity and memory
- [56]: KCNJ3/GIRK1 primary G-protein-gated potassium channel; couples GPCR to hyperpolarization
- [55]: CACNA2D1 α2δ-1 overexpression in GBM promotes proliferation/migration; TLR-4 regulation
- [27]: AC8 directly controls its microenvironment through association with cytoskeleton and cAMP production

## Program: Cell Adhesion Molecule-Mediated Neural Development and Migration
A program involving cell adhesion molecules NEGR1 (neuronal growth regulator 1), CDH7 (cadherin-7), and potentially NRG3 (neuregulin 3) that regulate neural cell-cell interactions, cortical layering, brain development, and cellular migration. NEGR1 belongs to the IgLON superfamily of cell adhesion molecules and is involved in cortical layering[13][16]. Negr1-knockout mice show neuroanatomical abnormalities including ventricle enlargement, decreased whole brain volume, reduced corpus callosum volume, reduced globus pallidus, and diminished hippocampus[13][16]. NEGR1 regulates neuronal outgrowth, arborization, and synaptogenesis through FGFR2 signaling pathway; NEGR1-deficient hippocampal neurons exhibit large F-actin-rich protrusions with diffuse lamellopodia and increased filopodia[13]. Negr1-deficient mice show decreased parvalbumin-positive inhibitory interneurons in hippocampus, indicating role in E/I balance[13][16]. In psychiatric disorder models, NEGR1 dysfunction associates with schizophrenia, autism, ADHD, and depression phenotypes. CDH7 (cadherin-7) is a calcium-dependent cell-cell adhesion glycoprotein involved in notochord development[57]; cadherin-7 function is required for normal development of zebrafish notochord, with knockdown producing undulating body phenotype[57]. Cadherins mediate cell-cell adhesion primarily through homophilic interactions. NRG3, a neuregulin EGF family ligand for ErbB4 receptor tyrosine kinase, plays pleotropic roles in neurodevelopment including cortical cell migration and patterning[18]. NRG3 expression is developmentally regulated and pathologically increased in schizophrenia; rs10748842 SNP strongly predicts brain NRG3 expression and schizophrenia risk[18]. NRG1 enhances L1 (cell adhesion molecule) expression in glioma cells and promotes migration[46]; similar NRG-L1 interactions likely apply to NRG3. In glioblastoma context, dysregulation of these adhesion molecules could impair normal neural development (increasing glioma susceptibility) or enhance glioma cell migration and invasiveness through altered cell-cell interactions and mechanotransduction.

**Predicted impacts**
- NEGR1 dysfunction impairs normal brain development; Negr1-knockout phenotype (ventricle enlargement, corpus callosum reduction) resembles abnormalities seen in glioma-predisposition syndromes
- Reduced parvalbumin-positive interneurons in NEGR1-deficient brain suggests E/I imbalance may predispose to aberrant neural development
- CDH7 essential for notochord development; cadherin dysregulation could impair normal CNS development and alter cellular interactions
- NRG3 increased expression in schizophrenia suggests dysregulation of developmental patterning and migration pathways
- In glioblastoma context: NRG3 upregulation may promote glioma migration through enhanced ErbB4-FAK-focal adhesion signaling, similar to NRG1-L1 mechanism
- Altered cell adhesion molecule expression in GBM enhances epithelial-to-mesenchymal transition and invasive potential
- Loss of NEGR1 adhesion function could disrupt contact inhibition and normal tissue architecture
- NRG3-ErbB4 pathway dysregulation may promote both neural developmental alterations predisposing to glioma AND glioma progression through enhanced migration

**Evidence summary**
NEGR1 is a developmentally important cell adhesion molecule whose deletion produces neuroanatomical abnormalities relevant to multiple psychiatric disorders and potentially to glioma predisposition[13][16]. Negr1-knockout mice show ventricle enlargement, reduced brain/hippocampus/corpus callosum volumes, and decreased parvalbumin+ interneurons indicating E/I imbalance[13][16]. NEGR1 promotes neurite outgrowth through FGFR2 signaling and is essential for normal cortical layering and brain development[13]. CDH7 is a classical cadherin required for proper notochord development; cdh7 morphant zebrafish show severe notochord disruption[57]. NRG3, an EGF family neuregulin ligand for ErbB4, plays critical roles in cortical cell migration and patterning[18]. NRG3 expression is developmentally regulated and pathologically elevated in schizophrenia; rs10748842 SNP strongly predicts brain NRG3 levels and schizophrenia risk[18]. NRG1 (close NRG3 ortholog) enhances L1 expression in glioma cells and promotes migration; NRG1 siRNA downregulates L1 in GBM cell lines[46]. ErbB receptor inhibitors combined with NRG1 inhibit glioma cell migration[46]. The presence of NEGR1, CDH7, and NRG3 in the input list, combined with their established roles in neural development and the known importance of developmental aberrations in glioma predisposition, suggests this program represents both developmental vulnerabilities and mechanisms of glioma invasion.

**Atomic biological processes**
- Cell-cell adhesion through homophilic interactions. Genes: NEGR1, CDH7
  - [13]: NEGR1 involved in cortical layering and neural cell adhesion; essential for normal brain morphology
  - [57]: Cadherin-7 mediates calcium-dependent cell-cell adhesion primarily through homophilic interactions
- Neuronal outgrowth and neurite morphogenesis. Genes: NEGR1
  - [13]: NEGR1 regulates neuronal outgrowth, arborization, and synaptogenesis via FGFR2 signaling; NEGR1-deficiency increases neurite number/length/branching
- Cortical cell migration and patterning. Genes: NRG3
  - [18]: NRG3 plays critical roles in neurodevelopment including cortical cell migration and patterning; dysregulation associated with schizophrenia
  - [46]: NRG1 regulates L1 expression in glioma cells and promotes migration; NRG3 likely has similar mechanism
- ErbB4 receptor signaling in neural development. Genes: NRG3
  - [18]: NRG3 is ligand for ErbB4 receptor tyrosine kinase; plays pleiotrophic roles in neurodevelopment
  - [46]: ErbB receptor activation by NRG1 enhances cell motility through focal adhesion kinase activation
- Excitatory-inhibitory balance in neural circuits. Genes: NEGR1
  - [13]: NEGR1-deficiency results in decreased parvalbumin-positive inhibitory interneurons; E/I imbalance associated with social impairment

**Atomic cellular components**
- IgLON cell adhesion molecule family. Genes: NEGR1
  - [13]: NEGR1 belongs to immunoglobulin (IgLON) superfamily of cell adhesion molecules
- Classical cadherin adhesion complex. Genes: CDH7
  - [57]: CDH7 classical type cadherin mediating calcium-dependent cell-cell adhesion
- Neuregulin-ErbB signaling complex. Genes: NRG3
  - [18]: NRG3-ErbB4 ligand-receptor pair; dysregulated in schizophrenia and neurodevelopmental disorders

**Required genes (not in input)**
- Genes: FGFR2, GDNF, NCAM, L1, N-cadherin, E-cadherin, P-cadherin, ErbB4, ErbB3, ErbB2, FAK, SRC, PAX6, Reelin, RELN, DISC1, PV+ markers, GABAergic markers
  - [13]: FGFR2 upstream signaling for NEGR1; NCAM, cadherins essential for neural development
  - [18]: ErbB4, ErbB3, Pax6 required for NRG3 function in cortical development
  - [46]: FAK, SRC downstream signaling for ErbB-mediated migration in glioma

**Program citations**
- [13]: NEGR1 required for normal brain development; deletion produces neuroanatomical abnormalities and behavioral deviations
- [16]: Negr1-/- mice endophenotype related to psychiatric disorders; neuroanatomical abnormalities include enlarged ventricles
- [57]: CDH7 essential for zebrafish notochord development; cadherin family mediates cell adhesion
- [18]: NRG3 plays critical roles in neurodevelopment; pathologically increased in schizophrenia
- [46]: NRG1 enhances L1 expression in glioma cells; promotes migration through ErbB receptor signaling

## Program: Metabolic Adaptation and Nutrient Uptake
A program involving solute carrier (SLC) transporter genes including SLC14A1 (urea transporter), SLC47A2 (MATE2 organic cation/H+ antiporter), and SLC22A3 (organic cation transporter 3) that regulate cellular nutrient uptake, metabolic homeostasis, and tumor progression. SLC14A1 acts as a tumor suppressor through multiple mechanisms: at the plasma membrane, it prevents accumulation of arginine and urea by facilitating their cellular export; in the nucleus, it recruits HDAC1 to transrepress oncometabolite genes (HK2, DEGS1), maintaining metabolic homeostasis and suppressing mTOR signaling[37][40]. SLC14A1 downregulation through promoter hypermethylation is common in urothelial carcinoma and prostate cancer and associates with poor prognosis[37][40]. Functionally, SLC14A1 overexpression inhibits cell proliferation, metastasis, and xenograft growth in vivo[37][40]. SLC14A1 prevents accumulation of arginine in ASS1-deficient cancers and enhances mitochondrial fusion and aerobic respiration while inhibiting glycolysis[37]. SLC47A2 and SLC22A3 represent alternative solute transport systems whose dysregulation in GBM could affect neurotransmitter and metabolite homeostasis. In GBM context, glioma cells exhibit reprogrammed metabolism favoring lipogenesis (driven by SREBP-1 activation through EGFR/PI3K/AKT and glutamine-glucose crosstalk)[44], increased glycolysis despite adequate oxygen (Warburg effect), and altered amino acid metabolism. Loss of normal SLC14A1 expression would fail to constrain these metabolic alterations, allowing accumulation of oncometabolites and enabling mTOR-mediated proliferation. The presence of multiple nutrient transporters in the input list suggests glioblastoma cells exploit altered metabolic transport to support rapid growth.

**Predicted impacts**
- SLC14A1 loss in GBM allows accumulation of arginine and other oncometabolites, activating mTOR-dependent proliferation
- Impaired OXPHOS and mitochondrial fusion through SLC14A1 downregulation shifts metabolism toward glycolysis (Warburg effect)
- Enhanced HK2 and DEGS1 expression (oncometabolite genes) when nuclear SLC14A1 is absent
- Altered cell cycle progression through impaired CDK1/CCNB1 inhibition when SLC14A1 is low
- Enhanced MMP-9 expression and invasion when mTOR pathway is activated through SLC14A1 loss
- SLC47A2 and SLC22A3 dysregulation could impair neurotransmitter/metabolite homeostasis specific to CNS tissue
- SLC14A1 restoration through epigenetic therapy (HDAC inhibitors) could restore metabolic homeostasis and impair GBM growth
- Synergy between SLC14A1 restoration and mTOR inhibitors or chemotherapy through metabolic constraint

**Evidence summary**
SLC14A1 has emerged as a novel tumor suppressor in urothelial carcinoma and prostate cancer through dual mechanisms: membranous SLC14A1 prevents oncometabolite accumulation while nuclear SLC14A1 recruits HDAC1 to repress oncometabolite genes[37][40]. SLC14A1 downregulation correlates with poor prognosis in urothelial cancer (two cohorts: n=340 UTUC, n=295 UBUC) and prostate cancer, with epigenetic silencing (promoter hypermethylation) contributing to loss of expression[37][40]. Functionally, SLC14A1 overexpression inhibits proliferation and metastasis in vitro and suppresses xenograft tumor growth in vivo[37][40]. SLC14A1 prevents accumulation of arginine and urea, enhancing mitochondrial fusion and OXPHOS while inhibiting glycolysis[37]. SLC14A1-mediated metabolic reprogramming inhibits mTOR signaling and reduces CDK1/CCNB1 and MMP-9 expression[37][40]. In arginine-deprived conditions, SLC14A1 sensitizes ASS1-deficient tumors to arginine deprivation therapy[37]. The presence of SLC14A1 combined with SLC47A2 and SLC22A3 in the input list, along with evidence that GBM exhibits metabolic reprogramming toward lipogenesis and glycolysis, suggests this transporter program is relevant to GBM metabolic adaptation and therapy resistance.

**Atomic biological processes**
- Amino acid transporter-mediated cellular export. Genes: SLC14A1
  - [37]: SLC14A1 membranous form facilitates export/prevention of arginine and urea accumulation in UC and PC
  - [40]: SLC14A1 overexpression inhibits CDK1/CCNB1 cell cycle pathway and mTOR/MMP-9 signaling in prostate cancer
- Nuclear SLC14A1-HDAC1 transcriptional repression. Genes: SLC14A1
  - [37]: Nuclear SLC14A1 recruits HDAC1/SIN3A to transrepress HK2 and DEGS1 oncometabolite genes
- Mitochondrial OXPHOS vs glycolysis switch. Genes: SLC14A1
  - [37]: SLC14A1 enhances mitochondrial fusion and aerobic respiration; inhibits glycolysis through transcriptional effects
- mTOR pathway inhibition through metabolic constraint. Genes: SLC14A1
  - [37]: SLC14A1 prevents arginine/urea accumulation; reduced arginine concentrations inhibit mTOR signaling in vitro and in vivo
  - [40]: SLC14A1 overexpression suppresses CDK1/CCNB1 and mTOR/MMP-9 pathways
- Organic cation/neurotransmitter transport. Genes: SLC47A2, SLC22A3
  - [37]: SLC47A2 and SLC22A3 represent alternative organic cation transport systems

**Atomic cellular components**
- Plasma membrane urea/solute transporter. Genes: SLC14A1
  - [37]: SLC14A1 membrane form functions as urea transporter; membranous SLC14A1 plays tumor suppressive role
  - [40]: SLC14A1 encoded B-type urea transporter; located on chromosome 18q12.3
- HDAC1 chromatin remodeling complex. Genes: SLC14A1
  - [37]: SLC14A1 recruits HDAC1 and SIN3A to promoters for transcriptional repression
- Organic cation transporter family. Genes: SLC47A2, SLC22A3
  - [37]: SLC47A2 (MATE2) and SLC22A3 (OCT3) alternative organic ion transport systems

**Required genes (not in input)**
- Genes: mTOR, KRAS, MAPK, EGFR, PI3K, AKT, SREBP-1, FASN, ACC1, SCD1, GLS, ASS1, ARG1, ARG2, ODC1, ALDH3B1, ENO1, LDHA, PFKL, HK2, DEGS1, HDAC1
  - [37]: mTOR, ARG metabolic genes, HDAC1, HK2, DEGS1 downstream targets of SLC14A1
  - [44]: SREBP-1, FASN, ACC, SCD1, GLS genes driving GBM lipogenesis and glutaminolysis

**Program citations**
- [37]: SLC14A1 dual-function tumor suppressor through plasma membrane and nuclear mechanisms in urothelial carcinoma
- [40]: SLC14A1 downregulation in prostate cancer activates CDK1/CCNB1 and mTOR pathways

## Bibliography
1. Yoshiro M, Shintaro Y, Akira K, Chisei S, Hiroyuki M, Naohiro Y, et al.. Nonsense mutation in . Neurology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6598815/
2. Nada H, Heike O, Judit H, Maimoona AZ, Manfred F, Niki TL, et al.. DNAH5 mutations are a common cause of primary ciliary dyskinesia with outer dynein arm defects.. American journal of respiratory and critical care medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2662904/
3. Chunyue M, Qian J, Huili L, Qin Z, Baoling B, Yihua B, et al.. Mutations in the Motile Cilia Gene DNAAF1 Are Associated with Neural Tube Defects in Humans.. G3 (Bethesda, Md) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5068950/
4. Available from: https://discovery.ucl.ac.uk/10063629/1/Fassad_Thesis.pdf
5. Available from: https://en.wikipedia.org/wiki/DNAH5
6. Available from: https://patents.google.com/patent/US20210363525A1/en
7. Rafael B, Matheus D, Osvaldo M, Jurandir MRF, Rafael R, Marcelo ACF, et al.. Gene Expression of GABA. Brain sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969028/
8. Frank S, Nina S, Dilansu G, Patrick JC, Dolores H, Michael S, et al.. Loss of host-derived osteopontin creates a glioblastoma-promoting microenvironment.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5817947/
9. Sukhbir K, Steven MB, Dipasmita P-N, Thomas WM, David RS-P, David DR. Functions of Thrombospondin-1 in the Tumor Microenvironment.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33925464/
10. Barron T, Yalçın B, Su M, Byun YG, Gavish A, Shamardani K, et al.. GABAergic neuron-to-glioma synapses in diffuse midline gliomas. Nature [Internet]. 2025Feb19;639(8056). Available from: https://www.nature.com/articles/s41586-024-08579-3
11. Available from: https://www.oncotarget.com/article/11483/text/
12. Eleonora C, Claudia F, Francesca C, Veronica P, Biagio P, Giuseppina M, et al.. THBS1 and THBS2 Enhance the In Vitro Proliferation, Adhesion, Migration and Invasion of Intrahepatic Cholangiocarcinoma Cells.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/38339060/
13. Singh K, Jayaram M, Kaare M, Leidmaa E, Jagomäe T, Heinla I, et al.. Neural cell adhesion molecule Negr1 deficiency in mouse results in structural brain endophenotypes and behavioral deviations related to psychiatric disorders. Scientific Reports [Internet]. 2019Apr1;9(1). Available from: https://www.nature.com/articles/s41598-019-41991-8
14. Hua M, Drake GL, Jingxuan Y, Vivian FZ, Min L. Deregulated signaling pathways in glioblastoma multiforme: molecular mechanisms and therapeutic targets.. Cancer investigation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3799884/
15. Wei-Jiang Z, Guan-Yong O, Wen-Wen L. Integrative Analysis of Neuregulin Family Members-Related Tumor Microenvironment for Predicting the Prognosis in Gliomas.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8155525/
16. Katyayani S, Mohan J, Maria K, Este L, Toomas J, Indrek H, et al.. Neural cell adhesion molecule Negr1 deficiency in mouse results in structural brain endophenotypes and behavioral deviations related to psychiatric disorders.. Scientific reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30932003/
17. Liu H, Tang T. MAPK signaling pathway-based glioma subtypes, machine-learning risk model, and key hub proteins identification. Scientific Reports [Internet]. 2023Nov4;13(1). Available from: https://www.nature.com/articles/s41598-023-45774-0
18. Kao W-T, Wang Y, Kleinman JE, Lipska BK, Hyde TM, Weinberger DR, et al.. Common genetic variation in Neuregulin 3 (
            <i>NRG3</i>
            ) influences risk for schizophrenia and impacts
            <i>NRG3</i>
            expression in human brain. Proceedings of the National Academy of Sciences [Internet]. 2010Aug16;107(35). Available from: https://www.pnas.org/doi/10.1073/pnas.1005410107
19. Tsai H-F, Chang Y-C, Li C-H, Chan M-H, Chen C-L, Tsai W-C, et al.. Type V collagen alpha 1 chain promotes the malignancy of glioblastoma through PPRC1-ESM1 axis activation and extracellular matrix remodeling. Cell Death Discovery [Internet]. 2021Oct26;7(1). Available from: https://www.nature.com/articles/s41420-021-00661-3
20. Available from: https://www.nature.com/articles/cddis2013433
21. Liu Z, Su D, Qi X, Ma J. MiR‑500a‑5p promotes glioblastoma cell proliferation, migration and invasion by targeting chromodomain helicase DNA binding protein 5. Molecular Medicine Reports [Internet]. 2018Jul9;. Available from: https://www.spandidos-publications.com/10.3892/mmr.2018.9259
22. Ruolun W, Jiasheng Z, Brandon B, Xianzhi L. Glioma actively orchestrate a self-advantageous extracellular matrix to promote recurrence and progression.. BMC cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308147/
23. Sheng-Hua C, Yan-Bin M, Dong-Fu F, Hong Z, Zhi-An Z, Zhi-Qiang L, et al.. Upregulation of SATB1 is associated with the development and progression of glioma.. Journal of translational medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3492129/
24. Lei X, Fengling S, Tengling L, Qijun L, Dongmei T, Yi T. Pan-Cancer Analysis Identifies CHD5 as a Potential Biomarker for Glioma.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/35955624/
25. Huan B, Yun C, Yonghui Z, Ketao J, Huanrong L. Recent Advances in the Delivery of Bone Morphogenetic Proteins for Targeting Glioma: An Updated Review.. International journal of nanomedicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12136072/
26. Xu C, Yang C, Ye Q, Xu J, Tong L, Zhang Y, et al.. Mosaic PKHD1 in Polycystic Kidneys Caused Aberrant Protein Expression in the Mitochondria and Lysosomes. Frontiers in Medicine [Internet]. 2021Dec16;8. Available from: https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2021.743150/full
27. Laura JA, Stephen JB, Michelle LH, Gerald RVH, Luis V, Jonathan P, et al.. Adenylyl cyclase AC8 directly controls its micro-environment by recruiting the actin cytoskeleton in a cholesterol-rich milieu.. Journal of cell science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3311928/
28. Sachdeva R, Wu M, Johnson K, Kim H, Celebre A, Shahzad U, et al.. BMP signaling mediates glioma stem cell quiescence and confers treatment resistance in glioblastoma. Scientific Reports [Internet]. 2019Oct10;9(1). Available from: https://www.nature.com/articles/s41598-019-51270-1
29. Ming-Zhi Z, Weiyi M, Cunxi L, Sae-youll C, Chuanming H, Gilbert M, et al.. PKHD1 protein encoded by the gene for autosomal recessive polycystic kidney disease associates with basal bodies and primary cilia in renal epithelial cells.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC356947/
30. Zhang M, Wang H. Ca2+-stimulated ADCY1 and ADCY8 regulate distinct aspects of synaptic and cognitive flexibility. Frontiers in Cellular Neuroscience [Internet]. 2023Jul3;17. Available from: https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2023.1215255/full
31. Alice JW, Vanessa T, Stanley SS, Hong PTN, Andrew PM, Andrew HK, et al.. The role of interleukin-6-STAT3 signalling in glioblastoma.. Oncology letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6144698/
32. Wan Z, Sun R, Liu Y-W, Li S, Sun J, Li J, et al.. Targeting metabotropic glutamate receptor 4 for cancer immunotherapy. Science Advances [Internet]. 2021Dec10;7(50). Available from: https://www.science.org/doi/10.1126/sciadv.abj4226
33. Gonzalo GH, María M, Marta EA-R. The Role of BANK1 in B Cell Signaling and Disease.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8151866/
34. Available from: https://academic.oup.com/noa/article/7/1/vdaf017/7979170
35. Mery SLP, Fábio K, Chairini CT, Paulo VW, Diogo L de O. Metabotropic glutamate receptors as a new therapeutic target for malignant gliomas.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5400663/
36. Available from: https://www.proteinatlas.org/ENSG00000153064-BANK1
37. Ti-Chun C, Wen-Jeng W, Wei-Ming L, Meng-Shin S, Yow-Ling S, Chien-Feng L. SLC14A1 prevents oncometabolite accumulation and recruits HDAC1 to transrepress oncometabolite genes in urothelial carcinoma.. Theranostics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/33052246/
38. Toshiro M, Tomoko H, Wei-Wei P, Yu F, Matthew VH, Jun Q, et al.. The Hippo Pathway Kinases LATS1/2 Suppress Cancer Immunity.. Cell [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5512418/
39. Massinen S, Hokkanen M-E, Matsson H, Tammimies K, Tapia-Páez I, Dahlström-Heuser V, et al.. Increased Expression of the Dyslexia Candidate Gene DCDC2 Affects Length and Signaling of Primary Cilia in Neurons. PLoS ONE [Internet]. 2011Jun16;6(6). Available from: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0020580
40. Ma J, Xue K, Jiang Y, Wang X, He D, Guo P. Down-regulation of SLC14A1 in prostate cancer activates CDK1/CCNB1 and mTOR pathways and promotes tumor progression. Scientific Reports [Internet]. 2024Jun28;14(1). Available from: https://www.nature.com/articles/s41598-024-66020-1
41. Available from: https://www.oncotarget.com/article/6929/text/
42. Andrea B, Gayathri C, Arpit W, Steffen E, Jay G, Juha K, et al.. Genetic and protein interaction studies between the ciliary dyslexia candidate genes DYX1C1 and DCDC2.. BMC molecular and cell biology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/37237337/
43. Available from: https://aacrjournals.org/cancerres/article/56/6/1440/503069/Gene-Expression-of-Neural-Cell-Adhesion-Molecule
44. Yongjun K, Feng G, Deliang G. Lipid Metabolism in Glioblastoma: From De Novo Synthesis to Storage.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9405736/
45. Tian S, Du S, Wang C, Zhang Y, Wang H, Fan Y, et al.. Inhibition of primary cilia-hedgehog signaling axis triggers autophagic cell death and suppresses malignant progression of VHL wild-type ccRCC. Cell Death &amp; Disease [Internet]. 2024Oct10;15(10). Available from: https://www.nature.com/articles/s41419-024-07085-8
46. Available from: https://academic.oup.com/jnen/article/72/3/244/2917578
47. Zekanovic S, Achaiber SP, Leenstra S, Lamfers MLM. Cut the fat: targeting cholesterol and lipid metabolism in glioblastoma. Cell Death &amp; Disease [Internet]. 2025Oct7;16(1). Available from: https://www.nature.com/articles/s41419-025-07993-3
48. Matthew RS, Susan LS-R. Emerging Roles of Primary Cilia in Glioma.. Frontiers in cellular neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6391589/
49. Frank E, Leonidas CP. Emerging Role of Glioma Stem Cells in Mechanisms of Therapy Resistance.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10340782/
50. Ravi VM, Neidert N, Will P, Joseph K, Maier JP, Kückelhaus J, et al.. T-cell dysfunction in the glioblastoma microenvironment is mediated by myeloid cells releasing interleukin-10. Nature Communications [Internet]. 2022Feb17;13(1). Available from: https://www.nature.com/articles/s41467-022-28523-1
51. Available from: https://www.abcam.com/en-us/stories/articles/how-hypoxia-inducible-factors-drive-angiogenesis-glioblastoma
52. Liu J, Wang X, Chen AT, Gao X, Himes BT, Zhang H, et al.. ZNF117 regulates glioblastoma stem cell differentiation towards oligodendroglial lineage. Nature Communications [Internet]. 2022Apr22;13(1). Available from: https://www.nature.com/articles/s41467-022-29884-3
53. Matthew BW, Mark RG, Mioara L. T cell exhaustion in malignant gliomas.. Trends in cancer [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10038906/
54. Dimitra PV, Panagiotis GD, Kerasia G, Antonios DB, Kyriaki A, Konstantina Z, et al.. Hypoxia-inducible factor 1alpha and vascular endothelial growth factor in Glioblastoma Multiforme: a systematic review going beyond pathologic implications.. Oncology research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11267112/
55. Miriam F-G, Alejandra C-L, David M-H, Margarita L-L, Ricardo G-R, Alejandro S, et al.. Role of the Ca2+ channel α2δ-1 auxiliary subunit in proliferation and migration of human glioblastoma cells.. PloS one [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9754164/
56. Available from: https://maayanlab.cloud/Harmonizome/gene/KCNJ3
57. Qin L, James AM, Richard LL, Amy LW. Cadherin-7 function in zebrafish development.. Cell and tissue research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4379488/
58. Néant I, Haiech J, Kilhoffer M-C, Aulestia FJ, Moreau M, Leclerc C. Ca2+-Dependent Transcriptional Repressors KCNIP and Regulation of Prognosis Genes in Glioblastoma. Frontiers in Molecular Neuroscience [Internet]. 2018Dec18;11. Available from: https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00472/pdf
59. Available from: https://www.ncbi.nlm.nih.gov/gene/16519
60. Available from: https://maayanlab.cloud/Harmonizome/gene/CDH7
61. Available from: http://json-schema.org/draft-07/schema#"
