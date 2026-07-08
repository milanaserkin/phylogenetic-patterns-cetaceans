from Bio import SeqIO

def truncate_sequences(input_file, output_file, cutoff_position):
    """
    Truncate sequences in the input FASTA file at the given position and save them to a new file.
    
    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output FASTA file.
        cutoff_position (int): The 1-based position at which to truncate each sequence.
    """
    with open(output_file, "w") as output_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            truncated_seq = record.seq[:cutoff_position]  # Truncate sequence
            record.seq = truncated_seq  # Update the sequence in the record≈y
            SeqIO.write(record, output_handle, "fasta")

# Input parameters
input_fasta = "all_overlaps.fasta"  # Replace with your input FASTA file path
output_fasta = "all_overlaps_trimmed.fasta"  # Replace with your desired output FASTA file path
cutoff_position = 7392  # Truncate at position 19,011 (1-based index)

# Run the truncation
truncate_sequences(input_fasta, output_fasta, cutoff_position)

