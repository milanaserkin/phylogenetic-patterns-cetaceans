input_file_path = 'subset_taxa_sequences.phylip'  # Input file is in the same directory

try:
    # Read the input phylip file and separate each taxon
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        taxa = []  # List to store taxa names and sequences

        # Extract header and data lines
        header = lines[0]
        data_lines = lines[1:]

        # Parse each line of the phylip data
        for line in data_lines:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                taxon, sequence = parts
                taxa.append((taxon, sequence))

    # Create individual files for each taxon
    for taxon, sequence in taxa:
        file_name = f"{taxon}.fasta"
        with open(file_name, 'w') as taxon_file:
            # Write the sequence in phylip format
            taxon_file.write(f"1 {len(sequence.strip())}\n")  # PHYLIP header
            taxon_file.write(f"{taxon} {sequence.strip()}\n")  # Taxon and sequence

    print("Files successfully created for each taxon.")

except FileNotFoundError:
    print("Input file not found. Please ensure is in the same directory.")

