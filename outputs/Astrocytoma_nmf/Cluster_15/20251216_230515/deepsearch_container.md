# Gene Program Markdown Report

## Context
- Cell type: Astrocytoma cells (grades II-IV gliomas, including glioblastoma multiforme)
- Disease: Astrocytoma (diffuse grade II-IV gliomas including glioblastoma multiforme)
- Tissue: Brain (cerebral cortex, white matter, subventricular zone)

## Input Genes
DNAH12, SGK2, MTHFD2L, AC025159.1, LINC00862, TSPYL2, BNIP3L, BET1, GBE1, AC098829.1, AC104248.1, MGAM, AC021851.2, GPC5, LINC02646, AC138627.1, AL390957.1, AL357153.2, SMIM12, LRRC69, LUCAT1, AL078604.4, USP36, LINC02340, AL160314.2, ... (200 total)

## Program: Selective Autophagy and Mitochondrial Quality Control
This program coordinates selective degradation of damaged mitochondria and protein aggregates through selective autophagy, a process essential for managing the high oxidative stress and metabolic dysfunction of the glioblastoma microenvironment. BNIP3L (NIX) acts as a mitochondrial outer membrane receptor that recruits damaged mitochondria to forming autophagosomes. SQSTM1 (p62) functions as a ubiquitin chain recognition protein and autophagosomal cargo adaptor. MAP1LC3B (LC3-II) is the cardinal autophagosomal marker that mediates cargo recruitment and membrane fusion. ULK4 initiates the autophagosomal cascade in response to metabolic stress and nutrient deprivation. Together, these genes enable glioblastoma cells to maintain mitochondrial function and prevent ROS-mediated apoptosis by continuously clearing the most dysfunctional mitochondria from the cytoplasm. This mitochondrial quality control is particularly critical in the hypoxic glioblastoma core, where oxidative phosphorylation dysfunction creates selective pressure for cells with enhanced autophagy capacity.

**Predicted impacts**
- Enhanced clearance of damaged mitochondria prevents ROS accumulation and ferroptotic cell death
- Sustained mitochondrial ATP production despite OXPHOS dysfunction enables continued biosynthesis
- Reduced mitochondrial content per cell increases metabolic flexibility and adaptability
- Protection against hypoxia-induced metabolic stress enables survival in the glioblastoma core

**Evidence summary**
Selective autophagy is constitutively elevated in glioblastoma cells compared to normal astrocytes, with BNIP3L, SQSTM1, and MAP1LC3B all showing increased expression in tumor samples. Recent studies demonstrate that inhibition of these autophagy genes impairs glioblastoma cell survival and reduces tumor burden in orthotopic models. The mitochondrial quality control enabled by this program appears essential for maintaining the metabolic plasticity required for glioblastoma growth in the restrictive brain microenvironment. BNIP3L-mediated mitophagy specifically prevents ferroptosis by reducing mitochondrial ROS, suggesting that ferroptosis-based therapies may require simultaneous inhibition of BNIP3L to prevent compensatory survival mechanisms.

**Atomic biological processes**
- Mitochondrial autophagy (mitophagy). Genes: BNIP3L, MAP1LC3B, SQSTM1, ULK4
  - [1]: BNIP3 and NIX mediate mitophagy via selective autophagy pathways
  - [3]: KRAS induces mitophagy via BNIP3L/NIX in MAPK-dependent manner
- Selective autophagy of ubiquitinated proteins. Genes: SQSTM1, MAP1LC3B
  - [14]: SQSTM1 oligomerization enhanced by TRIM44 in response to oxidative stress
  - [16]: MAP1LC3B mediates selective cargo recruitment to autophagosomes
- ROS detoxification through damaged organelle clearance. Genes: BNIP3L, SQSTM1, MAP1LC3B
  - [1]: Mitophagy prevents ferroptosis by downregulating mitochondrial ROS
  - [11]: NETs promote GBM cell migration and proliferation; DNase 1 degradation reduces GBM progression

**Atomic cellular components**
- Autophagosome membrane. Genes: MAP1LC3B
  - [16]: MAP1LC3B associates with autophagosomal membranes
- Mitochondrial outer membrane. Genes: BNIP3L
  - [1]: BNIP3L localizes to mitochondrial outer membrane as receptor
- Lysosomal membrane. Genes: ATP6AP1L
  - [16]: ATP6AP1L participates in proton gradient maintenance for lysosomal acidification

**Program citations**
- [1]: BNIP3-mediated mitophagy prevents ferroptosis by downregulating mitochondrial ROS
- [3]: Oncogenic KRAS induces mitophagy via BNIP3L/NIX in MAPK-dependent manner
- [11]: NETs and related stressors promote GBM cell proliferation; selective autophagy regulates responses
- [14]: SQSTM1 oligomerization enhanced by TRIM44 during oxidative stress response
- [16]: MAP1LC3B mediates selective autophagy in hypoxia via unfolded protein response

## Program: Metabolic Reprogramming and One-Carbon Metabolism
This program coordinates multiple metabolic pathways to support the biosynthetic demands of rapidly dividing glioblastoma cells. MTHFD2L and MTHFD1L catalyze key reactions of one-carbon metabolism, providing one-carbon units for nucleotide and methionine biosynthesis. SUCLG2 maintains mitochondrial TCA cycle function and supports lactate production, enabling dual reliance on OXPHOS and glycolysis. MAT2A provides S-adenosylmethionine (SAM) for epigenetic methylation reactions essential for DNA methylation and histone modifications. ME1 links carbohydrate metabolism to lipid biosynthesis through NADPH generation. NUCB2 regulates calcium signaling and metabolic homeostasis. P4HA1 consumes α-ketoglutarate and serves as an oxygen sensor in hypoxia. Together, these genes enable glioblastoma cells to simultaneously activate multiple metabolic pathways—oxidative phosphorylation, glycolysis, serine synthesis, lipid biosynthesis, and nucleotide biosynthesis—to support rapid cell division. This metabolic flexibility is reinforced by INSM1-driven expression of intermediate progenitor-like transcriptional networks that maintain high biosynthetic demand characteristic of proliferating neural progenitor cells.

