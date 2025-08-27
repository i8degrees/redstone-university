# **Redstone University: The Curriculum**

**Project Vision:** To demystify computer science by guiding learners to build a tangible, 4-bit computer in Minecraft. The course prioritizes understanding foundational theory (Boolean algebra, digital logic) before applying it in satisfying, practical builds, with a strong emphasis on modular, expandable design.

---

## Part I: The Foundations - Speaking to the Machine

### Module 0 (Optional): The Redstone Toolkit – Orientation Day
-   **Narrative Beat:** Before we can speak to our computer, we need to learn how to hold the pen. This module equips you with the minimum viable skills to confidently follow the course.
-   **Learning Goals:** Identify core Redstone components, grasp the fundamental rules of power (signal strength, strong vs. weak), and build a simple test circuit.
-   **Lessons:**
    -   Lesson 0.1: The Engineer's Toolkit
    -   Lesson 0.2: How Redstone Thinks: The Rules of Power
    -   Lesson 0.3: Lab: The Fundamental Circuit
-   **Minecraft Artifact:** A working on/off lamp circuit using a lever, wire, and output lamp.

### Module 1: Speaking in 1s and 0s - The Input Interface
-   **Narrative Beat:** Before we can build a computer, we need a way to talk to it. Our language will be binary, and our input interface will be a set of simple levers.
-   **Learning Goals:** Understand binary as a system of on/off switches, build a physical interface to input binary numbers, and strengthen binary intuition through practice.
-   **Lessons:**
    -   Lesson 1.1: The Theory – Why Computers Use Binary
    -   Lesson 1.2: The Lab – Building and Using Our 4-Bit Input Interface
    -   Lesson 1.3: Drills & Games – Strengthening Your Binary Intuition
    -   Lesson 1.4: Module 1 Checkpoint
-   **Minecraft Artifact:** A working 4-bit input interface for binary numbers.

### Module 2: The Language of Logic - A Deep Dive into Boolean Algebra
-   **Narrative Beat:** We've built our keyboard, but to make the computer *think*, we need to learn its grammar. This isn't a Minecraft lesson; this is the fundamental language of all digital electronics. Welcome to Boolean Algebra.
-   **Learning Goals:** Move beyond physical blocks to understand the formal, abstract language that governs all digital circuits and learn how to design and simplify them on paper.
-   **Lessons:**
    -   Lesson 2.1: The Rules of Thought
    -   Lesson 2.2: The Core Operators (The Verbs of Logic)
    -   Lesson 2.3: The Laws of Logic & The Power of Simplification
    -   Lesson 2.4: The Special Operator – XOR
    -   Lesson 2.5: Software Superpowers – The XOR Trick for Programmers
    -   Lesson 2.6: The Negated Gates – NAND, NOR, and XNOR
    -   Lesson 2.7: Module Summary
    -   Lesson 2.8: Module 2 Checkpoint
-   **Minecraft Artifacts:** A set of working Redstone logic gates (NOT, AND, OR, XOR, NAND, NOR, XNOR).

### Interlude I (Optional): The Art of Compact Design
-   **Narrative Beat:** We've built our gates for clarity. Now, let's take a quick engineering deep dive to learn the trade-offs and techniques for building with efficiency and speed.
-   **Learning Goals:** Understand the engineering trade-offs between size, speed, and readability. Deconstruct common compact gate designs to prepare for larger builds.

### Module 3: Translators & Our First Display
-   **Narrative Beat:** We've learned the computer's language. Now let's build a translator so it can talk back to us, breaking the problem into two smart stages.
-   **Learning Goals:** Understand decoders and encoders, apply Boolean logic to a large-scale project, and see the connection to real-world hardware like ROM.
-   **Lessons:**
    -   Lesson 3.1: The Output Problem & Building the Display
    -   Lesson 3.2: The Plan – A Two-Stage Approach
    -   Lesson 3.3: Building the Decoder (Stage 1)
    -   Lesson 3.4: Building the Encoder (Stage 2)
    -   Lesson 3.5: The Grand Payoff: The Final Connection
    -   Lesson 3.6: Module 3 Checkpoint
-   **Minecraft Artifact:** A working two-stage translator: a 4-to-10 BCD decoder and a 7-segment display encoder, forming a complete digital display system.

### Interlude II (Optional): The Power of Abstraction in Practice
-   **Narrative Beat:** We've just built our first multi-part system. Now let's learn how real engineers manage that complexity by packaging our circuits into "black boxes."
-   **Learning Goals:** Understand and apply the principle of abstraction by creating and using subcircuits in a digital logic simulator, making complex designs clean and reusable.

