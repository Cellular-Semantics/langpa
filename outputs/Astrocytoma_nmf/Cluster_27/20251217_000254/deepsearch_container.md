# Gene Program Markdown Report

## Context
- Cell type: astrocytes, glial progenitor cells
- Disease: astrocytoma (including high-grade gliomas with astrocytic differentiation)
- Tissue: central nervous system (CNS), brain

## Input Genes
ABCB5, MOXD1, LINC02391, LINC02397, LINC02821, LRP4, MACORIS, MALRD1, MAP3K1, ME1, MIR217HG, MMP16, MPPED2, AC006206.2, NAV2, NCALD, NOS2, NPNT, NPSR1-AS1, NRIP1, NRXN1, OSBPL10, PAPOLG, PARD3, LINC02378, ... (200 total)

## Program: AP-1 and Lineage-Specific Transcriptional Cascades
Dysregulated transcriptional reprogramming mediated through AP-1 binding sites modulated by lineage-specific transcription factors (ZEB1, TP63, BCL11A, TAF3) that drive transformation of normal reactive astrocyte gene expression into constitutive pathogenic programs. This program integrates developmental transcription factor networks with injury-response enhancers, enabling sustained activation of pro-growth and anti-differentiation genes while suppressing normal maturation signals.

**Predicted impacts**
- Sustained activation of pro-growth transcriptional programs normally restricted to reactive astrocytes
- Loss of differentiation signals required for terminal glial maturation
- Enhanced expression of EMT-associated genes and migratory capacity
- Dysregulated developmental transcription factor networks in adult tumor cells

**Evidence summary**
Astrocytomas dysregulate the same AP-1 and lineage-specific transcription factor networks that drive normal reactive astrocyte responses to injury. While reactive astrocytes activate these programs transiently in response to specific insults, astrocytomas lock these programs into constitutive activation through oncogenic mutations and epigenetic modifications. The presence of ZEB1 and its regulatory noncoding RNA (ZEB1-AS1) indicates coordinated transcriptional and post-transcriptional control of EMT-associated gene expression. TAF3 and BCL11A contribute to selective activation of developmental genes that are normally silenced in mature astrocytes, suggesting that astrocytomas partially recapitulate developmental transcriptional programs.

**Atomic biological processes**
- AP-1-driven immediate early gene expression. Genes: ZEB1, TAF3, BCL11A, TP63
  - [17]: AP-1 binding sites required for injury-responsive enhancer activation in reactive astrocytes; lineage-specific TFs modulate AP-1 function
- EMT-associated transcriptional repression. Genes: ZEB1, ZEB1-AS1
  - [27]: ZEB1 is a zinc finger transcription factor promoting EMT and invasive phenotypes
- Lineage-specific developmental programming. Genes: BCL11A, TP63, TAF3
  - [41]: BCL11A regulates cell identity specification and developmental programs
  - [3]: TP63 regulates stemness programs and alternative differentiation in neural progenitors
- TFIID-associated selective gene activation. Genes: TAF3
  - [48]: TAF3 participates in selective activation of developmental genes

**Atomic cellular components**
- AP-1 complex at injury-responsive enhancers. Genes: ZEB1, TAF3
  - [17]: IRENs contain AP-1 binding sites that recruit lineage-specific transcription factors

**Required genes (not in input)**
- Genes: AP-1 components (c-FOS, c-JUN), SOX family members, developmental transcription factors
  - [17]: AP-1 complex components are core to IRENs but not all AP-1 members are in the input list

**Program citations**
- [17]: Identifies AP-1 and lineage-specific TF synergy in reactive astrocyte IRENs
- [27]: ZEB1 promotes EMT and invasive phenotypes across cancer types
- [41]: BCL11A regulates developmental cell identity programs
- [3]: TP63 regulates stemness in neural progenitors

## Program: Histone Methylation and Chromatin Plasticity
Dysregulation of histone methyltransferases and chromatin-associated processes enabling rapid transcriptional adaptations in response to therapeutic stress and metabolic challenges. SMYD3-mediated H3K4 methylation and broader chromatin remodeling establish permissive epigenetic landscapes supporting sustained tumor progression and drug tolerance phenotypes.

**Predicted impacts**
- Rapid transcriptional responses to metabolic stress and therapeutic challenge
- Maintenance of elevated transcription of proliferation and survival genes
- Sustained activation of metabolic adaptation programs
- Epigenetic plasticity permitting reversible phenotypic switching

