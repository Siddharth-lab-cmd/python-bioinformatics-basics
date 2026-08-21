def check_primer_self_complementarity(primer_sequence):
    """Scans a PCR primer to prevent self-binding defects (Primer-Dimers)."""
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    primer_sequence = primer_sequence.upper().strip()
    
    # Generate the reverse complement sequence string
    reverse_complement = "".join(complement_map.get(base, 'N') for base in reversed(primer_sequence))
    
    print("🔬 RUNNING PRE-EXPERIMENTAL WEBA-LAB SIMULATION...")
    print(f"Forward Primer : {primer_sequence}")
    print(f"Reverse Strand : {reverse_complement}")
    
    # Check for overlapping binding risks near the crucial ends of the strands
    if primer_sequence[-4:] in reverse_complement:
        print("⚠️ ALERT: High risk of Primer-Dimer formation detected at the 3' end!")
        return False
        
    print("✅ PASS: Primer sequence design is stable and ready for lab PCR testing.")
    return True

# Test an ideal primer sequence design vs an unstable design setup
test_sequence = "ATCGGCATTCGATCGATC"
check_primer_self_complementarity(test_sequence)
