### **Module 3: Translators & Our First Display**

**(Learning Goals:** Understand the concepts of decoders and encoders. Apply Boolean logic to a large-scale, modular project. See the direct connection between these components and real-world computer hardware.)

**(Narrative Beat:** "We've learned the computer's language. Now let's build a translator so it can talk back to us. A complex translation is often easiest when broken into two simpler steps: first, translating binary to a single idea, then translating that idea into a picture.")

---

#### **Lesson 3.1: The Two-Stage Approach**

When we look at the binary `0101` and want to show a "5" on our display, we're doing two things in our head:
1.  **Decoding:** We first recognize that the pattern `0101` *is* the number 5.
2.  **Encoding/Mapping:** We then recall which segments on a display need to light up to *draw* the shape of a 5.

We are going to build a machine that mimics this exact two-stage process.

*   **Stage 1: The Binary-to-Decimal Decoder.** This machine's only job is to look at a 4-bit binary input and activate **one, and only one,** of its 10 output lines (one for each digit 0-9).
*   **Stage 2: The Display Encoder/Driver.** This machine's job is simpler. It has 10 input lines (one for each digit 0-9). If the "5" line lights up, its job is to send power to the correct segments (a, c, d, f, g) to draw a 5.

This modular design is a core principle of good engineering. It lets us build, test, and understand each part separately before combining them.

---

#### **Lesson 3.2: The Lab - Building Stage 1 (The 4-to-10 BCD Decoder)**

**Goal:** To build a circuit that takes a 4-bit BCD input (0-9) and activates one of 10 corresponding output lines. This is a pure application of our Module 2 skills.

**The Design (On Paper First):**
Let our four input bits be `B3, B2, B1, B0`. Let our ten output lines be `L0, L1, ... L9`. The pattern is clear: each output line is controlled by its own 4-input AND gate.
*   **Logic for L3 (`0011`):** `(!B3) AND (!B2) AND B1 AND B0`
*   **Logic for L8 (`1000`):** `B3 AND (!B2) AND (!B1) AND (!B0)`

**The Minecraft Build:**
1.  **The Bus:** Start with your 4-bit input register. Create a full 8-line bus by running each of the 4 input lines in parallel, and then splitting off each one through a NOT gate to create its inverted version. You should have `B3, !B3, B2, !B2, B1, !B1, B0, !B0` all available.
2.  **The Logic Array:** Build ten 4-input AND gates. For each gate, tap into the correct four lines from your bus to detect a specific number from 0 to 9.

**ASCII Schematic (Conceptual View):**
```
      B3  !B3   B2  !B2   B1  !B1   B0  !B0   (8-line Bus)
      |    |    |    |    |    |    |    |
 L0<--+----*----|----*----|----*----|----*---- [4-input AND for '0000']
 L1<--+----*----|----*----|----*----*----|---- [4-input AND for '0001']
 L2<--+----*----|----*----*----|----|----*---- [4-input AND for '0010']
...and so on for L3 through L9.
```
**Test your work!** This component is now fully testable. Cycle through the inputs 0-9 and make sure the correct single output line (`L0`-`L9`) activates each time.

> **Real-World Connection: The Instruction Decoder**
>
> The circuit you just built is a simplified version of an **Instruction Decoder** in a real CPU. A CPU reads a binary instruction from memory (like `1011` for "ADD"). It feeds this binary code into a decoder just like this one, which activates a single wire that turns on all the circuitry responsible for performing addition.

---

#### **Lesson 3.3: The Lab - Building Stage 2 (The ROM and Display Encoder)**

**Goal:** To build a circuit that takes one of the 10 active lines from Stage 1 and lights up the correct combination of the 7 display segments.

**The Concept:** This stage is effectively a **Read-Only Memory (ROM)**. Its "address" is the active line from Stage 1 (`L0`-`L9`), and its "data" is the 7-segment information we "program" into it.

**The Design (The "Diode Matrix"):**
Imagine a grid. The 10 input lines from Stage 1 run horizontally. The 7 output lines for our display segments run vertically, crossing over them. We place a connection where a segment needs to be on for a given number.

**Visual Aid (Conceptual Grid):**
```
          Seg 'a'  Seg 'b'  Seg 'c' ... (7 Vertical Output Lines)
           |        |        |
L0 --------+--------+--------+---- ... (10 Horizontal Input Lines)
           |        |        |
L1 ------(No)------+--------+---- ...
           |        |        |
L2 --------+--------+------(No)--- ...
...
```

**The Minecraft Build:**
1.  **Layout:** Run your 10 input lines (`L0`-`L9`) horizontally. Run your 7 output lines (`a`-`g`) vertically.
2.  **The Connections:** At every intersection where a connection is needed (e.g., L2 needs to power Segment 'a'), place a **Repeater** facing *away* from the horizontal input line and *towards* the vertical output line. The repeater acts as a "diode," ensuring power flows in only one direction.
3.  **Programming:** You are physically "programming" the ROM. For each of the 10 input lines, go across and place repeaters on the vertical segment lines that need to be activated for that number.

> **Real-World Connection: Read-Only Memory (ROM)**
>
> This "diode matrix" you've built is a simple form of **Read-Only Memory**. The "program"—the shape of the numbers—is physically burned into the circuit's layout. Old video game cartridges and a computer's BIOS chip worked on this exact principle, with data permanently stored in the hardware's structure.

---

#### **Lesson 3.4: The Final Connection and The Grand Payoff**

Now, connect the two stages together. The 10 output lines from your Stage 1 Decoder become the 10 input lines for your Stage 2 Encoder.

**Let's Trace the Signal:**
1.  You set your input levers to `0011` (3).
2.  **Stage 1** activates. The AND gate for `(!B3) AND (!B2) AND B1 AND B0` fires. A signal is sent down the single `L3` line. All other 9 lines are off.
3.  The `L3` line enters **Stage 2**.
4.  The signal on the `L3` line powers the repeaters at the intersections for segments 'a', 'b', 'c', 'd', and 'g'.
5.  Those five segment lines light up, and your 7-segment display shows a perfect, glowing **3**.

---

#### **Module 3 Checkpoint**

*   **Quiz:**
    1.  What is the main difference between a decoder and an encoder?
    2.  For the number 2 (`0010`), which segments of a 7-segment display should be active? (A, B, G, E, D)
    3.  In our two-stage design, which stage is responsible for recognizing the binary pattern `1001`? (Stage 1).

*   **Challenge:**
    > The letter 'H' can be made on a 7-segment display (segments b, c, e, f, g). If we wanted to add an 11th input line (`LH`) to our Stage 2 Encoder, what would we need to do to make it display 'H'? Describe where you would place the repeaters.

**Module 3 Conclusion:**
By breaking the problem down into two distinct, logical stages, you've built a highly complex circuit in a way that is easy to understand, build, and debug. You've created a pure **Decoder** and a pure **Encoder/ROM**, two of the most fundamental building blocks in all of digital electronics. This is a massive milestone. But, as we'll discover in the next module, our simple BCD translator has a critical flaw that we'll need to overcome.