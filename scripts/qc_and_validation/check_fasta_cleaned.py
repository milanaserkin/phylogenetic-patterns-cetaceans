def validate_fasta(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        is_fasta = True
        has_errors = False
        
        for line_num, line in enumerate(lines):
            line = line.strip()
            
            # Check for missing or malformed headers
            if line.startswith('>'):
                if not line[1:]:  # Check if header is empty after '>'
                    print(f"Error: Missing header content on line {line_num + 1}")
                    has_errors = True
            elif line == '':
                # Skip empty lines
                continue
            else:
                # Check for unexpected characters in sequences
                if not all(base in 'ATCGN-' for base in line.upper()):
                    print(f"Error: Invalid characters detected in sequence at line {line_num + 1}")
                    has_errors = True

        if not has_errors:
            print("The FASTA file appears to be valid.")
        else:
            print("Errors were found in the FASTA file.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'subset_taxa_sequences_cleaned.fasta' with your file path
validate_fasta('all_overlaps_trimmed_clean.fasta')

