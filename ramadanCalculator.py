#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Countdown to historical estimated Ramadan start dates (not authoritative)."""
from __future__ import annotations
import argparse
from datetime import date
import tkinter as tk
from tkinter import ttk

# Original project's historical estimates, not independently verified.
# Local moon sighting and official announcements may differ by one or more days.
ESTIMATES = {
    "2018": date(2018, 5, 16),
    "2019": date(2019, 5, 6),
    "2020": date(2020, 4, 24),
    "2021": date(2021, 4, 13),
    "2022": date(2022, 4, 3),
    "2023": date(2023, 3, 23),
    "2024": date(2024, 3, 11),
    "2025": date(2025, 3, 1),
    "2026": date(2026, 2, 18),
    "2027": date(2027, 2, 8),
    "2028": date(2028, 1, 28),
    "2029": date(2029, 1, 16),
    "2030 (first)": date(2030, 1, 6),
    "2030 (second)": date(2030, 12, 26),
    "2031": date(2031, 12, 15),
    "2032": date(2032, 12, 4),
}

def days_until(target: date, today: date | None = None) -> int:
    return (target - (today or date.today())).days

def result(label: str, today: date | None = None) -> str:
    if label not in ESTIMATES:
        raise ValueError("Unknown estimate")
    target = ESTIMATES[label]
    count = days_until(target, today)
    when = f"{count} days remaining" if count >= 0 else f"{-count} days ago"
    return f"Estimated start: {target.isoformat()} — {when}"

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", choices=tuple(ESTIMATES), help="CLI mode")
    args = parser.parse_args()
    if args.year:
        print(result(args.year))
        return
    root = tk.Tk()
    root.title("Ramadan Date Estimates")
    root.geometry("540x240")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    selected = tk.StringVar(value="2026")
    output = tk.StringVar()
    ttk.Label(frame, text="Select an estimated Ramadan start (historical dataset)").pack(pady=8)
    ttk.Combobox(frame, textvariable=selected, values=tuple(ESTIMATES), state="readonly").pack(pady=5)
    def update() -> None:
        output.set(result(selected.get()))
    ttk.Button(frame, text="Calculate days", command=update).pack(pady=10)
    ttk.Label(frame, textvariable=output).pack()
    ttk.Label(frame, text="Dates are estimates, not official moon-sighting announcements.", wraplength=490).pack(pady=10)
    update()
    root.mainloop()

if __name__ == "__main__":
    main()
