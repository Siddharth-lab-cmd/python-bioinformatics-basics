import streamlit as str

str.set_page_config(page_title="Bioinformatics Aligner", page_icon="🧬")

str.title("🧬 Advanced DNA Sequence Checker")
str.write("Built by Siddharth-lab-cmd")

seq1 = str.text_input("Enter DNA Sequence 1:", "ATCGATCG").upper()
seq2 = str.text_input("Enter DNA Sequence 2:", "ATGGATCG").upper()

if str.button("Analyze Match"):
    if len(seq1) != len(seq2):
        str.error("For a simple match check, both sequences must be the same length!")
    else:
        matches = 0
        visual_line = ""
        for i in range(len(seq1)):
            if seq1[i] == seq2[i]:
                matches += 1
                visual_line += "|"
            else:
                visual_line += "."
                
        identity = (matches / len(seq1)) * 100
        
        str.success(f"Analysis Complete! Identity Score: {identity:.2f}%")
        str.text(f"Seq 1: {seq1}")
        str.text(f"Match: {visual_line}")
        str.text(f"Seq 2: {seq2}")
