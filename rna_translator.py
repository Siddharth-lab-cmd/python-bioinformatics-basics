def translate_rna_to_protein(rna_sequence):
    """Translates an mRNA sequence into a corresponding protein chain."""
    # Official Genetic Code Codon Table
    codon_table = {
        'AUG': 'M (Methionine - START)', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
        'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
        'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H',
        'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R',
        'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T',
        'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V',
        'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G',
        'GGA': 'G', 'GGG': 'G', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }
    
    rna_sequence = rna_sequence.upper().strip()
    protein_chain = []
    
    # Process the sequence in chunks of 3 bases (Codons)
    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, '?')
        
        if amino_acid == 'STOP':
            protein_chain.append('[STOP]')
            break
        protein_chain.append(amino_acid)
        
    return "-".join(protein_chain)

# Test sequence tracking a synthetic food-enzyme marker
sample_mrna = "AUGUUUUCUUAUUGUUGGUAA"
print("🧬 RUNNING COMPUTATIONAL RIBOSOMAL TRANSLATION ENGINE...")
print(f"Input mRNA Strand : {sample_mrna}")

resulting_protein = translate_rna_to_protein(sample_mrna)
print(f"Output Protein    : {resulting_protein}")
