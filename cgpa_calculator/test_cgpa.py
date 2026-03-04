"""Unit tests for the CGPA calculator."""

import pytest

from cgpa_calculator.cgpa import calculate_cgpa


def test_empty_courses():
    assert calculate_cgpa([]) == 0.0


def test_single_course():
    assert calculate_cgpa([("A", 3)]) == 9.0
    assert calculate_cgpa([("F", 4)]) == 0.0


def test_multiple_courses():
    courses = [("A", 3), ("B+", 4), ("C", 2)]
    # expected cgpa: ((9*3)+(8*4)+(6*2)) / (3+4+2) = (27+32+12)/9 = 71/9 = 7.888... -> 7.89
    assert calculate_cgpa(courses) == 7.89


def test_invalid_grade():
    with pytest.raises(ValueError):
        calculate_cgpa([("X", 3)])


def test_invalid_credits():
    with pytest.raises(ValueError):
        calculate_cgpa([("A", 0)])

    with pytest.raises(ValueError):
        calculate_cgpa([("A", -1)])


def test_gui_parse_lines():
    from cgpa_calculator.gui import CgpaGui

    gui = CgpaGui.__new__(CgpaGui)  # bypass __init__
    # valid input
    lines = ["A 3", "B+ 4", ""]
    assert gui.parse_lines(lines) == [("A", 3.0), ("B+", 4.0)]

    # missing credit
    with pytest.raises(ValueError):
        gui.parse_lines(["A"])

    # non-numeric credit
    with pytest.raises(ValueError):
        gui.parse_lines(["A three"])
