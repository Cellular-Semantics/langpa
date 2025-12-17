# Gene Program Markdown Report

## Context
- Cell type: Astrocytes, astrocytoma cells
- Disease: Astrocytoma
- Tissue: Brain

## Input Genes
AC004448.2, PIM3, MYL12A, NANS, NCBP2AS2, NLRC3, NR1D1, NUPR1, ODF3B, OSER1, OSGIN1, PELO, PLA2G4C, AC006449.6, PLCD1, PLIN2, PLIN3, PLXNB2, PMP22, PNRC1, POLR2K, PPP1R15A, PRKG1, PRSS3, MRPL50, ... (200 total)

## Program: Endoplasmic Reticulum Stress Response and Unfolded Protein Response
This program encompasses the cellular adaptive response to endoplasmic reticulum (ER) stress triggered by misfolded protein accumulation. The pathway includes DDIT3 (CHOP), ATF4, HERPUD1, heat shock proteins (HSPA1B, HSPA2, HSPE1), and PPP1R15A (GADD34). These genes coordinate the unfolded protein response through IRE1α-XBP1s, PERK-ATF4, and ATF6 branches. DDIT3 encodes CHOP, a transcription factor that controls both pro-survival and pro-death signaling during ER stress. HERPUD1 recruits ubiquitin ligases for ER-associated degradation of misfolded proteins. Heat shock proteins function as molecular chaperones facilitating protein refolding. PPP1R15A/GADD34 dephosphorylates eIF2α to allow translation reinitiation after stress-induced translational shutdown. This program is activated in response to hypoxia, nutrient deprivation, and oxidative stress characteristic of the astrocytoma microenvironment.

**Predicted impacts**
- Adaptive survival response enabling cell persistence during hypoxic and nutrient-deprived conditions
- Activation of IL-6 secretion through IRE1α-XBP1s pathway, contributing to immune suppression
- Prevention of protein aggregation and maintenance of proteostasis
- Potential shift toward pro-death signaling (apoptosis) if ER stress is prolonged or unresolved

**Evidence summary**
Recent studies demonstrate that tumor cells activate the IRE1α-XBP1s pathway in response to hypoxia and ER stress inducers. DDIT3/CHOP functions as a critical transcription factor controlling both pro-survival and pro-death genes. The search results indicate that ER stress inhibitors can suppress IL-6 secretion in tumor cells under hypoxic conditions, and that UPR-related marker genes are generally upregulated in non-small cell lung cancer, suggesting conserved ER stress activation across solid tumors including astrocytomas. The presence of multiple UPR components in the input gene list indicates active ER stress signaling in the astrocytoma context.

**Atomic biological processes**
- Unfolded protein response (UPR) initiation and signaling. Genes: ATF4, DDIT3, HSPA1B, HSPA2, HSPE1
  - [9]: Documents IRE1α-XBP1s pathway activation in response to hypoxia and ER stress inducers in tumor cells
  - [12]: Describes GRP78/IRE1/XBP1 pathway in ER stress response
- ER-associated protein degradation (ERAD). Genes: HERPUD1
  - [32]: HERPUD1 localizes to ER-derived quality control compartments and recruits ubiquitin ligases for ERAD
- Translational control during ER stress. Genes: PPP1R15A
  - [9]: PPP1R15A/GADD34 dephosphorylates eIF2α to restore translation after ER stress

**Atomic cellular components**
- Endoplasmic reticulum lumen and ER-derived quality control compartments. Genes: HSPA1B, HSPA2, HERPUD1
  - [12]: Describes localization of GRP78 and other ER-resident chaperones
- Ribosome and translation machinery. Genes: PPP1R15A
  - [9]: eIF2α phosphorylation blocks translation initiation during ER stress

**Required genes (not in input)**
- Genes: ERN1, XBP1, ATF6, PERK, HSPA5, GRP78
  - [9]: ERN1, XBP1, ATF6, and PERK are core UPR pathway components not present in input list but required for pathway function

**Program citations**
- [9]: Mechanistic insights into IL-6-mediated NK cell dysfunction demonstrate IRE1α-XBP1s pathway activation in tumor cells
- [12]: Heat shock proteins and ER stress pathways in cellular stress responses
- [32]: HERPUD1 and ER-associated protein degradation mechanisms

## Program: Inflammatory Cytokine and Immune Modulation
This program encompasses production and sensing of inflammatory cytokines and immune regulatory molecules within the tumor microenvironment. Key genes include TNFAIP6 (TNF-α-induced protein 6/TSG-6), TNFRSF12A (TNF receptor superfamily member 12A), IL32, S100A13, ANXA1 (annexin A1), ANXA2 (annexin A2), LGALS3 (galectin-3), and SOCS1 (suppressor of cytokine signaling 1). TNFAIP6/TSG-6 is induced by TNF-α and IL-1β and functions as an extracellular immunomodulator. S100A13 is a pan-reactive astrocyte marker upregulated following brain injury. Annexins function both as receptors for extracellular ATP and as anti-inflammatory lipid-binding proteins. LGALS3/galectin-3 functions in cell-cell interactions and pattern recognition. SOCS1 provides negative feedback on cytokine signaling. This program integrates with the ER stress program, as IRE1α-XBP1s pathway activity drives IL-6 secretion which suppresses NK cell function.

**Predicted impacts**
- Recruitment of infiltrating immune cells to tumor microenvironment
- Suppression of anti-tumor NK cell functionality through IL-6-mediated NKp30 downregulation
- Altered neuronal excitability in peritumoral regions through inflammatory mediators
- Production of soluble factors contributing to blood-brain barrier disruption and cerebral edema
- Negative feedback regulation limiting excessive inflammation while maintaining baseline immune activation

