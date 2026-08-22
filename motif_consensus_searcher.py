def find_consensus_genetic_motif(sequence_list):
    """Calculates consensus string matches from alignment multi-sequence grids."""
    print("🔎 RUNNING ALGORITHMIC MATRIX SEARCH FOR CONSERVED GENE MOTIFS...")
    print(f"📋 Aligning {len(sequence_list)} target biological sequences...")
    print("-" * 60)
    
    seq_length = len(sequence_list[0])
    consensus_sequence = []
    
    # Calculate most frequent nucleotide at each vertical matrix location
    for i in range(seq_length):
        column_bases = [seq[i].upper() for seq in sequence_list]
        base_counts = {base: column_bases.count(base) for base in set(column_bases)}
        
        # Pick the winner using maximum distribution count
        winning_base = max(base_counts, key=base_counts.get)
        consensus_sequence.append(winning_base)
        
    final_motif = "".join(consensus_sequence)
    print(f"✨ Success: Consensus Motif Located ──> [{final_motif}]")
    return final_motif

# Mock collection of slightly mutated sequences from a single bacterial outbreak
outbreak_strains = [
    "GATTACA",
    "GATTCCA",
    "GATTGCA",
    "GATTTCA"
]
find_consensus_genetic_motif(outbreak_strains)
