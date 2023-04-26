#! python3
# brute_force.py — An exercise in manipulating PDFs.
# For more information, see project_details.txt.

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.
