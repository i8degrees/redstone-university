### Module 2: The Language of Logic – A Deep Dive into Boolean Algebra

---

#### Module Summary

-   **Narrative Beat:** We've built our keyboard, but to make the computer *think*, we need to learn its grammar. This isn't a Minecraft lesson; this is the fundamental language of all digital electronics. Welcome to Boolean Algebra.
-   **Learning Goals:**
    -   Move beyond physical blocks to understand the formal, abstract language that governs all digital circuits.
    -   Understand *why* circuits work the way they do, and how to design and simplify them on paper before ever placing a block.
-   **Lesson Overview:**
    -   Lesson 2.1: The Rules of Thought
    -   Lesson 2.2: The Core Operators (The Verbs of Logic)
    -   Lesson 2.3: The Laws of Logic & The Power of Simplification
    -   Lesson 2.4: The Special Operator – XOR
    -   Lesson 2.5: Software Superpowers – The XOR Trick for Programmers
    -   Lesson 2.6: The Negated Gates – NAND, NOR, and XNOR
    -   Lesson 2.7: Module 2 Checkpoint
-   **Minecraft Artifact:** A set of working Redstone logic gates (NOT, AND, OR, XOR, NAND, NOR, XNOR).

---

#### Module Introduction

*For our build philosophy and the story behind this course, see the [main course introduction](../README.md).*

---

Welcome back to Redstone University!

In our last module, we built a physical way to speak to our computer in binary. We have our keyboard, a set of four simple levers. But right now, those levers are connected to nothing. Our machine can't yet *understand* or *do* anything with the numbers we give it. It can hear us, but it doesn't know the language.

In this module, we're going to give our computer a mind. We're going to take a crucial journey into theory to learn the fundamental grammar of all digital logic. This isn't just a Minecraft lesson; this is the language that powers every computer chip ever made.

Welcome to Boolean Algebra.

---

#### Lesson 2.1: The Rules of Thought

> **Key Takeaway:** Boolean algebra gives us a precise language for describing and manipulating logical statements, which is the foundation of all digital circuits.

In the mid-1800s, a mathematician named George Boole developed a new kind of algebra. Unlike the algebra you might know from school, where variables like `x` and `y` can be any number, Boole's variables were much simpler. They could only have two possible values: **True** or **False**.

This system, now called **Boolean Algebra**, was initially a mathematical curiosity. But a century later, when engineers started building the first electronic computers with on/off switches, they realized Boole had already invented the perfect mathematical system to describe them.

-   **The Core Idea:** We'll treat our Redstone signals as Boolean variables.
-   A powered Redstone line is **True**. We'll also call this `1`.
-   An unpowered Redstone line is **False**. We'll also call this `0`.

Boolean algebra gives us a set of rules and operators to manipulate these True/False values. These physical operators are called **logic gates**, and they are the bedrock (pun intended) of all computation.

---

#### Lesson 2.2: The Core Operators (The Verbs of Logic)


##### **How We Describe Each Gate**

To ensure a complete understanding, every logic gate is introduced using a consistent structure that moves from the abstract concept to the practical build.

-   **Visual Introduction:**

    -   **Abstract Symbol & Function:** We begin with an image showing the gate's standard engineering symbol alongside a simple circuit demonstrating its basic function.
    -   **Composite Diagram (For Composite Gates Only):** For gates built from our primitives, we then show a detailed CircuitVerse diagram of how they are constructed using only NOT and OR gates.
    -   **Minecraft Build:** Finally, we show a screenshot of the gate built in Minecraft, reflecting our "primitives-only" design philosophy.

-  **Formal Definition & Rules:**

    -   **Formal Definition:** The high-level concept and official terminology (e.g., "Conjunction").
    -   **Symbols:** Common ways the operator is written in logic (`∧`) and programming (`&&`).
    -   **The Rule:** A plain-English sentence describing what the gate does.
    -   **Truth Table:** A complete chart defining all possible input/output combinations. This is the ultimate "source of truth."
    -   **Primitive Boolean Expression:** The specific algebraic expression that represents our composite build using only `NOT` and `OR`.

 -   **Practical Application:**

     -   **Lab & Experiment:** A hands-on test to verify your Minecraft build against the gate's truth table.
     -   **Real-World Connection:** An example of where this logic is used in real technology.

---

##### A Note on Our Primitives

In the world of computer science, you can build any logic gate from a small set of "primitive" gates. For this course, our primitives are dictated by the game mehanis of Minecraft itself. The game gives us two logical operations right out of the box:

1.  **NOT:** A Redstone Torch naturally inverts a signal. This is our primitive NOT gate.
2.  **OR:** Redstone Dust naturally merges signals. If any line powering a central wire is ON, the whole wire becomes ON. This is our primitive OR gate.

From these two building blocks, **NOT** and **OR**, we will construct every other logic gate in our computer. This approach shows you how even the most complex digital machines can be built from the simplest possible parts.

While in real-world electronics, gates like NAND or NOR are often used as universal gates due to their efficiency in hardware, we choose NOT and OR for their intuitiveness and direct correspondence to Minecraft's Redstone system.

---

##### Operator 1: NOT (The Inverter) - A Minecraft Primitive

> **Key Takeaway:** The NOT gate flips a signal, turning ON to OFF, or 1 to 0. It’s the simplest way to create “opposite” logic in a circuit.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOT-gate_circuitverse.png" alt="NOT Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the NOT gate (left) and its function in a basic circuit (right), taking a single input A and producing an inverted output Y.</em></div></br></br>

-   **Formal Definition:** The NOT gate, or Inverter, performs **Negation**. It's the simplest possible operation: it takes a single input and outputs its exact opposite.
-   **Symbols:** `¬A` (logic), `!A` (programming).
-   **The Rule:** If the input is `True`, the output is `False`. If the input is `False`, the output is `True`.
-   **Truth Table: NOT Gate**
    | `A` | `!A` |
    |:---:|:----:|
    |  0  |  1   |
    |  1  |  0   |