**Evidence summary**
Recent characterization of astrocyte transcriptomes following brain injury revealed prominent upregulation of pan-reactive astrocyte markers including S100A13, TNF-related genes, and inflammatory pathway components. In glioblastoma models, complement-activated cells show strong enrichment of inflammation-related genes and NF-κB signaling pathways. Mechanistically, tumor-cell-derived IL-6 suppresses NKp30 expression on tumor-infiltrating NK cells through ER stress-dependent IRE1α-XBP1s pathway activation, creating a link between the ER stress program and immune suppression. The presence of multiple inflammatory genes in the input list indicates sustained inflammatory signaling within the astrocytoma microenvironment.

**Atomic biological processes**
- TNF-α and IL-1β induced inflammatory signaling. Genes: TNFAIP6, TNFRSF12A, S100A13
  - [2]: Recent studies show upregulation of pan-reactive astrocyte markers and TNF-related genes in acute brain injury astrocytes
  - [33]: TNF encodes a multifunctional proinflammatory cytokine central to immune and inflammatory responses
- Anti-inflammatory and immunomodulatory signaling. Genes: ANXA1, ANXA2
  - [14]: ANXA1 encodes a membrane protein that inhibits phospholipase A2 and exhibits anti-inflammatory activity
- IL-6 mediated immune suppression and NK cell dysfunction. Genes: IL32
  - [9]: Tumor-derived IL-6 suppresses NKp30 expression on tumor-infiltrating NK cells, impairing anti-tumor immunity
- Negative feedback on cytokine signaling. Genes: SOCS1
  - [8]: SOCS1 downregulates NF-κB stability and activity under inflammatory signaling

**Atomic cellular components**
- Cell surface TNF receptors and cytokine receptors. Genes: TNFRSF12A
  - [23]: TNFRSF1A encodes a TNF receptor superfamily member found in membrane-bound and soluble forms
- Extracellular space and secreted factors. Genes: TNFAIP6, S100A13, IL32
  - [2]: TNFAIP6 and S100A13 are secreted factors functioning in the extracellular microenvironment
- Cell membrane and plasma membrane associated proteins. Genes: ANXA1, ANXA2, LGALS3
  - [14]: ANXA1 and ANXA2 are membrane-localized proteins binding phospholipids

**Required genes (not in input)**
- Genes: IL-6, TNF-α, IL-1β, NF-κB, IL-17, STAT3, IRF-family transcription factors
  - [2]: IL-6, TNF-α, and IL-1β are core inflammatory cytokines driving the inflammatory program, though some effects are mediated through genes in the input list

**Program citations**
- [2]: Astrocyte activation and inflammatory gene expression post-injury
- [9]: IL-6-mediated NK cell dysfunction and ER stress linkage
- [19]: Inflammatory transcriptomic signatures in glioblastoma
- [14]: ANXA1 anti-inflammatory functions

## Program: Metabolic Remodeling and Bioenergetic Adaptation
This program encompasses metabolic reprogramming essential for supporting the biosynthetic and bioenergetic demands of astrocytoma progression. Key genes include GDF15 (growth differentiation factor 15), HMOX1 (heme oxygenase 1), SULT1A1 (sulfotransferase family 1A member 1), PLIN2 and PLIN3 (perilipin proteins), ATP6V0D2 (vacuolar ATPase component), MGST1 (microsomal glutathione S-transferase 1), and metabolic support genes. GDF15 is a stress-responsive cytokine upregulated during metabolic perturbation and oxidative stress. HMOX1 catalyzes heme degradation to biliverdin and subsequently to bilirubin, an antioxidant, while participating in regulation of cellular energetics. PLIN2 and PLIN3 coat lipid droplet surfaces and regulate lipid mobilization, reflecting increased dependence on fatty acid metabolism for energy and biosynthetic precursors. ATP6V0D2 supports lysosomal acidification essential for autophagy-mediated nutrient recycling. This program interconnects with ER stress responses through provision of amino acids and energy during metabolic limitation.

**Predicted impacts**
- Enhanced energy production through fatty acid oxidation during glucose limitation
- Support of membrane biogenesis and organellar expansion during rapid proliferation through fatty acid synthesis
- Management of oxidative stress generated by high metabolic activity
- Efficient recycling of cellular components and nutrients through autophagy-mediated lysosomal degradation
- Enhanced clearance and metabolism of drugs and hormones potentially affecting chemotherapy efficacy and endocrine signaling

**Evidence summary**
Astrocytomas exhibit profound metabolic reprogramming compared to normal brain tissue. The search results document that enhanced fatty acid synthesis and oxidation are vital to tumorigenesis and drug resistance, with fatty acid oxidation serving as a critical energy pathway particularly under hypoxic conditions. HMOX1 upregulation is observed in pathological conditions including tumors and contributes to chemotherapy resistance. The presence of perilipin genes (PLIN2, PLIN3) suggests astrocytoma-derived cells utilize lipid droplet-mediated lipid storage as a metabolic strategy. GDF15 functions as a stress-responsive signal upregulated during metabolic perturbation. This program intersects with the ER stress program through production of amino acids during autophagy and with the inflammatory program through metabolic support of cytokine production.

**Atomic biological processes**
- Fatty acid synthesis and oxidation. Genes: PLIN2, PLIN3
  - [3]: Enhanced fatty acid synthesis and oxidation are vital to tumorigenesis, progression, and drug resistance. Fatty acid oxidation provides energy particularly under hypoxic or glucose-deprived conditions
