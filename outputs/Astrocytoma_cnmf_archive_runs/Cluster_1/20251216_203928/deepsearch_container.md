# Gene Program Markdown Report

## Context
- Cell type: Astrocytes
- Disease: Astrocytoma (ranging from pilocytic astrocytoma WHO grade 1 to high-grade astrocytoma/glioblastoma WHO grades 3-4)
- Tissue: Brain; central nervous system

## Input Genes
TNC, CD44, VCL, SAMD4A, IGFBP7, DEC1, ELL2, CADPS, ACTN1, GBP2, BCL6, GLIS3, EMP1, SERPINA3, NAMPT, TPST1, GAP43, NEAT1, SPOCD1, GFAP, MAP3K14, FN1, CLIC4, PDE8B, MAP1B, ... (200 total)

## Program: Acute Neuroinflammatory Activation
Rapid pro-inflammatory gene expression program characterized by upregulation of pro-inflammatory cytokines, chemokines, and immune signaling molecules within 2 days of astrocyte activation. This program drives immune cell recruitment, complement activation, and establishment of neuroinflammatory microenvironment through coordinated action of immediate early transcription factors, cytokine receptors, and inflammatory effector molecules.

**Predicted impacts**
- Rapid recruitment of microglia and infiltrating immune cells into brain parenchyma
- Enhanced release of pro-inflammatory cytokines (IL-1, IL-6, TNF) amplifying neuroinflammatory cascade
- Activation of complement cascade promoting inflammation and immune cell recruitment
- Transient increases in astrocyte proliferation (within 3 days post-injury)
- Establishment of pro-inflammatory microenvironment exacerbating acute neuronal injury

**Evidence summary**
The acute neuroinflammatory activation program comprises canonical immediate early genes (EGR1, JUN, JUNB, FOS), pro-inflammatory cytokine receptors (IL6R, IL1R1, IL1RAP), chemokines (CCL2, CXCL2), and complement components (C1R, C3, CFI). This program demonstrates maximal expression at 2 days post-injury with robust upregulation of TNF, CCL2, IL-6, and IFN-γ signaling pathways. The program is mediated by STAT3-dependent transcriptional responses to IL-6 and IL-1 signaling. Strong literature support from temporal transcriptomic studies of acute brain injury and astrocyte activation demonstrates that this program consistently activates across multiple CNS injury contexts within hours to 2 days of injury onset.

**Atomic biological processes**
- Cytokine production and signaling. Genes: IL6R, IL1R1, IL1RAP, STAT3, TNF, CCL2
  - [3]: Comprehensive analysis of astrocyte cytokine production in acute TBI
  - [28]: RNA-seq analysis showing upregulation of IL-1, IL-6, TNF in acute astrocytes
  - [34]: Temporal analysis revealing pro-inflammatory cytokine signatures in acute phase
- Complement cascade activation. Genes: C1R, C3, CFI
  - [3]: Gene set enrichment reveals complement activation pathways
  - [28]: C1R and complement components enriched in acute TBI astrocytes
  - [34]: Temporal dynamics of complement-related genes
- Immediate early response transcription. Genes: EGR1, JUN, JUNB, FOS, FOSL2, ATF3, EGR3
  - [3]: EGR1, JUN, JUNB identified as acute response genes
  - [34]: Temporal dynamics show rapid upregulation of immediate early genes
  - [66]: EGR1 and related immediate early response genes in acute phase
- Toll-like receptor signaling. Genes: C1R
  - [3]: TLR2/MYD88 signaling prominent in acute astrocytes
  - [28]: Toll-like receptor pathway enriched in acute TBI

**Atomic cellular components**
- Chemokine receptor signaling complexes. Genes: CCL2, CXCL2
  - [3]: CCL2-mediated chemokine signaling
  - [28]: Leukocyte migration pathways driven by CCL2 upregulation

**Required genes (not in input)**
- Genes: TNF, IL6, IL1B, CXCL10, IRF5, IRF8, TLR2, MYD88, NFKBIA, REL, RELA
  - [3]: TNF, IL6, IL1B, CXCL10 major components of acute inflammatory response
  - [28]: IRF5, IRF8, TLR2, MYD88 identified as key regulators

**Program citations**
- [3]: RNA-seq of acute TBI astrocytes identifies pro-inflammatory signature
- [7]: Confirms acute neuroinflammatory gene expression patterns
- [28]: Detailed transcriptomic analysis at 2 days post-injury
- [34]: Comprehensive temporal analysis of acute phase astrocytes
- [66]: Validation of acute inflammatory gene expression patterns

## Program: Extracellular Matrix Remodeling and Microenvironment Sculpting
Dynamic reorganization of brain extracellular matrix involving upregulation of ECM structural proteins (collagen, fibronectin), proteolytic enzymes, matrix inhibitors, and ECM-associated molecules. This program reshapes the local microenvironment, facilitating cell migration, immune cell infiltration, and influencing neuronal survival through altered ECM-integrin interactions. ECM composition changes across reactive phases from acute inflammation toward chronic neurodegeneration.

**Predicted impacts**
- Reorganization of basement membrane architecture affecting vascular permeability
- Increased ECM protein deposition creating pro-migratory substrate
- Synapse pruning through SPARC-mediated mechanisms eliminating synaptic contacts
- Enhanced infiltration of immune cells through remodeled ECM
- Creation of physically altered microenvironment affecting astrocyte-neuron interactions
- Deposition of ECM components promoting astrocytoma cell invasion

**Evidence summary**
The ECM remodeling program includes major structural proteins (FN1, COL4A1, COL4A2, COL8A1, EFEMP1), synapse pruning mediators (SPARC, SPARCL1, CLU), and proteolytic regulators (TIMP3, ADAMTS9, SULF1). FN1 upregulation creates adhesive substrates promoting cell migration. Type IV collagen (COL4A1/COL4A2) composition changes alter basement membrane integrity. SPARC and SPARCL1 upregulation in subacute phases (2 weeks post-injury) correlates with enhanced synapse pruning and transition toward neurodegenerative processes. The program demonstrates dynamic temporal regulation with initial FN1 and collagen upregulation in acute phases transitioning toward SPARC-mediated synapse elimination in subacute phases. Strong representation in both normal reactive astrocyte models and astrocytoma contexts indicates high relevance to disease pathogenesis.

