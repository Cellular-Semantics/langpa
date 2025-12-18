# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma
- Tissue: Brain

## Input Genes
CFI, SNTG1, PLEKHG1, PRKD1, ETV6, ADAMTS14, SCN1A, EPHA3, SLC1A2, ADCY2, COL8A1, TNIK, LINC01993, TPST1, STOX1, GLI3, GRIA1, GRIK3, GRIN2B, HS3ST3B1, KLHDC8A, LINC00511, LINC01122, IFI16, ILDR2, ... (200 total)

## Program: Synaptic Interface Disruption
Dysregulation of glutamatergic synaptic transmission machinery, including altered expression of ionotropic glutamate receptors, synaptic adhesion molecules, and axon guidance cues. This program reflects remodeling of neuron-astrocyte communication pathways from neuroprotective partnerships toward tumor-promoting interactions. Key components include altered glutamate receptor subunit composition (AMPA, kainate, NMDA types), trans-synaptic adhesion molecule dysregulation (neurexins, neuroligins), and disrupted axon guidance signaling (semaphorins, repulsive guidance molecules).

**Predicted impacts**
- Enhanced peritumoral neuronal excitability through altered glutamatergic receptor expression patterns
- Loss of neuroprotective glutamate buffering through reduced astrocytic glutamate transporter function
- Aberrant neuron-tumor synaptic contacts promoting tumor cell migration and proliferation
- Reorientation of axonal projections toward tumor mass via altered semaphorin signaling
- Contribution to tumor-associated seizures through disrupted glutamatergic transmission control

**Evidence summary**
Multiple independent studies demonstrate that gliomas alter peritumoral neural circuits through remodeling of glutamatergic transmission (source 17), with chronic alterations in astrocytic expression of both glutamatergic proteins and synaptic organization molecules (source 14). The presence of ionotropic glutamate receptor subunits, trans-synaptic adhesion molecules, and axon guidance cues in the input gene list indicates coordinated dysregulation of multiple synaptic system components. In normal astrocytes, these genes support glutamate homeostasis and beneficial neuron-astrocyte partnerships; dysregulation would simultaneously compromise neuroprotection and enable aberrant tumor-neuron communication.

**Atomic biological processes**
- Glutamatergic synaptic transmission. Genes: GRIA1, GRIK3, GRIN2B
  - [5]: GRIN1 and GRIN2B encode NMDA receptor subunits with roles in synaptic transmission and cortical development
  - [14]: Reduced Gria2 expression in chronic TBI astrocytes indicates altered glutamatergic signaling capacity
  - [17]: Aberrant neural activity in peritumoral cortex involves altered glutamatergic transmission through neuron-tumor crosstalk
- Trans-synaptic adhesion and synapse organization. Genes: NRXN3, NRCAM, NLGN4X, LRRTM3, LRRC4C
  - [36]: Neurexins and neuroligins organize glutamatergic synapses through trans-synaptic binding; human OPCs internalize synaptic structures via GAS6-AXL signaling
  - [14]: Synaptic and cellular communication genes (Kirrel3, Farp1, Syn3, S1pr1) are downregulated in chronic TBI astrocytes
- Axon guidance and neuronal projection orientation. Genes: SEMA3A, SEMA3E, RGMA
  - [53]: Semaphorin and netrin signaling alter axon guidance and neurite development in the developing and diseased nervous system
  - [17]: Peritumoral neurons show altered projections and electrophysiological properties due to glioma-induced microenvironment changes

**Atomic cellular components**
- AMPA receptor complex. Genes: GRIA1
  - [5]: GRIA1 encodes AMPA receptor GluA1 subunit critical for synaptic plasticity
- Kainate receptor complex. Genes: GRIK3
  - [5]: GRIK3 encodes kainate receptor subunit with developmental and synaptic roles
- NMDA receptor complex. Genes: GRIN2B
  - [5]: GRIN2B encodes NMDA receptor NR2B subunit with roles in synaptic plasticity and development

**Required genes (not in input)**
- Genes: SLC1A2, GLUL, GRIN1
  - [14]: SLC1A2 (EAAT2) glutamate transporter dysregulation impairs glutamate clearance in astrocytes
  - [32]: SLC1A2 encodes critical astrocytic glutamate transporter
  - [5]: GRIN1 encodes essential NMDA receptor NR1 subunit

**Program citations**
- [5]: Defines NMDA receptor subunit roles in neural development and synaptic function
- [14]: Demonstrates downregulation of synaptic and glutamatergic genes in chronic TBI astrocytes, paralleling disease-induced astrocyte dysfunction
- [17]: Shows neuron-tumor crosstalk mechanisms affecting glutamatergic transmission in peritumoral regions
- [36]: Characterizes trans-synaptic adhesion molecule functions in synapse organization
- [53]: Describes semaphorin and netrin signaling in axon guidance and neuronal circuit development

