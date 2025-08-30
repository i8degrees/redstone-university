## Module 11: Addressable Storage – Building RAM

### Module 11 Summary

-   **Narrative Beat:** A single scratchpad isn't enough for a real program. We will now scale up the register we just built into a "notebook" with 16 numbered pages, building true Random Access Memory (RAM) by using a decoder as an address selector.
-   **Learning Goals:**
    -   Understand the concept of memory addressing and the role of an address bus.
    -   Use a decoder to select one of many memory registers.
    -   Combine multiple registers into a single, addressable RAM module.
    -   Emphasize debugging strategies for large, repetitive circuits.
-   **Lesson Overview:**
    -   Lesson 11.1: The Theory – From a Register to RAM
    -   Lesson 11.2: The Lab – The Grand Assembly of Memory
-   **Minecraft Artifact:** A functional, addressable 16x4-bit RAM module.

---

### Module 11 Introduction

In the last module, you gave our computer its first taste of memory: a single 4-bit register. This "scratchpad" is essential, but it's not enough. To run a real program, a computer needs to store many different values at once: variables, constants, and the program's instructions themselves.

A single sticky note isn't enough; we need a whole notebook.

In this module, we will perform one of the most satisfying acts of engineering: scaling up. We will take the 4-bit register you perfected in Module 10 and duplicate it 16 times. Then, using a decoder as a "page selector," we will wire it all together to create a **16x4-bit Random Access Memory (RAM)** module. This is the final major hardware component our computer needs before we can bring it to life.

---

### Lesson 11.1: The Theory – From a Register to RAM

> **Key Takeaway:** RAM is simply a large collection of registers combined with a decoder that allows us to select a specific register to read from or write to using a binary "address."

#### The Core Problem: Selection
Imagine a library with 16 books, but no labels on the shelves. If you want to find a specific book, you have no way to do it. We have 16 registers, but we need a system to select just *one* of them to interact with at a time. This is where **memory addressing** comes in.

-   **Address:** Each of our 16 registers is assigned a unique "address," a 4-bit number from `` `0000` `` (`0`) to `` `1111` `` (`15`).
-   **Address Bus:** We will create a new 4-bit bus, the **Address Bus**, whose only job is to carry the address of the register we want to access.

How do we turn a 4-bit address into a signal that activates only one of 16 registers? We've already built the perfect tool for this: the **4-to-16 decoder** from Module 4! This is a fantastic example of modular reuse. We will feed the 4-bit Address Bus into the decoder, and it will give us 16 unique output lines, one for each register.

#### Reading vs. Writing
We also need to control when we save data. The **Write Enable** signal is the key.

