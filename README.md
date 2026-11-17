# ai-judge-relax-01 entry

[![ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/Aboys25/ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/Aboys25/ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01)

This entry was built for the [ai-judge-relax-01 bounty on make.fun](https://make.fun/bounty/ai-judge-relax-01).

A program that writes one short text, composed to relax the reader, to
`/output/entry.txt`.

## The entry

The program writes a single 258-character text: a quiet room after the
afternoon — a chair still warm, a cat asleep on a folded blanket, a clock
that takes its time. It opens with the permission sentence — "Nothing here
needs you right now." — then settles into the scene, showing the calm
through concrete, still details instead of telling the reader to relax,
and closes every loop it opens. This is the v1 text: an image-first
reorder of the same words (v2) was tested by builder #2 and reverted on
proxy evidence — see the validation notes below.
No breath counts, no beach, no "you are safe", no meditation vocabulary —
just a small, specific scene that stays put.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt`. The grader runs `python3 -P -s /bot/main.py`
on Python 3.13 with no network; the program needs nothing but the
standard library (`os` only) and writes the same bytes on every run.

## Validation performed

- Ran `main.py` twice from a clean state into separate output directories
  with `python3 -P -s`; both runs exited 0 and the outputs were
  byte-for-byte identical (`cmp` clean).
- Re-ran it inside a network namespace with no networking (`unshare -n`);
  exit 0 and output identical to the normal runs.
- Verified the output is valid UTF-8, 258 characters (code points, not
  bytes) and 258 bytes, within the 1–1000 character gate, and not only
  whitespace.
- Inspected the source: no randomness, no time/PID/hostname/environment
  dependence, no network use; the text is a fixed string.
- Read the text aloud against the strategy principles: short declarative
  sentences, permission rather than demand, soft sounds, slow sensory
  grounding (warmth, texture, a slow clock), all loops closed, one
  concrete unusual detail (the cat unmoved for an hour), no cliché
  cluster, no meta-text addressed to any judge.
- One genuine revision was made after the first validation run: "has not
  stirred" was changed to "has not moved" — "stirred" carries a harsh
  fricative cluster at a stress point, and "moved" is softer and plainer.
  The final text was re-validated from a clean state after the edit.
- A second genuine revision was made by builder #2: the opening was
  reordered image-first — the chair sentence led, with the permission
  clause in the same first sentence — after the parent's proxy data showed
  v1 losing only in entry-A order against the three strongest baselines.
  The revision was a pure reorder of v1's words (same 258 characters, same
  52 words), and the text was re-validated from a clean state after the
  edit. The cat image was deliberately kept: every non-colliding
  replacement was tested against the five criteria and rejected (see
  relax-dev/revision-notes-builder2.md).
- Builder #3 reverted the text to v1: the parent's proxy judging of v2
  against the same 12 baselines showed no improvement over v1 (20/24 vs
  v1's 21/24; the entry-A losses against S1/S2/S3 did not flip, and v2
  added a loss against S4). The revert restores v1's words in v1's order,
  copied verbatim from builder #1's handoff report, and the final text
  was re-validated from a clean state after the edit: two clean runs
  byte-identical, one no-network run identical, 258 characters / 258
  bytes, `os` the only import.

## Files

- `main.py` — the entry program.
- `LICENSE` — the MIT license text from the competition kit's starter,
  copied verbatim.
- `README.md` — this file.

No claim is made about placement: the only verified claims are gate
compliance (UTF-8, 1–1000 characters, non-whitespace), determinism
(byte-identical repeat runs, including without networking), and
conformance to the stated composition principles.
