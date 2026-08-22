def compute_codon_usage_matrix(rna_sequence):
    """Calculates relative frequency ratios across dynamic mRNA codon triplets."""
    rna_sequence = rna_sequence.upper().replace("T", "U").strip()
    print("🧬 INITIALIZING HIGH-THROUGHPUT mRNA CODON USAGE COMPILER...")
    print("-" * 60)
    
    # Slice character arrays into discrete triplets
    codons = [rna_sequence[i:i+3] for i in range(0, len(rna_sequence) - 2, 3) if len(rna_sequence[i:i+3]) == 3]
    
    codon_counts = {}
    for triplet in codons:
        codon_counts[triplet] = codon_counts.get(triplet, 0) + 1
        
    total_codons = len(codons)
    print(f"📊 Processed Sequence Grid: Total Identions = {total_codons} Codon blocks")
    print(f"{'Codon Triplet':<15} | {'Raw Counts':<12} | {'Relative Frequency (%)':<20}")
    print("-" * 60)
    
    for triplet, count in sorted(codon_counts.items()):
        frequency = (count / total_codons) * 100
        print(f"🎰 {triplet:<12} | {count:<12} | {frequency:<19.2f}%")
        
    print("✅ CELLULAR CODON BIAS DISTRIBUTION MATRIX CONCLUDED.")

# Mock sequence containing multiple targeted leucine and alanine codons
mock_transcript = "AUGGCUACUGACGUAUGGCUACUGACGUAA"
compute_codon_usage_matrix(mock_transcript)
