// news-image-20261119 entry (Node 22, standard library only).
//
// The entry is the image file entry.png beside this program: a newspaper
// front page summing up Thursday, 19 November 2026, drawn programmatically
// during the build (see build_image.py). This program only copies it to the
// output directory the grader provides — /output, or MAKEFUN_OUTPUT_DIR
// when run locally:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// No network, no other files read, no randomness: the same bytes go in,
// the same bytes come out, on every run.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