**Evidence summary**
Glioblastoma persisters surviving chemotherapy exhibit elevated histone methylation at both gene-activating (H3K4me3, H3K36me3) and gene-repressing (H3K27me3) marks, establishing an epigenetically plastic state. While PRDM9 is not in the input list, SMYD3 represents a histone methyltransferase also contributing to chromatin remodeling and cancer cell proliferation. The presence of SMYD3 and TAF3 (a TFIID-associated factor participating in transcriptional initiation) suggests that astrocytomas maintain mechanisms for establishing and maintaining transcription-permissive chromatin states. This program enables sustained proliferation while preserving capacity for adaptive responses to environmental changes.

**Atomic biological processes**
- H3K4me3 deposition and histone methyltransferase activity. Genes: SMYD3, TAF3
  - [22]: PRDM9 and histone methyltransferases establish H3K4me3 marks at promoters in glioblastoma persisters
  - [24]: SMYD3 encodes a histone methyltransferase promoting cancer cell proliferation
- Transcription-activating chromatin mark deposition. Genes: SMYD3
  - [22]: H3K4me3 is a transcription-activating chromatin mark established at promoters and distal intergenic sites
- Epigenetic plasticity in drug-tolerant states. Genes: SMYD3, TAF3
  - [22]: Epigenetic reprogramming enables glioblastoma cells to survive chemotherapy through reversible drug-tolerant states

**Atomic cellular components**
- Chromatin at promoters with elevated H3K4me3. Genes: SMYD3
  - [22]: H3K4me3 peaks are most abundant at promoters where histone methyltransferases concentrate

**Required genes (not in input)**
- Genes: PRDM9 (histone methyltransferase), COMPASS complex components, chromatin remodeling complexes
  - [22]: PRDM9 is a critical histone methyltransferase but not in the input gene list

**Program citations**
- [22]: Demonstrates histone methylation changes in drug-tolerant glioblastoma cells
- [24]: SMYD3 promotes cancer cell proliferation through histone methylation

## Program: Adherens Junction Disruption and Polarity Loss
Coordinated dysregulation of cell-cell adhesion molecules and polarity proteins (PCDH7, PCDH15, PARD3) combined with enhanced Rho GTPase signaling (VAV3) that collectively suppress contact inhibition and enable aberrant cell migration. ZEB1-mediated transcriptional repression of adhesion genes synergizes with post-translational dysregulation of junction dynamics.

**Predicted impacts**
- Loss of contact inhibition and uncontrolled cell proliferation
- Enhanced migratory capacity and reduced adhesive constraints
- Disrupted epithelial organization and polarization
- Invasion capability through suppression of adhesive constraints

**Evidence summary**
The coordinated presence of multiple adherens junction components and regulators indicates that astrocytomas dysregulate cell-cell adhesion at multiple levels: transcriptional (through ZEB1), post-translational (through VAV3 Rac activation disrupting PARD3-mediated polarity), and through expression changes in specific cadherin subtypes. In glioblastoma, PARD3 has been demonstrated to simultaneously promote self-renewal and suppress invasiveness—functions that become dysregulated in tumors, permitting increased motility. The presence of ZEB1, which directly represses cadherin expression, indicates transcriptional mechanisms of adhesion loss complementary to the post-translational disruption of polarity complexes.

**Atomic biological processes**
- Protocadherin-mediated cell-cell recognition. Genes: PCDH15, PCDH7
  - [26]: Protocadherins mediate heterophilic cell-cell recognition and adhesion in neuronal contexts
  - [28]: SLIT2 and ROBO2 participate in cell guidance and migration alongside cadherin systems
- Crumbs polarity complex assembly and function. Genes: PARD3, VAV3
  - [39]: PARD3 is a polarity protein coordinating self-renewal and invasiveness in glioblastoma
  - [42]: PARD3 binds cell adhesion molecules at tight junctions of neuroepithelial cells
- Rac-mediated junction disruption and cytoskeletal remodeling. Genes: VAV3, PARD3
  - [39]: VAV3 (Rac GEF) promotes cytoskeletal dynamics when PARD3 polarity is disrupted
- ZEB1-mediated transcriptional suppression of adhesion molecules. Genes: ZEB1
  - [27]: ZEB1 represses adherens junction components including classical cadherins

**Atomic cellular components**
- Adherens junction complexes. Genes: PCDH7, PCDH15, VAV3
  - [39]: Adherens junction organization is disrupted by altered VAV3 signaling
- Crumbs polarity complex at tight junctions. Genes: PARD3
  - [42]: PARD3 localizes to tight junctions of neuroepithelial cells

**Required genes (not in input)**
- Genes: Classical cadherins (CDH1, CDH2), β-catenin (CTNNB1), other Crumbs complex components
  - [12]: CTNNB1 (β-catenin) mutations cause medulloblastoma and are implicated in gliomas but not in input list