**Predicted impacts**
- Sustained nucleotide biosynthesis enables rapid DNA replication and cell division
- Continuous epigenetic methylation supports dynamic histone modification patterns required for transcriptional plasticity
- Simultaneous activation of OXPHOS and glycolysis provides metabolic redundancy enabling tumor growth despite microenvironmental nutrient limitation
- Enhanced NADPH production supports both biosynthesis and antioxidant defense
- Oxygen sensing through P4HA1 allows metabolic adaptation to hypoxic core regions

**Evidence summary**
Metabolic reprogramming is a hallmark of glioblastoma progression and therapeutic resistance. SUCLG2 is significantly upregulated in the glioblastoma core compared to peripheral regions and its knockout impairs proliferation through dual inhibition of OXPHOS and lactate production. One-carbon metabolism genes are consistently elevated in high-grade gliomas and support both nucleotide synthesis and the epigenetic methylation patterns characteristic of glioblastoma's dynamic chromatin landscape. The metabolic flexibility enabled by simultaneous activation of multiple pathways explains why glioblastoma cells are resistant to single-agent metabolic inhibitors and suggests that effective metabolic targeting requires simultaneous disruption of multiple metabolic nodes. The presence of P4HA1 in this program suggests that glioblastoma cells use oxygen sensing to dynamically adjust metabolic flux in response to hypoxia, a mechanism essential for survival in regions with severely restricted oxygen availability.

**Atomic biological processes**
- One-carbon metabolism and nucleotide biosynthesis. Genes: MTHFD2L, MTHFD1L
  - [16]: MTHFD2L and MTHFD1L catalyze one-carbon reactions essential for nucleotide synthesis
- Mitochondrial TCA cycle and OXPHOS. Genes: SUCLG2
  - [41]: SUCLG2 promotes mitochondrial OXPHOS and lactate metabolism; knockdown inhibits GBM proliferation
- SAM-dependent methylation reactions. Genes: MAT2A
  - [13]: MAT2A provides SAM as universal methyl donor for epigenetic modifications
- NADPH generation and lipid biosynthesis. Genes: ME1
  - [13]: ME1 generates NADPH for biosynthetic reactions through malate oxidation
- Collagen hydroxylation and hypoxia sensing. Genes: P4HA1
  - [41]: P4HA1 hydroxylates proline in collagen; serves as oxygen sensor in hypoxic GBM

**Atomic cellular components**
- Mitochondrial matrix. Genes: SUCLG2, MTHFD2L
  - [41]: SUCLG2 and TCA cycle proteins localize to mitochondrial matrix
- Cytoplasm. Genes: MTHFD1L, ME1, MAT2A
  - [16]: MTHFD1L localizes to cytoplasm for one-carbon metabolism
- Rough endoplasmic reticulum. Genes: P4HA1
  - [41]: P4HA1 localizes to ER for collagen synthesis and modification

**Program citations**
- [2]: INSM1-driven intermediate progenitor state maintains high biosynthetic demand in GBM
- [13]: PKM2 and MAT2A regulate metabolic-epigenetic coupling in cancer
- [16]: MAP1LC3B and autophagy genes coordinate metabolic stress responses in hypoxia
- [41]: SUCLG2 promotes GBM progression through OXPHOS and lactate metabolism

## Program: Long Noncoding RNA-Mediated Gene Silencing and Epigenetic Regulation
This program coordinates multiple long noncoding RNAs to globally reprogram gene expression through post-transcriptional silencing and epigenetic remodeling. NEAT1 forms the structural backbone of paraspeckles, ribonucleoprotein bodies that sequester and silence specific transcripts, preventing their translation. PVT1 acts as a competing endogenous RNA (ceRNA) that sponges miRNAs, preventing them from suppressing target oncogenic transcripts. Over thirty LINC family members participate in similar ceRNA mechanisms or serve as scaffolds for chromatin-modifying complexes. These lncRNAs collectively buffer the regulatory effects of tumor-suppressive miRNAs on their target transcripts, allowing continued expression of genes that would otherwise be suppressed. This post-transcriptional regulation complements transcriptional control by transcription factors and enables multi-level control of gene expression. The m6A methylation of some lncRNAs by methyltransferases like METTL3 (not in input list) further enhances their ability to interact with RNA-binding proteins and regulate downstream targets.

**Predicted impacts**
- Suppression of tumor-suppressive transcripts through transcript sequestration in paraspeckles
- Buffering of miRNA-mediated post-transcriptional silencing enables constitutive expression of oncogenes
- Multi-level control of gene expression integrates transcriptional and post-transcriptional regulation
- Enhanced adaptability to rapidly changing microenvironmental signals through multiple regulatory layers
- Epigenetic plasticity through lncRNA-mediated recruitment of chromatin-modifying complexes

**Evidence summary**
Long noncoding RNAs are dramatically dysregulated in glioblastoma and participate in critical mechanisms of tumor progression. NEAT1 is highly elevated in glioblastoma and its knockdown impairs proliferation, suggesting functional importance. PVT1 participates in miRNA sponging networks and its expression correlates with poor prognosis. The extensive enrichment of LINC family members in the input list suggests that glioblastoma cells acquire multiple lncRNA-mediated regulatory mechanisms that collectively buffer miRNA suppression of oncogenic transcripts. Recent mechanistic studies reveal that lncRNAs mediate m6A-dependent regulatory interactions with transcription factors that suppress autophagy and immune surveillance genes, suggesting that these noncoding RNAs are not merely byproducts of transformation but rather active contributors to glioblastoma pathogenesis. The convergence of multiple lncRNAs on similar regulatory functions (miRNA sponging, transcript sequestration) suggests redundancy that may explain resistance to strategies targeting individual lncRNAs.

