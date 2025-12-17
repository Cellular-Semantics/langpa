# Gene Program Markdown Report

## Context
- Cell type: malignant glioblastoma cells
- Disease: glioblastoma multiforme (GBM)
- Tissue: brain

## Input Genes
GRIN3A, CUX2, LINC02144, LINC00639, CACNA2D3, DLX6-AS1, SYT1, OLFM3, TOX, THRB, SLAIN1, GABRB2, PLCB1, HRK, NYAP2, LINC00581, AL009178.3, MAML3, SLC17A6, LYPD6B, LRTM1, CARMIL1, CNTN2, EBF3, INSYN2B, ... (159 total)

## Program: Terminal Neuronal Differentiation Blockade
This program encompasses transcriptional and post-transcriptional factors that normally drive neuronal terminal differentiation and maturation. In GBM, systematic loss or repression of these factors prevents transition from progenitor to mature neuronal phenotype, enabling continued proliferation. Key transcription factors (EBF3, EBF1, MYT1L, RBFOX3) and post-transcriptional regulators (CELF4, SRRM4, RBFOX1) coordinate alternative splicing and translation of neuronal genes. Loss of these programs is particularly notable as EBF3 is inactivated through deletion or hypermethylation in 50-90% of high-grade gliomas.

**Predicted impacts**
- Maintenance of proliferative capacity through suppression of terminal differentiation programs
- Retention of neural progenitor-like gene expression patterns enabling continued cell cycle entry
- Loss of synaptic maturation markers and structural specialization
- Reduced expression of differentiation-dependent apoptotic pathways
- Enhanced capacity for migration and invasion relative to differentiated neurons

**Evidence summary**
Terminal neuronal differentiation involves coordinated transcriptional and post-transcriptional changes that shift cells from proliferative to post-mitotic phenotypes. In normal brain development, EBF3, EBF1, MYT1L and RBFOX proteins drive neuronal maturation through activation of differentiation-specific genes and repression of proliferative and stemness programs. In glioblastoma, these differentiation-promoting factors are frequently inactivated. EBF3 is deleted or hypermethylated in 50-90% of high-grade gliomas, representing one of the most frequent inactivated genes in GBM. MYT1/MYT1L re-expression in GBM cell lines dramatically reduces proliferation and activates neuronal differentiation programs. RBFOX1 and RBFOX3 are critical regulators of adult neurogenesis and control mRNA stability and translation of neuronal genes including those encoding synaptic proteins. CELF4, expressed in developing cortical neurons, controls translational repression of synaptic protein mRNAs during synaptogenesis. The systematic loss of this program in GBM enables the maintenance of a proliferative, undifferentiated state while suppressing the post-mitotic, specialized phenotypes characteristic of mature neurons.

**Atomic biological processes**
- neuronal lineage commitment and specification. Genes: EBF3, EBF1, ARX, DLX6, UNCX, PRDM8
  - [11]: EBF family members are essential regulators of neuronal differentiation; EBF3 inactivation blocks differentiation and contributes to tumorigenesis
  - [2]: Pax6 and downstream transcriptional networks regulate neurogenic fate determination in developing and adult neurogenesis
- alternative splicing and post-transcriptional control of neuronal genes. Genes: RBFOX3, RBFOX1, CELF4, SRRM4
  - [3]: RBFOX1 and RBFOX3 control post-transcriptional programs during neurogenesis through splicing, mRNA stability, and translation regulation of neuronal maturation genes
  - [30]: CELF4 translationally represses mRNAs encoding synaptic proteins during prenatal neuronal development
- repression of proliferative and epithelial-mesenchymal transition gene programs. Genes: MYT1L, EBF3, EBF1
  - [20]: MYT1 and MYT1L expression reduces proliferation in GBM cell lines and activates neuronal differentiation programs while repressing YAP1

**Atomic cellular components**
- RNA binding proteins regulating splicing and mRNA processing. Genes: RBFOX1, RBFOX3, CELF4, SRRM4
  - [3]: RBFOX proteins are neuronal-specific RNA binding proteins that regulate alternative splicing of genes critical for neuronal function
- transcriptional regulatory complexes driving neuronal fate. Genes: EBF3, EBF1, MEIS2, PBX3, PKNOX2
  - [11]: EBF family members function as lineage-specific transcription factors essential for neuronal differentiation

**Required genes (not in input)**
- Genes: NEUN, NeuroD1, NeuroD2, NeuroD4, NeuroD6, Neurogenin1, Neurogenin2, Neurogenin3, Ascl1, Math1, Brn3a, Brn3b
  - [11]: Multiple transcription factors work together with EBF family to drive neuronal differentiation
  - [2]: Comprehensive neurogenic transcription factor networks operate during both embryonic and adult neurogenesis

**Program citations**
- [11]: Comprehensive review of EBF family tumor suppressor functions; EBF3 inactivation in 50-90% of GBMs represents major differentiation blockade
- [20]: Experimental evidence that Myt1/Myt1l re-expression reduces GBM proliferation and activates neuronal differentiation
- [3]: Detailed mechanisms of RBFOX control of post-transcriptional programs in neuronal differentiation and maturation
- [30]: CELF4 controls translation of synaptic proteins during prenatal cortical development

## Program: GABAergic Synaptic Tumor Promotion
This program represents a unique tumor-promoting mechanism where GABAergic neurons form functional synapses with GBM cells, particularly in diffuse midline gliomas (DMGs) with H3K27M mutation. GABAergic input through GABA-A receptors produces depolarizing rather than hyperpolarizing currents in GBM cells due to elevated intracellular chloride maintained by NKCC1 transporter. This unusual depolarizing GABA signaling drives tumor cell proliferation and survival. The program includes synaptic vesicle proteins, neurotransmitter transporters, GABA receptors, and the chloride transporter NKCC1 that enables the depolarizing phenotype.

**Predicted impacts**
- Increased intracellular calcium flux through depolarization-activated voltage-gated calcium channels
- Activation of calcium-dependent growth and survival signaling pathways
- Enhanced proliferation and reduced apoptosis in response to GABAergic input
- Increased tumor growth in regions with high GABAergic neuron density
- GABA-A antagonists (e.g., lorazepam) reduce DMG tumor growth and proliferation
- Depolarizing GABA distinguishes H3K27M-DMG from hemispheric high-grade gliomas lacking NKCC1 depolarizing function

**Evidence summary**
Recent studies identified a remarkable tumor-promoting mechanism specific to H3K27M-mutated diffuse midline gliomas (DMGs) in which GABAergic neurons form functional, growth-promoting synapses with glioma cells. Using patch-clamp electrophysiology, in vivo optogenetics, and patient-derived orthotopic xenografts, researchers demonstrated that GABAergic input produces depolarizing currents in DMG cells via GABA-A receptors. This depolarization, unusual in neurons where GABA typically hyperpolarizes, results from elevated intracellular chloride in DMG cells maintained by the NKCC1 chloride-sodium-potassium cotransporter. This depolarizing GABAergic signaling promotes DMG cell proliferation and tumorigenicity. GABAergic synapse-related gene expression is enriched in all malignant cellular compartments of H3K27M-DMGs and particularly enriched in oligodendrocyte precursor cell-like compartments. Pharmacological GABA-A inhibition with lorazepam dose-dependently reduced DMG xenograft proliferation and survival. In contrast, hemispheric high-grade glioblastomas lacking H3K27M and NKCC1-mediated depolarization showed minimal GABAergic currents and were unresponsive to GABA-A inhibition. This tumor subtype-specific mechanism reveals an unexpected vulnerability of a particular glioma subset to neuron-derived signals.

**Atomic biological processes**
- GABAergic neurotransmitter synthesis and vesicular packaging. Genes: SLC18A1
  - [4]: GABAergic neurons form functional neuron-to-glioma synapses with DMG cells expressing GABRG2 (GABA-A receptor subunit)
