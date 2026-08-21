def filter_differential_expression(expression_dataset, threshold_fold_change):
    """Filters a genomic dataset to locate highly up-regulated gene markers."""
    significant_genes = {}
    
    print("🧬 SCANNING TRANSCRIPTOMIC CELLULAR DATA MATRICES...")
    print(f"{'Gene Identifier':<15} | {'Log2 Fold Change':<18} | {'Expression Status':<15}")
    print("-" * 55)
    
    for gene_id, fold_change in expression_dataset.items():
        if fold_change >= threshold_fold_change:
            status = "📈 UP-REGULATED"
            significant_genes[gene_id] = fold_change
        elif fold_change <= -threshold_fold_change:
            status = "📉 DOWN-REGULATED"
        else:
            status = "🛑 NO CHANGE"
            
        print(f"{gene_id:<15} | {fold_change:<18.2f} | {status:<15}")
        
    return significant_genes

# Mock gene tracking data for Salmonella bacteria exposed to food preservatives
preservative_stress_test = {
    "GENE_ST_001": 2.45,
    "GENE_ST_002": -1.89,
    "GENE_ST_003": 0.12,
    "GENE_ST_004": 3.10,
    "GENE_ST_005": -0.05
}

# Run pipeline to find genes with high expression changes (Threshold >= 2.00)
high_activity_genes = filter_differential_expression(preservative_stress_test, 2.0)
print(f"\n📊 ANALYSIS COMPLETE: Isolated {len(high_activity_genes)} target gene switches for further testing.")
