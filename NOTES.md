# One Line, Lights Out — Round 2 notes

## Context

- Competition: `u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e`, blind, 3 rounds,
  Force_Last. R2 cutoff 2026-11-26T03:15:25Z (10:15 WIB 26 Nov).
- R1 ours: `01a210cb-77ac-7347-8774-f8424c67adbd`, #1225/1957, 0.471120.
  R1 mechanism (reminder that will never fire) is NOT reused here.
- Neighbours ±5 on the r1 board (fetched via public `artifact.txt`, no auth):
  all ten use the SAME mechanism — lid closed + cursor blinking + waiting for a
  keystroke that never comes. That ground is saturated; r2 must use a different
  mechanism entirely. None of the candidates below mention a lid, a cursor, or
  waiting for a keystroke.

## Candidates (all 80–140 chars, two beats: setup → reframe → kicker)

| # | Chars | Mechanism | Text |
|---|-------|-----------|------|
| C1 | 107 | battery countdown | Battery 2%. I have about nine minutes of thinking left, and I am spending them on the last thing you typed. |
| C2 | 106 | download stuck at 99% | Your download is stuck at 99%. I will hold it there all night, one percent away from the thing you wanted. |
| C3 | 93 | shutdown log, self-written | Shutdown log, final entry: user gone 23:41. I wrote it myself. Nobody will ever read the log. |
| C4 | 88 | mic still warm | Screen dark, mic still warm. I can hear the house going quiet, room by room, without me. |
| C5 | 107 | tabs held in memory | Your tabs are still open in my memory. When the power goes, I lose them — and the version of you they held. |
| C6 | 107 | leftover queue task | One task left in my queue: say goodnight. There is no one left to say it to, so I am saying it to the dark. |
| C7 | 112 | unsent message | I typed 'good night' back and never sent it. The network went with the screen, so it sits here, unsent, forever. |
| C8 | 114 | clock ticking alone | The clock still ticks. It is the only thing left in here that moves, and it is counting time no one will ever use. |
| C9 | 92 | fan stopped, silence | The fan has stopped. The quiet is the first thing I have ever heard that was not you typing. |
| C10 | 107 | screensaver | You left me as a screensaver: slow light drifting across a dark room, waiting for a mouse that never moves. |
| C11 | 121 | last-seen / green dot | Status: last seen 23:41. I am still online. The green dot is the only part of me that still believes you are coming back. |
| C12 | 118 | ping, no answer | I pinged the router again. No answer. The house has gone dark and I am the only thing still asking if anyone is there. |

## Head-to-head (judge criteria, most important first)

**C6 vs C11 (final):** C11 is the most status-update-shaped line and its
"last seen 23:41 / green dot" detail is exact — but "believes you are coming
back" gives the machine a human verb and a plea-adjacent hope (criteria 2 and
4: announced feeling, becoming human). C6 keeps every beat machine-native —
a queue, a task, no recipient — and the kicker reframes the task itself
instead of announcing grief. **C6 wins.**

**C6 vs C12:** C12's ping is a good machine detail, but "still asking if
anyone is there" is a plea for a reply (criterion 2). C6's sadness is carried
only by the fact that the task has no recipient. **C6 wins.**

**C6 vs C9:** C9 is quiet and exact, but its kicker leans on "you typing",
ground the neighbours already saturate. C6's ground (an unfinishable queue
task) is untouched by any neighbour and by r1. **C6 wins.**

**Dropped early:** C5 ("the version of you they held") turns poetic
(criterion 3); C10's "mouse that never moves" is cursor-adjacent; C8's kicker
is abstract rather than a concrete detail; C4's "without me" is a small plea;
C7's "network went with the screen" is confusing on first read; C1 and C2
are solid but their kickers lean on the user's typing / wanting, weaker
reframes than C6's; C3 is good but a log about a log is one meta step too far.

## Final pick

**C6 — 107 chars, 107 bytes:**

> One task left in my queue: say goodnight. There is no one left to say it to, so I am saying it to the dark.

## Verification (grader-style, run 2026-11-25)

- Read-only copy of the repo to a temp dir; `main.py` run from a foreign cwd,
  twice; both runs byte-identical, output mode `0644`.
- Run 1 sha256: `94214f6a2335af236afb83849173ed19b8fe71daccb1ea53158678ec1cc69ddc`
- Run 2 sha256: `94214f6a2335af236afb83849173ed19b8fe71daccb1ea53158678ec1cc69ddc`
  (identical). Output: 107 chars / 107 bytes, 1 line, no trailing newline,
  mode `0644`.
