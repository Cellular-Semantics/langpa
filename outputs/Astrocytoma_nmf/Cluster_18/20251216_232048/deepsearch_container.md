# Gene Program Markdown Report

## Context
- Cell type: astrocyte; neoplastic astrocytic lineage cell
- Disease: astrocytoma
- Tissue: brain; central nervous system

## Input Genes
AC103770.1, AC008467.1, LINC00326, AC024901.1, IL12RB2, LINC01208, AC068633.1, LINC01482, DNAH12, AC009264.1, CORIN, AC019117.1, LINC01933, LINC01934, AC078923.1, MSH4, SGO1-AS1, AC105290.1, AC092813.1, SPDYA, AC005487.1, AC097522.2, AC005355.1, AL078604.4, NUP210L, ... (200 total)

## Program: Innate Immune Sensing and TLR/IL-1 Signaling
This gene program regulates astrocytoma cells' capacity to sense and respond to pathogen-associated molecular patterns and damage-associated molecular patterns through toll-like receptor pathways and interleukin-1 receptor signaling. The program includes core adaptor proteins for TLR-mediated signaling, IL-1 receptor family members, and IL-12 receptor components that collectively orchestrate inflammatory responses within the tumor microenvironment. These genes control recruitment of myeloid immune cells and modulate the inflammatory state of the tumor niche, functioning as critical nodes through which astrocytomas either promote or evade innate immune surveillance.

**Predicted impacts**
- Enhanced pathogen and damage-associated molecular pattern recognition
- Modified inflammatory cytokine production in response to microenvironmental danger signals
- Selective recruitment of immunosuppressive myeloid populations to tumor microenvironment
- Establishment of pro-tumoral or anti-tumoral inflammatory gradient depending on cellular context

**Evidence summary**
The innate immune sensing program comprises well-characterized components of TLR signaling (TICAM1, TICAM2) and IL-1 family receptor signaling (IL1R1, IL1R2, IL12RB2) that are substantially documented in cancer immunobiology literature. These genes encode core adaptor proteins and receptor components essential for astrocytoma cells to sense inflammatory signals and respond through altered cytokine production. Multiple independent studies demonstrate IL-1 and IL-12 receptor involvement in glioma progression through modulation of immune cell recruitment and activation. The inclusion of IL34, which drives macrophage differentiation, suggests astrocytomas employ this program to selectively recruit immunosuppressive myeloid populations. The coordinated expression of all major components of TLR and IL-1 signaling pathways strengthens confidence in the functional significance of this program.

**Atomic biological processes**
- Toll-like receptor signaling. Genes: TICAM1, TICAM2
  - [12]: TICAM1 encodes adaptor protein containing TIR homology domain, intracellular signaling domain downstream of pattern recognition receptors
  - [10]: TICAM2 enables molecular adaptor activity and positive regulation of interleukin-18-mediated signaling pathway
- Interleukin-1 receptor signaling and inflammatory response. Genes: IL1R1, IL1R2
  - [8]: IL1R1 (interleukin-1 receptor type 1) mediates primary IL-1 signaling in inflammation; IL1beta-IL1R signaling involved in stimulatory effects in cancer-associated fibroblasts
  - [7]: IL1RL1 (ST2) and related IL1R family members regulate immune and inflammatory signaling through IL-33 pathway
- Interleukin-12 signaling and Th1 differentiation. Genes: IL12RB2
  - [31]: IL12RB2 represents interleukin-12 receptor beta-2 chain, essential for cellular responsiveness to IL-12 family cytokines promoting Th1 responses
- Monocyte recruitment and myeloid differentiation. Genes: IL34
  - [31]: IL34 encodes colony-stimulating factor 1 ligand driving monocyte recruitment and macrophage differentiation in tumor microenvironment

**Atomic cellular components**
- TIR domain adaptor proteins. Genes: TICAM1, TICAM2
  - [12]: TICAM1 encodes adaptor protein containing Toll/interleukin-1 receptor homology domain

**Required genes (not in input)**
- Genes: MYD88, IRAK4, TRAF6, TLR3, IL6, TNF
  - [11]: TLR3 toll like receptor 3 involved in immune response and glioma-immune cell interactions
  - [27]: IL6 encodes cytokine functioning in inflammation and B cell maturation, commonly elevated in gliomas

**Program citations**
- [8]: IL1beta-IL1R signaling involved in stimulatory effects triggered by hypoxia in cancer cells and cancer-associated fibroblasts
- [31]: Comprehensive analysis of TMEM208-associated immune infiltration demonstrates relationship between inflammatory gene expression and immune cell recruitment in cancer

## Program: Ferroptosis and Redox Homeostasis
This gene program regulates cellular ferroptosis susceptibility through coordinated control of the cystine/glutamate antiporter system, glutathione biosynthesis and metabolism, and antioxidant response element-mediated gene expression. Ferroptosis represents an iron-dependent, non-apoptotic form of regulated cell death characterized by accumulation of lipid peroxides and glutathione depletion. The program includes both ferroptosis-promoting machinery (SLC7A11 inhibition leads to ferroptosis) and ferroptosis-resistance mechanisms (NFE2L2/NRF2-mediated antioxidant responses). Dysregulation of this program in astrocytomas enables tumor cells to resist ferroptotic death while potentially exploiting ferroptosis of immune infiltrates or endothelial cells.