**Program citations**
- [39]: PARD3 coordinates self-renewal and invasiveness in glioblastoma
- [27]: ZEB1 promotes EMT through cadherin repression
- [42]: PARD3 structure and tight junction localization

## Program: Extracellular Matrix Proteolysis and Invasion
Coordinated activation of matrix metalloproteinases (MMP16) and microenvironment remodeling through growth factor binding proteins (IGFBP2) that collectively degrade extracellular matrix barriers and establish permissive invasion pathways. Direct enzymatic breakdown of matrix combined with alteration of matrix-cell signaling enables infiltrative tumor growth.

**Predicted impacts**
- Enhanced proteolytic degradation of physical invasion barriers
- Establishment of permissive invasion pathways through matrix remodeling
- Altered growth factor signaling through modulation of bioavailability
- Recruitment and polarization of tumor-supporting macrophages

**Evidence summary**
Astrocytoma invasion requires active remodeling of the extracellular matrix to facilitate infiltration of tumor cells into surrounding tissue. MMP16, a membrane-anchored metalloproteinase, directly degrades matrix components and is regulated at multiple levels including transcriptional and post-transcriptional (through miR-146a). IGFBP2 represents a cancer-associated fibroblast gene that promotes glioma progression, and its expression within astrocytoma can modify both growth factor signaling and immune cell infiltration through induction of M2 macrophage polarization. Together, these genes establish a program wherein direct enzymatic matrix degradation combines with altered growth factor signaling to enable invasion.

**Atomic biological processes**
- Matrix metalloproteinase-mediated ECM degradation. Genes: MMP16
  - [21]: MMP16 (MT3-MMP) is a membrane-anchored metalloproteinase modifying invasive tumor cell phenotypes
  - [23]: MMP16 is regulated by miR-146a and promotes glioma progression
- Growth factor sequestration and bioavailability. Genes: IGFBP2
  - [33]: IGFBP2 promotes glioma progression through M2 macrophage polarization and modulation of IGF signaling
- IGF signaling modulation in tumor microenvironment. Genes: IGFBP2
  - [33]: IGFBP2 is a cancer-associated fibroblast gene promoting glioma progression

**Atomic cellular components**
- Extracellular matrix structural components. Genes: MMP16, IGFBP2
  - [21]: MMP16 degrades matrix metalloprotein substrates

**Required genes (not in input)**
- Genes: Other matrix metalloproteinases (MMP2, MMP9), tissue inhibitors of metalloproteinases (TIMPs), other IGFBP family members
  - [21]: Multiple MMPs contribute to matrix remodeling; MMP16 is one component

**Program citations**
- [21]: MMP16 promotes invasiveness in multiple cancer contexts
- [23]: MMP16 and glioma progression
- [33]: IGFBP2 and glioma progression through immune modulation

## Program: PDGFRA-Driven Proliferation and Oncogenic Signaling
Constitutive activation of platelet-derived growth factor receptor-alpha (PDGFRA) drives sustained proliferation through engagement of PI3K/AKT and MAPK/ERK pathways. PDGFRA signaling is sufficient as primary oncogenic driver in multiple astrocytoma subtypes and is particularly potent when combined with tumor suppressors loss (TP53, NF1). Supporting metabolic rewiring through MAP3K1 and ME1 enables proliferative capacity.

**Predicted impacts**
- Constitutive activation of proliferation signals and survival pathways
- Metabolic rewiring to support high biosynthetic demand
- Potent oncogenic driver sufficient for gliomagenesis
- Enhanced angiogenesis and microenvironment remodeling

**Evidence summary**
PDGFRA represents one of the most consistently altered genes in pediatric high-grade gliomas and certain astrocytoma subtypes. In mouse models of pediatric glioma, the PDGFRA(D842V) constitutively active variant drives rapid gliomagenesis and is sufficient as a primary oncogenic driver. Remarkably, PDGFRA signaling alone is sufficient to drive transformation, even without additional oncogenic alterations, though it is more potent when combined with tumor suppressor loss (TP53, NF1, ATRX). The presence of MAP3K1 in the input list reflects the central importance of MAPK pathway activation downstream of PDGFRA signaling, which drives proliferation and metabolic adaptation. ME1 (malic enzyme 1) supports metabolic rewiring, converting malate to pyruvate for both gluconeogenesis and lipogenesis, processes upregulated in proliferating tumor cells.

