## Module 7: Comparators and Status Flags – The Dawn of Decision-Making

### Module 7 Summary

-   **Narrative Beat:** Our machine can calculate, but it can't make decisions. To program it to think, it needs to be able to ask questions: "Is this result zero?" We'll build the fundamental circuits that allow for comparison and create "flags" to store the answers, giving our machine a primitive form of awareness.
-   **Learning Goals:**
    -   Understand the difference between a simple calculator and a computer that can make decisions.
    -   Build a 4-bit equality comparator using XNOR and AND gates.
    -   Learn how status flags (like the Zero Flag and Negative Flag) are the hardware foundation for `if` statements in programming.
    -   Build the logic circuits for the Zero Flag and the Negative Flag.
-   **Lesson Overview:**
    -   Lesson 7.1: From Calculation to Computation
    -   Lesson 7.2: The Equality Comparator
    -   Lesson 7.3: The Art of Awareness – An Introduction to Status Flags
    -   Lesson 7.4: Building the Flag Logic
-   **Minecraft Artifact:** A single component featuring a 4-bit equality comparator and a 2-bit flag register that indicates "Zero" and "Negative" conditions.

---

### Module 7 Introduction

Excellent work on building the core arithmetic circuits of our machine. It can now add and subtract, but it's still just a very sophisticated calculator. It can tell you that `$5 - 5 = 0$`, but it has no idea what that *means*. It cannot react to that result.

This module marks the most important leap in our entire course. We are going to bridge the gap between simple **calculation** and true **computation**.

The difference is **decision-making**.

In this module, we will give our machine the gift of awareness. We will build the hardware that allows it to ask questions about the numbers it processes. First, we'll construct a dedicated circuit to compare two numbers directly. Then, we will build the circuits for **status flags**, the real secret to how computers work. These flags are the physical foundation for every `if` statement and `while` loop in all of programming.

By the end of this module, you won't just have a few more circuits. You will have built the hardware that allows a machine to think.

---

### Lesson 7.1: From Calculation to Computation

> **Key Takeaway:** A computer's power comes not just from performing calculations, but from its ability to make decisions based on the results of those calculations.

So far, our machine operates on a linear path: you provide input, you tell it what to do (like "add"), and you get an output. It follows our instructions blindly.

But a useful program needs to be able to change its behavior based on what's happening.
- "If the player's health is `0`, then display the 'Game Over' screen."
- "While the enemy count is greater than `0`, keep the battle music playing."

These are **conditional statements**. They are the heart of all programming and all complex behavior. To make these statements possible, a machine needs the physical ability to answer questions. It needs hardware that can perform **comparisons**. This module is dedicated to building that hardware.

---

### Lesson 7.2: The Equality Comparator

> **Key Takeaway:** We can determine if two binary numbers are equal by checking if every pair of corresponding bits is the same, a task perfectly suited for XNOR gates.

The simplest question a computer needs to ask is, "Are these two things the same?" Before we learn the ultra-efficient way a real CPU does this, we'll build a dedicated "brute-force" circuit to understand the core logic.

#### The Theory

How do we know if two 4-bit numbers, $A$ and $B$, are equal?
- $A = 1011$
- $B = 1011$

We know they are equal because the bit in the `$8$`s place is the same for both, **AND** the bit in the `$4$`s place is the same, **AND** the bit in the `$2$`s place is the same, **AND** the bit in the `$1$`s place is the same.

We already have the perfect tool for this job: the **XNOR gate**, our "equality detector" from Module 3. It outputs a `1` only when its two inputs are identical. The blueprint for our comparator is simple:
1.  Use four XNOR gates, one for each pair of bits ($A_0$ and $B_0$, $A_1$ and $B_1$, etc.).
2.  Feed the outputs of all four XNOR gates into a single 4-input AND gate.

The final output of that AND gate will only be `1` if *all four* XNOR gates report that their bits were a match.

---

#### Lab & Experiment: Building the 4-Bit Equality Comparator

![4-Bit Equality Comparator CircuitVerse Diagram](./images/comparator-circuitverse.png)
*Figure: The logic for a 4-bit equality comparator. Each pair of bits ($A_i$, $B_i$) is checked by an XNOR gate, and a 4-input AND gate confirms that all pairs are identical.*

1.  **Build the circuit:** Construct the circuit as shown in the diagram. You will need two 4-bit input buses ($A$ and $B$) and a single output lamp, labeled "$A = B$".
2.  **Test for Equality:** Set both input $A$ and input $B$ to the same value, for example, `` `1010` ``. The "$A = B$" lamp should turn ON.
3.  **Test for Inequality:** Change just a single bit on either input. For example, change input $B$ to `` `1011` ``. The "$A = B$" lamp should immediately turn OFF.

![4-Bit Equality Comparator Minecraft Build](./images/comparator-minecraft.png)
*Figure: The 4-bit equality comparator built in Minecraft. The two 4-bit inputs are at the back, and the single output lamp at the front is lit, indicating the inputs are currently equal.*

You have now built a working comparator circuit! While useful, this dedicated hardware isn't how a real CPU usually handles comparison. In the next lesson, we'll learn the more elegant and powerful method.

---

### Lesson 7.3: The Art of Awareness – An Introduction to Status Flags

> **Key Takeaway:** A CPU doesn't just output a numerical answer; it also outputs a set of "status flags" that describe the properties of that answer, enabling efficient decision-making.

