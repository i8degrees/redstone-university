# **Redstone University: The Curriculum**

**Project Vision:** To demystify computer science by guiding learners to build a tangible, 4-bit computer in Minecraft. The course prioritizes understanding foundational theory (Boolean algebra, digital logic) before applying it in satisfying, practical builds, with a strong emphasis on modular, expandable design.

---

## Part I: The Foundations - Speaking to the Machine

### Module 0 (Optional): The Redstone Toolkit – Orientation Day
-   **Narrative Beat:** Before we can build our computer, we need to know our tools. This module equips you with the minimum viable skills to confidently follow the course.
-   **Learning Goals:** Identify core Redstone components, grasp the fundamental rules of power, and build a simple test circuit.
-   **Lessons:**
    -   Lesson 0.1: The Engineer's Toolkit
    -   Lesson 0.2: How Redstone Thinks: The Rules of Power
    -   Lesson 0.3: Lab: The Fundamental Circuit
-   **Minecraft Artifact:** A working on/off lamp circuit.

### Module 1: Speaking in 1s and 0s - The Input Interface
-   **Narrative Beat:** To talk to our computer, we must first learn its native language: binary. We'll build a physical panel to send it numbers.
-   **Learning Goals:** Understand binary as a system of on/off switches, build a physical interface to input binary numbers, and strengthen binary intuition through practice.
-   **Lessons:**
    -   Lesson 1.1: The Theory – Why Computers Use Binary
    -   Lesson 1.2: The Lab – Building Our 4-Bit Input Interface
    -   Lesson 1.3: Drills & Games – Strengthening Your Binary Intuition
-   **Minecraft Artifact:** A working 4-bit input interface for binary numbers.

### Module 2: The Grammar of Circuits – Foundational Logic Gates
-   **Narrative Beat:** We have a language, but no words. We'll learn the three fundamental "verbs" of logic—NOT, OR, and AND—that allow us to form our first logical thoughts.
-   **Learning Goals:** Master the concept of a truth table, understand Minecraft's primitive gates, and build a composite gate (AND) from scratch.
-   **Lessons:**
    -   Lesson 2.1: The Rules of Thought
    -   Lesson 2.2: The Primitives – Building NOT and OR Gates
    -   Lesson 2.3: The First Composite Gate – Building an AND Gate
-   **Minecraft Artifact:** A working set of the three foundational logic gates: NOT, OR, and AND.

### Module 3: The Art of Logic – Simplification and Special Gates
-   **Narrative Beat:** We know the basic words; now we learn to write poetry. We'll learn how to make our circuits more efficient and expand our toolkit with powerful new gates like XOR and NAND.
-   **Learning Goals:** Apply the laws of Boolean algebra to simplify circuits, build and understand the unique properties of XOR and the universal gates, and connect hardware logic to clever software algorithms.
-   **Lessons:**
    -   Lesson 3.1: The Laws of Logic & The Power of Simplification
    -   Lesson 3.2: The Special Operator – Building an XOR Gate
    -   Lesson 3.3: Software Superpowers – The XOR Trick for Programmers
    -   Lesson 3.4: The Negated Gates – NAND, NOR, and XNOR
-   **Minecraft Artifact:** A working set of advanced logic gates (XOR, NAND, NOR, XNOR).

### Interlude I (Optional): The Art of Compact Design
-   **Narrative Beat:** We've built our gates for clarity. Now, let's take a quick engineering deep dive to learn the trade-offs and techniques for building with efficiency and speed.
-   **Learning Goals:** Understand the engineering trade-offs between size, speed, and readability. Deconstruct common compact gate designs to prepare for larger builds.

### Module 4: Translators & Our First Display
-   **Narrative Beat:** We can talk to the machine, but it can't talk back. We'll now apply our full logic toolkit to a major project: building a translator that lets us see our binary numbers as digits.
-   **Learning Goals:** Understand decoders and encoders, apply Boolean logic to a large-scale project, and see the connection to real-world hardware like Read-Only Memory (ROM).
-   **Lessons:**
    -   Lesson 4.1: The Goal: Building Our 7-Segment Display
    -   Lesson 4.2: The Master Plan: A Two-Stage Translation
    -   Lesson 4.3: The Decoder: From Binary to a Single Signal
    -   Lesson 4.4: The Encoder: A "Diode Matrix" ROM
    -   Lesson 4.5: The Grand Payoff: System Integration
-   **Minecraft Artifact:** A working two-stage translator (decoder and encoder) connected to a 7-segment display.