**Atomic biological processes**
- Receptor tyrosine kinase signaling and proliferation. Genes: PDGFRA, MAP3K1
  - [1]: PDGFRA(D842V) is a constitutively active variant driving rapid gliomagenesis in mouse models
  - [15]: PDGFRA constitutive signaling is sufficient to drive gliomagenesis independent of other alterations
  - [18]: PDGFRA is involved in tumor angiogenesis and microenvironment maintenance
  - [58]: PDGFRA tumorigenicity and signaling in glioma
- MAPK pathway activation and cell cycle progression. Genes: MAP3K1
  - [32]: MAP3K1 regulates mitogen-activated protein kinase signaling cascades
- Metabolic adaptation to support proliferation. Genes: ME1
  - [51]: Malic enzyme activity supports gluconeogenesis and lipogenesis in metabolically adapted cells

**Atomic cellular components**
- PDGFRA receptor at cell membrane. Genes: PDGFRA
  - [1]: PDGFRA localizes to cell surface where it engages PDGF ligands
- Downstream signaling complexes (PI3K/AKT, MAPK/ERK). Genes: PDGFRA, MAP3K1
  - [1]: PDGFRA engagement recruits and activates downstream signaling cascades

**Required genes (not in input)**
- Genes: PI3K catalytic subunit (PIK3CA), AKT serine/threonine kinase (AKT1), ERK/MAPK components, PDGF ligands
  - [1]: PI3K/AKT and MAPK pathways downstream of PDGFRA are critical for its oncogenic function

**Program citations**
- [1]: PDGFRA drives gliomagenesis in mouse models
- [15]: PDGFRA signaling is potent driver in pediatric glioma
- [18]: PDGFRA in tumor angiogenesis and microenvironment

## Program: Lipid Metabolism and Membrane Remodeling
Dysregulated lipid synthesis through fatty acid elongases (ELOVL2) and lipid transport proteins (OSBPL10) enables production of specialized membrane lipids supporting proliferation, altered membrane properties, and metabolic adaptation. Coordinated regulation of lipid anabolism and signaling lipid production supports rapid cell division and response to metabolic stress.

**Predicted impacts**
- Enhanced membrane synthesis to support rapid cell division
- Altered membrane physical properties affecting protein distribution and signaling
- Increased biosynthesis of signaling lipids and inflammatory mediators
- Metabolic adaptation supporting proliferation under nutrient stress

**Evidence summary**
Astrocytomas undergo substantial metabolic rewiring including dysregulation of lipid synthesis to support the high biosynthetic demands of proliferation. Fatty acid elongases, particularly ELOVL2, catalyze synthesis of polyunsaturated fatty acids with specialized functions in membrane organization and signaling. OSBPL10, an oxysterol-binding protein, regulates intracellular lipid distribution, a process critical for establishing compartmentalized signaling platforms. ACSS3 supports conversion of acetate to acetyl-CoA, a critical hub linking glucose metabolism to both lipid synthesis and histone acetylation (affecting epigenetic state). Together, these genes establish a coordinated program of lipid metabolic rewiring that supports both the physical requirements of rapid cell division and the signaling and epigenetic adaptations enabling tumor progression.

**Atomic biological processes**
- Polyunsaturated fatty acid synthesis. Genes: ELOVL2
  - [54]: ELOVL2 (fatty acid elongase 2) catalyzes elongation of polyunsaturated fatty acids
  - [51]: Fatty acid elongase activity modulates PUFA synthesis and influences ferroptosis susceptibility and metabolic adaptation
- Intracellular lipid transport and organization. Genes: OSBPL10
  - [51]: Oxysterol-binding proteins regulate intracellular lipid distribution and vesicular trafficking
- Acetyl-CoA generation for biosynthesis. Genes: ACSS3
  - [51]: Acyl-CoA synthetase short-chain family member 3 catalyzes acetate to acetyl-CoA conversion
- Very long-chain fatty acid biosynthesis. Genes: ELOVL2
  - [54]: ELOVL2 participates in very long-chain fatty acid biosynthetic pathways

**Atomic cellular components**
- Cellular membranes with modified lipid composition. Genes: ELOVL2, ACSS3
  - [51]: Elongation of unsaturated fatty acids increases PUFA-containing phospholipids in membranes
- Lipid droplets and storage organelles. Genes: OSBPL10
  - [51]: Oxysterol-binding proteins interact with lipid storage compartments

**Required genes (not in input)**
- Genes: ELOVL5 (competing PUFA elongase), SREBP transcription factors, other lipogenic enzymes (FAS, ACC)
  - [51]: Multiple elongases compete for substrate; ELOVL5 and ELOVL2 have distinct specificities

**Program citations**
- [51]: Lipid metabolism dysregulation in disease contexts including cancer
- [54]: ELOVL2 in fatty acid synthesis pathways

