## Module 12: The Control Unit & Programmable Logic

### Module 12 Summary

-   **Narrative Beat:** The moment of truth. We will build the computer's conductor, the Control Unit, and connect everything. We will define a language for our machine, and then give it the power to read our status flags and **jump to different parts of a program**, enabling true `if/else` logic and loops.
-   **Learning Goals:**
    -   Understand the role of a clock, program counter, and instruction register.
    -   Define a simple instruction set with opcodes for arithmetic, memory, and control flow.
    -   Understand the fetch-decode-execute cycle as the fundamental process of a computer.
    -   Build a Control Unit that decodes and executes instructions, including a conditional jump.
-   **Lesson Overview:**
    -   Lesson 12.1: The Heartbeat – Building the System Clock
    -   Lesson 12.2: The Conductor – Building the Control Unit
    -   Lesson 12.3: The Language of the Machine – The RU-v1 Instruction Set
    -   Lesson 12.4: The Grand Assembly & The First Program
-   **Minecraft Artifact:** The final, complete, working 4-bit computer that can run a program with loops from RAM.
-   **The Ultimate Payoff:** Writing and watching a program that performs a countdown loop, demonstrating that the computer is making decisions based on the status flags.

---

### Module 12 Introduction

This is the moment of triumph. We have built all the organs of our computer: a processor (ALU) to think, a memory (RAM) to remember, and an interface to communicate. But it's not alive yet. It waits for us to flip every switch.

In this final core module, we will give our machine two last things: a **heartbeat** (the clock) to provide a steady rhythm, and a **conductor** (the Control Unit) to direct the orchestra of components. We will define a language for our machine to understand and, for the first time, give it the power to make its own decisions.

It's time to take our hands off the levers and watch our creation run a program on its own.

---

### Lesson 12.1: The Heartbeat – Building the System Clock

> **Key Takeaway:** A computer's clock is an oscillating circuit that produces a steady pulse, synchronizing the operations of all the different components.

A real computer works continuously, executing one instruction after the next in a perfectly synchronized dance. What drives this rhythm? A **clock**. A computer clock isn't for telling time; it's a circuit that produces a steady, oscillating signal: `` `1` ``, `` `0` ``, `` `1` ``, `` `0` ``...

Each time the clock signal pulses, every component knows it's time to perform its next step. The speed of this clock determines the speed of the processor, measured in Hertz (Hz).

#### Lab & Experiment: Building a Controllable Clock

1.  **The Concept:** The simplest clock in Minecraft is a loop of Redstone Repeaters.
2.  **The Build:** Create a small loop of repeaters, all facing the same direction. The more repeaters or the greater their delay, the slower the clock.
3.  **Adding Control:** We need to be able to start and stop our computer. We'll add an AND gate to our clock's output. One input is the oscillating signal. The other is a master lever labeled **`RUN/HALT`**. The output of the AND gate is our official **System Clock Bus**.

<div align="center"><img src="./images/controllable-clock-minecraft.png" alt="Controllable Clock Minecraft Build" width="512px"/><br/><em>Figure: A simple, controllable Redstone clock. The repeater loop on the left creates a pulse, which is controlled by the RUN/HALT lever via the AND gate on the right.</em></div><br/>

---

### Lesson 12.2: The Conductor – Building the Control Unit

> **Key Takeaway:** The Control Unit is the brain of the brain. It uses a Program Counter to fetch instructions from memory and a decoder to translate those instructions into control signals for the rest of the computer.

The Control Unit has three key parts:

1.  **The Program Counter (PC):** A special register that holds the memory address of the *next instruction* to be executed. On every clock tick, it usually just increments by one.
2.  **The Instruction Register (IR):** A register that holds the *current instruction* after it's been fetched from RAM. This is important because it holds the instruction steady while the PC is already getting ready for the next one.
3.  **The Instruction Decoder:** A circuit (like a ROM) that reads the instruction from the IR and outputs all the necessary control signals (e.g., "tell the ALU to add," "tell the RAM to write").

This system works in a perpetual loop, the **Fetch-Decode-Execute Cycle**:
1.  **Fetch:** Get the instruction from RAM at the address specified by the Program Counter. Place it in the Instruction Register.
2.  **Decode:** The Instruction Decoder reads the instruction and activates the correct control lines.
3.  **Execute:** The clock pulses, and the activated components (ALU, RAM, etc.) perform the operation. The Program Counter increments. The cycle repeats.

---

### Lesson 12.3: The Language of the Machine – The RU-v1 Instruction Set

> **Key Takeaway:** An instruction set is a dictionary that defines all the commands a processor can execute, where each command is represented by a unique binary number called an opcode.

Before we can build our instruction decoder, we must define the language it will understand. We will create our own simple but powerful 8-bit instruction set. Each instruction consists of a 4-bit opcode and a 4-bit piece of data (which can be a literal number or a memory address).

**The "Redstone University v1" (RU-v1) Instruction Set**

| Opcode (Hex) | Mnemonic | Description |
| :--- | :--- | :--- |
| `$0$` | `NOP` | No Operation. Do nothing. |
| `$1$` | `LDA [addr]` | **L**oa**d** from RAM address `[addr]` into Register **A**. |
| `$2$` | `LDB [addr]` | **L**oa**d** from RAM address `[addr]` into Register **B**. |
| `$3$` | `STA [addr]` | **St**ore the value from the ALU result into RAM address `[addr]`. |
| `$4$` | `ADD` | Add the values in Register A and Register B. Store result in ALU. |
| `$5$` | `SUB` | Subtract Register B from Register A. Store result in ALU. |
| `$6$` | `JMP [addr]` | **J**u**mp** (unconditionally) to the instruction at `[addr]`. |
| `$7$` | `JIZ [addr]` | **J**ump **i**f **Z**ero. If the Zero Flag is `1`, jump to `[addr]`. |
| `$8$` | `LDI A, [data]`| **L**oa**d I**mmediate. Load the literal value `[data]` into Register **A**. |
| `$F$` | `HLT` | **H**a**lt**. Stop the clock. |