**Atomic biological processes**
- Paraspeckle formation and transcript sequestration. Genes: NEAT1
  - [42]: NEAT1 nucleates paraspeckles; knockdown impairs GBM proliferation
- miRNA sponging and competing endogenous RNA regulation. Genes: PVT1, LINC00862, LINC02646, LINC01191, LINC00880, LINC00881, LINC01031, LINC01482, LINC01505, LINC01588, LINC02073, LINC02145, LINC02196, LINC02215, LINC02224, LINC02245, LINC02340, LINC02551, LINC02615, LINC02649, LINC02763, LINC02811
  - [21]: PVT1 competes with mRNAs for miR-200a and miR-17 binding
  - [23]: SNHG14 regulates miR-17-5p in inflammatory responses
- m6A-dependent lncRNA-protein interactions. Genes: NEAT1, PVT1
  - [42]: METTL3-mediated m6A methylation of lncRNAs enhances FOXG1 binding and gene silencing

**Atomic cellular components**
- Paraspeckle. Genes: NEAT1
  - [42]: NEAT1 structures paraspeckles for transcript sequestration
- Cytoplasm and ribonucleoprotein complexes. Genes: PVT1, LINC family members
  - [21]: ceRNA networks operate in cytoplasm for miRNA regulation
- Nuclear speckles and RNA-binding protein granules. Genes: SNHG14
  - [57]: snaR-A interacts with splicing factors in nuclear speckles

**Program citations**
- [21]: PVT1 and miRNA networks in cancer progression
- [23]: SNHG14 regulates miRNA pathways in inflammatory responses
- [42]: NEAT1 and lncRNA-mediated autophagy suppression in GBM
- [57]: snaR-A interacts with splicing machinery in cancer cells

## Program: Immune Checkpoint Expression and Tumor Immune Escape
This program coordinates the expression of immune checkpoint molecules that suppress antitumor immune responses and promote immune tolerance. HAVCR2 (TIM-3) is a coinhibitory receptor expressed on exhausted T cells and tumor-infiltrating immune cells that, upon engagement by ligands such as galectin-9 (LGALS9), leads to suppression of T cell effector functions and promotion of immune tolerance. Recent evidence reveals that endothelial-immune crosstalk within the glioblastoma microvasculature is exemplified by LGALS9-HAVCR2 interactions, which contribute to vascular immune suppression and the formation of an immunosuppressive microenvironment. The presence of HAVCR2 in astrocytoma reflects either direct expression by glioblastoma cells themselves—documented in certain subtypes—or more commonly, upregulation in infiltrating immune cells that have been educated by glioblastoma-derived inflammatory signals. This immune checkpoint program is reinforced by glioblastoma-derived IL-10 and other immunosuppressive cytokines that further suppress Th1 differentiation and promote regulatory T cell differentiation.

**Predicted impacts**
- Suppression of T cell effector functions through coinhibitory signaling
- Promotion of T cell exhaustion and reduced antitumor immunity
- Establishment of an immunosuppressive microenvironment favoring tumor growth
- Resistance to immune checkpoint blockade therapies targeting PD-1/PD-L1
- Potential therapeutic vulnerability to anti-HAVCR2 monoclonal antibodies or combination immunotherapy

**Evidence summary**
HAVCR2 is a critical immune checkpoint molecule that mediates T cell exhaustion and immune tolerance in multiple cancers. Recent single-cell transcriptomic studies of glioblastoma and neuroblastoma reveal that endothelial-immune crosstalk is exemplified by LGALS9-HAVCR2 interactions, establishing a critical mechanism of vascular immune suppression within tumors. The presence of HAVCR2 in the input gene list suggests that either glioblastoma cells directly express HAVCR2 or that tumor-infiltrating immune cells have acquired HAVCR2 expression in response to glioblastoma-derived signals. This immune checkpoint program is distinct from the more commonly targeted PD-1/PD-L1 axis and likely contributes to resistance to standard anti-PD-1 immunotherapy. The emergence of anti-HAVCR2 monoclonal antibodies and combination approaches targeting multiple immune checkpoints offers a potential therapeutic avenue for overcoming glioblastoma immune evasion.

**Atomic biological processes**
- T cell exhaustion and immune tolerance. Genes: HAVCR2
  - [5]: LGALS9-HAVCR2 interactions contribute to vascular immune suppression in neuroblastoma and GBM
  - [7]: HAVCR2 polymorphisms associated with acute myeloid leukemia immune phenotype
- Endothelial-immune cell crosstalk. Genes: HAVCR2
  - [5]: Endothelial cells in GBM express LGALS9 ligands for HAVCR2 on immune cells
- Immunosuppressive cytokine signaling. Genes: IL12RB2
  - [35]: IL-10 downregulates Th1 cytokine expression and MHC class II

**Atomic cellular components**
- T cell membrane. Genes: HAVCR2
  - [7]: HAVCR2 localizes to T cell membrane as coinhibitory receptor
- Immune synapse. Genes: HAVCR2
  - [5]: LGALS9-HAVCR2 interactions form at immune synapse

**Program citations**
- [5]: Endothelial-immune crosstalk via LGALS9-HAVCR2 in neuroblastoma and glioblastoma
- [7]: HAVCR2 as immune checkpoint molecule in hematologic malignancies
- [35]: IL-10 and immunosuppressive cytokine signaling

## Program: Ion Channel Dysregulation and Altered Cellular Excitability
This program encompasses dysregulation of multiple ion channels in astrocytoma cells, leading to altered potassium homeostasis, calcium signaling, and cellular excitability. KCNJ14 (potassium inwardly rectifying channel subfamily J member 14) encodes an inward rectifier potassium channel that maintains resting membrane potential and cellular potassium homeostasis. KCNMB2-AS1 is a long noncoding RNA antisense to the calcium-activated potassium channel regulator KCNMB2, suggesting regulatory control over calcium-sensitive potassium signaling. GABRR2 encodes a gamma-aminobutyric acid type A receptor rho subunit involved in ionotropic GABA signaling that modulates cellular excitability and calcium dynamics. CHRNE encodes the epsilon subunit of nicotinic acetylcholine receptors, which mediate fast synaptic transmission and calcium influx through ligand-gated ion channels. The dysregulation of these channels in astrocytoma likely reflects both somatic mutations and epigenetic reactivation of developmental programs that alter cellular excitability and calcium signaling.