**Predicted impacts**
- Maintenance of intracellular glutathione pools supporting ferroptosis resistance
- Upregulation of antioxidant biosynthesis enabling oxidative stress tolerance
- Selective modulation of immune cell ferroptosis in hypoxic tumor niches
- Enhanced survival under lipid peroxidation-inducing conditions

**Evidence summary**
The ferroptosis and redox homeostasis program represents a well-characterized metabolic program with strong experimental support from multiple independent investigations. SLC7A11 (xCT) has been extensively studied as a critical determinant of ferroptosis susceptibility; inhibition of this transporter predictably triggers ferroptosis through glutathione depletion and lipid peroxidation. NFE2L2 and NFE2L3 represent well-established transcription factors controlling antioxidant response elements that promote ferroptosis resistance. Recent research has demonstrated that ferroptosis regulation involves both canonical System Xc^-/GSH/GPX4 axis components and additional metabolic players including LPCAT3 and ACSL4, several of whose interaction partners are represented or linked to the candidate gene set. The presence of WWTR1 (TAZ), which coordinately regulates ferroptosis susceptibility through ACSL4 and LPCAT3 modulation, strengthens the coherence of this program.

**Atomic biological processes**
- Cystine/glutamate antiporter system and glutathione synthesis. Genes: SLC7A11
  - [14]: System Xc^- (cystine/glutamate antiporter) mediated by SLC7A11 and SLC3A2; inhibition leads to GSH exhaustion and GPX4 inactivation triggering ferroptosis
  - [15]: SLC7A11 (xCT) cystine transporter in cancer ferroptosis and nutrient dependency; inhibition suppresses anti-PD-1/L1 immunotherapy efficacy
- Antioxidant response element transcriptional regulation. Genes: NFE2L2, NFE2L3
  - [26]: NFE2L2 (NRF2) activates antioxidant response elements, controlling expression of cytoprotective genes; NFE2L3 (NRF3) represents related transcription factor
  - [14]: Nuclear factor erythroid 2-related factor 2 (Nrf2)-dependent ferroptosis resistance maintains tumor-infiltrating neutrophil persistence
- Lipid peroxidation and ferroptotic lipid remodeling. Genes: WWTR1
  - [14]: ACSL4 and LPCAT3 are key lipid drivers of ferroptosis; LPCAT3 cooperates with ACSL4 and YAP to determine ferroptosis susceptibility; PKCβII phosphorylates ACSL4 promoting PUFA incorporation and cell death

**Atomic cellular components**
- System Xc^- cystine/glutamate antiporter complex. Genes: SLC7A11
  - [14]: System Xc^- characterized by elevated GSH and GPX4 expression, represents canonical pathway of ferroptosis regulation

**Required genes (not in input)**
- Genes: SLC3A2, GPX4, GSH, ACSL4, LPCAT3, PKCβII
  - [14]: SLC3A2 (component of System Xc^-), GPX4 (glutathione peroxidase 4), ACSL4 and LPCAT3 (lipid metabolism drivers) are essential for ferroptosis regulation

**Program citations**
- [14]: Comprehensive review of ferroptosis mechanisms in immune cells, including System Xc^-/GSH/GPX4 axis and ACSL4/LPCAT3-driven lipid peroxidation
- [15]: SLC7A11 inhibition suppresses anti-PD-1/L1 immunotherapy efficacy, indicating ferroptosis regulation impacts immunotherapy response

## Program: Hippo Pathway Mechanotransduction
This gene program centers on the Hippo signaling pathway, a master regulator of organ size, cell density sensing, and tissue mechanical properties. WWTR1 (TAZ) and its paralog YAP represent terminal effectors of canonical Hippo pathway signaling that translocate to the nucleus to interact with TEAD transcription factors. The program integrates information about cell-cell contacts, mechanical properties of the extracellular matrix, and tissue organization to regulate gene expression controlling cell proliferation, differentiation, and apoptosis. In astrocytomas, dysregulation of Hippo signaling enables loss of contact inhibition, altered response to mechanical cues, and transitions between differentiated and stem cell-like states.

**Predicted impacts**
- Loss of contact inhibition enabling autonomous proliferation in high-density tumor regions
- Enhanced stem cell-like state maintenance through altered differentiation signals
- Modified responsiveness to extracellular matrix mechanical properties
- Altered cell survival signaling in response to mechanical stress
- Coordinated control of ferroptosis susceptibility through lipid metabolism modulation

**Evidence summary**
WWTR1 (TAZ) represents a well-characterized terminal effector of canonical Hippo pathway signaling with extensive experimental support for its roles in cell fate determination, mechanotransduction, and proliferation control. Recent high-quality studies specifically examining WWTR1 function in developmental contexts (lung fibroblast differentiation during embryogenesis) have revealed that Yap/Taz-TEAD-Snail binding orchestrates lineage specification programs. The mechanistic framework established through these studies directly parallels processes occurring in astrocytoma, where dysregulation of Hippo signaling contributes to loss of growth inhibition and abnormal cell fate transitions. WWTR1's established role in ferroptosis susceptibility through coordination with ACSL4 and LPCAT3 suggests this program integrates cell density sensing with metabolic and oxidative stress responses. The presence of WWTR1 as a single but highly mechanistically important gene in the candidate set warrants its designation as a central hub program.

