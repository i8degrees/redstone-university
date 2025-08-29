## Module 2: The Grammar of Circuits – Foundational Logic Gates

### Module 2 Summary

-   **Narrative Beat:**  We have a language (binary), but no words. We need to learn the three fundamental "verbs" of logic—NOT, OR, and AND—that will allow us to form our first logical thoughts.
-   **Learning Goals:**
    -   Understand the role of Minecraft's primitive gates (NOT, OR).
    -   Master the concept of a truth table as the "source of truth" for a gate's function.
    -   Successfully build a composite gate (AND) from the established primitives.
-   **Lesson Overview:**
    -   Lesson 2.1: The Rules of Thought
    -   Lesson 2.2: The Primitives – Building NOT and OR Gates.
    -   Lesson 2.3: The First Composite Gate – Building an AND Gate.
    -   Module 2 Checkpoint

-   **Minecraft Artifact:** A working set of the three foundational logic gates: NOT, OR, and AND.

---

### Module 2 Introduction

*For our build philosophy and the story behind this course, see the [main course introduction](../README.md).*

Welcome back to Redstone University!

In our last module, we built an input interface to send binary numbers as a signal over `4` wires forming a bus. Now we’ll learn how to process that signal using Boolean algebra and logic gates.

In this module, we're going to give our computer a mind. We're going to take a crucial journey into theory to learn the fundamental grammar of all digital logic. This isn't just a Minecraft lesson; this is the language that powers every computer chip ever made.

Welcome to Boolean Algebra.

---

### Lesson 2.1: The Rules of Thought

> **Key Takeaway:** Boolean algebra gives us a precise language for describing and manipulating logical statements, which is the foundation of all digital circuits.

In the mid-1800s, a mathematician named George Boole developed a new kind of algebra. Unlike the algebra you might know from school, where variables like `x` and `y` can be any number, Boole's variables were much simpler. They could only have two possible values: **True** or **False** (sometimes written as `1` and `0`).

This system, now called **Boolean Algebra**, was initially a mathematical curiosity. But a century later, when engineers started building the first electronic computers with on/off switches, they realized Boole had already invented the perfect mathematical system to describe them.

-   **The Core Idea:** We'll treat our Redstone signals as Boolean variables.
-   A powered Redstone line is **True**. We'll also call this `1`.
-   An unpowered Redstone line is **False**. We'll also call this `0`.

Boolean algebra gives us a set of rules and operators to manipulate these True/False values. These physical operators are called **logic gates**, and they are the bedrock (pun intended) of all computation.

---

### Lesson 2.2: The Core Operators (The Verbs of Logic)


#### How We Describe Each Gate

To ensure a complete understanding, every logic gate is introduced using a consistent structure that moves from the abstract concept to the practical build.

**Visual Introduction:**

-   **Abstract Symbol & Function:** We begin with an image showing the gate's standard engineering symbol alongside a simple circuit demonstrating its basic function.
-   **Composite Diagram (For Composite Gates Only):** For gates built from our primitives, we then show a detailed CircuitVerse diagram of how they are constructed using only NOT and OR gates.
-   **Minecraft Build:** Finally, we show a screenshot of the gate built in Minecraft, reflecting our "primitives-only" design philosophy.

**Formal Definition & Rules:**

-   **Formal Definition:** The high-level concept and official terminology (e.g., "Conjunction").
-   **Symbols:** Common ways the operator is written in logic (`∧`) and programming (`&&`).
-   **The Rule:** A plain-English sentence describing what the gate does.
-   **Truth Table:** A complete chart defining all possible input/output combinations. This is the ultimate "source of truth."
-   **Primitive Boolean Expression:** The specific algebraic expression that represents our composite build using only `NOT` and `OR`.

**Practical Application:**

-   **Lab & Experiment:** A hands-on test to verify your Minecraft build against the gate's truth table.
-   **Real-World Connection:** An example of where this logic is used in real technology.

#### A Note on Our Primitives

In the world of computer science, you can build any logic gate from a small set of "primitive" gates. For this course, our primitives are dictated by the game mechanics of Minecraft itself. The game gives us two logical operations right out of the box:

