"""Entry for make.fun contest the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (279 characters) to /output/entry.txt: an AI agent
turns $100 into the most money in 30 days by selling verified lead
lists to US roofing firms, paid in USDC. No network, deterministic.
"""

import os

ENTRY = (
    "Day 1: spend $30 on Apify+Hunter, scrape 3,000 US roofing "
    "firms, verify emails. Days 2-7: email 150/day, give 25 free "
    "leads, land first $99 sale. Days 8-30: sell 500 leads for $99 "
    "in USDC. Expect ~15 sales = $1,485. Edge: verified niche data, "
    "paid in USDC, no KYC/meetings."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
