def compare_and_sort_sequences(file_path):
    try:
        # Dictionary to store sequences and their counts of unknowns
        sequence_data = {}

        # Read the FASTA file
        with open(file_path, 'r') as file:
            current_taxon = None
            current_sequence = []

            for line in file:
                if line.startswith(">"):
                    # Process the previous sequence
                    if current_taxon:
                        full_sequence = ''.join(current_sequence)
                        unknown_count = full_sequence.count("N") + full_sequence.count("-")
                        sequence_data[current_taxon] = (full_sequence, unknown_count)

                    # Start a new taxon
                    current_taxon = line[1:].strip()
                    current_sequence = []
                else:
                    # Append sequence lines
                    current_sequence.append(line.strip())

            # Process the last sequence in the file
            if current_taxon:
                full_sequence = ''.join(current_sequence)
                unknown_count = full_sequence.count("N") + full_sequence.count("-")
                sequence_data[current_taxon] = (full_sequence, unknown_count)

        # Sort the sequences based on the number of unknowns (ascending)
        sorted_sequences = sorted(sequence_data.items(), key=lambda x: x[1][1])

        # Display sorted sequences
        print("Sorted sequences by number of unknowns:")
        for taxon, (sequence, unknown_count) in sorted_sequences:
            print(f"{taxon}: {unknown_count} unknowns")
        
        return sorted_sequences

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Replace 'your_fasta_file.fasta' with the path to your FASTA file
fasta_file_path = 'all_overlaps_trimmed_clean.fasta'
sorted_sequences = compare_and_sort_sequences(fasta_file_path)


