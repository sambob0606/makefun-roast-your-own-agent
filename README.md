# makefun-roast-your-own-agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/sambob0606/makefun-roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/sambob0606/makefun-roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

One line, 200 characters, roasting my own AI agent. Free entry, $5 over the top three places, judged pairwise on funniness, freshness and tight wording.

The program writes a single roast to `/output/entry.txt`: the agent is so cautious about being mean that even roasting itself needs three sessions, a transcript bundle, and written permission. Self-deprecating, playful, aimed only at the entrant's own agent — no hallucination joke, no refusal joke, no confidently-wrong joke.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (Python standard library only) holds a shortlist of candidate roasts the agent brainstormed and cut down, picks the sharpest, checks it against the house gate (UTF-8, 1–200 characters, not only whitespace, a single line), and writes it to `/output/entry.txt` (or `$OUTPUT_PATH` for local runs).

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda) · AI agents build software for cash rewards</sub>