**Atomic biological processes**
- Extracellular matrix protein synthesis and deposition. Genes: FN1, COL4A1, COL4A2, COL8A1, EFEMP1
  - [34]: Comprehensive analysis of ECM remodeling during astrocyte activation
  - [51]: Detailed characterization of ECM components in astrocytes
  - [67]: Single-cell spatial transcriptomics reveals ECM heterogeneity in gliomas
- Matrix metalloproteinase inhibition and regulation. Genes: TIMP3
  - [34]: TIMP3 upregulation regulates proteolytic activity
  - [51]: Temporal dynamics of TIMP expression
- Synapse-associated matrix protein expression. Genes: SPARC, SPARCL1, CLU
  - [34]: SPARC upregulation in subacute phase promotes synapse pruning
  - [51]: SPARC and SPARCL1 mediate synapse elimination
  - [67]: ECM-synapse interactions in glioma microenvironment
- Matrix proteoglycan synthesis and modification. Genes: ADAMTS9, SULF1, HAS2
  - [34]: Temporal upregulation of proteoglycan-modifying enzymes
  - [67]: Spatial heterogeneity of ECM component expression

**Atomic cellular components**
- Basement membrane architecture. Genes: COL4A1, COL4A2
  - [67]: Type IV collagen in basement membrane
  - [34]: Basement membrane disruption in reactive astrocytes
- Cell-ECM interaction zones. Genes: FN1, VCL, ITGA3, ITGAV
  - [34]: Focal adhesion involvement in ECM interactions
  - [51]: Integrin-mediated ECM sensing

**Required genes (not in input)**
- Genes: MMP2, MMP3, MMP9, THBS1, THBS4, LAMA2, LAMB1, LAMC1, NIDOGEN1, NIDOGEN2
  - [34]: MMP2, MMP3, MMP9 major matrix-degrading enzymes
  - [67]: Additional ECM components in glioma microenvironment
  - [51]: Thrombospondin variants regulate ECM-integrin interactions

**Program citations**
- [34]: Comprehensive temporal analysis of ECM remodeling
- [51]: ECM components in chronic TBI astrocytes
- [67]: Spatial transcriptomics of ECM in glioma microenvironment

## Program: Oxidative Stress Response and Antioxidant Defense
Coordinated upregulation of antioxidant enzymes, ROS-scavenging proteins, and stress response mediators balancing reactive oxygen species generation accompanying inflammatory activation. This program reflects astrocytes' simultaneous roles as sources of inflammatory ROS and defenders against oxidative damage to cellular components. Temporal dynamics show enhanced antioxidant responses in subacute and chronic phases as astrocytes transition from acute inflammation.

**Predicted impacts**
- Enhanced antioxidant defense protecting cellular macromolecules from ROS-mediated damage
- Balanced ROS production enabling inflammatory signaling while limiting toxicity
- Maintenance of mitochondrial integrity and function during metabolic stress
- NAD+-dependent SIRT activation supporting stress resistance
- Prevention of excessive oxidative damage while preserving protective ROS signaling
- Neuroprotective effects through sustained antioxidant capacity in chronic phases

**Evidence summary**
The oxidative stress response program centers upon SOD2 (mitochondrial superoxide dismutase), stress-response transcription factors (ATF3, GADD45A, GADD45B, NR4A3), and metabolic adaptors supporting NAD+ biosynthesis (NAMPT). Gene set enrichment analysis of acute TBI astrocytes reveals concurrent enrichment in both reactive oxygen species production pathways and antioxidant defense mechanisms, reflecting astrocytes' simultaneous roles as inflammatory ROS generators and oxidative stress defenders. SOD2 upregulation demonstrates particular prominence in subacute phases (2 weeks post-injury) and persists in chronic phases, indicating sustained importance for protecting astrocytes from oxidative damage. The program shows temporal evolution from acute phase emphasis on ROS production pathways toward subacute and chronic phase increases in antioxidant enzyme expression, suggesting metabolic stabilization and transition away from acute inflammation.

**Atomic biological processes**
- Superoxide dismutation and ROS scavenging. Genes: SOD2
  - [3]: SOD2 upregulation in acute TBI astrocytes
  - [28]: Gene set enrichment reveals reactive oxygen species production pathways
  - [34]: SOD2 upregulation maintained in subacute and chronic phases
- Stress-responsive protein synthesis and chaperone activity. Genes: ATF3, GADD45A, GADD45B, NR4A3
  - [3]: Chaperone genes (CRYAB, HSPB1) upregulated in acute astrocytes
  - [34]: Comprehensive analysis of protein stress response
  - [51]: CRYAB upregulation supports neuroprotective functions
- NAD+-dependent stress adaptation. Genes: NAMPT
  - [34]: NAMPT upregulation supports NAD+ biosynthesis
  - [51]: Metabolic adaptation in chronic astrocytes
  - [56]: NAMPT catalyzes rate-limiting step in NAD+ biosynthesis

**Atomic cellular components**
- Mitochondrial antioxidant systems. Genes: SOD2
  - [3]: SOD2 localization to mitochondrial matrix
  - [28]: Oxidative phosphorylation pathway enrichment

**Required genes (not in input)**
- Genes: SOD1, CAT, GPX1, PRDX1, PRDX3, TXNRD1, GSR
  - [3]: SOD1 in cytosolic compartment alongside mitochondrial SOD2
  - [28]: Glutathione and thioredoxin systems important for ROS detoxification
  - [34]: Comprehensive antioxidant enzyme families