-   **The Boolean Expression:** The output `Y` is simply `Y = !A`.

-   **Lab & Experiment:**

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOT-gate_minecraft.png" alt="NOT Gate in Minecraft" width="512px"/><br/><em>Figure: A NOT gate implemented in Minecraft using a Redstone Torch. The torch inverts the input from the lever, turning the lamp on when the lever is off and vice versa. This is the simplest physical realization of logical negation in the game.</em></div></br></br>

    > **Note:** The Redstone Torch itself is a physical NOT gate, but we will add some lamps and dust just to help visualize everything better. Feel free to use a simple torch moving forward if you prefer.

    1.  Build the circuit as shown in the Minecraft screenshot:

        1.  Place a redstone lamp with a lever on one side to represent input `A`.
        2.  On the backside of the lamp, place a redstone torch. This is the core component of the NOT gate.
        3.  From the torch, run a line of redstone dust to another redstone lamp representing output `Y`.

        > **Note:** The torch itself is the critical component of the NOT gate. The extra lamps and dust are just for visualization.

    2.  Test the circuit:

        1.  Set lever A to ON (1). Observe that the lamp is OFF (0).
        2.  Set lever A to OFF (0). Observe that the lamp is ON (1).

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

##### Operator 2: OR (The "At Least One" Gate) - A Minecraft Primitive

> **Key Takeaway:** The OR gate outputs 1 if at least one input is 1. It’s how we express “either/or” logic in hardware and software.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_OR-gate_circuitverse.png" alt="OR Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the OR gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active if at least one input is active.</em></div></br></br>


-   **Formal Definition:** The OR gate performs **Disjunction**. Think of it as the optimistic gate; it checks if *at least one* of its inputs is True.
-   **Symbols:** `A ∨ B` (logic), `A || B` (programming).
-   **The Rule:** The output is `True` if `A` is True, OR `B` is True, or if both are True.
-   **Truth Table: OR Gate**
  | `A` | `B` | `A OR B` |
  |:---:|:---:|:--------:|
  |  0  |  0  |    0     |
  |  0  |  1  |    1     |
  |  1  |  0  |    1     |
  |  1  |  1  |    1     |
-   **The Boolean Expression:** The output `Y` is `Y = A OR B`.
-   **Lab & Experiment:**
    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_OR_gate_minecraft.png" alt="OR Gate in Minecraft" width="512px"/><br/><em>Figure: A Minecraft OR gate built by merging two Redstone Dust lines. The output lamp lights up if either lever (input A or B) is switched on, visually demonstrating the "at least one" logic of the OR operation.</em></div></br></br>

    1.  Build the circuit as shown in the Minecraft screenshot:

        1.  Place two redstone lamps with at least one space between them.
        2.  Place a lever on each lamp (these represent inputs `A` and `B`).
        3.  On the other side of each lamp, place a redstone repeater facing away to act as a diode.
        4.  Run dust lines from each repeater and merge them into a single output line.
        5.  Connect this line to another redstone lamp for output `Y`.

    2.  **Engineering Note:** When building this OR gate, you might notice that merging dust lines directly from the lamps without repeaters can cause "back-powering." Powering one lamp might light the other, even if its lever is off. The repeaters prevent this by acting as diodes, letting signals flow out but not back in.
    3.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    4.  **Verification:** Confirm the output lamp matches the truth table for each test.

-   **Real-World Connection:** A security system might sound an alarm if `FrontDoorSensor=True` OR `BackDoorSensor=True`.

---

##### Practice Problem: Boolean Expression Evaluation

Given the Boolean expression `A OR !B`, evaluate the output for all possible input combinations (A, B = 0,0; 0,1; 1,0; 1,1) and create a truth table. Then, build a Minecraft circuit to verify your results.

<details>
<summary><strong>Solution: Boolean Expression Evaluation</strong></summary>

**Truth Table for A OR !B**:

| A | B | !B | A OR !B |
|---|---|----|---------|
| 0 | 0 |  1 |    1    |
| 0 | 1 |  0 |    0    |
| 1 | 0 |  1 |    1    |
| 1 | 1 |  0 |    1    |

**Minecraft Circuit**: Use a lever for A, a lever for B, a redstone torch on B’s block for !B, merge A and !B with dust for OR, and connect to a lamp for output. Test all combinations to verify.
</details>

---

##### Operator 3: AND (The "Strict" Gate) - Our First Composite Gate

> **Key Takeaway:** The AND gate only outputs 1 if all its inputs are 1. It’s how we require multiple conditions to be true at once.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_AND-gate_circuitverse.png" alt="AND Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the AND gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active only if inputs A and B are both active.</em></div></br></br>

Now we reach our first **composite gate**. Unlike NOT and OR, Minecraft does not give us a single block that performs the AND operation. Instead, we must build it from our primitives. This is a fundamental concept in digital engineering: combining simple components to create more complex functions. Our chosen primitives (NOT and OR) are *functionally complete*, meaning any possible logic function, including AND, can be built from them.

To connect the abstract concept of a gate to our physical build, we will use a consistent visual format. Each composite gate will be introduced with its standard, abstract symbol, which is how engineers represent it in high-level diagrams. This will be followed by a detailed composite diagram showing how to construct it from our primitive NOT and OR gates. In these diagrams, a dashed outline will enclose the group of primitives, visually demonstrating how they work together to become equivalent to the single, abstract gate.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_AND-gate-composite_circuitverse.png" alt="AND Gate Composite in CircuitVerse" width="512px"/><br/><em>Figure: The AND gate constructed from NOT and OR gates in CircuitVerse. This composite diagram shows how two NOT gates and one OR gate are grouped to function as a single AND gate, following the logic Y = !(!A OR !B).</em></div></br></br>