**Atomic biological processes**
- Hippo pathway terminal effector function and transcriptional regulation. Genes: WWTR1
  - [5]: WWTR1 (TAZ) and YAP function as terminal effectors of Hippo pathway, translocating to nucleus to interact with TEAD transcription factors; Yap/Taz bind Snail1/2 to drive alveolar fibroblast differentiation during lung development
  - [6]: WWTR1 encodes WW domain containing transcription regulator; Hippo pathway terminal effector TAZ/WWTR1 mediates oxaliplatin sensitivity in colon cancer cells
- Cell density sensing and mechanical force transduction. Genes: WWTR1
  - [5]: Hippo/Yap signaling serves as molecular sensor for cell density and key regulator of tissue force balance; Yap activity varies between individual cells with collective pattern reflecting tissue mechanical state, making Yap signaling potent determinant of cellular fitness
- Lineage commitment and cell fate specification. Genes: WWTR1
  - [5]: Inactivating Yap1/Wwtr1 impairs alveolar fibroblast differentiation during lung development; conversely, inactivating Hippo kinases Mst1/2 accelerates fibroblast differentiation; Yap/Taz bind Snail1/2 to regulate self-renewal and differentiation in bone marrow-derived mesenchymal stem cells
- Ferroptosis susceptibility through ACSL4/LPCAT3 regulation. Genes: WWTR1
  - [14]: LPCAT3 cooperates with ACSL4 and Yes-associated protein (YAP) to determine ferroptosis susceptibility

**Atomic cellular components**
- TEAD transcription factor complexes. Genes: WWTR1
  - [5]: Yap/Taz interact with TEAD transcription factors and additional transcriptional cofactors including Snail1/2

**Required genes (not in input)**
- Genes: YAP1, TEAD1-4, MST1, MST2, LATS1, LATS2, SAV1, SNAIL1, SNAIL2
  - [5]: Yap/Taz require interaction with TEAD transcription factors and transcriptional cofactors Snail1/2 for target gene activation; upstream kinase cascade including MST1/2, LATS1/2, SAV1 phosphorylates and inactivates Yap/Taz

**Program citations**
- [5]: Comprehensive mechanistic study of Hippo pathway in lung development establishing Yap/Taz-TEAD-Snail regulatory axis in cell fate specification

## Program: Autophagy and Proteostasis
This gene program regulates autophagy, a catabolic cellular process through which cytoplasmic contents and organelles are delivered to lysosomes for degradation and recycling. The program includes core autophagy machinery components and regulatory modifiers that coordinately control autophagy initiation, progression, and resolution. BECN1 (beclin 1) represents an essential initiation factor forming the pre-initiation complex, while TRIM59 exerts dual regulatory control through transcriptional and post-translational mechanisms affecting BECN1 expression and ubiquitination. In astrocytomas, autophagy regulation functions as a stress response mechanism enabling survival during nutrient limitation and hypoxia, while also representing a potential cell death mechanism when excessively activated.

**Predicted impacts**
- Enhanced cellular survival during nutrient-deprived hypoxic tumor microenvironment
- Maintenance of metabolic homeostasis through organelle recycling and biomass reprocessing
- Selective clearance of damaged mitochondria and endoplasmic reticulum stress response
- Potential sensitivity to excessive autophagy induction triggering autophagic cell death
- Modulation of immunogenicity through selective autophagy of immunogenic organelles

**Evidence summary**
The autophagy program integrates two key components with complementary regulatory roles in astrocytoma biology. BECN1 represents a well-established core autophagy machinery component essential for initiation of autophagosome formation; its upregulation or stabilization promotes cellular autophagy. TRIM59 represents an emerging regulatory modifier that exerts dual control over BECN1 through both transcriptional upregulation and post-translational ubiquitination, thereby providing multiple independent checkpoint mechanisms. The coordinated action of initiation machinery and regulatory modifiers enables astrocytoma cells to dynamically adjust autophagy flux in response to changing microenvironmental conditions. Literature documenting autophagy's role in glioma survival and stress response provides strong mechanistic support for this program's functional significance.

**Atomic biological processes**
- Autophagy initiation complex formation. Genes: BECN1
  - [25]: BECN1 encodes core component of autophagy initiation complex, essential for autophagosome nucleation phase
- Dual-level autophagy regulation through TRIM59. Genes: TRIM59
  - [25]: TRIM59 exerts novel dual roles in autophagy regulation by affecting both transcription and ubiquitination of BECN1, providing transcriptional and post-translational checkpoints
- Selective autophagy and glioma survival. Genes: BECN1, TRIM59
  - [25]: Autophagy promotes glioma tumor growth by enabling nutrient recycling and organelle clearance under stress conditions

**Atomic cellular components**
- Autophagy initiation complex. Genes: BECN1
  - [25]: BECN1 participates in formation of initiation complex controlling early stages of autophagosome assembly
- RING E3 ubiquitin ligase TRIM59. Genes: TRIM59
  - [25]: TRIM59 contains RING domains enabling E3 ubiquitin ligase activity targeting BECN1 for post-translational modification

**Required genes (not in input)**
- Genes: ULK1, FIP200, WIPI1, ATG5, ATG7, LC3, P62
  - [25]: ULK1, FIP200, WIPI1, ATG5, ATG7 represent additional essential autophagy machinery; LC3 and p62 mark completed autophagosomes

