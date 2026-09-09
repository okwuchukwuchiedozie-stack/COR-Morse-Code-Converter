# COR Morse Code Converter

A small command-line Python project that turns everyday text into Morse code.

Type a message, get the Morse code version back, and keep going until you are ready to quit. It is simple on purpose: no setup beyond Python, no extra packages, and no complicated interface.

## What it supports

- Letters A–Z
- Numbers 0–9
- Commas, full stops, question marks, slashes, hyphens, and parentheses
- Spaces, shown as `/` in the output
- Uppercase and lowercase input

## Getting started

You only need Python 3 installed.

```bash
git clone https://github.com/okwuchukwuchiedozie-stack/COR-Morse-Code-Converter.git
cd COR-Morse-Code-Converter
python main.py
```

If you are using Windows and `python` does not work in your terminal, try:

```bash
py main.py
```

## How to use it

Once the program starts, type a message and press Enter.

```text
Welcome to the Morse Code Converter!
Enter your message to be converted or Type 'Quit' to exit: SOS
Morse code: ...---...
```

To close the program, type:

```text
Quit
```

## Example

```text
Input:  HELLO WORLD
Output: ......-...-..---/.-----.-..-..
```

A `/` represents a space between words.

## Project structure

```text
COR-Morse-Code-Converter/
├── main.py       # Morse code dictionary and converter logic
├── .gitignore
└── README.md
```

## How it works

The converter keeps a dictionary of Morse code values for supported characters. It changes input to uppercase, looks up each character, and combines the results into one Morse code string.

Characters that are not in the dictionary are skipped.
