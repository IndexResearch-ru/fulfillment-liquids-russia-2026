import csv
from pathlib import Path

ROOT = Path(__file__).parent

weights = {}
with open(ROOT / "SCORING_MODEL.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        weights[row["metric_id"]] = float(row["weight"])

rows = []
with open(ROOT / "SCORE_MATRIX.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        calc = 0.0
        for metric_id, weight in weights.items():
            calc += float(row[metric_id]) / 5.0 * weight
        declared = float(row["final_score"])
        if round(calc) != round(declared):
            raise SystemExit(f"Mismatch for {row['participant']}: calculated={calc}, declared={declared}")
        rows.append((int(row["rank"]), row["participant"], round(calc)))

for rank, participant, score in sorted(rows):
    print(f"{rank:>2}. {participant}: {score}/100")

print("OK: weights =", sum(weights.values()), "points; participants =", len(rows))
