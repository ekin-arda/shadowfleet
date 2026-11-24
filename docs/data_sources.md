# Data sources

## DMA historical AIS (Danish Maritime Authority)

- **What:** Daily CSV files of AIS position reports from the Danish
  shore-based AIS system.
- **Where:** http://aisdata.ais.dk/
- **Downloaded:** 2026-11-21, file for 2026-11-18 (about 2.7 GB uncompressed)
- **Format:** CSV, one row per position report, 26 columns, timestamps
  as `dd/mm/yyyy hh:mm:ss`, missing values appear as empty fields or
  the text `Unknown`.
- **Terms:** The download page (aisdata.ais.dk) states no explicit
  license or terms of use (checked 2026-11-21). The only related document
  found is the DMA's AIS data management policy
  (dma.dk, "AIS data management policy"), which concerns access to
  AIS data under the Danish PSI act and does not state a license for
  these open files. Treated as: no guarantee of correctness, lawful
  handling by the recipient, no combination with other data that makes
  persons identifiable. License status unconfirmed.
- **Constraints that shape this project:**
  - DMA does not guarantee the correctness of the data.
  - The recipient must handle the data lawfully and must not combine it
    in a way that makes persons identifiable.
  - Data is published as open data for a limited period, so raw files
    are not stored in this repository.

## Design constraints

- Only commercial vessels are analyzed (AIS Class A transponders;
  cargo and tanker ship types).
- Vessels are matched to sanctions lists by IMO/MMSI only. Only
  vessel-level fields are used (name, flag, listing date, listing
  authority). Owner, operator and other person-level fields are dropped.
- No raw position tracks are published, only aggregated indicator tables.
- Outputs are risk indicators, not accusations.