# JSON-LD templates — how to use them

> Last checked: **2026-11-16**. Templates are examples only — replace every `EXAMPLE-` value with your real details before publishing. General information only, not legal advice.

This repository ships five schema.org JSON-LD templates in `templates/`. Paste the JSON inside a `<script type="application/ld+json"> … </script>` block in the `<head>` of the relevant page, then test it (see "Validate your markup" below).

## Which template for which page

| File | Type | Use it on |
|---|---|---|
| `templates/lodgingbusiness-jsonld.json` | `BedAndBreakfast` / `LodgingBusiness` | A B&B or holiday-let property page |
| `templates/hotel-jsonld.json` | `Hotel` | A hotel, guest house or inn page |
| `templates/faq-schema.json` | `FAQPage` | A licensing FAQ page (7 questions, facts checked 2026-11-16) |
| `templates/howto-jsonld.json` | `HowTo` | A guide page: "How to apply for a Scotland short-term let licence" |
| `templates/organization-jsonld.json` | `Organization` + `Service` | A business homepage (web design service for B&Bs and holiday lets) |

## How to replace the placeholders

Every value starting with `EXAMPLE-` is a placeholder and **must** be replaced before publishing:

| Placeholder | Replace with |
|---|---|
| `EXAMPLE — …` in `name` | Your real property or business name |
| `EXAMPLE-LICENCE-12345` in `licenceNumber` | Your real council licence or registration number. If you hold no licence or registration number yet, delete the `licenceNumber` field entirely — never publish a made-up number. |
| `example-…` in `url`, `email`, `sameAs` | Your real website, email and social profiles |
| `1 Example Lane`, `LA23 1AA`, `+44-20-7946-0000` | Your real address and phone number |
| `54.38`, `-2.91` in `geo` | Your real latitude and longitude |
| `ratingValue`, `reviewCount` in `aggregateRating` | Your real review figures, or delete `aggregateRating` if you have none |
| `numberOfRooms`, `priceRange`, `starRating`, `checkinTime`, `checkoutTime` | Your real figures; delete any field that does not apply |

**Hotel vs LodgingBusiness:** use `Hotel` for hotels, guest houses and inns; use `BedAndBreakfast` (a `LodgingBusiness` subtype) for a B&B or self-catering holiday let. Do not put both types on the same property page.

**Organization + Service:** the `makesOffer` prices in `organization-jsonld.json` are the published directbook.uk prices (£1,999 one-time build, £499/year care plan, checked 2026-11-16). If you adapt the template for your own business, replace them with your own prices.

**HowTo:** the steps follow the Scotland application process summarised in `data/scotland-councils.json` and on [directbook.uk/scotland-short-term-let-licence/](https://directbook.uk/scotland-short-term-let-licence/): contact your council, prepare documents, meet the mandatory conditions, wait for the decision without taking bookings, then display your licence number. Each council runs its own process and sets its own fees, so re-check your council's official page before publishing the guide. Do not add steps the official guidance does not support.

## Validate your markup

After pasting a template into your page, test it with [Google's Rich Results Test](https://search.google.com/test/rich-results):

1. Paste your page URL (or the code snippet) into the test.
2. Fix any errors it reports — a template with placeholder values left in will not be flagged, so check the placeholders by hand as well.
3. Re-test after every edit.

Note: valid JSON-LD does not guarantee a rich result in search — Google decides whether and how to show it.

## Keeping the facts current

The FAQ and HowTo templates quote licensing facts (deadlines, fines, fees) that change. Re-check them against the `data/` files in this repository — every record carries a `source_url` and a `last_checked` date — and against the official source before you rely on them. This repository is re-checked monthly; see `scripts/update-check.md`.
