def calculate_protein_hydrophobicity_index(peptide_sequence):
    """Maps the Kyte-Doolittle hydrophobicity index trends across a peptide chain."""
    # Standard Kyte-Doolittle chemical hydrophobicity scale mapping numbers
    hydrophobicity_scale = {
        'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
        'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
        'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
        'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
    }
    
    peptide_sequence = peptide_sequence.upper().strip()
    score_profile = []
    
    print("🔬 CALCULATING MOLECULAR HYDROPHOBICITY PROFILING INDEX...")
    print(f"{'Residue Position':<18} | {'Amino Acid':<12} | {'Hydrophobicity Score':<20}")
    print("-" * 58)
    
    for index, residue in enumerate(peptide_sequence):
        score = hydrophobicity_scale.get(residue, 0.0)
        score_profile.append(score)
        print(f"Position {index+1:<10} | {residue:<12} | {score:<20.2f}")
        
    avg_score = sum(score_profile) / len(score_profile) if score_profile else 0
    return avg_score

# Analyzing an active structural peptide string block from a whey milk protein
whey_peptide = "IVLGA"
overall_hydrophobicity = calculate_protein_hydrophobicity_index(whey_peptide)
print(f"\n📊 TOTAL COMPUTED STRUCTURAL MATRIX SCORE: {overall_hydrophobicity:.2f}")
