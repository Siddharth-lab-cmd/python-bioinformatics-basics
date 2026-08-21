def calculate_mutation_distance(sequence_alpha, sequence_beta):
    """Calculates the Hamming Distance between two matching genomic strands."""
    if len(sequence_alpha) != len(sequence_beta):
        raise ValueError("Error: Sequences must be of identical length to map point mutations.")
        
    mutation_count = 0
    mutation_coordinates = []
    
    for position in range(len(sequence_alpha)):
        if sequence_alpha[position] != sequence_beta[position]:
            mutation_count += 1
            mutation_coordinates.append(position)
            
    return mutation_count, mutation_coordinates

# Comparing original wild rice strain vs a climate-resistant variant strain
wild_strain   = "ATGCEGATGCTAGCTAGCTA"
mutant_strain = "ATGCGATGCTAGCTTCGCTA"

print("🔍 ALIGNING SEQUENCES FOR POINT MUTATION SCANNING...")
try:
    total_mutations, positions = calculate_mutation_distance(wild_strain, mutant_strain)
    print(f"Wild Gene Strain   : {wild_strain}")
    print(f"Mutant Gene Strain : {mutant_strain}")
    print(f"📊 Mutation Count  : Found {total_mutations} genetic variations.")
    print(f"📍 Mapped Indexes  : Base mismatches localized at index positions: {positions}")
except ValueError as error_message:
    print(error_message)