1.  **NOT:** A Redstone Torch naturally inverts a signal. This is our primitive NOT gate.
2.  **OR:** Redstone Dust naturally merges signals. If any line powering a central wire is ON, the whole wire becomes ON. This is our primitive OR gate.

From these two building blocks, **NOT** and **OR**, we will construct every other logic gate in our computer. This approach shows you how even the most complex digital machines can be built from the simplest possible parts.

While in real-world electronics, gates like NAND or NOR are often used as universal gates due to their efficiency in hardware, we choose NOT and OR for their intuitiveness and direct correspondence to Minecraft's Redstone system.

---

#### Operator 1: NOT (The Inverter) - A Minecraft Primitive

> **Key Takeaway:** The NOT gate flips a signal, turning ON to OFF, or `1` to `0`. It’s the simplest way to create “opposite” logic in a circuit.

![NOT Gate in CircuitVerse](./images/NOT-gate_circuitverse.png)
*Figure: The abstract symbol for the NOT gate (left) and its function in a basic circuit (right), taking a single input A and producing an inverted output Y.*

-   **Formal Definition:** The NOT gate, or Inverter, performs **Negation**. It's the simplest possible operation: it takes a single input and outputs its exact opposite.
-   **Symbols:** `¬A` (logic), `!A` (programming).
-   **The Rule:** If the input is `True`, the output is `False`. If the input is `False`, the output is `True`.
-   **Truth Table: NOT Gate**
    | `A` | `!A` |
    |:---:|:----:|
    | `0` | `1`  |
    | `1` | `0`  |
-   **The Boolean Expression:** The output `Y` is simply `Y = !A`.

-   **Lab & Experiment:**

    ![NOT Gate in Minecraft](./images/NOT-gate_minecraft.png)
    *Figure: A NOT gate implemented in Minecraft using a Redstone Torch. The torch inverts the input from the lever, turning the lamp on when the lever is off and vice versa. This is the simplest physical realization of logical negation in the game.*


    1.  Build the circuit as shown in the Minecraft screenshot:

        1.  Place a redstone lamp with a lever on one side to represent input `A`.
        2.  On the backside of the lamp, place a redstone torch. This is the core component of the NOT gate.
        3.  From the torch, run a line of redstone dust to another redstone lamp representing output `Y`.

            > **Note:** The torch itself is the critical component of the NOT gate. The extra lamps and dust are just for visualization.

    2.  Test the circuit:

        1.  Set lever A to ON (`1`). Observe that the lamp is OFF (`0`).
        2.  Set lever A to OFF (`0`). Observe that the lamp is ON (`1`).

    3.  **Verification:** The physical results perfectly match the truth table. You've built a working inverter! The extra lamps and dust we added should help visualize the NOT gate's function, but remember that the torch itself is the core component.

-   **Real-World Connection:** NOT gates are used everywhere, from creating the oscillating signal in a computer's clock (a "heartbeat") to flipping bits for representing negative numbers, which we'll do in a later module!

-   **Software Connection:** The NOT operation is used in programming to invert a condition or toggle a flag. For example, in Python:
    ```python
    is_on = False
    if not is_on:
        print("The device is off.")
    ```
    Here, `not` is the software equivalent of a NOT gate.

---

#### Operator 2: OR (The "At Least One" Gate) - A Minecraft Primitive

> **Key Takeaway:** The OR gate outputs `1` if at least one input is `1`. It’s how we express “either/or” logic in hardware and software.

![OR Gate in CircuitVerse](./images/OR-gate_circuitverse.png)
*Figure: The abstract symbol for the OR gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active if at least one input is active.*


-   **Formal Definition:** The OR gate performs **Disjunction**. Think of it as the optimistic gate; it checks if *at least one* of its inputs is True.
-   **Symbols:** `A ∨ B` (logic), `A || B` (programming).
-   **The Rule:** The output is `True` if `A` is True, OR `B` is True, or if both are True.
-   **Truth Table: OR Gate**
  | `A` | `B` | `A OR B` |
  |:---:|:---:|:--------:|
  | `0` | `0` |    `0`   |
  | `0` | `1` |    `1`   |
  | `1` | `0` |    `1`   |
  | `1` | `1` |    `1`   |
