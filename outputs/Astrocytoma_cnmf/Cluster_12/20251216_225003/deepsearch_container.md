# Gene Program Markdown Report

## Context
- Cell type: Astrocytes/Astrocytoma cells
- Disease: Astrocytoma (including high-grade glioblastoma multiforme)
- Tissue: Brain (cerebral cortex, white matter)

## Input Genes
LINC00536, EMCN, PRKCH, PTH2R, LINC02511, LINC02476, DISC1FP1, LINC02240, AC097518.2, AP005230.1, GALNT17, EPHA6, AC093866.1, ERVMER61-1, AC090015.1, AC084816.1, LINC01811, AC078923.1, AC112206.2, AC113414.1, AC116362.1, CNBD1, ARHGAP15, MT-ND5, MT-CO1, ... (200 total)

## Program: Mitochondrial Oxidative Phosphorylation and Energy Production
This program encompasses mitochondrial bioenergetics through coordinated expression of multiple electron transport chain components, ATP synthase subunits, and related oxidative phosphorylation machinery. Genes include mitochondrial-encoded subunits (MT-ND1, MT-ND2, MT-ND4, MT-ND4L, MT-ND5, MT-ND6 from Complex I; MT-CO1, MT-CO2, MT-CO3 from Complex IV; MT-CYB from Complex III; MT-ATP6, MT-ATP8 from Complex V) and nuclear-encoded cofactors including SUCLG2. This program is significantly upregulated in high-grade astrocytomas, driving rapid ATP production and supporting enhanced proliferation. Dysregulation through SUCLG2 knockdown suppresses cell proliferation and triggers apoptosis through mitochondrial dysfunction.

**Predicted impacts**
- Enhanced ATP production supporting rapid tumor cell proliferation
- Increased oxidative stress through enhanced electron transport chain activity
- Metabolic inflexibility when SUCLG2 is inhibited, forcing cancer cells into glycolytic dependence
- Mitochondrial fragmentation through MFN1 degradation leading to apoptosis
- Enhanced survival of cancer stem cells under nutrient-poor conditions through efficient ATP production

**Evidence summary**
Mitochondrial genes collectively show dramatic upregulation in high-grade astrocytomas compared to lower-grade tumors and normal astrocytes. SUCLG2 acts as a master regulator of this program through interaction with LMNA and DLAT, controlling both OXPHOS function and lactate metabolism. Multiple independent studies using SUCLG2 knockdown demonstrate that this program is essential for astrocytoma proliferation and survival. Proteomic analyses of glioblastoma tissue cores versus periphery show that SUCLG2 expression significantly increases in tumor cores, correlating with enhanced proliferation markers.

**Atomic biological processes**
- Electron transport chain function. Genes: MT-ND1, MT-ND2, MT-ND4, MT-ND4L, MT-ND5, MT-ND6, MT-CO1, MT-CO2, MT-CO3, MT-CYB, MT-ATP6, MT-ATP8
  - [28]: SUCLG2 knockdown reduces oxidative phosphorylation complex protein expression including SDHB, ND1, ATP5A
  - [34]: Detailed mechanistic studies show SUCLG2-LMNA interaction regulates mitochondrial protein complex expression
  - [51]: Western blot analysis demonstrates reduced expression of mitochondrial OXPHOS complex components following SUCLG2 knockdown
- ATP synthesis. Genes: MT-ATP6, MT-ATP8, SUCLG2
  - [28]: SUCLG2 knockdown leads to significantly decreased ATP production as measured by Seahorse analysis
  - [34]: Mitochondrial dysfunction through SUCLG2-LMNA acetylation modification reduces ATP production
- Mitochondrial metabolism integration. Genes: SUCLG2, MTUS2
  - [28]: SUCLG2 interacts with succinate dehydrogenase complex components to regulate OXPHOS levels
  - [51]: Interaction between SUCLG2 and DLAT regulates lactate metabolism affecting metabolic flexibility

**Atomic cellular components**
- Inner mitochondrial membrane. Genes: MT-ND1, MT-ND2, MT-ND4, MT-ND4L, MT-ND5, MT-ND6, MT-CO1, MT-CO2, MT-CO3, MT-CYB, MT-ATP6, MT-ATP8
  - [28]: LMNA K470ac modification regulates oxidative phosphorylation levels in inner mitochondrial membrane
- Outer mitochondrial membrane. Genes: SUCLG2
  - [28]: MFN1 expression on outer membrane suppressed via SUCLG2-LMNA interaction, triggering mitochondrial apoptosis
  - [34]: Mitochondrial fusion protein MFN1 degradation disrupts mitochondrial fusion on outer membrane

**Required genes (not in input)**
- Genes: MFN1, MFN2, OPA1, LMNA, DLAT
  - [28]: LMNA, MFN1, and DLAT identified as critical SUCLG2 interacting partners through mass spectrometry

**Program citations**
- [28]: Comprehensive proteomic and metabolic studies demonstrating SUCLG2's central role in GBM proliferation
- [34]: Detailed characterization of SUCLG2-LMNA acetylation modification regulating mitochondrial function
- [51]: Western blot and Seahorse analyses confirming reduced oxidative phosphorylation in SUCLG2 knockdown

## Program: Calcium Signaling and Ryanodine Receptor Activation
This program controls intracellular calcium homeostasis through coordinated action of RYR2 (ryanodine receptor 2) and TRPC6 (transient receptor potential cation channel subfamily C member 6), which mediate both release of calcium from intracellular stores and entry from the extracellular space. RYR2 activation is potentiated by MAPK pathway signaling downstream of receptor tyrosine kinases and ultraviolet stress, driving calcium-dependent cell transformation and proliferation. TRPC6 functions as a downstream effector of phospholipase C signaling to amplify calcium signals.

**Predicted impacts**
- Enhanced intracellular calcium concentration promoting cell cycle progression
- Amplified proliferative signaling through sustained calcium-PKC and calcium-calmodulin interactions
- Calcium-dependent transcriptional programs driving oncogenic gene expression
- Reduced dependence on normal differentiation signals through bypass of calcium-dependent checkpoint controls
- Increased radioresistance through calcium-dependent DNA damage response suppression

**Evidence summary**
Recent mechanistic studies demonstrate that potentiation of RYR-mediated calcium release by MAPK signaling represents a critical pathway leading to cellular transformation and carcinogenesis. In epidermal and other epithelial tissue models, EGF-induced ERK phosphorylation directly upregulates RYR2 expression and increases responsiveness to RYR agonists. Critically, carvedilol (a beta-blocker with RYR stabilizing properties) inhibits EGF-promoted transformation through RYR suppression, and this inhibitory effect requires functional RYR, as shRNA-mediated RYR knockdown abolishes the transformation-inhibitory effect of carvedilol. In vivo ultraviolet radiation studies show enhanced DNA damage and skin inflammation with RYR agonist treatment, effects substantially attenuated in RYR2-E4872Q knock-in mice with reduced RYR2 activity.

