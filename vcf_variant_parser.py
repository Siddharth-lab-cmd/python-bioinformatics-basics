def parse_vcf_variant_lines(raw_vcf_data):
    """Parses standard population variation metrics from raw VCF lines."""
    print("🔬 INITIALIZING HIGH-THROUGHPUT VARIANT CALL (VCF) PARSER...")
    print(f"{'Chrom ID':<10} | {'Position (bp)':<15} | {'Ref Base':<10} | {'Alt Base':<10} | {'Filter Status':<12}")
    print("-" * 65)
    
    for line in raw_vcf_data.strip().split("\n"):
        if line.startswith("#") or not line.strip():
            continue # Skip header comment lines
            
        columns = line.split("\n")[0].split("\t")
        chrom, pos, ref, alt, quality, filter_status = columns[0], columns[1], columns[3], columns[4], columns[5], columns[6]
        
        print(f"{chrom:<10} | {pos:<15} | {ref:<10} | {alt:<10} | {filter_status:<12}")

# Mock simulation of an incoming genomic variation line sheet from a sequencer machine
mock_vcf_stream = """##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO
chr01	145230	.	A	G	99	PASS	DP=45
chr01	147890	.	C	T	20	LOW_QUAL	DP=12
chr02	892110	.	G	C	100	PASS	DP=80"""

parse_vcf_variant_lines(mock_vcf_stream)
