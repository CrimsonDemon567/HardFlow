from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class IRValue:
    name: str


@dataclass
class IRNode:
    id: int
    op: str
    inputs: List[IRValue] = field(default_factory=list)
    output: Optional[IRValue] = None
    attrs: Dict[str, str] = field(default_factory=dict)


@dataclass
class IRProgram:
    nodes: List[IRNode] = field(default_factory=list)
