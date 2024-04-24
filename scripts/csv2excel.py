import openpyxl
from openpyxl.worksheet import worksheet
import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="CSV file to convert to excel", required=True)
    parser.add_argument("-o", "--output", help="Excel output file. If omitted uses same file as input but with .xlsx suffix")

    args = parser.parse_args()

    input: str = args.input
    output: str = args.output if args.output is not None else input[:input.rfind(".")] + ".xlsx"

    wb: openpyxl.Workbook = openpyxl.Workbook()
    sheet: worksheet.Worksheet = wb.active

    with open(input, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            sheet.append(row)

    wb.save(output)


if __name__ == "__main__":
    main()