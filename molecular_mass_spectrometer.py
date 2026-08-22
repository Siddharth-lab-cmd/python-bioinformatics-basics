def calculate_peptide_mass_spectrum(amino_acid_sequence):
    """Computes exact monoisotopic fragmentation masses for protein sequences."""
    # Standard residue masses in Daltons (Da) used by laboratory instruments
    mass_table = {
        'A': 71.0371, 'R': 156.1011, 'N': 114.0429, 'D': 115.0269, 'C': 103.0091,
        'E': 129.0426, 'Q': 128.0586, 'G': 57.0214,  'H': 137.0589, 'I': 113.0841,
        'L': 113.0841, 'K': 128.0950, 'M': 131.0405, 'F': 147.0684, 'P': 97.0528,
        'S': 87.0320,  'T': 101.0477, 'W': 186.0793, 'Y': 163.0633, 'V': 99.0684
    }
    
    print("⚖️ LOADING MONOISOTOPIC MASS SPECTROMETRY SCANNERS...")
    print(f"Target Peptide: {amino_acid_sequence.upper()}")
    print("-" * 60)
    
    current_mass = 18.0105 # Starting water loss adjustment mass baseline
    fragment_logs = []
    
    for idx, residue in enumerate(amino_acid_sequence.upper()):
        if residue in mass_table:
            current_mass += mass_table[residue]
            fragment_logs.append((idx + 1, residue, current_mass))
            
    print(f"{'Fragment Tag':<15} | {'Added Residue':<15} | {'Cumulative Mass (Da)':<20}")
    print("-" * 60)
    for tag, res, mass in fragment_logs:
        print(f"b-Ion (Position {tag}) | {res:<13} | {mass:<19.4f} Da")
        
    print("-" * 60)
    print(f"🚀 Mass Spectrum Final Checkpoint: Unified Value = {current_mass:.4f} Da")

calculate_peptide_mass_spectrum("MKWVP")