The comparator we just built is great, but it's inefficient. A real CPU uses a more clever approach. The ALU performs a single mathematical operation (like subtraction), and then it sets a few single-bit flags to create a "report" on the result. This small group of flags is stored in the **Status Register**.

This is the universal translator between arithmetic and logic. By performing a subtraction and simply checking the flags that result, the computer can know if the original numbers were equal, or if one was greater than the other. This is how every `if` statement you have ever written is physically implemented.

We are going to build the logic for the two most important flags:

1.  **The Zero Flag (Z):** The Z flag is set to `1` if the result of the last operation was `0000`. This is how computers check for equality. The software instruction `` `if (x == y)` `` is actually executed by the hardware as `$x - y$` and then checking if the **Zero Flag is `1`**.

2.  **The Negative Flag (N):** The N flag is set to `1` if the most significant bit of the result is `1`. This is how computers check for negative numbers, relying on the Two's Complement system we learned in Module 6. The software instruction `` `if (x < 0)` `` is a direct check of the **Negative Flag**.

By building these flags, we are building the physical foundation of all conditional logic.

---

### Lesson 7.4: Building the Flag Logic

> **Key Takeaway:** The logic required to detect the Zero and Negative flags is surprisingly simple, yet it unlocks the most powerful capabilities of our computer.

#### The Theory

-   **The Zero Flag (Z):** A 4-bit number $Y$ is `` `0000` `` only if all its bits are `0`. This logic, $\text{NOT}(Y_3 \lor Y_2 \lor Y_1 \lor Y_0)$, is the exact function of a **4-input NOR gate**.
-   **The Negative Flag (N):** A 4-bit number is negative if its sign bit (the MSB) is `1`. The logic is a direct copy: $N = Y_3$. The "circuit" is just a wire.

---

#### Lab & Experiment: Building the Flag Register

![Flag Logic CircuitVerse Diagram](./images/flag-logic-circuitverse.png)
*Figure: The logic for our 2-bit flag register. A 4-input NOR gate detects the zero condition, while a simple wire taps the MSB for the negative condition.*

1.  **Build the Zero Flag Circuit:**
    1.  Create a 4-bit input bus (this will eventually come from our ALU's output).
    2.  Build a 4-input NOR gate connected to this bus.
    3.  Connect the output to a lamp labeled "Zero Flag (Z)".
    4.  Test it: The lamp should only be ON when all four input levers are set to `` `0` ``.
2.  **Build the Negative Flag Circuit:**
    1.  Using the same 4-bit input bus, run a single wire from the most significant bit ($Y_3$, the `$8$`s place).
    2.  Connect this wire directly to a lamp labeled "Negative Flag (N)".
    3.  Test it: The lamp should be ON if and only if the `$8$`s place lever is ON.

![Flag Register Minecraft Build](./images/flag-register-minecraft.png)
*Figure: The flag logic circuits in Minecraft. The Z flag lamp is lit because the input is `0000`. The N flag lamp is off.*

---

### Module 7 Conclusion

Excellent work. You have now built the fundamental decision-making circuits for our computer. The machine can now not only calculate, but it can also generate metadata *about* those calculations in the form of status flags. This is the crucial gift of awareness that separates a simple calculator from a thinking machine.

You now have all the logical and comparison components ready. In the next modules, we will build the final piece of the puzzle, the multiplexer, before we forge everything into our complete Arithmetic Logic Unit.

---

### Module 7 Checkpoint

#### Practice Problem 7.5.1: Knowledge Check
1. Why are status flags generally more efficient than dedicated comparator circuits in a real CPU?
2. What calculation would a CPU perform to check if `$A > B$`? What flag would it look at?
3. What is the logic gate used to create the Zero Flag circuit?

<details>
<summary><strong>Show Solution</strong></summary>
1. Status flags allow the CPU to get many pieces of information (zero, negative, carry, overflow) from a single arithmetic operation (like subtraction), rather than needing separate, bulky hardware for every possible comparison.
2. It would calculate `$B - A$`. If the **Negative Flag** is `1`, it means the result was negative, which means that $A$ must have been greater than $B$.
3. A **NOR** gate.
</details>

#### Practice Problem 7.5.2: Design Challenge
Design a circuit that detects if a 4-bit number is the specific value `` `1111` `` (`15` decimal). What single logic gate can accomplish this?

<details>
<summary><strong>Show Solution</strong></summary>
To check if all four bits ($Y_3, Y_2, Y_1, Y_0$) are `1`, you would need a single **4-input AND gate**. Its output will only be `1` if all of its inputs are `1`.
</details>

#### Key Terms

-   **Comparator**: A digital circuit that compares two binary numbers and outputs a signal indicating the result of that comparison (e.g., equal, greater than, etc.).
-   **Flag**: A single bit stored in a status register that holds information about the result of the most recent ALU operation.
-   **Most Significant Bit (MSB)**: The bit in a binary number with the largest place value, which is used as the sign bit in Two's Complement representation.
-   **Status Register**: A collection of flag bits within a CPU that stores the status of the processor and information about the outcome of the last operation.
-   **Zero Flag (Z)**: A status flag that is set to `1` if the result of an operation is zero, and `0` otherwise. It is the primary mechanism for testing equality.
-   **Negative Flag (N)**: A status flag that is set to `1` if the result of an operation is negative (i.e., its MSB is `1`), and `0` otherwise.