---

## Part II: Engineering a Robust Arithmetic Unit

### Module 4: The Adder & The "Decoder" B*   **Narrative Beat:** Time for real math! We'll build an adder, but immediately discover that our amazing display has a critical limitation.
-   **Learning Goals:** Build a circuit for binary addition and understand the concept of an "out of range" error through practical failure.
-   **Minecraft Artifact:** A 4-Bit Ripple-Carry Adder.
-   **The "Aha!" Moment:** Adding `8+4` results in a blank display, proving the BCD decoder can't handle numbers above 9.

### Module 5: The Programmer's Solution - The Hexadecimal Upgrade
-   **Narrative Beat:** Our display failed! Instead of a messy fix, let's upgrade our system to speak Hexadecimal. Because of our modular design, this will be an upgrade, not a rebuild.
-   **Learning Goals:** Learn hexadecimal and appreciate modular design by easily expanding an existing circuit.
-   **Minecraft Artifacts:**
    1.  **Upgraded Decoder:** A full **4-to-16 Binary Decoder**.
    2.  **Upgraded Encoder:** Logic for drawing the letters A-F.
-   **The Payoff:** The `8+4` calculation now correctly displays a `C`.

### Module 6: The "Overflow" Bug & The Carry Bit
-   **Narrative Beat:** We'll push our Hex display to its limit and discover a new bug called "overflow," then learn to harness the powerful carry bit to solve it.
-   **Learning Goals:** Discover and understand arithmetic overflow and engineer a solution using the adder's carry-out bit.
-   **The "Aha!" Moment:** Adding `C + 5` (`12 + 5 = 17`) results in a `1`, but the Carry-Out lamp is lit, holding the missing `16`.
-   **The Build:** Construct a simple "Tens Digit" driver that displays a `1` when the carry-out is active.

### Module 7: The Subtractor & Negative Numbers (Two's Complement)
-   **Narrative Beat:** Our computer can add, but what about subtraction? Thanks to a brilliant mathematical trick, we can teach our existing adder how to subtract.
-   **Learning Goals:** Understand negative number representation (Two's Complement) and build a subtraction circuit using the existing adder.
-   **The Build:** A configurable inverter using XOR gates for one of the adder's inputs, allowing it to perform `A + (!B) + 1`.

---

## Part III: The Processor Core

### Module 8: The Multiplexer - The Digital Switch
-   **Narrative Beat:** Before building our final processor, we must build its 'steering wheel'—the Multiplexer, a digital selector switch.
-   **Learning Goals:** Understand the theory and application of a Multiplexer (MUX).
-   **Minecraft Artifact:** A fully functional, scalable 4-bit 2-to-1 MUX.

### Module 9: The ALU - The Grand Assembly
-   **Narrative Beat:** We will forge all our arithmetic and logic circuits into one component: the capstone project of our processor.
-   **Learning Goals:** Combine all functions into a single, controllable Arithmetic Logic Unit (ALU).
-   **The Build:** Construct parallel lanes for **ADD, SUB, AND, OR, XOR, and XNOR**, and use a large Multiplexer to select the final output.

---

## Part IV: Creating an Automated Computer

### Module 10: Memory - The Processor's Scratchpad
-   **Narrative Beat:** Our ALU is a powerful but forgetful brain. We need to give it a 'scratchpad' to store its thoughts by building a memory register.
-   **Learning Goals:** Understand how data is stored electronically using latches (the foundation of RAM).
-   **Minecraft Artifact:** A 4-bit memory register built from Gated D-Latches.

### Module 11: The Grand Assembly - Automation
-   **Narrative Beat:** It's time to take our hands off the levers. We will build a clock and a program counter, turning our calculator into a true, self-running computer.
-   **Learning Goals:** Understand how a clock signal and program counter execute a sequence of instructions automatically.
-   **Minecraft Artifacts:** A controllable Redstone Clock, a Program Counter, and a simple hard-coded program (ROM).

---

## Part V: Post-Graduate Studies (Bonus Content)

### Module 12: The "Real World" Display - The Double Dabble Algorithm
-   **Narrative Beat:** Remember the problem from Module 4? We found an elegant programmer's solution with Hex. Now, let's build the complex engineer's solution that digital clocks use.
-   **Learning Goals:** Solve the "numbers over 9" problem by building a proper Binary-to-BCD conversion circuit for multi-digit display.
-   **The Build:** A Double Dabble circuit that takes one 4-bit binary input and produces *two* 4-bit BCD outputs (tens and ones).
-   **The Final Payoff:** Inputting `1101` (13) makes one display show `1` and the other show `3`.
