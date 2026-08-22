def estimate_protein_charge_at_ph(peptide_sequence, environment_ph):
    """Calculates the net electrical charge profile of an amino acid string at specific pH thresholds."""
    peptide_sequence = peptide_sequence.upper().strip()
    
    # Standard biological charges at neutral thresholds
    positive_residues = {'K': 1.0, 'R': 1.0, 'H': 0.1}
    negative_residues = {'D': -1.0, 'E': -1.0, 'C': -0.1, 'Y': -0.1}
    
    total_charge = 0.0
    
    for residue in peptide_sequence:
        if residue in positive_residues:
            total_charge += positive_residues[residue]
        elif residue in negative_residues:
            total_charge += negative_residues[residue]
            
    print("⚖️ STRUCTURAL BIOCHEMISTRY ISOELECTRIC CHARGE CALCULATION...")
    print(f"Target Sequence : {peptide_sequence}")
    print(f"Environment pH  : {environment_ph}")
    print(f"📊 Net Estimated Charge: {total_charge:+.2f}")
    return total_charge

estimate_protein_charge_at_ph("MKRDEHC", environment_ph=7.0)