- **Formal Definition:** The AND gate performs **Conjunction**. It’s the strict gate: output is True only if *all* inputs are True.
- **Symbols:** `A ∧ B` (logic), `A && B` (programming).
- **The Rule:** The output is `True` only if `A` is True AND `B` is True.
- **Truth Table: AND Gate**
  | `A` | `B` | `A AND B` |
  |:---:|:---:|:---------:|
  |  0  |  0  |     0     |
  |  0  |  1  |     0     |
  |  1  |  0  |     0     |
  |  1  |  1  |     1     |
- **The Boolean Expression:** The output `Y` is `Y = A AND B`. (Our build uses `!(!A OR !B)`, which we’ll prove equivalent in Lesson 2.3.)
- **Lab & Experiment:**
    > **Note on Screenshots and Color Coding:**
    > Our Minecraft circuit screenshots use a pseudo-isometric view to show as much of the build as possible. However, it can sometimes be hard to tell if a redstone torch is attached to the backside of a block. To make this clear, any block with a torch on its backside is colored red in the screenshot. Blocks with torches only on top are easy to see, so they use the build’s default color unless they also have a backside torch, in which case they’re red. For redstone lamps used as inputs (with a lever on one side and a torch or repeater on the other), we can't color code them obviously, but the instructions clearly indicate when a torch is on the backside of one of these input blocks.

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_AND-gate-composite_minecraft.png" alt="AND Gate Composite in Minecraft" width="512px"/><br/><em>Figure: A composite AND gate in Minecraft, constructed using two Redstone Torches (NOT gates) and a Redstone Dust merger (OR gate), then inverted again. This build demonstrates how to achieve AND logic using only the game's primitive components.</em></div></br></br>

    1.  Build the verbose version as shown:

        1.  Place two redstone lamps with a lever on the front of each for inputs `A` and `B`.
        2.  Attach a redstone torch to the back of each redstone lamp to create the NOT gates for `!A` and `!B`.
        3.  Merge these signals to a central point with redstone dust. This creates an OR gate: `!A OR !B`.
        4.  Places a solid block and run the redstone dust into the back of the block.
        5.  Invert this signal by placing a redstone torch on the opposite side of the block. This final NOT gate gives us `!(!A OR !B)`.
        5.  Connect the output to a lamp for `Y`.

    3.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    4.  **Verification:** The output lamp lights only when both levers are ON.

-   **Real-World Connection:** A missile launch might need `TurnKey1=True` AND `PressButton=True`.

##### Practice Problem: Logic Gate Design Challenge

Design a circuit that implements the logic `A AND !B` using only the NOT and OR primitives (no direct AND gate). Build it in Minecraft and verify with a truth table.

<details>
<summary><strong>Solution: A AND !B Circuit</strong></summary>

**Truth Table for A AND !B**:

| A | B | !B | A AND !B |
|---|---|----|----------|
| 0 | 0 |  1 |    0     |
| 0 | 1 |  0 |    0     |
| 1 | 0 |  1 |    1     |
| 1 | 1 |  0 |    0     |

**Boolean Expression**: `A AND !B = !(!A OR B)` (by De Morgan’s Law).

**Minecraft Circuit**: Invert A to get !A. Then, take !A and the original B and feed them into an OR gate. Finally, invert the result of that OR gate.
</details>

---
#### Lesson 2.3: The Laws of Logic & The Power of Simplification

> **Key Takeaway:** Boolean laws let us simplify complex circuits and expressions, making our designs more efficient and easier to understand.

Just like `2 + x = x + 2` in normal algebra, Boolean algebra has laws that let us rearrange and simplify expressions. For us, **a simpler expression means a smaller, faster, and more reliable Redstone circuit.** This is a critical engineering skill.


##### Boolean Notation: Logical vs Arithmetic
You’ll often see logic written using symbols from regular math. For example, **AND** is sometimes written as multiplication (`A · B` or `AB`), **OR** as addition (`A + B`), and **NOT** as an overbar (`Ā`).

For this course, we will use a specific convention designed for maximum clarity:
 -   We will use the words **`AND`** and **`OR`** in our expressions, as they are unambiguous.
 -   For **negation**, we will use the exclamation mark (**`!`**), as in **`!A`**. This is the standard symbol used in many programming languages and keeps our complex expressions clean and readable.

##### The Laws of Boolean Algebra
Here are the key laws we will be using in our course. There are many more, but these are the most fundamental and useful for circuit design.

-   **Identity Law:** `A OR 0 = A` and `A AND 1 = A`.
-   **Annihilator Law:** `A OR 1 = 1` and `A AND 0 = 0`.
-   **De Morgan's Law:** This is the superstar. It gives us a way to convert between ANDs and ORs.
    -   `!(A AND B)` is the same as `!A OR !B`
    -   `!(A OR B)` is the same as `!A AND !B`

---

##### **Lab 1: Proving a Circuit with De Morgan's Law**

Let’s use De Morgan’s Law to prove our AND gate design is correct.

1.  The two redstone torches on the back of our redstone lamps are NOT gates, giving us `!A` and `!B`.
2.  Their signals merge into the central spot, which is an OR gate (`!A OR !B`).
3.  The final output torch is a NOT gate on that signal. Therefore, the full expression for our circuit is `!(!A OR !B)`.
4.  Applying De Morgan’s Law to the part in the parentheses: `!A OR !B` is the same as `!(A AND B)`.
5.  Substituting that back in, our expression becomes `!(!(A AND B))`.
6.  The two NOTs (`!!`) cancel each other out, leaving `A AND B`. We just proved our physical circuit is correct!

---

##### **Lab 2: Proving a Circuit with the Distributive Law**

The laws of logic don't just prove that a circuit is correct; they can also make our circuits much simpler. This is a crucial engineering skill called **simplification**.