-   **The Boolean Expression:** The output `Y` is `Y = A OR B`.
-   **Lab & Experiment:**
    ![OR Gate in Minecraft](./images/OR_gate_minecraft.png)
    *Figure: A Minecraft OR gate built by merging two Redstone Dust lines. The output lamp lights up if either lever (input A or B) is switched on, visually demonstrating the "at least one" logic of the OR operation.*

    1.  Build the circuit as shown in the Minecraft screenshot:

        1.  Place two redstone lamps with at least one space between them.
        2.  Place a lever on each lamp (these represent inputs `A` and `B`).
        3.  On the other side of each lamp, place a redstone repeater facing away to act as a diode.
        4.  Run dust lines from each repeater and merge them into a single output line.
        5.  Connect this line to another redstone lamp for output `Y`.

            > **Engineering Note: What is a diode?**
            > In electronics, a **diode** is a component that allows a signal to flow in only one direction, like a one-way valve or a turnstile for electricity. This property is essential for preventing signals from going where they aren't supposed to.
            >
            > In our OR gate, if we merge the dust lines directly, a signal from input `A` could travel backwards up the other wire and power input `B`'s lamp, even if `B`'s lever is off. This is called "back-powering."
            >
            > The **Redstone Repeater** is a perfect, purpose-built diode in Minecraft. Notice the small arrow on top of it, it will only allow a signal to pass in that direction. By placing a repeater on each input line, we ensure the signal can flow *out* towards the final lamp, but cannot flow *backwards* to interfere with the other input.

    2.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    3.  **Verification:** Confirm the output lamp matches the truth table for each test.

-   **Real-World Connection:** A security system might sound an alarm if `FrontDoorSensor=True` OR `BackDoorSensor=True`.

#### Practice Problem 2.2.1: Boolean Expression Evaluation

Given the Boolean expression $A \text{ OR } \text{NOT } B$ ($A \lor \neg B$), evaluate the output for all possible input combinations (`A`, `B` = `0,0`; `0,1`; `1,0`; `1,1`) and create a truth table. Then, build a Minecraft circuit to verify your results.

<details>
<summary><strong>Show Solution</strong></summary>

**Truth Table for $A \text{ OR } \text{NOT } B$ ($A \lor \neg B$):**

| A | B | !B | A OR !B |
| $A$ | $B$ | $\neg B$ | $A \lor \neg B$ |
|---|---|----|---------|
| `0` | `0` |  `1` |    `1`    |
| `0` | `1` |  `0` |    `0`    |
| `1` | `0` |  `1` |    `1`    |
| `1` | `1` |  `0` |    `1`    |

**Minecraft Circuit**: Use a lever for `A`, a lever for `B`, a redstone torch on `B`’s block for `!B`, merge `A` and `!B` with dust for OR, and connect to a lamp for output. Test all combinations to verify.
</details>

---

#### Operator 3: AND (The "Strict" Gate) - Our First Composite Gate

> **Key Takeaway:** The AND gate only outputs 1 if all its inputs are 1. It’s how we require multiple conditions to be true at once.

![AND Gate in CircuitVerse](./images/AND-gate_circuitverse.png)
*Figure: The abstract symbol for the AND gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active only if inputs A and B are both active.*

Now we reach our first **composite gate**. Unlike NOT and OR, Minecraft does not give us a single block that performs the AND operation. Instead, we must build it from our primitives. This is a fundamental concept in digital engineering: combining simple components to create more complex functions. Our chosen primitives (NOT and OR) are *functionally complete*, meaning any possible logic function, including AND, can be built from them.

To connect the abstract concept of a gate to our physical build, we will use a consistent visual format. Each composite gate will be introduced with its standard, abstract symbol, which is how engineers represent it in high-level diagrams. This will be followed by a detailed composite diagram showing how to construct it from our primitive NOT and OR gates. In these diagrams, a dashed outline will enclose the group of primitives, visually demonstrating how they work together to become equivalent to the single, abstract gate.

