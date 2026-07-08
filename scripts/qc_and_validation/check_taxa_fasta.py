def get_taxa_from_fasta(file_path):
    try:
        taxa = []
        with open(file_path, 'r') as file:
            for line in file:
                # Check if the line is a header (starts with ">")
                if line.startswith(">"):
                    # Extract the taxon name (remove the ">" and any trailing newline/whitespace)
                    taxon = line[1:].strip()
                    taxa.append(taxon)

        # Print the taxa names
        if taxa:
            print("Taxa found in the FASTA file:")
            for taxon in taxa:
                print(taxon)
        else:
            print("No taxa found in the FASTA file.")
            
        return taxa

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Replace 'your_fasta_file.fasta' with the path to your FASTA file
fasta_file_path = 'cetaceans.fasta'
taxa_list = get_taxa_from_fasta(fasta_file_path)