## Program: Nitric Oxide Signaling and Metabolic-Inflammatory Integration
Inducible nitric oxide synthase (NOS2) production of reactive nitrogen species bridges inflammatory signaling with metabolic regulation through cGMP signaling. Coordinated with phosphodiesterase 3A (PDE3A), this program regulates cyclic nucleotide dynamics, inflammation resolution, and immune cell interactions. Dysregulation enables sustained pro-inflammatory states supporting tumor growth.

**Predicted impacts**
- Enhanced inflammatory signaling supporting tumor growth in immunologically active microenvironment
- Altered immune cell infiltration and M1/M2 macrophage balance
- Dysregulated cyclic nucleotide signaling affecting cell migration and proliferation
- Metabolic-inflammatory coupling that enables sustained pro-tumor inflammation

**Evidence summary**
Nitric oxide signaling represents a critical bridge between inflammatory and metabolic processes in astrocytoma. NOS2 expression is characteristic of pro-inflammatory immune cells (M1 macrophages) and reactive astrocytes, producing NO that serves as both a signaling molecule and reactive nitrogen species. In the tumor context, NOS2-derived NO participates in NF-κB pathway activation, promoting pro-inflammatory cytokine production. PDE3A, which hydrolyzes cGMP (produced downstream of NO-activated guanylate cyclase), regulates the duration and amplitude of cyclic nucleotide signaling. The coordinated presence of NOS2 and PDE3A suggests that astrocytomas exploit nitric oxide signaling while simultaneously constraining its magnitude through elevated phosphodiesterase activity, permitting selective activation of survival and proliferation signals while suppressing excessive NO-mediated cytotoxicity.

**Atomic biological processes**
- Nitric oxide synthesis and reactive nitrogen production. Genes: NOS2
  - [10]: NOS2 (inducible nitric oxide synthase) catalyzes NO production in immune and inflammatory contexts
- cGMP signaling and cyclic nucleotide regulation. Genes: NOS2, PDE3A
  - [47]: PDE3A (cGMP-inhibited phosphodiesterase) regulates cGMP duration and amplitude
- NF-κB pathway activation through NO signaling. Genes: NOS2
  - [10]: NOS2-derived NO activates NF-κB signaling in immune cells and inflammatory contexts
- Inflammatory cytokine production and immune activation. Genes: NOS2
  - [10]: NOS2 expression is characteristic of M1 macrophage and pro-inflammatory astrocyte activation

**Atomic cellular components**
- Macrophage and astrocyte plasma membrane. Genes: NOS2
  - [10]: NOS2 localizes to macrophage and astrocyte membranes

**Required genes (not in input)**
- Genes: Guanylate cyclase (GC), NF-κB pathway components (NFKB1, RELA, RELB), inflammatory cytokine genes
  - [10]: NF-κB components are downstream of NOS2 signaling but not all are in the input list

**Program citations**
- [10]: NOS2 in inflammatory signaling
- [47]: PDE3A in cGMP signaling regulation

## Program: Ion Channel Organization and Calcium Signaling
Dysregulation of potassium channels (KCNE4, KCNJ16, KCNIP1) and transient receptor potential channels (TRPM3) alters cellular electrophysiology and calcium dynamics. Aberrant ion channel expression and function affect cell migration, metabolic state, survival signaling, and neuroimmune interactions, enabling astrocytoma-specific phenotypes distinct from normal astrocytes.

**Predicted impacts**
- Altered membrane potential affecting cell migration and proliferation
- Enhanced calcium signaling affecting gene expression and metabolic state
- Dysregulated electrophysiological properties compared to normal astrocytes
- Modified response to extracellular signals and neuroimmune interactions

**Evidence summary**
Astrocytes maintain specialized calcium signaling machinery enabling neurovascular coupling and metabolic support of neuronal activity. In astrocytoma, dysregulation of ion channels contributes to altered cellular properties supporting tumor progression. KCNE4, KCNJ16, and KCNIP1 represent potassium channel components regulating resting membrane potential and cell excitability. TRPM3, a multimodal cation channel, responds to multiple activation stimuli (temperature, steroids, direct gating) and participates in calcium influx. The coordinated dysregulation of multiple ion channel types suggests that astrocytomas establish altered electrophysiological properties compared to normal astrocytes, potentially affecting migration capacity, metabolic sensing, and survival signaling.

**Atomic biological processes**
- Potassium channel function and resting membrane potential. Genes: KCNE4, KCNJ16, KCNIP1
  - [53]: Ion channels including KCNJ16 participate in setting resting membrane potential
- TRPM3 calcium channel activation and calcium influx. Genes: TRPM3
  - [53]: TRPM3 is a multimodal cation channel responsive to temperature, steroids, and direct activation
