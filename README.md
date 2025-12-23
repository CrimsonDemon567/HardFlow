# HardFlow

HardFlow is a deterministic hardware execution model generated from RAX bytecode.  
It represents the physically fastest possible way to execute a program:  
**the program becomes the circuit.**

---

## Why HardFlow?

Traditional execution models rely on CPUs, pipelines, caches, branch predictors, and microarchitectural layers.  
Even optimized C code must pass through:

- instruction decoding  
- register allocation  
- branch prediction  
- cache hierarchies  
- microcode  
- shared pipelines  

HardFlow removes all of this.

A RAX program is translated into a hardware flow graph that directly maps to synthesizable logic.  
There is no CPU.  
There is no instruction dispatch.  
There is no runtime overhead.

Execution speed is limited only by the propagation delay of the synthesized circuit —  
**the physical lower bound of computation.**

---

## Pipeline Overview

Python -> RAX -> HardFlow -> FPGA/ASIC


1. **Python → RAX**  
   Python code is lowered into RAX, a deterministic, fixed‑width, slot‑based IR.

2. **RAX → HardFlow**  
   RAX bytecode is translated into HardFlow, a hardware‑oriented flow graph describing:
   - data paths  
   - control signals  
   - pipeline stages  
   - registers  
   - combinational logic  
   - state machines  

3. **HardFlow → Hardware**  
   HardFlow can be synthesized into Verilog/VHDL or directly into a netlist.  
   The result is a dedicated circuit implementing the program itself.

---

## Key Properties

- Deterministic execution  
- No branching penalties  
- No caches or memory hierarchies  
- No instruction decoding  
- No microarchitectural overhead  
- Fully analyzable timing  
- Hardware‑native performance  

---

## Repository Structure

- spec/       → HardFlow specification and RAX mapping
- hardflow/   → Parser, IR, and backend for HardFlow generation
- examples/   → Example RAX programs and their HardFlow output
- docs/       → Architecture and execution model documentation


---

## Status

Early development.  
The goal is to build a complete RAX → HardFlow compiler and synthesizable backend.

---

## Vision

HardFlow aims to define a new category of execution model:  
**software that becomes hardware.**

This project explores the boundary between programming languages, virtual machines, and physical computation — pushing executing speed to the limit allowed by physics.

## License
MIT