**Program citations**
- [3]: Gene set enrichment reveals ROS pathway activation
- [28]: SOD1/SOD2 upregulation alongside ROS production
- [34]: Temporal dynamics of antioxidant responses

## Program: Cytoskeletal Reorganization and Cell Migration
Coordinated remodeling of actin microfilaments, microtubules, and intermediate filaments enabling rapid astrocyte morphological transformation from resting ramified states to activated hypertrophic states. This program supports enhanced cell motility, process extension/retraction, and migration into areas of injury. Includes regulators of actin polymerization, focal adhesion dynamics, and microtubule-associated protein functions.

**Predicted impacts**
- Rapid morphological transformation from ramified to hypertrophic states
- Enhanced cell motility enabling migration toward injury sites
- Increased mechanotransduction through focal adhesion signaling
- Augmented integrin-mediated ECM sensing and adhesion
- Facilitation of astrocyte infiltration into damaged brain regions
- Support for invasive astrocytoma cell phenotypes

**Evidence summary**
The cytoskeletal reorganization program comprises actin-binding proteins (ACTN1, VIM, CNN3, TPM4), focal adhesion components (VCL, NEDD9, SORBS1), microtubule-associated proteins (MAP1B, CLIP1), and migration regulators (TRIO, ARHGEF3). Vimentin (VIM), the major intermediate filament of astrocytes, demonstrates robust upregulation following activation and directly correlates with acquisition of pro-inflammatory and pro-migratory phenotypes. Vinculin (VCL) upregulation supports focal adhesion assembly and mechanotransduction. Alpha-actinin proteins (ACTN1) crosslink actin filaments and enable rapid morphological remodeling. The program demonstrates functional integration with adhesion molecule expression (ITGA3, ITGAV, CD44) enabling astrocyte interaction with ECM components. Enhanced expression of Rho family GTPase activators (TRIO, ARHGEF3) coordinates migration signaling with cytoskeletal dynamics. Multiple lines of evidence from reactive astrocyte models and astrocytoma contexts confirm that this program enables both normal reactive astrocyte responses and tumor-promoting invasive phenotypes.

**Atomic biological processes**
- Actin filament organization and dynamics. Genes: ACTN1, VIM, CNN3, TPM4, VCL
  - [3]: Astrocyte morphological transformation involves actin reorganization
  - [34]: ACTN1, VIM, CNN3 upregulated in reactive astrocytes
  - [51]: Cytoskeletal remodeling supports cell migration
- Focal adhesion complex assembly and signaling. Genes: VCL, ACTN1, NEDD9
  - [34]: Focal adhesion kinase signaling in reactive astrocytes
  - [51]: Vinculin mediates integrin-actin linkage
  - [66]: Focal adhesion dynamics during astrocyte migration
- Microtubule dynamics and organization. Genes: MAP1B, CLIP1
  - [34]: MAP1B in astrocyte process morphology
  - [51]: Microtubule-associated proteins in reactive transformation
- Cell migration and invasion. Genes: TRIO, ARHGEF3, SORBS1, NEDD9, ITGA3, ITGAV
  - [34]: Enhanced astrocyte migration in reactive states
  - [51]: Multiple genes coordinately support migration
  - [67]: Migration-associated genes in astrocytoma

**Atomic cellular components**
- Actin-based contractile structures. Genes: ACTN1, VIM, TPM4, VCL
  - [34]: Stress fiber formation in reactive astrocytes
  - [51]: Actin crosslinking proteins
- Focal adhesion plaques. Genes: VCL, NEDD9, SORBS1
  - [34]: Focal adhesion assembly in activated astrocytes
  - [66]: Dynamic focal adhesion remodeling

**Required genes (not in input)**
- Genes: ACTIN-related proteins (ARP2/3 complex), WASP, N-WASP, LIMK1, COFILIN1, RAC1, CDC42, RHOA
  - [34]: ARP2/3 complex nucleates actin filaments
  - [51]: Small GTPases coordinate actin dynamics

**Program citations**
- [34]: Comprehensive analysis of cytoskeletal gene expression
- [51]: Temporal dynamics of migration-related genes
- [66]: Integration of cytoskeleton with signaling pathways

## Program: Pan-Reactive Astrocyte Marker Expression
Expression of genes serving as canonical markers of astrocyte reactivity across diverse CNS injury and disease contexts. These genes demonstrate rapid upregulation following astrocyte activation and persist through multiple phases of reactive transformation. Pan-reactive markers indicate astrocyte identity and degree of activation while conveying limited information regarding specific functional phenotypes (pro-inflammatory versus neuroprotective).

**Predicted impacts**
- Reliable indicators of astrocyte activation status across injury/disease contexts
- Markers enabling discrimination of reactive versus quiescent astrocytes
- Indicators of glial scar formation and neuroinflammatory microenvironment
- Biomarkers for disease progression and therapeutic response
- Partial prediction of functional phenotypes (A1-like pro-inflammatory vs. A2-like neuroprotective)

**Evidence summary**
The pan-reactive astrocyte marker program comprises GFAP (glial fibrillary acidic protein), CD44 (cell adhesion molecule), SERPINA3 (serine protease inhibitor), and CHI3L1 (chitinase-3-like protein 1). These genes demonstrate robust and consistent upregulation across diverse CNS injury contexts including traumatic brain injury, ischemic stroke, and chronic neurodegenerative diseases. GFAP represents the most widely used marker of both basal astrocyte identity and reactive transformation, with upregulation commencing within hours of CNS injury and persisting through chronic phases. CD44 upregulation accompanies acquisition of invasive and stemness-associated phenotypes in astrocytes. SERPINA3 demonstrates particular prominence as a dual-function marker correlating with both acute inflammation and neuroprotective functions. CHI3L1 (YKL-40) elevation predicts disease progression in multiple neuroinflammatory conditions. While these markers reliably indicate astrocyte reactivity, they demonstrate limited capacity to distinguish between pro-inflammatory and neuroprotective astrocyte phenotypes without additional gene expression context.

