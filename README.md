# scanner_tracker_dly
Maps numeric IDs to names for easier identification.
# Off-Roll Scanner Tracker

Maps numeric off-roll scanner IDs to names for accountability.

## Problem
- On-roll: ID = Name → tracked
- Off-roll: ID = Number → untraceable

## Solution
- Python + Pandas maps IDs → Names
- Enables RCA on scan errors, short-sent, compliance

## Files
- `scanner_tracker.py` – Main script
- `daily_scans.csv` – Sample input
- `offroll_mapping.csv` – Mapping

Built at Delhivery Hyderabad (with dummy data). Ready for WMS integration.
