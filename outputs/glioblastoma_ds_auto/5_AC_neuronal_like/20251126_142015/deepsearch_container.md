# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: glioblastoma multiforme (GBM)
- Tissue: brain

## Input Genes
LINC02235, AC037486.1, PCDH11X, LINC01829, AL591043.2, ZNF423, ADAMTS18, AL133538.1, DOCK2, SCN1A-AS1, AL022068.1, SEPTIN14, SGCZ, ADAM28, RYR2, DOCK8, ACER2, AC128687.3, AC120193.1, OLR1, AC110296.1, AC109466.1, SPOCK3, ST6GALNAC5, AL136441.1, ... (373 total)

## Program: Calcium-mediated cell migration
Transient receptor potential (TRP) and ryanodine receptor channels regulate calcium influx and signaling cascades that control glioblastoma cell migration, invasion, and chemotaxis. Multiple TRP channels (TRPM8, TRPV4, TRPM3) and ryanodine receptors (RYR2, RYR3) work in concert with potassium channels to modulate intracellular calcium levels, activate kinases like CaMKII, and regulate cytoskeletal dynamics through BK channel-dependent pathways. This calcium signaling promotes volume changes necessary for lamellipodium extension and cell migration, and radiation-induced calcium signaling through TRPM8 confers radioresistance.

**Predicted impacts**
- Enhanced cell migration and chemotaxis through calcium-mediated cytoskeletal reorganization
- Increased radioresistance via radiation-induced TRPM8 upregulation and impaired DNA repair
- Promotion of cell cycle progression through calcium-dependent kinase activation
- Facilitated transmigration through extracellular matrix barriers

**Evidence summary**
Multiple ion channel families work coordinately to regulate calcium signaling in GBM. TRPM8 shows the highest mRNA upregulation among TRP channels in GBM compared to normal brain tissue. TRPM8 and TRPV4 both show strong correlation with glioma progression and poor patient prognosis. Calcium-dependent processes control migration through activation of intermediate and big conductance potassium channels that regulate volume changes. Radiation induces TRPM8-mediated calcium signaling that both impairs apoptosis and enhances migration. The combination of TRP, ryanodine, and voltage-gated potassium channels creates a coordinated system controlling migration and survival.

**Atomic biological processes**
- calcium influx and signaling. Genes: TRPV4, TRPM8, TRPM3, RYR2, RYR3, KCNH7, KCNIP4, KCNMB4, KCNE4
  - [31]: TRPM8 activation increases Ca2+ signaling that controls cell cycle and migration in GBM
  - [34]: TRP channels including TRPM8 and TRPV4 promote Ca2+ entry into glioma cells
  - [32]: KCND2-mediated potassium channel activity accumulates extracellular K+ affecting neuronal excitability
- cell volume regulation and migration mechanics. Genes: TRPV4, TRPM8, KCNH7, KCNIP4, KCNMB4
  - [31]: Ca2+ activated potassium channels (BK and IK) regulate glioma cell migration through volume changes
  - [35]: Potassium channels control osmotic pressure and cell migration in glioma
- radiation-induced calcium signaling and radioresistance. Genes: TRPM8, RYR2, RYR3
  - [31]: Ionizing radiation activates and upregulates TRPM8-mediated Ca2+ signaling that impairs DNA repair and promotes radioresistance through CaMKII activation

**Atomic cellular components**
- TRP ion channels. Genes: TRPV4, TRPM8, TRPM3
  - [34]: TRPC6, TRPM8, TRPV4, TRPV1/V2 are associated with glioma patient survival and promote pro-tumoral processes
- ryanodine receptors. Genes: RYR2, RYR3
  - [16]: RYR2 promotes cancer cell metastasis, inhibited by S107 drug
  - [13]: RYR mutations show high correlation with tumor mutational burden
- voltage-gated potassium channels. Genes: KCNH7, KCNIP4, KCNMB4, KCNE4
  - [35]: Kv channels control neuronal excitability and affect glioma cell behavior
  - [32]: KCND2 encoding Kv4.2 channels enhance neuronal excitability at cancer-neuron interface

**Required genes (not in input)**
- Genes: CACNA1A, CACNA1C, CACNB4, ITPR1, ITPR2, ITPR3, SLC8A1, ATP2B2, ATP2B3
  - [34]: Other calcium channel families including VGCC and IP3 receptors also regulate calcium signaling in GBM

**Program citations**
- [31]: Comprehensive study of TRPM8 function in GBM migration, radioresistance, and cell cycle control
- [34]: TRP channels in brain tumors including TRPC6, TRPM8, TRPV4 roles in GBM
- [35]: Potassium channels control proliferation, migration, and apoptosis in glioma
- [32]: KCND2 regulation of neuronal excitability at glioma-neuron interface
- [13]: RYR mutations and tumor mutational burden correlation
- [16]: RYR2 metastasis promotion and pharmacological inhibition

## Program: Extracellular matrix degradation and invasion
ADAMTS metalloproteinases, along with regulatory factors including periostin, reelin, and collagens, control extracellular matrix architecture and remodeling. ADAMTS3, ADAMTS14, and ADAMTS18 proteolytically cleave ECM components including aggrecan and versican, generating bioactive matrikines that promote tumor cell motility and invasion. Periostin (POSTN) interacts with integrins to promote invasion and resistance to anti-angiogenic therapy. In contrast, reelin acts as a natural inhibitor of glioma cell migration and invasion by disrupting integrin-matrix interactions. This program is critical for infiltrative behavior characteristic of GBM.

**Predicted impacts**
- Degradation of basement membrane and perivascular ECM enabling infiltration of brain parenchyma
- Generation of pro-invasive matrikines from cleaved ECM components
- Enhanced integrin-mediated signaling promoting EMT and migration
- Resistance to anti-angiogenic therapy through POSTN-mediated pathway activation
- Countervailing anti-invasive effects from reelin that limit infiltration

**Evidence summary**
ADAMTS proteases are dysregulated in GBM and promote ECM remodeling essential for tumor progression. POSTN expression is elevated in high-grade gliomas and correlates directly with tumor grade, recurrence, and poor survival. POSTN mediates resistance to anti-VEGF therapy through STAT3-dependent upregulation of HIF1α and EMT markers. Reelin acts as an anti-invasive factor with expression negatively associated with tumor grade and positively associated with increased overall survival. The presence of reelin in matrices delays both cell attachment and detachment while reducing transmigration capacity. This program represents critical balance between pro- and anti-invasive ECM functions.

