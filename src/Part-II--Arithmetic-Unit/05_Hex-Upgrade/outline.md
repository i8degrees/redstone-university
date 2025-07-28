### **Module 5: The Programmer's Solution - The Hexadecimal Upgrade**

**(Learning Goals:** Learn about hexadecimal (base-16) as the native language for binary. Appreciate the power of modular design by easily expanding an existing circuit. Connect hex to its practical use in software.)

**(Narrative Beat:** "Our display failed because it only speaks 'decimal'. We could try to teach it to speak 'teens', but that's complicated. Instead, let's do what real programmers do and teach it to speak the computer's native tongue: Hexadecimal. Because we designed our system well, this will be an upgrade, not a rebuild.")

---

#### **Lesson 5.1: Why Hexadecimal is Easy for Computers**

When our adder outputted `1100`, our BCD decoder failed because it didn't have a rule for the number 12. We could try to build a very complex system with two separate displays for a "1" and a "2", but there's a much more elegant solution that programmers and engineers have used for decades.

Instead of forcing the computer to think in our base-10 system, we can meet it halfway and learn to read its preferred system: **Hexadecimal**, or base-16.

Binary groups nicely into sets of four. A 4-bit number can represent exactly 16 unique values (0-15). Hexadecimal is a number system with 16 symbols, designed specifically to represent a 4-bit "nibble" with a single character.

**The Hexadecimal Symbols:**
*   For numbers 0-9, it uses the same symbols: `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`.
*   For numbers 10-15, it uses letters: `A` (10), `B` (11), `C` (12), `D` (13), `E` (14), `F` (15).

**The Binary to Hex Conversion Table:**

| Decimal | Binary | Hex |
|:-------:|:------:|:---:|
|    8    | `1000` | `8` |
|    9    | `1001` | `9` |
|   10    | `1010` | `A` |
|   11    | `1011` | `B` |
|   12    | `1100` | `C` |
|   13    | `1101` | `D` |
|   14    | `1110` | `E` |
|   15    | `1111` | `F` |

This isn't a complex conversion; it's a direct, 1-to-1 lookup. This is why low-level programmers use hex constantly—it's a human-readable shorthand for binary.

---

#### **Lesson 5.2: The Lab - Upgrading Our System**

This is where our two-stage design proves its genius. We don't have to rebuild everything. We just have to **add to it**.

##### **Part A: Upgrading Stage 1 (The Decoder)**
*   **Goal:** Our decoder needs to understand the numbers 10 through 15. We will expand it from a 4-to-10 BCD decoder into a full **4-to-16 Binary Decoder**.
*   **The Build:** This is just more of what you already did in Module 3!
    1.  Go back to your Stage 1 Decoder's logic array.
    2.  **Add a new AND gate.** Wire it up to detect `1010`. Connect its output to a new line labeled `LA`.
    3.  **Add another AND gate.** Wire it up to detect `1011`. Connect to line `LB`.
    4.  Continue this for `C`, `D`, `E`, and `F`, until you have 6 new output lines, for a total of 16 output lines (`L0` through `LF`).

##### **Part B: Upgrading Stage 2 (The Encoder/ROM)**
*   **Goal:** Our display driver needs to know what to do when one of the new lines (`LA` through `LF`) activates. We need to "program" the shapes for the letters.
*   **The Build:** This is also just an expansion of our "diode matrix."
    1.  Extend your ROM. You now have 16 horizontal input lines (`L0`-`LF`) crossing the same 7 vertical segment lines.
    2.  **Program the new letters.** Let's program `A`. A good shape for 'A' uses segments `a, b, c, e, f, g`.
    3.  Go to the `LA` input line. At every point it crosses one of those segment lines, add a repeater/diode.
    4.  Repeat this process for B, C, D, E, and F.
    5.  **Design Note:** You may have to be creative with the shapes for `b` and `d` to distinguish them from `8` and `0`. A common solution is to use lowercase for them: `A, b, C, d, E, F`.

---

#### **Lesson 5.3: The Integration Test & The Payoff**

Now, let's rerun the test that "failed" in Module 4.

*   **The Test:** Set Register A to `1000` (8) and Register B to `0100` (4).
    1.  The Adder correctly outputs `1100` (12).
    2.  The binary `1100` enters your **upgraded** Stage 1 Decoder. The `LC` AND gate fires, activating the `LC` line.
    3.  The `LC` line enters your **upgraded** Stage 2 Encoder. The repeaters on that line for segments `a, d, e, f` all activate.
    4.  **Result:** The 7-segment display shows a beautiful, glowing `C`. **Success!**

---

#### **Module 5 Checkpoint**

*   **Quiz:**
    1.  What is the hexadecimal representation of the binary number `1110`? (E)
    2.  What is the decimal value of the hexadecimal number `B`? (11)
    3.  Why was our two-stage design easy to upgrade compared to a single, monolithic design?

*   **Software Connection (LeetCode): Bit Masking**
    > Programmers use hexadecimal constantly to make "bit masks" more readable. A mask is used to check or change specific bits in a number. Writing a mask as `0xF0` is much clearer to a human than its decimal equivalent `240`. `0xF0` instantly tells a programmer, "I am interested in the upper 4 bits of this 8-bit byte." This clarity is why hex is used in all low-level programming.
    >
    > Problems like "Reverse Bits" and generating all "Subsets" of a set on LeetCode are often much easier to reason about when you think about the numbers as hexadecimal bit masks.

**Module 5 Conclusion:**
Look at what you've done. You didn't just fix a bug; you performed a major system upgrade. Because you built your system in two modular stages, you were able to expand it with minimal effort. You expanded the decoder's 'vocabulary' and then expanded the encoder's 'dictionary'. This principle of modular, expandable design is one of the most important concepts in all of engineering. Our computer is now more robust than ever, but is it perfect? In our next module, we will push it to its absolute limit and discover another, even more fundamental bug.
