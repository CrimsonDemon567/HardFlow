from dataclasses import dataclass
from typing import List


@dataclass
class RAXInstruction:
    opcode: str
    args: List[str]
    line: int


def _strip_comment(line: str) -> str:
    pos = line.find("#")
    if pos == -1:
        return line
    return line[:pos]


def parse_rax_source(source: str) -> List[RAXInstruction]:
    """
    Very simple RAX assembly parser.

    Example:
        LOAD r1, 5
        LOAD r2, 7
        ADD r3, r1, r2
        STORE r3, result
    """
    instructions: List[RAXInstruction] = []
    for idx, raw_line in enumerate(source.splitlines(), start=1):
        line = _strip_comment(raw_line).strip()
        if not line:
            continue

        if " " in line:
            opcode, rest = line.split(" ", 1)
            raw_args = [a.strip() for a in rest.split(",") if a.strip()]
        else:
            opcode = line
            raw_args = []

        instructions.append(
            RAXInstruction(
                opcode=opcode.upper(),
                args=raw_args,
                line=idx,
            )
        )

    return instructions