**Atomic biological processes**
- ECM proteolysis and matrikine generation. Genes: ADAMTS3, ADAMTS14, ADAMTS18
  - [21]: ADAMTS proteases dysregulation occurs in cancer and roles in ECM remodeling and cell signaling modulation
  - [24]: ECM degradation generates bioactive matrikines that promote proliferation, migration and protein synthesis
- periostin-integrin signaling in invasion. Genes: POSTN
  - [45]: POSTN interacts with integrins (αvβ1, αvβ3) to regulate EMT, migration, and resistance to anti-VEGF therapy via STAT3 activation
- reelin-mediated inhibition of invasion. Genes: RELN
  - [14]: RELN serves as natural stop signal, modulates matrix attachment/detachment, and delays transmigration through ECM

**Atomic cellular components**
- ADAMTS proteases. Genes: ADAMTS3, ADAMTS14, ADAMTS18
  - [21]: ADAMTS family members regulate ECM component degradation and cell-ECM interactions
- ECM glycoproteins and structural proteins. Genes: COL4A6, COL12A1, COL19A1, SPOCK3, EMILIN2
  - [24]: Collagen, fibronectin, laminin and other ECM proteins are modified by remodeling enzymes
- ECM regulatory factors. Genes: POSTN, RELN
  - [45]: POSTN and TGF-β regulate GSC invasion and anti-VEGF resistance
  - [14]: RELN in fibronectin matrix affects invasion capacity

**Required genes (not in input)**
- Genes: MMP2, MMP9, MMP14, TIMP1, TIMP2, TIMP3, FN1, LAMA1, LAMA2, LAMB1
  - [24]: Matrix metalloproteinases, TIMPs, and ECM scaffold proteins required for complete ECM remodeling program

**Program citations**
- [21]: ADAMTS proteases in cancer progression and ECM remodeling
- [24]: ECM remodeling in tumor progression and matrikine signaling
- [45]: POSTN in glioma invasion and anti-VEGF therapy resistance
- [14]: Reelin as natural stop signal and anti-invasive factor in GBM

## Program: Cell adhesion and synaptic protein scaffolding
Protocadherin and cadherin family proteins (PCDH7, PCDH11X, PCDH11Y, CDH13, CDH18), along with synaptic adhesion molecules (NLGN4X, CNTNAP2, SYT1, SYN3), organize cellular junctions and synaptic contacts. These proteins regulate intercellular adhesion, cell migration, proliferation, and survival through calcium-dependent signaling and interactions with the actin cytoskeleton. CNTNAP2 functions in neurite outgrowth, dendritic spine stability, and synaptic transmission, while NLGN4X serves as a glioma-associated tumor antigen. Dysregulation of adhesion molecules contributes to epithelial-mesenchymal transition (EMT) and glioma stem cell (GSC) maintenance.

**Predicted impacts**
- Altered cell-cell adhesion affecting glioma cell migration and invasiveness
- Enhanced synaptic integration with neuronal circuits driving proliferation
- Dysregulation of EMT programs through altered cadherin function
- Formation of neuron-glioma synaptic contacts enabling BDNF and other paracrine factor exchange
- Therapeutic vulnerability through NLGN4X as tumor-associated antigen for CAR-T approaches

**Evidence summary**
Protocadherins and classical cadherins regulate CSC function and tumor progression. PCDHA8 is hypermethylated in gliomas and associated with shorter survival through impaired cell-to-cell contact. Synaptic adhesion molecules including NLGN4X and CNTNAP2 integrate glioma cells into neural circuits. NLGN4X is overexpressed in human gliomas and serves as immunogenic tumor-associated antigen recognized by vaccine-induced TCR. CNTNAP2 regulates dendritic spine stability and synaptic transmission; its loss reduces spine density and synaptic inputs. SYT1 appears as core gene associated with GBM progression. Multiple adhesion molecules show altered expression that impacts GBM pathogenesis.

**Atomic biological processes**
- cell-cell adhesion and junction formation. Genes: PCDH7, PCDH11X, PCDH11Y, CDH13, CDH18
  - [3]: Cell adhesion molecules regulate migration, invasion, proliferation and survival; context-specific roles in CSC function
  - [1]: N-cadherin expression remains upregulated in GBM and promotes CSC invasion via ERK and integrin α6
- synaptic adhesion and neuron-glioma interactions. Genes: NLGN4X, SYT1, SYN3
  - [37]: NLGN4X is glioma-associated antigen and serves as target for TCR T cell therapy
  - [40]: NLGN3 and neuroligin-mediated synaptic contacts are paracrine factors driving glioma proliferation
- synaptic plasticity and spine stability. Genes: CNTNAP2
  - [15]: CNTNAP2 regulates neurite outgrowth, dendritic spine density and stability, and synaptic transmission
  - [18]: CNTNAP2 loss reduces dendritic spine density and synaptic inputs; CASPR2 ecto-domain promotes calcium export

**Atomic cellular components**
- protocadherin and classical cadherin proteins. Genes: PCDH7, PCDH11X, PCDH11Y, CDH13, CDH18
  - [3]: CAMs including protocadherins and classical cadherins regulate CSC adhesion and migration
- neuroligin and neurexin-binding proteins. Genes: NLGN4X, CNTNAP2
  - [37]: Neuroligins are postsynaptic adhesion molecules binding neurexins, essential for synaptic formation
  - [15]: CNTNAP2 forms complexes regulating synaptic organization and neuronal development
- synaptic vesicle and calcium sensing proteins. Genes: SYT1, SYN3
  - [40]: SYT1 functions as primary calcium sensor in neurotransmission; SV2B involved in synaptic function and co-expressed with SYT1

**Required genes (not in input)**
- Genes: CDH1, CDH2, CTNNB1, CTNND1, NRXN1, NRXN2, NRXN3, CASPR2
  - [3]: Classical cadherins, catenins, and neurexins required for complete adhesion program

**Program citations**
- [3]: CAMs regulate CSC migration, invasion, proliferation and survival
- [1]: N-cadherin expression in invasive GBM cells
- [37]: NLGN4X as glioma-associated antigen and TCR target
- [40]: NLGN3 and neuronal activity in GBM proliferation
- [15]: CNTNAP2 in synaptic plasticity and dendritic spine
- [18]: CNTNAP2 dendritic spine density and synaptic function

## Program: Tumor-associated macrophage polarization and immune suppression
Scavenger receptors (CD163/MSR1, OLR1/LOX-1) and pattern recognition receptors (TLR2, LY96/MD2) direct monocyte-derived macrophages (MDMs) toward pro-tumoral M2-like phenotypes in the GBM microenvironment. CD163+ macrophages and M2-polarized tumor-associated macrophages (TAMs) accumulate in perivascular and peritumoral regions, expressing immunosuppressive genes including complement inhibitors and producing pro-tumoral cytokines. LY96 associates with TLR4 activation of NF-κB pathway promoting pro-inflammatory cytokine production and TAM recruitment. MSR1/CD204 expression marks M2 macrophages and contributes to immunosuppression. CD96 and VSIG4 provide inhibitory signals to T cells, while other immune modifiers limit anti-tumor immunity.

