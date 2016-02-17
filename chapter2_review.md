#Chapter 2 Review Questions
Name: Shanmukh Surya Pratap Nadella

Course: 5143 Operating Systems

Date: 17 Feb 2016

## 1. What are the three objectives of OS Design ?
  
 Operating System takes complete control of Hardware and create a platform which is easy for user to write different applications.Convenience: An OS makes a computer more user-friendly.
Efficiency: An OS allows the computer system resources to be used in an efficient manner.
Ability to evolve: An OS should be constructed in such a way as to permit the effective development, testing, and introduction of new system functions without interfering with service.

## 2. What is the kernel of an OS ?

The kernel is a portion of the operating system that includes the most heavily used portions of software. Generally, the kernel is maintained permanently in main memory. The kernel runs in a privileged mode and responds to calls from processes and interrupts from devices.

## 3. What is multiprogramming?

Ability of Operating System to hold multiple ready to run programs in the main memory so that if the running program requires I/O, Then CPU can be switched to another ready program.

## 4. What is a process ?

process is a program under execution, unit of execution, instance of a program

## 5. How is the execution context of a process used by the OS?

Also known as the process state, the execution context is the internal data the Operating system uses to control or supervise a process

## 6. List and briefly explain five storage management responsibilities of a typical OS ?

Process isolation:one process memory shouldn't interfere with another process memory. 

Automatic allocation and management: Programs should be dynamically
allocated across the memory hierarchy as required.  Dynamic memory allocation relieves programmer frm assigning memory to the program.

Support of modular programming: Programmers should be able to define program
modules, and to create, destroy, and alter the size of modules dynamically.

Protection and access control: Sharing of memory, at any level of the memory
hierarchy, creates the potential for one program to address the memory space
of another. The OS must allow portions of memory to be accessible in various ways by
various users. Sharing sometimes threatens the integrity of program so protection plays a key role.

Long-term storage: Many application programs require means for storing
information for extended periods of time, after the computer has been
powered down.

## 7. Explain the distinction between a real address and a virtual address ?
real address refers to physical address that refer to hardware addresses of physical memory.
Virtual addresses refer to the virtual store viewed by the process.

## 8. Describe the round-robin scheduling technique?

The round-robin technique uses a circular queue.In this strategy, order priority and time slicing are considered
Important criteria: Arriving time + time quantum.
If time quantum is very small, efficiency is zero.
If time Quantum is low, context switching occurs, improves response time.
If Time Quantum is high, First Come First Serve is followed and very poor response time.


## 9. Explain the difference between a monolithic kernel and a microkernel.
A monolithic kernel is implemented as a single process, with
all elements sharing the same address space. A microkernel architecture assigns
only a few essential functions to the kernel, including address spaces, interprocess
communication (IPC), and basic scheduling

## 10. What is multithreading?
Multithreading is a technique in which a process, executing an application, is divided into threads that can run concurrently.

## 11. List the key design issues for an SMP operating system ?

Concurrent Process / Threads

Scheduling

Synchronization

Memory Management

Reliability / Fault Tolerance
