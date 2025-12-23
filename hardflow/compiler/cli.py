import sys
from pathlib import Path

from . import compile_rax_to_hardflow


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: hardflowc <input.rax> <output.hf>")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    if not in_path.exists():
        print(f"Input file not found: {in_path}")
        sys.exit(1)

    source = in_path.read_text(encoding="utf-8")
    hf = compile_rax_to_hardflow(source)
    out_path.write_text(hf, encoding="utf-8")
    print(f"HardFlow written to {out_path}")
