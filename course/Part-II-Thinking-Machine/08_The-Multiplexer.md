---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Module 8: The Multiplexer – The Digital Switch

## Module 8 Summary

* **Narrative Beat:** We have components that can add, subtract, and compare, but our computer has no way to choose between them. Before we can build the final processor, we must first build its "steering wheel", the Multiplexer, a circuit that lets us select which data path to use.
* **Learning Goals:**
  * Understand the theory and practical application of a Multiplexer (MUX) as a digital selector switch.
  * Build a 1-bit 2-to-1 MUX from basic logic gates.
  * Scale that design up to a 4-bit MUX that will be used in our ALU.
* **Lesson Overview:**
  * Lesson 8.1: The Theory – The Power of Choice
  * Lesson 8.2: The Lab – Building a 1-Bit MUX
  * Lesson 8.3: The Lab – Scaling Up to a 4-Bit MUX
* **Minecraft Artifact:** A functional, 4-bit 2-to-1 MUX.

***

## Module 8 Introduction

You've built an impressive collection of specialized circuits. You have components that can add, subtract, and perform logical comparisons. Now we face a new problem: if all of these circuits are operating in parallel, how do we choose _which result_ we want to use at any given moment?

This module introduces the solution: the **Multiplexer (MUX)**.

A multiplexer is a digital "selector switch." It's like the channel selector on a TV, allowing us to choose one of many input signals to send to a single output. This is the "steering wheel" for our processor, allowing us to route data and select the result of a specific operation. It is the final component we need before we can assemble our entire collection of circuits into the grand centerpiece of our machine: the Arithmetic Logic Unit.

***

## Lesson 8.1: The Theory – The Power of Choice

> **Key Takeaway:** A Multiplexer uses a "select" signal to choose which of its data inputs to pass through to its single output, using AND gates as controllable "gatekeepers."

Imagine you have two different video streams, $A$ and $B$, but only one screen, $Y$. You need a selector switch, $S$. The rule is simple: if the switch $S$ is set to `0`, the screen $Y$ should show stream $A$. If $S$ is set to `1`, the screen $Y$ should show stream $B$.

A **2-to-1 Multiplexer** is the perfect hardware for this. It has two data inputs ($A$ and $B$), one select input ($S$), and one data output ($Y$).

How can we build this with logic gates? We use AND gates as "gatekeepers" and an OR gate to combine their outputs.

1. One gatekeeper checks: $A \text{ AND } (\text{NOT } S)$ ($A \land \neg S$). This gate's output will be equal to $A$ only when $S$ is `0`. Otherwise, its output is `0`.
2. The other gatekeeper checks: $B \text{ AND } S$ ($B \land S$). This gate's output will be equal to $B$ only when $S$ is `1`. Otherwise, its output is `0`.
3. We combine the results with an OR gate. At any time, only one of the AND gates can be letting a signal through, so the OR gate simply passes on the selected input.

The full Boolean expression for a 2-to-1 MUX is: $Y = (A \land \neg S) \lor (B \land S)$

Let's trace the logic:

* If $S=0$: The expression becomes $(A \land \neg 0) \lor (B \land 0)$, which simplifies to $(A \land 1) \lor 0$, which is just $A$. The output is $A$!
* If $S=1$: The expression becomes $(A \land \neg 1) \lor (B \land 1)$, which simplifies to $(A \land 0) \lor B$, which is just $B$. The output is $B$!

The logic is sound. We can build a digital switch from simple gates.

***

## Lesson 8.2: The Lab – Building a 1-Bit MUX

> **Key Takeaway:** A 1-bit MUX is a direct physical implementation of the Boolean expression $Y = (A \land \neg S) \lor (B \land S)$.

### Lab & Experiment

![1-Bit MUX CircuitVerse Diagram](images/1-bit-mux-circuitverse.png)\
&#xNAN;_&#x46;igure: The logic diagram for a 1-bit 2-to-1 MUX. The select line S (and its inverse) controls which of the two AND gates allows its data input (A or B) to pass through to the final OR gate._\


1. **Inputs:** Create three levers for inputs $A$, $B$, and $S$ (Select).
2. **Logic:**
   * Build one AND gate. Its inputs are $A$ and $\neg S$ (the $S$ lever run through a NOT gate).
   * Build a second AND gate. Its inputs are $B$ and $S$.
   * Take the outputs from both AND gates and feed them into an OR gate.
3. **Output:** Connect the final OR gate's output to a Redstone Lamp, $Y$.
4. **Test the circuit:**
   * Set $S$ to `` `0` ``. Flip $A$ on and off; the output lamp $Y$ should exactly copy $A$. $B$ should have no effect.
   * Set $S$ to `` `1` ``. Flip $B$ on and off; the output lamp $Y$ should exactly copy $B$. $A$ should have no effect.

