def count_nucleotide_frequencies(dna_sequence):
    """Counts the exact number of A, T, G, and C bases in a DNA strand."""
    dna_sequence = dna_sequence.upper().strip()
    
    # Initialize a dictionary to store our counts
    frequencies = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'Unknown': 0}
    
    for base in dna_sequence:
        if base in frequencies:
            frequencies[base] += 1
        else:
            frequencies['Unknown'] += 1
            
    return frequencies

# Mock DNA data representing an unknown pathogen isolated from a milk sample
food_pathogen_dna = "ATGCGTACGATCGACTAGCTAGCTAGCTAGCTAGC"

print("🧫 INITIATING FOOD SAFETY MOLECULAR FREQUENCY SCAN...")
print(f"Target Bacterial DNA Strand: {food_pathogen_dna}\n")

results = count_nucleotide_frequencies(food_pathogen_dna)

print("📊 COUNTS PER NUCLEOTIDE BASE:")
print("-" * 30)
for base, count in results.items():
    percentage = (count / len(food_pathogen_dna)) * 100
    print(f"Base {base} : {count:<3} | Percentage: {percentage:.1f}%")

print("-" * 30)
print("✅ MOLECULAR FREQUENCY SCAN PROCESSING COMPLETED SUCCESSFUL.")
