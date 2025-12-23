from .parser.rax_parser import parse_rax_source
from .ir.ir_builder import IRBuilder
from .backend.hardflow_backend import HardFlowBackend


def compile_rax_to_hardflow(source: str) -> str:
    """
    Top-level API: takes RAX assembly source and returns HardFlow representation as text.
    """
    instructions = parse_rax_source(source)
    ir_builder = IRBuilder()
    ir_program = ir_builder.build(instructions)
    backend = HardFlowBackend()
    hardflow_text = backend.emit(ir_program)
    return hardflow_text