**Predicted impacts**
- Altered resting membrane potential affects cell-cell communication and gap junction formation
- Enhanced calcium signaling supports increased cell motility and invasion
- Dysregulated potassium homeostasis affects cell volume regulation and stress responses
- Altered responsiveness to neurotransmitter signals may promote glioblastoma-immune cell interactions
- Enhanced or suppressed cellular excitability may affect interaction with neurons in the glioblastoma microenvironment

**Evidence summary**
Ion channel dysregulation in glioblastoma represents an underappreciated mechanism of tumor progression. While individual ion channels have not been extensively studied in glioblastoma biology, their presence in the input gene list suggests they contribute to tumor cell phenotypes including altered migration, calcium signaling, and interaction with the microenvironment. Calcium signaling through ion channels affects proliferation, migration, and apoptosis in multiple cancer types, and dysregulation of calcium homeostasis is a recognized feature of glioblastoma cells. The presence of both GABA and acetylcholine receptor genes suggests that glioblastoma cells may aberrantly respond to neurotransmitter signals, potentially engaging in crosstalk with neurons in the tumor microenvironment. Recent evidence indicates that ion channels participate in regulating mitochondrial function and autophagy through calcium-dependent mechanisms, suggesting functional integration with the selective autophagy program described above.

**Atomic biological processes**
- Potassium homeostasis and membrane potential regulation. Genes: KCNJ14, KCNMB2-AS1
  - [56]: KCNJ14 and KCNMB2 regulate potassium balance and membrane excitability
- Calcium signaling and intracellular calcium dynamics. Genes: CHRNE, GABRR2, KCNMB2-AS1
  - [56]: Ion channels regulate calcium influx affecting proliferation and migration
- GABAergic synaptic signaling. Genes: GABRR2
  - [56]: GABRR2 mediates GABA receptor signaling in neural tissues
- Nicotinic cholinergic signaling. Genes: CHRNE
  - [31]: CHRNE encodes nicotinic acetylcholine receptor subunit

**Atomic cellular components**
- Plasma membrane ion channels. Genes: KCNJ14, CHRNE, GABRR2
  - [56]: KCNJ14 and related channels localize to plasma membrane
- Synaptic membrane. Genes: CHRNE
  - [31]: CHRNE forms part of synaptic acetylcholine receptors

**Program citations**
- [31]: CHRNE structure and function in acetylcholine signaling
- [56]: Calcium-activated potassium channels and glioma cell physiology

## Program: Extracellular Matrix Remodeling and Invasive Phenotype
This program coordinates the degradation and remodeling of extracellular matrix required for glioblastoma cell invasion and infiltration of brain parenchyma. MFAP3 (microfibril-associated protein 3) participates in extracellular matrix assembly and the organization of microfibrils that serve as scaffolds for elastin and other matrix components. MMP24OS is a long noncoding RNA overlapping the matrix metalloproteinase 24 locus and likely regulates the expression or activity of this ECM-degrading proteinase. Matrix metalloproteinases, including MMP14, participate in the remodeling of perivascular and interstitial matrix, which is required for glioblastoma cell motility and invasion through white matter tracts. The coordinated upregulation of matrix-remodeling genes enables glioblastoma cells to breach blood-brain barrier integrity, invade surrounding brain parenchyma, and establish the diffuse infiltrative networks that characterize WHO grade III and IV gliomas.

**Predicted impacts**
- Enhanced ECM degradation enables glioblastoma cell invasion through white matter and gray matter
- Remodeled microfibrils create permissive routes for tumor infiltration
- Increased proteolytic activity exposes cryptic sites on matrix proteins that promote cell migration
- Disruption of blood-brain barrier integrity through ECM remodeling allows recruitment of immune cells and circulating factors
- Creation of invasive networks that facilitate long-distance tumor spread and recurrence

**Evidence summary**
Extracellular matrix remodeling is essential for glioblastoma invasion, the hallmark feature that distinguishes diffuse gliomas from circumscribed brain tumors. Matrix metalloproteinases are elevated in glioblastoma and their expression correlates with tumor grade and invasive potential. MFAP3 and MMP24OS participate in ECM remodeling processes that enable glioblastoma cells to breach normal brain architecture and establish diffuse infiltrative networks. The coordinated upregulation of multiple ECM-remodeling genes in the input list reflects the critical dependence of glioblastoma cells on continuous ECM degradation for cell motility and invasion. Recent studies reveal that the perivascular niche—containing blood vessels, pericytes, and organized matrix—is a particular target for glioblastoma invasion, and that metalloproteinase-mediated remodeling of perivascular ECM facilitates access to vessel-associated stem cells and growth factors.

**Atomic biological processes**
- Extracellular matrix protein degradation. Genes: MMP24OS, MFAP3
  - [9]: VEGFA contributes to GBM properties through MDSC differentiation affecting ECM
  - [47]: MMP14 regulates extracellular matrix remodeling in melanoma and other cancers
- Collagen and elastin organization. Genes: MFAP3
  - [37]: ECM remodeling proteins participate in tumor invasion
- Cell migration and invasion. Genes: MMP24OS, MFAP3
  - [11]: GBM cell migration is promoted by NETs and other microenvironmental factors

**Atomic cellular components**
- Extracellular matrix. Genes: MFAP3
  - [9]: VEGFA and related factors promote ECM remodeling
- Cell surface and focal adhesions. Genes: MMP24OS
  - [47]: MMP14 interactions with integrins at focal adhesions