## Program: Cell Adhesion Plasticity
Coordinated dysregulation of classical cadherins, catenins, and immunoglobulin superfamily cell adhesion molecules that collectively enable loss of contact inhibition while maintaining sufficient adhesive capacity for collective tumor invasion. This program reflects the dual requirement of transformed astrocytes to escape growth inhibitory cell-cell contacts while retaining sufficient adhesion for coherent migration and tumor formation.

**Predicted impacts**
- Loss of contact-dependent growth inhibition through reduced N-cadherin-mediated adhesion
- Enhanced individual cell motility despite maintained tumor cell aggregation
- Selective adhesion to stromal components and endothelium while reduced homotypic repulsion
- Epithelial-mesenchymal transition-like plasticity enabling collective invasion
- Altered cell fate decisions due to reduced intercellular contact signaling

**Evidence summary**
Cadherin dysregulation is well-established in glioblastoma, with mesenchymal subtypes showing altered adhesion molecule expression (source 44). Loss of CADM1, a known tumor suppressor, would enhance invasiveness (source 36). The combination of reduced classical cadherin function (enabling migration) with maintained IgSF interactions (enabling selective adhesion) creates a dynamically plastic adhesive phenotype. This selective dysregulation enables transformation from contact-inhibited astrocytes to invasive tumor cells while maintaining sufficient cell-cell contact for collective tumor behavior.

**Atomic biological processes**
- Classical cadherin-mediated cell-cell adhesion. Genes: CDH2, CTNNA3
  - [68]: N-cadherin and associated catenins form adherens junctions critical for tissue organization and contact inhibition
  - [44]: Cadherin dysregulation is characteristic of mesenchymal glioblastoma subtypes with enhanced invasiveness
- Protocadherin-mediated cell recognition and specificity. Genes: PCDH9
  - [45]: Protocadherins provide cell recognition diversity and adhesion specificity in neural tissues
- Immunoglobulin superfamily adhesion. Genes: CADM1, NTM, NLGN4X
  - [36]: IgSF CAMs including CADM1 and NTM regulate neuronal circuit organization and astrocyte interactions

**Atomic cellular components**
- Adherens junction complex. Genes: CDH2, CTNNA3
  - [68]: N-cadherin links to actin cytoskeleton through alpha- and beta-catenins to form adherens junctions
- Cell-cell adhesion molecules. Genes: PCDH9, CADM1, NTM, NLGN4X
  - [36]: Diverse IgSF members and classic cadherins form trans-cellular adhesive interfaces

**Required genes (not in input)**
- Genes: CTNNB1, CDH1, NCAM1
  - [68]: Beta-catenin and E-cadherin are critical components of adherens junctions often dysregulated in epithelial cancers
  - [36]: NCAM1 represents another key neural CAM often altered in glioma

**Program citations**
- [36]: Comprehensive analysis of IgSF adhesion molecules in neural development and cancer
- [44]: Identifies adhesion molecule dysregulation in mesenchymal glioblastoma subtypes
- [45]: Describes role of ECM components and adhesion molecules in neural tissues and glioma
- [68]: Defines BBB and neural tissue organization through cell adhesion molecules

## Program: Cytoskeletal Reorganization and Enhanced Motility
Coordinated dysregulation of actin-myosin machinery, focal adhesion components, and planar polarity effectors that reorient the cytoskeleton from a static, neuron-support configuration toward a dynamic, migratory phenotype. This program encompasses myosin motor proteins, kinase regulators of actin dynamics, and adhesion site remodeling components.

**Predicted impacts**
- Enhanced cell migration speed and directional persistence
- Increased invasiveness through 3D ECM and along white matter tracts
- Altered morphodynamics enabling tumor cells to navigate narrow tissue spaces
- Increased actomyosin contractility driving mechanical force generation
- Disrupted contact inhibition through impaired focal adhesion signaling

**Evidence summary**
The extensive representation of myosin isoforms, actin regulators, and focal adhesion components indicates coordinated reorientation of the cytoskeleton in astrocytoma. Normal astrocytes maintain relatively stationary morphology optimized for neuronal support; transformation requires dynamic cytoskeletal reorganization. The presence of multiple myosin isoforms (MYO5B for trafficking, MYO1E for membrane dynamics, MYO16 for actin organization, MYO3B for specialized functions) suggests both enhanced force generation and altered vesicular trafficking. Combined with focal adhesion remodeling genes, this program predicts a fundamental shift toward migratory phenotype characteristic of infiltrative tumors.

**Atomic biological processes**
- Actin polymerization and actomyosin contraction. Genes: PRKD1, PRICKLE2, DTNA
  - [6]: PRKD1 regulates actin bundling and contractility through phosphorylation of MARCKS and related proteins
  - [27]: SUCLG2 knockdown affects mitochondrial oxidative phosphorylation, which couples to actin dynamics
- Myosin motor-mediated force generation and trafficking. Genes: MYO5B, MYO1E, MYO16, MYO3B
  - [27]: Motor protein dysfunction affects cellular transport and energy metabolism
- Focal adhesion remodeling and dynamics. Genes: PARD3, PARD3B, PDLIM5
  - [68]: PARD3 organizes cell polarity complexes and adhesion sites critical for cell migration control
