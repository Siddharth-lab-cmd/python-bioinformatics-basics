def locate_open_reading_frames(dna_sequence):
    """Scans a genomic strand to isolate functional Open Reading Frames (ORFs)."""
    dna_sequence = dna_sequence.upper().strip()
    detected_orfs = []
    
    print("🧬 RUNNING DE NOVO GENE PREDICTION ENGINE (ORF SCANNER)...")
    print(f"Input Sequence Matrix: {dna_sequence}\n")
    
    # Scan through the sequence
    i = 0
    while i < len(dna_sequence) - 2:
        # Look for the canonical START codon (ATG)
        if dna_sequence[i:i+3] == "ATG":
            for j in range(i + 3, len(dna_sequence) - 2, 3):
                codon = dna_sequence[j:j+3]
                # Look for standard STOP codons
                if codon in ["TAA", "TAG", "TGA"]:
                    orf_segment = dna_sequence[i:j+3]
                    detected_orfs.append((i, j+3, orf_segment))
                    i = j # Move pointer forward past this ORF
                    break
        i += 1
        
    return detected_orfs

# Sample sequence containing a hidden bacterial gene fragment
raw_bacterial_sequence = "CCGATGCATTCGATCGATCGATAGGATC"
found_genes = locate_open_reading_frames(raw_bacterial_sequence)

print("🎯 TRANSCRIPT PROCESSING RESULTS:")
print("-" * 55)
for index, (start, end, fragment) in enumerate(found_genes):
    print(f"Gene #{index+1:<2} | Coordinate Indices: [{start}:{end}] | Sequence: {fragment}")
