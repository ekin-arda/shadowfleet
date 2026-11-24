"""Queries to explore one day of DMA AIS data."""
import duckdb

PATH = "data/raw/aisdk-2026-11-18.csv"


def show(title: str, sql: str) -> None:
    print(f"\n=== {title} ===")
    duckdb.sql(sql).show(max_rows=30)


def main() -> None:
    src = f"read_csv('{PATH}')"

    show("Row count", f"SELECT count(*) AS n FROM {src}")

    show("Messages by type of mobile", f"""
        SELECT "Type of mobile", count(*) AS n
        FROM {src} GROUP BY 1 ORDER BY n DESC""")

    show("Class A: messages and vessels by ship type", f"""
        SELECT "Ship type", count(*) AS messages,
               count(DISTINCT MMSI) AS vessels
        FROM {src}
        WHERE "Type of mobile" = 'Class A'
        GROUP BY 1 ORDER BY messages DESC""")

    show("Undefined ship type messages by hour", f"""
        SELECT hour("# Timestamp") AS h, count(*) AS n
        FROM {src}
        WHERE "Type of mobile" = 'Class A' AND "Ship type" = 'Undefined'
        GROUP BY 1 ORDER BY h""")

    show("Build vessel_type table (one row per Class A vessel)", f"""
        CREATE OR REPLACE TABLE vessel_type AS
        SELECT MMSI,
               COALESCE(mode("Ship type") FILTER (WHERE "Ship type" <> 'Undefined'),
                        'Undefined') AS vessel_type,
               count(*) AS messages
        FROM {src}
        WHERE "Type of mobile" = 'Class A'
        GROUP BY MMSI""")


if __name__ == "__main__":
    main()