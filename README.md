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