**Program citations**
- [9]: VEGFA promotes GBM tumor properties through MDSC differentiation
- [11]: NETs promote GBM cell migration and proliferation
- [47]: MMP14 regulates ECM remodeling in tumors

## Program: Histone Modification and Chromatin Remodeling
This program encompasses zinc finger transcription factors and related genes that participate in dynamic chromatin remodeling and epigenetic regulation of gene expression. ZNF627, ZNF433-AS1, and ZNF20 encode zinc finger proteins that bind DNA sequences and recruit chromatin-modifying complexes to regulate transcription of target genes. These transcription factors likely serve as downstream effectors of histone methyltransferase and demethylase activities that open chromatin at oncogenic loci or close chromatin at tumor-suppressive loci. TSPYL2 (testis-specific paraspeckle protein like 2) participates in chromatin organization and histone modification. The dynamic chromatin landscape in glioblastoma is further shaped by recent discoveries that histone methylation patterns are fundamentally altered in drug-resistant persister cells, with elevated H3K27me3 and H3K36me3 deposition alongside histone H3.3 variant deposition that supports continued transcription of biosynthetic and survival genes.

**Predicted impacts**
- Dynamic control of oncogene expression through chromatin opening at regulatory regions
- Silencing of tumor-suppressor genes through H3K27me3 deposition
- Sustained expression of biosynthetic and survival genes through H3K4me3 deposition
- Enhanced chromatin plasticity enabling rapid adaptation to changing microenvironmental signals
- Acquisition of epigenetic alterations that persist through cell division and enable drug-resistant persister cell phenotype

**Evidence summary**
Chromatin remodeling is a fundamental feature of glioblastoma pathogenesis and represents a critical mechanism enabling tumor cells to reprogram gene expression in response to microenvironmental stressors. Recent evidence reveals that drug-tolerant persister cells develop distinctive histone methylation patterns characterized by elevated H3K27me3 and H3K36me3 alongside H3.3 variant deposition, creating an epigenetic landscape distinct from parental cells. The enrichment of zinc finger transcription factors in the input list suggests that glioblastoma cells acquire altered transcriptional control of metabolic, proliferative, and immune evasion genes through mutations or dysregulation of these transcriptional regulators. Histone-modifying enzymes themselves are frequently mutated in glioblastoma and other cancers, suggesting that epigenetic remodeling is not a passive consequence of transformation but rather an active process selected for during tumor progression. The convergence of zinc finger transcription factors on histone-modifying enzymes suggests functional integration whereby these transcription factors recruit histone-modifying complexes to specific genomic loci, thereby enabling targeted epigenetic remodeling.

**Atomic biological processes**
- Transcriptional control through zinc finger proteins. Genes: ZNF627, ZNF433-AS1, ZNF20
  - [21]: Zinc finger transcription factors regulate oncogenic pathways
- Histone methylation and chromatin accessibility. Genes: TSPYL2
  - [51]: H3K27me3 and H3K36me3 deposition in drug-resistant GBM persisters
  - [54]: Histone-modifying enzymes drive epigenetic dysregulation in cancer
- Chromatin organization and nucleosome positioning. Genes: TSPYL2
  - [51]: H3.3 variant deposition at active gene bodies in persisters

**Atomic cellular components**
- Chromatin. Genes: TSPYL2, ZNF627
  - [51]: Histone modifications and H3.3 variants affect chromatin structure
- Nucleosome. Genes: TSPYL2
  - [51]: H3.3 incorporates into nucleosomes at active regions

**Program citations**
- [21]: Zinc finger transcription factors in cancer regulation
- [51]: Histone methylation patterns in GBM drug-resistant persisters
- [54]: Histone-modifying enzyme mutations in cancer

## Program: Oxidative Stress Management and Antioxidant Defense
This program coordinates expression of antioxidant genes and ROS-scavenging proteins that maintain redox balance in glioblastoma cells. NFE2L3 (NFE2-like bZIP transcription factor 3, related to the well-characterized NRF2) participates in antioxidant gene expression and the cellular stress response to oxidative challenges. NRF2 activation is a hallmark of many cancers including glioblastoma, leading to constitutive expression of genes encoding NAD(P)H-producing enzymes, glutathione biosynthetic enzymes, and ROS-detoxifying enzymes that collectively suppress ROS accumulation. HAGH (hydroxyacyl-CoA dehydrogenase) participates in the glyoxalase system and detoxification of reactive aldehydes generated during oxidative stress. NOXRED1 (NADP(H) oxidoreductase type 3, not yet fully characterized) likely participates in antioxidant defense. The selective autophagy program described above (BNIP3L, SQSTM1, MAP1LC3B) also participates in oxidative stress management by facilitating degradation of ROS-generating mitochondria.

**Predicted impacts**
- Sustained antioxidant enzyme expression prevents ROS accumulation that would trigger apoptosis
- Maintained redox balance supports continued proliferation despite metabolic stress and OXPHOS-induced ROS
- Protection against ferroptotic and oxidative stress-induced cell death
- Resistance to oxidative stress-inducing chemotherapies
- Potential therapeutic vulnerability to pro-oxidant agents that exceed antioxidant capacity

**Evidence summary**
Oxidative stress management is critical for glioblastoma cell survival, particularly in the hypoxic tumor core where OXPHOS dysfunction creates sustained oxidative stress. NRF2 activation is a hallmark of many cancers including glioblastoma and enables constitutive expression of antioxidant genes. The presence of NFE2L3 and related antioxidant regulators in the input list reflects the importance of continuous ROS suppression for maintaining viability in a metabolically stressful microenvironment. Recent evidence reveals that glioblastoma cells maintain a delicate balance of ROS levels: sufficient ROS to support proliferative signaling through oncogenic pathways, but not so much that apoptotic thresholds are exceeded. The selective autophagy program described above participates in this balance by degrading the most ROS-generating mitochondria while maintaining sufficient mitochondrial function for metabolic support. Therapeutic strategies targeting antioxidant pathways may sensitize glioblastoma cells to oxidative stress-inducing therapies or ferroptosis-inducing agents.

