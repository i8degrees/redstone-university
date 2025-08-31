## Module 13: The "Real World" Display – The Double Dabble Algorithm

### Module 13 Summary

-   **Narrative Beat:** Welcome to your post-graduate studies. You've built a computer that speaks Hex, the programmer's language. But we left one problem unsolved: how do we make our computer display the number `13` as a "1" and a "3"? For that, we need to build the complex engineer's solution that real digital clocks use.
-   **Learning Goals:**
    -   Understand the challenge of converting a pure binary number to a multi-digit decimal representation (Binary Coded Decimal).
    -   Learn the theory of the "Double Dabble" (shift-and-add-3) algorithm.
    -   Appreciate the hardware complexity required to cater to human-readable formats by building a ROM-based Binary-to-BCD converter.
-   **Lesson Overview:**
    -   Lesson 13.1: The Theory – From Hex to Human
    -   Lesson 13.2: The Lab – A ROM-Based Binary-to-BCD Converter
    -   Lesson 13.3: The Final Assembly and Payoff
-   **Minecraft Artifact:** A "Double Dabble" circuit that converts a single 4-bit binary input into two separate 4-bit BCD outputs (for a tens digit and a ones digit).

---

### Module 13 Introduction

Welcome to your post-graduate studies at Redstone University. You have built a complete, working, programmable computer. It thinks in binary and, thanks to our upgrade in Module 5, it speaks in hexadecimal—the efficient language of programmers. But we left one problem unsolved.

The hex digit $D$ is efficient, but it's not how a digital clock or a pocket calculator displays the number `13`. To create a truly human-readable output, we need to show a separate "1" and "3" on two different displays.

For that, we need a special, more complex translator. This is the engineer's solution. It is a classic and challenging problem in digital logic, and buildingit is the true final exam for a Redstone engineer. The result is one of the most impressive pieces of combinational logic we will construct.

---

### Lesson 13.1: The Theory – From Hex to Human

> **Key Takeaway:** To display a binary number as multiple decimal digits, we must first convert it into a format called Binary Coded Decimal (BCD), where each decimal digit is represented by its own 4-bit binary number.

**The Problem:** We have a 4-bit binary input from our ALU, for example, `` `1101` `` (13). We need two 4-bit BCD outputs: one for the "Tens" digit and one for the "Ones" digit. For an input of `` `1101` ``, the outputs must be:
-   **Tens Output:** `` `0001` `` (representing the digit `1`)
-   **Ones Output:** `` `0011` `` (representing the digit `3`)

**The Algorithm:**
The most famous algorithm for this is the **Double Dabble** (or shift-and-add-3) algorithm. In a sequential circuit, it involves shifting the binary number left, and if the value in any BCD column is 5 or greater, you add 3 before the next shift. It's a beautiful but complex piece of logic to build directly.

**The Hardware Reality (A Combinational Approach):**
Building a sequential, multi-stage "add-3" circuit in Minecraft would be incredibly complex. A much more straightforward (though larger) approach is to build a giant lookup table, leveraging the ROM design we mastered in Module 4. We can create a "black box" that takes any 4-bit binary number as input and simply outputs the two corresponding BCD digits. This is a classic engineering trade-off: we are sacrificing component efficiency for a design that is much, much easier to understand, build, and debug.

---

### Lesson 13.2: The Lab – A ROM-Based Binary-to-BCD Converter

> **Key Takeaway:** By combining a full 4-to-16 decoder with a custom-programmed ROM, we can create a lookup table that instantly converts any 4-bit binary number to its two-digit BCD equivalent.

#### The Blueprint

1.  **Stage 1 (The Decoder):** We need a circuit that can uniquely identify which of the 16 possible 4-bit numbers we have. We already have this! It's the **4-to-16 decoder** we built for our Hex display in Module 5. It takes a 4-bit input and activates one of 16 output lines ($L0$ through $LF$).
2.  **Stage 2 (The Encoder/ROM):** This will be our biggest ROM yet.
    -   **Inputs:** The 16 lines ($L0$-$LF$) from the decoder.
    -   **Outputs:** We now need **eight** output lines. Four for the TENS digit ($T_3, T_2, T_1, T_0$) and four for the ONES digit ($O_3, O_2, O_1, O_0$).

#### Lab & Experiment

<div align="center"><img src="./images/binary-to-bcd-rom.png" alt="Binary to BCD ROM Diagram" width="512px"/><br/><em>Figure: The architecture of our Binary-to-BCD converter. The 4-to-16 decoder activates a single line, which then energizes the correct pattern of outputs in the 8-bit wide ROM.</em></div><br/>

