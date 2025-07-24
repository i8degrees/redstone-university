### **Redstone University: The Complete Curriculum**

**Project Vision:** To demystify computer science by guiding learners to build a tangible, 4-bit computer in Minecraft. The course prioritizes understanding foundational theory (Boolean algebra, digital logic) before applying it in satisfying, practical builds, with a strong emphasis on modular, expandable design.

---

### **Part I: The Foundations - Speaking to the Machine**

#### **Module 1: Speaking in 1s and 0s - The Input Register**
*   **Learning Goals:** Understand binary representation (bits, nibbles, place value). Build a physical interface to input binary numbers.
*   **Narrative Beat:** "Let's build our keyboard. It won't have letters, just four switches that let us speak the computer's native language: binary."
*   **Minecraft Artifact:** A 4-bit manual register (4 levers) with a 4-line output bus.

#### **Module 2: The Language of Logic - A Deep Dive into Boolean Algebra**
*   **Learning Goals:** Move beyond physical blocks to understand the formal language of logic (NOT, AND, OR, XOR, NAND, NOR, XNOR) and its rules (De Morgan's Law).
*   **Narrative Beat:** "We have our keyboard, but to make the computer *think*, we need to learn its grammar. This is the abstract theory that powers all digital electronics."
*   **Minecraft Artifacts:** Individual, working logic gates built from scratch. Drills involve creating truth tables on paper and verifying them with the physical gates.

#### **Module 3: Translators & Our First Display (The Two-Stage Design)**
*   **Learning Goals:** Understand the concepts of decoders and encoders. Apply Boolean logic to a large-scale, modular project.
*   **Narrative Beat:** "Let's build a translator so our computer can talk back to us. We'll build it in two smart stages: first, translating binary to a single idea, then translating that idea into a picture."
*   **Minecraft Artifacts:**
    1.  **Stage 1 (Decoder):** A **4-to-10 BCD Decoder** that converts a 4-bit binary input (0-9) into one of ten active output lines.
    2.  **Stage 2 (Encoder/Driver):** A **10-to-7 Display Encoder** that takes one of the ten active lines and lights up the correct segments on a 7-segment display.
*   **The Payoff:** A fully working display that shows the decimal numbers 0-9 based on the input from the Module 1 register.

---

### **Part II: Engineering a Robust Arithmetic Unit**

#### **Module 4: The Adder & The "Decoder" Bug**
*   **Learning Goals:** Build a circuit that performs binary addition. Discover and understand the concept of an "out of range" error through practical failure.
*   **Narrative Beat:** "Time for real math! We'll build an adder and connect it to our amazing display. But what happens when our computer gets an answer our display wasn't programmed to understand?"
*   **Minecraft Artifact:** A 4-Bit Ripple-Carry Adder.
*   **The "Aha!" Moment:** Adding `4+3` works perfectly. Adding `8+4` results in a blank display, proving the BCD decoder can't handle numbers above 9.

#### **Module 5: The Programmer's Solution - The Hexadecimal Upgrade**
*   **Learning Goals:** Learn about hexadecimal as the native language for binary. Appreciate the power of modular design by easily expanding an existing circuit.
*   **Narrative Beat:** "Our display failed! Instead of a messy fix, let's do what programmers do: upgrade our system to speak the computer's native tongue, Hexadecimal. Because we designed it well, this will be an upgrade, not a rebuild."
*   **Minecraft Artifacts:**
    1.  **Upgraded Stage 1:** The BCD decoder is expanded into a full **4-to-16 Binary Decoder**.
    2.  **Upgraded Stage 2:** The Display Encoder is expanded to include the logic for drawing the letters A-F.
*   **The Payoff:** The `8+4` calculation now correctly displays a `C`. The system is now robust... or is it?

#### **Module 6: The "Overflow" Bug & The Carry Bit**
*   **Learning Goals:** Discover and understand the concept of arithmetic **overflow**. Engineer a solution using the adder's **carry-out** bit to create a two-digit display.
*   **Narrative Beat:** "Our Hex display is powerful, but let's push it to its absolute limit. What happens when the answer is too big for even a single Hex digit? We'll discover a new bug and learn to harness a single, powerful bit—the carry bit—to solve it."
*   **"Aha!" Moment:** Adding `C + 5` (`12 + 5 = 17`) results in the Hex display showing `1`, which is wrong. The student discovers the `Carry-Out` lamp is lit, holding the missing `16`.
*   **The Build:** Construct a simple "Tens Digit" driver that displays a `1` when the carry-out is active.
*   **The Payoff:** The display now correctly shows `11` (hex for 17). Our adder's output is now fully and accurately represented.

#### **Module 7: The Subtractor & Negative Numbers (Two's Complement)**
*   **Learning Goals:** Understand how negative numbers are represented in binary (Two's Complement). Learn how to build a circuit that can perform subtraction using the existing adder.
*   **Narrative Beat:** "Our computer can add, but what about subtraction? Are we going to have to build a whole new, complicated 'subtractor' circuit? No! Thanks to a brilliant mathematical trick, we can teach our existing adder to subtract."
*   **The Build:** Create a configurable inverter using XOR gates for one of the adder's inputs, allowing it to perform `A + (!B) + 1`, which is the formula for subtraction.

---

### **Part III: The Processor Core**

#### **Module 8: The Multiplexer - The Digital Switch**
*   **Learning Goals:** Understand the theory and practical application of a Multiplexer (MUX) as a digital selector switch.
*   **Narrative Beat:** "We've mastered arithmetic. Now we need a way to choose between different operations. Before we build our final processor, we must first build the component that acts as its 'steering wheel'—the Multiplexer."
*   **Minecraft Artifact:** A fully functional, scalable 4-bit 2-to-1 MUX, establishing the design for the larger MUX to come.

#### **Module 9: The ALU - The Grand Assembly**
*   **Learning Goals:** Combine all arithmetic and logic functions into a single, controllable Arithmetic Logic Unit (ALU), the true heart of a CPU.
*   **Narrative Beat:** "We have mastered arithmetic and logic. Now we will forge them all into one component. This will be the capstone project of our processor, a single unit that can be commanded to perform a wide range of calculations."
*   **The Build:** Construct parallel lanes for **ADD, SUB, AND, OR, XOR, and XNOR**, and then use a large Multiplexer to select the final output.

---

### **Part IV: Creating an Automated Computer**

#### **Module 10: Memory - The Processor's Scratchpad**
*   **Learning Goals:** Understand how data is stored electronically using latches (the foundation of RAM).
*   **Narrative Beat:** "Our ALU is a powerful but forgetful brain. We need to give it a 'scratchpad' to store its thoughts. Let's build a memory register."
*   **Minecraft Artifact:** A 4-bit memory register built from Gated D-Latches.

#### **Module 11: The Grand Assembly - Automation**
*   **Learning Goals:** Understand how a clock signal and program counter work together to execute a sequence of instructions automatically.
*   **Narrative Beat:** "It's time to take our hands off the levers. We will build a clock to provide a heartbeat and a program counter to act as a conductor, turning our calculator into a true, self-running computer."
*   **Minecraft Artifacts:** A controllable Redstone Clock, a Program Counter, and a simple hard-coded program (ROM) that tells the computer to perform a sequence of operations.

---

### **Part V: Post-Graduate Studies (Bonus Content)**

#### **Module 12: The "Real World" Display - The Double Dabble Algorithm**
*   **Learning Goals:** Solve the original "numbers over 9" problem by building a proper Binary-to-BCD conversion circuit for multi-digit display.
*   **Narrative Beat:** "Remember the problem from Module 4? We found an elegant programmer's solution with Hex. Now, as a final challenge, let's build the complex engineer's solution that digital clocks use."
*   **The Build:** A Double Dabble circuit that takes one 4-bit binary input and produces *two* 4-bit BCD outputs (tens and ones), which then feed into two separate BCD display decoders.
*   **The Final Payoff:** Inputting `1101` (13) makes one display show `1` and the other show `3`, completing the journey from abstract binary to multi-digit human-readable numbers.