*(Note: We will need to add two simple 4-bit registers, A and B, to hold the inputs for the ALU. These are just like the register we built in Module 10.)*

---

### Lesson 12.4: The Grand Assembly & The First Program

> **Key Takeaway:** By connecting the Clock, Program Counter, RAM, and ALU through the Control Unit, we create a machine that can execute a sequence of stored instructions, a true von Neumann architecture.

This is the final, exhilarating step. We are connecting everything together.

#### Lab & Experiment

1.  **The Build:** This is an integration challenge.
    -   Build the **Program Counter** (a register that can increment).
    -   Build the **Instruction Register**.
    -   Build the **Instruction Decoder** (a large ROM that takes the 4-bit opcode as input).
    -   Carefully connect all the components: the PC's output goes to the RAM's address input. The RAM's output goes to the Instruction Register. The IR's opcode part goes to the decoder. The decoder's control lines go to *everything* (the ALU's opcode, the registers' write enable lines, etc.).
    -   Build the logic for the `JIZ` instruction: an AND gate that combines the "Jump" signal from the decoder with the **Zero Flag** from the ALU.
2.  **The Program:** Let's write a program to count down from 3 to 0. We'll store the number `3` in RAM address `15`.
    -   `Addr 0: LDI A, 1` (Load the number 1 into A)
    -   `Addr 2: LDB [15]` (Load the current count from address 15 into B)
    -   `Addr 4: SUB` (Calculate B-A)
    -   `Addr 6: STA [15]` (Store the new value back to address 15)
    -   `Addr 8: JIZ [12]` (If the result was zero, jump to the HLT instruction)
    -   `Addr 10: JMP [2]` (Jump back to the start of the loop)
    -   `Addr 12: HLT` (Halt the computer)
3.  **The First Boot-Up:**
    -   Manually store `0011` (`3`) at RAM address `15`.
    -   Program the instructions above into the first few addresses of your RAM.
    -   Reset the Program Counter to `0`.
    -   Flip the **`RUN/HALT`** switch to RUN.
4.  **The Payoff:** Watch the display connected to RAM address `15`. You will see it cycle: `3`... `2`... `1`... `0`. The computer will then halt. You didn't touch a thing. It read a program from memory and made a decision based on the Zero Flag. You have built a true computer.

<div align="center"><img src="./images/final-computer-minecraft.png" alt="Final Computer Minecraft Build" width="512px"/><br/><em>Figure: The final, assembled 4-bit computer. All components, the ALU, RAM, and Control Unit, are connected and ready to execute a program.</em></div><br/>

---

### Module 12 Conclusion

This is the moment of triumph. You have taken a collection of disparate parts and breathed life into them with a clock, a memory, and a control unit. You have defined a language and written a program that your machine understood and executed, complete with a logical decision. This system, where instructions and data are stored in the same memory, is a **von Neumann architecture**, the design basis for nearly every computer you have ever used.

You have completed the core curriculum of Redstone University. You have built a computer.

In our final "Post-Graduate" module, we'll return to a problem we left behind to see how we could make our machine's output even more human-friendly, a perfect encore to this grand project.

---

### Module 12 Checkpoint

#### Practice Problem 12.5.1: Knowledge Check
1. What are the three steps of the Fetch-Decode-Execute cycle?
2. What is the difference between the Program Counter and the Instruction Register?
3. What is the key hardware component that makes a conditional jump (like `JIZ`) possible?

<details>
<summary><strong>Show Solution</strong></summary>
1. **Fetch:** Get the instruction from memory. **Decode:** Determine what the instruction means. **Execute:** Activate the correct components to perform the instruction.
2. The **Program Counter (PC)** holds the address of the *next* instruction to be fetched. The **Instruction Register (IR)** holds the *current* instruction that is being decoded and executed.
3. The **Status Flags** (specifically, the Zero Flag in this case). The Control Unit's decision to jump is based on the state of this flag.
</details>

#### Practice Problem 12.5.2: The Programmer
Write the RU-v1 assembly code for a program that calculates `$5 - 3$` and stores the result in RAM address `10`.

<details>
<summary><strong>Show Solution</strong></summary>
```assembly
LDI A, 5     // Load the number 5 into Register A
LDI B, 3     // Load the number 3 into Register B
SUB          // Subtract B from A
STA     // Store the result in RAM address 10 (0xA)
HLT          // Halt
```
</details>

#### Key Terms
-   **Clock**: A circuit that generates a steady pulse to synchronize the operations of a computer.
-   **Control Unit**: The part of the CPU that directs the operation of the processor. It fetches, decodes, and executes instructions by sending control signals to other components.
-   **Fetch-Decode-Execute Cycle**: The fundamental process of a computer, where it retrieves an instruction from memory, determines its operation, and performs that operation.
-   **Instruction Register (IR)**: A register in the Control Unit that holds the instruction that is currently being executed or decoded.
-   **Instruction Set Architecture (ISA)**: The part of the computer architecture related to programming, including the native data types, instructions, registers, and memory model.
-   **Program Counter (PC)**: A register in the Control Unit that holds the memory address of the next instruction to be fetched.
-   **von Neumann Architecture**: A computer architecture based on the concept of a stored-program computer where instruction data and program data are stored in the same memory.```
