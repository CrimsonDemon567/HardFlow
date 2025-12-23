# RAX → HardFlow Mapping

This document defines how each RAX instruction is translated into HardFlow nodes.

---

## Arithmetic

| RAX Opcode | HardFlow Node | Notes |
|-----------|----------------|-------|
| ADD       | add            | Pure combinational |
| SUB       | sub            | Pure combinational |
| MUL       | mul            | May map to DSP block |
| DIV       | div            | FSM or pipelined divider |

---

## Memory

| RAX Opcode | HardFlow Node | Notes |
|-----------|----------------|-------|
| LOAD      | mem_read       | Maps to RAM port |
| STORE     | mem_write      | Maps to RAM port |

---

## Control Flow

| RAX Opcode | HardFlow Node | Notes |
|-----------|----------------|-------|
| JMP       | fsm_transition | Direct state change |
| CJMP      | mux + fsm      | Conditional branch |

---

## Slots → Pipeline

Each RAX slot boundary inserts a HardFlow register.