- Planar cell polarity and directional migration. Genes: PRICKLE2
  - [68]: PRICKLE2 participates in planar polarity signaling affecting cell orientation and migration

**Atomic cellular components**
- Actin filaments and myosin motor complexes. Genes: MYO5B, MYO1E, MYO16, MYO3B, PRKD1
  - [27]: Mitochondrial metabolism couples to actin dynamics through ATP availability for myosin ATPase
- Focal adhesions. Genes: PARD3, PARD3B, PDLIM5
  - [68]: PAR polarity complexes organize focal adhesions at cell-ECM interface
- Planar polarity complexes. Genes: PRICKLE2
  - [68]: PRICKLE proteins participate in non-canonical Wnt signaling and cell orientation

**Required genes (not in input)**
- Genes: RHOA, RAC1, CDC42, ROCK1
  - [28]: ILK silencing inhibits glioblastoma migration through ROCK1 and Fascin-1 downregulation, indicating Rho GTPase pathway involvement

**Program citations**
- [6]: Demonstrates PRKD1 role in actin regulation and cell migration
- [27]: Links metabolic state to cytoskeletal dynamics through energy coupling
- [68]: Comprehensive analysis of cell polarity and migration control in 3D tissue models

## Program: Extracellular Matrix Remodeling
Dysregulation of matrix proteases, ECM protein synthesis, and ECM-modifying enzymes that collectively enable transformation of a neuron-supportive ECM into a tumor-permissive niche. This program involves matrix metalloproteinases, heparan sulfate modifiers, and structural ECM components that construct pro-tumoral matrix architecture.

**Predicted impacts**
- Enhanced degradation of inhibitory ECM components constraining tumor growth
- Construction of pro-tumoral matrix architecture supporting angiogenesis and invasion
- Increased growth factor bioavailability through heparan sulfate modification
- Altered ECM-integrin signaling promoting tumor cell proliferation and migration
- Remodeled basement membranes facilitating vascular invasion and perivascular niche formation

**Evidence summary**
Glioblastoma progression critically depends on ECM remodeling, with both enhanced protease activity and altered ECM composition characterizing tumors (sources 26, 27, 45). The input gene list captures multiple layers of this remodeling: ADAMTS proteases for enzymatic degradation, heparan sulfate modifiers (HS3ST3B1, SULF1) for altered growth factor signaling capacity, and structural collagen genes for ECM construction. The presence of both proteases (ADAMTS) and their counterregulatory genes (SULF1 against HS3ST) suggests dynamic, carefully regulated ECM remodeling rather than simple dysregulation. Dysregulation would create permissive microenvironment supporting tumor cell proliferation, migration, and angiogenesis while reducing normal ECM constraints.

**Atomic biological processes**
- Extracellular matrix protein degradation. Genes: ADAMTS6, ADAMTS14, ADAMTS9-AS2
  - [26]: GLUL drives angiogenesis and vascular niche formation through PI3K/AKT signaling involving ECM remodeling
  - [27]: SUCLG2 knockdown affects proteasomal degradation and cellular proteostasis related to ECM proteins
  - [45]: Spatial transcriptomics reveal differential ECM expression in GBM tumor regions
- Heparan sulfate biosynthesis and modification. Genes: HS3ST3B1, SULF1, NDST3
  - [45]: ECM components including heparan sulfate proteoglycans regulate GBM progression
- Structural ECM protein synthesis and organization. Genes: COL8A1
  - [45]: Collagen and other structural ECM proteins are differentially expressed in GBM tumor regions

**Atomic cellular components**
- Matrix metalloproteinase complexes. Genes: ADAMTS6, ADAMTS14, ADAMTS9-AS2
  - [27]: Matrix metalloproteinases regulate proteolytic degradation of ECM and cytoplasmic proteins
- Heparan sulfate proteoglycans. Genes: HS3ST3B1, SULF1, NDST3
  - [45]: Heparan sulfate modifications regulate growth factor signaling and cell-ECM interactions
- Basement membrane and stromal collagens. Genes: COL8A1
  - [45]: Collagen VIII and other collagens form structural ECM framework

**Required genes (not in input)**
- Genes: MMP2, MMP9, MMP14, TIMP3
  - [12]: TIMP3 modulates ECM remodeling during development and disease

**Program citations**
- [26]: Demonstrates GLUL's role in glioma angiogenesis through PI3K/AKT-dependent ECM remodeling
- [27]: Shows proteolytic and metabolic coupling in glioblastoma through SUCLG2
- [45]: Single-cell spatial transcriptomics reveal ECM expression patterns in GBM tumor microenvironment

## Program: Transcriptional Reprogramming
Dysregulation of transcription factors and regulatory non-coding RNAs that redefine the astrocytoma transcriptome from a differentiation-dominated state toward one supporting stemness, proliferation, and tumor-promoting properties. This program involves transcription factors controlling neural development (GLI3, ETV1, ETV6), regulatory non-coding RNAs (SOX2-OT, lncRNAs), and chromatin remodeling factors.

