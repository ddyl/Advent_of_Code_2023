from pathlib import Path
import os
import re

def trebuchet(input, digit_only = True):
    # Originally I didn't bother with regex for part 1, but regex is much simpler for part 2
    
    regex_string = None
    if digit_only:
        regex_string = r"(\d)"
    else:
        regex_string = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|ten))"

    string_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    all_sum = 0
    for line in input:
        matches = re.findall(regex_string, line, re.MULTILINE)
        if matches[0].isdigit():
            all_sum += int(matches[0]) * 10
        else:
            all_sum += string_to_int[matches[0]] * 10
        
        if matches[-1].isdigit():
            all_sum += int(matches[-1])
        else:
            all_sum += string_to_int[matches[-1]]
    
    return all_sum



def main():
    input_path = os.path.join(Path(__file__).parent, "inputs", "day_01.txt")
    
    with open(input_path) as input_file:
        input = input_file.read().splitlines()
        print ("Part 1 Answer:", trebuchet(input=input, digit_only=True))
        print ("Part 2 Answer:", trebuchet(input=input, digit_only=False))
