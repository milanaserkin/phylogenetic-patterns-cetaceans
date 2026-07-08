from Bio import SeqIO

# Define the list of taxa to select
selected_taxa = [
    "DdelSJR","Gmac39091", "Ggri", "Hippo", "Oorc",
    "Pmac", "Pcra123188", "Scoe", "Ttru"
]

# Input and output file names
input_file = "all_overlaps_trimmed_clean.fasta"
output_file = "language_ceteceans.fasta"

# Filter and write sequences to the new file
with open(output_file, "w") as outfile:
    for record in SeqIO.parse(input_file, "fasta"):
        # Check if the taxon name is in the selected taxa list
        if record.id in selected_taxa:
            SeqIO.write(record, outfile, "fasta")

print(f"Filtered sequences written to {output_file}.")