- Oxidative stress management and antioxidant defense. Genes: HMOX1, GDF15
  - [27]: HMOX1 cleaves heme to form biliverdin and bilirubin, providing antioxidant defense while managing heme toxicity
- Lysosomal acidification and autophagy-mediated nutrient recycling. Genes: ATP6V0D2
  - [9]: Vacuolar ATPase mediates vesicular proton transport supporting lysosomal functions during metabolic stress
- Drug and hormone metabolism. Genes: SULT1A1
  - [26]: SULT1A1 catalyzes sulfate conjugation of hormones, neurotransmitters, drugs, and xenobiotics in cytosolic metabolism
- Metabolic stress signaling. Genes: GDF15
  - [10]: GDF15 is acute exercise-inducible and increases in response to metabolic stress and unfolded protein response

**Atomic cellular components**
- Lipid droplets. Genes: PLIN2, PLIN3
  - [3]: PLIN2 and PLIN3 coat lipid droplet surfaces regulating lipid storage and mobilization
- Endoplasmic reticulum membrane and associated systems. Genes: MGST1
  - [26]: MGST1 functions as a microsomal enzyme involved in detoxification processes on ER membranes
- Lysosomes and vacuolar compartments. Genes: ATP6V0D2
  - [9]: ATP6V0D2 is a core component of the vacuolar H+-ATPase essential for lysosomal acidification

**Required genes (not in input)**
- Genes: FASN, ACC, CPT1, ACSL, PGC1α, PPARA, PPARG
  - [3]: Fatty acid synthase (FASN), ACC, and other core metabolic enzymes are not in input list but regulate fatty acid synthesis and oxidation

**Program citations**
- [3]: JAB1/CRL4B complex regulates PPARG/ACSL5 and fatty acid metabolism in cancer progression
- [10]: GDF15 increases in response to metabolic stress and ER stress
- [26]: SULT1A1 role in drug and hormone metabolism
- [27]: HMOX1 in heme metabolism and antioxidant defense

## Program: Autophagy-Lysosomal Pathway and Proteostasis
This program encompasses autophagy-lysosomal pathway (ALP) components essential for lysosomal protein degradation, selective autophagy, and cellular proteostasis. Key genes include MAP1LC3B (microtubule-associated protein 1 light chain 3 beta), SQSTM1 (sequestosome 1/p62), and related autophagy-associated factors. MAP1LC3B, specifically its processed LC3-II form, localizes to autophagosomal membranes and participates in autophagosome formation and maturation. SQSTM1/p62 functions as an autophagic adapter protein recognizing ubiquitinated substrates and directing them to autophagosomes for selective degradation (aggrephagy, xenophagy). CTSL (cathepsin L) participates in lysosomal protein degradation. This program provides alternative energy sources during nutrient limitation, removes damaged organelles and misfolded proteins, and supports cell survival during metabolic stress. Autophagy flux is progressively induced in various pathological brain conditions.

**Predicted impacts**
- Increased survival during nutrient limitation through macroautophagy-mediated provision of amino acids and energy
- Removal of damaged mitochondria (mitophagy) reducing oxidative stress and ROS production
- Clearance of protein aggregates and misfolded proteins (aggrephagy) supporting proteostasis
- Selective destruction of intracellular pathogens and organelles (xenophagy) supporting immune responses
- Potential suppression or promotion of tumorigenesis depending on tumor stage and genetic context

**Evidence summary**
The autophagy-lysosomal pathway is progressively induced in various pathological brain conditions as cells experience proteostasis stress from multiple sources including ER stress, oxidative stress, and rapid proliferation. Recent multiomics studies identify autophagy-lysosomal pathway dysregulation as a prominent feature in polyglutamine expansion diseases. MAP1LC3B serves as the most widely used marker for monitoring autophagy flux, and SQSTM1/p62 functions as a critical cargo adapter in selective autophagy. The presence of both components in the input gene list indicates active autophagy signaling in astrocytoma cells. This program intersects with the ER stress program, as the UPR can trigger macroautophagy to provide amino acids during ER stress-induced metabolic limitation.

**Atomic biological processes**
- Autophagosome formation and maturation. Genes: MAP1LC3B
  - [24]: MAP1LC3B/LC3 directly participates in autophagosome formation and maturation as a core component of autophagosomal membranes
- Selective autophagy and cargo recognition. Genes: SQSTM1
  - [24]: SQSTM1/p62 acts as a selective autophagy receptor recognizing ubiquitinated substrates for degradation
- Lysosomal protein degradation. Genes: CTSL
  - [24]: Cathepsins S, Z, and L are prominently upregulated in pathological conditions and participate in lysosomal protein degradation

**Atomic cellular components**
- Autophagosomal membranes. Genes: MAP1LC3B
  - [24]: MAP1LC3B localizes specifically to autophagosomal membranes and serves as a marker for autophagy flux
- Lysosomes and lysosomal compartments. Genes: CTSL
  - [24]: Cathepsins localize to lysosomes and participate in proteolysis of autophagy substrates

**Required genes (not in input)**
- Genes: ATG proteins, WIPI proteins, Class III PI3K complex, Rab GTPases, SNARE proteins
  - [24]: Core autophagy machinery including ATG genes and PI3K complex components are required but not present in input list

**Program citations**
- [24]: Autophagy-lysosomal pathway factors and lysosomal cathepsins are progressively induced in pathological conditions

