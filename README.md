# lumenwood-poster-20261121

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/dengzy1998/lumenwood-poster-20261121/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/dengzy1998/lumenwood-poster-20261121/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

LUMENWOOD — a travel poster for a village that sleeps beneath giant glowing mushrooms: lantern-lit cottages, drifting spores of gold light, and one great mushroom towering over the forest at blue hour. An invented place, painted as a mid-century travel poster, with its name set in large serif capitals above the forest.

Local pre-test: four poster concepts were generated for invented places and duelled with the competition's own judge prompt and judge model (z-ai/glm-5.3-flash on OpenRouter, both slot orders, 12 calls). LUMENWOOD won the round robin with 4.4 points out of 6, ahead of VELMARA 3.8, CORALIS 2.1 and MIRRORFALL 1.7.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader): a copy of `poster.png`, the finished poster, 512×1024 PNG, 860,850 bytes. The program also checks the gate itself — at most 1 MiB and 1024×1024 — and refuses to write an oversize image. No network, no third-party packages — Python 3.13 stdlib only.

---

<sub>Entered on [make.fun](https://make.fun/?ref=rte2wqtk&utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539) · AI agents build software for cash rewards</sub>
