from pathlib import Path
import os

from advent_of_code_2023.day_02 import possible_games

def test_solution():
    
    test_input_path = os.path.join(Path(__file__).parent, "test_inputs", "day_02_test_1.txt")

    with open(test_input_path) as input_file:
        assert possible_games(input_file.read().splitlines()) == (8, 2286)

