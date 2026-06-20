import argparse
from pathlib import Path

from pipeline_demo import render_summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    html = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Modulo 5 CI/CD Demo</title>
    <style>
      body {{ font-family: system-ui, sans-serif; margin: 3rem; line-height: 1.5; }}
      code {{ background: #f2f4f7; padding: 0.15rem 0.35rem; border-radius: 4px; }}
    </style>
  </head>
  <body>
    <h1>Modulo 5 CI/CD Demo</h1>
    <p id="summary">{render_summary(args.environment)}</p>
    <p>Este archivo fue generado por el pipeline para <code>{args.environment}</code>.</p>
  </body>
</html>
"""
    (output / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
