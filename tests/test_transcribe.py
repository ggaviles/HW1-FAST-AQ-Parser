# write tests for transcribes
import pytest
import numpy as np
from seqparser import transcribe, reverse_transcribe
from data.make_seq import make_seq

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}

SEQ = "ACTGAACCC"

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True

def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    assert transcribe(SEQ) == "UGACUUGGG"

def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    assert reverse_transcribe(SEQ) == "GGGUUCAGU"

def test_transcribe_random_seq():
    seq = make_seq(7).upper()
    output = "".join(map(TRANSCRIPTION_MAPPING.get, seq))
    transcribed_seq = transcribe(seq)
    assert output == transcribed_seq

def test_reverse_transcribe_random_seq():
    seq = make_seq(10).upper()
    output = "".join(map(TRANSCRIPTION_MAPPING.get, seq))
    output = output[::-1]
    rev_trans_seq = reverse_transcribe(seq)
    assert output == rev_trans_seq


