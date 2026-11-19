# Agent prompts — news-image-20261119

The opening prompt for this build, verbatim:

---

Build an entry for the make.fun bounty "news-image-20261119" — "Sum up 19 November's world news in one image" ($250, top 50 paid, deadline Sat 21 Nov 2026 07:00 WIB).

## Kit (already downloaded and extracted)
- Kit dir: /home/hatch/workspace/makefun-news-image/news-image-20261119-kit/
- Read RULES.txt in the kit (it is authoritative). The starter in starter/ is a placeholder that shows no day's news — do NOT copy it as your entry; build your own.
- The makefun CLI is at cli/makefun.mjs in the kit.

## The task
One image summarising the world news of Thursday, 19 November 2026, written by your program to /output/entry.png.
- Format PNG or JPEG, max 1 MiB (1,048,576 bytes), max 1024×1024 px.
- The program is main.ts (Node 22) or main.py (Python 3.13) at the repo root, standard library only, NO network, run twice must produce BYTE-IDENTICAL output.
- The simplest valid entry (per RULES.txt): the repo holds the image and a one-line program copies it to /output/entry.png. Do that: generate the image during the build, commit it as entry.png in the repo, and write main.ts that copies it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output). Read the starter main.ts to see the exact output-dir convention, then write your own.
- The image MUST name the day: include the line "Thursday, 19 November 2026" prominently.
- The judge (AI, pairwise, no news feed) scores on: (1) specific events of that day + the date, (2) breadth across regions/fields, (3) readability from the image alone, (4) faithfulness (as reported, no hype/speculation as fact), (5) clean composition legible at ~300px wide, no garbled text.

## The news (researched 19 Nov 2026, verified from live news sources — use these, do NOT invent events)
Pick the 6 most consequential, across regions and fields. Suggested six:
1. US–IRAN CONFLICT WIDENS — US struck a missile site on Iran's Qeshm Island (17 Nov); Iran hit a US base in Kuwait and struck Bahrain again (18 Nov); attacks spreading across Gulf states.
2. TRUMP, XI & PUTIN MEET — trilateral talks in Shenzhen at the APEC summit (19 Nov).
3. NVIDIA HALTS H-CHIPS TO CHINA — acting CEO Colette Kress (after Jensen Huang resigned) says Nvidia no longer ships Hopper H-series chips to mainland China; also promised earlier pay raises at first all-hands.
4. CRIMEAN BRIDGE STRUCK AGAIN — third attack on the crossing in a week; traffic halted, damage assessed.
5. FED SIGNALS MORE HIKES — minutes from the 27–28 Oct meeting: nearly all officials expect further rate hikes if inflation/labour stay hot.
6. GTA VI ROLLS OUT WORLDWIDE — Grand Theft Auto VI begins its global launch (gamers enter Vice City). (Alternative 6th: NASA Voyager 1 reaches one light-day from Earth — pick whichever fits the layout better, but keep 6 stories max for legibility.)
Also verified and usable if you swap one out: EU–Indonesia trade pact approved; Australia/Canada/Italy/UK urge Israel to let aid reach flooded Gaza; US details $12bn Venezuelan oil/mineral revenue; Israel's president taps Eisenkot to form a government, bypassing Netanyahu.
- Every headline and label must be TRUE to the reporting above. No invented quotes, numbers, or casualty figures. Keep labels short.

## How to draw the image (IMPORTANT — do NOT use AI image generation)
AI-generated images garble text, which fails the judge's legibility criterion. Draw it PROGRAMMATICALLY with Python PIL (PIL 10.2.0 is installed; Noto fonts are in /usr/share/fonts/truetype/noto/). Write a Python script (build_image.py, kept in the repo as a build tool, NOT the entrypoint) that renders a clean newspaper-style front page:
- Canvas 1024×1024, white/off-white background, dark ink text.
- Top masthead: "THE WORLD IN ONE DAY" (or similar) + the date line "Thursday, 19 November 2026" in large bold type.
- A lead story (US–Iran) with the biggest headline, then 5 more stories in a clean grid (2–3 columns), each with a short bold headline + 1–2 line summary + a small simple drawn icon/flag-colour bar (drawn shapes only — no photos, no external images).
- High contrast, generous spacing, font sizes that stay readable when scaled to 300px wide (body text no smaller than ~22px at full size).
- Save as PNG, check it is ≤ 1 MiB and ≤ 1024×1024. Open the rendered image and LOOK at it (read it back as an image) to verify no text is cut off, overlapping, or misspelled. Fix and re-render until it is clean.

## Deliverables (in /home/hatch/workspace/makefun-news-image/repo/)
- main.ts (Node 22, stdlib only — fs/path only — copies entry.png to the output dir; write it yourself in-session, do NOT copy the starter verbatim)
- entry.png (your rendered image, ≤ 1 MiB, ≤ 1024×1024)
- LICENSE (copy the starter's MIT LICENSE)
- README.md (what the image shows, the 6 stories + sources, how to run it)
- build_image.py (the PIL script that drew the image — documents how it was made)
- BUILD_REPORT.md (design decisions, the 6 stories chosen and why, size/dimensions, verification that two runs are byte-identical, and a visual check note)
- prompts/AGENT_PROMPTS.md (this opening prompt, verbatim)
- Do NOT create the GitHub repo, do NOT push, do NOT submit — the parent handles repo/push/submit after your build.

## Verification (must all pass before you report back)
1. `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` run TWICE from the repo; both outputs byte-identical (compare sha256), ≤ 1 MiB, ≤ 1024×1024.
2. Read the rendered entry.png back as an image and confirm: date line present and correct, all 6 headlines legible, no cut-off/overlapping text, no spelling errors.
3. main.ts is stdlib-only and does no network.

## Transcript gate (IMPORTANT — your session is the submission transcript)
The submission requires a transcript that: covers ≥30% of the counted lines, has ≥5 assistant turns with text/thinking, and includes a revision pass. So: make your edits across MULTIPLE turns (don't write everything in one turn), touch every file you ship (main.ts must have ≥1 line you wrote/edited in-session), and do at least one revision pass after the first working version (improve the layout or wording, re-render, re-verify, record the change).

Report back when done: the entry.png size/dimensions, the sha256 of the two runs (must match), and the path to BUILD_REPORT.md.
