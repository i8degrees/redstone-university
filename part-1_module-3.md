### **Module 3: Translators - Decoders, Encoders, and our First Display (Two-Stage Design)**

**(Learning Goals:** Understand the power of modular design by building a two-stage display driver. First, decode binary to a specific signal, then encode that signal for a complex display.)

**(Narrative Beat:** "We've learned the computer's language. Now let's build a translator. A complex translation is often easiest when broken into two simpler steps. First, we'll translate the computer's binary into a single, specific thought. Then, we'll translate that thought into the complex actions needed to draw a number.")

---

#### **Lesson 3.1: The Two-Stage Approach**

When we look at the binary `0101` and want to show a "5" on our display, we're doing two things in our head:
1.  **Decoding:** We first recognize that the pattern `0101` *is* the number 5.
2.  **Encoding/Mapping:** We then recall which segments on a display need to light up to *draw* the shape of a 5.

We are going to build a machine that mimics this exact two-stage process.

*   **Stage 1: The Binary-to-Decimal Decoder.** This machine's only job is to look at a 4-bit binary input and activate one, and only one, of its 10 output lines (one for each digit 0-9).
*   **Stage 2: The Display Encoder/Driver.** This machine's job is simpler. It has 10 input lines (one for each digit 0-9). If the "5" line lights up, its job is to send power to the correct segments (a, c, d, f, g) to draw a 5.

---

#### **Lesson 3.2: The Lab - Building Stage 1 (The 4-to-10 BCD Decoder)**

**Goal:** To build a circuit that takes a 4-bit BCD input (0-9) and activates one of 10 corresponding output lines.

**The Concept:** This is *exactly* like the 2-to-4 decoder from our mini-lab, just with more inputs and outputs. It's a pure application of Module 2 skills.

**The Design (On Paper First):**
Let our four input bits be `B3, B2, B1, B0`.
Let our ten output lines be `L0, L1, L2, ... L9`.

Let's design the logic for two of the lines:
*   **When should Line 3 (L3) turn on?** Only when the input is `0011`.
    *   **Logic for L3:** `(!B3) AND (!B2) AND B1 AND B0`
*   **When should Line 8 (L8) turn on?** Only when the input is `1000`.
    *   **Logic for L8:** `B3 AND (!B2) AND (!B1) AND (!B0)`

The pattern is clear: each of the 10 output lines will be controlled by its own 4-input AND gate, fed by the correct combination of normal and inverted bus lines.

**The Minecraft Build:**
1.  **The Bus:** Start with your 4-bit input register. Create a full 8-line bus by splitting off each input and running it through a NOT gate. You should have `B3, !B3, B2, !B2, B1, !B1, B0, !B0` all running in parallel.
2.  **The Logic Array:** Build ten 4-input AND gates. For each gate, tap into the correct four lines from your bus to detect a specific number from 0 to 9.
3.  **The Output:** You now have 10 distinct output lines. When you set your input levers to `0111` (7), only the line corresponding to `L7` will be powered. All others will be off.

**Test your work!** This component is now fully testable. Cycle through the inputs 0-9 and make sure the correct single output line activates each time.

---

#### **Lesson 3.3: The Lab - Building Stage 2 (The ROM and Display Encoder)**

**Goal:** To build a circuit that takes one of the 10 active lines from Stage 1 and lights up the correct combination of the 7 display segments.

**The Concept:** This stage is effectively a read-only memory, or **ROM**. Its "address" is the active line from Stage 1, and its "data" is the 7-segment information. But in Minecraft, we can think of it as a massive set of OR gates.

**The Design (The "Matrix"):**
Imagine a grid.
*   The **rows** of our grid are the 10 input lines from Stage 1 (`L0` through `L9`).
*   The **columns** of our grid are the 7 output lines going to our display segments (`a` through `g`).

We will place a connection (a Redstone Torch or dust) at the intersection of a row and column if that segment needs to be ON for that number.

**Let's design the logic for ONE segment (column): Segment 'a'.**
1.  Look at the 7-segment diagram. Which numbers need Segment 'a' (the top bar) to be lit?
    *   The numbers are: **0, 2, 3, 5, 6, 7, 8, 9**.
2.  **The Logic:** This is incredibly simple! It's just a giant OR gate.
    *   `Segment 'a' = L0 OR L2 OR L3 OR L5 OR L6 OR L7 OR L8 OR L9`
3.  We do this for every segment. Let's try **Segment 'f'**.
    *   It's needed for numbers: **0, 4, 5, 6, 8, 9**.
    *   **Logic:** `Segment 'f' = L0 OR L4 OR L5 OR L6 OR L8 OR L9`

**The Minecraft Build (The Diode Matrix):**
1.  **Layout:** Run your 10 input lines (`L0`-`L9`) from Stage 1 horizontally and in parallel. Run your 7 output lines (`a`-`g`) for the display vertically, crossing over the input lines.
2.  **The Connections:** At every intersection where a connection is needed (based on our logic above), we'll place a "diode" to prevent power from back-flowing. A simple Repeater is a perfect diode.
    *   To build the logic for Segment 'a', look at its vertical line. At every point it crosses an input line it needs (L0, L2, L3, etc.), place a repeater facing *away* from the input line and *towards* the output line.
    *   All these repeaters will feed into the single 'a' output line.
3.  Repeat this process for all seven vertical segment lines. You are physically "programming" the display information.

---

#### **Lesson 3.4: The Final Connection and The Grand Payoff**

Now, connect the two stages together. The 10 output lines from your Stage 1 Decoder become the 10 input lines for your Stage 2 Encoder.

**Let's Trace the Signal:**
1.  You set your input levers to `0011` (3).
2.  **Stage 1** springs to life. The AND gate for `(!B3) AND (!B2) AND B1 AND B0` activates. A signal is sent down the single `L3` line. All other 9 lines are off.
3.  The `L3` line enters **Stage 2**.
4.  The signal on the `L3` line powers the repeaters at the intersections for segments 'a', 'b', 'c', 'd', and 'g'. It does *not* power the repeaters for 'e' or 'f'.
5.  Those five segment lines light up, and your 7-segment display shows a perfect, glowing **3**.

**Conclusion:**
By breaking the problem down into two distinct, logical stages, you've built a highly complex circuit in a way that is easy to understand, build, and debug. You've created a pure **Decoder** and a pure **Encoder/ROM**, two of the most fundamental building blocks in all of digital electronics. This method is not just a "Minecraft trick"; it mirrors how real-world integrated circuits are often designed for clarity and modularity.