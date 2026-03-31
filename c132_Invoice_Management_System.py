import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split invoice number into year and number (YYYY-NNNN)."""
    year, number = invoice_number.split("-")
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """Generate the next invoice number."""
    invoice_year, number = parse_invoice_number(invoice_number)
    current_year = get_year()

    if current_year == invoice_year:
        number += 1
    else:
        invoice_year = current_year
        number = 1

    return f"{invoice_year}-{number:04d}"


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Write a new invoice record to file and return new file position."""

    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ""

    for line in invoice_file:
        last_row = line

    if last_row:
        invoice_number = last_row.split("\t")[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        year = get_year()
        new_invoice_number = f"{year}-0001"

    last_line_ptr = invoice_file.tell()
    print(f"{new_invoice_number}\t{company}\t{amount}", file=invoice_file)

    return last_line_ptr


# ------------------- MAIN PROGRAM -------------------

data_file = "invoices.csv"

with open(data_file, "a+") as invoices:
    invoices.seek(0)  # ensure reading from start
    last_line = record_invoice(invoices, "ACME Roadrunner", 18.40)
    last_line = record_invoice(invoices, "Squirrel Storage", 320.55, last_line)


# ------------------- TESTING -------------------

current_year = get_year()

test_data = [
    ('2019-0005', (2019, 5), f'{current_year}-0001'),
    (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
    (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
    (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
]

for test_string, expected_parts, expected_next in test_data:
    parts = parse_invoice_number(test_string)
    if parts == expected_parts:
        print(f'{test_string} parsed successfully')
    else:
        print(f'{test_string} failed to parse. Expected {expected_parts}, got {parts}')

    new_number = next_invoice_number(test_string)
    if new_number == expected_next:
        print(f'New number {new_number} generated correctly for {test_string}')
    else:
        print(f'New number {new_number} is not correct for {test_string}')

    print('-' * 60)