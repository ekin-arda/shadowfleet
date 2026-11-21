# Data sources

## DMA historical AIS (Danish Maritime Authority)

- **What:** Daily CSV files of AIS position reports from the Danish
  shore-based AIS system.
- **Where:** http://aisdata.ais.dk/
- **Downloaded:** 21-11-2026, file for 2026-11-18 (about 2.7 GB uncompressed)
- **Format:** CSV, one row per position report, 26 columns, timestamps
  as `dd/mm/yyyy hh:mm:ss`, missing values appear as empty fields or
  the text `Unknown`.
- **Terms:** The download page (aisdata.ais.dk) states no explicit
  license or terms of use (checked 21-11-2026). The only related document
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