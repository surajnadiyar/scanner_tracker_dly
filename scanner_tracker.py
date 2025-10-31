import pandas as pd

offroll = pd.read_csv("offroll_mapping.csv")
offroll_dict = dict(zip(offroll['scanner_id'], offroll['name']))

scans = pd.read_csv("daily_scans.csv")
scans['scanner_name'] = scans['scanner_id'].map(offroll_dict).fillna("On-Roll Employee")
scans.to_csv("tracked_scans.csv", index=False)

print("Top 10 Scanners:\n", scans['scanner_name'].value_counts().head(10))
