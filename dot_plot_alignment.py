def generate_text_dot_plot(seq1, seq2):
    """Generates a text-based Dot Plot matrix to visually align two genetic sequences."""
    seq1, seq2 = seq1.upper().strip(), seq2.upper().strip()
    
    print("🎨 INITIALIZING STRUCTURAL GENOMIC DOT-PLOT VISUALIZATION...")
    print(f"Sequence 1 (Top) : {seq1}")
    print(f"Sequence 2 (Side): {seq2}\n")
    
    # Print the top horizontal header row
    print("    " + " ".join(seq1))
    print("  " + "-" * (len(seq1) * 2 + 3))
    
    # Build and print the structural alignment grid
    for base2 in seq2:
        row_chars = []
        for base1 in seq1:
            if base1 == base2:
                row_chars.append("█") # Visual indicator marker for a solid match coordinate
            else:
                row_chars.append(".") # Space placeholder for a mismatch
        print(f"{base2} | " + " ".join(row_chars))

# Comparing a wild-type genetic sequence segment against a mutant strand variant
strand_alpha = "ATCGATCG"
strand_beta  = "ATGGATCG"

generate_text_dot_plot(strand_alpha, strand_beta)