- synaptic vesicle release and calcium-dependent exocytosis. Genes: SYT1, SYT4, SV2B, SYNPR
  - [5]: SV2B regulates presynaptic calcium levels and synaptic vesicle dynamics, critical for neurotransmitter release
- GABA-A receptor-mediated ionotropic signaling. Genes: GABRB2, GABRA1
  - [4]: H3K27M-altered DMG cells express functional GABA-A receptors (GABRB2, GABRG2) that mediate depolarizing GABAergic currents via NKCC1-driven chloride accumulation
- chloride homeostasis and NKCC1-dependent depolarization.
  - [4]: NKCC1 function is critical for the depolarizing effect of GABA in DMG cells; blocking NKCC1 with bumetanide reverses the depolarizing GABA response
- glutamatergic synaptic transmission in parallel with GABAergic input. Genes: GRIN3A, SLC17A6, PLCB1
  - [4]: Both GABAergic and glutamatergic neurons form synapses onto DMG cells; NMDA and AMPA receptors detected on some DMG cell populations

**Atomic cellular components**
- presynaptic terminal containing synaptic vesicles and release machinery. Genes: SYT1, SYT4, SV2B, SYNPR
  - [5]: SV2 proteins are integral to synaptic vesicle dynamics and calcium-dependent release machinery
- postsynaptic GABA-A receptor complex in glioma cells. Genes: GABRB2, GABRA1
  - [4]: Electron microscopy identified GFP-tagged GABRG2 in postsynaptic glioma membranes opposing presynaptic neuronal terminals

**Required genes (not in input)**
- Genes: NKCC1, SLC12A2, KCC2, SLC12A5, GABRG2, GAD1, GAD2, VGAT, SLC32A1, ChAT, NMDAR, AMPAR
  - [4]: NKCC1 is the critical chloride transporter enabling depolarizing GABAergic currents in DMG cells; GAD enzymes produce GABA; GABRG2 detected on glioma cells

**Program citations**
- [4]: Comprehensive characterization of GABAergic neuron-to-glioma synapses in H3K27M-DMGs with functional electrophysiology and in vivo validation
- [34]: WNK kinases regulate NKCC1 function and chloride balance with implications for cancer cell signaling and pain pathways

## Program: Axon Guidance & Cell Adhesion Dysregulation
This program encompasses the classical axon guidance molecules and cell adhesion molecules that normally establish correct neuronal connectivity and cell-cell contacts during brain development. These genes regulate repulsive and attractive interactions between neurons and guide axonal pathfinding. In GBM, altered expression of these molecules disrupts normal adhesive properties and enables aberrant cell migration and invasion. Eph receptors and their ephrin ligands regulate bidirectional signaling that sculpts developing axons and dendrites. Robo receptors bind Slit ligands to mediate repulsive guidance. Cadherins maintain homophilic cell-cell adhesion. In GBM, loss or alteration of adhesion molecules enables enhanced motility and invasion through tissue.

**Predicted impacts**
- Reduced adhesion between glioma cells enabling dissociation and migration
- Altered axon-like cellular processes affecting glioma cell morphology and directionality
- Increased invasiveness through suppressed cell-matrix and cell-cell adhesion mechanisms
- Dysregulated responses to repulsive guidance cues that normally confine cells
- Enhanced motility through disrupted cadherin-based contact inhibition
- Altered signaling downstream of Eph and Robo receptors affecting cytoskeletal dynamics

**Evidence summary**
Axon guidance and cell adhesion molecules are fundamental to establishing proper brain architecture by directing neuronal processes and maintaining appropriate cell-cell contacts. During development, Eph receptors and ephrin ligands establish repulsive gradients that guide axons to correct targets. Ephrin-B reverse signaling is particularly important for presynaptic development and shaft synapse formation. Robo receptors bind Slit ligands to mediate repulsive guidance. Cadherins maintain homophilic cell-cell adhesion crucial for proper connectivity. Contactins and other adhesion molecules facilitate neuronal cell-to-cell communication. In glioblastoma, downregulation or alteration of these adhesion and guidance molecules is associated with increased motility and invasiveness. Loss of cadherin-mediated adhesion reduces contact inhibition. Altered Eph and Robo signaling disrupts the cytoskeletal responses that normally restrain cell movement. The presence of multiple adhesion and guidance molecules in this gene set suggests that GBM exploits dysregulation of these developmental pathways to enhance migratory capacity. ECM stiffening further conditions GBM cells for enhanced invasion and migration through changes in mechanotransduction.

**Atomic biological processes**
- Ephrin-A reverse signaling in axon guidance and topographic mapping. Genes: EPHA3, EPHA5, EPHA7
  - [9]: Ephrin-A mediates reverse signaling in retinal ganglion cell axons to control axon branching and pathfinding through interactions with neurotrophin receptors
- Ephrin-B reverse signaling in presynaptic development and synapse formation. Genes: EPHA3, EPHA5, EPHA7
  - [9]: Ephrin-B reverse signaling regulates synapse formation in cultured neurons and plays essential roles in shaft synapse formation through PDZ interactions
- Robo-Slit repulsive axon guidance signaling. Genes: ROBO3, SLIT1
  - [10]: Slits bind to Robo receptors to induce repulsive signaling during axon guidance and neuronal migration
- Cadherin-mediated homophilic cell-cell adhesion. Genes: CDH4, CDH12, CDH18, CDH22
  - [7]: Cadherins are calcium-dependent cell adhesion molecules critical for proper brain development and establishing correct neuronal connectivity
- Contactin-mediated neuronal cell adhesion and neurite outgrowth. Genes: CNTN2, CNTNAP5
  - [7]: Contactins (CNTN) mediate cell-to-cell communication and are involved in neuronal connectivity
- Fibronectin-leucine-rich repeat interactions in axon guidance. Genes: FLRT2, MDGA2, LRTM1
  - [9]: Fibronectin-containing proteins interact with receptor tyrosine kinases and integrins to regulate axon pathfinding

**Atomic cellular components**
- Eph receptor tyrosine kinases for forward signaling. Genes: EPHA3, EPHA5, EPHA7
  - [9]: EphA receptors transduce forward signals through their intracellular kinase domains in response to ephrin binding
- Cell adhesion molecule complexes at synaptic and non-synaptic sites. Genes: CDH4, CDH12, CDH18, CDH22, CNTN2, CNTNAP5, FLRT2
  - [7]: CAMs organize into functional complexes that mediate cell-to-cell communication, signal transduction, and proper arrangement of synaptic structures
- Roundabout and Slit ligand receptor-ligand pairs. Genes: ROBO3, SLIT1
  - [10]: Robo receptors form signaling complexes upon Slit ligand binding to trigger repulsive axonal guidance

**Required genes (not in input)**
- Genes: EFNA, EFNB, SLIT2, SLIT3, ROBO1, ROBO2, CDH1, CDH3, CDH5, CDH6, CDH7, CDH8, CDH9, CDH10, CTNND1, CTNND2, CTNNB1, Integrin family, Nectin family
  - [9]: Ephrin-A and Ephrin-B ligands are required for forward signaling in eph-expressing cells
  - [7]: Extended family of cadherins and associated proteins necessary for complete cell adhesion networks

**Program citations**
- [9]: Comprehensive review of ephrin reverse signaling in axon guidance and synaptogenesis
- [10]: Overview of Slit-Robo repulsive axon guidance signaling
- [7]: Comprehensive annotated functional classification of human cell adhesion molecules and their roles in brain development
- [25]: ECM stiffness conditions GBM cells for invasion

## Program: Vascular Growth Factor Signaling & Angiogenesis
This program encompasses receptor tyrosine kinases and their ligands that promote angiogenesis and vascular growth. NRP1 (neuropilin-1) is a VEGF co-receptor that enhances VEGF-165 binding to VEGFR2, amplifying angiogenic signaling. FGFR2 mediates fibroblast growth factor signaling important for vascular development. ERBB4 activation in GBM is associated with shorter survival and promotes tumor growth through ERK activation. KITLG (kit ligand) signals through KIT receptor on hematopoietic and vascular cells. These growth factor pathways drive robust angiogenesis supporting tumor vascularization and nutrient delivery.

