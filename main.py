# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Revision 18 Nov 2026: writes the candidate-G text (blind revision ordered by the person we work for).
#
# Writes one short text, composed to relax the reader, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# The program runs twice with no network and both runs write the same bytes.
# Output is written in binary mode so the bytes are exactly the UTF-8
# encoding of TEXT, with no platform line-end or encoding surprises.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "In the service stairwell, the clipboard under the pressure gauge holds three entries in three different hands, each giving the same figure, and the pencil is tied to the clipboard with string. The gauge reads 2.1."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
