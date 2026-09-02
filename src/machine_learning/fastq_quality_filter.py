def filter_fastq_reads(raw_fastq_records, minimum_quality_cutoff):
    """Filters sequencing reads based on average base call accuracy mapping."""
    clean_records = {}
    
    print("💾 INGESTING RAW ILLUMINA HIGH-THROUGHPUT FASTQ STREAMS...")
    for read_id, (sequence, quality_string) in raw_fastq_records.items():
        # Convert ASCII characters to standard Phred-33 scores
        quality_scores = [ord(char) - 33 for char in quality_string]
        average_quality = sum(quality_scores) / len(quality_scores)
        
        if average_quality >= minimum_quality_cutoff:
            clean_records[read_id] = sequence
            status = "✅ HIGH QUALITY PASS"
        else:
            status = "❌ LOW QUALITY DROPPED"
            
        print(f"Read: {read_id:<9} | Avg Phred Score: {average_quality:<5.1f} | Result: {status}")
        
    return clean_records

# Sample database containing data-heavy machine sequencer output streams
fastq_database = {
    "READ_001": ("ATGCGTACG", "IIIIIIIII"),     # High quality clean read (I = score 40)
    "READ_002": ("CCGATAGCA", "!!!!!!!!!"),     # Horrible error filled read (! = score 0)
    "READ_003": ("GGATCGTTA", "ABCDEFGHI")      # Medium clean read
}

# Run quality assessment pipeline with a strict filtering limit of Q20 (99% accuracy)
filtered_results = filter_fastq_reads(fastq_database, 20)
print(f"\n📊 PRE-PROCESSING COMPLETE: Maintained {len(filtered_results)} reliable genomic reads.")
