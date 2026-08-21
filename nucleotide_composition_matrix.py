def generate_composition_matrix(sequence_database):
    """Generates a comprehensive composition table summary from a multi-sequence database."""
    print("📊 COMPILING MULTI-STRAIN GENOMIC MATRIX CALCULATIONS...")
    print(f"{'Sample ID':<12} | {'A%':<6} | {'T%':<6} | {'G%':<6} | {'C%':<6}")
    print("-" * 45)
    
    matrix_summary = {}
    
    for sample_id, sequence in sequence_database.items():
        sequence = sequence.upper().strip()
        length = len(sequence)
        
        if length == 0:
            continue
            
        # Matrix percentage calculations
        a_pct = (sequence.count('A') / length) * 100
        t_pct = (sequence.count('T') / length) * 100
        g_pct = (sequence.count('G') / length) * 100
        c_pct = (sequence.count('C') / length) * 100
        
        matrix_summary[sample_id] = {'A': a_pct, 'T': t_pct, 'G': g_pct, 'C': c_pct}
        print(f"{sample_id:<12} | {a_pct:<5.1f}% | {t_pct:<5.1f}% | {g_pct:<5.1f}% | {c_pct:<5.1f}%")
        
    return matrix_summary

# Comparing three distinct crop variations
crop_strains = {
    "Strain_Alpha": "ATGCGTACGTAC",
    "Strain_Beta":  "AAAAATTTTTGG",
    "Strain_Gamma": "GGGGCCCCATAT"
}

generate_composition_matrix(crop_strains)
