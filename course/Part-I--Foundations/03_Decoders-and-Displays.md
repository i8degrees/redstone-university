### Module 3: Translators & Our First Display

---

#### Module Summary

-   **Narrative Beat:** We've learned the computer's language. Now let's build a translator so it can talk back to us. A complex translation is often easiest when broken into two simpler steps: first, translating binary to a single idea, then translating that idea into a picture.
-   **Learning Goals:**
    -   Understand the concepts of decoders and encoders.
    -   Apply Boolean logic to a large-scale, modular project.
    -   See the direct connection between these components and real-world computer hardware.
-   **Lesson Overview:**
    -   Lesson 3.1: The Output Problem & Building the Display
    -   Lesson 3.2: The Plan – A Two-Stage Approach
    -   Lesson 3.3: Building the Decoder (Stage 1)
    -   Lesson 3.4: Building the Encoder (Stage 2)
    -   Lesson 3.5: The Grand Payoff: The Final Connection
    -   Lesson 3.6: Module 3 Checkpoint
-   **Minecraft Artifact:** A working two-stage translator: a 4-to-10 BCD decoder and a 7-segment display encoder, forming a complete digital display system.

---

#### Module Introduction

In the previous modules, you learned how to speak to your computer in binary and how to manipulate those signals with logic gates. But a computer that can only listen isn't very satisfying. We want it to talk back! This is our first large-scale engineering project, and with it comes a new way of thinking.

> **Our New Rule: The Power of Abstraction**
>
> In Module 2, we built every gate from scratch to understand how it worked. From this point forward, we will operate at a higher level of abstraction.
>
> When a diagram or instruction says to "Build an AND gate," **how you choose to build it is now up to you.**
>
> -   You can build the verbose, easy-to-read version from Module 2.
> -   You can use a smaller, more efficient version from the Interlude.
> -   You can design your own!
>
> As long as your component functions according to its truth table, it is a valid build. This freedom is a major step in your journey from student to engineer. The preceding Interlude, **The Art of Compact Design**, gives you the foundation for making these choices.
>
> If you are ever unsure, the verbose builds from Module 2 are guaranteed to work.

---

#### Lesson 3.1: The Output Problem & Building the Display

Our computer can hear us, but it can’t talk back. We’ve built an input interface and learned how to process signals with logic gates, but so far, all our work is invisible—buried in wires and circuits. How do we make our computer show us numbers in a way we understand?

The answer is the **7-segment display**—a classic output device found in digital clocks, calculators, and scoreboards. It uses seven segments consisting of 3 redstone lamps each, labeled `a` through `g`, arranged like this:

     aaa
  fff   bbb
     ggg
  eee   ccc
     ddd

Each segment can light up independently. By combining them, we can display any digit from 0 to 9.

**Lab: Building the Display**

Let’s start by building the physical display in Minecraft. Place 7 segements of redstone lamps in the “8” shape shown above. For simplicity of wiring, we will surround the lamps with block concrete. This simplifies the wiring tremendously. To power each segment, you simply need to place a block below the middle lamp of each segment andrun a repeater into the middle lamp. This will power all three lamps in each segment.  For the rest of this lesson, let's put a block behind the repeater and put a lever on it to control and test each segment individually. In the next lessons we will be wiring these segments up to the logic that controls them.

:TODO: finish this lesson, let's add some pictures, and a lab that instructs the student to use the levers to create a few specific numbers, so they fully grok how the segments need to be powered in order to display each digit.

---

#### Lesson 3.2: The Plan – A Two-Stage Approach

Now that we have our display, how do we control it? If we tried to connect our 4-bit input directly to the seven segments, the wiring would be complex and confusing. Instead, let’s think like engineers and break the problem into two manageable stages:

1. **Decoder:** Translates a 4-bit binary input into a single active output line (representing the digit 0–9).
2. **Encoder:** Maps that active output line to the correct combination of segments to draw the digit.

This modular approach makes our system easier to build, test, and debug. Here’s the signal flow:

```
[4-bit Input] → [Decoder] → [Encoder/ROM] → [7-Segment Display]
```

Let’s build each stage step by step.

---

#### Lesson 3.3: Building the Decoder (Stage 1)

**Goal:** Build a circuit that takes a 4-bit BCD input (0–9) and activates one of 10 corresponding output lines. This is a pure application of your Module 2 logic skills.

**The Design (On Paper First):**
-   Let your four input bits be `B3, B2, B1, B0`.
-   Let your ten output lines be `L0, L1, ... L9`.
-   Each output line is controlled by its own 4-input AND gate.
    -   **Logic for L3 (`0011`):** `(!B3) AND (!B2) AND B1 AND B0`
    -   **Logic for L8 (`1000`):** `B3 AND (!B2) AND (!B1) AND (!B0)`

