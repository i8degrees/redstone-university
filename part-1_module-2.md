### **Module 2: The Language of Logic - A Deep Dive into Boolean Algebra**

**(Learning Goals:** Move beyond physical blocks to understand the formal, abstract language that governs all digital circuits. To understand *why* circuits work the way they do, and how to design and simplify them on paper before ever placing a block.)

**(Narrative Beat:** "We've built our keyboard, but to make the computer *think*, we need to learn its grammar. This isn't a Minecraft lesson; this is the fundamental language of all digital electronics. Welcome to Boolean Algebra.")

#### **Lesson 2.1: The Rules of Thought**

In the mid-1800s, a mathematician named George Boole developed a new kind of algebra. Unlike the algebra you might have learned in school—where variables like `x` and `y` can be any number—Boole's variables were much simpler. They could only have two possible values: **True** or **False**.

This system, now called **Boolean Algebra**, was initially a mathematical curiosity. But a century later, when engineers started building the first electronic computers with on/off switches, they realized Boole had already invented the perfect mathematical system to describe them.

**The Core Idea:**
*   A powered Redstone line is **True**. We'll also call this `1`.
*   An unpowered Redstone line is **False**. We'll also call this `0`.

Boolean algebra gives us a set of rules and operators to manipulate these True/False values. These operators are called **logic gates**. Let's learn the three most fundamental ones.

---

#### **Lesson 2.2: The Three Core Operators (The Verbs of Logic)**

##### **Operator 1: NOT (The Inverter)**

The NOT gate is the simplest but most powerful. It does one thing: **it flips its input to the opposite value.**

*   **Formal Name:** Negation
*   **Symbol:** In logic, it's a `¬` symbol before a variable, like `¬A`. In programming and our course, we'll often use an exclamation point: `!A`.
*   **The Rule:** If the input is `True`, the output is `False`. If the input is `False`, the output is `True`.

**The Truth Table:**
A "truth table" is a simple chart that exhaustively lists every possible input and shows the resulting output. It's the ultimate way to define what a logic gate does.

| Input A | Output !A |
|:-------:|:---------:|
|    0    |     1     |
|    1    |     0     |

**The Minecraft Gate: The Redstone Torch**
The developers of Minecraft gave us a perfect, purpose-built NOT gate: the **Redstone Torch**.
1.  **The Lab:** Place a single block on the ground.
2.  Place a lever on its front. This is our input `A`.
3.  Place a Redstone Torch on the back of the block.
4.  Run a line of Redstone dust from the torch to a Redstone Lamp. This is our output `!A`.

**Experiment:**
*   With the lever OFF (input `A` = 0), the torch is ON, and the lamp is lit (output `!A` = 1).
*   Flip the lever ON (input `A` = 1). The block becomes powered, which *de-powers* the torch. The torch turns OFF, and the lamp goes dark (output `!A` = 0).

This physical device perfectly matches our truth table. The Redstone Torch *is* a NOT gate.

---

##### **Operator 2: OR (The "At Least One" Gate)**

The OR gate looks at two inputs and asks a simple question: **"Is at least one of these inputs True?"**

*   **Formal Name:** Disjunction
*   **Symbol:** In logic, `A V B`. In programming, `A || B`. We'll use `A OR B`.
*   **The Rule:** The output is `True` if input A is True, OR if input B is True, OR if both are True. The only way it's `False` is if both inputs are `False`.

**The Truth Table:**
Since we have two inputs, there are 2² = 4 possible combinations.

| Input A | Input B | Output A OR B |
|:-------:|:-------:|:-------------:|
|    0    |    0    |       0       |
|    0    |    1    |       1       |
|    1    |    0    |       1       |
|    1    |    1    |       1       |

**The Minecraft Gate: Merging Wires**
This is another gift from the game's designers. The logic of an OR gate is inherent to how Redstone dust behaves.
1.  **The Lab:** Place two levers several blocks apart. These are inputs `A` and `B`.
2.  Run a line of Redstone dust from each lever.
3.  Have those two lines of dust merge into a single, third line.
4.  Connect this final line to a Redstone Lamp. This is our output.

**Experiment:**
*   If both levers are OFF, the lamp is OFF.
*   If you flip on just lever A, the lamp turns ON.
*   If you flip on just lever B, the lamp turns ON.
*   If you flip on both A and B, the lamp stays ON.

This is a perfect, physical representation of the OR truth table.

---

##### **Operator 3: AND (The "Strict" Gate)**

The AND gate is like a strict security guard. It looks at two inputs and asks: **"Are BOTH of these inputs True?"**

*   **Formal Name:** Conjunction
*   **Symbol:** In logic, `A ∧ B`. In programming, `A && B`. We'll use `A AND B`.
*   **The Rule:** The output is `True` only if input A is True AND input B is True. If either one (or both) is `False`, the output is `False`.