![1-Bit MUX Minecraft Build](images/1-bit-mux-minecraft.png)\
&#xNAN;_&#x46;igure: A 1-bit 2-to-1 MUX in Minecraft. The Select lever (center) is currently set to \`0\`, so the output lamp's state is being controlled by input A (left), while input B (right) is ignored._\


***

## Lesson 8.3: The Lab – Scaling Up to a 4-Bit MUX

> **Key Takeaway:** A 4-bit MUX is simply four 1-bit MUXes placed side-by-side, all controlled by the same shared select line.

Our computer works with 4-bit numbers, so we need a MUX that can select between two 4-bit buses. This sounds complex, but the solution is elegantly simple: we just build **four 1-bit MUXes** and run them in parallel. The crucial part is that the **Select ($S$) line is shared**. The same $S$ lever controls all four MUXes simultaneously, so they all switch in perfect unison.

### Lab & Experiment

1. **Inputs:** You'll have two 4-bit input buses (Bus A and Bus B) and one single Select lever ($S$).
2. **The MUX Array:** Build four copies of the 1-bit MUX circuit you created in the previous lesson.
3. **Wiring:**
   * Connect the four $A$ inputs of your MUXes to the four wires of Bus A.
   * Connect the four $B$ inputs of your MUXes to the four wires of Bus B.
   * Connect the single $S$ lever (and its inverter $\neg S$) to the $S$ inputs of _all four_ MUXes.
4. **Output:** The four $Y$ outputs from your MUXes form a new 4-bit bus, which is your final result.
5. **Test the circuit:**
   * Set $S$ to `` `0` ``. The output bus should be an exact copy of Bus A.
   * Set $S$ to `` `1` ``. The output bus should be an exact copy of Bus B.

![4-Bit MUX Minecraft Build](images/4-bit-mux-minecraft.png)\
&#xNAN;_&#x46;igure: A 4-bit 2-to-1 MUX in Minecraft. It is four 1-bit MUXes stacked vertically. The single Select lever controls all four slices at once._\


***

## Module 8 Conclusion

You have now built one of the most fundamental control components in digital logic. This digital switch is the key that will unlock the full potential of our processor. With the ability to choose, we can now assemble all of our separate arithmetic and logic circuits into one unified, powerful, and versatile component. In the next module, we will do exactly that, building the grand centerpiece of our machine: the ALU.

***

## Module 8 Checkpoint

### Practice Problem 8.4.1: Knowledge Check

1. In plain English, what does a Multiplexer do?
2. If we want to build a MUX that can select between _four_ different 4-bit buses, how many select lines would we need?
3. What is the Boolean expression for a 2-to-1 MUX?

<details>

<summary><strong>Show Solution</strong></summary>

1\. A Multiplexer (or MUX) selects one of several data inputs and forwards it to a single output. 2. We would need \*\*two\*\* select lines. To represent four choices (0, 1, 2, 3), you need 2 bits (\`\` \`00\` \`\`, \`\` \`01\` \`\`, \`\` \`10\` \`\`, \`\` \`11\` \`\`). 3. $Y = (A \land \neg S) \lor (B \land S)$

</details>

### Practice Problem 8.4.2: The Demultiplexer

A **Demultiplexer (DEMUX)** does the opposite of a MUX. It takes one data input and routes it to one of many possible outputs, based on a select line. Sketch out a logic diagram for a 1-to-2 DEMUX with one data input ($D$), one select line ($S$), and two outputs ($Y\_0$ and $Y\_1$).

<details>

<summary><strong>Show Solution</strong></summary>

**Logic:**

* If $S=0$, then $Y\_0$ should equal $D$, and $Y\_1$ should be `0`. The expression is $Y\_0 = D \land \neg S$.
* If $S=1$, then $Y\_1$ should equal $D$, and $Y\_0$ should be `0`. The expression is $Y\_1 = D \land S$.

**Diagram:**

![1-to-2 DEMUX CircuitVerse Diagram](images/demux-circuitverse.png)\
&#xNAN;_&#x46;igure: A 1-to-2 DEMUX. The data input D is sent to two AND gates. The select line S (and its inverse) determines which of the AND gates opens to let the data through to its corresponding output._\


</details>

### Key Terms

* **Multiplexer (MUX)**: A digital circuit that selects one of several input signals and forwards the selected input into a single output line. It acts as a digital switch.
* **Select Line(s)**: The control input(s) to a MUX that determine which data input is passed to the output.
