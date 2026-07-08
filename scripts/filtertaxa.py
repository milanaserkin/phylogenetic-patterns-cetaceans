file_path = "/Users/milana/Desktop/BINF6205/final/DATASET_B(1).phylip"

# Desired taxa to select
desired_taxa = nicknames = [ 
    "Bmys", 
    "Bbor", 
    "Bmus49099", 
    "Bphy_baits", "Bphy", 
    "Cmar59905", 
    "Chea7320", 
    "Dleu", 
    "Dcap108471", "Dcap79929", "Ddeltrop4525", "DdelSJR", 
    "Erob133443", 
    "Gmac39091", 
    "Gmel", 
    "Ggri", 
    "Igeo", 
    "Ksim", 
    "Lacu", 
    "Lalb", 
    "Lobl", 
    "Lobs", 
    "Lvex", 
    "Lbor", 
    "Mnov", 
    "Mden", 
    "Meur", 
    "Mmir", 
    "Mmon", 
    "Npho", 
    "Oorc", 
    "Ppho", 
    "Pdal", 
    "Pmac", 
    "Pbla7349", 
    "Pcra123188", 
    "Scly1726", "Scly1724", 
    "Scoe", 
    "Slon24923", "Slon16012", 
    "Sbre116871", "Sbre18437", 
    "Ttru", 
    "Zcav", 
    "Hippo", 
]



with open(file_path, "r") as file:
    lines = file.readlines()

taxa_dict = {}
for line in lines[1:]:
    parts = line.split()
    if len(parts) > 1:
        taxon = parts[0]
        sequence = parts[1:]
        taxa_dict[taxon] = sequence

# Filter sequences for the desired taxa
selected_sequences = {taxon: taxa_dict[taxon] for taxon in desired_taxa if taxon in taxa_dict}

# Write the selected sequences to a new file
with open("all_overlaps.phylip", "w") as out:
    out.write(f"{len(selected_sequences)}{len(next(iter(selected_sequences.values())))}\n")
    for taxon, sequence in selected_sequences.items():
        out.write(f"{taxon} {' '.join(sequence)}\n")