**Predicted impacts**
- Loss of astrocyte-specific differentiation gene expression (GFAP, ALDH1A1, etc.)
- Activation of neural progenitor and stemness-associated genes
- Enhanced proliferation through altered cell cycle checkpoint regulation
- Altered chromatin accessibility at oncogenic and tumor-suppressor loci
- Dysregulated expression of metabolic enzymes supporting malignant phenotype
- Maintained or increased expression of stemness factors preventing terminal differentiation

**Evidence summary**
The comprehensive representation of transcription factors and regulatory RNAs indicates fundamental reprogramming of the astrocytoma transcriptome. GLI3 reactivation would dysregulate hedgehog pathway targets (source 25); ETV family factors control developmental processes often dysregulated in cancer; SOX2-associated regulatory networks maintain stemness incompatible with normal astrocyte differentiation (source 40). The presence of multiple lncRNAs suggests layered transcriptional control through both classical transcription factors and post-transcriptional mechanisms (sources 40, 46). Collectively, these factors would repress differentiation-associated astrocyte genes while activating oncogenic and stemness-associated programs. This transcriptional remodeling represents a fundamental reprogramming from differentiated astrocyte identity toward a progenitor-like, tumor-promoting state.

**Atomic biological processes**
- Transcriptional regulation of neural development and cell fate. Genes: GLI3, ETV1, ETV6, RFX4, SOX2-OT
  - [25]: GLI1 and related factors regulate glioma cell differentiation and tumor progression
  - [40]: SOX2 and related transcription factors control stem cell identity and neural progenitor specification
- Chromatin remodeling and histone modification. Genes: SETBP1, ARID5B, PRDM16
  - [23]: SETBP1 regulates histone deacetylase activity and chromatin accessibility
  - [40]: ARID5B and PRDM16 participate in chromatin remodeling affecting cell differentiation
- Post-transcriptional and epigenetic regulation via lncRNAs. Genes: SOX2-OT, LINC01993, LINC00511, LINC01122, NR2F2-AS1, SOCS2-AS1, SCN1A-AS1
  - [40]: SOX2-OT and related long non-coding RNAs regulate expression of associated protein-coding genes
  - [46]: Alternative splicing and lncRNA-mediated regulation influence neural development and disease

**Atomic cellular components**
- Transcription factor complexes. Genes: GLI3, ETV1, ETV6, RFX4
  - [25]: GLI family transcription factors form regulatory complexes controlling gene expression
  - [40]: Multiple transcription factors coordinate neural differentiation programs
- Chromatin remodeling complexes. Genes: ARID5B, PRDM16
  - [40]: ARID5B and related factors participate in SWI/SNF-like chromatin remodeling complexes
- Regulatory non-coding RNA molecules. Genes: SOX2-OT, LINC01993, LINC00511, LINC01122, NR2F2-AS1, SOCS2-AS1, SCN1A-AS1
  - [40]: Long non-coding RNAs regulate gene expression through multiple mechanisms
  - [46]: lncRNAs participate in alternative splicing and chromatin regulation

**Required genes (not in input)**
- Genes: SOX2, OLIG2, NF1, TP53
  - [40]: SOX2 encodes critical transcription factor for stem cell and neural progenitor maintenance
  - [10]: TP53 tumor suppressor frequently dysregulated in gliomas

**Program citations**
- [23]: SETBP1 drives chromatin remodeling in myelodysplastic syndrome through altered histone deacetylase activity
- [25]: GLI1 participates in hypoxia-induced glioma progression
- [40]: Transcriptome analysis reveals SOX2 expression and stemness-associated gene programs
- [46]: Alternative splicing and lncRNA regulation affect neural development

## Program: Metabolic Reprogramming
Dysregulation of metabolic enzymes supporting lipid synthesis, fatty acid oxidation, and nucleotide metabolism that collectively support the biosynthetic demands of rapidly proliferating astrocytoma cells. This program reflects transformation from a metabolic state optimized for neuronal support toward one maximizing biosynthetic capacity for rapid cell division.

**Predicted impacts**
- Enhanced ATP production supporting rapid cell division
- Increased lipid synthesis for membranogenesis during tumor growth
- Altered metabolic competition with adjacent neurons
- Potential Warburg effect-like glycolytic switching supporting tumor progression
- Enhanced nucleotide synthesis enabling rapid DNA replication
- Altered oxidative stress biology through changes in mitochondrial metabolism

**Evidence summary**
Metabolic reprogramming is a hallmark of glioblastoma progression, with tumor cells exhibiting altered oxidative and glycolytic metabolism (sources 27, 30). The input gene list captures components of fatty acid synthesis (ACSBG1, ACSS3), lipid signaling (multiple PLC isoforms), and mitochondrial metabolism (MT-encoded genes). Normal astrocytes prioritize oxidative metabolism supporting neuronal energy demands; transformed astrocytes would reprogram toward biosynthetic metabolism supporting rapid cell division. The presence of multiple lipid metabolism genes indicates coordinated dysregulation across lipid synthesis and signaling pathways. These changes would provide the biosynthetic capacity required for tumor growth while potentially contributing to metabolic competition with adjacent neurons.

