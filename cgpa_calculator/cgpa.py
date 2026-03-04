"""Simple CGPA (Cumulative Grade Point Average) calculator.

This module provides functions for calculating CGPA given course grades and
their corresponding credit hours. It also offers a command-line interface
for interactive usage.
"""

from typing import Iterable, Tuple


GRADE_POINT_MAP = {
    "A+": 10.0,
    "A": 9.0,
    "B+": 8.0,
    "B": 7.0,
    "C": 6.0,
    "D": 5.0,
    "F": 0.0,
}


def calculate_cgpa(courses: Iterable[Tuple[str, float]]) -> float:
    """Compute CGPA.

    Args:
        courses: An iterable of tuples where each tuple contains the grade string
            (e.g., "A", "B+") and the credit hours for the course.

    Returns:
        The cumulative grade point average as a float rounded to two decimals.

    Raises:
        ValueError: If credit hours are non-positive or grade is unrecognized.
    """
    total_points = 0.0
    total_credits = 0.0

    for grade, credits in courses:
        if credits <= 0:
            raise ValueError("Credit hours must be positive")
        try:
            point = GRADE_POINT_MAP[grade.upper()]
        except KeyError:
            raise ValueError(f"Unknown grade: {grade}")

        total_points += point * credits
        total_credits += credits

    if total_credits == 0:
        return 0.0

    cgpa = total_points / total_credits
    return round(cgpa, 2)


if __name__ == "__main__":
    import sys

    def parse_input(line: str):
        parts = line.strip().split()
        if len(parts) != 2:
            raise ValueError("Each entry must contain grade and credit separated by space")
        grade = parts[0]
        try:
            credits = float(parts[1])
        except ValueError:
            raise ValueError("Credit hours must be a number")
        return grade, credits

    print("Enter courses one per line in format: <grade> <credits>")
    print("Blank line to finish")
    entries = []
    for line in sys.stdin:
        if not line.strip():
            break
        try:
            entries.append(parse_input(line))
        except ValueError as e:
            print(f"Invalid input: {e}")
    try:
        result = calculate_cgpa(entries)
        print(f"Your CGPA is {result}")
    except ValueError as exc:
        print(f"Error: {exc}")
