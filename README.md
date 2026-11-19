# The World in One Day — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ryanmahrez44/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ryanmahrez44/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world news of **Thursday, 19 November 2026**,
built for the [make.fun "Sum up 19 November's world news in one image"
bounty](https://make.fun/bounty/news-image-20261119). A newspaper front
page, drawn programmatically with Python PIL — crisp text, no photos, no
AI-generated imagery.

## What the image shows

Six stories, chosen for consequence and breadth across regions and fields:

1. **U.S.–Iran Strikes Widen Across the Gulf** (Middle East) — Washington
   hit a missile site on Iran's Qeshm Island; Tehran struck a U.S. base in
   Kuwait and hit Bahrain again.
2. **Trump, Xi and Putin to Meet in Shenzhen** (Diplomacy) — trilateral
   talks on the sidelines of the APEC summit.
3. **Nvidia Halts H-Chips to China** (Technology) — acting chief Colette
   Kress says no more Hopper chips for the mainland, and pledges earlier
   pay rises.
4. **Crimean Bridge Struck a Third Time** (Europe) — the crossing is hit
   again in a week; traffic halts while damage is assessed.
5. **Fed Signals More Rate Hikes Ahead** (Economy) — minutes show nearly
   all officials expect further rises if inflation stays hot.
6. **GTA VI Begins Its Global Rollout** (Culture) — Grand Theft Auto VI
   launches worldwide as players enter Vice City.

Every headline is faithful to the reporting of 19 November 2026; nothing
is invented, no quotes or figures were made up. Sources: live news wires
and news round-ups of 19 November 2026 (see BUILD_REPORT.md).

## How it works

- `build_image.py` — the PIL script that draws `entry.png` (1024×1024,
  ~138 KB). Run it to re-render the image.
- `main.ts` — the entrypoint (Node 22, standard library only). It copies
  `entry.png` to the output directory, so both runs produce byte-identical
  output:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