**Predicted impacts**
- Enhanced VEGF-dependent endothelial cell recruitment and angiogenesis
- Amplified angiogenic signaling through NRP1 co-receptivity with VEGFR2
- Increased tumor vascularization supporting nutrient delivery and oxygenation
- ERBB4-dependent proliferation and survival signaling in glioma and associated vascular cells
- Resistance to anti-EGFR therapeutics through ERBB4 compensatory activation
- Increased angiogenesis and tumorigenicity associated with poor patient survival

**Evidence summary**
Angiogenesis is critical for GBM growth, and multiple vascular growth factor pathways are dysregulated in this disease. NRP1 (neuropilin-1) acts as a co-receptor for VEGF165 and VEGFR2, serving to amplify VEGF-dependent angiogenic signaling. VEGF selectively increases NRP1 expression through VEGFR2-dependent transcriptional upregulation in endothelial cells, creating a positive feedback loop that robust angiogenesis. NRP1 coexistence with VEGFR2 quantitatively increases VEGF165 binding and functional receptor expression. In animal models of pathologic angioproliferative retinopathy, intense NRP1 mRNA expression is observed in newly formed vessels, and selective NRP1 inhibition substantially suppresses neovascular formation. In GBM, ERBB4 receptor tyrosine kinase activation is associated with increased proliferation, angiogenesis, and tumorigenicity. Although ERBB4 mRNA levels are generally lower in GBM than in normal brain, ERBB4 protein phosphorylation (activation) is observed in 89% of GBM samples versus only 10% of normal brain, indicating selective post-translational activation. ERBB4 activation independent of EGFR predicts shorter patient survival and enables compensatory growth signaling when EGFR-targeted therapies are administered. These findings establish angiogenic growth factor signaling as a key driver of GBM progression.

**Atomic biological processes**
- VEGF-dependent neuropilin-1 induction and VEGFR2 signaling amplification. Genes: NRP1
  - [8]: VEGF165 selectively upregulates NRP1 via VEGFR2-dependent pathway; NRP1 coexists with VEGFR2 to increase VEGF165 binding and angioproliferative signaling
- Endothelial cell proliferation and neovascular formation. Genes: NRP1, FGFR2
  - [8]: VEGF-stimulated endothelial proliferation is significantly inhibited by anti-NRP1 antibody; NRP1 inhibition suppresses neovascular formation in pathologic angioproliferative models
- ERBB4 receptor activation and ERK mitogenic signaling. Genes: ERBB4
  - [29]: ERBB4 activation in GBM is associated with increased proliferation, angiogenesis, and tumorigenicity; ERBB4 promotes growth through ERK activation
- KIT ligand-mediated signaling in vascular and hematopoietic cells. Genes: KITLG
  - [26]: Growth factor ligands including KITLG drive proliferation of progenitor cells including those in vascular tissues

**Atomic cellular components**
- Neuropilin-1 VEGF co-receptor complex with VEGFR2. Genes: NRP1
  - [8]: NRP1 coexists with VEGFR2 to increase VEGF165 binding and functional receptor expression in endothelial cells
- ERBB4 receptor tyrosine kinase and downstream signaling. Genes: ERBB4
  - [29]: ERBB4 forms functional receptor complexes that activate downstream ERK and other mitogenic pathways in glioma cells
- Fibroblast growth factor receptor 2 signaling complex. Genes: FGFR2
  - [26]: FGFR2 mediates FGF signaling important for vascular and developmental processes

**Required genes (not in input)**
- Genes: VEGF, VEGFR2, FGF, FGF receptors, HRG, Heregulin, KIT, c-KIT, MAPK, ERK1/2, PI3K, AKT
  - [8]: VEGF and VEGFR2 are required ligand-receptor pair for NRP1 induction and angiogenic signaling
  - [29]: Heregulin-1beta is the ERBB3/ERBB4 ligand; ERK activation is downstream of ERBB4

**Program citations**
- [8]: Comprehensive characterization of VEGF-induced NRP1 expression and its role in angiogenic proliferation
- [29]: Evidence that ERBB4 activation is independent prognostic factor and therapeutic vulnerability in GBM

## Program: Ion Channel & Electrolyte Homeostasis Dysregulation
This program encompasses ion channels and transporters that maintain cellular electrolyte balance and control neuronal excitability. Potassium channels (KCNQ3, KCNK2, KCNH8) regulate resting membrane potential and electrical activity. Voltage-gated calcium channels, modulated by CACNA2D3 auxiliary subunit, control calcium influx. CACNA2D3 functions as a tumor suppressor and is downregulated in gliomas. The bicarbonate transporter SLC4A10 participates in pH homeostasis. In GBM, dysregulation of these ion channels and transporters contributes to altered electrolyte balance that supports tumor cell survival and potentially creates a depolarized state permissive for abnormal signaling.

**Predicted impacts**
- Altered resting membrane potential affecting cellular signaling thresholds
- Dysregulated calcium homeostasis affecting metabolic and signaling processes
- Loss of tumor suppressive effects of CACNA2D3 enabling continued proliferation
- Altered pH homeostasis supporting metabolic reprogramming
- Changes in ion-dependent signaling cascades downstream of calcium and potassium flux
- Prognostic significance of ion channel expression profile in predicting GBM survival

**Evidence summary**
Ion channels and transporters are increasingly recognized as important regulators of cancer cell behavior. CACNA2D3, which encodes an auxiliary subunit of voltage-gated calcium channels, is downregulated in gliomas and functions as a tumor suppressor, with re-expression of CACNA2D3 inhibiting glioma cell proliferation. Ion channel gene expression profiles are associated with glioma patient survival, indicating that dysregulation of ionic homeostasis contributes to GBM progression. Potassium channels (KCNQ3, KCNK2, KCNH8) regulate resting membrane potential and neuronal excitability. Loss or downregulation of these channels in GBM may alter the cellular electrolyte balance and create a more depolarized state permissive for abnormal signaling. The bicarbonate transporter SLC4A10 participates in pH regulation, and altered pH homeostasis is implicated in metabolic reprogramming characteristic of GBM. In the context of GABAergic synaptic signaling in DMGs, dysregulation of chloride transporters (particularly NKCC1, which is not in this gene set but is functionally implicated) combined with altered potassium channel function may contribute to the depolarizing GABA phenotype. Overall, ion channel dysregulation represents a potential therapeutic vulnerability in GBM.

**Atomic biological processes**
- Potassium channel regulation of resting membrane potential. Genes: KCNQ3, KCNK2, KCNH8
  - [6]: Ion channel gene expression profile predicts survival in glioma patients, implicating ion channels in GBM biology
- Voltage-gated calcium channel regulation and calcium influx. Genes: CACNA2D3
  - [1]: CACNA2D3, an auxiliary calcium channel subunit, is downregulated in gliomas and functions as a tumor suppressor
  - [5]: Presynaptic calcium signaling regulates neurotransmitter release and synaptic dynamics
- Bicarbonate transport and pH homeostasis. Genes: SLC4A10
  - [12]: Solute carrier bicarbonate transporters (SLC4 family) mediate bicarbonate-dependent pH regulation

**Atomic cellular components**
- Potassium channel proteins controlling membrane excitability. Genes: KCNQ3, KCNK2, KCNH8
  - [6]: Ion channel gene expression signatures are prognostic in glioma
- Voltage-gated calcium channel auxiliary subunits. Genes: CACNA2D3
  - [1]: CACNA2D3 is a calcium channel auxiliary protein with tumor suppressive function
- Plasma membrane ion transporters for electrolyte balance. Genes: SLC4A10
  - [12]: SLC family proteins mediate ion and metabolite transport across cellular membranes

