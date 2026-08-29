cat << 'EOF' > rna_translation_engine.py
from Bio.Seq import Seq

def translate_rna_stream(rna_string):
    print("🔬 Initializing Transcription-Translation Cloud Engine Loop...")
    rna_sequence = Seq(rna_string.upper())
    
    # Transcribe RNA back to DNA pattern or translate straight to Amino Acid chains
    protein_sequence = rna_sequence.translate(to_stop=True)
    
    print("\n🔍 Structural Sequence Extraction Complete:")
    print(f"🧬 Input mRNA Sequence: {rna_string}")
    print(f"👑 Output Amino Acid Chain (Protein): {protein_sequence}")
    print(f"🧪 Total Peptide Chain Length: {len(protein_sequence)} Residues")

if __name__ == "__main__":
    sample_mrna = "AUGGCCAUGGGGGCAUCUAAUAGU"
    translate_rna_stream(sample_mrna)
EOF