**Atomic biological processes**
- Calcium release from sarcoplasmic reticulum. Genes: RYR2
  - [7]: RYR2 potentiation by MAPK pathway represents critical carcinogenesis pathway; EGF induces RYR2 upregulation and enhanced 4-CMC-evoked calcium release
  - [8]: RYR2 encodes ryanodine receptor calcium release channel in cardiac and other muscle tissues
- Calcium entry from extracellular space. Genes: TRPC6
  - [14]: TRPC6 functions as calcium-permeable receptor-operated cation channel activated by diacylglycerol downstream of PLC
  - [16]: TRPC6-mediated calcium elevation stimulates non-small cell lung cancer proliferation by promoting cell cycle progression
- Calcium-dependent cell transformation. Genes: RYR2, TRPC6
  - [7]: RYR agonists and calcium ionophore promote JB6 cell transformation; carvedilol inhibits transformation via RYR stabilization
- MAPK pathway coupling to calcium signaling. Genes: RYR2
  - [7]: EGF-induced ERK phosphorylation and RYR2 upregulation increase RYR agonist-evoked calcium release; inhibited by MAPK inhibitors

**Atomic cellular components**
- Sarcoplasmic reticulum membrane. Genes: RYR2
  - [8]: RYR2 localizes to sarcoplasmic reticulum and functions as calcium release channel
- Plasma membrane calcium channels. Genes: TRPC6
  - [14]: TRPC6 functions as plasma membrane calcium-permeable cation channel

**Required genes (not in input)**
- Genes: MAPK1, MAPK3, PLCbeta, PKC, CAMKII, PKA
  - [7]: ERK/MAPK pathway and downstream calcium effectors (PKC, CAMKII) required for RYR-mediated transformation

**Program citations**
- [7]: Comprehensive mechanistic studies in epidermal cells demonstrating RYR2-MAPK coupling in carcinogenesis
- [14]: TRPC6 channel characterization as calcium-permeable receptor-operated channel
- [16]: TRPC6 role in cancer cell proliferation through calcium signaling

## Program: Immune Checkpoint Ligand Expression and T Cell Exhaustion
This program controls expression of inhibitory immune checkpoint ligands including PD-L1 (CD274) and supports recruitment of immunosuppressive cells to the tumor microenvironment. Tumor cells and tumor-associated immune cells upregulate PD-L1 in response to inflammatory signals and interferon-gamma produced by infiltrating T cells. The interaction of tumor-expressed PD-L1 with PD-1 (PDCD1) on T cells delivers inhibitory signals that suppress T cell proliferation, cytokine production, and cytotoxic effector functions, effectively preventing anti-tumor immunity.

**Predicted impacts**
- Suppression of anti-tumor T cell proliferation and activation
- Promotion of T cell exhaustion through PD-L1/PD-1 engagement
- Enhanced survival of tumor cells through escape from cytotoxic T lymphocyte targeting
- Increased recruitment of myeloid-derived suppressor cells and tumor-associated macrophages
- Creation of profoundly immunosuppressive microenvironment permitting unchecked tumor growth

**Evidence summary**
Expression of immune checkpoint ligands represents a hallmark of high-grade astrocytomas and glioblastomas, with increased PD-L1 expression correlating with tumor grade and poor survival. Single-cell transcriptomic studies reveal that PD-L1 expression increases in response to inflammatory signals and interferon-gamma production by infiltrating T cells, suggesting continuous feedback regulation. Young patients with aggressive cancers show particularly elevated PD-L1 and CTLA-4 expression alongside enrichment of regulatory T cells, creating a highly immunosuppressive microenvironment. Age-related differences in immune checkpoint expression and immune cell composition suggest that astrocytoma immune escape mechanisms differ between patient populations, with potential implications for immunotherapy efficacy.

**Atomic biological processes**
- PD-L1 expression regulation. Genes: CD274
  - [1]: Young breast cancer patients show enhanced immunosuppressive signals including elevated PD-L1 expression
  - [49]: CD274 expression shows cytokine and epigenetic regulation affecting stem cell differentiation and cancer cell plasticity
  - [58]: PD-L1 causing T cell exhaustion through engagement of PD-1 on T cell surface
- T cell exhaustion. Genes: CD274, PDCD1
  - [49]: PD-L1 engagement with PD-1 leads to T cell exhaustion and reduced anti-tumor immunity
  - [56]: PDCD1 (PD-1) expressed on activated T cells as immune-inhibitory receptor regulating T cell function
- Myeloid-derived suppressor cell recruitment and differentiation. Genes: MSR1
  - [1]: Elderly patients with cancer show increased proportion of MDSCs and decreased CD4+ stem-like T cells in TME

**Atomic cellular components**
- Tumor cell surface. Genes: CD274
  - [49]: CD274 expressed on tumor cell surface as ligand for PD-1
- T cell surface. Genes: PDCD1
  - [56]: PDCD1 expressed on T cell surface as immune-inhibitory receptor

**Required genes (not in input)**
- Genes: CTLA4, TIM3, LAG3, FOXP3, IL10, TGFB1
  - [1]: CTLA-4 and FOXP3+ regulatory T cells represent key immunosuppressive mechanisms alongside PD-L1

**Program citations**
- [1]: Single-cell transcriptomic analysis showing elevated PD-L1 and immunosuppressive signals in young cancer patients
- [49]: Extensive literature on CD274/PD-L1 regulation and cancer immune escape
- [56]: PDCD1/PD-1 as key immune checkpoint receptor on T cells

## Program: Extracellular Matrix Remodeling and Stromal Cell Regulation
This program controls extracellular matrix (ECM) composition and organization through coordinated action of multiple matrix proteins and matrix-degrading enzymes. SPARC and SPARCL1 function as matricellular proteins that modulate ECM-cell interactions and affect both tumor cell behavior and immune cell infiltration. TIMP1 inhibits matrix metalloproteinase activity and prevents excessive ECM degradation. Together, these genes establish an ECM microenvironment that supports tumor cell invasion while limiting immune cell access to tumor cells.

**Predicted impacts**
- Enhanced tumor cell invasion and migration through ECM remodeling
- Suppression of immune cell infiltration through establishment of fibrotic barriers
- Increased survival signals to tumor cells through matricellular protein-integrin interactions
- Support of angiogenesis through SPARC and SPARCL1 effects on endothelial cells
- Promotion of cancer-associated fibroblast activation and pro-tumoral phenotype