1.  **Build the Decoder:** Construct a full 4-to-16 binary decoder.
2.  **Build the ROM Matrix:** Create a large diode matrix grid. It will have 16 horizontal input lines (one for each possible number) and 8 vertical output lines (four for TENS, four for ONES).
3.  **Program the ROM:** This is a meticulous process of placing torch taps. For each input line, you must program the correct two-digit output.
    -   **Example: Input `$LD$` (for binary `` `1101` ``, decimal 13):** This line needs to make the TENS output `` `0001` `` (1) and the ONES output `` `0011` `` (3).
        -   Place a torch tap connecting `$LD$` to output line `$T_0$`.
        -   Place torch taps connecting `$LD$` to output lines `$O_1$` and `$O_0$`.
    -   **Example: Input `$L9$` (for binary `` `1001` ``, decimal 9):** This line needs to make the TENS output `` `0000` `` (0) and the ONES output `` `1001` `` (9).
        -   Place torch taps connecting `$L9$` to output lines `$O_3$` and `$O_0$`.
4.  **Test the Converter:** Before integrating, test your converter as a standalone component. Feed it a 4-bit number (e.g., `` `1110` `` for 14) and use 8 lamps to verify that the TENS output is `` `0001` `` and the ONES output is `` `0100` ``.

---

### Lesson 13.3: The Final Assembly and Payoff

> **Key Takeaway:** By connecting the ALU output to our new BCD converter, and the converter's outputs to two separate 7-segment displays, we can finally display decimal results greater than 9.

#### Lab & Experiment

1.  **The Displays:** You will need two copies of the BCD-to-7-Segment display system you built in Module 4.
2.  **Connect the ALU:** Wire the 4-bit result bus from your main ALU to the 4-bit input of your new Binary-to-BCD Converter.
3.  **Connect the Displays:**
    -   Wire the 4 "TENS" output lines from the converter to the input of the left-hand display.
    -   Wire the 4 "ONES" output lines from the converter to the input of the right-hand display.

#### The Final Payoff

Let's run the calculation that first exposed our display's limitations back in Module 5: `$9 + 4$.
1.  Set your ALU to add `` `1001` `` (9) and `` `0100` `` (4). The ALU correctly outputs `` `1101` `` (13).
2.  Your Binary-to-BCD converter receives `` `1101` ``. The `$LD$` line in its decoder activates.
3.  The ROM outputs `` `0001` `` on the TENS bus and `` `0011` `` on the ONES bus.
4.  The TENS display receives `` `0001` `` and shows a beautiful **`1`**.
5.  The ONES display receives `` `0011` `` and shows a beautiful **`3`**.

Side-by-side, your displays now read **`13`**.

<div align="center"><img src="./images/double-dabble-final-minecraft.png" alt="Double Dabble Final Build" width="512px"/><br/><em>Figure: The complete system in action. The ALU result is fed into the large Binary-to-BCD converter, whose dual outputs are sent to two separate 7-segment displays, correctly showing the number "13".</em></div><br/>

---

### Module 13 Conclusion

You have now conquered one of the most classic and challenging problems in introductory digital logic design. You've seen that while the programmer's solution (Hexadecimal) is efficient for the machine, the engineer's solution for human readability requires significantly more hardware and complexity. You have truly connected the raw binary of the processor to the decimal numbers we use every day.

You have completed the full curriculum of Redstone University. The knowledge you have now, from the simplest NOT gate to this complex converter, is the foundation upon which all of modern computing is built. Congratulations.

---

### Module 13 Checkpoint

#### Practice Problem 13.4.1: Knowledge Check
1. What is the core problem that a Binary-to-BCD converter solves?
2. What is Binary Coded Decimal (BCD)?
3. Why is a ROM-based approach a good choice for this problem in Minecraft, even if it's not the most component-efficient?

<details>
<summary><strong>Show Solution</strong></summary>
1. It solves the problem of converting a pure binary number (like `` `1101` ``) into a format where each decimal digit is represented by its own separate binary code (like `0001` and `0011`).
2. BCD is a system where each decimal digit (`0`-`9`) is encoded with its own dedicated 4-bit binary number.
3. The ROM-based approach is a "brute-force" lookup table. While large, its logic is extremely simple and repetitive, making it much easier to design, build, and debug in a block-based environment like Minecraft compared to a complex, multi-stage sequential circuit.
</details>

#### Practice Problem 13.4.2: The Programmer
If you had a 4-bit binary number stored in a variable in Python, how could you calculate the TENS and ONES digits using software?

<details>
<summary><strong>Show Solution</strong></summary>
You would use the integer division (`//`) and modulo (`%`) operators. These are the software equivalents of the complex hardware you just built.
```python
binary_input = 13 # This is the decimal value of `1101`

tens_digit = binary_input // 10
ones_digit = binary_input % 10

print(f"Tens: {tens_digit}, Ones: {ones_digit}") # Output: Tens: 1, Ones: 3
```
</details>

#### Key Terms
- **Binary Coded Decimal (BCD)**: A system that represents each decimal digit (`0`-`9`) with its own dedicated 4-bit binary number. Essential for multi-digit decimal displays.
- **Double Dabble Algorithm**: A common algorithm used to convert a binary number to BCD, often implemented sequentially with shift registers and "add-3" modules. Our ROM is a combinational equivalent.