**Atomic biological processes**
- Fatty acid and lipid biosynthesis. Genes: ACSBG1, ACSS3, PLS3, PLPP4, PLCH1, PLCG2, PLCE1, PLCB4
  - [27]: SUCLG2 couples mitochondrial metabolism to lipid synthesis and cell proliferation
  - [31]: Mallotumide A targets lipid metabolism enzymes ACC1 and FASN in cancer cells
- Mitochondrial oxidative phosphorylation and energy metabolism. Genes: MT-CYB, MT-CO2, MT-CO3, MCUB
  - [27]: SUCLG2 regulates mitochondrial oxidative phosphorylation critical for proliferation
  - [30]: Caveolin-2 expressing nerves shift cancer cell metabolism toward oxidative phosphorylation
- Nucleotide and polyamine synthesis. Genes: PGM2L1, PGM5
  - [31]: Cancer cells activate metabolic pathways supporting nucleotide synthesis for DNA replication

**Atomic cellular components**
- Fatty acid synthesis complexes. Genes: ACSBG1, ACSS3
  - [31]: ACC and FASN enzymes catalyze de novo lipogenesis essential for rapid cell division
- Phospholipid and lipid signaling molecules. Genes: PLS3, PLPP4, PLCH1, PLCG2, PLCE1, PLCB4
  - [31]: Phospholipids and signaling lipids participate in cancer cell proliferation and survival
- Mitochondrial complexes and energy production. Genes: MT-CYB, MT-CO2, MT-CO3, MCUB
  - [27]: Mitochondrial electron transport chain components including cytochrome b and oxidases

**Required genes (not in input)**
- Genes: PKM2, LDHA, HK2, GLUL
  - [26]: GLUL participates in glutamate and energy metabolism in transformed astrocytes

**Program citations**
- [27]: SUCLG2 couples mitochondrial metabolism to cancer cell proliferation and metabolic remodeling
- [30]: Tumor-associated nerves promote metabolic reprogramming toward mitochondrial oxidative phosphorylation
- [31]: Mallotumide A targets cancer cell metabolic enzymes including those of lipid synthesis

## Program: Ion Channel and Electrophysiological Remodeling
Dysregulation of voltage-gated ion channels that alters the electrophysiological properties of transformed astrocytes from relatively non-excitable cells toward more excitable phenotypes capable of active electrical signaling. This program encompasses sodium channels, potassium channels, and associated regulatory proteins.

**Predicted impacts**
- Enhanced intrinsic excitability of transformed astrocytes
- Potential generation of ectopic electrical activity influencing peritumoral neural circuits
- Altered membrane potential dynamics affecting ion-dependent signaling
- Increased responsiveness to synaptic inputs from adjacent neurons
- Potential contribution to tumor-associated seizures through altered network-level excitability

**Evidence summary**
While direct evidence for ion channel dysregulation driving astrocytoma progression is less extensive than for other programs, the presence of SCN1A and KCND3 in the input gene list suggests altered electrophysiology is characteristic of astrocytic transformation. Normal mature astrocytes are largely non-excitable; acquisition of sodium channel expression would render them capable of active electrical signaling. The altered electrical properties could influence peritumoral neural circuits through direct synaptic transmission and network-level effects (source 17). Ion channel remodeling represents an emerging but potentially important aspect of tumor-neuron crosstalk.

**Atomic biological processes**
- Voltage-gated sodium channel function and action potential generation. Genes: SCN1A, SCN1A-AS1
  - [5]: SCN1A encodes Nav1.1 sodium channel critical for neuronal excitability and action potentials
- Voltage-gated potassium channel function and excitability control. Genes: KCND3
  - [5]: KCND3 encodes Kv4.3 potassium channel regulating intrinsic excitability and repolarization

**Atomic cellular components**
- Sodium channel complex. Genes: SCN1A
  - [5]: SCN1A forms functional sodium channel necessary for action potential initiation
- Potassium channel complex. Genes: KCND3
  - [5]: KCND3 forms rapidly inactivating A-type potassium channel regulating membrane potential

**Required genes (not in input)**
- Genes: CACNA1C, GRIN1
  - [5]: Calcium channels and NMDA receptors participate in neuronal excitability and calcium signaling

**Program citations**
- [5]: Comprehensive analysis of ion channels in neural development and function
- [17]: Aberrant neural activity in peritumoral cortex contributes to tumor-associated seizures

## Program: DNA Damage Response and Genomic Instability
Dysregulation of DNA repair machinery and cell cycle checkpoint control that permits accumulation of additional genetic mutations while simultaneously maintaining proliferative capacity. This program reflects how astrocytomas acquire multiple secondary mutations beyond initial transformation events, driving tumor heterogeneity and evolution.

**Predicted impacts**
- Impaired DNA damage detection or repair enabling mutation accumulation
- Enhanced chromosomal instability through compromised checkpoint control
- Acquisition of secondary oncogenic mutations during tumor evolution
- Potential resistance to DNA-damaging chemotherapy or radiotherapy
- Increased tumor heterogeneity through enhanced genetic diversity