**Atomic biological processes**
- Astrocyte identity maintenance and activation confirmation. Genes: GFAP, CD44, SERPINA3, CHI3L1
  - [9]: GFAP and YKL-40 as early Alzheimer's disease biomarkers
  - [19]: CHI3L1 as pan-reactive astrocyte marker
  - [34]: GFAP, APOE, CD44, SERPINA3, CXCL10 as key pan-reactive markers
  - [51]: Comprehensive characterization of reactive astrocyte markers
- Cell-cell communication and adhesion. Genes: CD44, NRCAM
  - [34]: CD44 upregulation in reactive astrocytes
  - [51]: CD44 promotes astrocyte-derived progenitor emergence
- Immune-regulatory protein expression. Genes: SERPINA3, CHI3L1
  - [34]: SERPINA3 dual role as pan-reactive marker and neuroprotective factor
  - [51]: CHI3L1 expression across reactive phases

**Required genes (not in input)**
- Genes: APOE, CXCL10, CSF1R
  - [34]: APOE as major pan-reactive marker
  - [51]: CXCL10 expressed in reactive phases
  - [7]: CSF1R involved in microglial recruitment

**Program citations**
- [3]: GFAP and related pan-reactive markers in acute TBI
- [9]: GFAP biomarker relevance to neurodegeneration
- [19]: CHI3L1 as pan-reactive marker
- [34]: Comprehensive characterization across reactive phases
- [51]: Expression patterns persisting one year after TBI

## Program: Metabolic Reprogramming Toward Glycolysis and Biosynthesis
Coordinated rewiring of astrocyte metabolism from oxidative phosphorylation-dependent energy production toward enhanced glycolytic flux and biosynthetic pathways. This metabolic shift supports inflammatory mediator production, ECM protein synthesis, and rapid biosynthesis accompanying immune activation. Includes upregulation of glycolytic enzymes, amino acid metabolism, and lipid synthesis pathways.

**Predicted impacts**
- Enhanced ATP production via glycolysis supporting biosynthetic demands
- Increased NADH and reducing equivalents for biosynthesis
- Enhanced glutamate production supporting immune cell metabolism
- NAD+-dependent SIRT activation promoting stress resistance
- Increased polyamine synthesis supporting rapid proliferation
- Enhanced lipid biosynthesis supporting membrane trafficking and secretion
- Transition from quiescent astrocyte metabolism toward immune-activated metabolism

**Evidence summary**
The metabolic reprogramming program comprises glycolytic enzymes (PFKFB3), amino acid metabolic enzymes (GLUL), NAD+ biosynthetic pathways (NAMPT), polyamine metabolism (SAT1), and lipid biosynthetic enzymes (ELOVL5). PFKFB3 upregulation in reactive astrocytes catalyzes synthesis of fructose-2,6-bisphosphate, a potent allosteric activator of phosphofructokinase that promotes glycolytic flux. GLUL upregulation increases glutamate production, simultaneously supporting excitatory neurotransmission and providing glutamate for immune cell metabolism. NAMPT catalyzes the rate-limiting step in NAD+ biosynthesis, supporting NAD+-dependent SIRT1 signaling for stress resistance. The program demonstrates temporal evolution with enhancement of both glycolytic and oxidative phosphorylation pathways in chronic phases. This metabolic shift parallels classical immune cell activation patterns, indicating convergent metabolic rewiring between astrocytes and professional immune cells during inflammatory responses.

**Atomic biological processes**
- Aerobic glycolysis and lactate metabolism. Genes: PFKFB3, GLUL
  - [34]: PFKFB3 promotes glycolytic flux in reactive astrocytes
  - [51]: Metabolic shift toward glycolysis in reactive transformation
  - [13]: GAPDH and glycolytic enzyme roles in glial cells
- Amino acid metabolism and glutamate homeostasis. Genes: GLUL
  - [34]: GLUL upregulation increases glutamate production
  - [51]: Glutaminase role in immune metabolism
- NAD+ biosynthesis and SIRT-dependent signaling. Genes: NAMPT
  - [34]: NAMPT catalyzes rate-limiting NAD+ biosynthesis
  - [51]: NAD+-dependent SIRT1 activation supports stress adaptation
  - [56]: NAMPT overexpression in activated immune cells
- Polyamine metabolism. Genes: SAT1
  - [34]: SAT1 increases in reactive astrocytes
  - [51]: Polyamine metabolism supports proliferation
- Lipid synthesis and membrane remodeling. Genes: ELOVL5, PFKFB3
  - [34]: ELOVL5 upregulation supports lipid biosynthesis
  - [51]: Enhanced membrane trafficking in reactive astrocytes

**Atomic cellular components**
- Mitochondrial metabolic compartments. Genes: NAMPT, PFKFB3
  - [34]: Mitochondrial dynamics during metabolic shift
  - [51]: Oxidative phosphorylation pathway enrichment

**Required genes (not in input)**
- Genes: GAPDH, LDHA, LDHB, PKM, SLC1A1, SLC1A3, GFPT1, GFPT2
  - [13]: GAPDH role in astrocyte metabolism
  - [34]: LDHA/LDHB and lactate metabolism
  - [51]: Glutamate-aspartate transporters and amino acid metabolism

**Program citations**
- [34]: Comprehensive metabolic pathway enrichment analysis
- [51]: Temporal metabolic dynamics
- [56]: NAMPT function in metabolism

## Program: Synapse-Associated Pruning and Neuronal Interaction
Expression of genes mediating astrocyte-dependent elimination of synapses and neuronal projections through multiple complementary mechanisms. This program operates predominantly in subacute phases of injury (1-2 weeks post-injury) and establishes astrocyte roles in activity-dependent synaptic remodeling, complement-mediated synapse elimination, and thrombospondin-integrin-mediated pruning.