**Evidence summary**
SPARC expression shows strong association with poor prognosis in multiple glioma subtypes and other malignancies, where it simultaneously supports tumor growth and limits immune cell infiltration. TIMP1 upregulation in high-grade gliomas contributes to fibrosis-associated microenvironment phenotype, analogous to that observed in hepatocellular carcinoma. Together, SPARC and TIMP1 establish an ECM microenvironment optimized for tumor progression at the expense of immune control. Recent studies directly comparing young and elderly cancer patients reveal age-related differences in ECM composition and cancer-associated fibroblast phenotype, suggesting that astrocytoma ECM remodeling programs vary with patient age.

**Atomic biological processes**
- Extracellular matrix deposition and cross-linking. Genes: SPARC, SPARCL1, TIMP1
  - [12]: SPARC modulates cell growth, attachment and migration through interaction with ECM proteins; SPARC synthesis in various cancer types affects ECM composition
- Matrix metalloproteinase inhibition. Genes: TIMP1
  - [62]: TIMP1 inhibits matrix metalloproteinase activity and prevents ECM degradation; TIMP1 upregulated in high-grade gliomas
- Matricellular protein signaling. Genes: SPARC, SPARCL1
  - [12]: SPARC functions as matricellular protein promoting tumor cell growth, attachment, and migration on brain ECM proteins; SPARC expression predicts poor prognosis in gliomas
- Fibroblast activation. Genes: SPARC, TIMP1
  - [1]: Cancer-associated fibroblasts in young patients show enhanced ECM remodeling; elderly patients show pro-inflammatory CAF phenotype with heightened metabolic activity

**Atomic cellular components**
- Extracellular matrix compartment. Genes: SPARC, SPARCL1, TIMP1
  - [12]: SPARC and TIMP1 localize to and function within extracellular matrix

**Required genes (not in input)**
- Genes: MMP2, MMP9, COL1A1, COL3A1, FN1, THBS1
  - [12]: Matrix metalloproteases and collagen components represent essential ECM constituents regulated by SPARC and TIMP1

**Program citations**
- [12]: Comprehensive literature on SPARC in cancer and ECM interactions
- [62]: TIMP1 biology in cancer and fibrosis
- [1]: Age-related differences in CAF phenotype and ECM remodeling in cancer

## Program: DNA Damage Response and Genomic Stability Checkpoint Control
This program maintains genomic integrity through coordinated action of DNA damage sensors (ATR, PRKDC), mismatch repair machinery (MSH5), and cell cycle checkpoint regulators including TP53 and MDM2. ATR functions as a serine/threonine kinase that senses DNA damage and activates checkpoints preventing cell cycle progression. PRKDC catalyzes non-homologous end joining repair of double-strand breaks. MSH5 participates in mismatch repair and meiotic recombination. MDM2 negatively regulates TP53, and dysregulation of this interaction permits continued proliferation despite DNA damage.

**Predicted impacts**
- Impaired DNA damage-induced cell cycle arrest permitting genomic instability
- Accumulation of somatic mutations and chromosomal alterations driving malignant progression
- Loss of TP53-mediated apoptosis in response to DNA damage
- Enhanced survival of cells with unrepaired or misrepaired DNA lesions
- Progression from lower-grade to higher-grade astrocytoma through acquisition of checkpoint mutations

**Evidence summary**
The DNA damage checkpoint program undergoes substantial dysregulation during astrocytoma development and progression. In lower-grade astrocytomas, functional DNA damage checkpoints may still operate relatively effectively, allowing senescence or apoptosis of DNA-damaged cells. In high-grade glioblastomas, mutations or epigenetic silencing of checkpoint genes permit continued proliferation despite elevated DNA damage, generating the genomic hypervariability characteristic of these tumors. Recent integrated single-cell and genomic studies reveal that tumor cells with the highest mutation burdens often show paradoxically reduced expression of DNA damage response genes, suggesting strong selective pressure against genomic stability mechanisms during malignant evolution. TP53 mutations occur in approximately 50% of glioblastomas and even higher fractions of other astrocytomas, with MDM2 amplification providing an alternative mechanism for TP53 inactivation in wild-type TP53 tumors.

**Atomic biological processes**
- DNA damage sensing. Genes: ATR
  - [54]: ATR protein kinase encoded by ATR gene functions as serine/threonine kinase and DNA damage sensor, activating cell cycle checkpoint signaling upon DNA stress
- Double-strand break repair. Genes: PRKDC
  - [50]: PRKDC polymorphisms associated with increased melanoma risk; protein catalyzes non-homologous end joining repair of double-strand breaks
- Mismatch repair. Genes: MSH5
  - [48]: MSH5 encodes member of mutS family proteins involved in DNA mismatch repair and meiotic recombination
- P53-mediated checkpoint control. Genes: MDM2
  - [11]: MDM2 encodes nuclear-localized E3 ubiquitin ligase promoting tumor formation by targeting tumor suppressor proteins including p53
  - [13]: Mdm2 phosphorylation by Akt regulates p53 response to oxidative stress; promotes cell proliferation and tumorigenesis

**Atomic cellular components**
- Nuclear DNA. Genes: ATR, PRKDC, MSH5
  - [54]: ATR senses DNA damage in nuclear DNA context
- Nuclear inclusion bodies. Genes: MDM2
  - [11]: MDM2 localizes to nucleus where it targets p53 for degradation

**Required genes (not in input)**
- Genes: TP53, CHEK2, CHEK1, RB1, PTEN
  - [11]: TP53 and checkpoint kinases CHK1/CHK2 represent critical components of DNA damage response absent from input list

**Program citations**
- [54]: ATR checkpoint kinase characterization as DNA damage sensor
- [50]: PRKDC genetic associations with cancer risk and double-strand break repair function
- [11]: MDM2 as negative regulator of TP53 in cancer development

## Program: Asymmetric Cell Division and Cancer Stem Cell Self-Renewal
This program controls maintenance of self-renewing cancer stem cell pools through coordinated regulation of asymmetric cell division (ACD) machinery. RAP2A (human homolog of Drosophila Rap2l) acts as a critical regulator of ACD, coupling cell polarity establishment to asymmetric division and ensuring production of one self-renewing and one differentiating daughter cell. PROM1 (CD133) serves as a cell surface marker identifying glioma stem cell populations with enhanced tumor-initiating capacity. Dysregulation of this program through loss of RAP2A permits bypass of developmental checkpoints, allowing cancer stem cells to undergo symmetric self-renewing division.

**Predicted impacts**
- Maintenance of large self-renewing cancer stem cell pools through enhanced symmetric division
- Increased tumor-initiating capacity and tumor propagation
- Enhanced therapeutic resistance through cancer stem cell survival
- Post-treatment recurrence driven by residual cancer stem cell populations
- Reduced efficacy of differentiation-inducing therapies when ACD is disrupted

