#! python3
# brute_force.py — An exercise in manipulating PDFs.
# For more information, see project_details.txt.

import logging
from PyPDF2 import PdfReader, PdfWriter

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def create_dictionary():
    with open("dictionary.txt", "r") as f:
        dictionary_list = f.readlines()
        stripped_list = []
        for word in dictionary_list:
            stripped_list.append(word.strip())
            stripped_list.append(word.lower().strip())
    return stripped_list


def find_password(passwords):
    user_input = input("Please type name of PDF you would like to crack: ")
    pdf_to_decrypt = f"{user_input}.pdf"
    reader = PdfReader(pdf_to_decrypt)

    for word in passwords:
        if reader.decrypt(word) == 2:
            print(f"The password is {word}.")
            break


password_list = create_dictionary()
find_password(password_list)
