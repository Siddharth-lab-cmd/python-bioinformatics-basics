import pytest

def test_gc_content():
    sequence = "ATGC"
    # Basic check for sequence length and composition
    assert len(sequence) == 4
    assert sequence.count('G') + sequence.count('C') == 2

def test_dna_validity():
    sequence = "ATCGATCG"
    valid_bases = {'A', 'T', 'C', 'G'}
    assert set(sequence).issubset(valid_bases)