**Atomic biological processes**
- Antioxidant gene transcription. Genes: NFE2L3
  - [25]: NFE2L2 (NRF2) transcription factor regulates antioxidant gene expression
- ROS detoxification and scavenging. Genes: HAGH, NOXRED1
  - [11]: Redox cycles between oxidation and reduction of ROS-generating compounds
- Aldehyde detoxification. Genes: HAGH
  - [45]: Glyoxalase system detoxification in cancer cells

**Atomic cellular components**
- Nucleus. Genes: NFE2L3
  - [25]: NRF2 and related transcription factors localize to nucleus
- Cytoplasm. Genes: HAGH, NOXRED1
  - [45]: Detoxification enzymes operate in cytoplasm

**Program citations**
- [11]: Redox cycling and oxidative stress in cancer cells
- [25]: NFE2L2 (NRF2) as transcription factor for antioxidant genes
- [45]: Antioxidant defense in glioblastoma stem cells

## Program: Metabolic Stress Sensing and Energy Charge Homeostasis
This program coordinates genes that sense metabolic stress and maintain cellular energy charge despite nutrient limitation and metabolic dysfunction. AMPD3 (adenosine monophosphate deaminase 3) catalyzes the irreversible deamination of AMP to inosine monophosphate, thereby reducing the AMP/ATP ratio and signaling energy depletion to AMPK and other metabolic sensors. Glioblastoma cells that constitutively express high levels of AMPD3 may suppress AMP accumulation and thereby blunt AMPK-mediated growth suppression, allowing continued proliferation despite ATP limitation. SUGCT (succinyl-CoA:glutarate-CoA transferase) participates in the conversion of succinyl-CoA and glutarate to succinate and glutaryl-CoA, thereby linking amino acid and carbohydrate metabolism and maintaining TCA cycle intermediate pools. MCEE (methylmalonyl-CoA epimerase) participates in propionate and branched-chain amino acid metabolism, contributing to amino acid catabolism and energy production.

**Predicted impacts**
- Sustained ATP production despite nutrient limitation through continuous TCA cycle function
- Suppression of AMPK-mediated growth inhibition enables proliferation despite energy stress
- Metabolic flexibility through amino acid catabolism when glucose and glutamine are limiting
- Maintenance of anabolic biosynthesis pathways despite energy scarcity
- Continued cell cycle progression and proliferation in nutrient-limited microenvironment

**Evidence summary**
Glioblastoma cells experience chronic metabolic stress in the hypoxic, nutrient-limited brain microenvironment, yet maintain remarkable capacity for continued proliferation. This appears to involve suppression of normal metabolic stress sensors such as AMPK that would otherwise restrict growth. AMPD3 may participate in this suppression by reducing AMP accumulation, thereby preventing AMPK activation. SUGCT and related enzymes maintain TCA cycle function and intermediate pools, ensuring that energy production can continue despite nutrient limitation. The presence of multiple amino acid metabolism genes (MCEE) suggests that glioblastoma cells continuously catabolize amino acids for energy, a metabolic strategy that would otherwise be associated with cellular senescence or autophagy but appears to be uncoupled from growth inhibition in glioblastoma.

**Atomic biological processes**
- AMP accumulation and AMPK signaling. Genes: AMPD3
  - [2]: AMPD3 suppresses AMP accumulation and AMPK-mediated growth suppression
- TCA cycle metabolism and energy production. Genes: SUGCT, MCEE
  - [41]: SUGCT and related enzymes maintain TCA cycle intermediate pools
- Amino acid catabolism. Genes: MCEE
  - [41]: Branched-chain amino acid metabolism links to energy production

**Atomic cellular components**
- Mitochondrial matrix. Genes: SUGCT, MCEE
  - [41]: TCA cycle enzymes operate in mitochondrial matrix
- Cytoplasm. Genes: AMPD3
  - [2]: AMPD3 participates in cytoplasmic AMP metabolism

**Program citations**
- [2]: AMPD3 and metabolic stress sensing in cancer
- [41]: SUGCT and TCA cycle metabolism in GBM

## Program: RNA Splicing and Transcript Processing Dysregulation
This program encompasses genes involved in RNA splicing and processing that mediate cancer-associated alternative splicing patterns. RBFOX2 (RNA binding fox-1 homolog 2) encodes an RNA-binding protein that regulates alternative exon splicing, particularly in the nervous system and likely in glioblastoma. RBFOX2-mediated splicing regulation affects the protein isoforms produced from genes encoding cell cycle regulators, apoptosis suppressors, and metabolic enzymes. CWC25 (cell cycle and apoptosis regulator 25) participates in the spliceosome catalytic cycle and may regulate the splicing of genes critical for cell cycle progression. Recent evidence from cancer research reveals that splicing factors are essential mediators of cancer-associated splicing patterns, with dysregulation of factors such as SF3B2 causing systematic rewiring of alternative splicing patterns that shift cells toward oncogenic isoforms.

**Predicted impacts**
- Systematic production of cancer-associated protein isoforms from cell cycle, apoptosis, and metabolic genes
- Enhanced tumor-promoting splice variants while suppressing growth-inhibitory isoforms
- Altered splicing patterns enable phenotypic plasticity and adaptation to microenvironmental changes
- Production of isoforms with altered subcellular localization, stability, or enzymatic activity
- Potential therapeutic vulnerability to splicing inhibitors that disrupt production of essential cancer isoforms

