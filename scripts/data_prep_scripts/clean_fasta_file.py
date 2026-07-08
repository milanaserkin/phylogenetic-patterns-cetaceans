def clean_fasta(input_file, output_file):
    """
    Cleans a FASTA file by replacing invalid characters in sequences with 'N'.
    
    Parameters:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to save the cleaned FASTA file.
    """
    valid_chars = set("ATGCatgcNn-")  # Valid nucleotide characters
    cleaned_lines = []  # List to store cleaned lines
    
    with open(input_file, "r") as infile:
        for line in infile:
            if line.startswith(">"):
                # Keep header lines as is
                cleaned_lines.append(line.strip())
            else:
                # Replace invalid characters with 'N'
                cleaned_sequence = "".join([char if char in valid_chars else "N" for char in line.strip()])
                cleaned_lines.append(cleaned_sequence)
    
    # Write the cleaned sequences to the output file
    with open(output_file, "w") as outfile:
        outfile.write("\n".join(cleaned_lines) + "\n")
    
    print(f"Cleaned FASTA file written to {output_file}")


# File paths
input_file = "all_overlaps_trimmed.fasta"
output_file = "all_overlaps_trimmed_clean.fasta"

# Clean the FASTA file
clean_fasta(input_file, output_file)

