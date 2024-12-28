"""Solve the second day of aoc24."""
from pathlib import Path
import pandas as pd

"""
Challenge description

The input consists of multiple lines, called reports
Each report consists of numbers called levels, each level is separated by a space

Rules:
All levels on a report (line) must increase or decrease, but not both, stagnation is not allowed
the absolute delta between two levels has to be between 1 and 3

Ideas:
Seems like a kernel/convolution problem?
Maybe think about early failure detection methods for each entry?
Calculate the possible range for each starting number check whether the last number is within

Plan:
1. Read each line and split it into a list of numbers
2. Shove it into a df if possible?
3. Check whether the rules hold
4. Calculate the number of rows where it holds.
"""


def parse_input(input_path: Path) -> pd.DataFrame:
    """
    Parse the challenge input.

    :param input_path: The path of the input file.

    :return: The parsed data as a DataFrame.
    """
    # The max amount of measurements in a single report seems to be 8
    # Pandas doesn't like it when the column counts are different, so specify it
    parsed_data = pd.read_csv(input_path, sep=' ', header=None)
    return parsed_data

if __name__ == '__main__':
    parsed_input = parse_input(Path('input.txt'))
    print(parsed_input)
