import argparse

from doctor_scraper.pipeline import run_to_excel


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--url", default="https://www.medifind.com/specialty/otolaryngology")
    args = parser.parse_args()

    out = run_to_excel(output_path=args.output, url=args.url)
    print(out)
