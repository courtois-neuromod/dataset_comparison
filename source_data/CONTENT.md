# Source Data

All source data is manually curated and version-controlled via git.

- `schema.json` — JSON Schema defining all possible fields for a dataset entry. Edit this to add new modalities or sub-fields.
- `<name>.yaml` — one YAML file per dataset, with only the relevant fields populated. Validated against `schema.json` by `invoke fetch`.
- `<name>.md` — markdown sidecar per dataset, justifying each value with direct quotes from the corresponding publication(s) or official documentation.
