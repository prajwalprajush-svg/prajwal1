# CGPA Calculator

This repository contains a simple Python-based CGPA (Cumulative Grade Point
Average) calculator.

## Project Structure

```
/cgpa_calculator
    cgpa.py          # calculator logic and CLI
    test_cgpa.py     # unit tests (pytest)
    __init__.py      # package marker
```

## Running the Calculator

Install dependencies (only pytest if you plan to run tests):

```bash
python3 -m pip install -r requirements.txt  # if requirements file exists
# or simply: pip install pytest
```

Run interactively (command‑line):

```bash
python3 -m cgpa_calculator.cgpa
```

Type each course grade and credit (e.g. `A 3`) per line. Press enter on an
empty line to compute the CGPA.

Run the GUI version:

```bash
python3 -m cgpa_calculator.gui
```

A window will appear where you can paste or type courses one per line and
click **Calculate** to see the result. The **Clear** button resets the form.

Run the web version (requires Flask):

```bash
python3 -m cgpa_calculator.web
```

Then open `http://localhost:8000` in a browser and enter courses into the
text area. Submit the form to see your CGPA calculation.

## Running Tests

```bash
pytest cgpa_calculator/test_cgpa.py
```
