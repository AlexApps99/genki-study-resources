#!/usr/bin/env python3
# Generates icons of different sizes for the site
# TODO change usages to correct sizes

import subprocess
from typing import Optional


def convert(src: str, size: Optional[tuple[int, int]], dest: str, background: Optional[str] = None):
    args = ["convert", src]

    if background is not None:
        args.extend(["-background", background, "-alpha", "remove", "-alpha", "off"])

    if size is not None:
        args.extend(["-resize", f"{size[0]}x{size[1]}"])

    args.append(dest)

    subprocess.check_call(args)


if __name__ == "__main__":
    convert("genki.png", None, f"genki-thumb.png", "#f60")
    for s in [120, 192, 200]:
        convert("genki.png", (s, s), f"genki-{s}.png")
        convert("genki.png", (s, s), f"genki-thumb-{s}.png", "#f60")
