def generate_phylogenetic_distance_matrix(strains_dict):
    """Compiles a complete distance matrix tracking point mutations between multiple strains."""
    strain_names = list(strains_dict.keys())
    num_strains = len(strain_names)
    
    print("✂️ COMPILING MULTI-STRAIN EVOLUTIONARY DISTANCE MATRIX...")
    # Print the horizontal header column row
    header_line = "            " + "".join(f"{name:<15}" for name in strain_names)
    print(header_line)
    print("-" * len(header_line))
    
    for name_a in strain_names:
        row_values = []
        for name_b in strain_names:
            seq_a = strains_dict[name_a].upper().strip()
            seq_b = strains_dict[name_b].upper().strip()
            
            # Count the point mutations (Hamming Distance)
            mutations = sum(1 for base_a, base_b in zip(seq_a, seq_b) if base_a != base_b)
            row_values.append(mutations)
            
        # Print current row with beautiful grid alignment
        matrix_row = f"{name_a:<11} | " + "".join(f"{val:<15}" for val in row_values)
        print(matrix_row)

# Comparing four viral outbreaks from different food production plants
outbreak_samples = {
    "Plant_Alpha": "ATGCGTAC",
    "Plant_Beta":  "ATGCGTTC", # 1 mutation away from Alpha
    "Plant_Gamma": "ATGGGTTC", # 2 mutations away from Alpha
    "Plant_Delta": "TTGGGTTC"  # 3 mutations away from Alpha
}

generate_phylogenetic_distance_matrix(outbreak_samples)
