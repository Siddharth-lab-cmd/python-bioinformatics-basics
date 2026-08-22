def build_mutation_distance_grid(sequence_dict):
    """Computes a structural cross-comparison matrix mapping point mutations."""
    print("🧬 COMPILING POPULATION GENETIC DISTANCE GRID LOGS...")
    print("-" * 60)
    
    labels = list(sequence_dict.keys())
    print(f"{'Strain Map':<12} | " + " | ".join(f"{lbl:<10}" for lbl in labels))
    print("-" * (15 + 13 * len(labels)))
    
    for label_a in labels:
        row_values = []
        for label_b in labels:
            seq_a = sequence_dict[label_a].upper()
            seq_b = sequence_dict[label_b].upper()
            
            # Match character distances step by step
            distance = sum(1 for base_a, base_b in zip(seq_a, seq_b) if base_a != base_b)
            row_values.append(distance)
            
        print(f"{label_a:<12} | " + " | ".join(f"{val:<10}" for val in row_values))
    print("-" * (15 + 13 * len(labels)))
    print("✅ COMPUTE LOG: POPULATION DIVERGENCE TREE VERIFIED STABLE.")

# Mock strands tracking a small mutation trajectory
viral_variants = {
    "Strain_Alpha": "ATGCEEE",
    "Strain_Beta":  "ATGCGGG",
    "Strain_Gamma": "ATGCFFF"
}
build_mutation_distance_grid( viral_variants )