## Program: Signal Transduction and Cell Proliferation Control
This program encompasses signal transduction pathways controlling cell proliferation, survival, and differentiation. Key genes include PRKG1 (protein kinase G), MKNK2 (MAP kinase interacting serine/threonine kinase 2), PIM3 (Pim-3 proto-oncogene), PLCD1 and PLCD3 (phospholipase C delta isoforms), SPHK1 (sphingosine kinase 1), and S1PR1 (sphingosine 1-phosphate receptor 1). PRKG1 encodes a serine/threonine kinase activated by cyclic GMP signaling. MKNK2 phosphorylates eIF4E and regulates translation initiation in response to MAPK signaling. PIM3 functions as a proto-oncogene in hematopoietic malignancies. PLCD1 and PLCD3 hydrolyze PIP2 to generate IP3 and DAG, activating calcium signaling and protein kinase C. SPHK1 catalyzes phosphorylation of sphingosine to S1P, a lipid signaling molecule. S1PR1 is a G protein-coupled receptor through which S1P signals to regulate cell proliferation, survival, and cell junction stability.

**Predicted impacts**
- Enhanced translation of critical proliferation factors through MKNK2-mediated eIF4E phosphorylation
- Increased intracellular calcium signaling supporting cell proliferation and differentiation
- Enhanced cell survival signaling through multiple kinase pathways
- Altered cell junction stability and immune cell trafficking through S1PR1-mediated signaling
- Support of rapid cell cycle progression and proliferation despite stressful microenvironmental conditions

**Evidence summary**
Multiple signal transduction pathways are represented in the input list, collectively supporting sustained cell proliferation despite the stressful astrocytoma microenvironment. MKNK2 phosphorylates eIF4E in response to MAPK pathway activation, enhancing translation of proliferation-promoting factors. Phospholipase C isoforms generate IP3 and DAG, mobilizing intracellular calcium and activating protein kinase C. S1PR1 signaling has been implicated in cell proliferation and drug resistance in multiple myeloma, suggesting similar mechanisms in other malignancies including astrocytoma. The proto-oncogene PIM3 is known to promote proliferation and stemness in malignant cells. These pathways collectively drive sustained proliferation signaling.

**Atomic biological processes**
- Cyclic GMP-mediated signaling. Genes: PRKG1
  - [41]: CREB1 mediates cAMP-responsive signaling, related to cyclic nucleotide-dependent pathways
- MAPK signaling and translation regulation. Genes: MKNK2
  - [11]: MKNK2 and related kinases regulate MAPK pathway output through eIF4E phosphorylation affecting translation
- Phosphoinositide signaling and calcium mobilization. Genes: PLCD1, PLCD3
  - [40]: PLCD1 encodes phospholipase C delta that generates IP3 and DAG from PIP2
  - [42]: PLCD3 promotes cell behaviors through PI3K/AKT/P21 signaling in cancer
- Sphingosine 1-phosphate signaling and immune regulation. Genes: SPHK1, S1PR1
  - [17]: S1PR1 signaling plays roles in cell proliferation and drug resistance in multiple myeloma, with therapeutic targeting potential
- Proto-oncogene signaling in malignancy. Genes: PIM3
  - [45]: PIM3 is overexpressed in hematopoietic malignancies and promotes proliferation, invasion, and stemness

**Atomic cellular components**
- Plasma membrane and G protein-coupled receptors. Genes: S1PR1
  - [17]: S1PR1 is a G protein-coupled receptor localized to the plasma membrane
- Cytoplasmic signaling complexes and kinase cascades. Genes: PRKG1, MKNK2, PIM3
  - [11]: MKNK2 functions in MAPK signaling cascades
- Phosphoinositide pools in plasma membrane and intracellular membranes. Genes: PLCD1, PLCD3
  - [40]: PLCD1 substrate PIP2 localizes to various cellular membranes

**Required genes (not in input)**
- Genes: RAF, MEK, ERK1/2, mTORC1, AKT, GSK3β
  - [11]: Core MAPK pathway components are not in input list but are required for pathway function

**Program citations**
- [11]: MKNK2 and MAPK pathway signaling in translation control
- [17]: S1PR1 in cell proliferation and drug resistance
- [40]: PLCD1 phospholipase C signaling
- [42]: PLCD3 in PI3K/AKT pathway and cancer progression
- [45]: PIM3 proto-oncogene in malignancy

## Program: Circadian Rhythm Regulation and Time-Dependent Drug Sensitivity
This program encompasses circadian clock regulation with direct implications for chemotherapy sensitivity and DNA repair. The primary gene is NR1D1 (nuclear receptor subfamily 1 group D member 1), which encodes REV-ERBα, a nuclear receptor fundamental to circadian rhythm generation and metabolic regulation. NR1D1 also interacts with core tumor suppressor and DNA repair pathways. Recent evidence demonstrates that circadian clock genes including NR1D1, BMAL1, and PER2 function as diagnostic and prognostic biomarkers of glioma and directly regulate temozolomide (TMZ) sensitivity. NR1D1 recruitment to DNA damage sites inhibits PARP1 activity and is associated with chemosensitivity, indicating that circadian regulation of DNA repair mechanisms directly affects treatment efficacy. Pharmacological activation of REV-ERBs is lethal in cancer cells.

**Predicted impacts**
- Time-of-day dependent temozolomide sensitivity with implications for optimal treatment timing
- Altered DNA repair capacity through circadian regulation of PARP1 and other DNA repair enzymes
- Potential reversal of chemotherapy resistance through pharmacological REV-ERB activation
- Integration of circadian time-keeping with metabolic state, creating interdependence of circadian and metabolic programs
- Opportunities for personalized chronotherapy approaches based on individual circadian clock characteristics

