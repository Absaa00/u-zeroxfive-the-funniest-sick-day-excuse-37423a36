#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Deterministic, no network, no input: prints exactly one sick-day excuse
under 200 characters, then exits.
"""

EXCUSE = (
    "I woke up fluent in a language I don't speak, and my cat is the only "
    "one who understands me - staying home until one of us learns English again."
)


def main() -> None:
    print(EXCUSE)


if __name__ == "__main__":
    main()
