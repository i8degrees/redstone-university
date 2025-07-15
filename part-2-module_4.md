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