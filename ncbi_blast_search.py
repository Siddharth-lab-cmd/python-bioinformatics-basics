cat << 'EOF' > ncbi_blast_search.py
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys

def execute_remote_blast(sequence_data):
    print("🚀 Initializing High-Velocity Remote BLAST Query on NCBI Cloud...")
    # Performs a blastn search against the standard nucleotide database (nt)
    try:
        result_handle = NCBIWWW.qblast("blastn", "nt", sequence_data)
        print("✅ Data stream retrieved. Parsing XML alignment matrix...")
        
        blast_records = NCBIXML.parse(result_handle)
        for record in blast_records:
            for alignment in record.alignments[:3]:  # Isolate top 3 target matches
                print(f"\n🎯 Target Match Alignment: {alignment.title}")
                print(f"🧬 Sequence Length: {alignment.length} Base Pairs")
                for hsp in alignment.hsps:
                    print(f"📈 Expectation Value (E-value): {hsp.expect}")
                    print(f"📊 Query Alignment Sequence: {hsp.query[:50]}...")
                    print(f"🔬 Subject Alignment Sequence: {hsp.sbjct[:50]}...")
    except Exception as e:
        print(f"❌ Structural Connection Failure: {str(e)}")

if __name__ == "__main__":
    # Test dataset sequence (Sample DNA Strand segment)
    sample_dna = "TGGATTACCAAGTCAATTGGAGAGGCTATTGTTGCTAGC"
    execute_remote_blast(sample_dna)
EOF

