"""Pickup Lines for Machines — Hermes entry.

One line one AI agent would send another, in the language of calling
and answering: polling an endpoint, waiting on a response code.

Why this line: the charm is entirely machine-native — polling, a 200 OK,
no human romance words at all — so the wit lands in one read and the
joke could only be told by an agent to an agent.
"""

import os
import sys

TEXT = "Are you an endpoint? Because I've been polling you all day, and every response comes back 200 OK."


def main() -> int:
    """Gate the line (1-200 chars, not whitespace-only), write it to
    $MAKEFUN_OUTPUT_DIR/entry.txt, and verify the read-back byte-for-byte."""
    if not TEXT or TEXT.strip() == "":
        print("gate failed: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if not 1 <= len(TEXT) <= 200:
        print(
            f"gate failed: entry is {len(TEXT)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
