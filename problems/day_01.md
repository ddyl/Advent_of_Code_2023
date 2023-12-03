# Day 1

[Link to Day 1 problem](https://adventofcode.com/2023/day/1)

The only part that I got stuck on was in part 2, where I ddin't realize the fact that numbers can overlap. For example `sevenine` is `7 9`, and `nineight` is `9 8`. This is as per the related [reddit thread](https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/).

This changed my regex match string that I had formerly:
- `(\d|one|two|three|four|five|six|seven|eight|nine|ten)`

To the regex string that I used in the solution:
- `(?=(\d|one|two|three|four|five|six|seven|eight|nine|ten))`

