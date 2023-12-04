# Day 2

[Link to Day 2 problem](https://adventofcode.com/2023/day/2)

Similar to Day 1, the regex was the hardest part. I used two regex strings, one to separate out each handful with in a game, and one to extract each color count from each handful.

## Regex for extracting handfuls

Given a line from the example input:
- `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`

I used the following to extract each handful:
```python
regex_single_game = r"(?=(?::|;) (.*?)(?:;|$))"

# String object "line" represents a line from the input
# For example, use the following line:
#   Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
games = re.findall(regex_single_game, line)
```

After which `games` will hold:
- `['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']`

The regex can be explained as:
- Complete regex: `(?=(?::|;) (.*?)(?::|;|$))`
    - `(?=` is required for overlapping patches.
    - `(?:` Indicates that everything in the group is non-capturing. These will be included in the search, but not returned as a group.
    - `:|;) ` Searches for either the `: ` or `; ` which denote the beginning of a handful. Note that the closing bracket completes the non-capturing group above, and the following space is included in the group.
    - `(.*?)` Searches includes any character except for line breaks (`.`) lazily (`*?`).
    - `(?:` Once again, this specifies a non-capturing group.
    - `;|$)` Searches for either the semicolon (`;`) or end of line (`$`) which denote the end of the handful.
    - `)` The final bracket completes the regex search.

## Regex for extracting color counts

Now that the first regex returned an array of each handful, it is possible to separate the count of each color for each handful.

```python
regex_color_count = r"(\d*)(?: )(\w*?)(?:,|$)"

# String object "game" represents an element from the previous regex's output.
# For example, consider game to be the first string from the previous output:
#   '3 blue, 4 red'
colors = re.findall(regex_color_count, game)
```

After wich `colors` will hold:
- `[('3', 'blue'), ('4', 'red')]`

The regex can be explained as:
- Complete regex: `(\d*) (\w*?)(?:,|$)`
    - `(\d*) ` Get all digits, as there may be 10 or more counts of each color. Note that the space between the count and color is included in this portion as well.
    - `(\w*?)` Lazily match all word characters.
    - `(?:` Indicates a non-capturing group.
    - `,|$)` Search for either a comma (which indicate the end of each color count) or the end of line (`$`).