**Predicted impacts**
- Accumulation of pro-tumoral M2-like macrophages in GBM microenvironment
- Enhanced TLR4 signaling promoting MDM recruitment and inflammatory responses
- Suppression of CD8+ T cell proliferation and anti-tumor immunity
- Production of immunosuppressive cytokines and complement inhibitors by TAMs
- Poor response to checkpoint blockade immunotherapy due to macrophage-mediated immune suppression
- Perivascular and peritumoral niche establishment promoting GSC maintenance

**Evidence summary**
Multiple immune receptors coordinate to establish pro-tumoral macrophage phenotypes in GBM. CD163+ cells are most common immune population in GBM tumor core and peritumoral areas. M2-like TAMs accumulate in perivascular regions and produce pro-tumoral cytokines. MSR1/CD204 marks M2 macrophages; SR-A1 (MSR1) deletion paradoxically promotes M2 polarization via STAT3/STAT6, suggesting complex regulation. LY96 shows marked upregulation in GBM compared to normal tissue and correlates with poor survival. TLR4-LY96 axis activates NF-κB promoting pro-inflammatory responses and monocyte recruitment. CD163+ macrophages suppress T cell function. VSIG4 also inhibits T cell proliferation. OLR1 overexpression activates NF-κB pathway promoting migration. This program creates immunosuppressive niche resistant to checkpoint blockade.

**Atomic biological processes**
- scavenger receptor-mediated M2 macrophage polarization. Genes: MSR1, CD163
  - [43]: SR-A1 (MSR1) deletion promotes M2-like TAM polarization via STAT3 and STAT6 signaling; high SR-A1 expression protects against M2 polarization
  - [46]: MSR1 is marker of M2 macrophage polarization and involved in pro-tumoral phenotype
- pattern recognition receptor signaling and innate immunity. Genes: LY96, TLR2
  - [33]: LY96 (MD2) interacts with TLR4 and activates NF-κB pathway promoting pro-inflammatory cytokine production and TAM recruitment
- T cell inhibition and immune checkpoint signaling. Genes: CD96, VSIG4, CFH
  - [12]: CD163 and other scavenger receptors suppress T cell function; VSIG4 inhibits T cell proliferation
- oxidized LDL receptor signaling in macrophages. Genes: OLR1
  - [38]: OLR1 (LOX-1) overexpression upregulates NF-κB and pro-oncogenic genes in cancer cells; involved in cancer cell migration
  - [41]: LOX-1 is scavenger receptor involved in immune cell activation and inflammatory processes

**Atomic cellular components**
- scavenger receptors on macrophages. Genes: MSR1, CD163, OLR1
  - [12]: Scavenger immunosuppressive program includes MRC1 (CD206), MSR1 (CD204), CD163 and other scavenger receptors
- toll-like receptors. Genes: TLR2, LY96
  - [33]: LY96 and TLR2 pattern recognition receptors activate innate immune signaling
- T cell checkpoint and inhibitory molecules. Genes: CD96, VSIG4
  - [12]: CD96 and VSIG4 are T cell inhibitory molecules expressed on immune cells

**Required genes (not in input)**
- Genes: TLR4, IL6, IL10, TNF, STAT3, STAT6, CSF1R, CCL2, CD39, CD73, NF-KBI, IL33
  - [27]: IL-1β/IL-1R1 circuit between tumor and MDM; IL-6, IL-10, TNF cytokine signaling
  - [43]: STAT3/STAT6 signaling in macrophage polarization; CSF1R for myeloid cell growth

**Program citations**
- [12]: Comprehensive myeloid cell programs in gliomas including scavenger immunosuppressive program
- [43]: SR-A1 (MSR1) modulates macrophage polarization in GBM
- [46]: MSR1 in tumor-associated macrophages and immune suppression
- [33]: LY96 pan-cancer analysis showing upregulation in GBM and NF-κB activation
- [38]: OLR1 in cancer progression and NF-κB signaling
- [41]: LOX-1 as immune receptor in inflammatory processes
- [9]: Myeloid cells in GBM microenvironment and immune regulation

## Program: Wnt/β-catenin pathway and stemness maintenance
PLD1, WNT16, KLF5, and associated signaling components regulate canonical Wnt/β-catenin pathway that maintains glioblastoma stem cell (GSC) self-renewal and pluripotency. PLD1 promotes Wnt/β-catenin signaling through phospholipase D activity and cross-talk with PI3K/Akt pathway, affecting GSC stemness and chemoresistance. KLF5 transcription factor functions downstream in GSC maintenance. STAT4 and MEOX2 provide additional transcriptional regulation. This pathway is essential for GSC maintenance, resistance to temozolomide (TMZ), and intrinsic tumorigenicity distinct from proliferating tumor core.

**Predicted impacts**
- Enhanced GSC self-renewal and undifferentiated state maintenance
- Increased resistance to temozolomide chemotherapy
- Promotion of tumor initiation and heterogeneity
- Activation of pluripotency programs and multi-lineage differentiation potential
- Cross-talk with other stemness pathways (Notch, Hedgehog, BMP)

**Evidence summary**
Wnt/β-catenin pathway is critical regulator of GSC maintenance distinct from proliferative tumor core. PLD1 controls stemness through dual regulation of Wnt/β-catenin and PI3K/Akt axes. PLD1 inhibition specifically targets GSCs, not neuroprogenitor cells, and sensitizes GSC-derived intracranial tumors to TMZ. KLF5 regulates expression of genes controlling stemness and differentiation. STAT4 functions as transcriptional regulator. WNT16 provides direct Wnt pathway stimulation. Aberrant Wnt signaling in GSCs renders them resistant to conventional chemo- and radiotherapy. MEOX2 provides developmental transcriptional regulation. This program is distinct from EMT/invasion program and targeted approach could overcome therapy resistance.

**Atomic biological processes**
- canonical Wnt/β-catenin signaling and GSC maintenance. Genes: WNT16, KLF5, STAT4
  - [26]: Wnt signaling maintains stemness of GSCs; aberrant Wnt pathway promotes stemness, self-renewal and therapeutic resistance
  - [29]: β-catenin nuclear translocation and TCF/LEF transcription activate Wnt target genes promoting cell proliferation
