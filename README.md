# Phylogenetic Patterns of Brain Size and Language Complexity in Cetaceans

**Project Overview**

This repository contains the workflow, scripts, and phenotypic data used to explore the evolutionary trajectory of brain size and communication complexity across cetacean species. The goal of this project was to determine how many times large brain sizes and complex communication traits have independently evolved within cetacean lineages, utilizing *Hippopotamus amphibius* as an outgroup. This research provides insight into understanding the complexity of vocal and social aspects in cetaceans and can be applied to general knowledge on how brains have evolved to support advanced learning and communication. The raw phylogenetic sequence data (DATASET_B.phylip) was obtained from McGowen et al. (2020).

### Technical Stack
* **Languages:** Python, R, Bash
* **Sequence Data:** Nucleotide sequences[Improved_RAxML_Tree.pdf](https://github.com/user-attachments/files/29811833/Improved_RAxML_Tree.pdf)
 (FASTA, PHYLIP, NEXUS) for 7 targeted functional genes 
* **Tools:** Biopython, Clustal Omega, RAxML, R (`phangorn`, `phytools`, `ape`)
* **Infrastructure:** SLURM (High-Performance Computing cluster)

---

### Pipeline Workflow

**Steps:** Sequence Trimming -> Multiple Sequence Alignment (Clustal Omega) -> Model Testing (`phangorn`) -> Phylogenetic Tree Construction (RAxML) -> Ancestral State Reconstruction (ASR)

---

### Results

<img width="913" height="641" alt="Screen Shot 2026-07-07 at 11 23 56 PM" src="https://github.com/user-attachments/assets/84eb24b1-6cd3-45b6-a53d-1442e6098fdc" />

Starting with data for 36 overlapping species, the dataset was filtered to 19 cetacean species and one outgroup (*Hippopotamus amphibius*) to maximize sequence quality under computational constraints. Seven genes of interest were isolated, uniformly truncated, and aligned via Clustal Omega. 

**Phylogenetic Metrics**
* **Model Selection:** A JC+G(4)+I model (or equivalent optimal substitution model) was selected using `phangorn` based on having the lowest BIC and AIC scores.
* **Tree Topology:** The RAxML phylogenetic tree demonstrated strong nodal support across major lineages, clearly separating the Mysticeti and Odontoceti suborders. 

**Trait Evolution**
Ancestral state reconstruction was performed utilizing a custom transition matrix to infer the evolutionary pathways of cognitive traits. Log-transformed brain size was tracked continuously, while a subset of species was evaluated using custom 1-5 scales for vocalization and social complexity. For instance, *Tursiops truncatus* (Bottlenose Dolphin) scored highly for fluid, multilevel alliances and complex signature whistles. Species with these advanced cognitive capacities demonstrated convergent patterns of significant brain mass expansion relative to ancestral nodes.

---

### Limitations and Future Improvements

The analysis was primarily constrained by computational power and time, which required downsampling the initial dataset to 19 species. Multi-gene concatenations can also sometimes mask individual gene tree conflicts. 

Future improvements to this pipeline could include:

* **Expanded Dataset:** Running the sequence alignment and RAxML tree construction on all 36 initially identified species to achieve a higher-resolution phylogeny.
* **Genomic Coverage:** Expanding the scope from targeted genes to a broader phylogenomic approach to increase topological resolution.
* **Reproducibility:** Streamlining the individual R and Bash scripts into an automated workflow manager (like Nextflow) to increase efficiency.
---

### Repository Structure

```text
├── data/
│   ├── metadata/                           
│   │   └── mapping.csv.txt                 # Mapping tips to full names
│   │
│   ├── raw_sequences/
│   │   ├── all_overlaps_trimmed_clean.fasta# Cleaned intermediate sequence (invalid chars replaced)
│   │   ├── cetaceans.fasta                 # Broad cetacean raw sequences
│   │   ├── clean_cetacean.fasta.zip        # Cleaned broad cetacean sequences 
│   │   └── language_ceteceans.fasta        # Filtered 9-species raw sequences
│   │
│   ├── processed_alignments/
│   │   ├── language_ceteceans_aligned.fasta# Clustal Omega output (9 species)
│   │   ├── languageConcat.phy              # RAxML matrix (9 species)
│   │   ├── languageConcat.nex              # NEXUS matrix (9 species)
│   │   ├── language-Raxml-part.txt         # Gene boundaries (9 species)
│   │   ├── cetaceans_aligned.fasta         # Clustal Omega output (20 species)
│   │   ├── cetaceansConcat.phy             # RAxML matrix (20 species)
│   │   ├── cetaceansConcat.nex             # NEXUS matrix (20 species)
│   │   └── cetaceans-Raxml-part.txt        # Gene boundaries (20 species)
│   │
│   └── phenotypic_data/
│       ├── phenotypic_data.xlsx - DATA.csv       # Brain mass & complexity scores (for ASR)
│       ├── phenotypic_data.xlsx - TIP_DATES.csv  # FAD/LAD dates (for calibration)
│       └── phenotypic_data.xlsx - Node_Dates.csv # Internal node ages (for calibration)
├── scripts/
│   ├── final.Rmd                           # MASTER NOTEBOOK: R code, SLURM commands, and full phylogenetic pipeline
│   │
│   ├── data_prep_scripts/
│   │   ├── clean_fasta_file.py             # Replaces invalid DNA characters with 'N' (Used in final pipeline)
│   │   ├── clean_fasta_fully.py            # Deletes invalid characters entirely (Alternate draft, not used in final)
│   │   ├── fix_lengths_post_alignment.py   # Recalculates partition boundaries by counting new alignment gaps
│   │   ├── separate_sequences.py           # Splits a monolithic PHYLIP file into individual FASTA files
│   │   ├── subset_fasta.py                 # Filters the master sequence file down to your target taxa
│   │   └── trim_sequences.py               # Truncates all sequences to exactly 7,392 base pairs prior to alignment
│   │
│   ├── qc_and_validation/
│   │   ├── check_fasta_cleaned.py          # Validates FASTA formatting, missing headers, and valid characters
│   │   ├── check_lengths.py                # Uses Biopython to verify all sequences are uniform in length
│   │   ├── check_taxa_fasta.py             # Utility to print out every species currently residing in a FASTA file
│   │   ├── checkfiltering.py               # Cross-references FASTA and PHYLIP files to ensure no data was dropped
│   │   ├── choose_best_sequence.py         # Calculates ambiguity percentage to pick the highest-quality dolphin sequence
│   │   ├── compare_best_sequences.py       # Sorts all sequences from best to worst based on 'N' counts and gaps
│   │   └── verify_order.py                 # Sanity check to ensure taxa order didn't scramble during alignment
│   │
│   └── exploratory_scripts/               
│       ├── checkoverlap.py                 # Compares and verifies dual taxa sets using hardcoded lists
│       ├── filtertaxa.py                   # Draft script for filtering taxa from a PHYLIP file
│       ├── find_overlaps.py                # Advanced overlap check mapping full scientific names to nicknames
│       └── taxanames.py                    # Extracts and prints a raw list of all species inside a PHYLIP file
├── results/
│   ├── model_testing/
│   │   └── modelTest_results.txt             # AIC/BIC scores for substitution model selection
│   │
│   └── raxml_trees/
│       ├── RAxML_bestTree.languageboot       # Final ML tree for 9-species language subset (Newick format)
│       ├── RAxML_bootstrap.languageboot      # Raw bootstrap replicates for language subset
│       ├── RAxML_bestTree.cetaceansboot      # Final ML tree for 20-species brain mass dataset
│       ├── RAxML_bootstrap.cetaceansboot     # Raw bootstrap replicates for 20-species dataset
│       └── RAxML_bestTree.cetaceansraxml     # Alternate ML tree run
├── figures/
│   ├── ASRbrain.png                         # Final brain mass evolutionary mapping
│   ├── ASRlanguage.png                      # Final language complexity evolutionary mapping
│   ├── Improved_RAxML_Tree.pdf              # Polished phylogenetic tree with bootstrap values
│   └── heatmap.png                          # Genetic/trait distance matrix visualization
├── Final_Project_BINF_6205.pdf              # Full academic project report
└── README.md                                # Project documentation
