def compute_genomic_gc_skew(dna_strand, window_size=4):
    """Calculates sliding-window GC Skew to localize genomic replication origins."""
    dna_strand = dna_strand.upper().strip()
    skew_profile = []
    
    print(f"📊 COMPUTING CHROMOSOMAL GC SKEW (Sliding Window Size: {window_size})...")
    print(f"{'Window Coordinates':<20} | {'Sub-Sequence':<15} | {'Computed Skew Value':<20}")
    print("-" * 62)
    
    for i in range(0, len(dna_strand) - window_size + 1, window_size):
        sub_seq = dna_strand[i:i+window_size]
        g_count = sub_seq.count('G')
        c_count = sub_seq.count('C')
        
        # Calculate skew formula: (G - C) / (G + C)
        if (g_count + c_count) == 0:
            skew_value = 0.0
        else:
            skew_value = (g_count - c_count) / (g_count + c_count)
            
        skew_profile.append(skew_value)
        print(f"Indices [{i:<2}:{i+window_size:<2}]       | {sub_seq:<15} | {skew_value:<20.2f}")
        
    return skew_profile

# Mock bacterial genome ring segment
bacterial_genome_segment = "GGGGCCCCATATGGGG"
compute_genomic_gc_skew(bacterial_genome_segment)