- PLD1-mediated Wnt pathway activation and stemness. Genes: PLD1
  - [25]: PLD1 regulates GSC stemness and self-renewal via Wnt/β-catenin and PI3K/Akt pathways; PLD1 inhibition sensitizes GSCs to TMZ
  - [28]: PLD1 inhibition attenuates tumorigenesis by blocking PI3K/Akt and Wnt/β-catenin signaling
- transcriptional regulation of stemness genes. Genes: KLF5, MEOX2
  - [57]: KLF5 regulates expression of stemness genes, proliferation, apoptosis, and migration in various cancers

**Atomic cellular components**
- Wnt ligands and pathway initiation. Genes: WNT16
  - [26]: WNT family of 19 secreted glycoproteins essential for cell proliferation and tissue homeostasis
- transcription factors in Wnt pathway. Genes: KLF5, MEOX2, STAT4
  - [29]: TCF/LEF transcription factors mediate β-catenin signaling; KLF family members regulate target gene expression
- lipid signaling and PLD1 regulation. Genes: PLD1
  - [25]: PLD1 produces phosphatidic acid affecting Wnt signaling and stemness

**Required genes (not in input)**
- Genes: FZD1, FZD2, FZD3, FZD7, FZD9, LRP5, LRP6, CTNNB1, GSK3B, TCF7, LEF1, TCF7L2, APC, AXIN1, AXIN2, NOTCH1, NOTCH2, SHH, GLI1
  - [26]: Canonical Wnt pathway components including frizzled receptors, LRP complex, destruction complex components, and TCF/LEF transcription factors
  - [29]: Crosstalk of Wnt pathway with Notch, Hedgehog, and other developmental pathways

**Program citations**
- [25]: PLD1 in cancer stemness and Wnt/β-catenin signaling
- [26]: Wnt signaling in GBM stem cell maintenance
- [28]: PLD1 and temozolomide resistance
- [29]: Wnt pathway biology and disease
- [57]: KLF5 transcription factor in cancers

## Program: Cholinergic immune modulation
CHRNA7 (alpha 7 nicotinic acetylcholine receptor) and downstream signaling mediate anti-inflammatory effects through the cholinergic anti-inflammatory pathway (CAP). Activation of α7nAChR on macrophages and other immune cells suppresses pro-inflammatory cytokine production (IL-1, IL-6, TNF-α) via JAK2/STAT3 and NF-κB inhibition. This pathway provides immune regulatory function that may be co-opted by GBM to establish immunosuppressive microenvironment. CHRNA7 signaling represents intersection of neuronal and immune function relevant to glioma-neural circuit interactions.

**Predicted impacts**
- Suppression of pro-inflammatory cytokine production in macrophages and microglia
- Modulation of microglia polarization from M1 to less inflammatory states
- Reduced infiltration of inflammatory immune cells into tumor
- Establishment of immunotolerant microenvironment favoring tumor growth
- Neuronal-immune cell coupling promoting tumor-supportive cross-talk

**Evidence summary**
Cholinergic anti-inflammatory pathway via α7nAChR provides immunomodulatory effects through JAK2/STAT3 and NF-κB inhibition. Activation of α7nAChR reduces LPS-induced systemic inflammation and protects organs. In macrophages, α7nAChR activation decreases pro-inflammatory cytokine production while anti-inflammatory cytokine production remains unaffected. α7nAChR signaling enhances macrophage-macrophage interactions under inflammatory conditions. Microglia with LPS-induced pro-inflammatory phenotype can be reversed by α7nAChR agonists. GBM may exploit this anti-inflammatory pathway to establish immunosuppressive microenvironment. The intersection of neuronal CHRNA7 signaling with immune regulation connects glioma-neuron circuits to immune suppression.

**Atomic biological processes**
- α7nAChR-mediated anti-inflammatory signaling. Genes: CHRNA7
  - [8]: Activation of α7nAChR reduces inflammation via cholinergic anti-inflammatory pathway; JAK2/STAT3 phosphorylation inhibits pro-inflammatory cytokine expression
  - [11]: α7nAChR signaling in macrophages has anti-inflammatory and organ-protective effects
- immune cell communication and macrophage-macrophage signaling. Genes: CHRNA7
  - [11]: α7nAChR activation enhances macrophage-macrophage interactions leading to anti-inflammatory effects

**Atomic cellular components**
- alpha 7 nicotinic acetylcholine receptor. Genes: CHRNA7
  - [8]: α7nAChR highly permeable to calcium and activated by acetylcholine and choline

**Required genes (not in input)**
- Genes: JAK2, STAT3, NFKBIA, IL6, TNF, IL1B, IL10, ACH, CHAT, CHRFAM7A
  - [8]: JAK2/STAT3 pathway, NF-κB, cytokines IL-6, TNF, IL-1β, IL-10 in cholinergic signaling

**Program citations**
- [8]: Comprehensive review of α7nAChR in neuroinflammation and cholinergic pathway
- [11]: α7nAChR macrophage signaling and anti-inflammatory effects

## Program: DOCK protein-mediated immune synapse formation
DOCK2 and DOCK8 proteins function as guanine nucleotide exchange factors (GEFs) for Rho GTPases (CDC42, RAC1, RHO) controlling cytoskeleton dynamics and immune cell function. DOCK8 is particularly critical for T cell, B cell, and NK cell function through regulation of immune synapse formation, lymphocyte migration, and survival. DOCK proteins connect T cell receptor (TCR) signaling to actin cytoskeleton reorganization through WASP pathway. Loss of DOCK function impairs immune surveillance and increases cancer susceptibility. DOCK5 provides additional GEF function in cellular contexts.

**Predicted impacts**
- Impaired T cell immune synapse formation reducing anti-tumor T cell killing
- Decreased lymphocyte migration into tumor reducing immune infiltration
- Reduced B cell function and antibody production affecting tumor surveillance
- Impaired NK cell-mediated cytotoxicity
- Compromised antigen presentation and immune activation

**Evidence summary**
DOCK8 is critical for immune synapse formation through promoting F-actin recombination and LFA-1 polarization. DOCK8 connects TCR signaling to actin cytoskeleton through WASP pathway. Absence of DOCK8 impairs immune synapse formation preventing maintenance of B cell germinal centers and long-lived antibody production. DOCK8 deficiency causes combined immunodeficiency with low T, B, and NK cells plus susceptibility to cancer. DOCK8 mutations associated with impaired CD8 T cell activation and reduced antiviral cytokine production. DOCK2 and DOCK5 provide related GEF functions. Loss of DOCK function would compromise anti-tumor immunity and enable GBM progression.

**Atomic biological processes**
- immune synapse formation and T cell receptor signaling. Genes: DOCK2, DOCK8
  - [7]: DOCK8 regulates immune synapse formation through LFA-1 polarization and accumulation of adhesion molecules and cytotoxic particles
