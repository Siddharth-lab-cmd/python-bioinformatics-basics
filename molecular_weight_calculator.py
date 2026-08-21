def calculate_protein_molecular_weight(protein_sequence):
    """Calculates the total molecular mass (Daltons) of an amino acid chain."""
    # Standard residue monoisotopic mass weights
    amino_acid_weights = {
        'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
        'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
        'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
        'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06
    }
    
    protein_sequence = protein_sequence.upper().strip()
    total_mass = 0.0
    water_molecule_mass = 18.02 # Added to correct the terminal end mass structure
    
    for residue in protein_sequence:
        if residue in amino_acid_weights:
            total_mass += amino_acid_weights[residue]
        else:
            print(f"⚠️ Warning: Unknown amino acid character '{residue}' skipped.")
            
    return total_mass + water_molecule_mass if total_mass > 0 else 0.0

# Analyzing a peptide segment from a dairy milk protein (Casein)
milk_peptide = "MKVLILE"
weight = calculate_protein_molecular_weight(milk_peptide)

print("🧪 PARSING PROTEOMIC MASS SPECTROMETRY SCANS...")
print(f"Target Peptide Chain : {milk_peptide}")
print(f"⚖️ Total Computed Mass : {weight:.2f} Daltons (Da)")
