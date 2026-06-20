import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", required=True)
    parser.add_argument("--site", required=True)
    args = parser.parse_args()

    index = Path(args.site) / "index.html"
    html = index.read_text(encoding="utf-8")

    expected = f"ambiente={args.environment}"
    if expected not in html:
        raise SystemExit(f"Smoke test failed: missing {expected}")
    if "total=85" not in html:
        raise SystemExit("Smoke test failed: expected calculated total")

    print(f"Smoke tests passed for {args.environment}")