The final logic for writing to a specific register (e.g., Register #6) is:
"We can write to Register #6 if the `Select Line #6` from the decoder is ON **AND** the master `Write Enable` signal is ON."

This means a register will only ever save new data when two conditions are met: it's the specific one being addressed, and the command to write has been given.

<div align="center"><img src="./images/ram-architecture-circuitverse.png" alt="RAM Architecture Diagram" width="512px"/><br/><em>Figure: The architecture of our 16x4-bit RAM. A 4-bit address is decoded to select one of 16 registers. The shared Write Enable and Data In buses go to all registers, but only the selected one will actually store the new data.</em></div><br/>

---

### Lesson 11.2: The Lab – The Grand Assembly of Memory

> **Key Takeaway:** Building RAM is a lesson in scale and precision, requiring the careful duplication and wiring of a modular component.

This is the largest and most repetitive build in the course, but the result is one of the most impressive components of a real computer.

#### Lab & Experiment

1.  **Build the Register Array:**
    1.  Start with the 4-bit register design you perfected in Module 10.
    2.  Carefully duplicate this register 16 times, arranging them in a compact grid (e.g., a 4x4 or 8x2 layout). This is your memory array.
2.  **Build the Address Decoder:**
    1.  Build a 4-to-16 decoder, just like the one from the Hexadecimal upgrade in Module 5.
    2.  Create a 4-bit input bus for this decoder, which will be our **Address Bus**. Label the input levers `` `A0` `` through `` `A3` ``.
3.  **Wire the Select Lines:**
    1.  This is the most delicate wiring. Run each of the 16 output lines from your decoder to the "select" input of a single, unique register in your array. (You will need to add an AND gate to each register's `STORE` line to combine the `Select` signal with the master `Write Enable` signal).
4.  **Wire the Shared Buses:**
    1.  Create another 4-bit input bus, the **Data Bus**. Wire these four lines in parallel to the data inputs of *all 16* registers.
    2.  Create a single **Write Enable** lever. Wire its signal in parallel to the other input of the select AND gate on *all 16* registers.
5.  **Wire the Output:**
    1.  This can be tricky. You need to combine the 4-bit outputs of all 16 registers onto a single 4-bit **Memory Output Bus**. A large array of OR gates (or simple dust merging with diodes) is required, one for each of the 4 bits.

<div align="center"><img src="./images/ram-minecraft.png" alt="16x4 RAM Minecraft Build" width="512px"/><br/><em>Figure: A complete 16x4-bit RAM module in Minecraft. The address decoder is on the left, sending select signals to the large array of memory registers on the right. The shared data buses run throughout the structure.</em></div><br/>

#### The Final Test

This is the ultimate test of your memory system.
1.  **Write a value:**
    -   Set the **Address Bus** to an address, for example, `` `0110` `` (address 6).
    -   Set the **Data Bus** to a value, for example, `` `1100` `` (the number 12).
    -   Pulse the **Write Enable** lever ON, then OFF. A value has now been stored.
2.  **Verify the value:**
    -   Change the Data Bus to `` `0000` ``. The Memory Output Bus should still be showing `` `1100` ``, because the register at address 6 is still selected and outputting its stored value.
3.  **Check another address:**
    -   Change the Address Bus to a different address, for example, `` `0111` `` (address 7). The output should now change to whatever random value was in that register.
    -   Switch the Address Bus back to `` `0110` ``. The output should immediately switch back to `` `1100` ``.

You have built true, addressable Random Access Memory.

---

### Module 11 Conclusion

Take a step back and admire your work. This is a monumental achievement. You have scaled a simple 1-bit memory cell into a complex, addressable 16x4-bit RAM module. You have now built the computer's "notebook", a place where it can store and retrieve data, the final major hardware component required for automation.

You now have a processor (the ALU) and a memory (the RAM). In our final core module, we will build the last piece of the puzzle: the Control Unit. We will give the machine a clock to act as its heartbeat and teach it how to read and execute a sequence of instructions from its new memory, transforming it from a collection of powerful components into a true, self-running computer.

---

### Module 11 Checkpoint

#### Practice Problem 11.3.1: Knowledge Check
1. In the term "16x4-bit RAM," what does the "16" represent, and what does the "4" represent?
2. What is the role of the decoder in a RAM module?
3. Why is the `Write Enable` signal necessary? What problem does it solve?

<details>
<summary><strong>Show Solution</strong></summary>
1. The "16" represents the number of unique memory locations or addresses. The "4" represents the number of bits that can be stored at each of those locations.
2. The decoder takes the binary address from the Address Bus and activates a single "select line" to choose which of the many registers will be active for a read or write operation.
3. The `Write Enable` signal is necessary to differentiate between reading from and writing to a memory address. When it's OFF, the selected register outputs its data but doesn't change it. When it's ON, the selected register overwrites its current data with the data from the Data In bus.
</details>

#### Practice Problem 11.3.2: The Expansion
You want to upgrade your computer's memory from 16x4-bit to **256x4-bit**.
1. How many registers would you need to build?
2. How many bits would your Address Bus need to be to select one of 256 unique addresses?
3. What kind of decoder would you need?

<details>
<summary><strong>Show Solution</strong></summary>
1. You would need **256** individual 4-bit registers.
2. To represent 256 unique values ($2^8$), your Address Bus would need to be **8 bits** wide.
3. You would need an **8-to-256 decoder**.
</details>

#### Key Terms
-   **Address**: A unique binary number that specifies a particular location in memory.
-   **Address Bus**: A set of parallel wires that carries the address of the memory location to be read from or written to.
-   **Data Bus**: A set of parallel wires used to transfer data to and from the CPU and memory.
-   **RAM (Random Access Memory)**: A form of computer memory that can be read and changed in any order. It is used to store working data and machine code.
-   **Write Enable**: A control signal that tells a memory module whether to store the data currently on the data bus into the selected address.
