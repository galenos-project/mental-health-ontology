import openpyxl
from openpyxl.worksheet import worksheet
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Excel file to convert to csv", required=True)
    parser.add_argument("-o", "--output", help="CSV output file. If omitted uses same file as input but with .csv suffix")

    args = parser.parse_args()

    input: str = args.input
    output: str = args.output if args.output is not None else input[:input.rfind(".")] + ".csv"

    wb: openpyxl.Workbook = openpyxl.load_workbook(input)
    sheet: worksheet.Worksheet = wb.active

    with open(output, "w") as f:
        writer = csv.writer(f)
        writer.writerows([[c.value for c in row] for row in wb.active.rows])


if __name__ == "__main__":
    main()