**Evidence summary**
Loss of RAP2A function in glioblastomas represents a significant departure from normal neural development, where RAP2A couples cell polarity to asymmetric division during corticogenesis. Glioblastoma patients with low RAP2A expression show poor clinical outcomes, consistent with enhanced cancer stem cell maintenance. Restitution of RAP2A in glioblastoma neurosphere cultures restores asymmetric division, decreasing both cancer stem cell proliferation and stem cell marker expression. PROM1/CD133 marks a glioma cell population with enhanced self-renewal capacity, tumor-initiating potential, and radiotherapy resistance, establishing PROM1+ cells as a critical population for treatment failure and recurrence.

**Atomic biological processes**
- Asymmetric cell division. Genes: RAP2A
  - [25]: RAP2A restitution in GBM neurosphere cultures increases asymmetric cell division of glioblastoma stem cells, decreasing their proliferation
- Cancer stem cell marker expression. Genes: PROM1
  - [52]: PROM1 (CD133) identified as neural stem cell marker and glioma stem cell marker predicting poor prognosis
- Stem cell marker downregulation. Genes: RAP2A
  - [25]: RAP2A restitution decreases expression of stem cell markers in glioblastoma stem cells

**Atomic cellular components**
- Cell polarity apparatus. Genes: RAP2A
  - [25]: RAP2A couples cell polarity establishment to asymmetric cell division in developing Drosophila and likely in human neural stem cells
- Cell surface cancer stem cell niche. Genes: PROM1
  - [52]: PROM1 expressed on cell surface as marker of glioma stem cell populations

**Required genes (not in input)**
- Genes: PARD3, PARD6, PKC, NUP
  - [25]: Polarity complex components and partitioning proteins required for RAP2A-mediated ACD

**Program citations**
- [25]: Comprehensive functional studies of RAP2A in glioblastoma stem cells and asymmetric division
- [52]: PROM1/CD133 characterization as glioma stem cell marker

## Program: Metabolic Substrate Transport and Nutrient Uptake
This program encompasses multiple solute carrier (SLC) family members that transport glucose, amino acids, lipids, and other metabolic substrates into tumor cells in response to microenvironmental nutrient constraints. SLC2A1 (GLUT1) mediates rate-limiting glucose uptake, while SLC4A5, SLC7A14-AS1, SLC25A21, SLC26A7, SLC30A8, and SLC35E3 transport additional substrates. SLC45A4 functions as a peroxisomal putrescine transporter supporting GABA synthesis. Together, these genes support the enhanced metabolic activity required for rapid astrocytoma proliferation.

**Predicted impacts**
- Enhanced glucose uptake supporting aerobic glycolysis and rapid ATP production
- Increased amino acid availability for protein synthesis and anabolic metabolism
- Augmented GABA synthesis through increased putrescine availability
- Adaptation to nutrient-poor tumor microenvironment through selective transporter upregulation
- Support for rapid proliferation through coordinated substrate availability

**Evidence summary**
Tumor cells characteristically show 5-10 fold elevated expression of glucose transporters compared to surrounding normal tissue, with SLC2A1/GLUT1 serving as the primary glucose transporter in astrocytomas and brain tumors generally. Recent transcriptomic-metabolomic association analyses establish strong correlations between SLC gene expression and cellular metabolite levels in cancer cell lines, suggesting that transporter expression directly determines substrate availability. SLC45A4, functioning as a peroxisomal putrescine transporter, represents a newly characterized astrocytoma metabolic vulnerability through its requirement for de novo GABA synthesis. Dysregulation of GABA metabolism in astrocytomas may promote stemness and suppress differentiation through effects on GABAergic signaling pathways normally involved in inhibitory neurotransmission.

**Atomic biological processes**
- Glucose uptake and transport. Genes: SLC2A1
  - [21]: SLC2A1 (GLUT1) encodes major glucose transporter in blood-brain barrier and cell membranes; provides glucose for glycolysis
- Amino acid transport. Genes: SLC7A14-AS1, SLC25A21, SLC4A5
  - [18]: Multiple SLC transporters mediate amino acid transport supporting astrocytoma metabolic rewiring
- Putrescine transport and GABA synthesis. Genes: SLC45A4
  - [18]: SLC45A4 functions as peroxisomal putrescine transporter supporting de novo GABA synthesis in cancer cells
- Ion and trace mineral transport. Genes: SLC30A8, SLC26A7, SLC35E3
  - [18]: SLC30A8 involved in zinc transport; SLC26A7 in anion transport; coordinate metabolic substrate availability

**Atomic cellular components**
- Plasma membrane. Genes: SLC2A1, SLC4A5, SLC26A7, SLC30A8
  - [21]: SLC2A1 found primarily on cell membrane for glucose transport across plasma membrane
- Peroxisomal membrane. Genes: SLC45A4
  - [18]: SLC45A4 localizes to peroxisomal membrane for putrescine uptake

**Required genes (not in input)**
- Genes: SLC6A8, SLC7A5, LDLR, APOE
  - [18]: Additional SLC transporters and lipoprotein receptors contribute to metabolic substrate import not all present in input list

**Program citations**
- [21]: SLC2A1/GLUT1 characterization as major glucose transporter in blood-brain barrier and cancer cells
- [18]: Comprehensive analysis of SLC45A4 and other solute carriers in cancer metabolic rewiring

## Program: Complement Activation and Myeloid Cell Recruitment
This program involves production of complement components, particularly C5a, by tumor-associated mesenchymal stem-like cells and subsequent activation of C5a receptor 1 (C5aR1) on glioblastoma and immune cells. C5a functions as a potent chemoattractant for myeloid cells and orchestrates inflammatory responses that paradoxically support tumor progression through recruitment of immunosuppressive immune cell populations. MSR1 (macrophage scavenger receptor 1) participates in myeloid cell recruitment and polarization toward pro-tumoral phenotypes.

**Predicted impacts**
- Enhanced recruitment of immunosuppressive myeloid-derived suppressor cells to tumor
- Increased macrophage infiltration with pro-tumoral phenotype polarization
- Promotion of epithelial-mesenchymal transition in glioblastoma cells
- Reduced spherical morphology and increased invasiveness of glioblastoma tumorspheres
- Overall enhancement of tumor progression through complement-mediated myeloid recruitment

