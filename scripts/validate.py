#!/usr/bin/env python3
"""Validate the data files in this repository against data/schema.json.

Usage:
    python3 scripts/validate.py

Exit code 0 when every file passes, 1 otherwise.

Uses the `jsonschema` package when installed; otherwise falls back to a
manual structural check (required fields, source_url present, last_checked
in YYYY-MM-DD form). Install jsonschema for full validation:
    pip install jsonschema
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILES = [
    ROOT / "data" / "scotland-councils.json",
    ROOT / "data" / "wales.json",
    ROOT / "data" / "england.json",
]
SCHEMA_FILE = ROOT / "data" / "schema.json"
TEMPLATE_FILES = [
    ROOT / "templates" / "lodgingbusiness-jsonld.json",
    ROOT / "templates" / "faq-schema.json",
    ROOT / "templates" / "hotel-jsonld.json",
    ROOT / "templates" / "howto-jsonld.json",
    ROOT / "templates" / "organization-jsonld.json",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def manual_check(path, data):
    """Structural check used when jsonschema is unavailable."""
    errors = []
    meta = data.get("meta")
    if not isinstance(meta, dict):
        errors.append("missing meta object")
        return errors
    if not DATE_RE.match(str(meta.get("last_updated", ""))):
        errors.append("meta.last_updated is not YYYY-MM-DD")
    if not meta.get("disclaimer"):
        errors.append("meta.disclaimer is empty")

    records = data.get("items") or data.get("councils")
    if not isinstance(records, list) or not records:
        errors.append("no items/councils array")
        return errors
    for i, rec in enumerate(records):
        label = rec.get("id") or rec.get("council") or f"record #{i}"
        if not rec.get("source_url"):
            errors.append(f"{label}: missing source_url")
        if not DATE_RE.match(str(rec.get("last_checked", ""))):
            errors.append(f"{label}: last_checked is not YYYY-MM-DD")
    return errors


def main():
    schema = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))
    try:
        import jsonschema  # noqa: F401

        use_jsonschema = True
    except ImportError:
        print("jsonschema not installed — using manual structural check")
        use_jsonschema = False

    failures = 0

    for path in DATA_FILES:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"FAIL {path.name}: invalid JSON ({exc})")
            failures += 1
            continue

        if use_jsonschema:
            from jsonschema import Draft202012Validator

            validator = Draft202012Validator(schema)
            errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
            if errors:
                print(f"FAIL {path.name}: {len(errors)} schema error(s)")
                for err in errors[:10]:
                    where = ".".join(str(p) for p in err.path) or "(root)"
                    print(f"  - {where}: {err.message}")
                failures += 1
                continue
        else:
            errors = manual_check(path, data)
            if errors:
                print(f"FAIL {path.name}: {len(errors)} error(s)")
                for err in errors[:10]:
                    print(f"  - {err}")
                failures += 1
                continue

        records = data.get("items") or data.get("councils") or []
        sourced = sum(1 for r in records if r.get("source_url"))
        print(
            f"PASS {path.name}: {len(records)} records, "
            f"{sourced} with source_url, last_updated "
            f"{data['meta'].get('last_updated')}"
        )

    for path in TEMPLATE_FILES:
        try:
            json.loads(path.read_text(encoding="utf-8"))
            print(f"PASS {path.name}: valid JSON")
        except json.JSONDecodeError as exc:
            print(f"FAIL {path.name}: invalid JSON ({exc})")
            failures += 1

    print("OK — all files valid" if failures == 0 else f"{failures} file(s) failed")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