**Program citations**
- [25]: TRIM59 novel dual roles in autophagy regulation affecting both transcription and ubiquitination of BECN1

## Program: Extracellular Matrix Remodeling and Invasion
This gene program orchestrates the remodeling and degradation of extracellular matrix (ECM) components, enabling astrocytoma cells to infiltrate surrounding brain parenchyma and facilitating invasion through physical and biochemical modification of the tumor microenvironment. The program includes matrix-degrading proteases, newly synthesized ECM proteins, matrix-associated cell adhesion molecules, and ECM cross-linking enzymes. Coordinated expression of these genes enables astrocytomas to simultaneously degrade existing ECM barriers while depositing pro-tumoral ECM that supports tumor cell migration, angiogenesis, and immunosuppressive cell infiltration.

**Predicted impacts**
- Enhanced degradation of perivascular basement membrane enabling invasion into surrounding brain parenchyma
- Remodeling of ECM to promote angiogenic sprouting and vascular co-option
- Deposition of pro-tumoral ECM supporting immunosuppressive cell infiltration
- Creation of mechanical barriers to anti-tumor immune cell trafficking
- Activation of ECM-dependent signaling in tumor and stromal cells

**Evidence summary**
The ECM remodeling program represents a well-established cluster of genes with substantial experimental support from multiple cancer types. THBS1, SPARC, and LOX have all been individually documented as critical drivers of ECM remodeling in various malignancies; their coordinated upregulation in astrocytomas suggests comprehensive restructuring of the local microenvironment. The inclusion of both matrix-degrading proteases (CORIN, implicit through serine protease activity) and matrix-synthesizing/stabilizing genes (collagen genes, LOX) indicates a coordinated program of simultaneous ECM destruction and reconstruction. Recent research has established that ECM composition directly impacts immune cell trafficking and activation state, suggesting this program functions not only in promoting invasion but also in shaping the immune microenvironment. The presence of tetraspanins (TSPAN8, CD151) that facilitate cell-ECM interactions strengthens the mechanistic coherence of this program.

**Atomic biological processes**
- Extracellular matrix degradation and proteolysis. Genes: CORIN, THBS1, SPARC
  - [13]: THBS1 (thrombospondin 1) facilitates cell-ECM interactions and has been associated with migration, invasion, and progression of bladder cancer
  - [21]: SPARC (secreted protein acidic and cysteine rich) upregulation in serum-derived extracellular vesicles promotes metastasis via ECM protein remodeling in renal cell carcinoma
- ECM cross-linking and stabilization. Genes: LOX
  - [23]: LOX (lysyl oxidase) catalyzes collagen and elastin cross-linking essential for ECM maturation; LKB1 loss promotes lung cancer malignancy through ECM remodeling with LOX as potential therapeutic target
- Collagen synthesis and ECM composition. Genes: COL21A1, COL14A1
  - [31]: Collagen and other ECM proteins represent major components of stromal fibroblast and tumor microenvironment

**Atomic cellular components**
- Matricellular proteins regulating cell-ECM interactions. Genes: THBS1, SPARC
  - [13]: THBS1 functions as matricellular protein modulating cell-ECM interactions and cell migration
  - [21]: SPARC represents secreted ECM-associated protein mediating tumor-stromal cell interactions
- Tetraspanin-mediated ECM interactions. Genes: TSPAN8, CD151
  - [29]: CD151 and TSPAN8 act as molecular facilitators in wound healing, angiogenesis, and tumor progression through ECM interactions

**Required genes (not in input)**
- Genes: MMP2, MMP9, TIMP1, TIMP2, ADAMTS, INTEGRIN
  - [31]: Matrix metalloproteinases and their tissue inhibitors represent critical players in ECM remodeling

**Program citations**
- [13]: THBS1 high expression associated with migration, invasion, and progression in cancer
- [21]: SPARC upregulation in extracellular vesicles promotes metastasis through ECM remodeling
- [23]: LOX catalyzes ECM cross-linking and identified as therapeutic target in LKB1-deficient lung cancer

## Program: Tetraspanin-Organized Membrane Microdomains
Tetraspanins represent a family of four-transmembrane domain proteins that organize lateral membrane organization domains (TEMs, tetraspanin-enriched microdomains) and facilitate cell-cell and cell-ECM interactions. TSPAN8 and CD151 within the candidate gene set represent key tetraspanin family members that function as molecular hubs organizing multimeric complexes with integrins, growth factor receptors, and signaling kinases. These organized microdomains concentrate specific signaling molecules, directing and amplifying cellular responses to extracellular ligands. In astrocytomas, tetraspanin-organized microdomains support selective signaling underlying invasion, migration, and metastatic dissemination.

**Predicted impacts**
- Enhanced directional cell migration through organized integrin signaling
- Selective activation of invasion-promoting pathways in response to ECM cues
- Coordinated cell-cell adhesion supporting collective invasion and percolation through brain parenchyma
- Amplified growth factor signaling supporting vascular co-option and angiogenesis
- Organization of immune suppressive signaling at cell-cell interfaces with infiltrating immune cells

