import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path

ROOT = Path(__file__).parent.parent

df = pd.read_csv(ROOT / "output" / "processed.csv")

# Bar chart: revenue by region
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["region"], df["revenue"])
ax.set_title("Revenue by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Total Revenue")
plt.tight_layout()
plt.savefig(ROOT / "output" / "chart.png", dpi=150)

# PDF report
with PdfPages(ROOT / "output" / "report.pdf") as pdf:
    pdf.savefig(fig)
    # Add a summary table page, title page, etc.