# HardFlow Execution Model

Execution is driven by:

1. Dataflow within a stage  
2. Register propagation between stages  
3. FSM transitions for control flow  

There is no instruction dispatch.  
The circuit itself *is* the program.