- cytoskeleton reconstruction and cell migration. Genes: DOCK2, DOCK8
  - [7]: DOCK8 regulates cytoskeleton reconstruction affecting migration of immune cells and immune synapse formation
- lymphocyte differentiation and survival. Genes: DOCK8
  - [7]: DOCK8 associated with lymphocyte migration, survival, and Th17 differentiation of CD4+ T cells
  - [10]: DOCK8 deficiency results in loss of function mutations causing combined immunodeficiency

**Atomic cellular components**
- DOCK guanine nucleotide exchange factors. Genes: DOCK2, DOCK8, DOCK5
  - [7]: DOCK8 as GEF for CDC42 and Rho GTPases regulating immune cell function
- immune synapse adhesion machinery. Genes: DOCK8, DOCK2
  - [7]: LFA-1 polarization and BCR engagement promoted by DOCK8 for immune synapse formation

**Required genes (not in input)**
- Genes: CDC42, RAC1, RHO, WASP, RHOG, TCR, CD3E, LFA1, ICAM1, BCR
  - [7]: Rho GTPases (CDC42, RAC1, RHO), WASP, and adhesion molecules required for complete immune synapse program

**Program citations**
- [7]: DOCK8 in immune synapse formation and immune cell function
- [10]: DOCK8 deficiency and combined immunodeficiency with cancer susceptibility

## Program: Long non-coding RNA regulation of GBM processes
Long non-coding RNAs (lncRNAs) from the LINC family, including LINC-PINT, MIR222HG, RMST, and numerous other LINC species, function as regulatory nodes controlling invasion, epithelial-mesenchymal transition (EMT), stemness, and therapeutic resistance. LINC-PINT suppresses cell proliferation, invasion, and EMT by blocking Wnt/β-catenin signaling. LINC species show dysregulation in GBM tumors compared to normal brain and associate with aggressive phenotypes. These lncRNAs regulate EMT-related genes (N-cadherin, Vimentin, Slug), interact with miRNAs, and coordinate signaling pathway activation.

**Predicted impacts**
- Reduced epithelial-mesenchymal transition and invasive capacity when lncRNAs are upregulated
- Suppression of Wnt/β-catenin stemness pathway and cancer stem cell self-renewal
- Modulation of miRNA availability and post-transcriptional gene regulation
- Alteration of chromatin states affecting gene expression programs
- Potential therapeutic targets through lncRNA modulation

**Evidence summary**
lncRNAs represent emerging class of GBM regulators with diverse functions in tumorigenesis. LINC-PINT is downregulated in GBM tissues compared to normal brain and associated with good prognosis. LINC-PINT suppresses tumor proliferation, invasion, and EMT by blocking Wnt/β-catenin pathway through β-catenin, TCF1/TCF7, C-Jun, and CD44 downregulation. Gene correlation analysis reveals LINC-PINT negative correlation with EMT markers (N-cadherin, Vimentin, Slug). MIR222HG produces miR-22-3p and miR-22-5p that regulate Wnt signaling in GSCs. Over 35+ LINC genes present in input gene list suggesting coordinated regulatory roles. lncRNAs regulate nuclear organization, chromatin remodeling, and gene expression. Multiple LINC species likely provide overlapping or complementary functions in controlling GBM processes.

**Atomic biological processes**
- EMT regulation and invasion suppression. Genes: LINC02235, LINC01829, LINC01467, LINC01725, LINC00944, LINC01122, LINC01091, LINC00504, LINC00355, LINC01135, LINC00299, LINC00886, LINC00607, LINC01163, LINC02234, LINC01182, LINC01923, LINC02246, LINC02300, LINC02306, LINC02378, LINC02664, LINC02775, LINC02798, LINC02821, LINC01934, LINC01877, LINC01208, LINC01876, LINC01842, LINC01798, LINC01579, LINC01357, LINC02055, LINC01241
  - [2]: LINC-PINT suppresses cell proliferation, invasion, and EMT by blocking Wnt/β-catenin signaling; negative correlation with EMT markers (N-cadherin, Vimentin, Slug)
- Wnt/β-catenin pathway regulation. Genes: MIR222HG, LINC02235
  - [2]: LINC-PINT inhibits Wnt/β-catenin signaling pathway through β-catenin, TCF1/TCF7, C-Jun, and CD44 suppression
- miRNA targeting and post-transcriptional regulation. Genes: MIR222HG, MIR548XHG, RMST
  - [5]: lncRNAs regulate gene expression through miRNA sponging and post-transcriptional mechanisms; regulate proliferation, migration, invasion, apoptosis
- chromatin remodeling and transcriptional regulation. Genes: RMST
  - [5]: lncRNAs assemble nuclear domains, associate with chromatin-modifying complexes, regulate transcriptional silencing

**Atomic cellular components**
- LINC family long non-coding RNAs. Genes: LINC02235, LINC01829, LINC01467, LINC01725, LINC00944, LINC01122, LINC01091, LINC00504, LINC00355, LINC01135, LINC00299, LINC00886, LINC00607, LINC01163, LINC02234, LINC01182, LINC01923, LINC02246, LINC02300, LINC02306, LINC02378, LINC02664, LINC02775, LINC02798, LINC02821, LINC01934, LINC01877, LINC01208, LINC01876, LINC01842, LINC01798, LINC01579, LINC01357, LINC02055, LINC01241
  - [5]: Over 167,000 annotated lncRNAs in humans; lincRNAs associated with chromatin-modifying complexes
- miRNA host and processing lncRNAs. Genes: MIR222HG, MIR548XHG
  - [2]: MIR222HG produces miR-22-3p and miR-22-5p regulating Wnt signaling in GSCs

**Required genes (not in input)**
- Genes: DICER1, DROSHA, AGO2, DGCR8, POLR2A, POLR3A, DNMT3A, EZHS2, SUZ12
  - [5]: lncRNA biogenesis, miRNA processing, and chromatin modifying complexes required for complete lncRNA program

**Program citations**
- [2]: LINC-PINT suppresses GBM invasion and EMT via Wnt pathway
- [5]: Comprehensive review of ncRNA roles in GBM including lncRNAs

## Program: Neuron-glioma synaptic plasticity
Glioblastoma cells form functional synapses with neurons through BDNF-TrkB signaling and other activity-dependent mechanisms. NLGN4X, CNTNAP2, SYT1, and SYN3 are core synaptic proteins mediating these interactions. BDNF secretion from neurons in response to activity increases glutamate-evoked currents in glioma cells through AMPA receptor trafficking, promoting tumor proliferation and progression. Glioma cells integrate into neural circuits at cancer-neuron interface, with activity-dependent synaptic plasticity regulating tumor behavior. This malignant plasticity represents cooption of normal adaptive mechanisms by tumor.

