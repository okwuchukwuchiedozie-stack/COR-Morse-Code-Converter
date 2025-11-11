MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-', 'L': '.-..',  'M': '--',   'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-', 'V': '...-',  'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def string_to_morse(text):
    morse_text = ""
    for char in text.upper():
        if char == "":
            morse_text += "/"
        elif char in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char]
        else:
            morse_text += ""
    return morse_text.strip()

def main():
    print("Welcome to the Morse Code Converter!")
    is_finished = True
    while is_finished:
        message = input("Enter your message to be converted or Type 'Quit' to exit: ")
        if message.lower() == "quit":
            print("Thank you for using Morse Code Converter. Goodbye!")
            is_finished = False
        else:
            morse_code = string_to_morse(message)
            if morse_code == "":
                print("You've typed an invalid message")
                is_finished = False
            else:
                print(f"Morse code: {morse_code}")

if __name__ == "__main__":
    main()

# is_finished = True
# while is_finished:
#     message = input("Enter your message: ")
#     morse_code = string_to_morse(message)
#     if morse_code == "":
#         print("You've typed an invalid message")
#         is_finished = False
#     else:
#         print(f"Morse code: {morse_code}")
