# List 1: First set of taxa to compare
taxa_set_1 = [
    "Bmys", "Bbor", "Bmus49099", "Bphy_baits", "Cmar59905", "Chea7320", 
    "Dleu", "DdelSJR", "Erob133443", "Gmac39091", "Gmel", "Ggri", "Igeo", 
"Ksim", 
    "Lacu", "Lalb", "Lobl", "Lobs", "Lvex", "Lbor", "Mnov", "Mden", 
"Meur", "Mmir", 
    "Mmon", "Npho", "Oorc", "Pdal", "Ppho", "Pmac", "Pbla7349", 
"Pcra123188", "Scoe", 
    "Ttru", "Zcav"
]

# List 2: Second set of taxa to compare
taxa_set_2 = [
    "Bmys", "Bbor", "Bmus49099", "Bphy_baits", "Bise", "Cmar59905", 
"Chea7320", 
    "Dleu", "DdelSJR", "Erob133443", "Gmac39091", "Gmel", "Ggri", "Igeo", 
"Ksim", 
    "Lacu", "Lalb", "Lobl", "Lobs", "Lvex", "Lbor", "Mnov", "Mden", 
"Meur", "Mmir", 
    "Mmon", "Npho", "Oorc", "Pdal", "Ppho", "Pmac", "Pbla7349", 
"Pcra123188", "Scly", 
    "Scoe", "Slon", "Sbre", "Ttru", "Zcav"
]

# Convert both lists to sets for easier comparison
set_1 = set(taxa_set_1)
set_2 = set(taxa_set_2)

overlap = set_1.intersection(set_2)

# Find the differences (taxa that don't overlap)
only_in_set_1 = set_1.difference(set_2)
only_in_set_2 = set_2.difference(set_1)

# Print the results
print(f"Overlap between the two sets: {overlap}")
print(f"Taxa in set 1 but not in set 2: {only_in_set_1}")
print(f"Taxa in set 2 but not in set 1: {only_in_set_2}")
