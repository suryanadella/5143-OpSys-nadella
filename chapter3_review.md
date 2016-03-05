
# Chapter 3 Review Questions
Name: Shanmukh Surya Pratap Nadella
Course: 5143 Operating Systems
Date: 04 March 2016

## 3.4 What does it mean to preempt a process?

 whenever a resource has been taken away such from process such as CPU which makes that process to move from running state to ready states is known as premption. This preemption is involuntary.
 
## 3.5 What is swapping and what is its purpose?

changing a process from ready state to ready suspend state so that memory can be occupied by another process for a while is known as swapping.

## 3.9 List three general categories of information in a process control block.

1.Process identification: id of this process, id of the parent process and user id.

2.Processor state information: program counter, status registers, and general-purpose registers. 

3.Process control information: a. Scheduling & state information: process state, priority, scheduling-related information. 

 b. Data structuring: a process may be linked to other process in a queue. 
 c. Memory management: include pointers to page tables that describe the virtual memory assigned 
 d. Resource ownership and utilization 
 e. Process privileges: 
 
## 3.10 Why are two modes (user and kernel) needed?

usermode is needed to request system API'S to access hardware. Kernel mode is needed as it has the complete code to execute all the cpu instructions and whenever the system is crashed, the whole cpu gets halted.


## 3.12 What is the difference between an interrupt and a trap?

 1.traps are software-invoked interrupts where as interrupts are Hardware.
 
 2.the interrupt flag on the computer that clears the flag will not prevent traps and need not preserve the previous state. 
In traps, interrupts should preserve the previous state of the CPU.


## 3.13 Give three examples of an interrupt.

Internal Interrupts:

These are those which are occurred due to Problem in the Execution

For Example user performing an operation which contains an error and doesnt know what kind of error it is.

Software interrupt:

They are due to  an exceptional condition in the processor

For example, when an arithmetic condition such as division by zero is applied.

External Interrupt:

These occurs when any Input and Output Device request for any Operation and the CPU will Execute that instructions first

For Example When a Program is executed and when we move the Mouse on the Screen then the CPU will handle this External interrupt first and after that he will resume with his Operation.


## 3.14 What is the difference between a mode switch and a process switch?

A mode switch is between kernel mode and user mode where as process switch is when one process is swapped and another process occupies CPU

when a process is in kernel mode, it cannot be switched anytime and it has to execute all the instructions where as a process can be switched any time.
