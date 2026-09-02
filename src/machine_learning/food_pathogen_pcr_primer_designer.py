


def design_food_pathogen_pcr_primer(target_dna_sequence):
    """Designs a forward PCR primer and calculates its biochemical melting temperature."""
    target_dna_sequence = target_dna_sequence.upper().strip()
    print("🔬 INITIALIZING LAB-READY PCR PRIMER DESIGN INFRASTRUCTURE...")
    print("-" * 65)
    
    # Pick a standard 10-base pair primer from the start of the pathogen DNA
    primer_length = 10
    forward_primer = target_dna_sequence[0:primer_length]
    
    # Calculate GC count to find the melting temperature (Wallace Formula: Tm = 2*(A+T) + 4*(G+C))
    a_count = forward_primer.count('A')
    t_count = forward_primer.count('T')
    g_count = forward_primer.count('G')
    c_count = forward_primer.count('C')
    
    melting_temperature = (2 * (a_count + t_count)) + (4 * (g_count + c_count))
    
    print(f"🎯 Target Pathogen Stream : {target_dna_sequence}")
    print(f"🧬 Engineered Forward Primer: [{forward_primer}] (Length: {primer_length} bp)")
    print(f"🌡️ Computed Melting Temp  : {melting_temperature}°C")
    print("-" * 65)
    
    # Check if the primer is biochemically stable for a lab environment
    if 30 <= melting_temperature <= 45:
        print("✅ SYSTEM VERDICT: Primer matches structural limits. Ready for wet-lab testing.")
    else:
        print("⚠️ SYSTEM VERDICT: Temperature profile unstable. Redesign sequence boundaries.")

# Mock DNA sequence representing a dangerous food pathogen like Salmonella
salmonella_mock_dna = "ATGCGGCCAAATTTGGGCCCAAA"
design_food_pathogen_pcr_primer(salmonella_mock_dna)
