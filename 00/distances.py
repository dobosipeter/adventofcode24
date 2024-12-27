"""Solve the first aoc24 challenge."""
from pathlib import Path
import pandas as pd

def parse_input(input_path: Path) -> pd.DataFrame:
    """
    Parse the raw input.

    :param input_path: A Path object pointing to the input file.

    :return: The parsed input.
    """
    parsed_data = pd.read_csv(input_path, sep='   ', header=None, engine='python')
    parsed_data.columns = ['left', 'right']

    return parsed_data

def sort_input(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Sort the parsed values.

    :param input_data: The input data to parse.

    :return: The parsed input data.
    """
    sorted_data = pd.DataFrame({
        'left': sorted(input_data['left']),
        'right': sorted(input_data['right'])
    })

    return sorted_data

def calculate_deltas(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the absolute distance between the two columns.

    :param input_data: The input data to use.

    :return: The input augumented with the results.
    """
    input_data['delta'] = (input_data['left'] - input_data['right']).abs()
    return input_data

def calculate_occurences(input_data: pd.DataFrame) -> dict:
    """
    Calcualte the amount of times each item in the left column appears in the right column.

    :param input_data: The input data to use.

    :return: A dictionary keyed by the items in the left column and their value counts in the right column as values.
    """
    value_counts = input_data.right.value_counts().to_dict()
    for _, value in input_data.left.items():
        if value not in value_counts:
            value_counts[value] = 0
    return value_counts

def calculate_similarity_score(input_data: pd.DataFrame, occurence_counts: dict) -> pd.DataFrame:
    """
    Calculate the similarity score of the items in the left column, weighted by their occurence counts.

    :param input_data: The input data to use.
    :param occurence_counts: The dictionary of occurence counts.

    :return: The DataFrame augumented with the results.
    """
    input_data['similarity'] = input_data['left'] * input_data.left.map(occurence_counts)
    return input_data


if __name__ == '__main__':
    parsed_input = parse_input(Path('input.txt'))
    sorted_input = sort_input(parsed_input)
    calculated_deltas = calculate_deltas(sorted_input)
    print(f'Sum of deltas: {calculated_deltas.delta.sum()}')
    occurences = calculate_occurences(sorted_input)
    similarity_scores = calculate_similarity_score(sorted_input, occurences)
    print(f'Sum of similarity scores: {similarity_scores.similarity.sum()}')