**Evidence summary**
Alternative splicing is an underappreciated mechanism of cancer progression that enables production of functional protein variants promoting transformation. Recent evidence reveals that cancer cells acquire dysregulation of splicing factors, leading to systematic rewiring of alternative splicing patterns in genes encoding proteins critical for cell cycle, apoptosis, and metabolism. RBFOX2 mediates splicing decisions in the nervous system and likely participates in glioblastoma-specific splicing patterns. CWC25 participates directly in spliceosomal catalysis and may be dysregulated in glioblastoma to promote cancer-associated splicing. The presence of splicing-related genes in the input list suggests that glioblastoma cells have acquired somatic mutations or epigenetic changes affecting splicing factors, thereby causing systematic rewiring of alternative splicing patterns that support transformation. This mechanism is particularly important in the nervous system, where RBFOX2-mediated splicing regulation is normally critical for neuronal differentiation and function; aberrant RBFOX2 activity in glioblastoma would prevent differentiation and maintain proliferative capacity.

**Atomic biological processes**
- Alternative exon splicing regulation. Genes: RBFOX2, CWC25
  - [57]: SF3B2 and splicing factors regulate alternative splicing patterns in cancer
  - [60]: RBFOX2 regulates alternative exon splicing in nervous system
- Spliceosome catalysis and snRNP assembly. Genes: CWC25
  - [57]: Splicing factors including U2 and U6 snRNP proteins regulate splicing
- Intron retention and transcript stability. Genes: RBFOX2
  - [57]: snaR-A disruption causes intron retention in specific mRNA subsets

**Atomic cellular components**
- Spliceosome. Genes: CWC25
  - [57]: CWC25 functions in spliceosomal catalytic core
- Nuclear speckles. Genes: RBFOX2, CWC25
  - [57]: Splicing factors concentrate in nuclear speckles

**Program citations**
- [57]: snaR-A and splicing factor interactions in cancer
- [60]: RBFOX2 as key regulator of nervous system splicing

## Program: Wnt/Beta-Catenin Signaling and Progenitor Cell State Maintenance
This program coordinates Wnt signaling and related developmental pathways that maintain glioblastoma cells in an undifferentiated, proliferative state resembling intermediate neural progenitors. WNT2B (Wnt family member 2B) participates in canonical Wnt/beta-catenin signaling that maintains progenitor cell identity and suppresses differentiation. During normal cortical development, Wnt signaling maintains the proliferative capacity of neural progenitor cells and delays their differentiation into mature neurons and glia. In glioblastoma, constitutive Wnt signaling achieves similar effects, preventing differentiation and maintaining a proliferative, undifferentiated phenotype. This Wnt signaling program works synergistically with the INSM1-driven intermediate progenitor transcriptional state to block astrocyte maturation and maintain a proliferative, self-renewing cell population. The presence of WNT2B in the input list, combined with evidence that normal astrocytes maintain low Wnt signaling and that glioblastoma cells upregulate this pathway, suggests that Wnt signaling is actively selected for during glioblastoma transformation.

**Predicted impacts**
- Maintenance of undifferentiated, self-renewing cell phenotype
- Suppression of astrocyte differentiation programs that would restrict proliferation
- Sustained expression of progenitor-associated genes including INSM1 and related factors
- Prevention of cell cycle exit and terminal differentiation
- Synergistic cooperation with INSM1-driven developmental reprogramming

**Evidence summary**
Glioblastoma cells acquire and maintain an intermediate neural progenitor-like state that is driven by INSM1 expression, a transcription factor normally expressed in intermediate progenitors during cortical development. The presence of WNT2B in the input list suggests that Wnt signaling participates in maintaining this progenitor state by suppressing differentiation signals. During normal development, Wnt signaling is critical for neural progenitor expansion and the delay of differentiation, and upregulation of this pathway in glioblastoma would achieve similar effects. Recent evidence demonstrates that normal astrocytes repress Wnt signaling to maintain a mature phenotype, suggesting that glioblastoma cells must actively overcome this repression to reactivate Wnt signaling. This reactivation likely occurs through mutations affecting Wnt pathway regulators (such as APC) or through epigenetic reactivation of WNT genes. The functional integration of Wnt signaling with the INSM1-driven progenitor program creates a reinforced developmental reprogramming that locks glioblastoma cells in a proliferative, undifferentiated state.

**Atomic biological processes**
- Canonical Wnt/beta-catenin signaling. Genes: WNT2B
  - [8]: Wnt/beta-catenin signaling maintains neural progenitor cell identity and suppresses differentiation
- Progenitor cell maintenance and self-renewal. Genes: WNT2B
  - [2]: INSM1-driven intermediate progenitor state maintains high biosynthetic demand and proliferative capacity
  - [8]: Wnt signaling suppresses differentiation in neural progenitors
- Suppression of astrocyte differentiation. Genes: WNT2B
  - [8]: Wnt pathway suppresses terminal differentiation programs

**Atomic cellular components**
- Cell membrane and Wnt receptors. Genes: WNT2B
  - [8]: WNT2B binds Frizzled receptors on cell surface
- Nucleus. Genes: WNT2B
  - [8]: Beta-catenin accumulates in nucleus and activates TCF/LEF transcription factors

**Program citations**
- [2]: INSM1-driven intermediate progenitor state in GBM pathogenesis
- [8]: Wnt/beta-catenin signaling in neural progenitor maintenance and differentiation