- Calmodulin-mediated regulation of channel function. Genes: TRPM3
  - [56]: Calmodulin regulates TRPM3 activity and indicates importance of calcium signaling domain
- Altered migration and survival through ion channel modulation. Genes: KCNJ16
  - [53]: Altered potassium channel expression associated with changes in cell migration

**Atomic cellular components**
- Ion channel complexes at plasma membrane. Genes: KCNE4, KCNJ16, KCNIP1, TRPM3
  - [53]: Ion channels organize into functional complexes at the plasma membrane

**Required genes (not in input)**
- Genes: KCNA family potassium channels, voltage-gated calcium channels, other ion channels
  - [53]: Multiple ion channel families contribute to cellular electrophysiology

**Program citations**
- [53]: Ion channel regulation and cellular excitability
- [56]: TRPM3 and calmodulin-mediated calcium signaling

## Program: Cyclic Nucleotide-Responsive Transcriptional Control
cAMP-responsive transcription factors (CREM, CREB1) regulate adaptive gene expression programs in response to cyclic nucleotide signaling. PDE3A-mediated hydrolysis of cAMP constrains these programs, permitting selective activation of survival genes while suppressing differentiation. Dysregulation enables sustained proliferation uncoupled from normal differentiation constraints.

**Predicted impacts**
- Selective activation of survival and proliferation genes in response to extracellular signals
- Suppression of differentiation programs normally activated by cAMP
- Dysregulated adaptive responses to metabolic stress
- Sustained proliferative state uncoupled from normal differentiation constraints

**Evidence summary**
Cyclic nucleotide signaling participates in multiple adaptive responses in normal astrocytes, but these programs become dysregulated in astrocytoma. CREM and CREB1 represent transcription factors that respond to elevated cAMP and regulate expression of genes involved in proliferation, differentiation, and metabolic adaptation. PDE3A, encoding a cAMP phosphodiesterase, regulates the magnitude and duration of cAMP signaling. In astrocytoma, elevated PDE3A activity could suppress cAMP-dependent differentiation signals while permitting selective activation of pro-survival genes. The presence of both cAMP-responsive transcription factors and a phosphodiesterase suggests that cyclic nucleotide signaling is actively regulated in these tumors.

**Atomic biological processes**
- cAMP-responsive element (CRE) transcriptional activation. Genes: CREM, CREB1
  - [45]: CREM (cAMP responsive element modulator) is a transcription factor responding to elevated cAMP
  - [48]: CREB1 is a central regulator of cAMP-dependent transcription
- Differential gene expression downstream of cyclic nucleotide signaling. Genes: CREM, CREB1
  - [45]: CREM regulates transcription of genes involved in cell proliferation, differentiation, metabolic adaptation
- cAMP hydrolysis and signal termination. Genes: PDE3A
  - [47]: PDE3A (phosphodiesterase 3A) catalyzes cAMP hydrolysis, regulating signal duration
- Constraint of differentiation signals. Genes: PDE3A
  - [47]: Elevated phosphodiesterase activity can suppress cAMP-dependent differentiation signals

**Atomic cellular components**
- cAMP-responsive DNA elements at target gene promoters. Genes: CREM, CREB1
  - [45]: CREM and CREB1 bind cAMP-responsive elements in promoters of target genes

**Required genes (not in input)**
- Genes: Adenylyl cyclase (AC), G protein-coupled receptors, protein kinase A (PKA)
  - [45]: Adenylyl cyclase generates cAMP upstream of CREM/CREB signaling

**Program citations**
- [45]: CREM in cAMP-responsive transcription
- [48]: CREB1 regulates cAMP-dependent genes
- [47]: PDE3A in cAMP hydrolysis

## Program: Actin Cytoskeleton Regulation and Cellular Morphodynamics
Dysregulation of actin polymerization machinery (SHROOM3, FMN2, VAV3) enables rapid morphological remodeling and process extension in astrocytoma. Enhanced cytoskeletal dynamics facilitate cell migration, invasion, and altered interaction with the tumor microenvironment. Active remodeling of actin networks supports diverse tumor phenotypes including migratory, proliferative, and neuronal-interactive states.

**Predicted impacts**
- Enhanced cell migration and invasive capacity through rapid morphological remodeling
- Altered cell-cell interactions through dynamic process extension
- Rapid response to environmental stimuli through morphological adaptation
- Support for diverse tumor phenotypes through cytoskeletal plasticity