**The Truth Table:**

| Input A | Input B | Output A AND B |
|:-------:|:-------:|:--------------:|
|    0    |    0    |        0       |
|    0    |    1    |        0       |
|    1    |    0    |        0       |
|    1    |    1    |        1       |

**The Minecraft Gate: Our First Logic Puzzle**
Unlike NOT and OR, there is no single component that acts as an AND gate. We have to *build* one using the gates we already know. This is our first act of true digital engineering!

The most common design uses a combination of NOTs and an OR. It's based on a principle called **De Morgan's Law**, which we'll cover in the next lesson. For now, let's just build it.

1.  **The Lab:**
    *   Place two levers, `A` and `B`.
    *   Connect each lever to its own NOT gate (a torch on a block). So you have outputs for `!A` and `!B`.
    *   Take the outputs of these two NOT gates and feed them into an OR gate (merge the wires).
    *   Take the final output of that OR gate and feed it into one last NOT gate.
    *   Connect the final output to a lamp.

**The Boolean Expression for this circuit is: `!(!A OR !B)`**

**Experiment:**
Go through the truth table. You will find that the lamp only turns ON when both lever A and lever B are ON. This complex-looking contraption perfectly implements the AND gate's logic.

**A More Compact Design:**
The design above is great for understanding the theory. In practice, Redstone engineers use a more compact design.
1.  Place a single block.
2.  Place two Redstone torches on two different sides of that block.
3.  Place a single piece of Redstone dust on top of the block. This is your output.
4.  Your inputs are the blocks that the two torches are sitting on. Powering both of those input blocks is the only way to turn off both torches, which unpowers the dust, which allows an output signal to continue. (This is actually a NAND gate, so you put a final NOT torch on the output). The most common design is this:
    *   Place a block. Place a Redstone Torch on its front face. This is the output torch.
    *   Run two input lines (A and B) so they power the block this final torch is on. But use two torches to invert the inputs first. `!(!A OR !B)` becomes `A AND B`. This is De Morgan's Law in action!

---

#### **Lesson 2.3: The Laws of Logic**

Just like `2 + x = x + 2` in normal algebra, Boolean algebra has laws that let us rearrange and simplify expressions. A simpler expression means a smaller, faster Redstone circuit.

*   **Identity Law:** `A OR 0 = A` (ORing with something that's off doesn't change anything). `A AND 1 = A` (ANDing with something that's on doesn't change anything).
*   **Annihilator Law:** `A OR 1 = 1` (If one input to an OR gate is always on, the output is always on). `A AND 0 = 0` (If one input to an AND gate is always off, the output is always off).
*   **De Morgan's Law:** This is the superstar. It gives us a way to convert between ANDs and ORs.
    *   `!(A AND B)` is the same as `!A OR !B`.
    *   `!(A OR B)` is the same as `!A AND !B`.
    *   This is exactly why our first AND gate build worked! We built `!(!A OR !B)`. By De Morgan's law, `!A OR !B` is the same as `!(A AND B)`. So we built `!(!(A AND B))`. The two NOTs (`!!`) cancel out, leaving us with just `A AND B`. We used logic to prove our circuit was correct!

---

#### **Lesson 2.4: The Special Operator - XOR**

There is one more crucial gate we need. It's built from the others, but it's so common it gets its own name.

*   **Formal Name:** Exclusive OR
*   **Symbol:** `A ⊕ B` or `A ^ B`
*   **The Rule:** The XOR gate asks, **"Are the two inputs DIFFERENT?"** It outputs `True` only if one input is `True` and the other is `False`.

**The Truth Table:**
Notice the key difference from OR in the last row.

| Input A | Input B | Output A XOR B |
|:-------:|:-------:|:--------------:|
|    0    |    0    |        0       |
|    0    |    1    |        1       |
|    1    |    0    |        1       |
|    1    |    1    |        0       |

**The Minecraft Gate:**
There are many clever and compact XOR gate designs. One common one uses three NOT gates, two AND gates, and one OR gate.
*   **The Boolean Expression:** `(A AND !B) OR (!A AND B)`
*   **The Build:** You can build this directly, or look up a more compact design online. For the course, we'll provide a standard, reliable XOR gate design in the world download for you to use as a component.

**Foreshadowing:** The XOR gate is the "magic" that makes adding numbers possible. Its "difference detection" property is key to figuring out the sum in binary addition, as we will see in a later module.

---

**Module 2 Conclusion:**
This was a huge module! But you now have the most powerful tool an engineer can possess: a formal language to describe, design, and simplify complex systems. You know the "verbs" of logic: NOT, AND, OR, and XOR. You've built them, tested them, and seen how Boolean algebra predicts their behavior.

In the next module, we will use this newfound language to build our first truly complex and useful machine: a translator that will take the binary from our input register and show it on a human-readable display.