**Evidence summary**
Recent evidence demonstrates that circadian clock genes, particularly NR1D1, directly regulate temozolomide sensitivity in glioblastoma through time-dependent changes in DNA repair mechanisms. Clock gene disruption reduces TMZ efficacy, while pharmacological activation of REV-ERBs is lethal in cancer cells, suggesting therapeutic potential. The circadian factor Period 2 modulates p53 stability and transcriptional activity, indicating intersection with core tumor suppressor pathways. NR1D1 recruitment to DNA damage sites inhibits PARP1 activity and is associated with altered chemosensitivity. These findings establish circadian clock regulation as a therapeutic target in gliomas.

**Atomic biological processes**
- Circadian rhythm generation and clock gene regulation. Genes: NR1D1
  - [38]: Circadian clock genes including NR1D1 regulate time-of-day dependent TMZ sensitivity in glioblastoma
  - [39]: NR1D1 encodes REV-ERBα with fundamental roles in circadian rhythm generation
- DNA repair and chemotherapy sensitivity. Genes: NR1D1
  - [38]: Clock gene disruption reduces TMZ efficacy through altered DNA repair regulation and changes in MGMT expression
  - [39]: NR1D1 recruitment to DNA damage sites inhibits PARP1 activity and affects chemosensitivity
- Metabolic regulation by circadian factors. Genes: NR1D1
  - [39]: NR1D1 couples circadian clock to metabolic pathways including steroidogenesis

**Atomic cellular components**
- Cell nucleus and transcriptional machinery. Genes: NR1D1
  - [39]: NR1D1 functions as a nuclear receptor localizing to the nucleus
- DNA damage response sites. Genes: NR1D1
  - [39]: NR1D1 recruits to sites of DNA damage to regulate PARP1 activity

**Required genes (not in input)**
- Genes: BMAL1, CLOCK, PER1, PER2, CRY1, CRY2, PARP1, MGMT
  - [38]: Core circadian clock components BMAL1, CLOCK, PER, and CRY proteins are required for circadian rhythm generation but not present in input list

**Program citations**
- [38]: Personalized chronotherapy in glioblastoma based on circadian clock gene expression
- [39]: NR1D1 and circadian regulation of DNA repair and metabolic processes

## Program: Extracellular Matrix Interactions and Cell Motility
This program encompasses cell-matrix adhesion and cytoskeletal organization controlling cell migration, invasion, and mechanotransduction. Key genes include ITGA5 (integrin alpha 5), ITGBL1 (integrin beta-like 1), SDC4 (syndecan 4), KRT10 (keratin 10), RHOC (Rho family small GTPase C), and LAMTOR5 (late endosomal/lysosomal adaptor MAPK and mTOR activator 5). ITGA5 heterodimerizes with integrin β1 to form the fibronectin receptor, activating focal adhesion kinase (FAK) and ERK pathways. SDC4 is a transmembrane heparan sulfate proteoglycan participating in cell adhesion and signaling. KRT10 encodes keratin 10, a cytoplasmic intermediate filament protein. RHOC is a master regulator of cytoskeletal organization controlling actin polymerization and stress fiber formation. LAMTOR5 localizes to lysosomal compartments and regulates mTORC1 signaling in response to amino acid availability, linking adhesion signals to metabolic sensing.

**Predicted impacts**
- Enhanced cell motility and invasion through integrin-FAK-ERK signaling in response to fibronectin matrix
- Increased mechanotransduction sensitivity allowing adaptation to changing microenvironmental stiffness
- Remodeling of cell-matrix contacts in response to tumor-associated extracellular matrix alterations
- Integration of adhesion signals with metabolic and proliferation pathways through mTORC1 signaling
- Support of tumor cell infiltration and peritumoral invasion essential for tumor progression
- Dynamic cytoskeletal rearrangement supporting migration and invasion phenotypes

**Evidence summary**
Cell-matrix adhesion and cytoskeletal organization programs are critical for astrocytoma cell invasion and migration. Recent characterization of nerve regeneration demonstrates that mechanical substrate stiffness exerts biphasic effects on cell phenotype: compliant matrices induce a repair phenotype (dedifferentiation), while rigid substrates promote specialized functions (redifferentiation). Tumor microenvironments are typically fibrotic and stiffened, suggesting that astrocytoma cells encounter rigid matrix promoting specialized functions. Integrin signaling through α5β1 activates FAK and downstream kinases controlling proliferation and survival. Syndecans participate in growth factor signaling and cell junction formation. Rho GTPases control actin dynamics essential for cell morphology and migration. LAMTOR5-mediated mTORC1 regulation links amino acid sensing to proliferation signals.

**Atomic biological processes**
- Integrin-mediated cell-matrix adhesion and signaling. Genes: ITGA5, ITGBL1
  - [25]: Integrin signaling through α5β1 activates focal adhesion kinase (FAK) and downstream signaling, transmitting extracellular matrix signals into cells
- Syndecane-mediated cell adhesion and growth factor signaling. Genes: SDC4
  - [25]: Syndecans bind extracellular ligands including growth factors and matrix components, transducing signals through cytoplasmic tails
- Rho GTPase-mediated cytoskeletal reorganization. Genes: RHOC
  - [25]: Rho GTPases cycle between inactive GDP-bound and active GTP-bound states, controlling actin polymerization and stress fiber formation
