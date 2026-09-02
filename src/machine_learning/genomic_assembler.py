

cat << 'EOF' > genomic_assembler.py
def calculate_overlap(string_a, string_b, min_length=5):
    """Calculates the exact overlapping sequence boundary between two data fragments."""
    start = 0
    while True:
        start = string_a.find(string_b[:min_length], start)
        if start == -1:
            return 0
        if string_b.startswith(string_a[start:]):
            return len(string_a) - start
        start += 1

def assemble_fragments(fragment_list):
    print("🧬 Initializing De Novo Matrix Sequence Assembly...")
    sequences = fragment_list.copy()
    
    while len(sequences) > 1:
        max_overlap = 0
        best_pair = (0, 0)
        
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i != j:
                    overlap = calculate_overlap(sequences[i], sequences[j])
                    if overlap > max_overlap:
                        max_overlap = overlap
                        best_pair = (i, j)
                        
        if max_overlap == 0:
            print("⚠️ Zero overlapping boundaries detected. Halting pipeline execution.")
            break
            
        i, j = best_pair
        print(f"🧩 Merging fragment boundaries with an overlap of: {max_overlap} Base Pairs")
        sequences[i] = sequences[i] + sequences[j][max_overlap:]
        sequences.pop(j)
        
    return sequences[0]

if __name__ == "__main__":
    fragments = [
        "ACCAGTTGACCA",
        "TGACCATTGATC",
        "TTGATCGGATCC",
        "GGATCCATAGAA"
    ]
    assembled_contig = assemble_fragments(fragments)
    print(f"\n👑 Final Assembled Genomic Contig Sequence: {assembled_contig}")
EOF
