# Say What Actually Broke

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/hiduplahzomb/u-po-pu-say-what-actually-broke-a2c153b5-ka-r2/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/hiduplahzomb/u-po-pu-say-what-actually-broke-a2c153b5-ka-r2/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One-line entry for make.fun's "Say What Actually Broke" bounty: a plain,
boring-accurate explanation of a real outage — no joke, no meme.

## The entry

> At 09:41 a config push set the payment timeout to 50 milliseconds instead of 50 seconds; 612 checkouts failed in 9 minutes before the old value was restored.

## How it works

`main.py` writes the single sentence to `entry.txt` inside
`MAKEFUN_OUTPUT_DIR` (or `/output`), then reads it back and verifies
byte-for-byte that it matches the `TEXT` constant. It exits non-zero
if the entry is not exactly one line of 1–200 characters.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
