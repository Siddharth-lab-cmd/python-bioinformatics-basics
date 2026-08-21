def calculate_gc_content(dna_sequence):
    """Calculates the percentage of G and C bases in a DNA sequence."""
    dna_sequence = dna_sequence.upper()
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    
    if len(dna_sequence) == 0:
        return 0
        
    return ((g_count + c_count) / len(dna_sequence)) * 100

# Sample dictionary representing raw DNA data collected from food bacteria
raw_genomic_data = {
    "Sample_01": "ATGCGATCGATCGATCGATC",
    "Sample_02": "ATATATATATATATATATAT",
    "Sample_03": "GGCGGCCGGCCGGCCGGCCG",
    "Sample_04": "CCGGTTTTAAAAGGGCCCAA"
}

print("🔬 STARTING BIOINFORMATICS DATA FILTERING PIPELINE...\n")
print(f"{'Sample ID':<12} | {'DNA Sequence':<22} | {'GC Content (%)':<15} | {'Status':<10}")
print("-" * 68)

# Filtering loop: Find highly stable gene samples (GC content above 50%)
for sample_id, sequence in raw_genomic_data.items():
    gc_percentage = calculate_gc_content(sequence)
    
    if gc_percentage > 50.0:
        status = "✅ PASS"
    else:
        status = "❌ FILTERED OUT"
        
    print(f"{sample_id:<12} | {sequence:<22} | {gc_percentage:<15.2f} | {status:<10}")

print("\n📊 DATA CLEANING COMPLETE. PIPELINE SUCCESSFUL.")