**The Minecraft Build:**
1.  **The Bus:** Start with your 4-bit input interface. Create a full 8-line bus by running each of the 4 input lines in parallel, then splitting each one through a NOT gate to create its inverted version. You should have `B3, !B3, B2, !B2, B1, !B1, B0, !B0` all available.
2.  **The Logic Array:** Build ten 4-input AND gates. For each gate, tap into the correct four lines from your bus to detect a specific number from 0 to 9.

**ASCII Schematic (Conceptual View):**
```
      B3  !B3   B2  !B2   B1  !B1   B0  !B0   (8-line Bus)
      |    |    |    |    |    |    |    |
 L0<--+----*----|----*----|----*----|----*---- [4-input AND for `0000`]
 L1<--+----*----|----*----|----*----*----|---- [4-input AND for `0001`]
 L2<--+----*----|----*----*----|----|----*---- [4-input AND for `0010`]
...and so on for L3 through L9.
```

**4-to-10 Decoder Mapping Table**

| Output | Binary Input | Logic Expression                  |
|--------|--------------|-----------------------------------|
| L0   | `0000`         | `!B3 AND !B2 AND !B1 AND !B0`     |
| L1   | `0001`         | `!B3 AND !B2 AND !B1 AND B0`      |
| L2   | `0010`         | `!B3 AND !B2 AND B1 AND !B0`      |
| L3   | `0011`         | `!B3 AND !B2 AND B1 AND B0`       |
| L4   | `0100`         | `!B3 AND B2 AND !B1 AND !B0`      |
| L5   | `0101`         | `!B3 AND B2 AND !B1 AND B0`       |
| L6   | `0110`         | `!B3 AND B2 AND B1 AND !B0`       |
| L7   | `0111`         | `!B3 AND B2 AND B1 AND B0`        |
| L8   | `1000`         | `B3 AND !B2 AND !B1 AND !B0`      |
| L9   | `1001`         | `B3 AND !B2 AND !B1 AND B0`       |

**Test your work!** Cycle through the inputs 0–9 and make sure the correct single output line (`L0`–`L9`) activates each time.

**Troubleshooting Tips:**
- If more than one output line is active, double-check your NOT gates and AND gate wiring.
- If no output line is active, make sure all four input bits are connected and that your AND gates are receiving the correct signals.
- Use colored wool or signs to label each line for easier debugging.

> **PLACEHOLDER:** Insert Minecraft screenshot and CircuitVerse diagram of the 4-to-10 decoder build.

**Lesson Summary:**
You’ve just built a circuit that can recognize any single digit from 0 to 9 in binary. This is an essential skill for translating between human and machine language.

**Real-World Connection: The Instruction Decoder**
>
> The circuit you just built is a simplified version of an **Instruction Decoder** in a real CPU. A CPU reads a binary instruction from memory (like `1011` for "ADD"). It feeds this binary code into a decoder just like this one, which activates a single wire that turns on all the circuitry responsible for performing addition.

---

#### Lesson 3.4: Building the Encoder (Stage 2)

**Goal:** Build a circuit that takes one of the 10 active lines from Stage 1 and lights up the correct combination of the 7 display segments.

**The Concept:** This stage is effectively a **Read-Only Memory (ROM)**. Its "address" is the active line from Stage 1 (`L0`–`L9`), and its "data" is the 7-segment information we "program" into it.

**The Design (The "Diode Matrix"):**
-   Imagine a grid. The 10 input lines from Stage 1 run horizontally. The 7 output lines for our display segments run vertically, crossing over them. We place a connection where a segment needs to be on for a given number.

**Visual Aid (Conceptual Grid):**
```
          Seg `a`  Seg `b`  Seg `c`  Seg `d`  Seg `e`  Seg `f`  Seg `g`
           |        |        |        |        |        |        |
L0 --------+--------+--------+--------+--------+--------+--------+ (`0`)
L1 --------+--------+--------+--------+--------+--------+--------+ (`1`)
L2 --------+--------+--------+--------+--------+--------+--------+ (`2`)
...and so on for L3 through L9.
```

**7-Segment Display Segment Table**

| Digit | `a` | `b` | `c` | `d` | `e` | `f` | `g` |
|-------|-----|-----|-----|-----|-----|-----|-----|
| `0`   |  X  |  X  |  X  |  X  |  X  |  X  |     |
| `1`   |     |  X  |  X  |     |     |     |     |
| `2`   |  X  |  X  |     |  X  |  X  |     |  X  |
| `3`   |  X  |  X  |  X  |  X  |     |     |  X  |
| `4`   |     |  X  |  X  |     |     |  X  |  X  |
| `5`   |  X  |     |  X  |  X  |     |  X  |  X  |
| `6`   |  X  |     |  X  |  X  |  X  |  X  |  X  |
| `7`   |  X  |  X  |  X  |     |     |     |     |
| `8`   |  X  |  X  |  X  |  X  |  X  |  X  |  X  |
| `9`   |  X  |  X  |  X  |  X  |     |  X  |  X  |

