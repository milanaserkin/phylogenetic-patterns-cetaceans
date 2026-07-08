# Dataset 1: List of taxa names
dataset1 = [
    "Albertocetus_meffordorum", "NMVP252567", "Aulophyseter_morricei", 
"Balaena_mysticetus", 
    "Balaenoptera_borealis", "Balaenoptera_musculus", 
"Balaenoptera_physalus", 
    "Basilosaurus_cetoides", "Basilosaurus_isis", "Caperea_marginata", 
"Cephalorhynchus_commersonii", 
    "Cephalorhynchus_heavisidii", "ChM_PV2761", "ChM_PV4961", 
"Dalanistes_ahmedi", "Delphinapterus_leucas", 
    "Delphinus_delphis", "Dorudon_atrox", "Eschrichtius_robustus", 
"Fucaia_goedertorum", 
    "Globicephala_macrorhynchus", "Globicephala_melas", "Grampus_griseus", 
"Inia_geoffrensis", 
    "Janjucetus_hunderi", "Kentriodon_pernix", "Kogia_breviceps", 
"Kogia_sima", "Lagenorhynchus_acutus", 
    "Lagenorhynchus_albirostris", "Lagenorhynchus_obliquidens", 
"Lagenorhynchus_obscurus", 
    "Lipotes_vexillifer", "Lissodelphis_borealis", 
"Llanocetus_denticrenatus", "Megaptera_novaeangliae", 
    "Mesoplodon_densirostris", "Mesoplodon_europaeus", "Mesoplodon_mirus", 
"Monodon_monoceros", 
    "Neophocaena_phocaenoides", "Orcinus_orca", 
"Orycterocetus_crocodilinus", "Parietobalaena_palmeri", 
    "Phocoena_phocoena", "Phocoena_spinipinnis", "Phocoenoides_dalli", 
"Physeter_macrocephalus", 
    "Piscobalaena_nana", "Platanista_gangetica", "Pontoporia_blainvillei", 
"Pseudorca_crassidens", 
    "Genus_Y_ChM_PV2757", "Rodhocetus_kasrani", "Saghacetus_osiris", 
"Schizodelphis_morckhoviensis", 
    "Simocetus_rayi", "Sotalia_fluviatilis", "Squalodon_calvertensis", 
"Squaloziphius_emlongi", 
    "Stenella_clymene", "Stenella_coeruleoalba", "Stenella_longirostris", 
"Steno_bredanensis", 
    "Tursiops_truncatus", "Xenorophus_n_sp._ChM_PV4266", 
"Xiphiacetus_bossi", "Xiphiacetus_cristatus", 
    "Ziphius_cavirostris", "Zygorhiza_kochii"
]