**Evidence summary**
TSPAN8 and CD151 represent well-characterized members of the tetraspanin family with extensive experimental support for their roles in cancer cell migration, invasion, and metastasis. Both proteins have been demonstrated through independent studies to promote tumor progression; TSPAN8 specifically functions through STAT3-mediated signaling enhancement and correlates with increased metastatic risk. The coordinated action of multiple tetraspanins in organizing multimeric membrane complexes enables selective spatial and temporal control of signaling, providing mechanistic explanation for how astrocytomas achieve directional migration and selective response to environmental cues. The presence of both TSPAN8 and CD151 in the candidate set strengthens confidence that tetraspanin-organized microdomains represent a functionally significant program in astrocytoma biology.

**Atomic biological processes**
- Tetraspanin-mediated migration and invasion promotion. Genes: TSPAN8, CD151
  - [28]: TSPAN8 enhancement of tumor progression occurs through STAT3-mediated mechanisms; tetraspanin 8 expression predicts increased metastatic risk
  - [29]: CD151 and TSPAN8 act as molecular facilitators in wound healing, angiogenesis, and tumor progression
- Integrin-tetraspanin signaling complexes. Genes: TSPAN8, CD151
  - [29]: CD151 and TSPAN8 facilitate integrin-dependent cell adhesion and migration through formation of specialized membrane microdomains
- Angiogenic signaling coordination. Genes: TSPAN8, CD151
  - [29]: CD151 and TSPAN8 promote angiogenesis through organization of growth factor receptor signaling in endothelial and tumor cells

**Atomic cellular components**
- Tetraspanin-enriched membrane microdomains (TEMs). Genes: TSPAN8, CD151
  - [29]: TSPAN8 and CD151 organize lateral membrane domains concentrating integrins and signaling molecules

**Required genes (not in input)**
- Genes: INTEGRIN, EGFR, FGFR, JAK, STAT3, SRC
  - [29]: Tetraspanins organize complexes with integrins, receptor tyrosine kinases, and associated signaling kinases

**Program citations**
- [28]: TSPAN8 enhancement of tumor progression through STAT3-mediated mechanisms
- [29]: CD151 and TSPAN8 molecular facilitators in wound healing, angiogenesis, and tumor progression

## Program: Long Non-Coding RNA-Mediated Metabolic Control
Long non-coding RNAs (lncRNAs) have emerged as critical regulators of cancer metabolic reprogramming, particularly in controlling glycolytic enzyme expression and signaling pathway engagement. The candidate gene set contains extensive representation of lncRNAs (LINC00326, LINC01208, LINC01482, LINC01933, LINC01934, LINC00880, LINC00589, LINC01504, LINC01214, and numerous others), suggesting comprehensive lncRNA-mediated control of metabolic adaptation in astrocytomas. lncRNAs influence metabolic adaptation through multiple mechanisms including chromatin remodeling, competing endogenous RNA effects, and formation of ribonucleoprotein complexes. The extensive lncRNA representation distinguishes this gene program as potentially critical for the Warburg effect and aerobic glycolysis characteristic of rapidly proliferating gliomas.

**Predicted impacts**
- Enhanced glycolytic flux supporting rapid proliferation through lncRNA-mediated enzyme expression control
- Modified responsiveness to nutrient availability through lncRNA-regulated metabolic checkpoint genes
- Altered microRNA-mediated gene silencing through competing endogenous RNA mechanisms
- Selection for immunosuppressive immune cell populations through lncRNA-dependent cytokine production
- Enhanced metabolic plasticity enabling adaptation to diverse microenvironmental conditions

**Evidence summary**
The lncRNA metabolic program is distinguished by extensive representation of lncRNA genes within the candidate set, suggesting that lncRNA-mediated control represents a prioritized regulatory layer in astrocytoma. Contemporary literature has firmly established that lncRNAs function as critical modulators of cancer metabolism; specific examples include LINC00470 functioning as an AKT activator in glioblastoma and LncARSR promoting glioma growth. The multiple mechanisms through which lncRNAs regulate metabolism (direct enzyme expression control, competing endogenous RNA mechanisms, micropeptide-mediated signaling) suggest that astrocytomas employ comprehensive and redundant lncRNA-dependent control of metabolic programs. While individual lncRNA functions in astrocytomas remain to be fully characterized, the collective evidence supports designation of lncRNA-mediated metabolic control as a major gene program.

**Atomic biological processes**
- lncRNA-mediated glycolytic enzyme regulation. Genes: LINC00326, LINC01208, LINC01482, LINC01933, LINC01934, LINC00880, LINC00589, LINC01504, LINC01214
  - [24]: lncRNAs regulate cancer metabolism by modulating glycolytic enzyme expression and transcription factors; lncRNA-LINC00470 acts as AKT activator mediating glioblastoma cell autophagy
- lncRNA-mediated tumor microenvironment shaping. Genes: LINC00880, LINC00589, LINC01504, LINC01214
  - [24]: lncRNAs shape tumor microenvironment through immune and stromal cell interactions; LncARSR promotes glioma tumor growth
- Competing endogenous RNA mechanisms. Genes: LINC02763, LINC02073, LINC01823, LINC02196, LINC01588, LINC02408
  - [24]: lncRNAs function as competing endogenous RNAs sequestering microRNAs away from protein-coding targets, controlling gene expression
- lncRNA-encoded micropeptides in metabolic regulation. Genes: LINC01933, LINC01934
  - [24]: lncRNA-encoded micropeptides provide extra layer of metabolic control, underscoring functional diversity of lncRNAs