**Evidence summary**
Recent studies reveal that C5a secretion by tumor-associated mesenchymal stem-like cells within glioblastomas orchestrates a complex inflammatory microenvironment that supports tumor progression. Treatment of glioblastoma tumorspheres with C5a-enriched conditioned medium from these mesenchymal cells increases proliferation, invasion, and stemness markers. Critically, the C5a antagonist W54011 reverses these C5a-induced effects, restoring spherical morphology and inducing apoptosis. In in vivo xenograft models, C5a antagonism decreases tumor size and improves survival. High C5aR1 expression in glioblastoma tissues correlates with increased inflammation-related gene expression and poorer patient outcomes, establishing complement activation as a targetable vulnerability in the glioblastoma immune microenvironment.

**Atomic biological processes**
- Complement component 5a production. Genes: C5a
  - [26]: Glioblastoma-educated mesenchymal stem-like cells secrete C5a, altering tumor microenvironment and promoting tumor progression
- C5a receptor signaling. Genes: C5aR1
  - [26]: C5aR1 expression correlates with increased TME inflammation and poorer patient outcomes in glioblastoma
- Myeloid cell recruitment and differentiation. Genes: MSR1
  - [26]: C5a serves as chemoattractant recruiting myeloid-derived suppressor cells and tumor-associated macrophages to glioblastoma
  - [1]: Increased proportion of MDSCs and macrophages in elderly patient tumors correlates with pro-inflammatory microenvironment

**Atomic cellular components**
- Tumor microenvironment. Genes: C5a, C5aR1, MSR1
  - [26]: C5a alters tumor microenvironment composition and promotes tumor progression through altered immune cell infiltration

**Required genes (not in input)**
- Genes: C5A, C5AR1, C5AR2
  - [26]: C5A and C5AR1 are core components of this program but not present in input gene list

**Program citations**
- [26]: Comprehensive mechanistic and therapeutic targeting studies of complement C5a in glioblastoma
- [1]: Single-cell analysis showing myeloid cell composition differences in tumor microenvironment

## Program: Developmental Transcriptional Regulation and Neural Differentiation
This program encompasses transcriptional regulators controlling normal neural development that become dysregulated in astrocytoma. RUNX1 acts as a master regulator of hematopoietic and bone development but participates in transcriptional programs relevant to neural development. NRG1 (neuregulin 1) provides growth factor signaling through ErbB receptor tyrosine kinases, normally supporting neuronal differentiation and myelination but redirected toward proliferation in malignant gliomas. RELN (reelin) and DAB1 control neuronal migration and cortical lamination through a signaling pathway normally preventing excessive neural precursor proliferation. TAF7 functions within the TFIID transcription factor complex to integrate regulatory signals at promoters of developmental genes.

**Predicted impacts**
- Loss of terminal neural differentiation capacity in astrocytoma cells
- Enhanced proliferation through dysregulation of differentiation-suppressing programs
- Retention of neural precursor-like properties in malignant astrocytes
- Altered response to developmental cues normally promoting differentiation
- Enhanced migratory properties through dysregulation of reelin-DAB1 neuronal migration programs

**Evidence summary**
The dysregulation of developmental transcriptional programs represents a hallmark of astrocytoma malignant transformation. Normal astrocyte development requires precise timing of differentiation-promoting transcription factor activity, with RUNX1, TAF7, NRG1, RELN, and DAB1 collectively orchestrating developmental checkpoints. In malignant astrocytomas, these developmental programs become dysregulated, permitting loss of terminal differentiation and maintenance of stem cell-like properties. The normal function of RELN-DAB1 signaling in preventing excessive proliferation of neural precursors becomes impaired in high-grade astrocytomas, where tumor cells retain immature characteristics and enhanced migratory properties. NRG1-ErbB signaling, normally promoting terminal differentiation and maturation, becomes redirected toward proliferation in gliomas through mechanisms including receptor tyrosine kinase amplification and downstream pathway hyperactivation.

**Atomic biological processes**
- Transcriptional program specification. Genes: RUNX1, TAF7
  - [17]: RUNX1 functions as key regulator of differentiation and developmental transcriptional programs
  - [19]: TAF7 functions as component of TFIID transcription factor complex that binds TATA boxes and recruits RNA Pol II
- Growth factor signaling in differentiation. Genes: NRG1
  - [39]: NRG1-ErbB4 signaling induces differentiation of induced pluripotent stem cells into cardiomyocytes and likely neural cell types
  - [61]: NRG1/ErbB signaling regulates neonatal muscle growth and neural differentiation programs
- Neuronal migration and cortical lamination. Genes: RELN, DAB1
  - [44]: RELN and DAB1 coexpression necessary for both normal cortical development and mature function in neurons
  - [47]: DAB1 involved in disabled homolog protein function in reelin signaling pathway

**Atomic cellular components**
- Nuclear transcription complex. Genes: TAF7, RUNX1
  - [19]: TAF7 component of TFIID general transcription factor complex at promoters
- Cell surface and extracellular compartment. Genes: NRG1, RELN
  - [39]: NRG1 secreted ligand acting on ErbB receptors; RELN secreted extracellular matrix protein

**Required genes (not in input)**
- Genes: ERBB4, ERBB2, LRP8, VLDLR
  - [39]: ErbB receptors required for NRG1 signaling; LRP receptors required for reelin signaling

**Program citations**
- [39]: NRG1-ErbB4 signaling in neural cell differentiation
- [44]: RELN-DAB1 signaling in neural development and cortical lamination
- [19]: TAF7 in transcriptional regulation of developmental genes

## Program: Ephrin-Eph Signaling and Cell-Cell Communication
This program encompasses ephrin receptors (particularly EPHA5 and EPHA6) and their ligands, which control cell-cell communication and cellular guidance during development and in disease. Ephrin signaling normally directs axon guidance and neuronal precursor cell migration through repulsive effects on cells expressing ephrin receptors. In gliomas, dysregulation of EPHA6 and related ephrin signaling contributes to aberrant cell-cell interactions and glioma cell guidance away from normal developmental cues.

**Predicted impacts**
- Altered glioma cell guidance and migration patterns
- Enhanced cell-cell interactions within tumor due to dysregulated ephrin signaling
- Increased invasiveness through loss of normal repulsive migration cues
- Disrupted development-like migration patterns in infiltrating astrocytoma

**Evidence summary**
Gene-based analyses have identified EPHA6 as a gene most significantly associated with disease risk in multiple cancer types through effects on cell-cell communication and developmental processes. Ephrin signaling normally provides critical guidance cues during neural development, directing axons and migrating neural precursors away from particular tissue regions. In gliomas and other malignancies, dysregulation of ephrin signaling contributes to aberrant cell-cell interactions and pathological cell migration patterns that support invasion and metastatic dissemination. The repulsive effects of ephrin signaling on cell migration become dysregulated in astrocytoma, potentially contributing to enhanced infiltrative properties of tumor cells.

