#!/usr/bin/env python

import argparse
import sys

FREQ_TABLE = {
    "REST": "0",
    "A0": "28",
    "BB0": "29",
    "A#0": "29",
    "B0": "31",
    "C1": "33",
    "DB1": "35",
    "C#1": "35",
    "D1": "37",
    "EB1": "39",
    "D#1": "39",
    "E1": "41",
    "F1": "44",
    "GB1": "46",
    "F#1": "46",
    "G1": "49",
    "AB1": "52",
    "G#1": "52",
    "A1": "55",
    "BB1": "58",
    "A#1": "58",
    "B1": "62",
    "C2": "65",
    "DB2": "69",
    "C#2": "69",
    "D2": "73",
    "EB2": "78",
    "D#2": "78",
    "E2": "82",
    "F2": "87",
    "GB2": "92",
    "F#2": "92",
    "G2": "98",
    "AB2": "104",
    "G#2": "104",
    "A2": "110",
    "BB2": "117",
    "A#2": "117",
    "B2": "123",
    "C3": "131",
    "DB3": "139",
    "C#3": "139",
    "D3": "147",
    "EB3": "156",
    "D#3": "156",
    "E3": "165",
    "F3": "175",
    "GB3": "185",
    "F#3": "185",
    "G3": "196",
    "AB3": "208",
    "G#3": "208",
    "A3": "220",
    "BB3": "233",
    "A#3": "233",
    "B3": "247",
    "C4": "262",
    "DB4": "277",
    "C#4": "277",
    "D4": "294",
    "EB4": "311",
    "D#4": "311",
    "E4": "330",
    "F4": "349",
    "GB4": "370",
    "F#4": "370",
    "G4": "392",
    "AB4": "415",
    "G#4": "415",
    "A4": "440",
    "BB4": "466",
    "A#4": "466",
    "B4": "494",
    "C5": "523",
    "DB5": "554",
    "C#5": "554",
    "D5": "587",
    "EB5": "622",
    "D#5": "622",
    "E5": "659",
    "F5": "698",
    "GB5": "740",
    "F#5": "740",
    "G5": "784",
    "AB5": "830",
    "G#5": "830",
    "A5": "880",
    "BB5": "932",
    "A#5": "932",
    "B5": "988",
    "C6": "1047",
    "DB6": "1109",
    "C#6": "1109",
    "D6": "1175",
    "EB6": "1245",
    "D#6": "1245",
    "E6": "1319",
    "F6": "1397",
    "GB6": "1480",
    "F#6": "1480",
    "G6": "1568",
    "AB6": "1661",
    "G#6": "1661",
    "A6": "1760",
    "BB6": "1865",
    "A#6": "1865",
    "B6": "1975",
    "C7": "2093",
    "DB7": "2217",
    "C#7": "2217",
    "D7": "2349",
    "EB7": "2489",
    "D#7": "2489",
    "E7": "2637",
    "F7": "2794",
    "GB7": "2960",
    "F#7": "2960",
    "G7": "3136",
    "AB7": "3322",
    "G#7": "3322",
    "A7": "3520",
    "BB7": "3729",
    "A#7": "3729",
    "B7": "3951",
    "C8": "4186",
}

DURATION_TABLE = {
    "1": "1",
    "2": "2",
    "2.": "3",
    "4": "4",
    "4.": "6",
    "8": "8",
    "8.": "12",
    "16": "16",
    "16.": "24",
    "32": "32",
    "32.": "48",
    "64": "64",
    "64.": "96",
}


def print_grub_init(tempo, notes):
    global FREQ_TABLE, DURATION_TABLE
    output = [tempo]

    for note in notes:
        parts = note.split(" ")
        if len(parts) != 2:
            print("Incorrect format for input")
            sys.exit(1)

        note, duration = parts[0].upper(), parts[1]

        if note in FREQ_TABLE:
            output.append(FREQ_TABLE[note])
        else:
            print(f"{note} not a valid value, aborting")
            sys.exit(1)

        if duration in DURATION_TABLE:
            output.append(DURATION_TABLE[duration])
        else:
            print(f"{duration} not a valid value, aborting")
            sys.exit(1)

    if "64" in output:
        adjust_output(64, output)
    elif "32" in output:
        adjust_output(32, output)
    elif "16" in output:
        adjust_output(16, output)
    elif "8" in output:
        adjust_output(8, output)

    print(" ".join(output))


def adjust_output(factor, output):
    global DURATION_TABLE
    output[0] = str(int(output[0]) * (factor // 4))

    for index, note in enumerate(output[1:], start=1):
        if note in DURATION_TABLE.values():
            if note == "1":
                output[index] = str(factor)
            else:
                output[index] = str(factor // int(note))


def main(argv):
    parser = argparse.ArgumentParser(
        prog="grub_init_gen", description="GRUB_INIT_TUNE generator"
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="Prints only the resulting code, useful for inputs from files",
        action="store",
        nargs="*",
    )
    args = parser.parse_args(argv)

    quiet = False
    if args.quiet is not None:
        quiet = True

    if not quiet:
        print("What's the BPM?")
    tempo = input()
    notes = []

    if not quiet:
        print("Notes are typed like this:")
        print("NOTE DURATION [with a '.' after it if it's a dotted note]")
        print("If it's a rest, REST DURATION")
        print(
            "You can also type in comments starting with #, which will be ignored (useful if you're passing the notes from a file)\n"
        )

    while True:
        if not quiet:
            print(
                "What is the next note with its duration? (NOTE DURATION[.])\nIf you want to end the melody, type END\n"
            )
        note = input()

        if note.upper() == "END":
            break
        elif note.startswith("#"):
            continue
        notes.append(note)

    print_grub_init(tempo, notes)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nScript aborted")
        sys.exit(1)