Consider a circuit that needs to turn on if `(A is ON and B is ON)` OR if `(A is ON and B is OFF)`. The direct Boolean expression would be:

`Y = (A AND B) OR (A AND !B)`

This looks like it would require two AND gates and one OR gate. Let's use the laws of logic to simplify it.

1.  **Start with the expression:** `Y = (A AND B) OR (A AND !B)`
2.  **Apply the Distributive Law:** Notice that `A AND` is common to both terms. We can "factor it out."
    *   This gives us: `Y = A AND (B OR !B)`
3.  **Apply the Inverse Law:** We know that an input OR'd with its own inverse (`B OR !B`) is always equal to `1` (True).
    *   The expression becomes: `Y = A AND 1`
4.  **Apply the Identity Law:** We know that any input AND'd with `1` is just itself.
    *   The final expression is: `Y = A`

**Lab Takeaway:** We have just proven that this entire three-gate circuit can be replaced by a single wire connected to input `A`. This is the power of simplification in action. It saves resources, space, and makes our designs more elegant.

---

##### Summary Table: Boolean Laws

| Law Name | Example(s) | Description |
|---|---|---|
| Identity | `A OR 0 = A`<br>`A AND 1 = A` | Leaves value unchanged |
| Annihilator | `A OR 1 = 1`<br>`A AND 0 = 0` | Output is always 1 (OR) or 0 (AND) |
| Idempotent | `A OR A = A`<br>`A AND A = A` | Repeating input doesn't change output |
| Inverse | `A OR !A = 1`<br>`A AND !A = 0` | Input and its ! always produce 1 (OR) or 0 (AND)|
| Commutative | `A OR B = B OR A`<br>`A AND B = B AND A` | Order doesn't matter |
| Associative | `(A OR B) OR C = A OR (B OR C)`<br>`(A AND B) AND C = A AND (B AND C)` | Grouping doesn't matter |
| Distributive | `A AND (B OR C) = (A AND B) OR (A AND C)` | AND distributes over OR |
| De Morgan's Laws | `!(A AND B) = !A OR !B`<br>`!(A OR B) = !A AND !B` | Converts between AND/OR with ! |

---

##### Functional Completeness: Building with Universal Gates

| Universal Gate | To Build a NOT Gate (`!A`) | To Build an AND Gate (`A AND B`) | To Build an OR Gate (`A OR B`) |
| :--- | :--- | :--- | :--- |
| **NAND** | `A NAND A` | `(A NAND B) NAND (A NAND B)` | `(A NAND A) NAND (B NAND B)` |
| **NOR** | `A NOR A` | `(A NOR A) NOR (B NOR B)` | `(A NOR B) NOR (A NOR B)` |

**Why does this matter?**

For real-world chip designers, this is an incredibly powerful concept. Manufacturing a computer chip is a complex process. Instead of needing separate, specialized machinery to produce AND, OR, and NOT gates, a factory can be optimized to produce just *one* type of gate (like a NAND gate) in massive quantities with extreme reliability and low cost.

Engineers then use the patterns from the table above to wire those identical simple gates together to create all the complex logic they need. The simplicity of manufacturing a single universal gate is a cornerstone of modern, affordable electronics.

##### Practice Problem: Circuit Simplification Challenge

Given the expression `(A OR B) AND (!A OR !B)`, simplify it using Boolean laws and build the simplified circuit in Minecraft.

<details>
<summary><strong>Solution: Simplifying (A OR B) AND (NOT A OR NOT B)</strong></summary>

**Simplification Steps:**
1. Start with `(A OR B) AND (!A OR !B)`.
2. Apply De Morgan’s Law to the second term: `!A OR !B = !(A AND B)`.
3. The expression becomes `(A OR B) AND !(A AND B)`.
4. Distribute: `(A AND !(A AND B)) OR (B AND !(A AND B))`.
5. Simplify each term:
   - `A AND !(A AND B) = A AND (!A OR !B) = (A AND !A) OR (A AND !B) = 0 OR (A AND !B) = A AND !B`.
   - Similarly, `B AND !(A AND B) = B AND !A`.
6. Final expression: `(A AND !B) OR (!A AND B)`, which is `A XOR B`.

**Minecraft Circuit**: Build the XOR circuit from Lesson 2.4, as it’s equivalent. Compare it to the original, which requires more blocks and dust.
</details>

---

#### Lesson 2.4: The Special Operator – XOR

> **Key Takeaway:** XOR outputs 1 only when its inputs are different. It’s essential for circuits like adders and programming tricks.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XOR-gate_circuitverse.png" alt="XOR Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the Exclusive OR (XOR) gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active only if the inputs are different.</em></div></br></br>

Like the AND gate, XOR is a composite gate. For all gates we show the asbtract symbol used in diagrams as we introduce them, but we will continue our practice of building it from our established primitives. Here is a version of an XOR gate built from OR and NOT, our minecraft primitives.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XOR-gate-composite_circuitverse.png" alt="XOR Gate in (Composite) CircuitVerse" width="512px"/><br/><em>Figure: The XOR gate constructed in CircuitVerse using only OR and NOT gates. This composite design highlights how the XOR function can be achieved by creatively wiring together these basic primitives.</em></div></br></br>

It's important to understand that this is just one of many ways to build an XOR gate. In Redstone engineering, as in real-world circuit design, there is often no single "correct" answer. Different designs might be bigger but easier to understand, or smaller but more complex. The design above is excellent for visualizing the underlying logic while learning.

-   **Formal Definition:** The **Exclusive OR (XOR)** gate outputs True only when inputs differ.
-   **Symbols:** `A ⊕ B` (logic), `A ^ B` (programming).
-   **The Rule:** The output is `True` if `A` is True and `B` is False, or vice versa; it’s `False` if inputs are the same.
-   **Truth Table: XOR Gate**

    | `A` | `B` | `A XOR B` |
    |:---:|:---:|:---------:|
    | 0 | 0 | 0 |
    | 0 | 1 | 1 |
    | 1 | 0 | 1 |
    | 1 | 1 | 0 |

