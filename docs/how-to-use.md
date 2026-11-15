# How to use this data

## Files at a glance

| File | Shape | Records |
|---|---|---|
| `data/scotland-councils.json` | `{meta, councils[]}` — one record per council | 32 |
| `data/wales.json` | `{meta, items[]}` — one record per rule | 19 |
| `data/england.json` | `{meta, items[]}` — one record per rule | 11 |
| `data/summary.csv` | Flat CSV, all jurisdictions | 62 |

## Field definitions

### Scotland — council record

| Field | Meaning |
|---|---|
| `council` | Council name |
| `licence_required` | `true` — a licence is mandatory across Scotland |
| `control_area` | `true` if a short-term let control area is in force; `false` if not; `null` if not verifiable |
| `fee_range` | Licence fee range as published by the council (usually a 3-year licence). `null` if the council does not publish fees in a readable form |
| `fine` | Maximum fine for operating without a licence |
| `planning_note` | Planning position (control area, change of use) |
| `notes` | Caveats — e.g. fee year, conflicting schedules, pending consultations |
| `source_url` | Official council page / fee schedule / policy PDF |
| `last_checked` | Date the record was last checked (YYYY-MM-DD) |

### Wales / England — rule record

| Field | Meaning |
|---|---|
| `id` | Stable record ID (use it when reporting corrections) |
| `topic` | registration / penalties / visitor_levy / licensing / planning / business_rates / council_tax / tax |
| `title` | Short human-readable title |
| `value` | Headline value. `null` means the official source has not published it |
| `detail` | Full explanation (English) |
| `detail_zh` | Full explanation (Chinese) |
| `status` | `in_force` / `not_yet_in_force` / `legislated_not_in_force` / `announced_expected` / `not_yet_published` / `proposal_only` / `consultation_closed_outcome_pending` |
| `source_name` | Human-readable source name |
| `source_url` | Official page the record was checked against |
| `last_checked` | Date the record was last checked (YYYY-MM-DD) |
| `verification` | `direct-read` (official page opened and read) or `search-verified` (official page quoted verbatim via search results) |
| `additional_sources` | Extra references (may include non-official explainers — the primary `source_url` is always official) |

### Meta object (every data file)

`last_updated` (date the file was last refreshed), `sources` (list of official sources used), `disclaimer` (reference-only, not legal advice).

## Examples

**Find the Edinburgh licence fee (Python):**

```python
import json
data = json.load(open("data/scotland-councils.json"))
edinburgh = next(c for c in data["councils"] if c["council"] == "City of Edinburgh")
print(edinburgh["fee_range"], edinburgh["source_url"])
```

**List everything not yet in force (jq):**

```bash
jq -r '.items[] | select(.status | test("not_yet|announced|proposal")) | [.id, .value] | @tsv' data/england.json
```

**Validate after editing:**

```bash
python3 scripts/validate.py
```

## Citing the data

Link to the file and the record's `source_url`. Include the `last_checked` date so readers know how fresh the figure is. Example:

> Scotland licence fees by council — directbook.uk dataset, checked 2026-11-16, source: City of Edinburgh Council fee schedule.

## What `null` means

A `null` value means the official source has not published that figure as of the `last_checked` date. It is not zero and not an estimate. Check the record's `notes` / `detail` for context, and re-check the official source — the figure may have been published since.

## Reporting corrections

Open an Issue with the record ID, the correct value, and a link to the official source. Corrections with an official source link are usually merged within a few days.
