# ppl_data_analytics

A demonstration project that showcases the [PPL](https://github.com) pipeline language working alongside Python for data processing and visualisation.

The pipeline ingests raw sales data, applies data quality rules, transforms and aggregates it by region, then hands the result off to a Python script that produces a bar chart and a PDF report.

## Project structure

```
ppl_data_analytics/
├── data/
│   └── sales.csv          # Raw sales input data
├── output/                # Generated artefacts (created at runtime)
│   ├── processed.csv
│   ├── chart.png
│   └── report.pdf
├── pipelines/
│   └── process.ppl        # PPL pipeline definition
├── scripts/
│   └── visualise.py       # Python visualisation script
├── run.py                 # Entry point – runs both steps in sequence
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9+
- The `ppl` CLI available on your `PATH`

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python run.py
```

This runs two steps in sequence:

1. **PPL pipeline** (`pipelines/process.ppl`) – loads `data/sales.csv`, cleans and aggregates the data, and writes `output/processed.csv`.
2. **Python visualisation** (`scripts/visualise.py`) – reads `output/processed.csv` and produces `output/chart.png` and `output/report.pdf`.

## Pipeline overview

| Step | Description |
|------|-------------|
| `source` | Load raw CSV |
| `assert` | Reject rows where `amount <= 0` |
| `fill` | Default missing `region` to `"Unknown"` |
| `trim` / `uppercase` | Normalise string columns |
| `cast` | Coerce `amount` → float, `date` → datetime |
| `filter` | Keep only `status == "completed"` rows |
| `add` | Derive `revenue = amount × quantity` |
| `group` / `agg` | Summarise by region (sum revenue, avg amount, count) |
| `sort` | Order by revenue descending |
| `save` | Write `output/processed.csv` |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
