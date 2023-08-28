#! python3
# brute_force.py — An exercise in manipulating PDFs.
# For more information, see project_details.txt.

import logging
from PyPDF2 import PdfReader

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def find_password():
    """Check user-defined PDF against each word from generator using
    PyPDF2 decrypt method and print password if match found."""

    with open("dictionary.txt", "r", encoding="utf-8") as f:
        passwords = (word.strip() for word in f.readlines())

    reader = PdfReader(
        f"{input('Please type name of PDF you would like to crack: ')}.pdf"
    )

    print("Checking for password ...")

    for word in passwords:
        if reader.decrypt(word) == 2:
            print(f"The password is {word}.")
            break
        if reader.decrypt(word.lower()) == 2:
            print(f"The password is {word.lower()}.")
            break


def main():
    find_password()


if __name__ == "__main__":
    main()
