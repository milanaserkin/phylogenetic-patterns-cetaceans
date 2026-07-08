from Bio import SeqIO

# Load the aligned sequence data
alignment = list(SeqIO.parse("language_ceteceans_aligned.fasta", "fasta"))

# Define the original gene segments (1 to 7392) as known
genes = {
    "AQP6": (1, 849),
    "FBXO2": (850, 1758),
    "FGG": (1759, 3099),
    "FOXP1": (3100, 4953),
    "HOXA13": (4954, 5919),
    "HOXA9": (5920, 6738),
    "HOXB7": (6739, 7392)
}

# Determine the number of gaps in the alignment
alignment_length = len(alignment[0].seq)
original_length = 7392
added_gaps = alignment_length - original_length

# Print information about the alignment
print(f"Original sequence length: {original_length}")
print(f"Alignment length: {alignment_length}")
print(f"Total added gaps: {added_gaps}\n")

# Adjust the gene boundaries for each gene
adjusted_genes = {}
for gene, (start, end) in genes.items():
    # The new end position should be adjusted by the number of added gaps
    adjusted_start = start
    adjusted_end = end + added_gaps  # Adjust end position based on added gaps
    
    # Print the adjusted boundaries
    print(f"Gene: {gene}")
    print(f"Original start: {start}, Original end: {end}")
    print(f"Adjusted start: {adjusted_start}, Adjusted end: {adjusted_end}\n")
    
    adjusted_genes[gene] = (adjusted_start, adjusted_end)

# The adjusted_genes dictionary now holds the new start and end positions

