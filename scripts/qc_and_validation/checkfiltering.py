input_fasta_path = 'language_ceteceans.fasta'
input_phy_path = 'all_overlaps.phylip'


try:
    # Read the input FASTA file
    with open(input_fasta_path, 'r') as fasta_file:
        fasta_lines = fasta_file.readlines()
        fasta_data = fasta_lines[1:]  # Skip the header
        taxa_sequences_fasta = {}

        # Parse each line of the FASTA data
        for line in fasta_data:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                taxon, sequence = parts
                taxa_sequences_fasta[taxon] = sequence.strip()

    # Read the input PHYLIP file
    with open(input_phy_path, 'r') as phy_file:
        phy_lines = phy_file.readlines()
        taxa_sequences_phy = {}

        # Skip the header line and parse the rest
        for line in phy_lines[1:]:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                taxon, sequence = parts
                taxa_sequences_phy[taxon] = sequence.strip()

    # Compare the two datasets
    mismatches = []
    for taxon, fasta_sequence in taxa_sequences_fasta.items():
        if taxon in taxa_sequences_phy:
            phy_sequence = taxa_sequences_phy[taxon]
            if fasta_sequence != phy_sequence:
                mismatches.append((taxon, "Sequence mismatch"))
        else:
            mismatches.append((taxon, "Taxon missing in PHYLIP"))

    # Identify extra taxa in PHYLIP not in FASTA
    for taxon in taxa_sequences_phy:
        if taxon not in taxa_sequences_fasta:
            mismatches.append((taxon, "Extra taxon in PHYLIP"))

    # Print results
    if mismatches:
        print("Mismatches found:")
        for mismatch in mismatches:
            print(f"{mismatch[0]}: {mismatch[1]}")
    else:
        print("No mismatches found. FASTA and PHYLIP are consistent.")

except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


