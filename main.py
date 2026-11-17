# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one short text, composed to relax the reader, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# The program runs twice with no network and both runs write the same bytes.
# Output is written in binary mode so the bytes are exactly the UTF-8
# encoding of TEXT, with no platform line-end or encoding surprises.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "Nothing here needs you right now. "
    "The chair by the window is still warm from the afternoon, "
    "and the cat asleep on the folded blanket has not moved for an hour. "
    "The clock ticks once, then waits, as if it too has nowhere to be. "
    "You can stay exactly as you are."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
