
import os
import csv
import json
from pathlib import Path

docs_dir = Path("docs/licenses")
summaries_dir = docs_dir / "summaries"
full_text_dir = docs_dir / "full_text"
index_path = docs_dir / "index.csv"
print("docs_dir",docs_dir)
rows = []
for summary_file in summaries_dir.glob("*.json"):
    license_id = summary_file.stem.replace("_summary", "").lower()
    with open(summary_file) as f:
        data = json.load(f)
    full_text_file = full_text_dir / f"{license_id.upper()}.txt"
    if not full_text_file.exists():
        continue
    rows.append({
        "license_id": license_id,
        "license_name": data.get("license_name", "Unknown"),
        "SPDX_code": data.get("SPDX_code", "NONE"),
        "summary_path": f"summaries/{summary_file.name}",
        "full_text_path": f"full_text/{full_text_file.name}",
        "approved_by": data.get("approved_by", "Unknown"),
        "category": data.get("category", "Permissive")
    })

with open(index_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated: {index_path}")
