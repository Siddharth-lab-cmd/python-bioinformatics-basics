def sliding_window_gc(dna_string, window_size, step_size):
    print("🔎 --- Chromosomal Sliding Window Analysis --- 🔎")
    print(f"Total DNA Chain Length: {len(dna_string)} | Window Size: {window_size}bp\n")

    for i in range(0, len(dna_string) - window_size + 1, step_size):
        sub_seq = dna_string[i:i+window_size]
        g_count = sub_seq.count('G')
        c_count = sub_seq.count('C')
        gc_score = ((g_count + c_count) / window_size) * 100
        print(f"Coordinates [{i}:{i+window_size}] -> Sequence Window: {sub_seq} -> GC Content: {gc_score:.1f}%")

sample_chromosome = "ATCGATCGATGGATCGATCGATCG"
sliding_window_gc(sample_chromosome, window_size=8, step_size=4)
