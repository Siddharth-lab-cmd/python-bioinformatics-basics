def calculate_enzyme_velocity(substrate_concentration, max_velocity, michaelis_constant):
    """Computes enzyme reaction velocities using the Michaelis-Menten mathematical model."""
    print("🧪 EVALUATING BIOCHEMICAL ENZYME KINETICS CHANNELS...")
    print(f"{'Substrate Conc (mM)':<22} | {'Computed Velocity (mM/s)':<25}")
    print("-" * 52)
    
    for concentration in substrate_concentration:
        # Michaelis-Menten Formula: V = (Vmax * [S]) / (Km + [S])
        velocity = (max_velocity * concentration) / (michaelis_constant + concentration)
        print(f"{concentration:<22.2f} | {velocity:<25.4f}")

# Substrate saturation limits (e.g., testing milk lactose concentration limits)
lactose_levels = [0.1, 0.5, 1.0, 5.0, 10.0]
calculate_enzyme_velocity(lactose_levels, max_velocity=12.5, michaelis_constant=1.2)