# Dataset 2: Dictionary of taxa names as keys
dataset2 = {
    "Peponocephala_electra": ["Pele"], "Balaenoptera_musculus": 
["Bmus49099"], 
    "Inia_geoffrensis": ["Igeo"], "Stenella_coeruleoalba": ["Scoe"], 
"Balaenoptera_acutorostrata": ["Bacu"], 
    "Cephalorhynchus_heavisidii": ["Chea7320"], 
"Lagenorhynchus_australis": ["Laus"], 
    "Kogia_brevirostris": ["Kbre"], "Balaenoptera_edeni": ["BedeAUS", 
"Bede66737"], 
    "Lipotes_vexillifer": ["Lvex"], "Mesoplodon_perrini": ["Mpni"], 
"Steno_bredanensis": ["Sbre116871", "Sbre18437"], 
    "Bos_taurus": ["Btau"], "Orcaella_brevirostris": ["Obre"], 
"Tursiops_truncatus": ["Ttru"], 
    "Lagenodelphis_hosei": ["Lhos452", "Lhos30470"], 
"Physeter_macrocephalus": ["Pmac"], 
    "Ovis_aries": ["Oari"], "Phocoena_phocoena": ["Ppho"], 
"Globicephala_melas": ["Gmel"], 
    "Feresa_attenuata": ["Fatt"], "Orcaella_heinsohnii": ["Ohei"], 
"Balaenoptera_physalus": ["Bphy_baits", "Bphy"], 
    "Mesoplodon_hectori": ["Mhec"], "Lagenorhynchus_obscurus": ["Lobs"], 
"Neophocaena_phocaenoides": ["Npho"], 
    "Balaenoptera_borealis": ["Bbor"], "Phocoenoides_dalli": ["Pdal"], 
"Mesolpodon_stejnegeri": ["Mste"], 
    "Vicugna_pacos": ["Vpac"], "Orcinus_orca": ["Oorc"], 
"Delphinapterus_leucas": ["Dleu"], 
    "Balaenoptera_bonaerensis": ["BbonAUS"], "Equus_caballus": ["Ecab"], 
"Gazella_arabica": ["Gaar"], 
    "Eubalaena_japonica": ["Ejap43864"], "Hippopotamus_amphibius": 
["Hippo"], "Eubalaena_glacialis": ["Egla13086"], 
    "Grampus_griseus": ["Ggri"], "Eubalaena_australis": ["EausAUS"], 
"Sotalia_guianensis": ["Sflu9837"], 
    "Kogia_sima": ["Ksim"], "Hyperoodon_ampullatus": ["Hamp"], 
"Mesoplodon_bowdoini": ["Mbow"], 
    "Berardius_bairdii": ["Bbai76728"], "Sus_scrofa": ["Sscr"], 
"Stenella_clymene": ["Scly1726", "Scly1724"], 
    "Lagenorhynchus_acutus": ["Lacu"], "Balaena_mysticetus": ["Bmys"], 
"Lissodelphis_peroni": ["LperAUS"], 
    "Lagenorhynchus_obliquidens": ["Lobl"], "Phocoena_spinnipinis": 
["Pspi"], 
    "Mesoplodon_carlhubbsi": ["Mcar"], "Mesoplodon_grayii": ["MgraAUS"], 
"Mesoplodon_gingkodens": ["Mgin"], 
    "Mesoplodon_densirostris": ["Mden"], "Eschrichtius_robustus": 
["Erob133443"], 
    "Panthalops_hodgsonii": ["Phod"], "Oryx_leucoryx": ["Orle"], 
"Monodon_monoceros": ["Mmon"], 
    "Pontoporia_blainvillei": ["Pbla7349"], "Caperea_marginata": 
["Cmar59905"], 
    "Mesoplodon_layardi": ["MlayAUS"], "Stenella_frontalis": ["Sfro7782", 
"Sfro7784"], 
    "Camelus_bactrianus": ["Cbac"], "Berardius_arnouxii": ["Barn"], 
"Choeropsis_liberiensis": ["Clib"], 
    "Megaptera_novaeangliae": ["Mnov"], "Lissodelphis_borealis": ["Lbor"], 
    "Mesoplodon_europaeus": ["Meur"], "Mesoplodon_bidens": ["Mbid"], 
    "Globicephala_macrorhynchus": ["Gmac39091"], "Stenella_attenuata": 
["Satt38219", "Satt18473"], 
    "Mesoplodon_peruvianus": ["Mper"], "Lagenorhynchus_albirostris": 
["Lalb"], 
    "Stenella_longirostris": ["Slon24923", "Slon16012"], 
"Sousa_chinensis": ["Schi"], 
    "Tursiops_aduncus": ["Tadu79924"], "Pseudorca_crassidens": 
["Pcra123188"], "Ziphius_cavirostris": ["Zcav"], 
    "Phocoena_dioptrica": ["Pdio"], "Tragelaphus_eurycerus": ["Treu2"], 
    "Tasmacetus_shepherdi": ["Tshe"], "Cephalorhynchus_commersoni": 
["Ccom40"], 
    "Hyperoodon_planifrons": ["Hpla9120"], "Delphinus_delphis": 
["Dcap108471", "Dcap79929", "Ddeltrop4525", "DdelSJR"], 
    "Mesoplodon_mirus": ["Mmir"], "Globicephala_gyrafus": ["Ggyf"], 
"Balaenoptera_rorquals": ["Brol"],
    "Basilosaurus_isis": ["Bisis"]
}

# Finding common taxa names between the two datasets
common_taxa = [taxon for taxon in dataset1 if taxon in dataset2]

# Output the common taxa names
print("Common taxa:")
print(common_taxa)