![AND Gate Composite in CircuitVerse](./images/AND-gate-composite_circuitverse.png)
*Figure: The AND gate constructed from NOT and OR gates in CircuitVerse. This composite diagram shows how two NOT gates and one OR gate are grouped to function as a single AND gate, following the logic Y = !(!A OR !B).*

- **Formal Definition:** The AND gate performs **Conjunction**. It’s the strict gate: output is True only if *all* inputs are True.
- **Symbols:** `A ∧ B` (logic), `A && B` (programming).
- **The Rule:** The output is `True` only if `A` is True AND `B` is True.
- **Truth Table: AND Gate**
  | `A` | `B` | `A AND B` |
  |:---:|:---:|:---------:|
  | `0` | `0` |     `0`   |
  | `0` | `1` |     `0`   |
  | `1` | `0` |     `0`   |
  | `1` | `1` |     `1`   |
- **The Boolean Expression:** The output `Y` is `Y = A AND B`. (Our build uses `!(!A OR !B)`, which we’ll prove equivalent in Lesson 2.3.)
- **Lab & Experiment:**
    > **Note on Screenshots and Color Coding:**
    > Our Minecraft circuit screenshots use a pseudo-isometric view to show as much of the build as possible. However, it can sometimes be hard to tell if a redstone torch is attached to the backside of a block. To make this clear, any block with a torch on its backside is colored red in the screenshot. Blocks with torches only on top are easy to see, so they use the build’s default color unless they also have a backside torch, in which case they’re red. For redstone lamps used as inputs (with a lever on one side and a torch or repeater on the other), we can't color code them obviously, but the instructions clearly indicate when a torch is on the backside of one of these input blocks.

    ![AND Gate Composite in Minecraft](./images/AND-gate-composite_minecraft.png)
    *Figure: A composite AND gate in Minecraft, constructed using two Redstone Torches (NOT gates) and a Redstone Dust merger (OR gate), then inverted again. This build demonstrates how to achieve AND logic using only the game's primitive components.*

    1.  Build the verbose version as shown:

        1.  Place two redstone lamps with a lever on the front of each for inputs `A` and `B`.
        2.  Attach a redstone torch to the back of each redstone lamp to create the NOT gates for `!A` and `!B`.
        3.  Merge these signals to a central point with redstone dust. This creates an OR gate: `!A OR !B`.
        4.  Place a solid block and run the redstone dust into the back of the block.
        5.  Invert this signal by placing a redstone torch on the opposite side of the block. This final NOT gate gives us `!(!A OR !B)`.
        6.  Connect the output to a lamp for `Y`.

    2.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    3.  **Verification:** The output lamp lights only when both levers are ON.

-   **Real-World Connection:** A missile launch might need `TurnKey1=True` AND `PressButton=True`.

#### Practice Problem 2.2.2: Logic Gate Design Challenge

Design a circuit that implements the logic $A \text{ AND } \text{NOT } B$ ($A \land \neg B$) using only the NOT and OR primitives (no direct AND gate). Build it in Minecraft and verify with a truth table for all input combinations (`A`, `B` = `0,0`; `0,1`; `1,0`; `1,1`).

<details>
<summary><strong>Show Solution</strong></summary>

**Truth Table for $A \text{ AND } \text{NOT } B$ ($A \land \neg B$):**

| A | B | !B | A AND !B |
| $A$ | $B$ | $\neg B$ | $A \land \neg B$ |
|---|---|----|----------|
| `0` | `0` |  `1` |    `0`     |
| `0` | `1` |  `0` |    `0`     |
| `1` | `0` |  `1` |    `1`     |
| `1` | `1` |  `0` |    `0`     |

**Boolean Expression**: $A \text{ AND } \text{NOT } B = \text{NOT } (\text{NOT } A \text{ OR } B)$ ($A \land \neg B = \neg(\neg A \lor B)$) (by De Morgan’s Law).

**Minecraft Circuit**: Invert `A` to get `!A`. Then, take `!A` and the original `B` and feed them into an OR gate. Finally, invert the result of that OR gate.
</details>


### Module 2 Checkpoint

#### Key Terms


### Module 2 Conclusion