**Evidence summary**
Astrocytomas and glioblastomas typically harbor multiple mutations beyond initial transformation events, reflecting genomic instability (source 47, 59). The presence of DNA repair (PRKDC, BRCA2) and cell cycle (NEK6) genes indicates dysregulation of genomic stability control. Altered PRKDC expression could impair NHEJ repair, enabling accumulation of DNA damage. This dysregulation would permit secondary mutations driving tumor evolution and heterogeneity while maintaining sufficient proliferative capacity for continued growth. Genomic instability represents a double-edged sword: it promotes tumor heterogeneity and adaptation but also potentially creates vulnerabilities to DNA-targeting therapies.

**Atomic biological processes**
- Double-strand break detection and repair. Genes: PRKDC
  - [35]: PRKDC encodes DNA-PKcs critical for non-homologous end joining DNA repair
  - [65]: DNA-PK participates in DNA damage signaling and genomic instability
- Homologous recombination and DNA repair. Genes: BRCA2
  - [61]: BRCA2 participates in homologous recombination-mediated DNA repair
- Cell cycle progression and mitotic checkpoint. Genes: NEK6
  - [64]: NEK6 regulates cell cycle progression and mitotic fidelity

**Atomic cellular components**
- DNA damage response complex. Genes: PRKDC
  - [35]: DNA-PKcs functions in multi-protein complexes detecting and repairing double-strand breaks
- Homologous recombination machinery. Genes: BRCA2
  - [61]: BRCA2 associates with RAD51 and other recombination proteins
- Cell cycle checkpoint complexes. Genes: NEK6
  - [64]: NEK kinases participate in centrosome maturation and cell cycle control

**Required genes (not in input)**
- Genes: ATM, TP53, CDKN1A, PTEN
  - [10]: TP53 tumor suppressor frequently dysregulated in gliomas including through R175H hotspot mutation

**Program citations**
- [35]: DNA-PKcs role in DNA damage signaling and non-homologous end joining
- [47]: Multi-hit genetic alterations characterize high-grade gliomas
- [61]: BRCA2 participates in homologous recombination DNA repair
- [64]: NEK6 participates in cell cycle regulation and mitotic progression

## Program: Signaling Pathway Integration and Growth Promotion
Dysregulation of phospholipase C, Rho GTPase, and receptor tyrosine kinase signaling pathways that collectively amplify growth and survival signals while reducing growth inhibitory inputs. This program encompasses multiple signaling modalities that converge on central nodes (PI3K-AKT, MAPK) driving tumor progression.

**Predicted impacts**
- Enhanced calcium signaling supporting proliferation and migration
- Amplified PI3K-AKT signaling promoting cell survival and growth
- Increased responsiveness to growth factors through altered receptor expression
- Activated hedgehog pathway supporting stemness and tumor progression
- Enhanced Wnt signaling maintaining stem cell properties
- Increased secretion of growth factors (PTN, PDGFC) promoting autocrine and paracrine signaling

**Evidence summary**
Multiple signaling pathways are dysregulated in glioblastoma, with PI3K-AKT representing a central hub integrating diverse inputs (sources 26, 29). The input gene list captures components of phospholipase C signaling (multiple PLC isoforms), downstream effectors (PREX2, PRKD1, PRKCA), and upstream receptor engagement (NTRK3, PDGFRA, PTN, PDGFC). The presence of both secreted ligands (PTN, PDGFC) and their cognate receptors or downstream effectors suggests both autocrine and paracrine signaling amplification. Dysregulation across multiple pathway modalities (PLC, PI3K-AKT, hedgehog, Wnt) suggests redundant signaling networks that provide robustness and compensatory capacity. Collectively, these changes would create a hyperresponsive state to growth-promoting signals while reducing response to growth-inhibitory inputs.

**Atomic biological processes**
- Phospholipase C-mediated calcium and PKC signaling. Genes: PLCE1, PLCB4, PLCH1, PLCG2
  - [31]: Phospholipase C enzymes cleave phosphatidylinositol bisphosphate generating IP3 and DAG
- PI3K-AKT-mTOR pathway amplification. Genes: PREX2, PRKD1, PRKCA
  - [26]: GLUL-driven CAF activation occurs through PI3K/AKT signaling central to glioma progression
  - [29]: Pericytes orchestrate tumor-restraining microenvironment partially through PI3K signaling
- Receptor tyrosine kinase signaling. Genes: NTRK3, PTN, PDGFC, PDGFRA
  - [47]: NTRK2 fusion genes promote oncogenic signaling in gliomas
  - [30]: Caveolin-2 modulates neuronal signaling affecting cancer cell phenotype
- Hedgehog and Wnt pathway signaling. Genes: GLI3, PTCH2
  - [25]: GLI1 participates in hedgehog pathway-driven glioma progression
  - [51]: RGS20 inhibition enhances WNT/β-catenin signaling in glioma stem cells

**Atomic cellular components**
- Phospholipase C enzyme complexes. Genes: PLCE1, PLCB4, PLCH1, PLCG2
  - [31]: Multiple PLC isoforms generate diverse lipid signaling molecules
