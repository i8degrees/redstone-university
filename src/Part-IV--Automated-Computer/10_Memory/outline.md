### **Module 10: Memory - Giving Our Computer a Brain to Remember (Enhanced Edition)**

**(Learning Goals:** Understand the concept of "state" in digital circuits. Learn how to build a basic memory cell (an RS Latch) and then upgrade it to a more useful, controllable Gated D-Latch. Combine these into a 4-bit register that can store and hold a number.)

**(Narrative Beat:** "Our ALU is a powerful calculator, but it has the memory of a goldfish. As soon as we change the inputs, the previous result is gone forever. A computer isn't truly useful if it can't remember things. In this module, we'll build a 'scratchpad' for our computer—a circuit that can latch onto a number and hold it, forming the foundation of computer memory, or RAM.")

---

#### **Lesson 10.1: The Problem of "Stateless" Circuits**

So far, all the circuits we've built are **combinational**. This means their output depends *only* on their current inputs. An AND gate's output is determined solely by what A and B are *right now*. Change the inputs, and the output instantly changes without any memory of what came before.

To build memory, we need a **sequential** circuit. Its output depends not only on the current inputs, but also on its *previous state*. We need to create a circuit that can get "stuck" in a `1` or `0` state, even after the input that put it there is gone.

How can we do this? By creating a **feedback loop**. We will take the output of a gate and feed it back into its own input.

---

#### **Lesson 10.2: The Lab - The Simplest Memory Cell (The RS Latch)**

**Goal:** To build the most basic memory circuit, the RS Latch (Reset-Set Latch), and understand its behavior.

**The Concept:** The RS Latch has two inputs, Set (S) and Reset (R), and two outputs, Q and its inverse, !Q.
*   Pulsing the **Set** input forces the Q output to `1`, and it stays `1`.
*   Pulsing the **Reset** input forces the Q output to `0`, and it stays `0`.
*   If both inputs are `0`, the latch "remembers" its last state.

**The Minecraft Build (using NOR Gates):**
The easiest way to build an RS Latch is by cross-coupling two NOR gates. A NOR gate is simply an OR gate followed by a NOT gate.
1.  **The Gates:** Place two NOR gates. (A NOR gate in Minecraft can be two input dust lines merging into a block with a torch on the front).
2.  **The Feedback Loop:**
    *   The output of the top NOR gate becomes an input for the bottom NOR gate.
    *   The output of the bottom NOR gate becomes an input for the top NOR gate.
3.  **The Inputs:** The second, unused inputs on each NOR gate are our `Set` and `Reset` lines.
4.  **The Outputs:** The signal coming off the top NOR gate's output wire is `!Q`. The signal from the bottom NOR gate is `Q`.

**ASCII Schematic:**
```
                          .----------<----------.
                          |                     |
Input S ---.                |                     |
           +---[NOR Gate]---+-------------------> Output Q
Input R ---'   ^            |
               |            v
           .---[NOR Gate]---+-------------------> Output !Q
           |                |
           '----------<-----.
```

**Lab & Experiment:**
1.  Use two buttons for S and R. Connect Q to a lamp.
2.  **Set:** Press the `S` button once. The Q lamp turns ON and, crucially, *stays on* after you release the button. You have stored a `1`.
3.  **Reset:** Press the `R` button once. The Q lamp turns OFF and *stays off*. You have stored a `0`.
4.  **The Forbidden State:** What happens if you press S and R at the same time? (The output becomes unpredictable, which is why simple RS Latches aren't used for everything).

---

#### **Lesson 10.3: A More Useful Memory - The Gated D-Latch**

**Goal:** To upgrade our simple latch into a practical memory cell that we can use in our computer.

**The Problem:** The RS Latch is a bit awkward. We want something simpler. We want a "Data" input (`D`) and a "Write Enable" input (`WE`).
*   When `WE` is ON, the latch should copy whatever value is on the `D` input.
*   When `WE` is OFF, the latch should ignore the `D` input and just remember what it was last told.

This is called a **Gated D-Latch** (or transparent latch), and we can build it by adding a few AND gates to our RS Latch.

**The Design:**
*   `Set = D AND WE`
*   `Reset = (!D) AND WE`

When `WE` is `0`, both the Set and Reset lines are forced to `0`, so the underlying RS Latch just holds its value. When `WE` is `1`, if `D` is `1`, the Set line activates. If `D` is `0`, the Reset line activates. It works perfectly!

**The Minecraft Build:**
1.  Start with your RS Latch from the previous lesson.
2.  Add the input logic: two AND gates and one NOT gate, wired up according to the logic above.
3.  You now have a new component with two inputs: `D` (Data) and `WE` (Write Enable), and one main output `Q`.
**(A clear ASCII schematic of the full Gated D-Latch would be provided here).**

---

#### **Lesson 10.4: The Lab - Building the 4-Bit Memory Register**

**Goal:** To combine four of our D-Latches to create a register that can store a 4-bit number from our ALU.

**The Build:**
1.  **Layout:** Place four of your Gated D-Latch modules side-by-side.
2.  **The Data Bus:** The 4-bit output bus from your ALU (from Module 9) will connect to the `D` inputs of your four latches. Bit 0 of the ALU goes to the `D` input of Latch 0, and so on.
3.  **The Control Line:** All four `WE` (Write Enable) inputs are connected together and controlled by a single new lever labeled **"STORE"** or **"WRITE TO MEMORY"**.
4.  **The Output:** The four `Q` outputs from the latches form a new 4-bit bus: the Memory Bus. Connect this bus to your Hex Display system.

**The Final Integration Test:**
This is the moment it all comes together.
1.  **Perform a calculation:** Set Input B to `0101` (5) and Input B to `0110` (6). Set your ALU control panel to `ADD`. The ALU output is now `1011` (11), and the display shows `B`.
2.  **Store the result:** Flip the **"STORE"** lever ON for a moment, then turn it OFF. The D-Latches have now "seen" the `1011` from the ALU and have latched onto it. The display still shows `B`.
3.  **Change the inputs:** Now, change Input A and B to `0001` and `0010`. The ALU now calculates `1+2=3`, but our display is still connected to the Memory Bus.
4.  **The Payoff:** The display *still shows `B`*. It has remembered the previous result, completely independent of what the ALU is currently doing. You have successfully built working computer memory (RAM)!

---

#### **Module 10 Checkpoint**

*   **Quiz:**
    1.  What is the key difference between a combinational circuit and a sequential circuit? (Sequential circuits have memory/state).
    2.  What is the purpose of the "Write Enable" line on a Gated D-Latch?
    3.  In an RS Latch, what happens if both Set and Reset are 0? (It holds its previous value).

*   **Real-World Connection: RAM**
    > The D-Latch you built is the fundamental building block of **Static RAM (SRAM)**. SRAM is a very fast type of memory used for a CPU's cache because it holds its value as long as it has power. The main system memory in your computer (DRAM) works on a slightly different principle but is still based on the idea of storing a charge to represent a `1` or a `0`. Every time you save a file or a game, you are using millions of circuits just like the one you built.

**Module 10 Conclusion:**
Our computer can now not only calculate but also remember. This is the last major hardware component we need. We have an input system, a processor (ALU), a memory (Register), and an output system (Display). All that's left is to make them work together automatically. In the next module, we'll give our machine its heartbeat and its conductor, turning it from a manually operated calculator into a true, self-running computer.
