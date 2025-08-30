## Module 9: The ALU – The Grand Assembly

### Module 9 Summary

-   **Narrative Beat:** The grand assembly. We will take all the individual arithmetic, logic, and comparison circuits we have built and forge them into the single, powerful, and controllable brain of our computer: the Arithmetic Logic Unit (ALU).
-   **Learning Goals:**
    -   Understand the architecture of a simple bitwise ALU.
    -   Combine multiple functions into parallel "calculation lanes."
    -   Use a large multiplexer to select the final output from one of the lanes.
    -   Integrate the status flag logic to create an ALU that reports on its results.
-   **Lesson Overview:**
    -   Lesson 9.1: The Blueprint for a Brain
    -   Lesson 9.2: The Lab – Assembling the Calculation Lanes
    -   Lesson 9.3: The Lab – Building the Output Selector
    -   Lesson 9.4: The Final Integration and Testing
-   **Minecraft Artifact:** A complete ALU that can add, subtract, and perform logical operations, outputting both a 4-bit result and 2 status flags.

---

### Module 9 Introduction

You have done it. You have built all the individual pieces of a processor's brain. You have circuits that can perform arithmetic, circuits that can perform bitwise logic, and circuits that can detect the status of a number. Now, it is time to forge them into one.

Welcome to the grand assembly.

In this module, we will build the single most important and complex component of our computer: the **Arithmetic Logic Unit (ALU)**. The ALU is the true heart of any CPU, the versatile core that handles all calculations and logical operations.

We will follow a classic design, building parallel "lanes" for each of our functions (ADD, SUB, AND, OR, etc.). Then, we will construct a large 4-bit multiplexer to act as a "selector," allowing us to choose which lane's result we want to see. Finally, we'll connect our status flag circuits to create a true-to-life ALU that doesn't just calculate, but also reports on the outcome. This is the capstone project of Part II.

---

### Lesson 9.1: The Blueprint for a Brain

> **Key Takeaway:** A bitwise ALU operates by performing many different calculations on the same inputs simultaneously, and then using a multiplexer to select the one desired result.

Our goal is to build an ALU that can perform a variety of operations. To do this, we won't be building a single, monolithic circuit. Instead, we'll use a much smarter, more modular design.

1.  **The Input Buses:** We will start with two 4-bit input buses, $A$ and $B$.
2.  **The Calculation Lanes:** The signals from $A$ and $B$ will be fed into *every* one of our calculation units at the same time. We will have a lane for addition, a lane for subtraction, a lane for AND, and so on. At any given moment, *all* of these circuits will be calculating their result.
3.  **The Selector (MUX):** We will then use a large 4-bit multiplexer, controlled by a few "select lines," to choose which of the many results we want to pass through to the final output. These select lines are our **opcode** (short for operation code).
4.  **The Outputs:** The ALU will have two outputs: the main 4-bit result bus, and the 2-bit status bus (for our Z and N flags).

![ALU Architecture Diagram](./images/alu-architecture-circuitverse.png)
*Figure: The high-level architecture of our ALU. Inputs A and B are fed to all lanes in parallel. A multi-bit MUX, controlled by an opcode, selects which result is sent to the final output.*

---

### Lesson 9.2: The Lab – Assembling the Calculation Lanes

> **Key Takeaway:** The first step of building an ALU is to construct all the individual processing units in parallel, ready to be selected by the MUX.

#### Lab & Experiment

1.  **Layout:** This will be our largest build yet. Start with your two 4-bit input buses ($A$ and $B$) at one end.
2.  **The Input Bus:** Wire the outputs of $A$ and $B$ so they are available as long, parallel lines to all the lanes you are about to build.
3.  **Lane 1 (ADD/SUB):** Build your complete Adder/Subtractor unit from Module 6. This single component will provide *two* of our results. The 4-bit sum output will be one result, and you can create a separate subtraction result by building a second adder or by using a MUX controlled by the subtract line. For simplicity, we will assume you build a dedicated subtraction lane for now.
4.  **Lane 2 (AND):** Build a 4-bit AND unit (four AND gates in parallel).
5.  **Lane 3 (OR):** Build a 4-bit OR unit (four OR gates in parallel).
6.  **Lane 4 (XOR):** Build a 4-bit XOR unit (four XOR gates in parallel).
7.  **Outputs:** You should now have four separate 4-bit result buses, one from each lane, ready to be fed into our selector.

![ALU Lanes Minecraft Build](./images/alu-lanes-minecraft.png)
*Figure: The calculation lanes of the ALU built in parallel in Minecraft. Each lane takes the same A and B inputs and calculates its result independently.*

---

### Lesson 9.3: The Lab – Building the Output Selector

> **Key Takeaway:** A 4-bit, 4-to-1 multiplexer can be constructed by using a decoder to control the AND "gatekeepers" for each of the four calculation lanes.