-   **The Boolean Expression**: `Y = !(A OR !(A OR B)) OR !(B OR !(A OR B))`.

    > **A Note on Design Equivalence**: This powerful expression is a direct translation of our circuit diagram. It cleverly uses a shared NOR gate to feed the main logic paths, a common strategy in circuit design for efficiency. We haven't officially introduced NOR gates, but since it is simply a negated OR gate you can look at it as an `OR` gate followed by a `NOT` gate. I went with this design, because it avoids crossing wires while requiring only our primitives.

    > While it looks very different from the textbook definition, we can prove with a truth table that it is functionally exactly the same. This is a perfect example of how different engineering approaches can lead to the same correct solution. There is always more than one way to build a gate!

-   **Lab & Experiment:**

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XOR-gate-composite_minecraft.png" alt="XOR Gate (Composite) in Minecraft" width="512px"/><br/><em>Figure: A composite XOR gate in Minecraft, built by combining Redstone Dust (OR logic) and Redstone Torches (NOT logic). The output lamp lights only when the two input levers are set to different states, illustrating the exclusive nature of XOR.</em></div></br></br>

    1.  Build the XOR gate as shown in the screenshot:

        1.  Place two redstone lamps with a lever on the front of each for inputs `A` and `B`
        2.  Build the shared `OR` Gate `(A OR B)` by running lines of redstone dust from both inputs `A` and `B` through a repeater each into a single point. This gate will be shared by both inputs.
        3.  Negate the `OR` gate we just built by running the merged line of redstone dust into a solid block. Now place a torch on the opposite side of the block. `!(A OR B)`
        4.  Now we will create our main logic paths with two more negated `OR` gates

            - **Left Path `!(A OR !(A OR B))`:

                - This `OR` gate takes inputs from Input A and from the negated `OR` gate we built in steps 1-3.
                - From the merge point of this `OR` Gate run the redstone in to another solid block.
                - Place a torch on the far side of this second block. The output from this torch is now the entire left half of our boolean expression.

            - **Right Path `!(B OR !(A OR B))`:

                - Mirror the left path. Create a third OR gate by running a line of dust directly from input B and another line from the same shared NOR torch's output.
                - Merge these two lines into a third solid block.
                - Place a torch on the far side of this third block. The output from this torch is the complete right half of our boolean expression.

        5.  Run a line of dust from each torch of the last two `OR` gates we built and merge them creating a final `OR` gate.
        6.  Connect this final `OR` gate merge point to the output lamp `Y`.

-   **Real-World Connection:** XOR is used in adders, error detection, and two-switch light systems (light toggles if one switch changes).

##### Practice Problem: Two-Switch Light System

Design a Minecraft circuit for a two-switch light system where flipping either switch toggles the light’s state (on to off, or off to on). Use only NOT and OR gates to implement the XOR logic.

<details>
<summary><strong>Solution: Two-Switch Light System</strong></summary>

**Logic:** The light should be ON when exactly one switch is ON (A XOR B).

**Truth Table:**

| A | B | Light (A XOR B) |
|---|---|-----------------|
| 0 | 0 |        0        |
| 0 | 1 |        1        |
| 1 | 0 |        1        |
| 1 | 1 |        0        |

**Minecraft Circuit:** Build the XOR circuit from Lesson 2.4 (using NOT and OR gates). Connect levers for A and B, and a lamp for the output. Test by flipping each lever and verifying the lamp toggles.
</details>

---

#### **Lesson 2.5: Software Superpowers – The XOR Trick for Programmers**

> **Key Takeaway:** XOR is a “secret weapon” in programming. Its reversible, self-canceling property allows for incredibly efficient solutions to common algorithmic problems.

**Why is XOR so useful in programming?**

The XOR gate has two magical properties that programmers exploit constantly:
1.  Any number XORed with itself is zero: `x ^ x = 0`.
2.  Any number XORed with zero is itself: `x ^ 0 = x`.

Because of these rules, XOR is reversible and "cancels itself out." This allows for brilliant solutions to problems that seem complex at first glance. This is where our hardware knowledge directly translates into writing efficient software.

Let's see it in action with a classic problem from programming interview sites like LeetCode.

**Example Problem: The "Single Number"**

> *   **The Challenge:** You are given a list of numbers where every number appears exactly twice, except for one number that appears only once. Find that unique number.
> *   **Example List:** `[4, 1, 2, 1, 2]`
> *   **The XOR Solution:** If you XOR all the numbers in the list together, every number that appears twice will cancel itself out and become zero. The only number left at the end will be the unique one! `4 ^ (1 ^ 1) ^ (2 ^ 2)` becomes `4 ^ 0 ^ 0`, which is `4`.

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Your Turn: The "Missing Number" Challenge**

Now that you've seen how the XOR trick works, try applying the same core principle to solve a different, but related, problem.

> **The Challenge:**
>
> You are given a list of numbers that contains every number from `0` to `n` exactly once, except for one number which is missing. Your task is to find that missing number.
>
> -   **Example List:** `nums = [3, 0, 1]`
> -   In this example, `n` would be 3. The full range of numbers should be `[0, 1, 2, 3]`. The missing number is `2`.
>
> **The Hint:**
> Think about the two groups of numbers you're dealing with: the list you *have* and the complete list you *should have*. How can you use XOR's self-canceling property to find the single difference between these two groups?

<br>

<details>
<summary><strong>Click here for the solution and explanation</strong></summary>

---

**The Logic:**

The core idea is to XOR all the numbers that *should* be in the list against all the numbers that *are* actually in the list.

