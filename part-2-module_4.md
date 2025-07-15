### **Module 4: The Adder & The First "Bug"**

**(Learning Goals:** Build a circuit that performs binary addition. Discover and understand the concept of an "out of range" error.)

**(Narrative Beat:** "Time for real math! We'll build an adder, a circuit that can perform addition. We'll connect it to our amazing two-stage display that we're so proud of. But what happens when our computer gets an answer it wasn't programmed to show?")

#### **Lesson 4.1: The Lab - Building the 4-Bit Adder**

This lesson remains the same. The student builds the 4-bit Ripple-Carry Adder using the XOR and AND gates from their Module 2 knowledge. It takes two 4-bit numbers (from Register A and Register B) as input and produces one 4-bit number as the sum.

#### **Lesson 4.2: The Integration Test & The Failure**

**The Setup:**
1.  Disconnect the main Input Register (Register A) from the Stage 1 Decoder.
2.  Instead, connect the **4-bit output bus from the Adder** to the 4-bit input of the Stage 1 Decoder.
3.  The inputs to the Adder are now Register A and Register B.

**The Test:**
*   **Drill 1 (Success):** Set Register A to `0100` (4) and Register B to `0011` (3).
    *   **Trace the signal:** The Adder calculates `4+3` and outputs the binary `0111`.
    *   The binary `0111` enters your Stage 1 Decoder. The `L7` line activates.
    *   The `L7` line enters your Stage 2 Encoder. The segments for "7" light up.
    *   **Result:** The display shows a perfect `7`. The student feels like a genius.

*   **Drill 2 (The "Aha!" Moment - The Problem):** Now, set Register A to `1000` (8) and Register B to `0100` (4).
    *   **Trace the signal:** The Adder calculates `8+4` and outputs the binary `1100` (12).
    *   The binary `1100` enters your Stage 1 Decoder.
    *   **...What happens?** Nothing. The student looks at their Stage 1 build. There is no AND gate designed to detect `1100`. None of the 10 output lines (`L0`-`L9`) activate.
    *   Since no line activates into Stage 2, the display remains blank.

**The Lesson:**
> "We've found our first bug! Our Adder is working perfectly—it calculated 12 correctly. But our display system is the problem. Our Stage 1 Decoder is a **BCD Decoder**; it was specifically built to only understand the numbers 0 through 9. We just gave it a number it doesn't recognize. This is a critical lesson: a computer is only as smart as its components are programmed to be. To fix this, we need to upgrade our system."

---

### **Module 5: The Programmer's Solution - The Hexadecimal Upgrade**

**(Learning Goals:** Learn about hexadecimal (base-16) as the native language for binary. Upgrade the existing modular display system to handle any possible 4-bit value.)

**(Narrative Beat:** "Our display failed because it only speaks 'decimal'. We could try to teach it to speak 'teens', but that's complicated. Instead, let's do what real programmers do and teach it to speak the computer's native tongue: Hexadecimal.")

#### **Lesson 5.1: Why Hex is Easy for Computers**

Introduce hexadecimal (base-16). Explain that its 16 symbols (0-9, A, B, C, D, E, F) map *perfectly* to the 16 possible combinations of a 4-bit number. Show the full binary-to-hex conversion table. This is not a hack; it's the natural way to represent groups of 4 bits.

#### **Lesson 5.2: The Upgrade - Expanding Our Design**

This is where your two-stage design proves its genius. We don't have to rebuild everything. We just have to **add to it**.

**Part A: Upgrading Stage 1 (The Decoder)**
*   **The Goal:** Our decoder needs to understand the numbers 10 through 15. We need to add 6 new output lines: `LA`, `LB`, `LC`, `LD`, `LE`, `LF`.
*   **The Build:** This is just more of what the student already did in Module 3!
    1.  Go back to your Stage 1 Decoder's logic array.
    2.  **Add a new AND gate.** Wire it up to detect `1010` (A). Connect its output to a new line labeled `LA`.
    3.  **Add another AND gate.** Wire it up to detect `1011` (B). Connect to line `LB`.
    4.  ...and so on, until you have 6 new output lines, for a total of 16 output lines coming from Stage 1.
*   **The Result:** You now have a full **4-to-16 Binary Decoder**. It's no longer just a BCD decoder.

**Part B: Upgrading Stage 2 (The Encoder/ROM)**
*   **The Goal:** Our display driver needs to know what to do when one of the new lines (`LA` through `LF`) activates. We need to "program" the shapes for the letters.
*   **The Build:** This is also just an expansion.
    1.  Extend your "matrix" from Module 3. You now have 16 horizontal input lines (`L0`-`LF`) crossing the same 7 vertical segment lines.
    2.  **Program the new letters.** Let's program 'A'. The shape for 'A' uses segments a, b, c, e, f, g.
    3.  Go to the `LA` input line. At every point it crosses one of those segment lines, add a repeater/diode.
    4.  Repeat this process for B, C, D, E, and F. (Note: You may have to be creative with the shapes for `b` and `d` to distinguish them from `8` and `0`. A common solution is lowercase: `A, b, C, d, E, F`).

#### **Lesson 5.3: The Final Test & The Payoff**

Now, rerun the "failed" test.
1.  Set Register A to `1000` (8) and Register B to `0100` (4).
2.  The Adder outputs `1100` (12).
3.  The binary `1100` enters your **upgraded** Stage 1 Decoder. The `LC` AND gate fires, activating the `LC` line.
4.  The `LC` line enters your **upgraded** Stage 2 Encoder. The repeaters on that line for segments a, d, e, f all activate.
5.  **Result:** The 7-segment display shows a beautiful, glowing `C`.

**Module Conclusion:**
> "Look at what you've done. You didn't have to rip out your old work. Because you built your system in two modular stages, you were able to **upgrade** it with minimal effort. You expanded the decoder's 'vocabulary' and then expanded the encoder's 'dictionary'. This principle of modular, expandable design is one of the most important concepts in all of engineering. Our computer is now more robust and powerful than ever, and ready for its next challenge: building a full Arithmetic Logic Unit."