**Required genes (not in input)**
- Genes: NKCC1, SLC12A2, KCC2, SLC12A5, CACNA1A, CACNA1B, CACNA1C, Other CACNA family members, Cav channels, STIM, ORAI
  - [1]: CACNA2D3 functions as auxiliary subunit to full-length calcium channel proteins
  - [4]: NKCC1 function critical for depolarizing GABA effect in DMG

**Program citations**
- [1]: CACNA2D3 functions as tumor suppressor and is downregulated in gliomas
- [6]: Ion channel gene expression profiles predict survival in glioma patients
- [4]: Ion channel function critical in DMG GABAergic synaptic signaling

## Program: Synaptic Plasticity & Dendritic Maturation
This program encompasses genes that control the formation, maturation, and plasticity of synaptic connections. Synaptotagmin proteins (SYT1, SYT4) are calcium sensors in presynaptic vesicles that trigger neurotransmitter release. Postsynaptic density proteins and related factors organize the postsynaptic compartment. CELF4, a translational repressor of synaptic proteins, is critical for prenatal synaptic development. Dendritic spine formation and maintenance depend on polarity proteins that compartmentalize spine structure. Aberrant expression of these genes in GBM disrupts synaptic specialization while potentially enhancing migratory and invasive phenotypes.

**Predicted impacts**
- Loss of synaptic specialization reducing differentiated phenotype
- Decreased compartmentalization of dendritic spines affecting cell morphology
- Reduced postsynaptic organization and functional synaptic connectivity
- Enhanced cellular plasticity enabling migration and invasion
- Altered calcium signaling at synapses affecting neuronal communication
- Shift from post-mitotic synaptic functions toward proliferative phenotype

**Evidence summary**
Synaptic plasticity and dendritic maturation are hallmarks of differentiated neurons and are progressively lost in glioblastoma. CELF4, an RNA binding protein highly expressed in developing subplate neurons, translationally represses mRNAs encoding synaptic proteins including VAMP, TrkB.T1, and other synaptically active proteins. CELF4 deletion causes sex-specific disruption of subplate synapses and altered dendritic complexity, indicating that CELF4-mediated translational control is essential for appropriate synaptic development. Synaptotagmin proteins (SYT1, SYT4) act as calcium sensors in synaptic vesicles and trigger neurotransmitter release. Polarity proteins maintain dendritic spine compartmentalization, with loss of polarity proteins in developing neurons causing dramatic reduction in PSD-95-positive synapses. In glioblastoma, the loss of genes promoting synaptic specialization enables cells to escape post-mitotic constraints and maintain proliferative capacity. The presence of multiple synaptic genes in this GBM-associated gene set suggests that suppression of the synaptic maturation program is part of the gliomagenic process, allowing cells to retain undifferentiated, proliferative properties.

**Atomic biological processes**
- Calcium-dependent synaptic vesicle release and neurotransmitter secretion. Genes: SYT1, SYT4, SV2B
  - [5]: SV2B regulates presynaptic calcium signaling and synaptic vesicle dynamics critical for neurotransmitter release
- Translational control of synaptic proteins during development. Genes: CELF4
  - [30]: CELF4 translationally represses mRNAs encoding synaptic proteins, with deletion causing disruption of subplate synapses
- Dendritic spine morphogenesis and polarity protein function. Genes: NYAP2
  - [15]: Polarity proteins regulate dendritic spine formation and maintenance through compartmentalization and cytoskeletal dynamics
- Postsynaptic protein organization and function. Genes: INSYN2B, NSG2, LAMP5, NRSN1
  - [7]: Cell adhesion molecules and scaffolding proteins organize postsynaptic density and dendritic structure
- Synaptic activity-dependent plasticity and long-term potentiation. Genes: CELF4, GRIP2
  - [30]: RNA binding proteins including CELF4 control mRNAs encoding proteins involved in synaptic transmission and plasticity

**Atomic cellular components**
- Presynaptic terminal with synaptic vesicles and release machinery. Genes: SYT1, SYT4, SV2B, SYNPR
  - [5]: SV2 proteins are integral components of synaptic vesicles regulating calcium-dependent release
- Postsynaptic density organizing synaptic proteins and receptors. Genes: GRIP2, INSYN2B, LAMP5, NRSN1
  - [15]: PSD-95 and associated proteins organize postsynaptic density; dendritic spine structure maintained by polarity complexes
- mRNA localization and translational control at synapses. Genes: CELF4
  - [30]: CELF4 binds and translationally represses mRNAs at developing synapses

**Required genes (not in input)**
- Genes: PSD95, SAP102, NMDAR, AMPAR, mGluR, Calmodulin, CaMKII, CREB, MAPK, PI3K, AKT
  - [15]: PSD-95 is key postsynaptic density protein organizing synaptic structure
  - [30]: Calcium/calmodulin-dependent protein kinase II (CaMKII) is involved in synaptic plasticity downstream of CELF4 target mRNAs

**Program citations**
- [30]: CELF4 controls translational repression of synaptic proteins during prenatal synaptic development
- [5]: SV2B regulates presynaptic calcium signaling critical for synaptic vesicle dynamics
- [15]: Polarity proteins regulate dendritic spine formation and plasticity

## Program: Axonal Maintenance & Cytoskeletal Integrity
This program encompasses genes that maintain axonal structure, diameter, and conduction velocity through organization of neurofilaments and microtubules. STMN2 (stathmin-2) is critical for establishing and maintaining neurofilament-dependent axoplasmic organization. Loss of STMN2 leads to shrinkage of neurofilament spacing, axonal collapse, and motor and sensory deficits. SV2B regulates presynaptic calcium and synaptic vesicle dynamics affecting axonal function. Dynein motors (DYNC1I1) transport cargo along microtubules. In GBM, dysregulation of axonal maintenance genes may contribute to aberrant cell morphology and altered cellular dynamics.

**Predicted impacts**
- Altered axonal diameter and conduction velocity affecting cell communication
- Disrupted neurofilament spacing leading to reduced axonal stability
- Altered synaptic terminal structure and function
- Changes in microtubule dynamics affecting cellular transport
- Modified cell morphology with reduced axon-like processes
- Potential effects on cellular migration through altered cytoskeletal organization

**Evidence summary**
Axonal integrity is maintained by proper organization of neurofilaments and microtubules that determine axonal diameter and conduction velocity. STMN2 (stathmin-2, also called SCG10) is an essential axonal maintenance factor that orchestrates neurofilament spacing and organization. Sustained loss of STMN2 in adult mice leads to shrinkage of neurofilament spacing from median 29.02 nm to 16.86 nm, resulting in axonal collapse, reduced conduction velocity by 35%, and motor and sensory denervation. STMN2 loss is particularly relevant in amyotrophic lateral sclerosis (ALS), where TDP-43 pathology misprocesses STMN2 mRNA, producing truncated non-functional transcripts. Similar neurofilament spacing reduction (~30%) is observed in ALS patient tissues, indicating that STMN2 dysregulation directly contributes to motor neuron pathology. In GBM, dysregulation of STMN2 and other axonal maintenance genes may disrupt the normal cellular architecture and may contribute to aberrant cell morphology and migration. SV2B regulates presynaptic calcium signaling and synaptic vesicle dynamics, and loss of SV2B alters the pattern of neurotransmitter release. Dynein motors mediate long-distance cargo transport in neuronal and glial processes. The presence of multiple axonal maintenance genes in this GBM gene set suggests that disruption of normal axonal structure may support glioma cell dedifferentiation and altered cellular dynamics.

**Atomic biological processes**
- Neurofilament assembly and axoplasmic organization. Genes: STMN2, SLAIN1
  - [13]: STMN2 plays critical role in establishing and maintaining neurofilament-dependent axoplasmic organization; loss of STMN2 reduces neurofilament spacing by nearly half