(X = segment on)


**The Minecraft Build:**
1.  **Layout:** Run your 10 input lines (`L0`–`L9`) horizontally. Run your 7 output lines (`a`–`g`) vertically.
2.  **The Connections:** At every intersection where a connection is needed (e.g., L2 needs to power Segment 'a'), place a **Repeater** facing *away* from the horizontal input line and *towards* the vertical output line. The repeater acts as a "diode," ensuring power flows in only one direction.
3.  **Programming:** You are physically "programming" the ROM. For each of the 10 input lines, go across and place repeaters on the vertical segment lines that need to be activated for that number.

> **PLACEHOLDER:** Insert Minecraft screenshot and CircuitVerse diagram of the diode matrix/ROM display encoder.

**Troubleshooting Tips:**
- If a segment doesn’t light up for a certain digit, check that the repeater (diode) is placed at the correct intersection.
- If multiple digits light up segments incorrectly, verify that each input line only powers its intended segments.
- Use temporary Redstone lamps to test each segment output individually.

**Lesson Summary:**
You’ve created a programmable display driver using a physical “ROM.” This is a powerful concept that bridges hardware and software.

**Real-World Connection: Read-Only Memory (ROM)**
>
> This "diode matrix" you've built is a simple form of **Read-Only Memory**. The "program," which is the shape of the numbers, is physically burned into the circuit's layout. Old video game cartridges and a computer's BIOS chip worked on this exact principle, with data permanently stored in the hardware's structure.

**Software Connection:**
> I'll keep this brief, because if you've done any programming, you've used a **lookup table** or hash map. If you find yourself stuck on an interview question, it is worth remembering that the majority of those types problems can be solved naively using a lookup table.

---

#### Lesson 3.5: The Grand Payoff: The Final Connection

Now, connect the two stages together. The 10 output lines from your Stage 1 Decoder become the 10 input lines for your Stage 2 Encoder.

**Let's Trace the Signal:**
1. You set your input levers to `0011` (3).
2. **Stage 1** activates. The AND gate for `(!B3) AND (!B2) AND B1 AND B0` fires. A signal is sent down the single `L3` line. All other 9 lines are off.
3. The `L3` line enters **Stage 2**.
4. The signal on the `L3` line powers the repeaters at the intersections for segments 'a', 'b', 'c', 'd', and 'g'.
5. Those five segment lines light up, and your 7-segment display shows a perfect, glowing **3**.

**Lesson Summary:**
By connecting your decoder and encoder to the display you built in Lesson 3.1, you’ve created a complete translation pipeline from binary input to human-readable output. This is a huge leap in making your computer interactive!

> **PLACEHOLDER:** Insert photo or diagram of the final connected system, showing a number displayed.**

---

#### Lesson 3.6: Module 3 Checkpoint

-   **Quiz:**
    1.  What is the main difference between a decoder and an encoder?
    2.  For the number 2 (`0010`), which segments of a 7-segment display should be active?
    3.  In our two-stage design, which stage is responsible for recognizing the binary pattern `1001`?

- **Challenge:**
    > The letter 'H' can be made on a 7-segment display (segments `b`, `c`, `e`, `f`, `g`). If we wanted to add an 11th input line (`LH`) to our Stage 2 Encoder, what would we need to do to make it display 'H'? Describe where you would place the repeaters.
    >
    > **Hint:** Think about which horizontal and vertical lines need to connect for the 'H' shape. Try sketching the 7-segment display and marking the segments!
    >
    > **Table for 'H' on 7-Segment Display:**
    >
    > | Segment | Should be ON for 'H'? |
    > |---------|----------------------|
    > |   `a`   |                      |
    > |   `b`   |         X            |
    > |   `c    |         X            |
    > |   `d`   |                      |
    > |   `e`   |         X            |
    > |   `f`   |         X            |
    > |   `g`   |         X            |
    >
    > Place repeaters at the intersections of the LH line and segments `b`, `c`, `e`, `f`, and `g`.

---


#### Module 3 Conclusion

By breaking the problem down into two distinct, logical stages, you've built a highly complex circuit in a way that is easy to understand, build, and debug. You've created a pure **Decoder** and a pure **Encoder/ROM**, two of the most fundamental building blocks in all of digital electronics. This is a massive milestone.

**What’s Next?**
In the next module, you’ll discover a critical flaw in our simple BCD translator. You’ll also learn how real engineers solve it!

---

#### Key Terms (Module 3)
- **Decoder:** A circuit that activates one output line based on a unique binary input.
- **Encoder:** A circuit that translates a single input into a coded output (here, segment patterns).
- **ROM (Read-Only Memory):** Hardware that stores fixed data, often used for lookup tables.
- **BCD (Binary-Coded Decimal):** A way of representing decimal digits in binary.
- **7-Segment Display:** An arrangement of LEDs or lamps used to display digits and some letters.
