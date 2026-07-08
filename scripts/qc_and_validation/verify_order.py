from Bio import SeqIO

# File paths
input_file = "cetacean_final.fasta"
output_file = "cetacean_alignment.fasta"

# Read the sequences from the input and output files
input_seqs = list(SeqIO.parse(input_file, "fasta"))
output_seqs = list(SeqIO.parse(output_file, "fasta"))

# Extract the IDs of the sequences
input_ids = [seq.id for seq in input_seqs]
output_ids = [seq.id for seq in output_seqs]

# Print the order of taxa in each file
print("Order of taxa in the input file:")
for idx, taxon in enumerate(input_ids):
    print(f"{idx + 1}: {taxon}")

print("\nOrder of taxa in the output file:")
for idx, taxon in enumerate(output_ids):
    print(f"{idx + 1}: {taxon}")

