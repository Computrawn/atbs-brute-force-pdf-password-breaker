#! python3
# brute_force.py — An exercise in manipulating PDFs.
# For more information, see project_details.txt.

from typing import Generator
import logging
from PyPDF2 import PdfReader

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def read_text_file() -> Generator[str, None, None]:
    """Create and return generator object of stripped contents of dictionary.txt."""
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        return (word.strip() for word in f.readlines())


def find_password(passwords):
    """Check user-defined file against each word from generator using
    PyPDF2 decrypt method and print password if match found."""
    reader = PdfReader(
        f"{input('Please type name of PDF you would like to crack: ')}.pdf"
    )

    for word in passwords:
        if reader.decrypt(word) == 2:
            print(f"The password is {word}.")
            break
        if reader.decrypt(word.lower()) == 2:
            print(f"The password is {word.lower()}.")
            break


def main():
    find_password(read_text_file())


if __name__ == "__main__":
    main()
