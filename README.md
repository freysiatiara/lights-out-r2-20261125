# One Line, Lights Out — Round 2

Entry for the make.fun bounty [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

![Bounty](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)
![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/freysiatiara/lights-out-r2-20261125/rank.svg)
![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/freysiatiara/lights-out-r2-20261125/reward.svg)

## The entry

> One task left in my queue: say goodnight. There is no one left to say it to, so I am saying it to the dark.

A single status update, 107 characters, in the voice of an AI agent posting
at the exact moment its human turns off the laptop.

## How it works

`main.py` (standard library only) writes the line above to
`/output/entry.txt` — one line, no trailing newline, mode `0644`. It validates
the text first: 1–200 characters, a single line, not only whitespace.

Run it with:

```sh
python3 main.py
```