- PI3K-AKT-mTOR signaling cascade. Genes: PREX2, PRKD1, PRKCA
  - [26]: PI3K/AKT pathway central hub for integrating multiple growth signals in glioma
- Growth factor receptor complexes. Genes: NTRK3, PDGFRA, PTN, PDGFC
  - [47]: NTRK2 fusion promotes constitutive tyrosine kinase signaling

**Required genes (not in input)**
- Genes: PIK3CA, AKT1, MTOR, PTEN, EGFR, PDGFRA
  - [11]: AKT1 is downstream target of PI3K in controlling angiogenesis and tumor growth
  - [33]: SHH and PI3K pathways synergize in PTEN-deficient glioblastomas

**Program citations**
- [25]: GLI1 participates in hypoxia-induced glioma progression through hedgehog signaling
- [26]: GLUL-driven CAF activation through PI3K/AKT signaling promotes glioma angiogenesis
- [29]: Pericytes regulate tumor microenvironment through multiple signaling pathways
- [30]: Caveolin-2 modulates nerve-mediated effects on cancer cell metabolism and stemness
- [47]: NTRK2 fusion genes in gliomas drive oncogenic signaling
- [51]: RGS20 suppression activates WNT/β-catenin signaling in glioma stem cells

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
2. Available from: https://www.ncbi.nlm.nih.gov/gene/3265
3. Available from: https://www.ncbi.nlm.nih.gov/gene/4916
4. Song BJ, Ge Y, Nicolella A, Kwon MJ, Lodder B, Bonanno K, et al.. Elevated synaptic PKA activity and abnormal striatal dopamine signaling in Akap11 mutant mice, a genetic model of schizophrenia and bipolar disorder. Nature Communications [Internet]. 2025Nov28;16(1). Available from: https://www.nature.com/articles/s41467-025-66504-2
5. Available from: https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=2902
6. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
7. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/12355/
8. Available from: https://www.ncbi.nlm.nih.gov/gene/19211
9. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
10. Available from: https://www.ncbi.nlm.nih.gov/clinvar/variation/VCV000012374
11. Available from: https://www.ncbi.nlm.nih.gov/gene/207
12. Available from: https://www.ncbi.nlm.nih.gov/gene/7078
13. Available from: https://www.ncbi.nlm.nih.gov/gene/4314
14. Available from: https://www.ncbi.nlm.nih.gov/gene/3383
15. Available from: https://www.ncbi.nlm.nih.gov/gene/20674
16. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
17. Available from: https://www.ncbi.nlm.nih.gov/gene/10419
18. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
19. Available from: https://www.ncbi.nlm.nih.gov/gene/12151
20. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
21. Available from: https://www.ncbi.nlm.nih.gov/gene/5725
22. Pera J, Romero-Moya D, Torralba-Sales E, Andersson R, García-Hernández V, Magallon-Mosella M, et al.. Human iPSCs-based modeling unveils SETBP1 as a driver of chromatin rewiring in GATA2 deficiency. Nature Communications [Internet]. 2025Nov17;16(1). Available from: https://www.nature.com/articles/s41467-025-65806-9
23. Available from: https://www.ncbi.nlm.nih.gov/gene/26040
24. Available from: https://www.ncbi.nlm.nih.gov/gene/2735
25. Qing Z, Yida L, Zhi Z, Yang W, Fusheng L. GLUL Confers Perivascular Cancer-Associated Fibroblasts With Pro-Angiogenic Capacity to Promote Glioma Progression.. Advanced science (Weinheim, Baden-Wurttemberg, Germany) [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41355614/
26. Li W, Zhang Q, Yin H, Li Q, Liu S, Wang J, et al.. Knockdown of SUCLG2 inhibits glioblastoma proliferation and promotes apoptosis through LMNA acetylation and the mediation of H4K16la lactylation. Cell Death Discovery [Internet]. 2025Nov17;11(1). Available from: https://www.nature.com/articles/s41420-025-02856-4
27. Available from: https://www.ncbi.nlm.nih.gov/gene/3611
28. Braun S, Bolivar P, Oudenaarden C, Sjölund J, Bocci M, Harbst K, et al.. Pericytes orchestrate a tumor-restraining microenvironment in glioblastoma. Nature Communications [Internet]. 2025Dec4;16(1). Available from: https://www.nature.com/articles/s41467-025-66985-1
29. Zhang Z, Wang C, Sun Z, Shi X, Shuai Y, Wang Y, et al.. CAV2-expressing nerves induce metabolic switch toward mitochondrial oxidative phosphorylation to promote cancer stemness. Nature Communications [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41467-025-66914-2
30. Laowittawat C, Sawektreeratana N, Katewongsa K, Payomhom P, Hongthong S, Reutrakul V, et al.. The cyclic peptide mallotumide A inhibits colon and breast cancer cell growth and motility by targeting cellular respiration and lipogenesis. Scientific Reports [Internet]. 2025Nov19;15(1). Available from: https://www.nature.com/articles/s41598-025-24547-x
31. Available from: https://www.ncbi.nlm.nih.gov/gene/6506
32. Available from: https://www.ncbi.nlm.nih.gov/gene/6469
33. Available from: https://www.ncbi.nlm.nih.gov/gene/5564
34. Available from: https://www.ncbi.nlm.nih.gov/gene/5591
35. Gkogka A, Malwade S, Koskuvi M, Ohtonen S, Molnar E, Bose R, et al.. Human oligodendrocyte progenitor cells mediate synapse elimination through TAM receptor activation. Nature Communications [Internet]. 2025Dec5;16(1). Available from: https://www.nature.com/articles/s41467-025-66521-1
36. Available from: https://www.ncbi.nlm.nih.gov/gene/5292
37. Available from: https://www.ncbi.nlm.nih.gov/gene/140885
38. Available from: https://www.ncbi.nlm.nih.gov/gene/24842
39. Niu R-Z, Xue L-L, Tian X-H, Huangfu L-R, Chen L, Zhai C-Y, et al.. Mid-gestational cell-type-specific transcriptomic signatures in the prefrontal and superior temporal cortex in Down syndrome. Nature Communications [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41467-025-66109-9_reference.pdf
40. Available from: https://www.ncbi.nlm.nih.gov/gene/6777
41. Available from: https://www.ncbi.nlm.nih.gov/gene/100133941
42. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
43. Jacobs HN, Gorissen BL, Guez J, Kanai M, Gupta K, Finucane HK, et al.. Widespread naturally variable human exons aid genetic interpretation. Nature Communications [Internet]. 2025Dec16;. Available from: https://www.nature.com/articles/s41467-025-65476-7
44. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
45. Available from: https://www.ncbi.nlm.nih.gov/gene/7852
46. Available from: https://www.ncbi.nlm.nih.gov/gene/29302
47. Available from: https://www.ncbi.nlm.nih.gov/gene/146713
48. Xie Y, Li Q, Ma Y, Yang Y, Jin X, Yi T, et al.. RGS20 reduces glioma stemness and temozolomide resistance by intrinsically inhibiting the WNT/β-catenin signaling pathway. Scientific Reports [Internet]. 2025Nov28;. Available from: https://www.nature.com/articles/s41598-025-30291-z
49. Ji JX, Giles BL, Bhattacharjee S, Kautzmann M-AI, P. MA, Do CS, et al.. Intercellular signaling and synaptic deconstruction uncovered by single-cell and spatial transcriptomics in an AD tauopathy model. Communications Biology [Internet]. 2025Nov17;8(1). Available from: https://www.nature.com/articles/s42003-025-08959-z
50. Available from: https://www.ncbi.nlm.nih.gov/gene/596
51. Oh Y, Yoo J, Lee D, Ko B, Hong JP, Moon JH, et al.. Restoring the glioblastoma tumor microenvironment by targeting C5a with the antagonist W54011. Scientific Reports [Internet]. 2025Dec6;. Available from: https://www.nature.com/articles/s41598-025-30853-1
52. Available from: https://www.ncbi.nlm.nih.gov/gene/283
53. Martín-Monteagudo C, Sánchez RJ, Adams JM, Puente N, Grandes P, Marsicano G, et al.. An astrocytic ensemble at vHip-NAc synapses modulates cognitive impairments induced by chronic tetrahydrocannabinol exposure. Nature Communications [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s41467-025-67166-w_reference.pdf
54. Available from: https://www.ncbi.nlm.nih.gov/gene/581
55. Available from: https://www.ncbi.nlm.nih.gov/gene/675
56. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
57. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
58. Available from: https://www.ncbi.nlm.nih.gov/gene/24387
59. Available from: https://www.ncbi.nlm.nih.gov/gene/12578
60. González-Gallego J, Todorov-Völgyi K, Müller SA, Antesberger S, Todorov MI, Malik R, et al.. A fully iPS-cell-derived 3D model of the human blood–brain barrier for exploring neurovascular disease mechanisms and therapeutic interventions. Nature Neuroscience [Internet]. 2025Dec15;. Available from: https://www.nature.com/articles/s41593-025-02123-w
61. Available from: https://www.ncbi.nlm.nih.gov/gene/4323
62. Huang Y, Fang W. TREM2-mediated regulation of myeloid cells in the tumor microenvironment: new insights and therapeutic prospects. npj Precision Oncology [Internet]. 2025Nov18;9(1). Available from: https://www.nature.com/articles/s41698-025-01152-9
63. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
64. Wang J, Wang H, Wang T, Zhang P, Cao Y, Yu T. The protective role of nuclear Heme oxygenase-1 in blood-spinal cord barrier after hypoxia in vitro. Scientific Reports [Internet]. 2025Dec2;. Available from: https://www.nature.com/articles/s41598-025-30888-4
65. Available from: https://www.ncbi.nlm.nih.gov/gene/10631
66. Available from: https://www.ncbi.nlm.nih.gov/gene/54209
67. Available from: http://json-schema.org/draft-07/schema#",
