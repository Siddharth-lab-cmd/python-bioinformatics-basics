def parse_fasta_data(raw_fasta_string):
    """Parses a multi-line FASTA string into a structured Python dictionary."""
    fasta_records = {}
    current_header = None
    current_sequence = []
    
    for line in raw_fasta_string.strip().split('\n'):
        line = line.strip()
        if line.startswith('>'):
            if current_header:
                fasta_records[current_header] = "".join(current_sequence)
            current_header = line[1:]  # Strip out the '>' token
            current_sequence = []
        else:
            current_sequence.append(line.upper())
            
    # Save the absolute final record entry block
    if current_header:
        fasta_records[current_header] = "".join(current_sequence)
        
    return fasta_records

# Simulating an official input file containing salmonella bacterial gene records
mock_file_data = """>NC_003197.2 Salmonella enterica strain LT2 chromosome segment 1
ATGTTACATAAATCAGAATACGAAATCAGAACACTTTTC
AGCAATTTTTATTCTGAACAAACCAGTATTATCTGTGTG
>NC_011083.1 Probiotic Lactobacillus acidophilus gene marker
ATGCGTAAAGCACTTTTAATTACAGATAAACTTGATATG
GCAAAACTTGCTGCCGAACAAGCTGTTAAAGTGGTTGCA"""

print("⚙️ INGESTING RAW INDUSTRIAL FASTA RECORD DATABASE...")
parsed_output = parse_fasta_data(mock_file_data)

for access_id, sequence_string in parsed_output.items():
    print(f"\nHeader ID   : {access_id}")
    print(f"Sequence Length : {len(sequence_string)} Base Pairs")
    print(f"First 15 Bases  : {sequence_string[:15]}...")
