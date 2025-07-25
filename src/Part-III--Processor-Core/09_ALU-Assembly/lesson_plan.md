### **Module 9: The ALU - A Versatile Processor**

**(Learning Goals:** Combine multiple arithmetic and logic functions into a single Arithmetic Logic Unit (ALU). Understand and build a Multiplexer (MUX) to select which function's output to use. Appreciate the ALU as the core computational unit of a CPU.)

**(Narrative Beat:** "Our computer can now add, and our display can handle any result. But a real processor is more than just a calculator—it's a *logic* machine. It's time to combine our Adder with the logic gates from Module 2 to build a true Arithmetic Logic Unit, or ALU. This is the component that does the real 'thinking'.")

---

#### **Lesson 9.1: What is an ALU?**

The **Arithmetic Logic Unit (ALU)** is the component inside a Central Processing Unit (CPU) that performs arithmetic operations (like addition, subtraction) and bitwise logic operations (like AND, OR, XOR).

Our computer can currently do ONE thing: add. But we've also built separate AND and OR gates. What if we wanted our computer to be able to do any of those, on demand?

We could have three separate output displays, one for each calculation. But that's inefficient. A real CPU has one set of registers and one main data bus. The solution is to perform all the calculations simultaneously and then use a special circuit to choose which result we care about. This special circuit is a **Multiplexer**.

**Our Plan:**
1.  Build three "calculation lanes" that all run in parallel, taking the same two 4-bit numbers (from Register A and B) as input. One lane for ADD, one for AND, one for OR.
2.  Build a "control panel" with levers that tell the computer which operation we want to perform.
3.  Build a **4-bit 3-to-1 Multiplexer (MUX)** that acts as a "selector switch." Based on our control panel, it will select one of the three results and pass it to our Hex Display.

---

#### **Lesson 9.2: The Lab - Building the Parallel Calculation Lanes**

**Goal:** To have three separate circuits all calculating at the same time.

**The Build:**
1.  **Layout:** This will be our largest build yet. Arrange your components with space:
    *   At the top, place your two 4-bit input registers (Register A and Register B).
    *   Below them, create three distinct horizontal "lanes."
2.  **Lane 1 (The AND Lane):** Build a bank of four AND gates.
3.  **Lane 2 (The OR Lane):** Build a bank of four OR gates.
4.  **Lane 3 (The ADD Lane):** Place your 4-bit Adder from Module 4.
5.  **The Input Bus:** This is the key. Wire the outputs of Register A and Register B so that they feed into *all three lanes simultaneously*. For example, the first bit from Register A will connect to the first AND gate, the first OR gate, AND the first Full Adder module.
6.  **The Outputs:** At the end of this step, you will have three separate 4-bit output buses. One shows `A AND B`, one shows `A OR B`, and one shows `A + B`. You can temporarily connect lamps to each to verify they are all working at once.

---

#### **Lesson 9.3: The Theory & Lab - Building the Multiplexer (MUX)**

**Goal:** To understand and build a circuit that can select one of several inputs to pass to a single output.

**The Concept:** A Multiplexer, or MUX, is a digital switch. Think of a train track with multiple parallel lines merging into one. A switch operator (our control panel) throws a lever to determine which train gets to go onto the main line.

**The Design (for a single bit):**
How do we choose which of the three result bits (the AND result, the OR result, or the ADD result) gets to go to our final display? We use AND gates as "gatekeepers."

Let's say `R_AND` is the result from the AND lane, `R_OR` is from the OR lane, and `R_ADD` is from the ADD lane. And let's say we have three control levers: `S_AND`, `S_OR`, `S_ADD` (where only one can be ON at a time).

*   The final output `Y` will be:
    *   `(R_AND AND S_AND) OR (R_OR AND S_OR) OR (R_ADD AND S_ADD)`

If we turn `S_AND` ON, the expression becomes `(R_AND AND 1) OR (R_OR AND 0) OR (R_ADD AND 0)`, which simplifies to just `R_AND`. The MUX has selected the AND result!

**The Minecraft Build (A 4-bit 3-to-1 MUX):**
1.  **Control Panel:** Create three levers, labeled "SELECT ADD," "SELECT AND," "SELECT OR."
2.  **Gatekeeper Array:** For each of the four bits of our output, we need to build this logic. Let's focus on **Bit 0**:
    *   Take Bit 0 from the AND Lane's output and feed it into a new AND gate. The other input to this gate is the "SELECT AND" lever.
    *   Take Bit 0 from the OR Lane's output and feed it into a new AND gate. The other input is the "SELECT OR" lever.
    *   Take Bit 0 from the ADD Lane's output and feed it into a new AND gate. The other input is the "SELECT ADD" lever.
3.  **Final Output Bus:** Merge the outputs of these three new "gatekeeper" AND gates. This single, merged line is Bit 0 of our final ALU output.
4.  **Repeat:** Duplicate this entire structure for Bits 1, 2, and 3.

**ASCII Schematic (Conceptual view for one bit):**
```
                    .---[AND Gate]---.
 (From AND Lane) ---+               |
                    '---(S_AND)     |
                                    |
                    .---[AND Gate]--(+)--[OR Gate]--> To Display
 (From OR Lane) ----+               |
                    '---(S_OR)      |
                                    |
                    .---[AND Gate]---'
(From ADD Lane) ---+
                    '---(S_ADD)
```

---

#### **Lesson 9.4: The Final Integration & Test**

Connect the final 4-bit output bus from your MUX to the 4-bit input of your Hex Display system from Module 5.

**The Experiment:**
1.  Set Register A to `0110` (6) and Register B to `0011` (3).
2.  Flip the **"SELECT AND"** lever ON. The display should show `2` (since `6 & 3 = 2`).
3.  Flip the **"SELECT OR"** lever ON. The display should show `7` (since `6 | 3 = 7`).
4.  Flip the **"SELECT ADD"** lever ON. The display should show `9` (since `6 + 3 = 9`).

---

#### **Module 9 Checkpoint**

*   **Quiz:**
    1.  What is the purpose of a Multiplexer (MUX)?
    2.  In our ALU, how many calculations are happening at any given moment? (Three: AND, OR, and ADD are all happening in parallel).
    3.  If we wanted to add a "XOR" function to our ALU, what two major components would we need to add? (A 4-bit XOR lane, and expand the MUX to be 4-to-1).

*   **Real-World Connection: The Control Unit**
    > Your MUX is the "steering wheel" of the ALU, and your control levers are a simplified version of the CPU's **Control Unit**. In a real CPU, the Control Unit reads a program's instructions (like "ADD" or "AND") and automatically sends the correct electrical signals to the ALU's multiplexer to select the right operation, thousands of times per second.

**Module 9 Conclusion:**
You have now built the single most important component of a processor. Your ALU combines arithmetic and logic into one controllable unit. Our machine can now do more than just calculate; it can be *told* what kind of calculation to perform. This is a massive leap towards creating a truly programmable computer. In the next Part, we'll give this powerful new processor a memory to store its results and a heartbeat to let it run on its own.