### Interlude II (Optional): The Power of Abstraction in Practice
-   **Narrative Beat:** We've just built our first multi-part system. Now let's learn how real engineers manage that complexity by packaging our circuits into "black boxes."
-   **Learning Goals:** Understand and apply the principle of abstraction by creating and using subcircuits in a digital logic simulator, making complex designs clean and reusable.

---

## Part II: Engineering a Robust Arithmetic Unit

### Module 5: The Adder & The "Decoder" Bug
-   **Narrative Beat:** Time for real math! We'll build an adder, but immediately discover that our amazing display has a critical limitation, forcing us to think like programmers.
-   **Learning Goals:** Build a circuit for binary addition and understand the concept of an "out of range" error through practical failure.
-   **Minecraft Artifact:** A 4-Bit Ripple-Carry Adder.
-   **The "Aha!" Moment:** Adding `$8+4$` results in a blank display, proving the BCD decoder can't handle numbers above 9.

### Module 6: The Programmer's Solution - The Hexadecimal Upgrade
-   **Narrative Beat:** Our display failed! Instead of a messy fix, let's upgrade our system to speak Hexadecimal. Because of our modular design, this will be an upgrade, not a rebuild.
-   **Learning Goals:** Learn hexadecimal and appreciate modular design by easily expanding an existing circuit.
-   **Minecraft Artifacts:** An upgraded 4-to-16 Binary Decoder and an upgraded encoder for displaying letters A-F.
-   **The Payoff:** The `$8+4$` calculation now correctly displays a `$C$`.

### Module 7: The "Overflow" Bug & The Carry Bit
-   **Narrative Beat:** We'll push our Hex display to its limit, discover a new bug called "overflow," then learn to harness the powerful carry bit to solve it.
-   **Learning Goals:** Discover and understand arithmetic overflow and engineer a solution using the adder's carry-out bit.
-   **The Build:** A "Tens Digit" driver that displays a `1` when the carry-out is active.

### Module 8: The Subtractor & Negative Numbers (Two's Complement)
-   **Narrative Beat:** Our computer can add, but what about subtraction? Thanks to a brilliant mathematical trick, we can teach our existing adder how to subtract.
-   **Learning Goals:** Understand negative number representation (Two's Complement) and build a subtraction circuit using the existing adder.
-   **The Build:** A configurable inverter using XOR gates for one of the adder's inputs.

---

## Part III: The Processor Core

### Module 9: The Multiplexer - The Digital Switch
-   **Narrative Beat:** Before building our final processor, we must build its 'steering wheel'—the Multiplexer, a digital selector switch.
-   **Learning Goals:** Understand the theory and application of a Multiplexer (MUX).
-   **Minecraft Artifact:** A fully functional, scalable 4-bit 2-to-1 MUX.

### Module 10: The ALU - The Grand Assembly
-   **Narrative Beat:** We will forge all our arithmetic and logic circuits into one component: the capstone project of our processor.
-   **Learning Goals:** Combine all functions into a single, controllable Arithmetic Logic Unit (ALU).
-   **The Build:** An ALU with parallel lanes for multiple operations, using a large Multiplexer to select the final output.

---

## Part IV: Creating an Automated Computer

### Module 11: Memory - The Processor's Scratchpad
-   **Narrative Beat:** Our ALU is a powerful but forgetful brain. We need to give it a 'scratchpad' to store its thoughts by building a memory register.
-   **Learning Goals:** Understand how data is stored electronically using latches (the foundation of RAM).
-   **Minecraft Artifact:** A 4-bit memory register built from Gated D-Latches.

### Module 12: The Grand Assembly - Automation
-   **Narrative Beat:** It's time to take our hands off the levers. We will build a clock and a program counter, turning our calculator into a true, self-running computer.
-   **Learning Goals:** Understand how a clock signal and program counter execute a sequence of instructions automatically.
-   **Minecraft Artifacts:** A controllable Redstone Clock, a Program Counter, and a simple hard-coded program (ROM).

---

## Part V: Post-Graduate Studies (Bonus Content)

### Module 13: The "Real World" Display - The Double Dabble Algorithm
-   **Narrative Beat:** Remember the problem from Module 5? We found an elegant programmer's solution with Hex. Now, let's build the complex engineer's solution that digital clocks use.
-   **Learning Goals:** Solve the "numbers over 9" problem by building a proper Binary-to-BCD conversion circuit for multi-digit display.
-   **The Build:** A Double Dabble circuit that takes one 4-bit binary input and produces *two* 4-bit BCD outputs (tens and ones).
-   **The Final Payoff:** Inputting `1101` (13) makes one display show `1` and the other show `3`.
