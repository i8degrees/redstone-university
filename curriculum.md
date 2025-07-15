### **Redstone University: The Complete Curriculum**

**Project Vision:** To demystify computer science by guiding learners to build a tangible, 4-bit computer in Minecraft. The course prioritizes understanding foundational theory (Boolean algebra, digital logic) before applying it in satisfying, practical builds, with a strong emphasis on modular, expandable design.

---

### **Part I: The Foundations - Speaking to the Machine**

#### **Module 1: Speaking in 1s and 0s - The Input Register**
*   **Learning Goals:** Understand binary representation (bits, nibbles, place value). Build a physical interface to input binary numbers.
*   **Narrative Beat:** "Let's build our keyboard. It won't have letters, just four switches that let us speak the computer's native language: binary."
*   **Minecraft Artifact:** A 4-bit manual register (4 levers) with a 4-line output bus.

#### **Module 2: The Language of Logic - A Deep Dive into Boolean Algebra**
*   **Learning Goals:** Move beyond physical blocks to understand the formal language of logic (NOT, AND, OR, XOR) and its rules (De Morgan's Law).
*   **Narrative Beat:** "We have our keyboard, but to make the computer *think*, we need to learn its grammar. This is the abstract theory that powers all digital electronics."
*   **Minecraft Artifacts:** Individual, working NOT, AND, OR, and XOR logic gates built from scratch. Drills involve creating truth tables on paper and verifying them with the physical gates.

#### **Module 3: Translators & Our First Display (The Two-Stage Design)**
*   **Learning Goals:** Understand the concepts of decoders and encoders. Apply Boolean logic to a large-scale, modular project.
*   **Narrative Beat:** "Let's build a translator so our computer can talk back to us. We'll build it in two smart stages: first, translating binary to a single idea, then translating that idea into a picture."
*   **Minecraft Artifacts:**
    1.  **Stage 1 (Decoder):** A **4-to-10 BCD Decoder** that converts a 4-bit binary input (0-9) into one of ten active output lines.
    2.  **Stage 2 (Encoder/Driver):** A **10-to-7 Display Encoder** that takes one of the ten active lines and lights up the correct segments on a 7-segment display.
*   **The Payoff:** A fully working display that shows the decimal numbers 0-9 based on the input from the Module 1 register.

---

### **Part II: Upgrading Our System - The Processor Core**

#### **Module 4: The Adder & The First "Bug"**
*   **Learning Goals:** Build a circuit that performs binary addition. Discover and understand the concept of an "out of range" error through practical failure.
*   **Narrative Beat:** "Time for real math! We'll build an adder and connect it to our amazing display. But what happens when our computer gets an answer it wasn't programmed to show?"
*   **Minecraft Artifact:** A 4-Bit Ripple-Carry Adder.
*   **The "Aha!" Moment:** The adder is connected to the display system. Adding `4+3` works perfectly. Adding `8+4` results in a blank display, proving the BCD decoder can't handle numbers above 9.

#### **Module 5: The Programmer's Solution - The Hexadecimal Upgrade**
*   **Learning Goals:** Learn about hexadecimal as the native language for binary. Appreciate the power of modular design by easily expanding an existing circuit.
*   **Narrative Beat:** "Our display failed! Instead of a messy fix, let's do what programmers do: upgrade our system to speak the computer's native tongue, Hexadecimal. Because we designed it well, this will be an upgrade, not a rebuild."
*   **Minecraft Artifacts:**
    1.  **Upgraded Stage 1:** The BCD decoder is expanded into a full **4-to-16 Binary Decoder** by adding 6 more output lines for A-F.
    2.  **Upgraded Stage 2:** The Display Encoder is expanded to include the logic for drawing the letters A-F.
*   **The Payoff:** The `8+4` calculation now correctly displays a `C`. The system is now robust and can display any 4-bit value. **The Hex Display is now the standard output.**

#### **Module 6: The ALU - A Versatile Processor**
*   **Learning Goals:** Combine multiple arithmetic and logic functions into a single Arithmetic Logic Unit (ALU). Use a multiplexer (MUX) to select a function.
*   **Narrative Beat:** "Our computer can add, but a real processor is more versatile. Let's build a true ALU and a control panel to choose whether we want to ADD, AND, or OR our numbers."
*   **The Build:** Construct parallel logic lanes for AND, OR, and the Adder, with a MUX to select which result is sent to the Hex Display.

---

### **Part III: The Automated Computer (Senior-Level Courses)**

#### **Module 7: Memory - Giving Our Computer a Brain**
*   **Learning Goals:** Understand how data is stored electronically using latches (the foundation of RAM).
*   **Narrative Beat:** "A computer isn't very useful if it can't remember things. Let's build a 'scratchpad' where our ALU can store a result."
*   **Minecraft Artifact:** A 4-bit memory register built from Gated D-Latches.

#### **Module 8: The Heartbeat & Conductor - Automating the Machine**
*   **Learning Goals:** Understand how a clock signal and program counter work together to execute a sequence of instructions automatically.
*   **Narrative Beat:** "It's time to take our hands off the levers. We'll build a clock to provide a heartbeat and a program counter to act as a conductor, telling the computer what to do on each beat."
*   **Minecraft Artifacts:** A controllable Redstone Clock, a Program Counter, and a simple hard-coded "program" (ROM) to run a sequence of operations.

---

### **Part IV: Post-Graduate Studies (Bonus Content)**

#### **Module 9: The "Real World" Display - The Double Dabble Algorithm**
*   **Learning Goals:** Solve the original "numbers over 9" problem by building a proper Binary-to-BCD conversion circuit for multi-digit display.
*   **Narrative Beat:** "Remember the problem from Module 4? We found an elegant programmer's solution with Hex. Now, as a final challenge, let's build the complex engineer's solution that digital clocks use."
*   **The Build:** A Double Dabble circuit that takes one 4-bit binary input and produces *two* 4-bit BCD outputs (tens and ones), which then feed into two separate BCD display decoders.
*   **The Final Payoff:** Inputting `1101` (13) makes one display show `1` and the other show `3`, completing the journey from abstract binary to multi-digit human-readable numbers.