Now we need to build the large multiplexer that will select our final output. Since we have four lanes, we will need two select lines ($S_1$ and $S_0$) to choose between them (`` `00` ``, `` `01` ``, `` `10` ``, `` `11` ``).

#### Lab & Experiment

1.  **The Control Panel:** Create a 2-bit "opcode" interface with two levers for $S_1$ and $S_0$.
2.  **The Decoder:** Connect these two levers to a **2-to-4 decoder**, just like the one we built in Module 4. This will turn our 2-bit code into four unique control lines (one for each lane).
3.  **The MUX Array:** This is a scaled-up version of the MUX from Module 8.
    -   For **each of the four bits** of the final output, you will build a large OR gate.
    -   Each of these OR gates will be fed by four AND gates.
    -   Each of these four AND gates acts as a "gatekeeper," combining one bit of a result (e.g., Bit 2 from the XOR lane) with the corresponding select line (e.g., the "Select XOR" line from your decoder).
4.  **The Output:** The final 4-bit bus from the MUX is the official result output of your ALU.

![ALU MUX Minecraft Build](./images/alu-mux-minecraft.png)
*Figure: The large 4-to-1 MUX array being wired up. The four vertical result buses from the calculation lanes are being fed into the selector, controlled by the decoder at the front.*

---

### Lesson 9.4: The Final Integration and Testing

> **Key Takeaway:** The final step is to connect the status flag logic to the ALU's output bus, creating a processor core that not only calculates but also reports on its results.

#### Lab & Experiment

1.  **Connect the Flags:** Take the final 4-bit result bus from your MUX. Connect this bus to the inputs of your **Zero Flag** (4-input NOR gate) and **Negative Flag** (a single wire from the MSB) circuits from Module 7.
2.  **The Final Test:** Your ALU is complete. Connect its final 4-bit result output and your 2-bit flag outputs to indicator lamps. Test every function!
    -   Set $A$=`` `1100` `` ($C$) and $B$=`` `0101` `` (5).
    -   Set the opcode levers to `` `00` `` (e.g., for ADD). The result should be `` `0001` `` (`1`), and the **Carry Flag** from the adder (if you wired it) and the **Negative Flag** should both be ON.
    -   Set the opcode to `` `01` `` (e.g., for SUB). The result should be `` `0111` `` (`7`). Both flags should be OFF.
    -   Set the opcode to `` `10` `` (e.g., for AND). The result should be `` `0100` `` (`4`). Both flags should be OFF.
    -   Test a case for the Zero Flag: set $A$=`` `0101` ``, $B$=`` `0101` ``, and the opcode to SUB. The result should be `` `0000` ``, and the **Zero Flag** should turn ON.

---

### Module 9 Conclusion

You have done it. This is the brain of your computer. You have assembled all the logic and arithmetic components into a single, controllable, and powerful processor core. This is the single most complex and important component in our machine. With the ALU complete, we are finally ready to enter the last phase of our project: building the architecture around it to make it run on its own.

---

### Module 9 Checkpoint

#### Practice Problem 9.5.1: Knowledge Check
1. In a bitwise ALU, why are all calculations performed in parallel?
2. What is the purpose of the decoder in the MUX control circuit?
3. If our ALU result is `` `1000` ``, what will the state of the Z and N flags be?

<details>
<summary><strong>Show Solution</strong></summary>
1. It's simpler to have all units working at once and then select the desired output, rather than trying to build complex logic to turn the different units on and off.
2. The decoder takes the binary "opcode" from the select lines and turns it into a single "active" line to open the correct AND gatekeepers in the multiplexer.
3. The Z (Zero) flag will be `0` because the result is not `0000`. The N (Negative) flag will be `1` because the most significant bit is `1`.
</details>

#### Practice Problem 9.5.2: The Expansion
You want to add a new function to your ALU: `NOT A`. You assign it the opcode `` `11` ``. Describe the steps you would need to take to add this new lane.

<details>
<summary><strong>Show Solution</strong></summary>
1. **Build the Lane:** Build a new "calculation lane" that consists of four NOT gates, taking its input from the 4-bit Bus A.
2. **Expand the MUX:** For each of the four output bits, you would need to add a fifth AND gate to the final OR gate.
3. **Connect the Lane:** This new AND gate would take its data input from one bit of your new `NOT A` lane, and its control input from the `` `11` `` output of your 2-to-4 decoder.
</details>

#### Key Terms
-   **Arithmetic Logic Unit (ALU)**: The part of a central processing unit (CPU) that carries out arithmetic and logic operations. It is the fundamental building block of a processor.
-   **Opcode (Operation Code)**: A set of bits that defines a specific machine language instruction to be performed by the CPU, such as `ADD` or `JUMP`.
-   **Bitwise Operation**: An operation that works on one or more binary numbers at the level of their individual bits (e.g., 4-bit AND).```
