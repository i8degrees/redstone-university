### **Module 8: The Multiplexer - The Digital Switch**

**(Learning Goals:** Understand the theory and practical application of a **Multiplexer (MUX)** as a digital selector switch. Build a simple 1-bit 2-to-1 MUX from basic gates. Scale that design up to a 4-bit MUX that will be used in our ALU.)

**(Narrative Beat:** "We've mastered arithmetic. We have components that can add and subtract, and we have logic gates that can perform AND, OR, and XOR. Now we face a new problem: how do we choose which of these operations to perform? Before we can build our final processor, we must first build the component that acts as its 'steering wheel'—the Multiplexer. This is the circuit that lets us make a choice.")

---

#### **Lesson 8.1: The Theory - The Power of Choice**

Imagine you have two different TV channels coming into your house on two separate wires, but you only have one TV screen. You need a "channel selector" box. This box would have three inputs: the wire for Channel A, the wire for Channel B, and a knob or switch to select which channel you want to watch. The box would then have one output that goes to your TV.

A **Multiplexer (MUX)** is exactly this: it's a digital channel selector. It takes multiple data inputs, one "select" input, and produces a single data output. It looks at the select line to decide which of the data inputs to "pass through" to the output.

**The Logic of a Simple 2-to-1 MUX:**
Let's design the simplest possible MUX. It has two data inputs (`A` and `B`) and one select line (`S`). It has one output (`Y`).
*   **The Rule:** If `S=0`, the output `Y` should be equal to `A`. If `S=1`, the output `Y` should be equal to `B`.

How can we build this with our familiar logic gates? We can use AND gates as "gatekeepers."
1.  One gatekeeper checks: `A AND (!S)`. This will only be `A` if `S` is 0. Otherwise, it's 0.
2.  The other gatekeeper checks: `B AND S`. This will only be `B` if `S` is 1. Otherwise, it's 0.
3.  We then combine the results with an OR gate.

*   **The Full Boolean Expression:** `Y = (A AND !S) OR (B AND S)`

Let's trace this:
*   If `S=0`: The expression becomes `(A AND 1) OR (B AND 0)`, which simplifies to `A OR 0`, which is just `A`. The output is A!
*   If `S=1`: The expression becomes `(A AND 0) OR (B AND 1)`, which simplifies to `0 OR B`, which is just `B`. The output is B!

The logic is sound. We can build a switch out of simple gates.

---

#### **Lesson 8.2: The Lab - Building a 1-Bit 2-to-1 MUX**

**Goal:** To build a physical, working "channel selector" for a single bit.

**The Build:** This circuit is a direct implementation of the Boolean expression from our theory lesson.
1.  **Inputs:** Create three levers: `A`, `B`, and `S` (Select).
2.  **Logic:**
    *   Build one AND gate. Its inputs are `A` and `!S` (the `S` lever run through a NOT gate).
    *   Build a second AND gate. Its inputs are `B` and `S`.
    *   Take the outputs from both AND gates and merge them together (an OR gate).
3.  **Output:** Connect the final merged line to a Redstone Lamp, `Y`.

**ASCII Schematic (Conceptual):**
```
Input A ---.                .---[AND Gate]---.
           +---------------+                  |
Input !S --'                |                  +---[OR Gate]---> Output Y
                            |                  |
Input B ---.                '---[AND Gate]---'
           +---------------+
Input S ---'
```
*(Note: `!S` is just the `S` signal passed through a NOT gate).*

**Lab & Experiment:**
1.  Set `S` to `0`. Now flip `A` on and off. You should see the output lamp `Y` exactly copy `A`. `B` does nothing.
2.  Set `S` to `1`. Now flip `B` on and off. You should see `Y` exactly copy `B`. `A` does nothing.
3.  **Verification:** You have successfully built a working digital switch!

---

#### **Lesson 8.3: The Lab - Scaling Up to a 4-Bit MUX**

Our computer works with 4-bit numbers, so we need a MUX that can select between two 4-bit buses.

**Goal:** To build a MUX that can select between a 4-bit Bus A and a 4-bit Bus B.

**The Concept:** This sounds hard, but it's incredibly simple. We just build **four 1-bit MUXes** side-by-side!
*   The first MUX will choose between Bit 0 of A and Bit 0 of B.
*   The second MUX will choose between Bit 1 of A and Bit 1 of B.
*   ...and so on for all four bits.

The crucial part is that the **Select (`S`) line is shared**. The same `S` lever will control all four MUXes simultaneously, so they all switch in perfect unison.

**The Build:**
1.  **Inputs:** You'll have two 4-bit input buses (Bus A and Bus B) and one single Select lever (`S`).
2.  **The MUX Array:** Build four copies of the 1-bit MUX circuit you created in the previous lesson.
3.  **Wiring:**
    *   Connect the four `A` inputs of your MUXes to the four wires of Bus A.
    *   Connect the four `B` inputs of your MUXes to the four wires of Bus B.
    *   Connect the single `S` lever (and its inverter `!S`) to the `S` inputs of *all four* MUXes.
4.  **Output:** The four `Y` outputs from your MUXes form a new 4-bit bus, which is your final result.

---

#### **Module 8 Checkpoint**

*   **Quiz:**
    1.  In plain English, what does a Multiplexer do? (It chooses one of several inputs to pass to a single output).
    2.  Which two logic gates are the primary building blocks of a simple MUX? (AND and OR).
    3.  If we want to build a MUX that can select between *four* different inputs instead of two, how many select lines would we need? (Hint: How many bits does it take to represent four choices?). (Answer: 2 select lines).

*   **Real-World Connection: The CPU Bus**
    > A real CPU has many different components that all need to send data to the same place (like main memory or the ALU). It uses large, complex multiplexers to control this traffic. When the CPU needs to read from RAM, the MUX selects the RAM's output bus. When it needs to read from the keyboard, the MUX switches to select the keyboard's input bus. The MUX is the traffic cop for the CPU's data highway.

**Module 8 Conclusion:**
You have now built one of the most fundamental control components in digital logic. This digital switch is the key that will unlock the full potential of our processor. With the ability to choose, we can now assemble all of our separate arithmetic and logic circuits into one unified, powerful, and versatile component. In the next module, we will do exactly that, building the grand centerpiece of our machine: the ALU.
