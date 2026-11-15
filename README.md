# UK Short-Term Let Regulations 2026

Structured, source-linked data on **UK short term let licensing 2026** — covering the **Scotland STL licence by council**, the **Wales visitor accommodation register**, and the **England short-term let register**. Built for hosts, agents, developers and researchers who need the rules in machine-readable form, with every figure traceable to an official page.

**Current status, November 2026:** Scotland already requires a council licence before you take a booking; Wales requires free registration by 31 March 2027; England's national register is announced but not yet open.

> **Reference only, not legal advice.** Rules change — always confirm against the official source linked in each record before acting. This dataset is maintained by [directbook.uk](https://directbook.uk/), a UK web developer building commission-free direct-booking websites for B&Bs and holiday lets.

## Quick comparison

| | Scotland | Wales | England |
|---|---|---|---|
| **Licence / register** | Mandatory council licence since 1 Oct 2022 | Free registration by **31 Mar 2027** (Welsh Revenue Authority) | National register expected **Mar 2027**, not yet open |
| **Cost** | Council-set, usually 3 years (e.g. Edinburgh £120–£6,869; Glasgow £156–£494) | Registration free; visitor levy £1.30 / 75p per person per night (each council decides, earliest 1 Apr 2027) | Fee not yet published |
| **Penalty** | Up to **£2,500** fine + possible 1-year ban on reapplying | **£100** late registration per premises, escalating to **£1,400** max | Not yet published |
| **Planning** | Control areas: Edinburgh (whole area) + Highland's Badenoch & Strathspey; elsewhere case-by-case | C3 / C5 / C6 use classes; Article 4 can remove permitted development | Case-by-case by local authority; Greater London **90-night** annual cap |
| **What's next** | Fee schedules reviewed each April | Full licensing scheme likely **2029**; statutory default **4 Mar 2030** | Register opening, fee and operator to be announced |

## What's in this repo

| File | Contents |
|---|---|
| `data/scotland-councils.json` | All **32 Scottish councils**: licence required, control area, fee range, fine, planning note, source, last checked |
| `data/wales.json` | **19 items**: registration, penalties, visitor levy, licensing, planning, business rates, council tax |
| `data/england.json` | **11 items**: national register, London 90-night cap, planning, business rates, tax |
| `data/summary.csv` | All 62 records in one flat file for spreadsheets |
| `data/schema.json` | JSON Schema for the three data files |
| `docs/how-to-use.md` | How to use, cite and download the data |
| `docs/sources.md` | Every official source, grouped by jurisdiction |
| `docs/safety-requirements.md` | Fire, gas, electrical, insurance and EPC summaries (England) |
| `templates/lodgingbusiness-jsonld.json` | `BedAndBreakfast` / `LodgingBusiness` JSON-LD template with `licenceNumber` |
| `templates/faq-schema.json` | FAQPage JSON-LD template (7 licensing questions) |
| `scripts/validate.py` | Validates all data files against the schema |
| `scripts/update-check.md` | Monthly update checklist |
| `llms.txt` | Machine-readable repo summary for AI tools |

Every record carries a `source_url` and a `last_checked` date (YYYY-MM-DD). A `null` value means the official source has not published that figure — we never invent numbers. Where a figure comes from an older published schedule (e.g. a 2025/26 fee table still current on a council page), the record's `notes` say so.

## How to use the data

**Download:** clone the repo, or download individual files from the `data/` folder above.

```bash
git clone https://github.com/yasuo22/uk-short-term-let-regulations-2026.git
cd uk-short-term-let-regulations-2026
python3 scripts/validate.py   # checks all data files against data/schema.json
```

**Cite it:** link to the file and the record's `source_url`. Example: "Scotland licence fees by council, directbook.uk dataset, checked 2026-11-16, source: City of Edinburgh Council fee schedule."

**Use the templates:** copy `templates/lodgingbusiness-jsonld.json` into your property website, replace every `EXAMPLE-` value with your real details, and test it with [Google's Rich Results Test](https://search.google.com/test/rich-results).

See [`docs/how-to-use.md`](docs/how-to-use.md) for field definitions and examples.

## How this fits with directbook.uk

We build the websites this dataset describes the rules for. Our guides go deeper on each nation:

- [UK short-term rental regulations — overview](https://directbook.uk/short-term-rental-regulations/)
- [Scotland short-term let licence](https://directbook.uk/scotland-short-term-let-licence/)
- [Wales holiday let registration](https://directbook.uk/wales-holiday-let-registration/)
- [England short-term let register](https://directbook.uk/england-short-term-let-register/)
- [Converting a property to a holiday let in Wales](https://directbook.uk/converting-a-property-to-a-holiday-let-in-wales/)
- [B&B website cost in the UK](https://directbook.uk/bed-and-breakfast-website-cost-uk/)

Every site we build includes a visible licence / registration number field, so you can display your credentials. Displaying the number is not the same as holding the licence: planning permission, licensing and safety compliance remain your responsibility. See [pricing](https://directbook.uk/pricing/).

## Changelog

### v1.0.0 — 2026-11-16

- Initial release. Scotland: all 32 councils with fees from official schedules (2 councils' fees unpublished in readable form — East Lothian, North Lanarkshire). Wales: 19 items, all sourced. England: 11 items, all sourced. Safety summaries (England), JSON-LD templates, validation script.

## Contributing & maintenance

- **Found an error or an out-of-date figure?** Open an Issue with the record ID, the correct value and a link to the official source.
- **Want to add a council or a jurisdiction?** Fork, follow the existing record format (every record needs `source_url` + `last_checked`), run `python3 scripts/validate.py`, and open a pull request.
- **Maintenance:** we re-check official sources monthly (see `scripts/update-check.md`), with extra checks around the Wales registration deadline (31 March 2027) and the England register opening (expected March 2027). Version bumps: patch for data refreshes, minor for new fields, major for breaking changes.

## Licence

MIT — see [LICENSE](LICENSE). Data is compiled from public official sources; the compilation and templates are released under MIT. Official guidance remains the property of its publishers.
