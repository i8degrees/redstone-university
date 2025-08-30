## Module 5: The 4-Bit Adder & The Hexadecimal Upgrade

### Module 5 Summary

-   **Narrative Beat:** Time for real math! We'll build an adder, the circuit that lets our computer calculate. But when we connect it to our display, we'll discover our first major bug, forcing us to upgrade our system to speak a new, more powerful language: Hexadecimal.
-   **Learning Goals:**
    -   Understand the theory of binary addition, including the sum and carry bits.
    -   Build a functional 4-bit ripple-carry adder from full-adder modules.
    -   Discover and diagnose an "out of range" error through system integration.
    -   Learn hexadecimal as a human-readable shorthand for binary.
    -   Appreciate modular design by upgrading the decoder and encoder.
-   **Lesson Overview:**
    -   Lesson 5.1: The Theory of Binary Addition
    -   Lesson 5.2: The Lab – Building the 4-Bit Ripple-Carry Adder
    -   Lesson 5.3: The Integration Test & The First Bug
    -   Lesson 5.4: The Programmer's Solution – Speaking Hexadecimal
    -   Lesson 5.5: The Lab – The Hexadecimal Upgrade
-   **Minecraft Artifacts:** A 4-bit adder connected to an upgraded 4-to-16 decoder and hex-capable display.
-   **The Payoff:** The calculation `$8+4$` initially fails, but after the upgrade, it correctly displays a `$C$`.

---

### Module 5 Introduction

You have successfully engineered a complete input and output system for our computer. It can understand the binary numbers we give it and translate them back into a format we can read. Now, it's time to make it *think*.

In this module, we will construct the mathematical heart of our machine: a **4-bit adder**. This is the circuit that will perform our first real calculations. We will dive into the theory of binary addition and then build a beautiful, chained "ripple-carry" adder from the logic gates we've already mastered.

But this module is also a story about real-world engineering. We will connect our brand new adder to the display system we're so proud of, only to watch it fail. This will lead us to discover our first "bug" and, in solving it, upgrade our entire system to understand **Hexadecimal**, the native language of low-level programmers. This is where the pieces truly start to come together.

---

### Lesson 5.1: The Theory of Binary Addition