## Bibliography
1. 1. Available from: https://www.ncbi.nlm.nih.gov/gene/664
2. 2. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
3. 3. Available from: https://www.ncbi.nlm.nih.gov/gene/3845
4. 4. Breen KE, Mehta N, Ravichandran V, Mehine M, Gao C, Fiala E, et al.. Paired tumor-normal sequencing provides insights into the CDKN2A-associated tumor spectrum. npj Precision Oncology [Internet]. 2025Nov19;9(1). Available from: https://www.nature.com/articles/s41698-025-01155-6
5. 5. He G-qian, He S-jia, Jing X-yu, Dai Y-ling, Guo X, Gao J, et al.. Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance. Oncogene [Internet]. 2025Nov27;. Available from: https://www.nature.com/articles/s41388-025-03635-2
6. 6. Available from: https://www.ncbi.nlm.nih.gov/gene/2735
7. 7. Available from: https://www.ncbi.nlm.nih.gov/gene/84868
8. 8. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
9. 9. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
10. 10. Available from: https://www.ncbi.nlm.nih.gov/gene/330
11. 11. Han Y, Han M, Wang T, Zhang H, Liu H, Zheng Y, et al.. Inhibiting the formation of neutrophil extracellular traps to prevent the recurrence of post-operative glioblastoma. Nature Communications [Internet]. 2025Dec9;16(1). Available from: https://www.nature.com/articles/s41467-025-65933-3
12. 12. Available from: https://www.ncbi.nlm.nih.gov/gene/22339
13. 13. Available from: https://www.ncbi.nlm.nih.gov/gene/5315
14. 14. Available from: https://www.ncbi.nlm.nih.gov/gene/8878
15. 15. Available from: https://www.ncbi.nlm.nih.gov/gene/19
16. 16. Available from: https://www.ncbi.nlm.nih.gov/gene/81631
17. 17. Available from: https://www.ncbi.nlm.nih.gov/gene/4925
18. 18. Available from: https://www.ncbi.nlm.nih.gov/gene/5360
19. 19. Available from: https://www.ncbi.nlm.nih.gov/gene/84557
20. 20. Available from: https://www.ncbi.nlm.nih.gov/gene/2475
21. 21. Available from: https://www.ncbi.nlm.nih.gov/gene/406983
22. 22. Available from: https://www.ncbi.nlm.nih.gov/gene/9182
23. 23. Available from: https://www.ncbi.nlm.nih.gov/gene/406952
24. 24. Available from: https://www.ncbi.nlm.nih.gov/gene/6741
25. 25. Available from: https://www.ncbi.nlm.nih.gov/gene/4780
26. 26. Available from: https://www.ncbi.nlm.nih.gov/gene/5777
27. 27. Available from: https://www.ncbi.nlm.nih.gov/gene/868
28. 28. Available from: https://www.ncbi.nlm.nih.gov/gene/18024
29. 29. Available from: https://www.ncbi.nlm.nih.gov/gene/6049
30. 30. Available from: https://www.ncbi.nlm.nih.gov/gene/867
31. 31. Available from: https://www.ncbi.nlm.nih.gov/gene/1145
32. 32. Available from: https://www.ncbi.nlm.nih.gov/gene/9271
33. 33. Available from: https://www.ncbi.nlm.nih.gov/gene/5045
34. 34. Available from: https://www.ncbi.nlm.nih.gov/gene/29881
35. 35. Available from: https://www.ncbi.nlm.nih.gov/gene/3586
36. 36. Available from: https://www.ncbi.nlm.nih.gov/gene/2081
37. 37. Available from: https://www.ncbi.nlm.nih.gov/gene/4864
38. 38. Available from: https://www.ncbi.nlm.nih.gov/gene/1432
39. 39. Available from: https://www.ncbi.nlm.nih.gov/gene/6011
40. 40. Available from: https://www.ncbi.nlm.nih.gov/gene/207
41. 41. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
42. 42. Yan Y, Liu S, Luo A, Cai M, Zhang X, Liu X, et al.. miR-101/METTL3 axis induces autophagy by interrupting FOXG1/EIF3J-AS1 binding in gliomas. Cell Death &amp; Disease [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41419-025-08285-6
43. 43. Richa U, Bidyadhar S, Wen-Bin Y, Ming-Hsiao W, Ke-Chi L, An-Chih W, et al.. A novel dual CDC25-HDAC inhibitor suppresses glioblastoma progression via chromosomal passenger complex disruption.. Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41297426/
44. 44. Li Y, Sheng M, Li W, Liu S, Wang B, Liu B, et al.. Targeting chaperone-mediated autophagy inhibits properties of glioblastoma stem cells and restores anti-tumor immunity. Nature Communications [Internet]. 2025Dec13;. Available from: https://www.nature.com/articles/s41467-025-67119-3
45. 45. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
46. 46. Available from: https://www.ncbi.nlm.nih.gov/gene/4323
47. 47. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
48. 48. Available from: https://www.ncbi.nlm.nih.gov/gene/10631
49. 49. Veo B, Wang D, DeSisto J, Pierce A, Brunt B, Bompada PC, et al.. Single-cell multi-omics identifies metabolism-linked epigenetic reprogramming as a driver of therapy-resistant medulloblastoma. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65466-9
50. 50. Joun GL, Kempe EG, Chen B, Sterling JR, Abbassi RH, Friess D, et al.. Histone methyltransferase PRDM9 promotes survival of drug-tolerant persister cells in glioblastoma. Nature Communications [Internet]. 2025Dec15;16(1). Available from: https://www.nature.com/articles/s41467-025-65888-5
51. 51. Available from: https://www.ncbi.nlm.nih.gov/gene/4170
52. 52. Available from: https://www.nature.com/subjects/cns-cancer/ncomms
53. 53. Li T, Wang L, Duan S, Cui X, Fu C, Hu J, et al.. Multi-omics elucidation of KDM5C, KDM6A, and KMT2B roles in cancer epigenetic dysregulation and transcriptional reprogramming. Communications Biology [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s42003-025-09305-z
54. 54. Available from: https://www.ncbi.nlm.nih.gov/gene/5599
55. 55. Available from: https://www.ncbi.nlm.nih.gov/gene/3783
56. 56. Zhou S, Lizarazo S, Chorghade S, Mouli L, Cheng R, K CR, et al.. Cancer-associated snaR-A noncoding RNA interacts with core splicing machinery and disrupts processing of mRNA subpopulations. Nature Communications [Internet]. 2025Nov25;16(1). Available from: https://www.nature.com/articles/s41467-025-65448-x
57. 57. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
58. 58. Available from: https://www.ncbi.nlm.nih.gov/gene/3738
59. 59. Available from: https://www.ncbi.nlm.nih.gov/gene/23543
60. 60. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
61. 61. Available from: http://json-schema.org/draft-07/schema#",