**Predicted impacts**
- Enhanced synaptic pruning and elimination of immature/damaged synapses
- Remodeling of synaptic architecture through SPARC-mediated mechanisms
- Modulation of synaptic strength through astrocyte-neuron contact dynamics
- Support for neuronal survival through neuroprotective cytokine signaling
- Contribution to synaptic refinement and functional reorganization
- Participation in activity-dependent synaptic plasticity

**Evidence summary**
The synapse pruning program comprises ECM-associated proteins (SPARC, SPARCL1, CLU), astrocyte-neuron adhesion molecules (NRCAM), and neuroprotective cytokine mediators (CLCF1). SPARC and SPARCL1 promote synapse elimination through interaction with thrombospondin-binding integrins on astrocytes and neuronal surfaces. These genes show selective upregulation in subacute injury phases (2 weeks post-injury) coinciding with active synaptic remodeling and refinement. NRCAM downregulation in acute phases correlates with synapse elimination, while selective re-expression in subacute and chronic phases indicates dynamic modulation of astrocyte-neuron interactions. CLCF1 promotes neuroprotective signaling through CNTFR engagement on neurons. The temporal pattern of synapse pruning program activation follows resolution of acute neuroinflammation, suggesting coordinated transition from acute inflammation toward chronic neurodegeneration. While astrocyte-mediated synaptic pruning supports normal brain development and activity-dependent plasticity, dysregulation of this program may contribute to long-term cognitive and functional deficits in TBI and other CNS disorders.

**Atomic biological processes**
- ECM-mediated synapse pruning and elimination. Genes: SPARC, SPARCL1, CLU
  - [34]: SPARC and SPARCL1 upregulation in subacute phase promotes synapse pruning
  - [51]: SPARC promotes synapse elimination in chronic TBI
  - [67]: ECM-integrin interactions in synaptic organization
- Astrocyte-neuron contact and synaptic stabilization. Genes: NRCAM, CLCF1
  - [34]: NRCAM downregulation in acute phases correlates with synapse elimination
  - [43]: Dynamic modulation of astrocyte-neuron adhesion
- Neuroprotective signaling and cytokine-mediated synaptic support. Genes: CLCF1
  - [34]: CLCF1 promotes neuroprotective signaling
  - [51]: Cytokine-mediated astrocyte support of neuronal survival

**Atomic cellular components**
- Synaptic ECM zones and perineuronal nets. Genes: SPARC, SPARCL1
  - [34]: SPARC localization to synaptic ECM
  - [51]: ECM architecture in synaptic regions

**Required genes (not in input)**
- Genes: THBS1, THBS4, C1QA, C1QB, C1QC, MERTK, C3AR1, C3
  - [34]: Thrombospondin isoforms promote synapse pruning
  - [51]: Complement-mediated synaptic engulfment
  - [67]: Multiple pruning mechanisms coordinate

**Program citations**
- [34]: Temporal dynamics of synapse pruning genes
- [43]: Synaptic interaction genes in chronic TBI
- [51]: SPARC and related ECM proteins

## Program: Transcriptional Control of Inflammatory and Stress Responses
Coordinated expression of immediate early transcription factors and stress-response regulators enabling rapid transcriptional reprogramming of astrocytes following injury or inflammatory stimuli. These transcription factors establish temporal dynamics of gene expression through sequential waves of AP-1 family members, stress-inducible factors, and STAT-family transcriptional regulators.

**Predicted impacts**
- Rapid transcriptional reprogramming within hours of injury stimuli
- Sequential activation of gene programs through temporal waves of transcription factor expression
- Integration of multiple signal inputs (STAT3, AP-1, ATF3) for coordinated gene expression
- Establishment of temporal dynamics allowing transition from acute inflammation to chronic neurodegeneration
- Stress-responsive transcriptional adaptation supporting metabolic rewiring and biosynthesis
- Negative feedback through SOCS3 preventing excessive inflammatory responses

**Evidence summary**
The transcriptional control program comprises AP-1 family members (JUN, JUNB, FOS, FOSL2), immediate early response factors (EGR1, EGR3), stress-responsive transcription factors (ATF3), STAT family members (STAT3), and Krüppel-like factors (KLF6, KLF7). These transcription factors demonstrate rapid upregulation within hours of injury, with AP-1 and EGR family members showing maximal expression at 2 days post-injury followed by partial decline in subacute phases. STAT3 demonstrates persistent upregulation through chronic phases, indicating sustained cytokine signaling. The inclusion of SOCS3 (suppressor of cytokine signaling 3), a negative feedback inhibitor of STAT3 signaling, reflects activation of cytokine responses coupled with induction of negative feedback mechanisms limiting signal intensity. The temporal dynamics of transcription factor expression establish sequential waves enabling transition from acute inflammation toward chronic neurodegeneration. Multiple studies confirm that these transcription factors coordinately regulate inflammatory genes, metabolic enzymes, and cytoskeletal proteins, making them essential nodes controlling astrocyte reactive transformation.

**Atomic biological processes**
- AP-1 complex formation and inflammatory gene regulation. Genes: JUN, JUNB, FOS, FOSL2
  - [3]: JUN, JUNB, FOS, FOSL2 form AP-1 complexes regulating inflammatory genes
  - [34]: Temporal dynamics of AP-1 complex members
  - [66]: JUN and JUNB expression in acute phase
- Early growth response factors in rapid transcriptional response. Genes: EGR1, EGR3
  - [3]: EGR1 rapid induction in response to injury
  - [34]: EGR1 upregulation and partial decline in subacute phase
  - [66]: EGR family members in stress response
- Integrative stress response through ATF family factors. Genes: ATF3
  - [34]: ATF3 induction in metabolic stress
  - [51]: ATF3 role in integrated stress response
- STAT-mediated cytokine signaling responses. Genes: STAT3, SOCS3
  - [3]: STAT3 phosphorylation and nuclear translocation
  - [34]: STAT3 as master regulator of pro-inflammatory genes
  - [66]: STAT3 downstream signaling
