import sys
import os
import pytest
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import (
    calculate_life_path_number,
    calculate_expression_number,
    calculate_soul_urge_number,
    calculate_personality_number,
    calculate_destiny_number,
    generate_fingerprint,
    calculate_pinnacles,
    calculate_personal_cycles
)

def test_calculate_life_path_number():
    assert calculate_life_path_number("1990-05-25") == 4
    assert calculate_life_path_number("2000-11-11") == 6

def test_calculate_expression_number():
    assert calculate_expression_number("John Doe") == 8
    assert calculate_expression_number("Jane Smith") == 9

def test_calculate_soul_urge_number():
    assert calculate_soul_urge_number("John Doe") == 8
    assert calculate_soul_urge_number("Jane Smith") == 6

def test_calculate_personality_number():
    assert calculate_personality_number("John Doe") == 9
    assert calculate_personality_number("Jane Smith") == 3

def test_calculate_destiny_number():
    assert calculate_destiny_number("John Doe") == calculate_expression_number("John Doe")

def test_generate_fingerprint():
    fp1 = generate_fingerprint("John Doe", "1990-05-25", 5, 8)
    fp2 = generate_fingerprint("John Doe", "1990-05-25", 5, 8)
    fp3 = generate_fingerprint("Jane Doe", "1990-05-25", 5, 8)
    assert fp1 == fp2
    assert fp1 != fp3

def test_calculate_pinnacles():
    p1 = calculate_pinnacles("1990-05-25")
    assert isinstance(p1, tuple)
    assert len(p1) == 4
    for val in p1:
        assert isinstance(val, int)

def test_calculate_personal_cycles():
    pc = calculate_personal_cycles("1990-05-25")
    assert isinstance(pc, tuple)
    assert len(pc) == 3
    for val in pc:
        assert isinstance(val, int)
        assert 1 <= val <= 33