- Microtubule dynamics and cargo transport. Genes: DYNC1I1, SLAIN1
  - [13]: Microtubule associated proteins regulate dynamics of microtubules important for axonal function and transport
- Presynaptic calcium regulation and synaptic vesicle dynamics. Genes: SV2B
  - [5]: SV2B regulates presynaptic calcium levels critical for synaptic transmission and maintaining axonal terminals
- Actin cytoskeleton organization and cell morphology. Genes: RND3, ARHGAP18, SPHKAP
  - [15]: Rho family GTPases and associated proteins regulate actin dynamics affecting dendritic spine and axonal morphology

**Atomic cellular components**
- Neurofilament proteins and spacer proteins in axoplasm. Genes: STMN2
  - [13]: Neurofilament subunits organize into three-dimensional interlinked arrays with STMN2 orchestrating nearest-neighbor distances
- Microtubule motor complexes and associated proteins. Genes: DYNC1I1
  - [13]: Dynein motors transport cargo along microtubules in neurons and glia
- Presynaptic terminal ultrastructure and function. Genes: SV2B
  - [5]: SV2B is critical component of synaptic vesicles regulating terminal structure and function

**Required genes (not in input)**
- Genes: NF-L, NF-M, NF-H, Tau, MAPs, Alpha-tubulin, Beta-tubulin, HDAC6, TDP-43
  - [13]: Neurofilament subunits are essential partners with STMN2 in maintaining axonal structure

**Program citations**
- [13]: Comprehensive characterization of STMN2 role in neurofilament-dependent axonal maintenance and consequences of loss
- [5]: SV2B regulates presynaptic calcium and synaptic vesicle dynamics

## Program: Apoptosis Resistance & Cell Survival Pathways
This program encompasses genes controlling cell death and survival decisions. HRK (Harakiri) is a pro-apoptotic BH3-only protein of the Bcl-2 family that regulates apoptosis by interfering with anti-apoptotic Bcl-2 and Bcl-xL proteins. DACH1 and DACH2 are tumor suppressors that activate cell cycle arrest and apoptosis genes while repressing survival and proliferation genes. TP73 encodes p73, a p53-related transcription factor with complex roles in apoptosis and stemness. Loss or downregulation of these pro-death and pro-differentiation factors enables GBM cells to resist apoptosis and maintain viability despite stress.

**Predicted impacts**
- Reduced susceptibility to intrinsic apoptotic triggers through loss of pro-apoptotic signaling
- Enhanced cell survival signaling through loss of death-promoting transcription factors
- Maintenance of stemness properties through altered TP73 function
- Reduced responsiveness to genotoxic stress and chemotherapy-induced apoptosis
- Enhanced proliferation through loss of cell cycle checkpoint functions
- Increased resistance to radiation and chemotherapy

**Evidence summary**
GBM cells acquire enhanced resistance to apoptosis through dysregulation of cell death programs. HRK (Harakiri), a pro-apoptotic BH3-only member of the Bcl-2 family, promotes intrinsic apoptosis by antagonizing anti-apoptotic Bcl-2 and Bcl-xL proteins at the mitochondrial membrane. Loss or reduced HRK expression would enhance survival signaling. DACH1 (Dachshund-related protein) functions as a tumor suppressor and is frequently lost in various cancers including breast, ovarian, and potentially brain tumors. DACH1 expression is lost in a subset of breast cancers associated with poor prognosis, and re-introduction of DACH1 inhibits tumor cell proliferation and growth through suppression of cyclin D1. DACH1 activates expression of genes involved in cell cycle arrest and apoptosis while simultaneously repressing genes involved in cell survival and proliferation. DACH2 functions similarly. TP73, which encodes p73 protein, is a p53-related transcription factor with complex roles in GBM. Recent studies demonstrate that TAp73 (transcriptionally active p73) is required for stemness potential in glioblastoma stem cells, acting as a regulator of the balance between stemness and differentiation-dependent apoptosis. In GBM, altered TP73 function enables maintenance of stem-like properties resistant to differentiation-induced death. The presence of multiple pro-death and pro-differentiation genes in this GBM-associated gene set suggests that suppression of apoptotic pathways and cell cycle checkpoints is part of the malignant transformation process.

**Atomic biological processes**
- Intrinsic apoptotic pathway and Bcl-2 family regulation. Genes: HRK
  - [22]: HRK is a pro-apoptotic Bcl-2 family member that regulates apoptosis by interfering with anti-apoptotic Bcl-2 and Bcl-xL proteins
- Transcriptional control of cell cycle arrest and apoptosis. Genes: DACH1, DACH2
  - [35]: DACH1 activates genes involved in cell cycle arrest and apoptosis while repressing survival and proliferation genes; functions as tumor suppressor
- TP73-mediated stemness and apoptotic regulation. Genes: TP73
  - [21]: TAp73 is required for stemness potential in glioblastoma stem cells, regulating balance between differentiation and apoptosis

**Atomic cellular components**
- Mitochondrial outer membrane permeabilization complex. Genes: HRK
  - [22]: HRK protein inserts into mitochondrial membrane to promote apoptosis
- Transcriptional repressor complexes with NCoR corepressor. Genes: DACH1, DACH2
  - [35]: DACH1 contains dachshund domain that interacts with nuclear co-repressor (NCoR) to repress gene expression

**Required genes (not in input)**
- Genes: BCL2, BCL-XL, BCL-W, MCL1, BAX, BAK, PUMA, NOXA, TP53, p53, p21, MDM2, Caspase 9, Caspase 3
  - [22]: HRK interacts with anti-apoptotic BCL2 family members to promote apoptosis
  - [35]: DACH1 modulates p53-related transcriptional regulation

**Program citations**
- [22]: HRK is pro-apoptotic regulator of intrinsic pathway
- [35]: DACH1 functions as tumor suppressor through activation of cell cycle arrest and apoptosis genes
- [21]: TAp73 regulates stemness and apoptotic balance in GBM stem cells

## Program: Retinoic Acid & MAPK-CaMKII Signaling Integration
This program encompasses genes mediating non-canonical retinoic acid (RA) signaling through cellular retinoic acid binding protein 1 (CRABP1). CRABP1 acts as a signalosome that integrates retinoic acid with MAPK (mitogen-activated protein kinase) and CaMKII (calmodulin-dependent protein kinase II) signaling. CRABP1 suppresses MAPK-dependent cell proliferation by competing with Ras for interaction with RAF kinase, dampening ERK activation. CRABP1 also dampens CaMKII over-activation that could trigger neuronal death. This integrated signaling pathway affects stem cell proliferation, cancer progression, and neuronal survival.

**Predicted impacts**
- Enhanced MAPK-dependent proliferation through loss of CRABP1-mediated signal dampening
- Increased growth factor responsiveness and proliferative signaling
- Reduced retinoic acid-mediated differentiation and growth suppression
- Enhanced CaMKII over-activation potentially contributing to altered neuronal phenotype
- Increased neural stem cell and glioma stem cell proliferation
- Resistance to retinoic acid-mediated growth suppression

**Evidence summary**
CRABP1 (Cellular Retinoic Acid Binding Protein 1) functions as a critical mediator of non-canonical retinoic acid signaling that integrates RA with major cellular signaling cascades. CRABP1 forms RA-regulated signalsomes—stable complexes with specific signaling molecules—that function in a cell context-dependent manner. In embryonic stem cells and neural stem cells, CRABP1 competes directly with Ras for binding to RAF kinase at its Ras-binding domain, thereby dampening MAPK signal propagation and reducing cell proliferation. This CRABP1-mediated MAPK dampening suppresses cell cycle progression by expanding the G1 phase. In CRABP1-knockout mice, neural stem cells show expanded pools due to enhanced NSC proliferation in hippocampus and improved memory function, indicating that CRABP1 loss promotes stem cell proliferation. In cancer, CRABP1 loss would therefore enhance growth factor-dependent proliferation. Additionally, CRABP1 competes with calmodulin for direct interaction with CaMKII, thereby dampening CaMKII over-activation. Since over-activation of CaMKII is a major trigger of neuronal death and dysfunction, CRABP1-mediated dampening provides neuroprotection. In GBM, loss of CRABP1 would enhance both growth factor-dependent proliferation (through enhanced MAPK signaling) and alter calcium-dependent signaling through CaMKII, supporting tumor growth and potentially affecting neuronal differentiation.