- Mechanical substrate stiffness sensing. Genes: RHOC, LAMTOR5
  - [25]: Substrate stiffness exerts biphasic effects on cell phenotypic regulation through mechanotransduction, with compliant matrices inducing dedifferentiation and rigid substrates promoting redifferentiation
- mTORC1 signaling in response to amino acid availability and growth signals. Genes: LAMTOR5
  - [25]: LAMTOR5 component of GATOR1 complex regulates mTORC1 signaling at lysosomes in response to amino acid levels

**Atomic cellular components**
- Focal adhesion complexes. Genes: ITGA5, ITGBL1
  - [25]: Integrin-mediated signaling establishes focal adhesion complexes containing FAK and related proteins
- Cell membrane and transmembrane proteins. Genes: ITGA5, ITGBL1, SDC4
  - [25]: ITGA5, ITGBL1, and SDC4 are transmembrane proteins mediating cell-matrix interactions
- Cytoskeletal actin filaments and stress fibers. Genes: RHOC, KRT10
  - [25]: RHOC regulates actin polymerization to control stress fiber formation and cell morphology
- Lysosomal surface and late endosomal membranes. Genes: LAMTOR5
  - [25]: LAMTOR5 localizes to late endosomal and lysosomal membranes as a component of GATOR1 complex

**Required genes (not in input)**
- Genes: ITGB1, FAK, SRC, PAK, CDC42, RAC1, ROCK
  - [25]: Core focal adhesion kinase, Rho GTPase effectors, and downstream signaling molecules are not present in input list but are required for pathway function

**Program citations**
- [25]: Comprehensive review of Schwann cell behavior, ECM interactions, and mechanotransduction relevant to cell-matrix interactions in various cell types

## Program: Reactive Astrocyte Activation and Pro-Inflammatory Phenotype
This program encompasses genes encoding markers of reactive astrocyte activation and glial differentiation states. Key genes include reactive astrocyte markers (TNFAIP6, S100A13, ANXA1, ANXA2), cell identity factors (ID3), histone variants, and heat shock proteins reflecting glial activation. Recent studies of astrocytes following traumatic brain injury reveal that both acute and chronic phases of injury involve distinct transcriptomic programs characterized by upregulation of pan-reactive astrocyte markers. ID3 (inhibitor of differentiation 3) is a helix-loop-helix transcription factor regulating cell differentiation and identity decisions, controlling the balance between stem-like and differentiated glial states. Multiple histone variants (H1F0, H3F3B, and core histones) reflect altered chromatin structure during glial activation. Heat shock proteins (HSPA1B, HSPA2, HSPB8, HSPE1) indicate elevated proteostasis stress and active protein quality control. This program represents a distinct glial activation state characterized by production of soluble mediators and sustained surveillance of the microenvironment.

**Predicted impacts**
- Sustained state of glial activation characterized by production of inflammatory mediators
- Recruitment and retention of infiltrating immune cells in tumor microenvironment
- Production of soluble factors modulating tumor cell behavior and peritumoral neuronal physiology
- Altered glial differentiation state with reduced capacity for normal homeostatic functions
- Active chromatin remodeling enabling rapid transcriptional responses to microenvironmental cues
- Enhanced protein quality control managing stress from activated state

**Evidence summary**
Recent characterization of astrocyte transcriptomes reveals distinct glial activation states characterized by prominent expression of pan-reactive astrocyte markers. Following traumatic brain injury, acute phase astrocytes express elevated levels of GFAP, CD44, SERPINA3N, CXCL10, and S100 family proteins, establishing a conserved injury response. These markers are associated with enhanced inflammatory and stress-related pathway signaling. The presence of ID3 and multiple histone genes suggests active cell identity remodeling during glial activation. Heat shock protein upregulation indicates heightened proteostasis stress during the activated state. This program overlaps significantly with the inflammatory program, indicating that reactive astrocyte activation and inflammatory signaling are intimately connected mechanisms driving neuroinflammation in the astrocytoma microenvironment.

**Atomic biological processes**
- Pan-reactive astrocyte marker expression. Genes: S100A13, TNFAIP6, ANXA1, ANXA2
  - [2]: Recent studies reveal prominent upregulation of pan-reactive astrocyte markers (e.g., GFAP, CD44, S100 proteins) in acute brain injury astrocytes with conserved injury responses across different pathologies
- Cell identity and differentiation control. Genes: ID3
  - [46]: ID3 regulates cell differentiation and identity decisions in various cell types including glial cells
- Chromatin remodeling and histone variant expression. Genes: H1F0, H3F3B, HIST1H2AE, HIST1H2BD, HIST1H2BF, HIST1H2BG, HIST1H2BJ, HIST1H3J, HIST1H4H, HIST2H2BE, HIST3H2A
  - [2]: Astrocyte activation involves altered chromatin structure reflecting dynamic epigenetic reprogramming
- Heat shock response and proteostasis. Genes: HSPA1B, HSPA2, HSPB8, HSPE1
  - [2]: Upregulation of heat shock proteins in astrocytes reflects protein quality control response to stress

**Atomic cellular components**
- Cell membrane and extracellular space. Genes: S100A13, ANXA1, ANXA2
  - [2]: Reactive astrocyte markers include cell surface proteins and secreted factors in extracellular space
- Chromatin and nucleus. Genes: ID3, H1F0, H3F3B, HIST1H2AE, HIST1H2BD, HIST1H2BF, HIST1H2BG, HIST1H2BJ, HIST1H3J, HIST1H4H, HIST2H2BE, HIST3H2A
  - [46]: Histone variants and ID3 transcription factor localize to chromatin and nuclear compartments
