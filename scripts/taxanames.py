# Path to the PHYLIP file
file_path = "/Users/milana/Downloads/DATASET_B(1).phylip"

# Open the file and process lines
with open(file_path, "r") as f:
    lines = f.readlines()

# Skip the first line (header) and handle potential empty lines
taxa = []
for line in lines[1:]:
    if line.strip():  # Skip empty lines
        parts = line.split()
        if parts:  # Check if the line has content
            taxa.append(parts[0])  # Take the first column as the taxon name

# Print the taxa names
for index, taxon in enumerate(taxa, start=1):
    print(f"{index}: {taxon}")

# Optionally save the taxa names to a file
with open("taxa_list.txt", "w") as output:
    output.write("\n".join(taxa))