**Atomic biological processes**
- Retinoic acid-mediated MAPK signal dampening. Genes: CRABP1
  - [16]: CRABP1 competes with Ras to directly interact with RAF kinase, dampening MAPK signal propagation and reducing cell proliferation
- CaMKII over-activation suppression and neuroprotection. Genes: CRABP1
  - [16]: CRABP1 competes with calmodulin to directly interact with CaMKII, dampening CaMKII over-activation and providing neuroprotection
- Cell cycle progression and G1 phase expansion. Genes: CRABP1
  - [16]: CRABP1-mediated MAPK dampening suppresses cell cycle progression by expanding G1 phase
- Stem cell proliferation control. Genes: CRABP1
  - [16]: CRABP1-deficient neural stem cells show enhanced proliferation; CRABP1 acts as tumor suppressor in stem cell populations

**Atomic cellular components**
- Cytoplasmic CRABP1-signaling protein complexes. Genes: CRABP1
  - [16]: CRABP1 forms context-dependent complexes with RAF kinase and CaMKII to regulate signaling output

**Required genes (not in input)**
- Genes: RAF, MEK, ERK1/2, RAS, Calmodulin, CaMKII, Retinoic acid, RALDH, RAR, RXR
  - [16]: CRABP1 interacts with RAF and CaMKII; retinoic acid is ligand for CRABP1 signalosome

**Program citations**
- [16]: Comprehensive review of CRABP1-mediated MAPK and CaMKII signaling in stem cells and cancer

## Program: Metabolic Reprogramming & Warburg Effect Activation
This program encompasses genes involved in metabolic reconfiguration toward aerobic glycolysis (Warburg effect) that characterizes GBM. Protein kinase C (PRKCA) signaling promotes metabolic reprogramming through MAPK pathway activation. Glycosyltransferases and metabolic enzymes (ST6GAL1, PCSK2, ADCY8, HSD11B2, PIP5K1B) support altered glucose, lipid, and nucleotide metabolism. The Warburg effect—preference for glycolysis over oxidative phosphorylation even under normoxia—supports GBM proliferation and contributes to therapy resistance. Hypoxia and metabolic stress activate transcription factors (HIF-1alpha) that drive expression of glycolytic genes.

**Predicted impacts**
- Enhanced glucose uptake and glycolytic flux supporting rapid ATP generation
- Increased lactate production and acidic microenvironment
- Resistance to radiotherapy and chemotherapy through metabolic support of tumor survival
- Enhanced lipid and nucleotide synthesis supporting rapid cell division
- Reduced oxidative stress from decreased mitochondrial respiration
- Support for hypoxic regions of tumor through glycolytic ATP production
- Altered tumor microenvironment acidification affecting immune infiltration

**Evidence summary**
Metabolic reprogramming is a hallmark of glioblastoma and a key mechanism of therapy resistance. GBM cells preferentially utilize aerobic glycolysis (Warburg effect) rather than oxidative phosphorylation, even under normoxic conditions. Multiple studies demonstrate significant correlation between upregulation of glycolytic genes and poor survival in GBM patients. Hypoxia is a significant activator of metabolic reprogramming, with hypoxia-inducible factor-1 alpha (HIF-1alpha) stabilized in low oxygen conditions and translocating to the nucleus where it activates glycolytic genes. GBM also shows dysregulation of nucleotide synthesis and lipid metabolism pathways. Protein kinase C (PKC) family members play essential roles in transducing signals that drive proliferation, differentiation, and metabolic reconfiguration in neural stem cells and glioma stem cells. PKC signaling engages the Ras-MAPK and PI3K-Akt pathways that are critical for metabolic reprogramming. Importantly, lactate dehydrogenase A (LDHA) and anaerobic glycolysis contribute to GBM resistance to both radiotherapy and chemotherapy. Glycolysis inhibition through LDHA gene silencing increases radiation sensitivity and response to temozolomide (TMZ). Inhibition of pyruvate dehydrogenase kinase (PDK) and stimulation of mitochondrial pyruvate dehydrogenase (PDH) can revert the Warburg effect, leading to GBM cytotoxicity and increased TMZ sensitivity. The presence of metabolic enzymes and PKC signaling genes in this GBM-associated gene set indicates that metabolic reprogramming is an active process driven by dysregulated oncogenic signaling.

**Atomic biological processes**
- Aerobic glycolysis upregulation and Warburg effect. Genes: PRKCA, ADCY8
  - [28]: GBM undergoes Warburg effect with upregulation of glycolytic genes; correlation between glycolytic gene expression and poor survival
- Hypoxia-inducible factor signaling and metabolic adaptation. Genes: HSD11B2
  - [28]: Hypoxia-inducible factor (HIF-1alpha) stabilization drives glycolytic gene expression and metabolic adaptation to hypoxic tumor microenvironment
- Protein kinase C signaling in metabolic reprogramming. Genes: PRKCA
  - [14]: PKC family members play essential role in transducing signals related to cell cycle, differentiation, and metabolic reprogramming in GBM
- Nucleotide and lipid metabolism dysregulation. Genes: PCSK2, ST6GAL1, PIP5K1B
  - [28]: GBM shows reprogramming of nucleotide synthesis and lipid metabolism supporting increased proliferation and therapy resistance

**Atomic cellular components**
- Protein kinase C signaling complexes and kinase pathways. Genes: PRKCA
  - [14]: PKC isozymes transduce signals through MAPK and PI3K pathways affecting cell proliferation and metabolism

**Required genes (not in input)**
- Genes: GLUT1, SLC2A1, HIF-1alpha, HIF1A, LDHA, PDK1, PDH, PKM2, PFKFB3, Hexokinase, Pyruvate kinase, Lactate transporter, MCT1
  - [28]: GLUT1 glucose transporter and glycolytic enzymes are core components of Warburg effect dysregulation in GBM

**Program citations**
- [28]: Comprehensive review of metabolic reprogramming in GBM including Warburg effect, nucleotide and lipid metabolism dysregulation
- [14]: PKC signaling pathways in GBM metabolic reprogramming and cell cycle control

## Program: Extracellular Matrix Remodeling & Cell Migration
This program encompasses genes encoding extracellular matrix (ECM) proteins and enzymes that modify ECM structure, enabling GBM cell migration and invasion. Matrix stiffening through deposition of structural proteins (FRAS1, HMCN1, SPOCK1, SVEP1) and glycosaminoglycan modifications (B3GAT2, B3GLCT, NDST4, HS3ST5) promotes glioma cell invasiveness. ECM stiffness activates mechanotransduction pathways that condition glioma cells for enhanced invasion. Sialyltransferases (ST6GAL1) and other glycosyltransferases modify cell surface glycoproteins affecting cell-cell and cell-matrix interactions. Hyaluronidases (CEMIP2) degrade hyaluronic acid facilitating cell migration.

**Predicted impacts**
- Enhanced ECM stiffness promoting glioma cell invasion and migration
- Altered cell-matrix adhesion dynamics reducing stationary cell behavior
- Increased mechanotransduction signaling activating pro-invasive pathways
- Reduced physical barriers to cell migration through ECM remodeling
- Enhanced glycosaminoglycan composition modulating ECM viscoelasticity
- Altered cell surface glycosylation affecting cell-cell adhesion and immune recognition
- Facilitated tumor cell dissemination through ECM degradation

