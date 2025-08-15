### **Module 9: The ALU - The Grand Assembly**

**(Learning Goals:** Combine all arithmetic and logic functions into a single, controllable Arithmetic Logic Unit (ALU), the true heart of a CPU. Solidify understanding of the Multiplexer by using it in a large-scale application.)

**(Narrative Beat:** "We have mastered arithmetic and logic. We have built all the individual pieces. Now, we will forge them all into one component. This will be the capstone project of our processor, a single unit that can be commanded to perform a wide variety of calculations. This is the ALU.")

---

#### **Lesson 9.1: Designing a Full-Featured ALU**

Our goal is to build an ALU that can perform multiple operations, selected by a set of control lines. We want to make full use of the components and concepts we've learned.

**Our ALU's Function List:**
We will implement 6 core functions:
1.  `A AND B` (Bitwise AND)
2.  `A OR B` (Bitwise OR)
3.  `A XOR B` (Bitwise XOR)
4.  `A XNOR B` (Bitwise Equality Check)
5.  `A + B` (Addition)
6.  `A - B` (Subtraction)

To select one of these 6 functions, we will need 3 select lines (since 2³=8, which is enough to address 6 choices).

---

#### **Lesson 9.2: The Lab - Assembling the Calculation Lanes**

**Goal:** To build all the processing units in parallel, ready to be fed into our Multiplexer.

**The Build:**
1.  **Layout:** This will be our largest and most dense build. Start with your two 4-bit input interfaces (Input A and Input B) at the top.
2.  **The Input Bus:** Wire the outputs of A and B so they are available to all the lanes below.
3.  **Lane 1 (AND):** Build a 4-bit AND unit.
4.  **Lane 2 (OR):** Build a 4-bit OR unit.
5.  **Lane 3 (XOR):** Build a 4-bit XOR unit.
6.  **Lane 4 (XNOR):** Build a 4-bit XNOR unit (this is just your XOR unit with a NOT gate on each of the 4 outputs).
7.  **Lane 5 & 6 (Adder/Subtractor):** Place your complete Adder/Subtractor unit from Module 7. This single unit will provide both the ADD and SUB results. We will use the MUX to select its output in two different modes.

---

#### **Lesson 9.3: The Lab - The 4-Bit 6-to-1 MUX**

**Goal:** To build the large multiplexer that will select our final output.

**The Build:**
1.  **The Control Panel:** Create a 3-bit "opcode" (operation code) interface with 3 levers. We will build a 3-to-8 decoder (just like our 2-to-4 decoder, but bigger) to turn this 3-bit code into one of 8 unique control lines. We'll only use the first 6.
2.  **The MUX Array:** This is the scaled-up version of the MUX from Module 8.
    *   For each of the 4 bits of the final output, you will build a large OR gate.
    *   Each OR gate will be fed by 6 AND gates.
    *   Each of these 6 AND gates acts as a "gatekeeper," combining one bit of a result (e.g., Bit 2 from the XOR lane) with the corresponding select line (e.g., the "Select XOR" line from your new decoder).
3.  **The Output:** The final 4-bit bus from the MUX is the official output of your ALU.

---

#### **Lesson 9.4: The Final Integration & Test**

Connect your final ALU output to your two-digit Hex Display system.

**The Experiment:**
Test every function! Set A=C (12) and B=5.
1.  Set the control levers to `000` (for AND). The display should show `4`.
2.  Set the control levers to `001` (for OR). The display should show `D`.
3.  Set the control levers to `100` (for ADD). The display should show `11`.
4.  Set the control levers to `101` (for SUB). The display should show `7`.

---

#### **Module 9 Checkpoint**

*   **Quiz:**
    1.  Why do we need 3 select lines to choose between 6 operations?
    2.  What is the purpose of the 3-to-8 decoder in our MUX control circuit?
    3.  Which physical component provides the results for *two* of our ALU's functions? (The Adder/Subtractor unit).

*   **Real-World Connection: CPU Opcodes**
    > The 3-bit control signal you designed is a simplified version of a CPU's **opcode**. Every instruction a CPU can perform, like `ADD`, `SUBTRACT`, or `JUMP`, has a unique binary opcode. When the CPU's Control Unit decodes an instruction, it sends the corresponding opcode to the ALU to tell it which of its many functions to perform on the data.

**Module 9 Conclusion:**
You have done it. This is the brain of your computer. You have assembled all the logic and arithmetic components into a single, controllable, and powerful processor core. This is the single most complex and important component in our machine. With the ALU complete, we are finally ready to enter the last phase of our project: building the architecture around it to make it run on its own.
