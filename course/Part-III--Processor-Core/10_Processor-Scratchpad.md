## Module 10: The Processor's Scratchpad – Building a Register

### Module 10 Summary

-   **Narrative Beat:** Our ALU is a powerful but forgetful brain. It can perform a calculation, but the result vanishes instantly. We need to give it a "sticky note", a memory register, to hold a number temporarily.
-   **Learning Goals:**
    -   Understand the difference between "stateless" combinational circuits and "stateful" sequential circuits.
    -   Learn how a feedback loop can create a 1-bit memory cell, the Gated D-Latch.
    -   Construct a 4-bit Memory Register by grouping latches together.
-   **Lesson Overview:**
    -   Lesson 10.1: The Theory – From Stateless to Stateful
    -   Lesson 10.2: The Lab – Building a 4-Bit Register
-   **Minecraft Artifact:** A functional 4-bit register that can store a single number.

---

### Module 10 Introduction

You have just completed the magnificent centerpiece of our machine: the ALU. It is a powerful calculator, but it has a critical flaw, it has the memory of a goldfish. As soon as you change the inputs, the previous result is gone forever.

A computer isn't truly useful if it can't remember things. To perform multi-step calculations or run a program, a processor needs a place to store its results temporarily.

In this module, we will build that place. We will explore the concept of "state" and create our first **sequential circuit**, a circuit that can remember. We'll start with the fundamental 1-bit memory cell, the **Gated D-Latch**, and then combine four of them to build a 4-bit **Memory Register**. This register will act as our ALU's scratchpad, the first and most crucial piece of memory in our computer.

---

### Lesson 10.1: The Theory – From Stateless to Stateful

> **Key Takeaway:** By creating a "feedback loop" where a gate's output is fed back into its own input, we can create a sequential circuit that holds its state, forming the basis of all computer memory.

So far, all the circuits we've built are **combinational**. This means their output depends *only* on their current inputs. An AND gate's output is determined solely by what its inputs are *right now*. Change the inputs, and the output instantly changes, with no memory of what came before.

To build memory, we need a **sequential** circuit. Its output depends not just on the current inputs, but also on its *previous state*. We need to create a circuit that can get "stuck" in a `` `1` `` or `` `0` `` state, even after the input that put it there is gone. The way we achieve this is with a **feedback loop**.

#### The Gated D-Latch: A Controllable Memory Cell

The fundamental building block of our register is the **Gated D-Latch**. It's a simple, 1-bit memory circuit with two inputs and one output:
-   **$D$ (Data):** The 1-bit value (`` `1` `` or `` `0` ``) that we want to store.
-   **$WE$ (Write Enable):** A control signal that tells the latch when to save.
-   **$Q$ (Output):** The 1-bit value that the latch is currently storing.

**The Rule:**
-   When the $WE$ signal is ON, the latch is "transparent." The output $Q$ will immediately copy the input $D$.
-   The moment $WE$ turns OFF, the latch "closes" and holds onto the last value it saw on the $D$ input, ignoring any further changes to $D$.

This circuit allows us to choose the exact moment we want to "save" a bit of data.

<div align="center"><img src="./images/gated-d-latch-circuitverse.png" alt="Gated D-Latch CircuitVerse Diagram" width="512px"/><br/><em>Figure: A Gated D-Latch constructed from basic gates. The Write Enable (WE) line controls AND gates that act as gatekeepers, allowing the Data (D) input to affect the underlying memory loop only when WE is active.</em></div><br/>

---

### Lesson 10.2: The Lab – Building a 4-Bit Register

> **Key Takeaway:** A 4-bit register is simply four 1-bit D-Latches placed side-by-side, with their Write Enable lines connected to a single, shared control signal.

Now that we understand the 1-bit memory cell, scaling it up to store our 4-bit numbers is easy.

#### Lab & Experiment

1.  **Build a 1-Bit Gated D-Latch:** First, construct and test a single D-Latch module based on the diagram from the previous lesson. Verify that it correctly stores a bit when you pulse the $WE$ lever.
2.  **Layout the Register:** Build four copies of your Gated D-Latch module side-by-side.
3.  **Wire the Data Bus:** Create a 4-bit input bus that will eventually come from our ALU's output. Connect each wire of this bus to the corresponding $D$ input of your four latches.
4.  **Wire the Control Line:** Connect all four $WE$ (Write Enable) inputs together. This single, shared wire will be controlled by a new lever labeled **`STORE`**.
5.  **Wire the Output:** The four $Q$ outputs from the latches form a new 4-bit bus: the **Memory Bus**.