1.  First, we calculate the XOR sum of the complete sequence of numbers from 0 to `n`. For our example `[3, 0, 1]`, `n` is 3, so this would be `0 ^ 1 ^ 2 ^ 3`.
2.  Next, we calculate the XOR sum of the numbers in the list we were given: `3 ^ 0 ^ 1`.
3.  If we XOR these two results together, all the numbers that are present in both lists will pair up and cancel out, leaving only the number that was missing from the input list.

`(0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)` can be rearranged as `(0^0) ^ (1^1) ^ (3^3) ^ 2`, which simplifies to `2`.

**The Python Code:**

```python
def missingNumber(nums):
    n = len(nums)
    expected_xor_sum = 0
    for i in range(n + 1):
        expected_xor_sum ^= i

    actual_xor_sum = 0
    for num in nums:
        actual_xor_sum ^= num

    return expected_xor_sum ^ actual_xor_sum
```

</details>

---

#### Lesson 2.6: The Negated Gates – NAND, NOR, and XNOR

> **Key Takeaway:** Negated gates combine basic operations with NOT. NAND and NOR are “functionally complete.” You can build anything with just one of them!

##### Operator 4: NAND (The "Not Both" Gate)

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NAND-gate_circuitverse.png" alt="NAND Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the NAND gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active unless both inputs A and B are active.</em></div></br></br>

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NAND-gate-composite_circuitverse.png" alt="NAND Gate (Composite) in CircuitVerse" width="512px"/><br/><em>Figure: A composite NAND gate in CircuitVerse, constructed using only OR and NOT gates. This diagram shows how the NAND function can be achieved by inverting the output of a composite AND gate built from these primitives, without using a dedicated AND gate block.</em></div></br></br>

-   **Formal Definition:** The NAND gate performs a **NOT-AND** operation (negation of AND).
-   **Symbols:** `A NAND B` or `¬(A ∧ B)`.
-   **The Rule:** The output is `True` unless both inputs are `True`.
-   **Truth Table: NAND Gate**
    | `A` | `B` | `A NAND B` |
    |:---:|:---:|:----------:|
    | 0 | 0 | 1 |
    | 0 | 1 | 1 |
    | 1 | 0 | 1 |
    | 1 | 1 | 0 |
-   **The Boolean Expression:** `Y = !A OR !B`

    > **A Note on De Morgan's Law in Action**: This is one of the most powerful tricks in digital logic. We know that NAND is !(A AND B). We also know from De Morgan's Law that !(A AND B) is perfectly equivalent to !A OR !B. Our composite AND gate was built as !(!A OR !B). To create a NAND gate, we simply remove the final ! (the last torch), which leaves us with the physical circuit for !A OR !B. This is a perfect physical proof of a fundamental logic law!

-   **Lab & Experiment:**

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NAND-gate-composite_minecraft.png" alt="NAND Gate in Minecraft" width="512px"/><br/><em>Figure: A NAND gate in Minecraft, constructed by modifying the composite AND gate and tapping the output before the final inversion. The output lamp turns off only when both input levers are on, matching the NAND truth table.</em></div></br></br>

    1.  Build the NAND gate:

        1.  Start by building our composite AND gate from Lesson 2.2.
        2.  To get the NAND output, remove the final torch.
        3.  The signal on the dust before that final torch is now your output. Connect this dust to the output lamp for Y. The lamp will now behave exactly like a NAND gate.

    2.  Test all four combinations from the truth table.
    3.  **Verification:** The output is `0` only when both inputs are `1`.

-   **Real-World Connection:** NAND gates are key in hardware (e.g., memory circuits) due to their functional completeness.

##### Operator 5: NOR (The "Neither" Gate)

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOR-gate_circuitverse.png" alt="NOR Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the NOR gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active only if both inputs A and B are inactive.</em></div></br></br>

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOR-gate-composite_circuitverse.png" alt="NOR Gate (Composite) in CircuitVerse" width="512px"/><br/><em>Figure: A composite NOR gate in CircuitVerse, constructed using only OR and NOT gates. The output is high only when both inputs are low, demonstrating NOR logic using our primitive gates.</em></div></br></br>

-   **Formal Definition:** The NOR gate performs a **NOT-OR** operation (negation of OR).
-   **Symbols:** `A NOR B` or `¬(A ∨ B)`.
-   **The Rule:** The output is `True` only when both inputs are `False`.
-   **Truth Table: NOR Gate**
    | `A` | `B` | `A NOR B` |
    |:---:|:---:|:---------:|
    | 0 | 0 | 1 |
    | 0 | 1 | 0 |
    | 1 | 0 | 0 |
    | 1 | 1 | 0 |
-   **The Boolean Expression:** The output `Y` is `Y = !(A OR B)`.
-   **Lab & Experiment:**

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOR-gate_minecraft.png" alt="NOR Gate in Minecraft" width="512px"/><br/><em>Figure: A NOR gate in Minecraft, created by merging two Redstone Dust lines (OR logic) and then inverting the result with a Redstone Torch. The output lamp lights up only when both input levers are off, demonstrating the NOR operation.</em></div></br></br>

    1.  Build the NOR gate:

        1.  Build the OR gate as in Lesson 2.2.
        2.  Between the merged dust and the output lamp, place a block with a torch on the output side to invert the signal.
        3.  Make sure the dust still connects everything to the output lamp for `Y`.

    2.  Test all four combinations from the truth table.
    3.  **Verification:** The output is `1` only when both inputs are `0`.

-   **Real-World Connection:** NOR gates are used in logic circuits needing a “neither” condition and are also functionally complete.