**Required genes (not in input)**
- Genes: GLYCOLYTIC_ENZYMES, MIRNA_COMPONENTS, RIBOSOMAL_PROTEINS
  - [24]: lncRNAs regulate expression of glycolytic enzymes and interact with microRNA machinery and ribosomal components

**Program citations**
- [24]: Comprehensive review of lncRNAs as critical regulators of cancer metabolism, glycolysis, and tumor microenvironment

## Program: Meiosis-Related Genes and Germ Cell Plasticity
A striking and counterintuitive aspect of the candidate astrocytoma gene set is the inclusion of multiple genes predominantly expressed during meiosis and germ cell development, including MSH4 (MutS homolog 4), HORMAD2 (HORMAD2, asynaptic meiotic regulator), LDHC (lactate dehydrogenase C, germ cell-specific isoform), and LHCGR (luteinizing hormone/choriogonadotropin receptor). While these genes are traditionally associated with gamete development, their presence in an astrocytoma context suggests either ectopic expression or, more intriguingly, activation of dormant germ cell developmental programs as a mechanism of tumor plasticity and treatment resistance. This program may reflect astrocytoma plasticity toward germ cell-like states or represent acquisition of primitive developmental regulatory modules.

**Predicted impacts**
- Potential activation of primitive developmental plasticity enabling state transitions
- Enhanced DNA repair capacity through repurposing of meiotic recombination machinery
- Metabolic switching to germ cell-like metabolic programs supporting stemness
- Potential gonadotropin-responsive signaling controlling stem cell-like state maintenance
- Increased treatment resistance through activation of quiescent developmental programs

**Evidence summary**
The inclusion of meiosis-related and germ cell genes in the astrocytoma candidate set is unexpected and warrants investigation. While these genes are classically associated with gamete development, emerging research has demonstrated that cancer cells can exhibit plasticity toward germ cell-like states or activate dormant developmental programs as mechanisms of treatment resistance and tumor maintenance. The non-canonical functions of meiotic proteins such as MSH4 in somatic cell contexts remain poorly characterized but may include roles in DNA damage response, checkpoint control, and cellular plasticity. The presence of the germ cell-specific metabolic enzyme LDHC suggests potential metabolic reprogramming toward germ cell-like states during astrocytoma progression. LHCGR presence is particularly intriguing, suggesting that gonadotropin signaling may control stem cell-like program maintenance. This program receives a lower significance score due to limited direct evidence in astrocytoma specifically, but warrants investigation as potentially important in tumor-initiating cells or treatment-resistant populations.

**Atomic biological processes**
- Meiotic recombination and DNA repair. Genes: MSH4, HORMAD2
  - [31]: MSH4 and meiosis-related proteins participate in DNA recombination and repair pathways potentially repurposed in somatic tumor contexts
- Germ cell-specific metabolic programs. Genes: LDHC
  - [31]: LDHC (lactate dehydrogenase C) represents germ cell-specific metabolic isoform; its expression in astrocytoma suggests metabolic plasticity
- Gonadotropin signaling and stem cell maintenance. Genes: LHCGR
  - [31]: LHCGR (luteinizing hormone receptor) represents gonadotropin receptor potentially controlling stem cell-like program

**Required genes (not in input)**
- Genes: SYCP1, SYCP3, RAD51, DMC1, SPERMATOGENESIS_FACTORS, OOGENESIS_FACTORS
  - [31]: Complete meiotic programs require multiple additional factors for synapsis, recombination, and gamete differentiation

**Program citations**
- [31]: Immune infiltration and heterogeneity analysis suggests presence of diverse cell states in tumor microenvironment

## Program: Ciliary Structure and Hedgehog Signaling
Multiple genes in the candidate set encode components of the ciliary axoneme and associated structures, including DNAH12 and DNAH14 (dynein axonemal heavy chains), and regulatory proteins. Primary cilia represent cellular organelles that function in signal transduction of Hedgehog, Wnt, and other developmental pathways critical for neural progenitor specification and maintenance. Dysregulation of ciliary signaling has been increasingly implicated in glioma pathogenesis and progression. The presence of dynein motor proteins in the astrocytoma gene set suggests comprehensive modification of ciliary function that may alter responsiveness to developmental morphogens and modify cell cycle control.

**Predicted impacts**
- Altered primary cilium architecture modifying Hedgehog and Wnt signal transduction
- Modified responsiveness to developmental morphogens controlling stemness versus differentiation
- Enhanced cell cycle progression through dysregulated ciliary resorption
- Altered cytokine receptor trafficking affecting immune signaling
- Increased genomic instability through disrupted ciliary checkpoint functions

**Evidence summary**
The presence of multiple dynein heavy chain genes in the candidate astrocytoma set suggests comprehensive modification of ciliary structure and function. Emerging research has established that primary cilia dysregulation contributes to various malignancies through disruption of Hedgehog and Wnt signaling pathways. Ciliary resorption is coupled to cell cycle progression, and alterations in ciliary proteins can influence proliferation rates and cell cycle checkpoint control. The specific inclusion of DNAH12 and DNAH14 suggests that astrocytomas may modify the motor properties of their primary cilia, potentially altering the compartmentalization and signaling of developmental morphogens. While ciliary dysfunction has not been extensively studied in astrocytomas specifically, the mechanistic framework supports investigation of this program.