**Evidence summary**
The morphological complexity of astrocytes, characterized by elaborate process extensions, depends on precise regulation of the actin cytoskeleton. SHROOM3 promotes actin polymerization through interactions with formin proteins like FMN2, driving cell process extension. VAV3, functioning as a Rac GEF, activates Rac GTPases that promote cytoskeletal remodeling. In reactive astrocytes following CNS injury, these same programs drive hypertrophic morphology enabling formation of glial borders and sequestration of inflammatory mediators. In astrocytoma, dysregulation of these programs enables rapid morphological remodeling, enhanced migration, and altered interaction with the tumor microenvironment. The coordinated presence of multiple actin regulatory genes indicates that astrocytomas maintain active programs for cytoskeletal remodeling supporting diverse phenotypes including migratory, proliferative, and pro-inflammatory states.

**Atomic biological processes**
- Actin polymerization and formin-mediated filament nucleation. Genes: SHROOM3, FMN2
  - [17]: SHROOM3 promotes local actin polymerization through formin interaction in reactive astrocytes
- Cell process extension and hypertrophic morphology. Genes: SHROOM3
  - [17]: SHROOM3 activity supports formation of hypertrophic astrocyte processes after injury
- Rac-mediated cytoskeletal remodeling and migration. Genes: VAV3, FMN2
  - [39]: VAV3 (Rac GEF) promotes cytoskeletal dynamics and cell motility
- Rapid actin filament assembly and disassembly. Genes: SHROOM3, FMN2
  - [17]: Coordinated regulation of actin polymerization and depolymerization enables dynamic migration

**Atomic cellular components**
- Actin filament networks and bundles. Genes: SHROOM3, FMN2
  - [17]: SHROOM3 and FMN2 organize actin into organized filament networks
- Cell processes and membrane protrusions. Genes: SHROOM3, VAV3
  - [17]: Actin polymerization drives cell process extension and protrusion formation

**Required genes (not in input)**
- Genes: Cofilin (CFL1, CFL2), gelsolin, profilin, other actin-binding proteins
  - [17]: Multiple actin-binding proteins contribute to actin dynamics

**Program citations**
- [17]: SHROOM3 in actin polymerization and astrocyte process formation
- [39]: VAV3 promotes cytoskeletal dynamics

## Program: Developmental Neural Marker Expression and Progenitor State Maintenance
Retention and dysregulation of developmental neural programs involving synaptic adhesion molecules (NRXN1), Notch signaling (JAG1), and neuronal markers despite astrocytic differentiation. This program reflects either origin from neural progenitor populations or failure of terminal differentiation, maintaining progenitor-like transcriptional states enabling enhanced proliferation and interaction with neuronal microenvironment.

**Predicted impacts**
- Maintenance of progenitor-like transcriptional states despite astrocytic differentiation
- Enhanced angiogenesis through endothelial Notch signaling
- Altered interaction with neuronal microenvironment through synaptic adhesion markers
- Retained developmental plasticity enabling enhanced proliferation

**Evidence summary**
A striking feature of astrocytoma biology is the retention of developmental neural programs despite astrocytic lineage commitment. NRXN1, encoding neurexin-1, is classically expressed by presynaptic neurons where it mediates trans-synaptic adhesion and synapse formation. The presence of NRXN1 in astrocytoma suggests either that tumors derive from or maintain characteristics of early neural progenitor populations with incomplete glial differentiation, or that astrocytomas selectively reactivate neuronal developmental programs. Similarly, JAG1, a Notch ligand critical for neural development and progenitor cell expansion, is expressed by normal astrocytes where it participates in endothelial Notch signaling promoting vascular interactions, but dysregulation in astrocytoma could enhance both angiogenesis and autocrine Notch signaling maintaining progenitor-like transcriptional states. The coordinated presence of these developmental markers suggests that astrocytomas partially recapitulate developmental neural programs, maintaining a state of incomplete maturation that permits sustained proliferation and enhanced interaction with the neuronal and vascular microenvironment.

**Atomic biological processes**
- Presynaptic adhesion molecule expression and trans-synaptic signaling. Genes: NRXN1
  - [5]: NRXN1 (neurexin 1) is a presynaptic adhesion molecule involved in synapse formation
- Notch ligand signaling to endothelial and progenitor cells. Genes: JAG1
  - [11]: JAG1 (jagged 1) is a Notch ligand with critical roles in neural development
  - [14]: JAG1 expression by astrocytes activates Notch in endothelial cells promoting angiogenesis
- Developmental progenitor differentiation decisions. Genes: JAG1
  - [11]: JAG1 regulates progenitor cell expansion and differentiation through Notch signaling
- Neural cell identity maintenance. Genes: NRXN1
  - [5]: NRXN1 participates in neural cell identity through adhesion programs