##### Operator 6: XNOR (The "Equality Detector")

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XNOR-gate_circuitverse.png" alt="XNOR Gate in CircuitVerse" width="512px"/><br/><em>Figure: The abstract symbol for the Exclusive NOR (XNOR) gate (left) and its function in a basic circuit (right), taking two inputs A and B and producing an output Y that is active only if the inputs are the same.</em></div></br></br>

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XNOR-gate-composite_circuitverse.png" alt="XNOR Gate (Composite) in CircuitVerse" width="512px"/><br/><em>Figure: Composite XNOR gate in CircuitVerse, constructed using only OR and NOT gates. This diagram shows how XNOR logic can be achieved by inverting one input to a composite XOR gate built from these primitives, demonstrating the equivalence between XOR(A, NOT B) and XNOR(A, B).</em></div></br></br>

-   **Formal Definition:** The XNOR gate performs a **NOT-XOR** operation (negation of XOR).
-   **Symbols:** `A XNOR B` or `¬(A ⊕ B)`.
-   **The Rule:** The output is `True` when inputs are the same (both `True` or both `False`).
-   **Truth Table: XNOR Gate**
        | `A` | `B` | `A XNOR B` |
        |:---:|:---:|:----------:|
        | 0 | 0 | 1 |
        | 0 | 1 | 0 |
        | 1 | 0 | 0 |
        | 1 | 1 | 1 |
-   **The Boolean Expression:** `Y = !( !(A OR !(A OR B)) OR !(B OR !(A OR B)) )`

-   **Lab & Experiment:**

    <div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XNOR-gate-composite_minecraft.png" alt="XNOR Gate (Composite) in Minecraft" width="512px"/><br/><em>Figure: An XNOR gate in Minecraft, constructed by adding a NOT gate to one input of a composite XOR gate. The output lamp lights up only when both input levers are set to the same state, visually confirming the XNOR truth table.</em></div></br></br>

    > **Verifying the Build: A Proof of Equivalence**
    >
    > We are building our XNOR gate using a fantastic shortcut: an XNOR gate is functionally identical to an XOR gate if you just invert one of its inputs (`XOR(A, !B)`).
    >
    > How can we prove this using only our primitive gates?
    >
    > 1.  The expression for `XNOR(A, B)` is the **logical negation** of our entire complex XOR expression
    > 2.  The expression for `XOR(A, !B)` is our entire complex XOR expression, but with every `B` replaced by `!B`.
    >
    > While the direct algebraic proof is incredibly long, we can use a **truth table** to verify it. If you trace all four input combinations for both of these complex expressions, you will find they both produce the exact same final output column: `1, 0, 0, 1`. The trick works perfectly, even with our primitive-only design!

    1.  **Build the XNOR gate:**

        1.  First, build the complete **composite XOR gate** exactly as you did in Lesson 2.4.
        2.  Now, modify one of the inputs. We will invert input `B`.
        3.  Place a NOT gate on the input line for `B` before it enters the XOR circuit. The easiest way is to move the `B` lever back one block, place a torch on the back of the block the lever is on, and run the signal from that torch into the XOR gate's `B` input.
        4.  Ensure the dust from this new NOT gate correctly connects to the rest of the XOR circuit where the `B` input used to be.

    2.  Test all four combinations from the truth table (`0,0`, `0,1`, `1,0`, `1,1`).
    3.  **Verification:** The output is `1` only when the inputs are the same. You have successfully created an XNOR gate by modifying an XOR gate.

-   **Real-World Connection:** XNOR gates are used in equality checks, like comparators in computing.

##### Practice Problem: Universal Gate Challenge with NOR Gates

Build an AND gate using only NOR gates. Verify it with a truth table in Minecraft.

<details>
<summary><strong>Solution: AND Gate Using NOR Gates</strong></summary>

**Logic:** `A AND B = (A NOR A) NOR (B NOR B)`

**Truth Table:**

| A | B | A NOR A | B NOR B | (A NOR A) NOR (B NOR B) |
|---|---|---------|---------|-------------------------|
| 0 | 0 |    1    |    1    |            0            |
| 0 | 1 |    1    |    0    |            0            |
| 1 | 0 |    0    |    1    |            0            |
| 1 | 1 |    0    |    0    |            1            |

**Minecraft Circuit:** Build three NOR gates using redstone dust mergers and torches. Connect levers for A and B, and a lamp for the output. Test all combinations to verify AND behavior.
</details>

---

#### **Lesson 2.7: Module 2 Summary**

> You have reached the end of the learning portion of this module. You started with the basic idea of True and False and have now built a complete toolkit of the seven fundamental logic gates. You've learned how to describe them with truth tables and Boolean expressions, how to build them from our primitives, and how they connect to both real-world hardware and software.
>
> This summary table provides a single place to review all the gates at a glance.

##### **Logic Gates Summary Table**

|  Gate   |                       Symbol                             |             Core Logic Rule             |    Primitive Boolean Expression              |
| :------ | :---------------------------------------------------------------- | :-------------------------------------- | :--------------------------------------------|
| **!**   | <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOT.svg" alt="NOT Gate Symbol" width="64px">   | Inverts a single input.                 | `!A`                                         |
| **OR**  | <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_OR.svg" alt="OR Gate Symbol" width="64px">     | True if **at least one** input is True. | `A OR B`                                     |
| **AND** | <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_AND.svg" alt="AND Gate Symbol" width="64px">   | True only if **all** inputs are True.   | `!(!A OR !B)`                                |
| **XOR** | <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XOR.svg" alt="XOR Gate Symbol" width="64px">   | True only if inputs are **different**.  |`!(A OR !(A OR B)) OR !(B OR !(A OR B))`      |
| **NAND**| <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NAND.svg" alt="NAND Gate Symbol" width="64px"> | True unless **all** inputs are True.    | `!A OR !B`                                   |
| **NOR** | <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_NOR.svg" alt="NOR Gate Symbol" width="64px">   | True only if **all** inputs are False.  | `!(A OR B)`                                  |
| **XNOR**| <img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/02_XNOR.svg" alt="XNOR Gate Symbol" width="64px"> | True only if inputs are the **same**.   | `!(!(A OR !(A OR B)) OR !(B OR !(A OR B)))`  |