- Cytoplasm and protein quality control compartments. Genes: HSPA1B, HSPA2, HSPB8, HSPE1
  - [2]: Heat shock proteins function in cytoplasm and associated compartments for proteostasis

**Required genes (not in input)**
- Genes: GFAP, CD44, APOE, SERPINA3N, CXCL10, TIMP3
  - [2]: Core pan-reactive astrocyte markers including GFAP and CD44 are not present in input list but are characteristic of reactive glial phenotypes

**Program citations**
- [2]: Astrocyte activation persists one year after traumatic brain injury with distinct transcriptomic signatures of reactive phenotypes
- [46]: Type 2 DORCs associated with immune processes and transcriptional regulation of glial responses

## Program: Histone Modification and Epigenetic Regulation
This program encompasses histone-modifying enzymes and chromatin regulatory factors controlling epigenetic gene regulation and transcriptional responses. Key genes include HDAC2 (histone deacetylase 2), multiple histone variants, and histone acetyltransferase-related factors. HDAC2 belongs to the family of histone deacetylases that remove acetyl groups from histone and non-histone proteins, thereby regulating transcription through chromatin compaction and accessibility changes. HDAC2 acts through the formation of large multiprotein complexes that repress transcription of target genes. Histone deacetylase inhibitors have emerged as potential therapeutic agents in glioblastoma, suggesting that HDAC2-mediated epigenetic repression contributes to tumor maintenance. Circadian regulation may intersect with histone modification, as HDAC2 has been linked to circadian rhythm regulation. The collective histone gene expression in the input list (multiple histone variants) suggests active chromatin remodeling and altered nucleosome organization in the astrocytoma context.

**Predicted impacts**
- Dynamic epigenetic regulation permitting rapid transcriptional responses to microenvironmental cues
- Stable silencing of genes opposing tumor progression through histone deacetylation and chromatin compaction
- Altered histone isoform usage changing chromatin properties and accessibility
- Circadian-dependent epigenetic regulation of DNA repair and chemotherapy sensitivity genes
- Potential therapeutic vulnerability through histone deacetylase inhibitor treatment
- Maintenance of altered transcriptional programs during rapid cell division through histone synthesis and variant incorporation

**Evidence summary**
Histone deacetylase inhibitors have emerged as potential therapeutic agents in glioblastoma, suggesting that histone deacetylation contributes to tumor maintenance through epigenetic silencing of tumor suppressors or other growth-inhibitory genes. HDAC2 specifically has been linked to circadian rhythm regulation, establishing a connection between epigenetic and circadian programs. The presence of multiple histone variant genes in the input list suggests active histone synthesis and variant isoform incorporation during rapid proliferation. Epigenetic regulation through histone modification represents a mechanism for maintaining stable expression of tumor-promoting genes while retaining plasticity to respond to acute microenvironmental changes.

**Atomic biological processes**
- Histone deacetylation and chromatin compaction. Genes: HDAC2
  - [37]: HDAC2 removes acetyl groups from histones, promoting chromatin compaction and transcriptional repression
- Circadian-epigenetic coupling. Genes: HDAC2
  - [37]: HDAC2 has been linked to circadian rhythm regulation, suggesting integration of circadian and epigenetic programs
- Chromatin remodeling and nucleosome organization. Genes: H1F0, H3F3B, HIST1H2AE, HIST1H2BD, HIST1H2BF, HIST1H2BG, HIST1H2BJ, HIST1H3J, HIST1H4H, HIST2H2BE, HIST3H2A
  - [37]: Histone variants and chromatin-remodeling complexes alter nucleosome organization and chromatin accessibility

**Atomic cellular components**
- Chromatin and nucleosomes. Genes: HDAC2, H1F0, H3F3B, HIST1H2AE, HIST1H2BD, HIST1H2BF, HIST1H2BG, HIST1H2BJ, HIST1H3J, HIST1H4H, HIST2H2BE, HIST3H2A
  - [37]: HDAC2 and histone variants localize to chromatin and regulate nucleosome structure
- Histone deacetylase complexes. Genes: HDAC2
  - [37]: HDAC2 functions as part of large multiprotein complexes regulating transcription

**Required genes (not in input)**
- Genes: HAT proteins, Chromatin remodeling complexes, Corepressor proteins
  - [37]: Histone acetyltransferases and chromatin-remodeling complexes are not present in input list but are required for full epigenetic regulation

**Program citations**
- [37]: HDAC2 histone deacetylase family member in chromatin regulation and epigenetic control

