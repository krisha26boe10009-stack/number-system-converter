# Project Statement

## Problem Statement

Students and programmers frequently need to convert numbers between
different bases (binary, octal, decimal, hexadecimal, and others), but
most simple converters only handle one fixed pair of bases (e.g. only
binary-to-decimal) and quit after a single conversion. This project
solves that by building a general-purpose converter that works between
**any two bases from 2 to 36** and stays open for repeated use in one
session, similar to how a scientific calculator lets you keep working
without restarting.

## Scope of the Project

- Command-line, menu-driven application (no GUI in this version)
- Supports integer conversions (including negative integers) between
  bases 2–36
- Keeps a running history of conversions for the current session, with
  an optional persistent log file
- Does **not** currently handle fractional/decimal-point numbers —
  flagged as a future enhancement (see `README.md`)

## Target Users

- Students learning number systems / computer organization concepts
- Programmers who occasionally need a quick, reliable base converter
  without depending on an online tool

## High-Level Features

1. **Input validation** — rejects malformed numbers or out-of-range
   bases with a clear message before any conversion is attempted
2. **Conversion engine** — converts any base to decimal and decimal to
   any base, composed together for a full any-to-any conversion
3. **Session history / logging** — records every conversion performed,
   viewable at any time, with optional write-to-file logging
4. **Repeatable, menu-driven workflow** — convert as many numbers as
   needed in one run, view history, clear history, or quit