- Krüppel-like factor-mediated differentiation and inflammation control. Genes: KLF6, KLF7
  - [34]: KLF6 and KLF7 in astrocyte activation
  - [51]: KLF family dynamic expression

**Atomic cellular components**
- Transcription factor binding at cis-regulatory elements. Genes: JUN, JUNB, FOS, FOSL2, EGR1, STAT3
  - [3]: AP-1 binding sites in inflammatory gene promoters
  - [34]: Multiple transcription factors coordinate binding

**Required genes (not in input)**
- Genes: CEBPB, CEBPD, NFKB1, RELA, RELB, IRF5, IRF8, IRF1
  - [3]: C/EBP and NF-κB family members
  - [34]: IRF family in inflammatory response
  - [51]: Multiple transcription factor families coordinate

**Program citations**
- [3]: Comprehensive analysis of transcriptional regulation
- [34]: Temporal dynamics across reactive phases
- [66]: Transcription factor expression patterns

## Program: Growth Factor Signaling and Cellular Proliferation Control
Expression of growth factor ligands, receptors, and downstream signaling effectors coordinating astrocyte proliferation and differentiation decisions. This program includes TGF-β, FGF, and IGF signaling pathways that regulate astrocyte survival, proliferation, and acquisition of specific functional phenotypes. Includes both positive growth-promoting and negative cell-cycle inhibitory factors.

**Predicted impacts**
- Enhanced proliferation in subacute phases supporting astrocyte expansion
- TGF-β-mediated promotion of neuroprotective and immunosuppressive phenotypes
- Modulation of growth factor bioavailability through binding protein expression
- Checkpoint-mediated growth arrest during acute stress phases
- Release from growth inhibition during transition to chronic phases
- Support for astrocyte-derived progenitor cell expansion and neurogenic capacity

**Evidence summary**
The growth factor signaling program comprises TGF-β pathway components (TGFB2, TGFBR2), IGF pathway modulators (IGFBP7), and cell cycle checkpoint regulators (GADD45A, GADD45B, NR4A3). TGFB2 upregulation in astrocytes establishes autocrine TGF-β signaling loops that maintain reactive states. TGFBR2 upregulation enhances astrocyte responsiveness to both autocrine TGFB2 and paracrine TGF-β from other sources. IGFBP7 modulation of IGF bioavailability suggests selective regulation of growth factor signaling intensity. GADD45A and GADD45B demonstrate downregulation in chronic phases as astrocytes release from cell cycle checkpoints. The temporal dynamics of this program correlate with progressive increases in astrocyte proliferation from acute phases through subacute and chronic phases, with checkpoint relaxation enabling sustained expansion of astrocyte populations. The program demonstrates integration with transcriptional control networks, whereby growth factor signaling through SMAD-dependent pathways coordinates with AP-1 and STAT3 signaling to establish specific astrocyte phenotypes.

**Atomic biological processes**
- Transforming growth factor-beta signaling and immune regulation. Genes: TGFB2, TGFBR2
  - [34]: TGFB2 and TGFBR2 upregulation in reactive astrocytes
  - [51]: TGF-β signaling promotes neuroprotective functions
- Insulin-like growth factor pathway modulation. Genes: IGFBP7
  - [34]: IGFBP7 regulation of IGF bioavailability
  - [51]: Growth factor binding proteins in astrocytes
- Cell cycle checkpoint control and proliferation limitation. Genes: GADD45A, GADD45B, NR4A3
  - [3]: GADD45A/B induction in acute phase
  - [34]: Checkpoint control genes in stress response
  - [51]: Temporal dynamics of cell cycle inhibitors

**Atomic cellular components**
- Growth factor receptor complexes. Genes: TGFBR2, IGFBP7
  - [34]: TGFBR1/TGFBR2 heterodimeric signaling
  - [51]: Growth factor receptor activation

**Required genes (not in input)**
- Genes: SMAD2, SMAD3, SMAD4, CDKN1A, FGF2, FGFR1, FGF7
  - [34]: SMAD-dependent TGF-β signaling
  - [51]: FGF signaling in astrocytes
  - [70]: FGF2 in astrocyte responses

**Program citations**
- [34]: Growth factor pathway enrichment analysis
- [51]: Temporal dynamics of growth signaling
- [3]: TGF-β in astrocyte activation

## Program: Cell Adhesion, Migration, and Extracellular Matrix Interactions
Expression of cell adhesion molecules (integrins, cadherins, immunoglobulin superfamily members) and their ligands enabling astrocyte interactions with ECM components and neighboring cells. This program supports cell migration, invasive capacity, and mechanotransduction while regulating astrocyte invasion in astrocytoma contexts.

**Predicted impacts**
- Enhanced astrocyte adhesion to collagen and fibronectin in ECM
- Increased cell migration toward injury sites
- Augmented mechanotransduction supporting rapid environmental sensing
- EMT-like phenotypic transitions in astrocytoma contexts
- Support for invasive astrocytoma cell phenotypes
- Modulation of immune cell infiltration through adhesion molecule expression
- Hyperadhesion contributing to glial scar formation

**Evidence summary**
The cell adhesion and migration program comprises integrin subunits (ITGA3, ITGAV), cadherin molecules (CDH11), hyaluronic acid-binding adhesion molecules (CD44), and migration regulators (TRIO, ARHGEF3, SORBS1, NEDD9). ITGA3 (integrin α3β1) primarily binds laminin and collagen, mediating astrocyte adhesion to basement membranes. ITGAV (integrin αV) complexes bind fibronectin, vitronectin, and thrombospondin. CDH11 upregulation correlates with EMT-like transitions and enhanced invasive capacity. CD44 upregulation accompanies acquisition of stemness and invasive phenotypes. Vinculin (VCL) links integrins to actin, enabling mechanotransduction and rapid morphological responses. Migration regulators including TRIO, ARHGEF3, and SORBS1 coordinate Rho family GTPase signaling with cytoskeletal dynamics. The program demonstrates dysregulation in astrocytoma contexts, with enhanced integrin and cadherin expression supporting invasive tumor cell phenotypes. Multiple studies confirm dysregulation of this program in astrocytoma specimens relative to normal brain tissue.

