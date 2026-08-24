import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Simulate a heavy Multi-Omics Expression Matrix (3 Genes across 100 Patients)
np.random.seed(42)
data = {
    'BRCA1_Expression': np.random.normal(loc=5.5, scale=1.2, size=100),
    'TP53_Expression': np.random.normal(loc=2.1, scale=0.8, size=100),
    'Tissue_Type': np.random.choice(['Tumor', 'Normal'], size=100)
}
df = pd.DataFrame(data)

# 2. Advanced Matrix Filtration: Isolate high tumor expressions (Z-Score > 1.5)
tumor_data = df[df['Tissue_Type'] == 'Tumor']
high_expression_cutoff = tumor_data['BRCA1_Expression'].mean() + (1.5 * tumor_data['BRCA1_Expression'].std())
overexpressed_patients = tumor_data[tumor_data['BRCA1_Expression'] > high_expression_cutoff]

print("📊 --- Multi-Omics Expression Filter --- 📊")
print(f"Overexpressed Tumor Cutoff Threshold: {high_expression_cutoff:.2f}")
print(f"Identified {len(overexpressed_patients)} Patient Samples showing Critical Overexpression.\n")

# 3. Structural Output Layout for Your Portfolio Box
print(overexpressed_patients.head())