> **Key Takeaway:** Binary addition works just like decimal addition, using a sum and a carry for each column. The key rule to remember is `$1+1=0$, carry the `1`$.

Before we build, we must understand. How do we add `5+3` in binary?

    `0101` (5)
`+` `0011` (3)
  `------`

We add column by column, from right to left, just like in decimal.

1.  **`1`s Column:** $1 + 1 = 0$, carry a `1` to the `2`s column.
2.  **`2`s Column:** $0 + 1 + (\text{carry } 1) = 0$, carry a `1` to the `4`s column.
3.  **`4`s Column:** $1 + 0 + (\text{carry } 1) = 0$, carry a `1` to the `8`s column.
4.  **`8`s Column:** $0 + 0 + (\text{carry } 1) = 1$. No more carry.

The result is `` `1000` ``, which is `8` in decimal. It works!

Notice that for each column, we are actually processing *three* bits: bit $A$, bit $B$, and the **Carry-In** from the column to the right. And from this, we produce *two* bits of output: the **Sum** bit and the **Carry-Out** bit that goes to the next column. This 3-in, 2-out structure is called a **Full Adder**, and it's the key to our hardware design.

---
### Lesson 5.2: The Lab – Building the 4-Bit Ripple-Carry Adder

> **Key Takeaway:** A multi-bit adder can be constructed by chaining single-bit "Full Adder" modules together, allowing the "carry" to ripple from one column to the next.

> **A Note for the Curious: What About the "Half Adder?"**
> Students who have studied digital logic before might be wondering why we aren't starting with a simpler circuit called a "half adder." A half adder can add two bits, but it cannot handle a Carry-In, making it only useful for the very first bit in our chain.
>
> In this course, we prioritize building modular, reusable components. The **Full Adder** is the true "Lego brick" of arithmetic. It's the one component that can be used for *every single bit* in our adder. By starting directly with the Full Adder, every circuit you build is the final, useful version. We are skipping the transitional step to focus on the powerful, universal component.

#### The Concept: The 1-Bit Full Adder

We'll start by building a single module that can handle one column of addition. Its logic is a direct translation of the binary addition rules.

-   The **Sum** bit is $A \oplus B \oplus \text{CarryIn}$. (A 3-input XOR).
-   The **Carry-Out** bit is $(A \land B) \lor (\text{CarryIn} \land (A \oplus B))$.

#### Lab Part A: Build a 1-Bit Full Adder Module
1.  Using the logic above, combine AND, OR, and XOR gates to create a single, compact module. It must have 3 inputs ($A$, $B$, $C_{in}$) and 2 outputs ($Sum$, $C_{out}$).
2.  Test this single module thoroughly to ensure it correctly adds `0+0+0` up to `1+1+1`.

<div align="center"><img src="./images/full-adder-circuitverse.png" alt="1-Bit Full Adder CircuitVerse Diagram" width="512px"/><br/><em>Figure: A standard logic diagram for a 1-bit full adder, showing the two XOR gates for the Sum and the combination of AND/OR gates for the Carry-Out.</em></div><br/>

#### Lab Part B: Assemble the 4-Bit Ripple-Carry Adder
1.  **Layout:** Create two 4-bit input buses, Input $A$ and Input $B$.
2.  **Chaining:** Build and place four of your Full Adder modules in a line.
3.  **Wiring:**
    -   The $A$ and $B$ inputs of the first Full Adder (for the `1`s place) connect to the first bit of Input $A$ and Input $B$. Its $C_{in}$ is connected to `0` (grounded).
    -   The $A$ and $B$ inputs of the second Full Adder connect to the second bit of the input buses. Its $C_{in}$ connects to the $C_{out}$ of the first adder.
    -   Continue this chain for all four bits. The carry "ripples" down the line.
4.  **Output:** The four $Sum$ outputs from your adders form the 4-bit result of the addition.

<div align="center"><img src="./images/4-bit-adder-minecraft.png" alt="4-Bit Ripple-Carry Adder Minecraft Build" width="512px"/><br/><em>Figure: A 4-bit ripple-carry adder in Minecraft. Four full adder modules are chained together. The Carry-Out from each module (visible on the repeaters) "ripples" to become the Carry-In for the next.</em></div><br/>

---

### Lesson 5.3: The Integration Test & The First Bug

> **Key Takeaway:** Integrating two perfectly functional components can reveal system-level bugs that only appear when they work together.

#### The Test
It's time for a major payoff. We will connect our new adder (the "processor") to our display system from Module 4.

1.  **Connect the Output:** Wire the 4-bit $Sum$ output bus from the Adder to the 4-bit input of your 4-to-10 Decoder.
2.  **Test 1 (Success):** Set Input A to `0100` (4) and Input B to `0011` (3).
    -   The Adder calculates $4+3$ and outputs `0111`.
    -   The Decoder receives `0111`, activating its $L7$ line.
    -   The Encoder receives the signal from $L7$ and lights up the segments for a `7`.
    -   **Result:** The display shows a perfect **`7`**. It's a thrilling moment!

3.  **Test 2 (The "Aha!" Moment):** Now, set Input A to `1000` (8) and Input B to `0100` (4).
    -   The Adder works perfectly, calculating $8+4$ and outputting the binary result `1100` (12).
    -   The binary `1100` is sent to your Decoder...
    -   **...and the display is blank.**

#### The Diagnosis
We've found our first bug! But where is the failure? The Adder is correct. The display works for numbers `0-9`. The problem is the **interface between them.** Our decoder is a **Binary-Coded Decimal (BCD) Decoder**; it was specifically built to only understand the ten patterns for the numbers `0` through `9`. We just gave it a number it has no rule for. This is a critical lesson: **a system is only as smart as its components are programmed to be.**

---

### Lesson 5.4: The Programmer's Solution – Speaking Hexadecimal

> **Key Takeaway:** Hexadecimal (base-16) is a number system that uses 16 symbols to perfectly represent 4-bit binary values, making it a natural language for programmers and engineers.

We could try to build a complex system to show "12" on two separate displays, but there's a more elegant solution. Instead of forcing the computer to think in our base-10 system, we can meet it halfway and learn to read its preferred shorthand: **Hexadecimal**.

A 4-bit number can represent exactly 16 unique values (`0`-`15`). Hexadecimal was designed specifically for this, using one character to represent one 4-bit "nibble."

-   **Symbols:**
    -   `0-9` for values zero through nine.
    -   `A, B, C, D, E, F` for values ten through fifteen.

Our adder output `` `1100` ``, which is `12` in decimal. According to the hex system, `12` is simply **`C`**. By teaching our display to show letters, we can represent all 16 possible outputs of our 4-bit adder with a single character.

---

### Lesson 5.5: The Lab – The Hexadecimal Upgrade

> **Key Takeaway:** A well-designed modular system is easy to upgrade and expand without rebuilding it from scratch.

This is where our two-stage display design proves its genius. We don't have to start over. We just need to **add to it.**

#### Lab Part A: Upgrading the Decoder
1.  **Goal:** Expand our 4-to-10 BCD Decoder into a full **4-to-16 Binary Decoder**.
2.  **The Build:** Go back to your decoder from Module 4. Simply add six more output lines ($LA$ through $LF$) with the appropriate taps to detect the binary patterns for `` `1010` `` through `` `1111` ``.

#### Lab Part B: Upgrading the Encoder (ROM)
1.  **Goal:** Program our "Diode Matrix" ROM with the patterns for the letters `A` through `F`.
2.  **The Build:** Extend your ROM to accept the 16 input lines from the upgraded decoder. Then, for each new line, place torch taps to light up the correct segments. For example, for `` `C` ``, you would program the segments `a, f, e, d`.

#### The Payoff Test
Let's rerun the test that failed.

-   Set Input A to `` `1000` `` (8) and Input B to `` `0100` `` (4).
    -   The Adder correctly outputs `` `1100` `` (12).
    -   The binary `` `1100` `` enters your **upgraded** Decoder. The `$LC$` line activates.
    -   The `$LC$` line enters your **upgraded** Encoder. The segments for "C" light up.
    -   **Result:** The display shows a beautiful, glowing **`C`**. Success!

---

### Module 5 Checkpoint

#### Practice Problem 5.6.1: Knowledge Check
1. In binary, what is `1011` + `0010`?
2. What is the hexadecimal representation of the binary number `1101`?
3. What is the decimal value of the hexadecimal number `$B$`?

<details>
<summary><strong>Show Solution</strong></summary>
1. `` `1101` `` (which is $11+2=13$).
2. `$D$`.
3. `11`.
</details>

#### Practice Problem 5.6.2: The Software Adder
How would you add two numbers in a language that disabled the `+` key? You would mimic the hardware! The LeetCode problem "Sum of Two Integers" is solved by repeatedly using XOR for the sum bits and a shifted AND for the carry bits, until the carry is zero. Your hardware knowledge directly translates to this clever software algorithm.

```python
def getSum(a, b):
    mask = 0xffffffff
    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a & mask if b > 0 else a```

#### Key Terms
-   **Adder**: A digital circuit that performs the addition of numbers.
-   **Binary-Coded Decimal (BCD)**: A system that represents each decimal digit (`0`-`9`) with a 4-bit binary number.
-   **Full Adder**: A 1-bit circuit that adds three bits ($A$, $B$, and a Carry-In) and produces a Sum and a Carry-Out.
-   **Hexadecimal**: A base-16 number system used as a human-friendly representation of binary data.
-   **Ripple-Carry Adder**: A type of multi-bit adder built by chaining Full Adders together, where the carry bit "ripples" from one stage to the next.

---

### Module 5 Conclusion

Excellent work. You have not only built a machine that can perform mathematics, but you've also experienced the realistic engineering cycle of integrating components and discovering a system-level bug. This wasn't a failure; it was a discovery. By embracing a programmer's mindset and upgrading your system to speak hexadecimal, you made it more robust and powerful.

This principle of modular, expandable design is one of the most important concepts in all of engineering. Our computer is now more capable than ever, but is it perfect? In the next module, we will push it to its absolute limit and discover another, even more fundamental bug.