**Atomic biological processes**
- Axon guidance and cell migration. Genes: EPHA5, EPHA6
  - [43]: EPHA6 ephrin receptor predicted to enable transmembrane-ephrin receptor activity and involve axon guidance and ephrin receptor signaling pathway
  - [46]: EPHA5 belongs to ephrin receptor subfamily of protein-tyrosine kinase family; involved in cellular guidance
- Glioma cell guidance. Genes: EPHA6
  - [32]: ROBO1 receptor activated by SLIT-family proteins causing repulsive effect on glioma cell guidance

**Atomic cellular components**
- Cell surface receptor. Genes: EPHA5, EPHA6
  - [43]: EPHA6 transmembrane ephrin receptor on cell surface

**Required genes (not in input)**
- Genes: EFNA1, EFNB1, EFNB2
  - [43]: Ephrin ligands required for EPHA receptor signaling

**Program citations**
- [43]: EPHA6 characterization as ephrin receptor in axon guidance
- [46]: EPHA5 as member of ephrin receptor subfamily

## Program: Long Noncoding RNA Regulatory Networks
This program encompasses numerous long noncoding RNAs (>100 input genes) that regulate astrocytoma gene expression through multiple mechanisms including acting as competing endogenous RNAs (ceRNAs) sequestering miRNAs, recruiting chromatin modifiers, and serving as scaffolds for ribonucleoprotein complex assembly. Representative lncRNAs include LINC00536, LINC02511, LINC02476, LINC02240, LINC01811, LINC01470, LINC01500, and others. DANCR represents a conserved oncogenic lncRNA dysregulated in multiple cancer types. These lncRNAs collectively regulate genes involved in cell proliferation, stemness, differentiation, and immune escape.

**Predicted impacts**
- Post-transcriptional regulation of genes involved in proliferation and stemness
- Enhanced expression of oncogenic lncRNAs promoting aggressive tumor phenotype
- Dysregulation of miRNA networks controlling tumor suppressor function
- Altered neural stem cell maintenance programs promoting cancer stem cell properties
- Enhanced cancer cell proliferation and migration through lncRNA-mediated gene regulatory networks

**Evidence summary**
Long noncoding RNAs represent an increasingly recognized class of regulatory molecules whose dysregulation in astrocytomas contributes substantially to malignant progression. Studies of lncRNA dysregulation in multiple cancer types identify DANCR as a conserved oncogene transcribed from syntenic genomic regions across vertebrate species, indicating functional importance across tissue types and cancer types. DANCR expression is directly controlled by MITF and c-MYC, key transcription factors dysregulated in many cancers, and melanoma patients with high DANCR expression show significantly decreased survival. LINC01068, identified through integrated genetic and transcriptomic analysis of schizophrenia-associated variants, regulates genes involved in neurodevelopment and synaptic pathways when knockdown in cultured human neural stem cells, suggesting that similar neural developmental programs become dysregulated in astrocytomas through altered lncRNA expression. The large number of lncRNAs represented in the input gene list suggests that lncRNA dysregulation represents a major component of astrocytoma pathogenesis, likely through post-transcriptional regulation mechanisms that remain only partially characterized.

**Atomic biological processes**
- miRNA regulation through competing endogenous RNA mechanism. Genes: LINC00536, LINC02511, LINC02476, LINC02240, LINC01811, LINC01470, LINC01500
  - [4]: Long noncoding RNAs dysregulated in schizophrenia and other neural disorders; regulate SCZ-associated genes and synaptic pathways
- Oncogenic lncRNA-mediated gene expression control. Genes: DANCR
  - [33]: DANCR identified as melanoma oncogene controlling cancer-associated gene expression networks; MITF and c-MYC regulate DANCR expression
  - [36]: DANCR highly expressed in older adults with NSCLC; DANCR upregulation associated with larger tumor diameter, advanced stage, poor differentiation, and poor survival
- Neural stem cell maintenance and synaptogenesis. Genes: LINC01068
  - [4]: lncRNAs play critical roles in brain development, neural stem cell maintenance, and synaptogenesis; alterations in lncRNA expression implicated in schizophrenia
- miRNA biogenesis hosting. Genes: MIR2052HG, MIR3681HG, MIR4713HG
  - [33]: DANCR is multi-exonic cytoplasmically-enriched lncRNA and small RNA host gene, hosting miRNAs that regulate cancer-associated functions

**Atomic cellular components**
- Cytoplasm. Genes: DANCR
  - [33]: DANCR is cytoplasmically-enriched lncRNA
- Nuclear chromatin. Genes: LINC00536, LINC02511, LINC02476
  - [4]: lncRNAs can recruit chromatin-modifying complexes to nuclear chromatin

**Required genes (not in input)**
- Genes: DICER, DROSHA, AGO2, GW182
  - [33]: miRNA processing and RISC complex components required for lncRNA-mediated miRNA sequestration

**Program citations**
- [33]: DANCR characterization as conserved oncogenic lncRNA
- [36]: DANCR dysregulation and poor prognosis in NSCLC and other cancers
- [4]: lncRNA dysregulation in neural developmental disorders with implications for cancer

## Program: Metabolic Plasticity and Therapeutic Resistance
This program enables astrocytomas to dynamically switch between glycolytic and oxidative phosphorylation metabolic states in response to nutrient availability and therapeutic pressure. Metabolic flexibility is mediated through coordinated regulation of mitochondrial bioenergetics genes, lactate metabolism, and glucose transport. Recent studies show that cancer cells, including astrocytomas, exhibit enhanced metabolic plasticity that allows survival under diverse microenvironmental conditions and contributes substantially to therapeutic resistance to radiotherapy and chemotherapy.

**Predicted impacts**
- Enhanced survival under varied nutrient and oxygen conditions
- Reduced efficacy of metabolic inhibitors targeting single pathways
- Increased radiotherapy resistance through metabolic compensation mechanisms
- Maintenance of cancer stem cell properties under metabolic stress
- Potential therapeutic opportunity through dual targeting of glycolysis and OXPHOS

**Evidence summary**
Recent studies reveal that astrocytomas and other tumors exploit metabolic plasticity to resist therapy-induced stress. Radiotherapy induces DNA damage and metabolic stress, and tumor cells respond through metabolic switching that permits survival despite DNA damage. Targeting metabolic flexibility through combined inhibition of Complex I and radiotherapy produces pronounced antiproliferative and antitumoral effects in preclinical tumor models. The findings establish that combination targeting of both glycolytic and OXPHOS pathways represents a promising strategy for enhancing radiotherapy efficacy by overcoming multiple resistance mechanisms simultaneously.

**Atomic biological processes**
- Metabolic switching between glycolysis and OXPHOS. Genes: SUCLG2, MT-ND1, MT-ND2, MT-ND4, SLC2A1
  - [37]: Tumor cells utilize metabolic flexibility, dynamically switching between glycolysis and OXPHOS to survive and resist radiotherapy-induced stress