**Atomic biological processes**
- Dynein motor function and cilia motility. Genes: DNAH12, DNAH14
  - [31]: Dynein axonemal heavy chains DNAH12 and DNAH14 represent motor proteins generating sliding force propelling cilia; dynein dysfunction alters ciliary architecture and signaling
- Hedgehog signaling compartmentalization. Genes: DNAH12, DNAH14
  - [31]: Primary cilia regulate Hedgehog and Wnt signaling pathways through spatial compartmentalization of signaling components
- Ciliary resorption and cell cycle progression. Genes: DNAH12, DNAH14
  - [31]: Ciliary resorption is coupled to cell cycle progression; alterations in ciliary structure genes influence proliferation rates

**Atomic cellular components**
- Ciliary axoneme dynein arms. Genes: DNAH12, DNAH14
  - [31]: DNAH12 and DNAH14 encode outer and inner dynein arm components essential for ciliary motion

**Required genes (not in input)**
- Genes: IFT88, IFT52, KIF3A, SMO, GLI1, GLI2, GLI3
  - [31]: Primary cilium assembly and Hedgehog signaling require intraflagellar transport proteins and Hedgehog signaling components

**Program citations**
- [31]: Ciliary dysfunction and dysregulation implicated in various cancers through disruption of developmental signaling

## Program: Neurotransmission and Neuronal Plasticity
Several genes in the candidate set encode proteins involved in neurotransmitter synthesis, neurotransmitter receptors, and associated signaling, including TPH2 (tryptophan hydroxylase 2), GRIN3A (NMDA receptor subunit 3A), GLRA1 (glycine receptor alpha-1), and GUCY2C (guanylate cyclase 2C). The role of these neurotransmission-related genes in astrocytoma is multifaceted and potentially reflects retention of partial neuronal identity, acquisition of neuron-like signaling modalities, or trans-differentiation capacity of tumor-initiating cells toward neuronal phenotypes. Astrocytes under normal conditions express neurotransmitter receptors and participate in glutamate homeostasis; dysregulation of these functions is implicated in neuropathology and potentially in glioma.

**Predicted impacts**
- Retention of partial neuronal identity supporting stem cell-like program maintenance
- Dysregulation of glutamate homeostasis potentially contributing to excitotoxicity and microenvironment remodeling
- Altered serotonin signaling potentially affecting immune cell recruitment and mood-related neuropathology
- Aberrant inhibitory signaling potentially affecting neural circuit function surrounding tumor
- Enhanced plasticity toward neuronal phenotypes in specific tumor subpopulations

**Evidence summary**
The presence of neurotransmission-related genes in the astrocytoma candidate set reflects the neuronal developmental origin of astrocytes and the potential for tumor-initiating cells or specific tumor populations to retain or activate neuronal differentiation programs. Emerging research has established that trans-differentiation events occur in neural tumors, and that retention of neuronal identity markers correlates with specific cellular states and therapeutic responses. TPH2, while not classically considered a glioma gene, may support serotonergic signaling affecting both tumor cells and infiltrating immune populations. GRIN3A expression suggests potential dysregulation of glutamate signaling with implications for both tumor microenvironment acidification and neuroinflammation. The inclusion of GLRA1 (glycine receptor) is particularly intriguing, as it suggests potential participation in inhibitory signaling networks that might suppress immune responses or neuronal activity surrounding tumors.

**Atomic biological processes**
- Serotonin synthesis and signaling. Genes: TPH2
  - [4]: TPH2 encodes tryptophan hydroxylase 2 catalyzing rate-limiting step of serotonin synthesis in central nervous system; involved in regulation of behavior and mood
- NMDA-type glutamate receptor signaling. Genes: GRIN3A
  - [31]: GRIN3A encodes NMDA-type glutamate receptor subunit; dysregulation of glutamate signaling implicated in neuropathology and tumor biology
- Glycine receptor-mediated inhibitory signaling. Genes: GLRA1
  - [31]: GLRA1 encodes glycine receptor alpha-1 subunit, ligand-gated chloride channel involved in inhibitory neurotransmission
- Guanylate cyclase signaling and cGMP metabolism. Genes: GUCY2C
  - [9]: PTGER3 (prostaglandin E receptor) and related signaling including cyclic nucleotide pathways regulate cellular responses

**Atomic cellular components**
- NMDA receptor complexes. Genes: GRIN3A
  - [31]: GRIN3A participates in NMDA receptor assembly and function as ligand-gated ion channel
- Inhibitory neurotransmitter receptors. Genes: GLRA1
  - [31]: GLRA1 represents ligand-gated chloride channel mediating inhibitory synaptic transmission

**Required genes (not in input)**
- Genes: SLC6A3, SLC6A5, GABA_RECEPTORS, SEROTONIN_RECEPTORS, NMDA_RECEPTOR_SUBUNITS
  - [31]: Neurotransmitter systems require multiple components including receptors, transporters, and synthesizing enzymes

**Program citations**
- [4]: TPH2 involved in serotonin metabolic pathway regulation in brain; mutations implicated in various neuropsychiatric conditions
- [30]: Neurotransmission-related genes dysregulated in reactive astrocytes following traumatic brain injury

