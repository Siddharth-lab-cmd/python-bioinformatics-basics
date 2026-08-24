import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Bioinformatics Aligner", page_icon="🧬")

st.title("🧬 Advanced DNA Analyzer & Visualizer")
st.write("Built with tactical precision by Siddharth-lab-cmd")

# Input field for DNA
seq = st.text_input("Enter DNA Sequence to Analyze:", "ATCGATCGATGGATCGATCG").upper()

# Core calculation logic
if st.button("Run Analytics"):
    # 1. Calculate length and counts
    total_length = len(seq)
    a_count = seq.count("A")
    t_count = seq.count("T")
    c_count = seq.count("C")
    g_count = seq.count("G")
    
    # 2. Check for empty or invalid inputs
    if total_length == 0:
        st.error("Please enter a valid DNA sequence!")
    else:
        gc_total = g_count + c_count
        gc_percentage = (gc_total / total_length) * 100
        
        # Display text matrix scores
        st.success("Analysis Complete!")
        st.write(f"**Total Base Pairs:** {total_length}")
        st.write(f"**GC Content Percentage:** {gc_percentage:.2f}%")
        
        # 3. Create the Plotly Data Frame Table
        data = {
            'Nucleotide': ['Adenine (A)', 'Thymine (T)', 'Cytosine (C)', 'Guanine (G)'],
            'Count': [a_count, t_count, c_count, g_count]
        }
        df = pd.DataFrame(data)
        
        # 4. Generate Interactive Plotly Bar Chart
        fig = px.bar(
            df, 
            x='Nucleotide', 
            y='Count', 
            title="DNA Base Distribution Frequency",
            color='Nucleotide',
            labels={'Count': 'Number of Bases'}
        )
        
        # Render the interactive chart on our Streamlit site
        st.plotly_chart(fig)