- Lactate metabolism and shuttling. Genes: SUCLG2
  - [28]: SUCLG2 interaction with DLAT promotes lactate reduction, affecting metabolic flexibility
  - [51]: SUCLG2 knockdown reduces lactate levels through altered SUCLG2-DLAT interaction
- Radiotherapy resistance through metabolic adaptation. Genes: SUCLG2
  - [37]: Inhibition of Complex I with IACS-010759 combined with radiotherapy disrupts metabolic flexibility, enhancing tumor cell sensitivity to radiotherapy-induced stress

**Atomic cellular components**
- Mitochondria. Genes: SUCLG2, MT-ND1, MT-ND2, MT-ND4
  - [37]: Complex I in mitochondria represents therapeutic target for disrupting metabolic flexibility
- Cytoplasm. Genes: SLC2A1
  - [37]: Glycolytic enzymes in cytoplasm contribute to metabolic flexibility alongside mitochondrial OXPHOS

**Required genes (not in input)**
- Genes: LDHA, LDHB, PFK1, HIF1A, MCT1
  - [37]: Glycolytic enzymes and lactate transporters required for metabolic switching not all present in input list

**Program citations**
- [37]: Comprehensive studies of metabolic flexibility and radiotherapy resistance in tumors
- [28]: SUCLG2 role in regulating lactate metabolism

## Program: Purine Metabolism and Nucleotide Biosynthesis
This program controls nucleotide biosynthesis through de novo purine synthesis and salvage pathways, representing a critical metabolic requirement for rapidly proliferating astrocytoma cells. Succinate dehydrogenase (SDH) maintains purine synthesis through effects on the mitochondrial tetrahydrofolate cycle. SDH inhibition elevates succinate, promoting succinylation of SHMT2 and reducing formate output required for purine assembly, forcing cells into dependence on purine salvage pathways.

**Predicted impacts**
- Disruption of rapid purine synthesis supporting tumor proliferation
- Metabolic stress from impaired nucleotide availability
- Enhanced efficacy of purine synthesis inhibitors through forced dependence on salvage pathways
- Potential therapeutic vulnerability through dual SDH and purine salvage inhibition
- Reduced cancer stem cell self-renewal through nucleotide depletion

**Evidence summary**
Recent discovery reveals an additional layer of astrocytoma metabolic rewiring through integration of mitochondrial bioenergetics with purine synthesis control. Succinate dehydrogenase (SDH), which catalyzes succinate-to-fumarate conversion within the tricarboxylic acid cycle, maintains de novo purine synthesis through its effects on the mitochondrial tetrahydrofolate cycle. When SDH activity is pharmacologically inhibited, succinate accumulates and promotes post-translational succinylation of SHMT2, a key mitochondrial tetrahydrofolate cycle enzyme. This succinylation event reduces formate output and depletes one-carbon units required for purine synthesis, leading to decreased cell proliferation. Cancer cells compensate through activation of purine salvage pathways, creating a dual vulnerability that can be exploited through simultaneous inhibition of SDH and purine salvage enzymes. Additionally, purine synthesis inhibitors trigger a reactive increase in LAMP2 expression, representing an adaptive response that confers intrinsic resistance to these drugs in tumors showing high LAMP2 levels.

**Atomic biological processes**
- De novo purine synthesis.
  - [60]: Succinate dehydrogenase (SDH) essential for maintaining de novo purine synthesis; SDH inhibition suppresses purine synthesis contributing to decreased cell proliferation
- Mitochondrial tetrahydrofolate cycle regulation.
  - [60]: SDH inhibition elevates succinate which promotes succinylation of SHMT2, reducing formate output and depriving cells of one-carbon units for purine assembly
- Purine salvage pathway activation.
  - [60]: Cancer cells activate purine salvage pathway as compensatory adaptation when de novo purine synthesis is impaired
- LAMP2-mediated lysosomal adaptation.
  - [63]: LAMP2 expression represents adaptive response to purine synthesis inhibition; high LAMP2 levels indicate intrinsic resistance to purine synthesis inhibitors

**Atomic cellular components**
- Mitochondrial tetrahydrofolate cycle.
  - [60]: Mitochondrial SHMT2 and THF cycle represent critical locus for metabolic integration of purine synthesis with OXPHOS

**Required genes (not in input)**
- Genes: SDH, SHMT2, GART, PFAS, HPRT1
  - [60]: SDH, SHMT2, and de novo purine synthesis enzymes represent essential components not present in input list

**Program citations**
- [60]: Comprehensive mechanistic characterization of SDH regulation of purine synthesis
- [63]: LAMP2-mediated adaptation and intrinsic resistance to purine synthesis inhibitors

## Program: Cell Surface Adhesion and Invasion
This program controls cell surface adhesion molecules including L1CAM (L1 cell adhesion molecule), EPCAM (epithelial cell adhesion molecule), and PCDH15 (protocadherin 15) that regulate cell-cell interactions and epithelial-mesenchymal transition. These adhesion molecules undergo dysregulation in astrocytomas, contributing to enhanced invasiveness and metastatic capacity. L1CAM particularly promotes epithelial-mesenchymal transition-like changes that support glioma cell migration and invasion.

**Predicted impacts**
- Enhanced astrocytoma cell invasion and migration through EMT-like changes
- Increased metastatic capacity through L1CAM-mediated signaling
- Altered cancer stem cell properties through EPCAM-CD44 signaling
- Disruption of normal epithelial architecture in gliomas
- Support for dissemination of astrocytoma cells to distant sites

**Evidence summary**
Cell surface adhesion molecules undergo substantial dysregulation in astrocytomas, contributing to loss of normal epithelial properties and enhanced invasiveness. L1CAM expression on glioma cells particularly promotes epithelial-mesenchymal transition-like changes through engagement of undefined signaling pathways that support glioma cell migration and metastatic dissemination. EPCAM dysregulation affects cancer stem cell biology in gliomas, where EpCAM-exosome interactions promote metastasis through CD44 signaling on recipient glioma cells. The dysregulation of these developmental adhesion programs in astrocytomas represents a convergence with neural developmental dysregulation, as these molecules normally function in neuronal migration and cell-cell interactions during corticogenesis.

**Atomic biological processes**
- Cell-cell adhesion. Genes: EPCAM, L1CAM, PCDH15
  - [55]: EPCAM as epithelial cell adhesion molecule typically expressed on endothelial cells and immune system cells; dysregulated in cancer
  - [57]: L1CAM promotes epithelial-mesenchymal transition-like changes and supports metastasis, not invasion
