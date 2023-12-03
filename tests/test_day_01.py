from pathlib import Path
import os

from advent_of_code_2023.day_01 import trebuchet

def test_solution_1():
    
    test_input_path = os.path.join(Path(__file__).parent, "test_inputs", "day_01_test_1.txt")

    with open(test_input_path) as input_file:
        assert trebuchet(input_file.read().splitlines(), digit_only=True) == 142

def test_solution_2():
    
    test_input_path = os.path.join(Path(__file__).parent, "test_inputs", "day_01_test_2.txt")

    with open(test_input_path) as input_file:
        assert trebuchet(input_file.read().splitlines(), digit_only=False) == 281