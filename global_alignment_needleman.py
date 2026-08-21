def simple_sequence_alignment_score(seq1, seq2, match=2, mismatch=-1, gap=-2):
    """Calculates a global alignment score between two sequences."""
    seq1, seq2 = seq1.upper(), seq2.upper()
    n, m = len(seq1), len(seq2)
    
    # Initialize a scoring matrix table grid
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill out the boundary gap penalty rows and columns
    for i in range(n + 1): score_matrix[i][0] = i * gap
    for j in range(m + 1): score_matrix[0][j] = j * gap
    
    # Populate the scoring matrix using dynamic calculation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i-1] == seq2[j-1]:
                score = score_matrix[i-1][j-1] + match
            else:
                score = score_matrix[i-1][j-1] + mismatch
                
            score_matrix[i][j] = max(score, score_matrix[i-1][j] + gap, score_matrix[i][j-1] + gap)
            
    return score_matrix[n][m]

print("📐 EXECUTING GLOBAL GENOMIC SEQUENCE ALIGNMENT MATRIX...")
gene_a, gene_b = "HELLOMC", "HELLOMGC"
final_score = simple_sequence_alignment_score(gene_a, gene_b)

print(f"Sequence Alpha    : {gene_a}")
print(f"Sequence Beta     : {gene_b}")
print(f"🏆 Final Alignment Alignment Score: {final_score}")
