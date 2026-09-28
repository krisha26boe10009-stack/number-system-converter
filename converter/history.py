"""
----------
history.py
----------
FUNCTIONAL MODULE 3: Conversion History / Logging
This module is essentially a history keeper for all conversions 
performed during the current session,
and has an optional persistence feature (saving to a log file). 
This module allows the project to hit the "Logging or monitoring" requirement box, 
while also providing an extra feature (reviewing past conversions) instead of a bolted-on solution.
"""

import datetime
import os


class ConversionHistory:
    """ Stores and displays running log of ceonversions for one session"""

    def __init__(self, log_file=None):
        self._entries = []
        # Resource efficiency: only touch the filesystem if the caller
        # actually wants persistent logging.
        self.log_file = log_file

    def add_entry(self, result: dict):
        """
        Record one conversion. `result` is the dict returned by
        NumberConverter.convert().
        """
        entry = dict(result)  # shallow copy so we own our own data
        entry["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._entries.append(entry)

        if self.log_file:
            self._write_to_file(entry)

    def _write_to_file(self, entry):
        """Append a single line to the log file. Failures here should
        never crash the main program (Reliability requirement) -
        logging is a nice-to-have, not core functionality."""
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(
                    f"[{entry['timestamp']}] "
                    f"{entry['input']} (base {entry['from_base']}) -> "
                    f"{entry['output']} (base {entry['to_base']})\n"
                )
        except OSError as e:
            print(f"(Warning: could not write to log file: {e})")

    def load_from_file(self):
        """
        Read past conversions back in from self.log_file, if it exists,
        so history survives between separate runs of the program.
        Parses lines written by _write_to_file(), e.g.:
        [2026-09-26 15:57:25] 1010 (base 2) -> A (base 16)
        """
        if not self.log_file or not os.path.exists(self.log_file):
            return

        import re
        pattern = re.compile(
            r"\[(?P<timestamp>.+?)\] (?P<input>.+?) \(base (?P<from_base>\d+)\) -> "
            r"(?P<output>.+?) \(base (?P<to_base>\d+)\)"
        )

        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    match = pattern.match(line.strip())
                    if match:
                        self._entries.append({
                            "timestamp": match.group("timestamp"),
                            "input": match.group("input"),
                            "from_base": int(match.group("from_base")),
                            "output": match.group("output"),
                            "to_base": int(match.group("to_base")),
                        })
        except OSError as e:
            print(f"(Warning: could not read log file: {e})")

    def show(self):
        """ Priint a numed list of every conversions so far"""
        if not self._entries:
            print("No conversions yet this session.")
            return

        print("\n--- Conversion History ---")
        for i, entry in enumerate(self._entries, start=1):
            print(
                f"{i}. {entry['input']} (base {entry['from_base']}) -> "
                f"{entry['output']} (base {entry['to_base']})  "
                f"[{entry['timestamp']}]"
            )
        print("---------------------------\n")

    def clear(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)
