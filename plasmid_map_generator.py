def generate_text_plasmid_map(plasmid_name, sequence_length, features_dict):
    """Generates a text-based circular structural visualization map of a plasmid vector."""
    print(f"🧬 GENERATING RECOMBINANT PLASMID MAP: [{plasmid_name.upper()}]")
    print(f"📊 Total Sequence Length: {sequence_length} Base Pairs (bp)")
    print("-" * 55)
    
    # Create a visual representation of a circular loop
    print("      <-===-- ORIGINAL PLASMID BACKBONE --===>")
    print("   /                                             \\")
    
    for feature, (start, end) in features_dict.items():
        print(f"  |  📍 INSERT DETECTED: {feature:<12} | Coordinates: [{start} -> {end} bp]")
        
    print("   \\                                             /")
    print("      <========================================>")
    print("\n✅ PLASMID GENETIC SCHEMATIC VECTOR GENERATED SUCCESSFULLY.")

# Mapping an engineered plasmid used to produce food-grade lactase enzymes
engineered_features = {
    "Promoter_LacZ": (150, 280),
    "Target_Gene":    (320, 1450),
    "Amp_Resistance": (1600, 2200)
}

generate_text_plasmid_map("pBBAU-Food-Lactase", 2500, engineered_features)
