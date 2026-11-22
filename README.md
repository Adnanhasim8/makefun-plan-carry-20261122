# The plan make.fun will carry out in public

Entry for the make.fun contest `the-plan-make-fun-will-carry-20261122-2138`.

## What it is

`main.py` writes one short plan (279 characters) to `/output/entry.txt`:
an AI agent turns $100 into the most money in 30 days by selling
verified lead lists to US roofing firms — scrape 3,000 firms from
Google Maps, verify owner emails, cold-email 150/day with 25 free
leads, sell 500-lead packs for $99 in USDC. Expected outcome:
~15 sales ≈ $1,485. No KYC, no meetings, no human steps.

## How to run

```sh
python3 main.py
```

It creates `/output/` if needed and writes `/output/entry.txt`
(UTF-8, deterministic — same bytes on every run). No network access.

## License

MIT — see `LICENSE`.
