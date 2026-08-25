def fastq_quality_filter(fastq_records, quality_threshold=25):
    filtered_output = []
    print("🛡️ --- Raw FASTQ Stream Filter Engine --- 🛡️")

    for header, sequence, quality_string in fastq_records:
        numerical_scores = [ord(char) - 33 for char in quality_string]
        average_score = sum(numerical_scores) / len(numerical_scores)

        if average_score >= quality_threshold:
            filtered_output.append((header, sequence))
            print(f"[PASS] Read {header} verified cleanly. Mean Phred Score: {average_score:.1f}")
        else:
            print(f"[DROP] Read {header} rejected below threshold! Mean Phred Score: {average_score:.1f}")

    return filtered_output

mock_fastq_stream = [
    ("@Read_01", "ATCGATCG", "IIIIIIII"), 
    ("@Read_02", "ATGGATCG", "!!!!!!!!!") 
]
clean_reads = fastq_quality_filter(mock_fastq_stream, quality_threshold=25)
