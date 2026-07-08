from Bio import SeqIO

# Define file paths
fasta_files = ["language_ceteceans_aligned.fasta"]

# Function to calculate sequence lengths
def get_sequence_lengths(file_path):
    lengths = {}
    for record in SeqIO.parse(file_path, "fasta"):
        lengths[record.id] = len(record.seq)
    return lengths

# Print the sequence lengths for each file
for file in fasta_files:
    print(f"Lengths for {file}:")
    seq_lengths = get_sequence_lengths(file)
    for taxa, length in seq_lengths.items():
        print(f"{taxa}: {length} bases")
    print("\n")

