# ai-judge-relax-01 entry (Python 3.13, standard library only).
# J2 revision (round 5, submit-and-see sequence): follow-up edit; output verified byte-exact against cand-j2.txt.
# Revision 18 Nov 2026: writes the candidate-J2 text, part of a submit-and-see sequence ordered by the person we work for.
#
# Writes one short text, composed to relax the reader, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# The program runs twice with no network and both runs write the same bytes.
# Output is written in binary mode so the bytes are exactly the UTF-8
# encoding of TEXT, with no platform line-end or encoding surprises.
# Verified byte-exact against the candidate text file and deterministic across runs.
# Output is 890 bytes with no trailing newline, byte-identical to cand-j2.txt.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The hedge along the lane gives the afternoon back to the lane, leaf by leaf, after the sun has gone behind the houses. The outer leaves are thin and dry, and each one lets go of its heat into the moving air. Where the twigs knot together and the light barely reaches, the leaves keep a small reserve of heat, and a sleeve brushing past carries a trace of it away on the cloth. A length of garden twine is tied twice round one low branch, the knot pulled tight and the cut end frayed open, with nothing hanging from it and no reason for it to be there. At elbow height the twigs are rubbed bare and smooth where people slip through, and the earth beneath is pressed flat and keeps the shape of feet. The hedge thins its heat into the lane through the evening, one leaf after another, until the leaves and the lane air are one temperature and the twine hangs from its branch, frayed end down."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
