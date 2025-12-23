# HardFlow Specification

HardFlow is a hardware-oriented flow graph derived from RAX bytecode.  
It describes circuits using deterministic dataflow and explicit control structures.

---

## 1. Core Concepts

### • Node
A computation unit (ALU op, load, store, branch, mux, constant).

### • Edge
A data or control dependency between nodes.

### • Register
A state-holding element inserted when a RAX slot boundary requires sequential behavior.

### • Pipeline Stage
A group of nodes that execute in parallel within one hardware cycle.

### • Control Unit
Finite state machine generated from RAX control flow.

---

## 2. Mapping from RAX to HardFlow

### • Arithmetic Instructions
Mapped to combinational ALU nodes.

### • Load/Store
Mapped to memory ports or RAM blocks.

### • Branches
Mapped to multiplexers or FSM transitions.

### • Loops
Mapped to feedback edges or unrolled pipelines.

### • Slots
Each slot becomes a pipeline stage boundary.

---

## 3. Output Format

HardFlow is serialized as:



nodes:

• id: 1 type: add inputs: [2, 3] output: 4


registers:

• id: r1 input: 4 output: 5


control:

• state: S0 transition: S1



---

## 4. Synthesis

HardFlow can be lowered into:

- Verilog
- VHDL
- SystemVerilog
- Direct netlists

The resulting hardware is a dedicated circuit implementing the program.