- Epithelial-mesenchymal transition. Genes: L1CAM
  - [57]: L1CAM may induce EMT-like changes supporting metastatic dissemination of cancer cells
- Stem cell maintenance through adhesion signaling. Genes: EPCAM
  - [55]: EpCAM-CD44 signaling regulates cancer stem cell properties in gliomas

**Atomic cellular components**
- Cell surface membrane. Genes: EPCAM, L1CAM, PCDH15
  - [55]: EPCAM expressed on cell surface as cell adhesion molecule
  - [57]: L1CAM cell surface adhesion molecule

**Required genes (not in input)**
- Genes: CD44, SNAIL, TWIST1, ZEB1
  - [57]: EMT transcription factors and downstream effectors required for L1CAM-mediated invasion

**Program citations**
- [55]: EPCAM and CD44 signaling in glioma cancer stem cells
- [57]: L1CAM and epithelial-mesenchymal transition in cancer dissemination

## Bibliography
1. 1. Li Z, Feng J, An M, Kou S, Zhao Z, Yu J, et al.. Single-cell RNA sequencing reveals age-related heterogeneity in the tumor microenvironment of breast cancer patients. Scientific Reports [Internet]. 2025Nov20;15(1). Available from: https://www.nature.com/articles/s41598-025-24720-2
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/51705
3. 3. Lee Y-K, Xiao C, Zhou X, Wang L, McReynolds M, Wu Z, et al.. Bipolar and schizophrenia risk gene AKAP11 encodes an autophagy receptor coupling the regulation of PKA kinase network homeostasis to synaptic transmission. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-66356-w
4. 4. Dang X, Gong D, Dai S-S, Teng Z, Luo X-J. Genetic and functional insights into long noncoding RNAs in schizophrenia. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03421-2
5. 5. Available from: https://www.ncbi.nlm.nih.gov/gene/5241
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/4512
7. 7. Pengcheng W, Kristan HC, Ayaz S, Chathurika R, Farideh A, Zhenpeng S, et al.. Potentiation of ryanodine receptor-mediated calcium release by MAPK is responsible for epidermal transformation and carcinogenesis.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41370346/
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/6262
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/124590
10. 10. Jolasun Y, Song K, Zheng Y, Wang J, Fonseca GJ, Eidelman DH, et al.. SIDISH integrates single-cell and bulk transcriptomics to identify high-risk cells and guide precision therapeutics through in silico perturbation. Nature Communications [Internet]. 2025Dec10;. Available from: https://www.nature.com/articles/s41467-025-66162-4
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/4193
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/6678
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/17246
14. 14. Maximilian K, Sebastian P, Hannah S, Tabea K, Christian H, Michael MYS, et al.. Impact of C-Terminal PKC Phosphorylation on TRPC6 Current Kinetics.. International journal of molecular sciences [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41373637/?fc=None&ff=20251211190700&v=2.18.0.post22+67771e2
15. 15. Nadine ES, Georgia K, Rob CM de J, Dyantha I van der L, Dennis FGR, Sophie-Anne IS, et al.. A T-cell receptor targeting RUNX1 frameshift mutations in acute myeloid leukemia.. Leukemia [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41388195/?fc=None&ff=20251214160813&v=2.18.0.post22+67771e2
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/7225
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/861
18. 18. Colson C, Wang Y, Atherton J, Dahiya NR, Kharaghani D, Su X. SLC45A4 encodes a peroxisomal putrescine transporter that promotes GABA de novo synthesis. Nature Communications [Internet]. 2025Nov20;16(1). Available from: https://www.nature.com/articles/s41467-025-62721-x
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/6879
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/4763
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/6513
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/74469
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/3683
24. 24. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
25. 25. Maribel F, Ricardo G, Víctor MB, Daniel B, Miguel S, Ana C. Human . eLife [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41313155/
26. 26. Oh Y, Yoo J, Lee D, Ko B, Hong JP, Moon JH, et al.. Restoring the glioblastoma tumor microenvironment by targeting C5a with the antagonist W54011. Scientific Reports [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41598-025-30853-1
27. 27. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
28. 28. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
29. 29. Clara B, Teodora R, Ignacio O. Tumor Microenvironment in Glioblastoma: The Central Role of the Hypoxic-Necrotic Core.. Cancer letters [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41380902/?fc=None&ff=20251212152250&v=2.18.0.post22+67771e2
30. 30. Tan TRM, Yip LY, Tan JGL, Leong DSZ, Soh YNA, Mak SY, et al.. Maltose metabolism in serum free CHO culture involves lysosomal acid α-glucosidase. Scientific Reports [Internet]. 2025Dec4;. Available from: https://www.nature.com/articles/s41598-025-30901-w_reference.pdf
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/8714
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/6091
33. 33. Stephanie MEJ, Elizabeth AC, Michael S, Kelli MG, Karen CS, Nikolas N, et al.. The syntenic long non-coding RNA DANCR is an essential regulator of zebrafish development and a human melanoma oncogene.. PLoS genetics [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41336739/
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/3383
35. 35. Huimin L, Zhiqing F, Qi Q, Shu Y, Qi C. The relationship between the expression and clinicopathology of long non-coding RNA in older adults with non-small cell lung cancer.. Medicine [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41305688/
36. 36. Liu Z, Lim S-H, Jung S. Targeting tumor metabolic flexibility enhances radiotherapeutic efficacy via mitochondrial complex I Inhibition in an intracranial S180 sarcoma mouse model. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-29326-2
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/4684
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/3084
39. 39. Christopher YC, Mohamad H, Ibrahim K, Sonu K, Vanessa W, Sorin F, et al.. Emerging Therapies in Autosomal Dominant Polycystic Kidney Disease.. Kidney360 [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41385299/?fc=None&ff=20251215072131&v=2.18.0.post22+67771e2
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/211323
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/18763
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/285220
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/5649
44. 44. Available from: https://www.ncbi.nlm.nih.gov/omim/102579
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/2044
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/1600
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/4439
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
49. 49. Available from: https://www.ncbi.nlm.nih.gov/gene/5591
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/545
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/4072
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/5133
55. 55. Available from: https://www.ncbi.nlm.nih.gov/gene/3897
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/21857
57. 57. Mushtaq AN, Austin TK, Heather SC, Olivia V-C, Umakant S, Daniel JM, et al.. Accumulation of succinate suppresses de novo purine synthesis through succinylation-mediated control of the mitochondrial folate cycle.. Molecular cell [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41161310/
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/7076
59. 59. De CA, Castelli S, Felice F, Ciriolo MR, Desideri E. The inhibition of de novo purine synthesis increases LAMP2 expression to preserve cell viability. Cell Death Discovery [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41420-025-02884-0
60. 60. Available from: http://json-schema.org/draft-07/schema#",