<div align="center"><img src="./images/4-bit-register-minecraft.png" alt="4-Bit Register Minecraft Build" width="512px"/><br/><em>Figure: A 4-bit memory register in Minecraft, constructed from four Gated D-Latch modules. The single STORE line enables all four latches simultaneously, allowing a 4-bit number to be saved.</em></div><br/>

#### The Final Integration Test

This is the moment it all comes together.
1.  **Connect the ALU:** Wire the 4-bit result output from your ALU (from Module 9) to the 4-bit data input of your new register.
2.  **Connect the Display:** Wire the 4-bit output of the register (the Memory Bus) to the input of your Hex Display system from Module 5.
3.  **Perform a calculation:** Set the inputs to your ALU to calculate, for example, `$9+2$`. The ALU will output `` `1011` `` ($B$).
4.  **Store the result:** Pulse the **`STORE`** lever ON for a moment, then turn it OFF. The D-Latches have now "seen" the `` `1011` `` from the ALU and have latched onto it. Your display should show a `$B$`.
5.  **Change the inputs:** Now, change the ALU's inputs to calculate something else, like `$1+2=3$`. The ALU is now outputting `` `0011` ``, but your display is no longer connected to the ALU.
6.  **The Payoff:** The display **still shows `$B$`**. It has remembered the previous result, completely independent of what the ALU is currently doing. You have successfully built a working computer memory!

---

### Module 10 Conclusion

Excellent work. Our computer can now not only calculate but also remember. This is the first and most essential step in creating a machine that can execute multi-step processes. You have built a "scratchpad" where our ALU can store its results.

This single register is a huge milestone, but it's not enough for a real computer that needs to store a whole program. In the next module, we will take the register you've just perfected and scale it up into a full "notebook" with 16 addressable pages, building our Random Access Memory (RAM).

---

### Module 10 Checkpoint

#### Practice Problem 10.3.1: Knowledge Check
1. What is the key difference between a combinational circuit and a sequential circuit?
2. What is the purpose of a "feedback loop" in memory circuits?
3. What is the role of the "Write Enable" line on a Gated D-Latch?

<details>
<summary><strong>Show Solution</strong></summary>
1. A **combinational** circuit's output depends only on its current inputs. A **sequential** circuit's output depends on its current inputs *and* its previous state (it has memory).
2. A feedback loop, where a gate's output is connected back to its input, is what allows a circuit to hold its state and "remember" a value even after the initial input is gone.
3. The "Write Enable" line acts as a gatekeeper. When it is ON, the latch is "open" and copies its data input. When it is OFF, the latch is "closed" and holds its current value, ignoring the data input.
</details>

#### Practice Problem 10.3.2: The RS Latch
The circuit that forms the core of our D-Latch is often an **RS Latch**, built from two cross-coupled NOR gates. It has two inputs: $S$ (Set) and $R$ (Reset). Pulsing $S$ forces the output $Q$ to `1`. Pulsing $R$ forces $Q$ to `0`. What do you think happens if you pulse both $S$ and $R$ at the same time? Why might this be considered an "invalid" or "forbidden" state?

<details>
<summary><strong>Show Solution</strong></summary>
If both $S$ and $R$ inputs on a NOR-based RS Latch are set to `1`, both NOR gates will be forced to output `0`. This means both the $Q$ and $\neg Q$ outputs would be `0`, which violates the rule that they must be opposites. When the inputs are then returned to `0`, the latch enters an unpredictable "race condition," and it's impossible to know what state it will settle in. This is why the Gated D-Latch is a safer, more predictable design.
</details>

#### Key Terms
- **Combinational Logic**: A type of digital circuit whose output is purely a function of its present inputs only.
-   **Feedback Loop**: A circuit design where an output from a gate is fed back into its own input path, creating a stateful circuit that can hold a value.
-   **Gated D-Latch**: A 1-bit memory circuit that copies its Data ($D$) input to its output ($Q$) when the Write Enable ($WE$) signal is active, and holds its state when $WE$ is inactive.
-   **Register**: A group of latches that work together to store a multi-bit number. A 4-bit register is composed of four 1-bit latches.
-   **Sequential Logic**: A type of digital circuit whose output depends on the sequence of previous inputs, not just the current ones. It has memory.
-   **State**: The condition of a circuit at a particular time, representing the data it is currently storing.
