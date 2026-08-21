def find_dna_motif_coordinates(dna_sequence, target_motif):
    """Locates the exact starting index positions of a specific DNA motif pattern."""
    dna_sequence = dna_sequence.upper().strip()
    target_motif = target_motif.upper().strip()
    
    match_coordinates = []
    motif_length = len(target_motif)
    
    print("🔬 SCANNING GENOMIC STRAND FOR REGULATORY MOTIF PATTERNS...")
    print(f"Target Sequence : {dna_sequence}")
    print(f"Search Motif    : {target_motif}\n")
    
    # Slide across the sequence base by base
    for i in range(len(dna_sequence) - motif_length + 1):
        window = dna_sequence[i:i + motif_length]
        if window == target_motif:
            match_coordinates.append(i)
            
    return match_coordinates

# Simulating a bacterial gene sequence containing a conserved promoter signal (TATAAT)
bacterial_dna = "AGCTATATAATGGCCGATCCTATAATGCAT"
search_pattern = "TATAAT"

indices = find_dna_motif_coordinates(bacterial_dna, search_pattern)

print("📊 SCAN COMPLETION SUMMARY:")
print("-" * 40)
print(f"Total Matches Found : {len(indices)}")
print(f"Mapped Position IDs : Localization index coordinates at {indices}")
