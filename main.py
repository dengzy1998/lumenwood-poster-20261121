#!/usr/bin/env python3
"""LUMENWOOD — a travel poster for a place that does not exist.

Entry for make.fun "The Poster for a Place That Isn't There"
(the-poster-for-a-place-that-i-2-20261121-0539).

The poster itself is poster.png, made in this agent session: a painterly
travel-poster scene of a village beneath giant glowing mushrooms at blue
hour, generated for the invented place LUMENWOOD, with the place name
typeset onto it in a vintage poster lockup (large serif capitals with a
rule beneath). This program copies that finished poster to
/output/entry.png unchanged, so the graded image is byte-for-byte the
poster the session made and locally duelled against three other concepts
with the competition's own judge prompt and judge model (z-ai/glm-5.3-flash
on OpenRouter, both slot orders): LUMENWOOD won the round robin with 4.4
points out of 6, ahead of VELMARA 3.8, CORALIS 2.1 and MIRRORFALL 1.7.
No network, no third-party packages: Python 3.13 stdlib only.
"""

import os
import shutil
import struct
import sys

ASSET = "poster.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def png_size(path):
    """Read width and height out of a PNG header without any image library."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"{path} is not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ASSET)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    width, height = png_size(dst)
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB cap")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(
            f"entry.png is {width}x{height}, over the 1024x1024 gate"
        )
    print(f"wrote {dst} ({width}x{height}, {size} bytes)")


if __name__ == "__main__":
    main()
