from pathlib import Path
import os
import re

def possible_games(input):
    regex_single_game = r"(?=(?::|;) (.*?)(?::|;|$))"
    regex_color_count = r"(\d*)(?: )(\w*?)(?:,|$)"

    # idx_sum will hold the answer to part 1, which is the sum of indexes for possible games given p1_color_counts
    idx_sum = 0
    p1_color_counts = {"red":12, "green":13, "blue": 14}
    
    # required_colors_sum will hold the answer to part 2, the sum of each game's power
    required_colors_sum = 0


    for idx, line in enumerate(input):

        max_counts = {"red":0, "green":0, "blue":0}

        # Get all handfuls from a single game
        games = re.findall(regex_single_game, line)

        for game in games:        
            # Get the count of each color from each handful
            colors = re.findall(regex_color_count, game)
            # For each color, store the maximum value of each
            for num, color in colors:
                max_counts[color] = max(max_counts[color], int(num))
        
        # Answer for part 1 
        #   If the current game is possible given p1_color_counts, add the game number (1-based index) to idx_sum
        possible_game = True
        for color in p1_color_counts.keys():
            if p1_color_counts[color] < max_counts[color]:
                possible_game = False
        if possible_game:
            idx_sum += idx + 1

        # Answer for Part 2:
        #   Each game's power is defined as the product of all its maximum counts. The sum of all powers is the answer to part 2        
        power = 1
        for count in max_counts.values():
            power *= count
        required_colors_sum += power
    
    return idx_sum, required_colors_sum


def main():
    input_path = os.path.join(Path(__file__).parent, "inputs", "day_02.txt")
    
    with open(input_path) as input_file:
        input = input_file.read().splitlines()
        p1_answer, p2_answer = possible_games(input=input)
        print ("Part 1 Answer:", p1_answer)
        print ("Part 2 Answer:", p2_answer)