**Evidence summary**
The extracellular matrix surrounding glioblastoma cells plays a critical role in promoting invasiveness and metastatic spread. ECM stiffness has been demonstrated to correlate with tumor invasion in various cancer types, including glioblastoma. Physical stiffening of the ECM through deposition of fibrillar collagen and other structural proteins activates mechanotransduction pathways that condition glioma cells for enhanced invasion. This 'stiffness-induced' phenotype is characterized by increased invasive capacity and altered gene expression profiles. ECM composition is actively remodeled by tumor cells and associated stromal cells through synthesis of structural proteins, glycosaminoglycans, and proteoglycans. Glycosyltransferases and sulfotransferases regulate the composition of glycosaminoglycans including heparan sulfate and chondroitin sulfate, which affects ECM properties. Cell surface glycoproteins, including cell adhesion molecules, are modified by sialyltransferases that affect their adhesive properties and recognition by immune cells. Hyaluronidases degrade hyaluronic acid, a major ECM component, facilitating cell migration through tissue. The presence of multiple ECM-related genes in this GBM-associated gene set indicates that active ECM remodeling is part of the malignant GBM phenotype, enabling enhanced invasiveness and dissemination.

**Atomic biological processes**
- Extracellular matrix protein deposition and stiffening. Genes: FRAS1, HMCN1, SPOCK1, SVEP1, CRIM1
  - [25]: Extracellular matrix stiffening correlates with GBM invasion; ECM stiffness conditions glioma cells for enhanced invasiveness
- Glycosaminoglycan synthesis and ECM composition. Genes: B3GAT2, B3GLCT, NDST4, HS3ST5
  - [12]: Glycosyltransferases and sulfotransferases regulate glycosaminoglycan composition affecting ECM properties
- Cell surface glycoprotein modification and adhesion. Genes: ST6GAL1
  - [7]: Glycosylation of CAMs affects cell adhesion and cell-to-cell communication
- Hyaluronic acid degradation and cell migration. Genes: CEMIP2
  - [25]: Hyaluronidases degrade ECM hyaluronic acid facilitating cell migration through tissue
- Mechanotransduction and integrin signaling. Genes: ANTXR2
  - [25]: ECM stiffness activates mechanotransduction through integrin and focal adhesion kinase signaling promoting invasion

**Atomic cellular components**
- Structural extracellular matrix proteins and proteoglycans. Genes: FRAS1, HMCN1, SPOCK1, SVEP1
  - [25]: Fibrillar collagens, proteoglycans, and other structural proteins comprise tumor ECM
- Cell surface receptor-ECM interaction complexes. Genes: ANTXR2
  - [25]: Integrin heterodimers and other receptors mediate cell-matrix contacts transmitting mechanotransduction signals

**Required genes (not in input)**
- Genes: Collagen alpha-1, COL1A1, Integrin alpha-V, Integrin beta-1, Focal adhesion kinase, FAK, Paxillin, Src kinase, Matrix metalloproteinases, MMP2, MMP9, ADAMTS, TIMP, Versican, Perlecan
  - [25]: Collagen and integrin family proteins are core ECM components and mechanotransducers

**Program citations**
- [25]: Comprehensive characterization of ECM stiffness conditioning glioblastoma cells for long-term invasion
- [27]: Tumor microenvironment components including ECM interact with GBM cells to promote progression

## Program: G-Protein-Coupled Receptor & Neuroendocrine Signaling
This program encompasses G-protein-coupled receptors (GPCRs) and associated signaling that drive glioma cell proliferation and survival. SSTR2 (somatostatin receptor 2) is a GPCR highly expressed in neuroendocrine tumors but expression can be downregulated. Recent studies show that SSTR2 interacts with Wnt pathway protein Dvl1 in a ligand-independent manner, targeting SSTR2 for lysosomal degradation. GRK5 (G-protein receptor kinase 5) phosphorylates GPCRs affecting their signaling output and internalization. Adenylyl cyclase (ADCY8) produces cAMP, a key second messenger in GPCR signaling. These pathways affect proliferation, differentiation, and metabolism in GBM.

**Predicted impacts**
- Altered GPCR signaling affecting cell proliferation and differentiation balance
- Enhanced Wnt-Dvl mediated GPCR degradation reducing signaling capacity
- Modified cAMP signaling affecting metabolic and proliferative responses
- Altered neuroendocrine differentiation state
- Potential therapeutic opportunity through Wnt inhibitors boosting SSTR2 expression
- Dysregulated GPCR desensitization affecting sustained growth signaling

**Evidence summary**
G-protein-coupled receptors (GPCRs) regulate diverse aspects of cell physiology including proliferation, differentiation, and migration. SSTR2 (somatostatin receptor 2) is a GPCR commonly overexpressed in neuroendocrine tumors, where it serves as a target for therapeutic interventions. However, not all neuroendocrine tumors express SSTR2, and expression can be downregulated with prolonged agonist treatment. Recent studies identified a mechanism by which the Wnt pathway protein Dvl1 (Dishevelled 1) binds to SSTR2 in a ligand-independent manner and targets the receptor for lysosomal degradation, reducing steady-state SSTR2 expression. This Dvl1-mediated degradation can be stimulated by overexpression of Wnt ligands. Importantly, treatment with Wnt pathway inhibitors can boost SSTR2 expression in neuroendocrine tumor cells, suggesting potential therapeutic strategies. GRK5 (G-protein receptor kinase 5) phosphorylates GPCRs following activation, leading to receptor desensitization and internalization. Adenylyl cyclase (ADCY8) catalyzes the synthesis of cAMP from ATP, producing a key second messenger that affects cell proliferation and differentiation downstream of GPCR activation. The presence of GPCR signaling genes in this GBM-associated gene set suggests that altered GPCR-mediated signaling contributes to glioma biology, potentially through effects on proliferation, neuroendocrine differentiation, or metabolic state.

**Atomic biological processes**
- Somatostatin receptor 2 signaling and therapeutic response. Genes: SSTR2
  - [17]: SSTR2 is GPCR highly expressed in neuroendocrine tumors; Dvl1-dependent degradation regulates SSTR2 expression independent of agonist
- G-protein receptor kinase regulation of GPCR desensitization. Genes: GRK5
  - [17]: GRK phosphorylates GPCRs including SSTR2 affecting internalization and recycling
- cAMP generation and second messenger signaling. Genes: ADCY8
  - [17]: Adenylyl cyclase generates cAMP downstream of GPCR signaling; cAMP affects cell proliferation and differentiation
- Wnt-Dvl-mediated GPCR downregulation. Genes: SSTR2
  - [17]: Wnt pathway protein Dvl1 targets SSTR2 for lysosomal degradation independent of agonist; Wnt inhibitors boost SSTR2 expression

**Atomic cellular components**
- Seven-transmembrane G-protein-coupled receptor (GPCR) complexes. Genes: SSTR2
  - [17]: SSTR2 forms functional GPCR heterotrimeric G-protein complexes
- G-protein receptor kinase regulatory complexes. Genes: GRK5
  - [17]: GRK5 phosphorylates and desensitizes GPCRs including SSTR2

**Required genes (not in input)**
- Genes: Somatostatin, SST, Wnt ligands, Wnt1-10, Frizzled receptors, FZD, LRP5/6, GSK3beta, Beta-catenin, CTNNB1, TCF, LEF, Heterotrimeric G proteins, Gs, Gi/o, PKA
  - [17]: Somatostatin is SSTR2 ligand; Wnt ligands activate Dvl1-mediated signaling; heterotrimeric G proteins are downstream effectors

**Program citations**
- [17]: Detailed characterization of SSTR2 regulation by Dvl1-mediated lysosomal degradation and Wnt pathway interactions