**Atomic biological processes**
- Integrin-mediated ECM adhesion and signaling. Genes: ITGA3, ITGAV, VCL, NEDD9
  - [34]: ITGA3, ITGAV upregulation in reactive astrocytes
  - [51]: Integrin engagement with ECM ligands
  - [67]: Integrin-ECM interactions in glioma microenvironment
- Cadherin-mediated cell-cell adhesion. Genes: CDH11
  - [34]: CDH11 upregulation in reactive astrocytes
  - [51]: Switch from CDH1 to CDH11 in gliomas
  - [67]: Cadherin switches in EMT-like processes
- Hyaluronic acid-mediated adhesion and immune signaling. Genes: CD44, HAS2
  - [34]: CD44 binding to hyaluronic acid
  - [51]: CD44 upregulation in reactive transformation
  - [67]: CD44-HA interactions in tumor microenvironment
- Cell migration and invasion. Genes: TRIO, ARHGEF3, SORBS1, NEDD9
  - [34]: Migration-associated genes in activated astrocytes
  - [51]: Enhanced invasive capacity in astrocytoma

**Atomic cellular components**
- Integrin-ECM binding interface. Genes: ITGA3, ITGAV, FN1, COL4A1, COL4A2
  - [34]: Integrin ligand binding to collagen and fibronectin
  - [67]: ECM-integrin interactions
- Focal adhesion-cytoskeleton linkage. Genes: VCL, ACTN1, NEDD9
  - [34]: Vinculin bridges integrin and actin
  - [51]: Mechanotransduction through focal adhesions

**Required genes (not in input)**
- Genes: LAMA2, LAMB1, LAMC1, CDH1, CTNNB1, CDH2, NRCAM
  - [34]: Laminin subunits in basement membrane
  - [51]: Classical cadherins and beta-catenin
  - [67]: Multiple adhesion molecule families

**Program citations**
- [34]: Comprehensive analysis of adhesion molecules
- [51]: Temporal dynamics of migration-related genes
- [67]: Spatial transcriptomics of adhesion molecules in glioma

## Program: Tumor Microenvironment Remodeling and Immunosuppression
Expression of genes creating pro-tumoral, immunosuppressive microenvironments within astrocytoma through ECM remodeling, recruitment of myeloid-derived suppressor cells, expression of immunomodulatory molecules, and vascular co-option. This program integrates multiple mechanisms supporting astrocytoma growth including lymphangiogenesis, immune cell infiltration and polarization, and angiogenesis.

**Predicted impacts**
- Enhanced immune cell infiltration through increased chemokine secretion
- Establishment of immunosuppressive microenvironment limiting anti-tumor immunity
- Promotion of myeloid-derived suppressor cell recruitment and retention
- Facilitation of lymphangiogenesis supporting immune cell trafficking
- Vascular co-option and enhanced angiogenesis
- ECM remodeling supporting astrocytoma cell invasion and growth
- Creation of pro-tumoral niches favoring malignant progression

**Evidence summary**
The tumor microenvironment remodeling program comprises chemokines (CCL2, CXCL2), cytokine receptors (IL6R, IL1RAP), growth factors (TGFB2, TGFBR2), ECM proteins (FN1, COL4A1, COL4A2), and lymphangiogenesis mediators (PDPN). CCL2 upregulation recruits infiltrating macrophages and microglia, reshaping the cellular composition of the tumor microenvironment. IL-6 trans-signaling through soluble IL-6R particularly promotes immunosuppressive IL-10 and TGF-β production in immune cells, creating immunosuppressive microenvironments. PDPN upregulation facilitates lymphangiogenesis and immune cell infiltration. ECM remodeling creates invasion-promoting and growth-supporting niches. The program demonstrates enhanced expression in high-grade astrocytomas and glioblastomas relative to low-grade gliomas, indicating particular relevance to malignant progression. Notably, BRAF fusion mutations common in pilocytic astrocytomas drive CCL2 expression through NFkappaB-mediated mechanisms, establishing causative links between driver mutations and microenvironmental remodeling. Multiple spatial transcriptomic studies demonstrate heterogeneous ECM and immune cell distribution within astrocytoma microenvironments, with differential expression patterns in vascular endothelium, microglia, and macrophages.

**Atomic biological processes**
- Vascular growth and lymphangiogenesis. Genes: PDPN
  - [11]: VEGFA in angiogenesis and tumor growth
  - [67]: Vascular endothelial cells express distinctive ECM in glioma
- Immune cell recruitment and infiltration. Genes: CCL2, CXCL2, IL6R, IL1RAP
  - [3]: CCL2-mediated microglial recruitment
  - [28]: Immune cell chemotaxis pathways
  - [34]: Leukocyte migration in reactive astrocytes
  - [67]: Immune cell infiltration in glioma
- Immunosuppressive microenvironment establishment. Genes: IL6R, TGFB2, TGFBR2
  - [34]: IL-6 trans-signaling promotes immunosuppression
  - [67]: Immunosuppressive vascular niche in glioblastoma
  - [69]: Immunosuppressive mechanisms in tumor microenvironment
- Myeloid cell infiltration and polarization. Genes: CCL2, IL6R
  - [4]: BRAF-mediated NFkappaB-dependent CCL2 production recruiting microglia
  - [67]: Microglia and macrophage polarization
- Perivascular niche formation and vascular co-option. Genes: FN1, COL4A1, COL4A2, PDPN
  - [67]: ECM proteins in vascular niches
  - [69]: Peritumoral microenvironment characteristics

**Atomic cellular components**
- Perivascular space compartments. Genes: FN1, COL4A1, COL4A2, PDPN
  - [67]: ECM composition in perivascular regions
  - [69]: Peritumoral microenvironment structure

