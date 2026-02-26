import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

steps = [
    {
        "label": "PPL pipeline",
        "cmd": ["ppl", "pipelines/process.ppl"],
    },
    {
        "label": "Python visualisation",
        "cmd": [sys.executable, "scripts/visualise.py"],
    },
]

for i, step in enumerate(steps, 1):
    print(f"[{i}/{len(steps)}] Running {step['label']}...")
    result = subprocess.run(step["cmd"], cwd=ROOT)

    if result.returncode != 0:
        print(f"\n[ERROR] {step['label']} failed (exit code {result.returncode}). Aborting.")
        sys.exit(1)

    print(f"        ✓ {step['label']} completed.\n")