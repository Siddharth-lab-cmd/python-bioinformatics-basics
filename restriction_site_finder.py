def locate_restriction_enzyme_cuts(dna_strand, enzyme_restriction_site):
    """Maps the precise coordinate cut locations for genetic engineering tools."""
    dna_strand = dna_strand.upper().strip()
    enzyme_restriction_site = enzyme_restriction_site.upper().strip()
    
    cut_positions = []
    index = dna_strand.find(enzyme_restriction_site)
    
    while index != -1:
        cut_positions.append(index)
        # Advance forward to check the rest of the genetic sequence
        index = dna_strand.find(enzyme_restriction_site, index + 1)
        
    return cut_positions

# EcoRI is a famous restriction enzyme that always cuts at the sequence "GAATTC"
ecori_site = "GAATTC"
sample_crop_dna = "ATCGATCGAAATTCGCTAGCTAGAGAATTCGCTAGCTAGCGAATTCATCG"

positions = locate_restriction_enzyme_cuts(sample_crop_dna, ecori_site)

print("✂️ SCANNING GENOMIC MOLECULE FOR MOLECULAR SCISSORS LOOKUP...")
print(f"Target Cut Sequence (EcoRI): {ecori_site}")
print(f"📍 Mapping complete. DNA cuts located at sequence indices: {positions}")
