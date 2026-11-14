"""Copy the repo's food picture to the output directory (deterministic)."""
import hashlib
import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    expected = hashlib.sha256(SRC.read_bytes()).hexdigest()
    shutil.copyfile(SRC, OUT)
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    if digest != expected:
        raise SystemExit(f"sha256 mismatch: copied {digest} != source {expected}")
    print(f"wrote {OUT} sha256={digest} verified")


if __name__ == "__main__":
    main()
