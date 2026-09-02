

def extract_genbank_metadata(raw_genbank_record):
    """Parses standard administrative text metadata blocks from raw GenBank flatfiles."""
    metadata_report = {"LOCUS": "Unknown", "DEFINITION": "Unknown", "ORGANISM": "Unknown"}
    
    for line in raw_genbank_record.strip().split('\n'):
        line = line.strip()
        if line.startswith("LOCUS"):
            metadata_report["LOCUS"] = " ".join(line.split()[1:])
        elif line.startswith("DEFINITION"):
            metadata_report["DEFINITION"] = " ".join(line.split()[1:])
        elif line.startswith("ORGANISM"):
            metadata_report["ORGANISM"] = " ".join(line.split()[1:])
            
    return metadata_report

# Mock simulation of an incoming GenBank flatfile data stream from NCBI database systems
mock_genbank_file = """LOCUS       SCU49845     5028 bp    DNA     linear   PLN 21-JUN-2025
DEFINITION  Saccharomyces cerevisiae TCP1-beta gene, partial cds.
ACCESSION   U49845
SOURCE      Saccharomyces cerevisiae (baker's yeast)
  ORGANISM  Saccharomyces cerevisiae
            Eukaryota; Fungi; Ascomycota; Saccharomycetales; Saccharomycetaceae;"""

print("💾 INGESTING REMOTE DATA STREAMS FROM CENTRAL NATIONAL DATABASES...")
parsed_meta = extract_genbank_metadata(mock_genbank_file)

print("\n🎯 EXTRACTED METADATA PIPELINE SUMMARY REPORT:")
print("-" * 50)
for key, value in parsed_meta.items():
    print(f"{key:<12} : {value}")