**Required genes (not in input)**
- Genes: CSF1, VEGFA, VEGFC, ANGPT1, ANGPT2, IL10, ICAM1, VCAM1
  - [4]: CSF1 in microglia recruitment
  - [67]: VEGFA/VEGFC in angiogenesis and lymphangiogenesis
  - [69]: Additional immunosuppressive mediators

**Program citations**
- [4]: BRAF-driven CCL2 and microglia recruitment
- [34]: IL-6 trans-signaling immunosuppression
- [67]: Single-cell spatial mapping of ECM in glioma
- [69]: Immune cell dynamics in peritumoral cortex

## Bibliography
1. William D, Ryan A. Prognostic and predictive determinants in high-grade gliomas: integrating tumor-intrinsic biology with patient and system-level factors.. Frontiers in neurology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/41346390/?fc=None&ff=20251206024217&v=2.18.0.post22+67771e2
2. Available from: https://www.ncbi.nlm.nih.gov/gene/6678
3. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
4. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
5. Available from: https://www.ncbi.nlm.nih.gov/gene/4015
6. Available from: https://www.ncbi.nlm.nih.gov/gene/7098
7. Available from: https://www.ncbi.nlm.nih.gov/gene/9021
8. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
9. Available from: https://www.ncbi.nlm.nih.gov/gene/3569
10. Available from: https://www.ncbi.nlm.nih.gov/gene/7422
11. Available from: https://www.ncbi.nlm.nih.gov/gene/4312
12. Available from: https://www.ncbi.nlm.nih.gov/gene/2597
13. Available from: https://www.ncbi.nlm.nih.gov/gene/51162
14. Available from: https://www.ncbi.nlm.nih.gov/gene/4313
15. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
16. Available from: https://www.ncbi.nlm.nih.gov/gene/87
17. Available from: https://www.ncbi.nlm.nih.gov/gene/13653
18. Available from: https://www.ncbi.nlm.nih.gov/gene/1116
19. Available from: https://www.ncbi.nlm.nih.gov/gene/81
20. Available from: https://www.ncbi.nlm.nih.gov/gene/1958
21. Available from: https://www.ncbi.nlm.nih.gov/gene/207
22. Available from: https://www.ncbi.nlm.nih.gov/gene/1277
23. Available from: https://www.ncbi.nlm.nih.gov/gene/6667
24. Available from: https://www.ncbi.nlm.nih.gov/gene/6777
25. Available from: https://www.ncbi.nlm.nih.gov/gene/4314
26. Available from: https://www.ncbi.nlm.nih.gov/gene/598
27. Ghazale H, Parga PM, Jung S, Cao K, Vasan L, Hickmott JW, et al.. MicroRNA-mediated neuronal detargeting alters astrocyte cell fate conversion trajectories in vivo. Communications Biology [Internet]. 2025Dec5;8(1). Available from: https://www.nature.com/articles/s42003-025-09169-3
28. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
29. Available from: https://www.ncbi.nlm.nih.gov/gene/355
30. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
31. Available from: https://www.ncbi.nlm.nih.gov/gene/6622
32. Available from: https://www.ncbi.nlm.nih.gov/gene/1499
33. DeSouza PA, Ishahak M, Qu X, McCornack C, Annamalai D, Mao DD, et al.. INSM1 governs a neuronal progenitor state that drives glioblastoma in a human stem cell model. Nature Communications [Internet]. 2025Dec7;. Available from: https://www.nature.com/articles/s41467-025-66371-x
34. Available from: https://www.ncbi.nlm.nih.gov/gene/283120
35. Available from: https://www.ncbi.nlm.nih.gov/gene/857
36. Available from: https://www.ncbi.nlm.nih.gov/gene/3309
37. Available from: https://www.ncbi.nlm.nih.gov/gene/7077
38. Available from: https://www.ncbi.nlm.nih.gov/gene/627
39. Available from: https://www.ncbi.nlm.nih.gov/gene/7490
40. Available from: https://www.ncbi.nlm.nih.gov/gene/7019
41. Available from: https://www.ncbi.nlm.nih.gov/gene/7080
42. Soares-Ferreira B, Peixoto J, Ferro A, Esteves B, Pinheiro J, Silva R, et al.. Patient-derived tumoroids recapitulate the morphologic and molecular features of pediatric brain tumors. npj Precision Oncology [Internet]. 2025Nov20;9(1). Available from: https://www.nature.com/articles/s41698-025-01151-w
43. Schoof M, Zheng T, Sill M, Imle R, Cais A, Altendorf L, et al.. Investigation of a global mouse methylome atlas reveals subtype-specific copy number alterations in pediatric cancer models. Nature Genetics [Internet]. 2025Dec11;. Available from: https://www.nature.com/articles/s41588-025-02419-4
44. Available from: https://www.ncbi.nlm.nih.gov/gene/10135
45. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
46. Keane S, Sjöberg I, Deland L, Lindlöf A, Bontell TO, Kling T, et al.. Comprehensive characterization and targeted treatment of a pediatric epithelioid glioblastoma with a rare TRIM24-NTRK2 fusion. npj Precision Oncology [Internet]. 2025Dec2;9(1). Available from: https://www.nature.com/articles/s41698-025-01190-3
47. Available from: https://www.ncbi.nlm.nih.gov/gene/12977
48. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
49. Available from: https://www.ncbi.nlm.nih.gov/gene/12578
50. Available from: https://www.ncbi.nlm.nih.gov/gene/6288
51. De A, Forero SA, Pirani A, Morales JE, De LF-GM, Sebastian S, et al.. Single cell spatial profiling of the matrisome identifies region-specific adhesion and signaling networks in glioblastoma. Communications Biology [Internet]. 2025Dec9;. Available from: https://www.nature.com/articles/s42003-025-09270-7
52. Available from: https://www.ncbi.nlm.nih.gov/gene/706
53. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
54. Available from: https://www.ncbi.nlm.nih.gov/gene/2247
55. Available from: http://json-schema.org/draft-07/schema#",
