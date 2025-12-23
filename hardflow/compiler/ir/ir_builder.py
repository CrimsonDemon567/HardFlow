from typing import List, Dict
from .ir_nodes import IRNode, IRProgram, IRValue
from ..parser.rax_parser import RAXInstruction


class IRBuilder:
    """
    Minimal IR builder:
    - LOAD rX, const → const node
    - ADD rD, rA, rB → add node
    - STORE rS, name → store node
    """

    def __init__(self) -> None:
        self._next_id = 1
        self._values: Dict[str, IRValue] = {}
        self._program = IRProgram()

    def _new_id(self) -> int:
        nid = self._next_id
        self._next_id += 1
        return nid

    def _get_value(self, name: str) -> IRValue:
        if name not in self._values:
            self._values[name] = IRValue(name=name)
        return self._values[name]

    def build(self, instructions: List[RAXInstruction]) -> IRProgram:
        for instr in instructions:
            opcode = instr.opcode
            args = instr.args

            if opcode == "LOAD" and len(args) == 2:
                dest_reg, literal = args
                out_val = self._get_value(dest_reg)
                node = IRNode(
                    id=self._new_id(),
                    op="const",
                    inputs=[],
                    output=out_val,
                    attrs={"value": literal},
                )
                self._program.nodes.append(node)

            elif opcode == "ADD" and len(args) == 3:
                dest_reg, src_a, src_b = args
                in_a = self._get_value(src_a)
                in_b = self._get_value(src_b)
                out_val = self._get_value(dest_reg)
                node = IRNode(
                    id=self._new_id(),
                    op="add",
                    inputs=[in_a, in_b],
                    output=out_val,
                )
                self._program.nodes.append(node)

            elif opcode == "STORE" and len(args) == 2:
                src_reg, target_name = args
                src_val = self._get_value(src_reg)
                node = IRNode(
                    id=self._new_id(),
                    op="store",
                    inputs=[src_val],
                    output=None,
                    attrs={"target": target_name},
                )
                self._program.nodes.append(node)

            else:
                raise ValueError(
                    f"Unsupported instruction at line {instr.line}: "
                    f"{instr.opcode} {', '.join(instr.args)}"
                )

        return self._program
