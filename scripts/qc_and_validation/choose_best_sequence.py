from Bio import SeqIO

# File path to the FASTA file
file_path = "all_overlaps.fasta"

# Sequence IDs to check
target_ids = ["Dcap108471", "Dcap79929", "Ddeltrop4525", "DdelSJR"]

# Initialize variables for the best sequence
best_sequence = None
best_length = 0

# Iterate over each sequence in the FASTA file
for record in SeqIO.parse(file_path, "fasta"):
    if record.id in target_ids:
        print(f"Sequence ID: {record.id}")
        print(f"Length: {len(record)}")
        print(f"Ambiguous Base Percentage: {100 * sum(1 for base in record.seq if base not in 'ACGT') / len(record):.2f}%")

        # Update the best sequence if this one is longer
        if len(record) > best_length:
            best_length = len(record)
            best_sequence = record

# Print the best sequence found
if best_sequence:
    print("\nBest Sequence Found:")
    print(f"ID: {best_sequence.id}")
    print(f"Length: {len(best_sequence)}")
    print(f"Ambiguous Base Percentage: {100 * sum(1 for base in best_sequence.seq if base not in 'ACGT') / len(best_sequence):.2f}%")
else:
    print("\nNo matching sequences found.")