## Bibliography
1. Available from: https://www.ncbi.nlm.nih.gov/gene/57670
2. Abou-El-Hassan H, Yahya T, Zusman BE, Albastaki O, Imkamp HT, Ye JJ, et al.. Astrocyte activation persists one year after TBI: a dynamic shift from inflammation to neurodegeneration. Communications Biology [Internet]. 2025Dec4;8(1). Available from: https://www.nature.com/articles/s42003-025-09138-w
3. Hu T, Ma T, Huo M, Liu J, Zhang D, Li Y, et al.. JAB1/CRL4B complex represses PPARG/ACSL5 expression to promote breast tumorigenesis. Cell Death &amp; Differentiation [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41418-025-01642-0
4. Available from: https://www.ncbi.nlm.nih.gov/gene/2735
5. Available from: https://www.ncbi.nlm.nih.gov/gene/7098
6. Available from: https://www.ncbi.nlm.nih.gov/gene/4613
7. Available from: https://www.ncbi.nlm.nih.gov/gene/114548
8. Available from: https://www.ncbi.nlm.nih.gov/gene/4790
9. Wang Y, Guo Z, Xu A, Fu Z, Hou Y, Tang K, et al.. Mechanistic insights into IL-6-mediated NK cell dysfunction in NSCLC via the IRE1α-XBP1s-STAT3-UBE2S axis. npj Precision Oncology [Internet]. 2025Nov18;9(1). Available from: https://www.nature.com/articles/s41698-025-01140-z
10. Available from: https://www.ncbi.nlm.nih.gov/gene/9518
11. Available from: https://www.ncbi.nlm.nih.gov/gene/5594
12. Available from: https://www.ncbi.nlm.nih.gov/gene/14828
13. Available from: https://www.ncbi.nlm.nih.gov/gene/23886
14. Available from: https://www.ncbi.nlm.nih.gov/gene/301
15. Available from: https://www.ncbi.nlm.nih.gov/gene/19225
16. Available from: https://www.ncbi.nlm.nih.gov/gene/13609
17. Available from: https://www.ncbi.nlm.nih.gov/gene/1901
18. Available from: https://www.ncbi.nlm.nih.gov/gene/1029
19. Brandl S, Yu Q, Hagenbuchner J, Endmayr V, Höftberger R, Bradl M, et al.. Inflammatory transcriptomic signatures in a human cellular NMOSD model reveal upregulation of NF-κB and IL6 pathways. Scientific Reports [Internet]. 2025Dec8;15(1). Available from: https://www.nature.com/articles/s41598-025-27335-9
20. Available from: http://connect.biorxiv.org/archive/index.php?dt
21. Available from: https://www.ncbi.nlm.nih.gov/gene/1030
22. Available from: https://www.ncbi.nlm.nih.gov/gene/1052
23. Available from: https://www.ncbi.nlm.nih.gov/gene/21937
24. Almaguer-Mederos LE, Key J, Sen N-E, Canet-Pons J, Döring C, Meierhofer D, et al.. Multiomics approach identifies SERPINB1 as candidate biomarker for spinocerebellar ataxia type 2. Scientific Reports [Internet]. 2025Nov26;15(1). Available from: https://www.nature.com/articles/s41598-025-29070-7
25. Yang K, Yang S, Teng X, He X, Sun T, Chen H. Modulating Schwann cell behavior via functional nerve guidance conduits for enhanced peripheral nerve regeneration. npj Regenerative Medicine [Internet]. 2025Nov26;10(1). Available from: https://www.nature.com/articles/s41536-025-00443-w
26. Available from: https://www.ncbi.nlm.nih.gov/gene/6817
27. Available from: https://www.ncbi.nlm.nih.gov/gene/3162
28. Available from: https://www.ncbi.nlm.nih.gov/gene/4780
29. Available from: https://www.ncbi.nlm.nih.gov/gene/546
30. Available from: https://www.ncbi.nlm.nih.gov/gene/64209
31. Available from: https://www.ncbi.nlm.nih.gov/gene/7124
32. Available from: https://www.ncbi.nlm.nih.gov/gene/21926
33. Available from: https://www.ncbi.nlm.nih.gov/gene/406991
34. Available from: https://www.ncbi.nlm.nih.gov/gene/3066
35. Nelson N, Zimmer O, Relógio A. Personalized chronotherapy in glioblastoma: integrating circadian profiling and PK–PD modelling to optimize temozolomide timing. npj Precision Oncology [Internet]. 2025Dec12;. Available from: https://www.nature.com/articles/s41698-025-01205-z
36. Available from: https://www.ncbi.nlm.nih.gov/gene/9572
37. Available from: https://www.ncbi.nlm.nih.gov/gene/5333
38. Available from: https://www.ncbi.nlm.nih.gov/gene/1385
39. Available from: https://www.ncbi.nlm.nih.gov/gene/113026
40. Available from: https://www.ncbi.nlm.nih.gov/gene/29126
41. Available from: https://www.ncbi.nlm.nih.gov/gene/5524
42. Available from: https://www.ncbi.nlm.nih.gov/gene/415116
43. Zheng C, Hervé B, Meijer M, Rubio R-KLA, Guerreiro CAO, Kukanja P, et al.. Distinct transcriptomic and epigenomic responses of mature oligodendrocytes during disease progression in a mouse model of multiple sclerosis. Nature Neuroscience [Internet]. 2025Nov17;28(12). Available from: https://www.nature.com/articles/s41593-025-02100-3
44. Available from: https://www.ncbi.nlm.nih.gov/gene/5292
45. Available from: https://www.ncbi.nlm.nih.gov/gene/16189
46. Available from: https://www.ncbi.nlm.nih.gov/gene/4869
47. Bouwen BLJ, Bolleboom A, Tang Y, Yu Z, van der SA, van RJA, et al.. Aberrant neural activity in the peritumoral cortex underlies the progression of tumor-associated seizures. Nature Communications [Internet]. 2025Dec2;16(1). Available from: https://www.nature.com/articles/s41467-025-66226-5
48. Available from: https://www.ncbi.nlm.nih.gov/gene/7015
49. Available from: https://www.ncbi.nlm.nih.gov/gene/2670
50. Available from: https://www.ncbi.nlm.nih.gov/gene/6663
51. Available from: https://www.ncbi.nlm.nih.gov/gene/8842
52. Available from: https://www.ncbi.nlm.nih.gov/gene/24387
53. Available from: https://www.ncbi.nlm.nih.gov/gene/17172
