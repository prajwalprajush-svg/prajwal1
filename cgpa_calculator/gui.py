"""Tkinter-based GUI for the CGPA calculator."""

import tkinter as tk
from typing import List, Tuple

from cgpa_calculator.cgpa import calculate_cgpa


class CgpaGui:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("CGPA Calculator")

        tk.Label(root, text="Enter courses (grade credit) one per line:").pack(pady=(10, 0))

        self.text = tk.Text(root, height=10, width=40)
        self.text.pack(padx=10, pady=5)

        self.result_label = tk.Label(root, text="CGPA:", font=(None, 12, "bold"))
        self.result_label.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Calculate", command=self.compute).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)

    def parse_lines(self, lines: List[str]) -> List[Tuple[str, float]]:
        entries = []
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) != 2:
                raise ValueError("Each line must have a grade and credits separated by space")
            grade = parts[0]
            try:
                credits = float(parts[1])
            except ValueError:
                raise ValueError("Credit hours must be numeric")
            entries.append((grade, credits))
        return entries

    def compute(self) -> None:
        raw = self.text.get("1.0", tk.END)
        lines = raw.strip().splitlines()
        try:
            entries = self.parse_lines(lines)
            cgpa = calculate_cgpa(entries)
            self.result_label.config(text=f"CGPA: {cgpa}")
        except Exception as exc:
            self.result_label.config(text=f"Error: {exc}")

    def clear(self) -> None:
        self.text.delete("1.0", tk.END)
        self.result_label.config(text="CGPA:")


def run_gui() -> None:
    root = tk.Tk()
    CgpaGui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
