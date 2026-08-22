import json
from datetime import datetime

class GenomicPipeline:
    def __init__(self, sample_name: str):
        self.sample_name = sample_name
        self.processed_records = []

    def calculate_gc_content(self, DNA_sequence: str) -> float:
        """Calculates the percentage of Guanine (G) and Cytosine (C) in a sequence."""
        if not DNA_sequence:
            return 0.0
        
        # Count the bases accurately
        gc_count = sum(1 for base in DNA_sequence if base in 'GCgc')
        total_bases = len(DNA_sequence)
        
        return round((gc_count / total_bases) * 100, 2)

    def parse_sequence_record(self, sequence_id: str, DNA_sequence: str):
        """Processes a single raw genomic text entry into clean data."""
        gc_percentage = self.calculate_gc_content(DNA_sequence)
        
        # Categorize the safety flag based on GC density metrics
        status = "STABLE" if 40.0 <= gc_percentage <= 60.0 else "VARIANT_SPIKE"
        
        record = {
            "record_id": sequence_id,
            "processed_at": datetime.utcnow().isoformat(),
            "gc_content_percent": gc_percentage,
            "sequence_length": len(DNA_sequence),
            "status_flag": status
        }
        
        self.processed_records.append(record)
        return record

    def export_to_json(self) -> str:
        """Converts the processed biological data into a clean JSON string."""
        output_data = {
            "sample_batch": self.sample_name,
            "total_parsed": len(self.processed_records),
            "results": self.processed_records
        }
        return json.dumps(output_data, indent=4)

# Quick local test simulation
if __name__ == "__main__":
    pipeline =超 = GenomicPipeline(sample_name="Cancer_Research_Batch_A")
    pipeline.parse_sequence_record("READ_001", "ATGCTAGCTAGCTAGCG")
    pipeline.parse_sequence_record("READ_002", "GGGGCCCCGGGGCCCCA")
    print(pipeline.export_to_json())