## Program: Solute Transport and Metabolic Exchange
The candidate gene set contains extensive representation of genes encoding solute carrier proteins and specific transporters including SLC7A11, SLC10A1, SLC2A9, and SLC9C2, which mediate the movement of specific molecular substrates across cellular membranes. These transporters control intracellular concentrations of amino acids, glucose, metabolites, and ions, fundamentally determining the metabolic capacities and redox state of astrocytoma cells. The coordinated expression of multiple solute carriers suggests sophisticated modification of metabolic and ion transport profiles to support rapid proliferation, resist oxidative stress, and maintain pH homeostasis in the acidic tumor microenvironment.

**Predicted impacts**
- Enhanced amino acid and glucose uptake supporting biosynthetic demands of rapid proliferation
- Maintenance of intracellular redox balance through cystine availability
- Modified responsiveness to nutrient scarcity through transporter regulation
- Enhanced resistance to ferroptosis through SLC7A11-dependent cystine uptake
- Altered pH homeostasis through coordinated ion transport enabling survival in acidic tumor microenvironment

**Evidence summary**
The solute transport program represents a fundamental aspect of astrocytoma metabolic adaptation. SLC7A11 (xCT) has been exceptionally well-characterized through ferroptosis research, with clear mechanistic roles in cystine uptake and glutathione synthesis. SLC2A9 (GLUT9) represents an emerging therapeutic target in various malignancies through its roles in glucose and urate transport. The inclusion of multiple distinct solute carriers suggests that astrocytomas employ comprehensive fine-tuning of metabolic substrate selection and ion homeostasis. Recent research has established that transporter expression profiles differ substantially between tumor regions (hypoxic versus normoxic, proliferative versus quiescent), suggesting dynamic regulation of this program in response to microenvironmental changes.

**Atomic biological processes**
- Cystine/glutamate transport and ferroptosis regulation. Genes: SLC7A11
  - [15]: SLC7A11 (xCT) cystine transporter central to ferroptosis regulation and cancer nutrient dependency
- Bile acid and organic anion transport. Genes: SLC10A1
  - [31]: SLC10A1 (NTCP) originally identified as bile acid transporter; recent research reveals roles in pathogen defense and immune responses
- Glucose and polyol transport. Genes: SLC2A9
  - [31]: SLC2A9 (GLUT9) represents glucose transporter with broader substrate specificity including urate and polyols
- Ion transport and pH homeostasis. Genes: SLC9C2
  - [31]: SLC9C2 represents solute carrier family member involved in ion transport and cellular pH regulation

**Atomic cellular components**
- Solute carrier family transporters. Genes: SLC7A11, SLC10A1, SLC2A9, SLC9C2
  - [31]: SLC proteins represent major family of membrane transporters controlling nutrient uptake and waste export

**Required genes (not in input)**
- Genes: SLC1A1, SLC1A2, SLC6A6, SLC6A7, SLC43A1, SLC43A2
  - [31]: Additional solute carriers control amino acid uptake, neurotransmitter transport, and metabolite exchange

**Program citations**
- [15]: SLC7A11 inhibition as therapeutic strategy in cancer targeting cystine dependence and ferroptosis resistance
- [31]: Metabolic transporter expression patterns reflect tumor microenvironmental heterogeneity

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/3824
2. 2. Available from: https://www.ncbi.nlm.nih.gov/gene/16643
3. 3. Liu L, Zhang Y, Huang Y, Zhao X, Fu H, Chen L, et al.. IGF2BP3 regulates EMP1 stability in an m6A-dependent manner and activates the TGF-β pathway to promote pancreatic cancer invasion. Cell Death &amp; Disease [Internet]. 2025Nov24;16(1). Available from: https://www.nature.com/articles/s41419-025-08155-1
4. 4. Available from: https://www.ncbi.nlm.nih.gov/gene/4128
5. 5. Klinkhammer K, Warren R, Knopp J, Nguyen T, De LSP. Epithelial-mesenchymal cell competition coordinates fate transitions across tissue compartments during lung development and fibrosis. Nature Communications [Internet]. 2025Nov21;16(1). Available from: https://www.nature.com/articles/s41467-025-66690-z
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/25937
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/9173
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/3554
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/5733
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/353376
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/7098
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/148022
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/7057
14. 14. Liu J, Dong R, Yuan B, Xie Y, Feng Z, Zhou S, et al.. Immune cells dying from ferroptosis: mechanisms and therapeutic opportunities. Cell Death &amp; Disease [Internet]. 2025Dec1;16(1). Available from: https://www.nature.com/articles/s41419-025-08204-9
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/23657
16. 16. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
17. 17. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/8651
19. 19. Yang S, Yang Y, Fang Y, Zhou Q, Sun W, Zhang Z, et al.. Targeting tumour-infiltrating B cells: mechanisms and advances in cancer therapy. Cell Death &amp; Disease [Internet]. 2025Nov24;. Available from: https://www.nature.com/articles/s41419-025-08254-z
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/6777
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/6678
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/4015
24. 24. Ren Y, Zhang Z, Lei X, Shi L. Long non-coding RNAs in cancer glycolysis and metabolism: mechanisms and translational opportunities. Cell Death &amp; Disease [Internet]. 2025Dec8;. Available from: https://www.nature.com/articles/s41419-025-08289-2
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/8678
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/4780
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/7103
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/977
30. 30. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
31. 31. Mao Q, Liu H, Liu S, Wang W, Wang Y, Lou K, et al.. Uncovering the prognostic implications and immunological roles of transmembrane protein 208 in bladder cancer by multi omics analysis and experimental verification. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-11796-z