**Predicted impacts**
- Integration of glioma cells into functional neural circuits
- Activity-dependent enhancement of glioma proliferation and migration
- Increased glutamate-evoked depolarization promoting tumor progression
- Glioma-induced neuronal hyperexcitability and glioma-associated epilepsy
- Coordinated glioma-neuron network activity propagating through tumor microtubes via gap junctions

**Evidence summary**
Gliomas recruit mechanisms of adaptive neuroplasticity normally used for learning and memory. BDNF-TrkB signaling promotes malignant synaptic plasticity distinct from normal adaptive responses. Activity-regulated BDNF secretion from brain microenvironment increases glutamate-evoked current amplitude in glioma cells through AMPA receptor trafficking via CAMKII and GluA4 phosphorylation. NLGN4X serves as glioma-associated tumor antigen and essential synaptic adhesion molecule. CNTNAP2 regulates synaptic organization and function. SYT1 appears as core gene for GBM progression and calcium-dependent neurotransmission. TrkB loss or BDNF blocking abrogates these effects and prolongs survival. Glioma cells form gap-junctional networks where neuron-to-glioma synaptic inputs affect multiple tumor cells. This program represents hallmark of aggressive GBM phenotype.

**Atomic biological processes**
- activity-regulated BDNF secretion and TrkB signaling. Genes: SYT1, NLGN4X, SYN3
  - [40]: Neuronal activity-regulated BDNF secretion promotes malignant synaptic plasticity through TrkB receptor signaling in glioma cells
- glutamate receptor trafficking and synaptic strength. Genes: SYT1, CNTNAP2
  - [40]: BDNF-TrkB signaling promotes AMPA receptor trafficking to glioma cell membrane via CAMKII, increasing glutamate-evoked current amplitude
- neuron-glioma synaptic connectivity. Genes: NLGN4X, CNTNAP2, SYT1, SYN3
  - [40]: BDNF-TrkB signaling regulates number of neuron-to-glioma synapses; TrkB loss reduces responsive glioma cells

**Atomic cellular components**
- synaptic adhesion molecules. Genes: NLGN4X, CNTNAP2
  - [37]: NLGN4X is postsynaptic adhesion molecule binding neurexins, essential for synaptic formation
  - [15]: CNTNAP2 forms complexes regulating synaptic organization
- calcium sensing and vesicle machinery. Genes: SYT1
  - [40]: SYT1 functions as primary calcium sensor in neurotransmission and hormone secretion
- synaptic proteins and neurotransmitter release. Genes: SYN3, SYT1
  - [50]: SV2B and SYT1 are core genes associated with GBM progression in synaptic contexts

**Required genes (not in input)**
- Genes: NTRK2, BDNF, CAMKII, GLUAA1, GLUAA2, GLUAA3, GLUAA4, NRXN1, NRXN2, NRXN3, CASPR2
  - [40]: TrkB receptor, BDNF ligand, CAMKII kinase, AMPA receptor subunits, neurexins required for complete synaptic plasticity program

**Program citations**
- [40]: BDNF-TrkB signaling in malignant synaptic plasticity and GBM progression
- [37]: NLGN4X in glioma-neuron synapses and TCR T cell therapy
- [15]: CNTNAP2 in synaptic organization and neuronal function
- [50]: SYT1 and SV2B as prognostic biomarkers in GBM synaptic signaling

## Program: Scavenger receptor and pattern recognition signaling
Scavenger receptors (OLR1/LOX-1, MSR1/CD204, CD163) and pattern recognition receptors (TLR2, LY96/MD2) recognize pathogen-associated molecular patterns and oxidized ligands, activating NF-κB and inflammatory pathways. OLR1 upregulation in cancer cells promotes NF-κB activation leading to suppression of apoptosis and stimulation of proliferation. LY96 associates with TLR4, and TLR2 activates innate immunity. These receptors shape macrophage phenotype and promote pro-tumoral inflammation. In GBM context, scavenger receptor signaling establishes immunosuppressive microenvironment and promotes intrinsic tumor cell growth.

**Predicted impacts**
- Sustained NF-κB signaling promoting proliferation and suppressing apoptosis
- Pro-inflammatory cytokine production supporting tumor growth
- Macrophage polarization toward pro-tumoral M2 phenotype
- Enhanced migration and invasive capacity through NF-κB-dependent mechanisms
- Resistance to cell death and therapy

**Evidence summary**
Scavenger receptors are frequently upregulated in cancers including GBM and promote pro-tumoral functions. OLR1 expression upregulation increases NF-κB (p65) activation and expression of pro-oncogenic genes (BCL2, BCL2A1) while inhibiting apoptosis. OLR1 overexpression in cancer cells enhances migration without affecting adhesion. LY96 shows marked upregulation in GBM versus normal tissue and correlates with poor survival. LY96-TLR4 axis activates NF-κB promoting pro-inflammatory responses and monocyte recruitment. TLR2 directly activates innate immunity. MSR1 (CD204) marks M2 pro-tumoral macrophages. CD163+ cells abundant in GBM microenvironment. These receptors create feedback loops amplifying pro-tumoral signaling.

**Atomic biological processes**
- scavenger receptor-mediated NF-κB activation. Genes: OLR1, MSR1, CD163
  - [38]: OLR1 overexpression activates NF-κB (p65) and pro-oncogenic genes inhibiting apoptosis
- pattern recognition receptor signaling. Genes: LY96, TLR2
  - [33]: LY96 (MD2) interacts with TLR4 and activates NF-κB pathway promoting pro-inflammatory cytokine production
- ligand recognition and cellular uptake. Genes: OLR1, MSR1
  - [38]: OLR1 recognizes oxidized ligands and apoptotic cell surfaces; promoted by oxidative stress
  - [41]: LOX-1 recognizes oxidatively modified LDL and other oxidized molecules

**Atomic cellular components**
- oxidized low-density lipoprotein receptors. Genes: OLR1
  - [38]: OLR1 (LOX-1) is major receptor for oxidized LDL with pro-oncogenic signaling
- macrophage scavenger receptors. Genes: MSR1, CD163
  - [46]: MSR1 (CD204) is homo-trimeric transmembrane glycoprotein with collagen-like and SRCR domains
- toll-like receptors and TLR co-receptors. Genes: TLR2, LY96
  - [33]: LY96 (MD2) associates with TLR4 conferring responsiveness to LPS

**Required genes (not in input)**
- Genes: TLR4, MYD88, NFKB1, RELA, IKBKG, IKBKB, IL6, TNF, IL1B
  - [33]: TLR4, MYD88, NF-κB pathway components, and inflammatory cytokines required for complete pattern recognition program