---

#### **Lesson 2.8: Module 2 Checkpoint**

> **Module Summary:** You have reached the end of the most theory-intensive module in this course. You began with simple on/off switches and have now mastered the seven fundamental logic gates, the Boolean laws that govern them, the power of simplification, and the bridge between hardware logic and software problem-solving. It is time to test your newfound knowledge.

This checkpoint is divided into three parts to test the different skills you've acquired:
*   **Part 1: Knowledge Check** - Quick questions to test your memory and understanding of core concepts.
*   **Part 2: Logic Puzzles** - "On-paper" challenges requiring you to apply the laws of Boolean algebra.
*   **Part 3: The Debug Challenge** - A practical, in-game challenge to test your troubleshooting skills.

---

##### Part 1: Knowledge Check

Test your core understanding with these rapid-fire questions.

1.  What is the key difference in the output of an OR gate versus an XOR gate?
2.  Which two gates are considered "universal," and what is the name of this property?
3.  Using De Morgan's Law, what is the equivalent expression for `!(A OR B)`?

<details>
<summary><strong>Click for answers</strong></summary>

1.  An **OR** gate outputs `1` if *at least one* input is `1`. An **XOR** gate outputs `1` only if the inputs are *different*.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is `!A AND !B`.

</details>

---

##### Part 2: Logic Puzzles

Apply the laws of Boolean algebra to solve these challenges on paper.

###### Puzzle 1: The Word Problem

A greenhouse has an automated climate control system. An alarm `Y` should sound if the following conditions are met:
*   The system is in "Manual Override" mode (`M` is `True`), **OR**
*   The Temperature `T` is too high **AND** the Water Sprinklers `W` have failed to turn on (`W` is `False`).

Write the single Boolean expression for the alarm `Y`.

<details>
<summary><strong>Click for the solution</strong></summary>

The expression translates directly from the requirements:

`Y = M OR (T AND !W)`

The parentheses are crucial to ensure the `AND` condition is evaluated before being `OR`'d with the manual override switch.

</details>

<br>

###### Puzzle 2: The Simplification

An engineer has designed a circuit with the expression: `Y = (A AND B) OR (A AND !B) OR (!A AND B)`.

This seems to require three AND gates and two OR gates. Simplify this expression to its most efficient form using Boolean laws.

<details>
<summary><strong>Click for the step-by-step proof</strong></summary>

1.  **Start with the expression:** `Y = (A AND B) OR (A AND !B) OR (!A AND B)`
2.  **Look for common terms to factor:** The first two terms both contain `A`. Let's factor it out using the Distributive Law.
    *   `A AND (B OR !B)`
3.  **Apply the Inverse Law:** We know that `B OR !B` is always `1`.
    *   So, the first part simplifies to `A AND 1`, which is just `A`.
4.  **Rewrite the expression:** Our expression is now much simpler: `Y = A OR (!A AND B)`
5.  **Apply the Distributive Law again (in a less obvious way):** The law `(X OR Y) AND (X OR Z) = X OR (Y AND Z)` can be applied here. Let `X = A`.
    *   We can expand `A OR (!A AND B)` into `(A OR !A) AND (A OR B)`.
6.  **Apply the Inverse Law again:** We know that `A OR !A` is always `1`.
    *   The expression becomes: `Y = 1 AND (A OR B)`
7.  **Apply the Identity Law:** `1 AND` anything is just the anything.
    *   The final, simplified expression is: `Y = A OR B`.

The entire complex circuit simplifies down to a single OR gate!

</details>

---

##### Part 3: The Debug Challenge (In-Game)

> In the world download for this module, you will find a section labeled "Module 2 Debug Challenge." I have built a circuit that is *supposed* to implement the logic for the greenhouse alarm from Part 2: `M OR (T AND !W)`.
>
> However, it's giving the wrong output for some input combinations! Your mission is to use your knowledge of truth tables and circuit tracing to diagnose the mistake in the Redstone wiring and fix it so it functions correctly. Good luck!

---

#### Module 2 Conclusion

This was a huge module! But you now have the most powerful tool an engineer can possess: a formal language to describe, design, and simplify complex systems. You know the "verbs" of logic, have built them from Minecraft's true primitives, and seen how that physical logic directly empowers elegant software solutions.

**What’s Next:** Now that you can “think in logic,” you’re ready to build circuits that translate, display, and process information. In the next module, we'll use this newfound language to build our first truly complex and useful machine: a translator that will let our computer speak to us.


> **A Note on the Following Optional Interlude**
> You have successfully completed Module 2. Congratulations!
> Before you move on to the next project, we have a special, optional section called an "Interlude." In this module, we focused on building for clarity, making our gates large so the logic was easy to see. The Interlude introduces the art of building for efficiency and compact design.
> Think of it as your first engineering deep-dive. You can read it now, or you can come back to it at any time. The choice is yours.

---

#### Key Terms (Module 2)

-   **Boolean Algebra:** A branch of mathematics for working with true/false values (1/0), using operators like AND, OR, and NOT.
-   **Logic Gate:** A physical or virtual device that implements a Boolean operation.
-   **Primitive Gate:** A basic, indivisible logic gate from which more complex gates are built. In our course, these are NOT and OR.
-   **Composite Gate:** A logic gate constructed by combining primitive gates (e.g., an AND gate built from NOT and OR gates).
-   **Truth Table:** A chart showing all possible input/output combinations for a logic gate or circuit.
-   **Functionally Complete:** A set of gates from which any Boolean function can be built (e.g., just NAND or just NOR).
-   **Bitwise Operation:** A software operation that manipulates individual bits of a number.
-   **XOR (Exclusive OR):** Outputs 1 if inputs are different; used in both hardware and software for unique logic tricks.
