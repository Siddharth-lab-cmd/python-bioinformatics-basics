
def optimize_codons_for_expression(amino_acid_sequence):
    """Optimizes an amino acid chain into highly preferred E. coli bacterial codons."""
    # E. coli highly preferred codon lookup chart
    bacterial_preference_table = {
        'M': 'ATG', 'F': 'TTC', 'L': 'CTG', 'S': 'TCT', 'Y': 'TAC',
        'C': 'TGC', 'W': 'TGG', 'P': 'CCG', 'H': 'CAC', 'Q': 'CAG',
        'R': 'CGT', 'I': 'ATC', 'T': 'ACC', 'N': 'AAC', 'K': 'AAA',
        'V': 'GTG', 'A': 'GCG', 'D': 'GAC', 'E': 'GAA', 'G': 'GGT'
    }
    
    amino_acid_sequence = amino_acid_sequence.upper().strip()
    optimized_dna_chunks = []
    
    for residue in amino_acid_sequence:
        codon = bacterial_preference_table.get(residue, 'NNN')
        optimized_dna_chunks.append(codon)
        
    return "".join(optimized_dna_chunks)

# Target target peptide segment to express inside a host cell matrix
target_peptide = "MKVLA"
optimized_dna = optimize_codons_for_expression(target_peptide)

print("⚙️ INITIATING SYNTHETIC BIOLOGY CODON OPTIMIZATION PIPELINE...")
print(f"Input Peptide Chain      : {target_peptide}")
print(f"🚀 Optimized DNA Sequence : {optimized_dna} (Engineered for high host cell expression)")
