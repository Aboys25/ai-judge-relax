# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Revision 18 Nov 2026: writes the candidate-K2 text, part of a submit-and-see sequence ordered by the person we work for.
#
# Writes one short text, composed to relax the reader, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# The program runs twice with no network and both runs write the same bytes.
# Output is written in binary mode so the bytes are exactly the UTF-8
# encoding of TEXT, with no platform line-end or encoding surprises.
# Verified byte-exact against the candidate text file and deterministic across runs.
# Output is 982 bytes with no trailing newline, byte-identical to cand-k2.txt.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "Three days ago the driver parked the bus behind the fence at the end of the yard, wiped the fare box with a cloth, folded the cloth over the box, and stepped down onto the gravel, and the yard gate shut with a soft knock. The bus stands with its doors open and its engine cold, and the suspension has settled by slow degrees until the frame rides level on its springs. The hiss from the doors has run down to nothing. The fan behind the driver has quit humming, and the hum in the ceiling lights has gone with it, and the bus keeps only the ticking of metal cooling underneath. The ticks thin until long minutes pass between them, and each tick arrives dry and brief, and leaves nothing after it. A paper luggage label hangs from a grab pole by a loop of twine, its ink faded to pale strokes and the name gone, with no bag beneath it and no journey left to mark. The poles stand empty, the light through the windows crosses the floor in a slow band, and the last tick does not come."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