**Program citations**
- [38]: OLR1 in cancer progression and NF-κB signaling
- [41]: LOX-1 as immune receptor in inflammatory processes
- [33]: LY96 pan-cancer analysis with GBM upregulation
- [46]: MSR1 in tumor-associated macrophages

## Bibliography
1. Dominique BH, Luigi M, Joachim W, Tanja W, Theresa JB, Wendy SM, et al.. Gene expression profile of glioblastoma multiforme invasive phenotype points to new therapeutic targets.. Neoplasia (New York, NY) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC1490313/
2. Zhu H, Chen Z, Shen L, Tang T, Yang M, Zheng X. Long Noncoding RNA LINC-PINT Suppresses Cell Proliferation, Invasion, and EMT by Blocking Wnt/β-Catenin Signaling in Glioblastoma. Frontiers in Pharmacology [Internet]. 2021Jan11;11. Available from: https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2020.586653/full
3. Soumya MT, Justin DL. Adhering towards tumorigenicity: altered adhesion mechanisms in glioblastoma cancer stem cells.. CNS oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6040057/
4. Li Q, Aishwarya S, Li J-P, Pan D-X, Shi J-P. Gene Expression Profiling of Glioblastoma to Recognize Potential Biomarker Candidates. Frontiers in Genetics [Internet]. 2022Apr27;13. Available from: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.832742/full
5. Uswa S, Stacey K, James TR, Sunit D. Noncoding RNAs in Glioblastoma: Emerging Biological Concepts and Potential Therapeutic Implications.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8037102/
6. Yena J, Wooyong C, Gyurin P, Yeongmin K, Junbeom H, Sangzin A. Tumor Microenvironment and Genes Affecting the Prognosis of Temozolomide-Treated Glioblastoma.. Journal of personalized medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9966340/
7. Longhui Z, Yang C, Xiangpeng D, Xiaoling Z. Deciphering the role of DOCK8 in tumorigenesis by regulating immunity and the application of nanotechnology in DOCK8 deficiency therapy.. Frontiers in pharmacology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9664064/
8. Tehila M, Adi V-D, Talma B, Millet T. Neuroinflammation Modulation via α7 Nicotinic Acetylcholine Receptor and Its Chaperone, RIC-3.. Molecules (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8539643/
9. Alessandra DL, Alessio U, Filippo V. Myeloid Cells in Glioblastoma Microenvironment.. Cells [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7824606/
10. Qian Z, Jeremiah CD, Ian TL, Alexandra FF, Huie J, Amanda JF, et al.. Combined immunodeficiency associated with DOCK8 mutations.. The New England journal of medicine [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2965730/
11. Nakamura Y, Matsumoto H, Wu C-H, Fukaya D, Uni R, Hirakawa Y, et al.. Alpha 7 nicotinic acetylcholine receptors signaling boosts cell-cell interactions in macrophages effecting anti-inflammatory and organ protection. Communications Biology [Internet]. 2023Jun23;6(1). Available from: https://www.nature.com/articles/s42003-023-05051-2
12. Miller TE, El FCA, Couturier CP, Chen Z, D’Antonio JP, Verga J, et al.. Programs, origins and immunomodulatory functions of myeloid cells in glioma. Nature [Internet]. 2025Feb26;640(8060). Available from: https://www.nature.com/articles/s41586-025-08633-8
13. Fenglin W, Jingbo Y, Ping L, Charalampos S, Shibo Z, Yuan G, et al.. The ryanodine receptor mutational characteristics and its indication for cancer prognosis.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9515073/
14. Erika O, Daniela Z, Philipp H, Christian RW, Klaus-Michael D, Mike-Andrew W, et al.. The Potential Role of the Extracellular Matrix Glycoprotein Reelin in Glioblastoma Biology.. Pharmaceuticals (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10975808/
15. St. G-HF, Kivisild T, Livesey FJ. The role of contactin-associated protein-like 2 in neurodevelopmental disease and human cerebral cortex evolution. Frontiers in Molecular Neuroscience [Internet]. 2022Oct20;15. Available from: https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.1017144/full
16. Chen T, Zhang X, Ding X, Feng J, Zhang X, Xie D, et al.. Ryanodine receptor 2 promotes colorectal cancer metastasis by the
                    <scp>ROS</scp>
                    /
                    <i>BACH1</i>
                    axis. Molecular Oncology [Internet]. 2022Dec21;17(4). Available from: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13350
17. Markus S, Christ V, Stefan S, Tobias W, Eugen K, Sabine H, et al.. RELN signaling modulates glioblastoma growth and substrate-dependent migration.. Brain pathology (Zurich, Switzerland) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/29222813/
18. Frances SG-H, Toomas K, Frederick JL. The role of contactin-associated protein-like 2 in neurodevelopmental disease and human cerebral cortex evolution.. Frontiers in molecular neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9630569/
19. Pablo I, Ann-Christin P, Marcos S, Michael S, Sabine R, Marianne K, et al.. Genome-wide interference of ZNF423 with B-lineage transcriptional circuitries in acute lymphoblastic leukemia.. Blood advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7948270/
20. Jeong-Seok N, Setsuo H, Lalage MW. Dysadherin: a new player in cancer progression.. Cancer letters [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2094007/
21. Rachele B, Shengnan Y, Elena R. ADAMTS Proteases: Their Multifaceted Role in the Regulation of Cancer Metastasis.. Diseases & research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7616120/
22. Elena S, Pasquale L, Silvia C, Arianna B, Elisa R, Sina A, et al.. Polycomb dysregulation in gliomagenesis targets a Zfp423-dependent differentiation network.. Nature communications [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4773478/
23. Shirong L, Zhi D, Dong Y, Wenxuan L, Hongjuan D, Bin S, et al.. Targeting β2 subunit of Na. American journal of cancer research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6610052/
24. Winkler J, Abisoye-Ogunniyan A, Metcalf KJ, Werb Z. Concepts of extracellular matrix remodelling in tumour progression and metastasis. Nature Communications [Internet]. 2020Oct9;11(1). Available from: https://www.nature.com/articles/s41467-020-18794-x
25. Lim SH, Lee H, Lee HJ, Kim K, Choi J, Han JM, et al.. PLD1 is a key player in cancer stemness and chemoresistance: Therapeutic targeting of cross-talk between the PI3K/Akt and Wnt/β-catenin pathways. Experimental &amp; Molecular Medicine [Internet]. 2024Jul1;56(7). Available from: https://www.nature.com/articles/s12276-024-01260-9
26. Ruoyu G, Xiaoming Z, Mian G. Glioblastoma stem cells and Wnt signaling pathway: molecular mechanisms and therapeutic targets.. Chinese neurosurgical journal [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7398200/
27. Zhihong C, Bruno G, Milota K, Montse PV, Kavita R, Gabrielle P, et al.. A paracrine circuit of IL-1β/IL-1R1 between myeloid and tumor cells drives genotype-dependent glioblastoma progression.. The Journal of clinical investigation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10645395/
28. Dong WK, Won CH, Yu NN, Kang SP, Do SM. Phospholipase D1 inhibition sensitizes glioblastoma to temozolomide and suppresses its tumorigenicity.. The Journal of pathology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7693208/
29. Xue C, Chu Q, Shi Q, Zeng Y, Lu J, Li L. Wnt signaling pathways in biology and disease: mechanisms and therapeutic advances. Signal Transduction and Targeted Therapy [Internet]. 2025Apr4;10(1). Available from: https://www.nature.com/articles/s41392-025-02142-w
30. Available from: https://www.jci.org/articles/view/175127
31. Available from: https://www.oncotarget.com/article/21436/text/
32. Ye Z, Wei D, Lingchao C, Junrui C, Wei X, Qi F, et al.. Potassium ion channel modulation at cancer-neural interface enhances neuronal excitability in epileptogenic glioblastoma multiforme.. Neuron [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/39532103/
33. Kechao N, Jing L, Luqi P, Mei Z, Wei H. Pan-Cancer Analysis of the Characteristics of LY96 in Prognosis and Immunotherapy Across Human Cancer.. Frontiers in molecular biosciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9130738/
34. Giorgia C, Hélène C, Oana C, Dimitra G. TRP Channels in Brain Tumors.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8076903/
35. Samar Y, Nisreen M, Mohamed S, Mohamad R, Dalal HH. Potassium Ion Channels in Glioma: From Basic Knowledge into Therapeutic Applications.. Membranes [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10144598/
36. Available from: https://www.ncbi.nlm.nih.gov/gene/23643
37. Christoper K, Michael K, Yu-Chan C, Alexandros K, Dirk CH, Tamara B, et al.. NLGN4X TCR transgenic T cells to treat gliomas.. Neuro-oncology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10836769/
38. Khaidakov M, Mitra S, Kang B-Y, Wang X, Kadlubar S, Novelli G, et al.. Oxidized LDL Receptor 1 (OLR1) as a Possible Link between Obesity, Dyslipidemia and Cancer. PLoS ONE [Internet]. 2011May26;6(5). Available from: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0020277
39. Daniel DL, Daniel G, Nicole LW-G, Anna EE, Benjamin FO-G, Irving LW. Modeling glioma intratumoral heterogeneity with primary human neural stem and progenitor cells.. Stem cell reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40749669/
40. Taylor KR, Barron T, Hui A, Spitzer A, Yalçin B, Ivec AE, et al.. Glioma synapses recruit mechanisms of adaptive plasticity. Nature [Internet]. 2023Nov1;623(7986). Available from: https://www.nature.com/articles/s41586-023-06678-1
41. Sarah T, Tilman EK, Stefan S, Danny J, Wulf B, Hortense S. Role of Lectin-Like Oxidized Low-Density Lipoprotein Receptor-1 in Inflammation and Pathogen-Associated Interactions.. Journal of innate immunity [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10866614/
42. Alba L, Luis GG-B, Julia LG-A, Conrado M-C, Maria AM-T. Neural Stem Cells as Potential Glioblastoma Cells of Origin.. Life (Basel, Switzerland) [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10145968/
43. Hanwen Z, Wenbin Z, Xuan S, Ruoyu D, Rongmei Z, Hui B, et al.. Class A1 scavenger receptor modulates glioma progression by regulating M2-like tumor-associated macrophage polarization.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5226571/
44. Dongchao X, Ajuan L, Xuan W, Yidan C, Yunyun S, Zhou T, et al.. Repression of Septin9 and Septin2 suppresses tumor growth of human glioblastoma cells.. Cell death & disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5938713/
45. Soon YP, Yuji P, Kang JJ, Jianwen D, John F de G. Periostin (POSTN) Regulates Tumor Resistance to Antiangiogenic Therapy in Glioma Models.. Molecular cancer therapeutics [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104278/
46. Gudgeon J, Marín-Rubio JL, Trost M. The role of macrophage scavenger receptor 1 (MSR1) in inflammatory disorders and cancer. Frontiers in Immunology [Internet]. 2022Oct17;13. Available from: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1012002/full
47. Available from: https://www.uniprot.org/uniprotkb/Q6ZU15/entry
48. Zarodniuk M, Steele A, Lu X, Li J, Datta M. CNS tumor stroma transcriptomics identify perivascular fibroblasts as predictors of immunotherapy resistance in glioblastoma patients. npj Genomic Medicine [Internet]. 2023Oct26;8(1). Available from: https://www.nature.com/articles/s41525-023-00381-w
49. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4639247/
50. Mustafov D, Siddiqui SS, Klena L, Karteris E, Braoudaki M. SV2B/miR-34a/miR-128 axis as prognostic biomarker in glioblastoma multiforme. Scientific Reports [Internet]. 2024Mar19;14(1). Available from: https://www.nature.com/articles/s41598-024-55917-6
51. Available from: https://www.proteinatlas.org/ENSG00000157890-MEGF11/cancer
52. Lei W, Zhengwen H. Functional Roles of Long Non-Coding RNAs (LncRNAs) in Glioma Stem Cells.. Medical science monitor : international medical journal of experimental and clinical research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6795106/
53. Available from: https://www.ncbi.nlm.nih.gov/books/NBK573690/
54. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=84465
55. Tingting X, Meng Z, Wei L, Ruilin Y, Shengping F, Zhenhai F, et al.. Advances in the role of STAT3 in macrophage polarization.. Frontiers in immunology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10110879/
56. Available from: https://www.proteinatlas.org/ENSG00000167077-MEI1/cancer
57. Yao L, Ceshi C. The roles and regulation of the KLF5 transcription factor in cancers.. Cancer science [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
58. Zhao W, Zhang Z, Xie M, Ding F, Zheng X, Sun S, et al.. Exploring tumor-associated macrophages in glioblastoma: from diversity to therapy. npj Precision Oncology [Internet]. 2025May2;9(1). Available from: https://www.nature.com/articles/s41698-025-00920-x
59. M R, Q W, P H, A BH, S B, J NR. Acquisition of meiotic DNA repair regulators maintain genome stability in glioblastoma.. Cell death & disease [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/25906155/
60. Available from: https://www.oncotarget.com/article/1456/pdf/
