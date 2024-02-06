import csv
import dataclasses
import os
from collections.abc import Generator
from itertools import groupby
from pathlib import Path

import openpyxl
import openpyxl.worksheet
from openpyxl import Workbook
from openpyxl.cell.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

LOCAL_PREFIX = "GMHO"


@dataclasses.dataclass
class External:
    prefix: str
    uri_prefix: str
    purl: str


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    with open(os.path.join(base_dir, "scripts", "external.csv"), "r") as f:
        reader = csv.DictReader(f)
        purls = dict([(r["PREFIX"], External(r["PREFIX"], r["URI_PREFIX"], r["PURL"])) for r in reader])

    ids = []
    for f in Path(base_dir).rglob("*.xlsx"):
        if os.path.basename(os.path.dirname(f)) == "UpperLevel":
            continue

        wb: Workbook = openpyxl.load_workbook(f, True)
        sheet: Worksheet = wb.active
        data: Generator[list[Cell], None, None] = sheet.rows

        header = next(data)

        id_col = next(i for i, v in enumerate(header) if v.value == "ID")
        label_col = next(i for i, v in enumerate(header) if v.value == "Label")
        curation_status_col = next(i for i, v in enumerate(header) if v.value == "Curation status")
        for row in data:
            id_value = row[id_col].value
            label_value = row[label_col].value
            curation_status = row[curation_status_col].value
            if id_value is not None and isinstance(id_value, str) and id_value.split(":")[0] != LOCAL_PREFIX:
                ids.append((id_value.split(":")[0], id_value, label_value))

    ids.sort(key=lambda x: x[0])
    by_ontology = groupby(ids, key=lambda x: x[0])

    wb = Workbook()
    sheet = wb.active
    sheet.append(["Ontology ID", "PURL", "ROOT_ID", "IDs", "Intermediates", "Prefix"])
    for o, ids in by_ontology:
        e = purls.get(o, None)
        if e is None or e.purl is None:
            purl = input(f"PURL for {o}: ")
            e = External(o, e.prefix if e is not None else None, purl)
            purls[o] = e

        sheet.append([o, e.purl, "entity [BFO:0000001]", '; '.join((f'{l} [{i}]' for _, i, l in ids)), "all"])

    wb.save(os.path.join(base_dir, "UpperLevel", f"{LOCAL_PREFIX}_External_Imports.xlsx"))

    with open(os.path.join(base_dir, "scripts", "external.csv"), "w") as f:
        writer = csv.DictWriter(f, ["PREFIX", "URI_PREFIX", "PURL"])
        writer.writeheader()
        writer.writerows(({
            "PREFIX": p.prefix,
            "URI_PREFIX": p.uri_prefix,
            "PURL": p.purl
        } for p in purls.values()))


if __name__ == "__main__":
    main()
