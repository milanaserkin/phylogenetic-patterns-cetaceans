def clean_fasta(file_path, output_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cleaned_lines = []
        has_errors = False

        for line_num, line in enumerate(lines):
            line = line.strip()
            if line.startswith('>'):
                # Add header lines unchanged
                cleaned_lines.append(line)
            elif line == '':
                # Skip empty lines
                continue
            else:
                # Remove invalid characters and print a warning if found
                cleaned_sequence = ''.join(base for base in line.upper() if base in 'ATCGN')
                if len(cleaned_sequence) != len(line):
                    has_errors = True
                    print(f"Warning: Removed invalid characters in sequence at line {line_num + 1}")
                cleaned_lines.append(cleaned_sequence)

        # Write the cleaned sequences to a new output file
        with open(output_path, 'w') as output_file:
            for cleaned_line in cleaned_lines:
                output_file.write(cleaned_line + '\n')

        if not has_errors:
            print("The FASTA file was already clean.")
        else:
            print(f"Cleaned FASTA file saved as {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'subset_taxa_sequences_cleaned.fasta' with your input file path
# and specify the output file path
clean_fasta('cetaceans.fasta', 'fully_cleaned_cetaceans.fasta')

