# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Revision 18 Nov 2026: writes the candidate-M2 text, part of a submit-and-see sequence ordered by the person we work for.
#
# Writes one short text, composed to relax the reader, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# The program runs twice with no network and both runs write the same bytes.
# Output is written in binary mode so the bytes are exactly the UTF-8
# encoding of TEXT, with no platform line-end or encoding surprises.
# Verified byte-exact against the candidate text file and deterministic across runs.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The rail in the coop carries the line of hens, and the hens shuffle sideways until their bodies touch, and each one finds its place and falls quiet. The rail is worn smooth where feet grip it night after night, and the hens curl their toes around the wood and draw one foot up into the feathers of the breast, balancing on the other while the tails angle down over the rail. The muttering drops to single notes, and the single notes thin to nothing, and the hens tuck their beaks into the feathers along their backs and close their eyes. The feathers puff out and settle flat, and one hen shifts and grips the rail again, and the rail creaks once under the movement, and the others do not stir. The rail under the feet. The feet under the folded bodies. The folded bodies under the closed wings. The closed wings under the cold air of the coop, and the cold air under nothing at all. The rail takes the weight and keeps it through the cold hours, and the weight does not shift."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
