from typing import List
import yaml

from ..ir.ir_nodes import IRProgram, IRNode


class HardFlowBackend:
    """
    HardFlow emitter:
    - Emits YAML for 'nodes', 'registers', and 'control'.
    """

    def emit(self, program: IRProgram) -> str:
        nodes_section: List[dict] = []

        for node in program.nodes:
            entry: dict = {
                "id": node.id,
                "type": node.op,
            }
            if node.inputs:
                entry["inputs"] = [v.name for v in node.inputs]
            if node.output is not None:
                entry["output"] = node.output.name
            if node.attrs:
                entry.update(node.attrs)
            nodes_section.append(entry)

        doc = {
            "nodes": nodes_section,
            "registers": [],
            "control": [
                {"state": "S0", "transition": "END"},
            ],
        }

        return yaml.dump(doc, sort_keys=False)
