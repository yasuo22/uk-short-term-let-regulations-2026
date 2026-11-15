# Monthly update checklist

Run these checks once a month (first working day) and after any announced
regulatory change. Update `last_checked` / `last_updated` dates, the version
number and the changelog in `README.md` whenever a value changes.

> The data in this repo is reference only, not legal advice. Always verify
> against the official source linked in each record before relying on it.

## 1. England — national short-term let register

- [ ] Check GOV.UK for the national register status (expected to open
      March 2027 as of November 2026). Has it opened? Has the date moved?
- [ ] Check whether the registration fee, renewal period or penalties
      have been published.
- [ ] Check the Greater London 90-night rule for changes.
- [ ] Update `data/england.json` and `data/summary.csv`.

## 2. Wales — visitor accommodation registration & licensing

- [ ] Check GOV.WALES / Welsh Revenue Authority for registration
      deadline changes (deadline: 31 March 2027 as of November 2026).
- [ ] Check the visitor levy (tourism tax) rates and start date.
- [ ] Check the licensing scheme timeline (planned 2029 as of
      November 2026) and the March 2030 statutory default.
- [ ] Check the 252-day / 182-day thresholds and C3 → C6 planning
      rules for changes.
- [ ] Update `data/wales.json` and `data/summary.csv`.

## 3. Scotland — licensing scheme & councils

- [ ] Check GOV.SCOT for scheme-level changes (fees guidance, fines,
      deadlines).
- [ ] Spot-check at least 5 council fee schedules (rotate through all
      32 across the year) for fee changes.
- [ ] Check for new or changed short-term let control areas.
- [ ] Update `data/scotland-councils.json` and `data/summary.csv`.

## 4. Safety & other requirements

- [ ] Check fire, gas, electrical, insurance and EPC guidance for
      changes (GOV.UK / HSE).
- [ ] Update `docs/safety-requirements.md` if applicable.

## 5. Validation & release

- [ ] Run `python3 scripts/validate.py` — all data files must pass.
- [ ] Bump the version in `README.md` changelog (patch for data
      refresh, minor for new fields, major for breaking changes).
- [ ] Commit with a dated message, e.g. `data: monthly refresh 2026-12-01`.
- [ ] Create a GitHub Release when a material rule changes
      (e.g. England register opens, Wales deadline passes).

## 6. Monitoring (quarterly)

- [ ] Check GitHub traffic / clones and search ranking for the target
      keywords (UK short term let licensing 2026, Scotland STL licence
      by council, Wales visitor accommodation register, England
      short-term let register).
- [ ] Check whether AI Overviews / ChatGPT / Gemini cite this dataset.
- [ ] Review open Issues for data-correction requests.
