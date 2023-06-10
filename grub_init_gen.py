#!/usr/bin/env python3

import argparse
import sys
from frequencies import FREQ_TABLE
from duration import DURATION_TABLE


def print_grub_init(tempo, notes):
    output = [tempo]

    for note in notes:
        parts = note.split(" ")
        if len(parts) != 2:
            raise ValueError("Incorrect format for input")

        note, duration = parts[0].upper(), parts[1]

        if note not in FREQ_TABLE:
            raise ValueError(f"{note} not a valid value, aborting")
        output.append(FREQ_TABLE[note])

        if duration not in DURATION_TABLE:
            raise ValueError(f"{duration} not a valid value, aborting")
        output.append(DURATION_TABLE[duration])

    for duration in [64, 32, 16, 8]:
        if str(duration) in output:
            adjust_output(duration, output)
            break

    print(" ".join(output))


def adjust_output(factor, output):
    output[0] = str(int(output[0]) * (factor // 4))

    for index, note in enumerate(output[1:], start=1):
        if note in DURATION_TABLE.values():
            if note == "1":
                output[index] = str(factor)
            else:
                output[index] = str(factor // int(note))


def parse_args(argv):
    parser = argparse.ArgumentParser(prog="grub_init_gen",
                                     description="GRUB_INIT_TUNE generator")
    parser.add_argument(
        "-q",
        "--quiet",
        help="Prints only the resulting code, useful for inputs from files",
        action="store",
        nargs="*",
    )
    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)

    quiet = args.quiet is not None

    if not quiet:
        tempo = input("What's the BPM?")
        print("Notes are typed like this:")
        print("NOTE DURATION [with a '.' after it if it's a dotted note]")
        print("If it's a rest, REST DURATION")
        print("You can also type in comments starting with #, which will be "
              "ignored (useful if you're passing the notes from a file)\n")
        prompt = (
            "What is the next note with its duration? (NOTE DURATION[.])\n"
            "If you want to end the melody, type END\n")
    else:
        tempo = input()
        prompt = ""

    notes = []

    while True:
        note = input(prompt)
        if note.upper() == "END":
            break
        elif note.startswith("#"):
            continue
        notes.append(note)

    try:
        print_grub_init(tempo, notes)
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nScript aborted")
        sys.exit(1)