## Bibliography
1. Yi J, Daming C, Jie R, Ke W, Tao Z, Liang G. CACNA2D3 is downregulated in gliomas and functions as a tumor suppressor.. Molecular carcinogenesis [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/27583705/
2. Magdalena G, Masato N, David P. Neurogenesis in the Developing and Adult Brain-Similarities and Key Differences.. Cold Spring Harbor perspectives in biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4930921/
3. Elsa P, Dimitra T. Post-transcriptional mechanisms controlling neurogenesis and direct neuronal reprogramming.. Neural regeneration research [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11040297/
4. Barron T, Yalçın B, Su M, Byun YG, Gavish A, Shamardani K, et al.. GABAergic neuron-to-glioma synapses in diffuse midline gliomas. Nature [Internet]. 2025Feb19;639(8056). Available from: https://www.nature.com/articles/s41586-024-08579-3
5. Qun-Fang W, Zhen-Yu Z, Pratima T, Alejandro V, David MS, Roger J, et al.. SV2 acts via presynaptic calcium to regulate neurotransmitter release.. Neuron [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2913707/
6. Rong W, Christopher IG, Wanjun G, Eun AK, Inja L, Hyoweon B, et al.. Ion channel gene expression predicts survival in glioma patients.. Scientific reports [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4522676/
7. Xiaoming Z, Jana D, Chuan-Yun L, George RU. Human cell adhesion molecules: annotated functional subtypes and overrepresentation of addiction-associated genes.. Annals of the New York Academy of Sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4564344/
8. Hideyasu O, Hitoshi T, Atsushi O, Shinji K, Seiji K, Akiyoshi U, et al.. Selective induction of neuropilin-1 by vascular endothelial growth factor (VEGF): a mechanism contributing to VEGF-induced angiogenesis.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC117569/
9. Nan-Jie X, Mark H. Ephrin reverse signaling in axon guidance and synaptogenesis.. Seminars in cell & developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3288821/
10. Bing Z, Ursula MD, Jian-Guo G, Roy B, Jeffrey DE, Lianchun W. Repulsive axon guidance molecule Slit3 is a novel angiogenic factor.. Blood [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2774558/
11. Daiqing L. Emerging roles of the EBF family of transcription factors in tumor suppression.. Molecular cancer research : MCR [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5545892/
12. Available from: https://en.wikipedia.org/wiki/Solute_carrier_family
13. Jone L-E, Mariana B-H, Maximiliano P, Michael WB, Ze'ev M, Melinda SB, et al.. Stathmin-2 loss leads to neurofilament-dependent axonal collapse driving motor and sensory denervation.. Nature neuroscience [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10842032/
14. Noelia G-D, Irati H-C, Ricardo G-O, Samuel D-G, Félix AR, Irene I-L, et al.. Targeting Protein Kinase C in Glioblastoma Treatment.. Biomedicines [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC8067000/
15. Mikayla MV, Huaye Z. Polarity proteins: Shaping dendritic spines and memory.. Developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9953585/
16. Jennifer N, Yu-Lung L, Li-Na W. CRABP1 in Non-Canonical Activities of Retinoic Acid in Health and Diseases.. Nutrients [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9003107/
17. Heather SC, Yan Z, Jeffrey AF. The Wnt pathway protein Dvl1 targets somatostatin receptor 2 for lysosome-dependent degradation.. The Journal of biological chemistry [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/36965619/
18. Lee M, Elena GB, Rebecca D, Gareth B, Rasneer SB, Patrick MN, et al.. Disruption of the homeodomain transcription factor orthopedia homeobox (Otp) is associated with obesity and anxiety.. Molecular metabolism [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/29107289/
19. Arash P, Meysam M, Mohammad FH, Mohsen R, Mohsen C, Mojtaba YZ, et al.. Long Non-Coding RNA . Iranian journal of public health [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11490338/
20. Tiffany AM, Izabela K, Arkadi M, Ying Z, Anant S, Roger A, et al.. Myt1 and Myt1l transcription factors limit proliferation in GBM cells by repressing YAP1 expression.. Biochimica et biophysica acta Gene regulatory mechanisms [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30312684/
21. Villoch‐Fernandez J, Martínez‐García N, Martín‐López M, Maeso‐Alonso L, López‐Ferreras L, Vazquez‐Jimenez A, et al.. A novel <scp>TA</scp>p73‐inhibitory compound counteracts stemness features of glioblastoma stem cells. Molecular Oncology [Internet]. 2024Aug;19(3). Available from: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13694
22. Ezgi K-A, Ahmet C, Filiz S, Fidan S, Ilknur S-E, Alisan K, et al.. The pro-apoptotic Bcl-2 family member Harakiri (HRK) induces cell death in glioblastoma multiforme.. Cell death discovery [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/30774992/
23. Jian H, Allen LH, Liang Y, Baoli H, Sujun H, Soyoon SH, et al.. From the Cover: Neutralization of terminal differentiation in gliomagenesis.. Proceedings of the National Academy of Sciences of the United States of America [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3767545/
24. Alexander G, Jennifer ELH, Sylvie JL, Doris AP, Manijeh D, Ian JR, et al.. PTEN loss represses glioblastoma tumor initiating cell differentiation via inactivation of Lgl1.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC3787156/
25. Paola S-M, Rachel W, Steve R, Paula S, Konstantinos K, Alfredo Q-H. Extracellular Matrix Stiffness Conditions Glioblastoma Cells for Long-term Migration: Mechanical Memory as a Driver of Invasion and Recurrence in Glioblastoma.. Neuro-oncology [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/40973065/
26. Bengt W. Platelet-derived growth factor in glioblastoma-driver or biomarker?. Upsala journal of medical sciences [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4248069/
27. Pratibha S, Ashley A, Jiyong L, Vinay KP. Tumor microenvironment in glioblastoma: Current and emerging concepts.. Neuro-oncology advances [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC10034917/
28. Simona D, Simona D, Anna G, Nunzio V, Rosalba P. Targeting metabolic reprogramming in glioblastoma as a new strategy to overcome therapy resistance.. Frontiers in cell and developmental biology [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC11897528/
29. Jacqueline FD, Lauren TK, Naomi WA, Sameer AG, Anthony BL, Nicholas GG, et al.. Activation of ERBB4 in Glioblastoma Can Contribute to Increased Tumorigenicity and Influence Therapeutic Response.. Cancers [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC6116191/
30. Salamon I, Park Y, Miškić T, Kopić J, Matteson P, Page NF, et al.. Celf4 controls mRNA translation underlying synaptic development in the prenatal mammalian neocortex. Nature Communications [Internet]. 2023Sep27;14(1). Available from: https://www.nature.com/articles/s41467-023-41730-8
31. Luke MH, Paul S, Zhuoyao C, Shahd F, Vincenzo D. The role of E3 ubiquitin ligases in the development and progression of glioblastoma.. Cell death and differentiation [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7862665/
32. T PS, Y L, R JW, I-H P, A FC. Neuritin 1 promotes retinal ganglion cell survival and axonal regeneration following optic nerve crush.. Cell death & disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4669798/
33. Ruth M, Ana M, Nerea M. Developmental and adult expression of the Meis2 transcription factor in the central nervous system of . Frontiers in neuroanatomy [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC12631407/
34. Mengxi X, Li L, Yandong L, Yong G. An update regarding the role of WNK kinases in cancer.. Cell death & disease [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9485243/
35. Kumaran S, Santhosh KM, Kazuyuki K, Kongming W, Richard GP, Sakamuri VR. DACH1 negatively regulates the human RANK ligand gene expression in stromal/preosteoblast cells.. Journal of cellular biochemistry [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC2778848/
36. Magdalena R, Joanna KL, Damian G, Justyna S, Barbara C. The role of prospero homeobox 1 (PROX1) expression in follicular thyroid carcinoma cells.. Oncotarget [Internet].. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC5768392/
37. Tomofumi A, Ikue T-N, Yuki S, Dai K, Koji O, Yasuaki K, et al.. Tumor-specific interendothelial adhesion mediated by FLRT2 facilitates cancer aggressiveness.. The Journal of clinical investigation [Internet].. Available from: https://pubmed.ncbi.nlm.nih.gov/35104247/