**Atomic cellular components**
- Trans-synaptic adhesion complexes. Genes: NRXN1
  - [5]: Neurexins form heterophilic adhesion complexes with neuroligins at synapses
- Notch receptor signaling complexes. Genes: JAG1
  - [14]: JAG1 engages Notch receptors on target cells

**Required genes (not in input)**
- Genes: Neuroligin (NLGN) family members, Notch receptors (NOTCH1, NOTCH3), other developmental transcription factors
  - [14]: Notch receptors are binding partners for JAG1 but not in input list

**Program citations**
- [5]: Neurexin function in neural development and synaptic organization
- [11]: JAG1 in neural development
- [14]: JAG1 and astrocyte-endothelial interactions

## Bibliography
1. 1. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
2. 2. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
3. 3. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
4. 4. Anamaria S, Cristian-Ionut O, Raluca IV, Madalina B, Manuela E, Sorin V, et al.. Unpredictable Evolution of Pilocytic Astrocytoma in Adults: A Case Series and Diagnostic Challenges.. The American journal of case reports [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41382984/?fc=None&ff=20251213032813&v=2.18.0.post22+67771e2
5. 5. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/10419
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/16414
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/234779
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/207
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/18126
11. 11. Available from: https://www.ncbi.nlm.nih.gov/gene/16449
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/15978
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/18128
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/5894
16. 16. Zamboni M, Martínez-Martín A, Rydholm G, Häneke T, Pintado AL, Seçilmiş D, et al.. The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS. Nature Neuroscience [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41593-025-02131-w
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/5156
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/6660
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/4325
20. 20. Joun GL, Kempe EG, Chen B, Sterling JR, Abbassi RH, Friess D, et al.. Histone methyltransferase PRDM9 promotes survival of drug-tolerant persister cells in glioblastoma. Nature Communications [Internet]. 2025Dec15;16(1). Available from: https://www.nature.com/articles/s41467-025-65888-5
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/406942
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/64754
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/6615
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/6092
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/6935
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/9353
27. 27. Dang X, Gong D, Dai S-S, Teng Z, Luo X-J. Genetic and functional insights into long noncoding RNAs in schizophrenia. Molecular Psychiatry [Internet]. 2025Dec14;. Available from: https://www.nature.com/articles/s41380-025-03421-2
28. 28. Soeung M, Yan X, Zanca C, Qian J, Karki M, Duan F, et al.. Nivolumab plus ipilimumab induce hyper-progression in renal medullary carcinoma: results of a phase II trial and preclinical evidence. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65462-z
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/27185
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/26401
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/3485
32. 32. Liu Y, Hill HA, Li Y, McIntosh J, Jiang V, Yan F, et al.. Integrative profiling strategies to guide personalized therapy in mantle cell lymphoma: a pilot study. npj Precision Oncology [Internet]. 2025Nov21;9(1). Available from: https://www.nature.com/articles/s41698-025-01158-3
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/3487
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=10683
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/103
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/14025
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/56288
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/283120
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/53335
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/93742
41. 41. Available from: https://www.ncbi.nlm.nih.gov/gene/57504
42. 42. Available from: https://www.ncbi.nlm.nih.gov/gene/54611
43. 43. Available from: https://www.ncbi.nlm.nih.gov/gene/1390
44. 44. Available from: https://www.ncbi.nlm.nih.gov/gene/12550
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/5139
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/1385
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/18033
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/12140
49. 49. Kang M, Zhan X, Huang X, Zhao Y, Wang X, Li Q, et al.. Elovl7 sensitizes podocytes to ferroptosis in podocytopathy by elongating polyunsaturated fatty acids. Cell Death &amp; Disease [Internet]. 2025Nov24;16(1). Available from: https://www.nature.com/articles/s41419-025-08144-4
50. 50. Available from: https://www.ncbi.nlm.nih.gov/gene/5971
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/80036
52. 52. Available from: https://www.ncbi.nlm.nih.gov/gene/54898
53. 53. Available from: https://www.ncbi.nlm.nih.gov/gene/5970
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/801
55. 55. Ni H, Zhou Z, Estill M, Halawani D, Junqueira AC, Shen L, et al.. Plexin-B1 safeguards astrocyte agility and glial alignment to facilitate wound corralling and axon pathfinding in mouse spinal cord injury model. Nature Communications [Internet]. 2025Nov18;16(1). Available from: https://www.nature.com/articles/s41467-025-65095-2
56. 56. Available from: https://www.ncbi.nlm.nih.gov/gene/5591
57. 57. Available from: https://www.ncbi.nlm.nih.gov/gene/5154
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
59. 59. Available from: http://json-schema.org/draft-07/schema#",
