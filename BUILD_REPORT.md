# BUILD REPORT — news-image-20261119

## Entry
- Bounty: "Sum up 19 November's world news in one image"
  (https://make.fun/bounty/news-image-20261119, $250, top 50 paid)
- Deadline: Sat 21 Nov 2026 07:00 WIB
- Image: `entry.png` — 1024×1024 px, 137,920 bytes (limit: 1 MiB, 1024×1024)
- Entrypoint: `main.ts` (Node 22, stdlib only — `node:fs`, `node:path`)
- Method: the repo holds the image; `main.ts` copies it to the output
  directory. The image was drawn programmatically with Python PIL
  (`build_image.py`), never AI-generated, so no text is garbled.

## The six stories (all verified from live news of 19 Nov 2026)
Chosen for consequence and breadth across regions and fields:

1. **U.S.–Iran Strikes Widen Across the Gulf** (Middle East, lead) —
   US struck a missile site on Iran's Qeshm Island (17 Nov); Iran hit a
   US base in Kuwait and struck Bahrain again (18 Nov).
2. **Trump, Xi and Putin to Meet in Shenzhen** (Diplomacy, Asia) —
   trilateral talks at the APEC summit on 19 Nov.
3. **Nvidia Halts H-Chips to China** (Technology) — acting CEO Colette
   Kress (after Jensen Huang's resignation) says Nvidia no longer ships
   Hopper H-series chips to mainland China; also promised earlier pay
   raises at the first all-hands.
4. **Crimean Bridge Struck a Third Time** (Europe, war) — third attack
   on the crossing in a week; traffic halted, damage assessed.
5. **Fed Signals More Rate Hikes Ahead** (Economy, US) — minutes from
   the 27–28 Oct meeting: nearly all officials expect further hikes if
   inflation and the labour market stay hot.
6. **GTA VI Begins Its Global Rollout** (Culture, games) — Grand Theft
   Auto VI launches worldwide; players enter Vice City.

Also verified but left out for space/legibility: EU–Indonesia trade pact
approved; Australia/Canada/Italy/UK urge Israel to let aid reach flooded
Gaza; US details $12bn Venezuelan oil/mineral revenue; Israel's
president taps Eisenkot to form a government, bypassing Netanyahu;
NASA Voyager 1 reaches one light-day from Earth. Nothing in the image
is invented — no made-up quotes, numbers, or casualty figures.

## Design
- Newspaper front page: masthead "THE WORLD IN ONE DAY", date line
  "Thursday, 19 November 2026" in large bold type, lead story full
  width, 4 stories in a 2×2 grid, one full-width culture story, footer.
- Warm paper background (#fbf9f4), near-black ink, one accent colour
  per story's kicker. Icons are drawn shapes only (burst, flag circles,
  chip, bridge, rising chart, skyline) — no photos, no external images.
- Smallest body text 22 px at full size, headlines 29–47 px, so the
  page stays readable scaled to ~300 px wide.

## Revision pass (v1 → v2)
- v1 rendered cleanly except the TECHNOLOGY chip icon (40 px + pins)
  overlapped the "Nvidia Halts H-Chips to China" headline, and the
  chart arrow reached into the headline row.
- v2: chip reduced to a 26 px rounded square with an inner die and no
  pins; flag circles shrunk to r=11; chart arrow shrunk (56×20) and
  moved fully inside the kicker row. Re-rendered and visually inspected
  — no overlap, no cut-off text, no spelling errors.

## Verification
- `mkdir -p out out2 && MAKEFUN_OUTPUT_DIR=out node main.ts` and
  `MAKEFUN_OUTPUT_DIR=out2 node main.ts`:
  - out/entry.png sha256:
    `f4b6a3234f51e156647e508b222a226ca9a90b59debb548ebc114eae3189dc14`
  - out2/entry.png sha256: identical
  - repo entry.png sha256: identical — **BYTE-IDENTICAL across runs**
  - Dimensions 1024×1024, mode RGB, 137,920 bytes ≤ 1,048,576
- Visual check (image read back): date line present and correct, all
  six headlines legible, no cut-off or overlapping text, no spelling
  errors.
- `main.ts` is stdlib-only (`node:fs`, `node:path`), does no network,
  reads only `./entry.png`.
