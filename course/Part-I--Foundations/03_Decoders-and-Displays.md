### Module 3: From Binary to Pictures - Building a Digital Display

---

#### Module Summary

-   **Narrative Beat:** We've learned the computer's language. Now, let's build a translator so it can talk back to us. This is our first major engineering project, where we'll turn abstract binary signals into a number we can actually read.
-   **Learning Goals:**
    -   Understand the distinct roles of a decoder and an encoder.
    -   Grasp the engineering trade-offs between a "brute-force" design and an elegant, compact design.
    -   Master "active-low" logic and its practical application in Redstone.
    -   Build a functional Diode Matrix and understand its role as a form of Read-Only Memory (ROM).
-   **Lesson Overview:**
    -   **Lesson 3.1:** The Goal: Building Our 7-Segment Display
    -   **Lesson 3.2:** The Master Plan: A Two-Stage Translation
    -   **Lesson 3.3:** The Decoder Lab: A Simple "Brute-Force" Build
    -   **Lesson 3.4:** The Decoder Solution: An Elegant, Compact Design
    -   **Lesson 3.5:** The Encoder: Building a "Diode Matrix" ROM
    -   **Lesson 3.6:** The Grand Payoff: The Final Connection
    -   **Lesson 3.7:** Module 3 Checkpoint
-   **Minecraft Artifact:** A working two-stage translator: a 4-to-10 BCD decoder and a 7-segment display encoder, forming a complete digital display system.

---

#### Module Introduction

In the previous modules, you learned how to speak to your computer in binary and how to manipulate those signals with logic gates. But a computer that can only listen isn't very satisfying. We want it to talk back! This is our first large-scale engineering project, and with it comes a new way of thinking about building.

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

#### Lesson 3.1: The Goal: Building Our 7-Segment Display

> **Key Takeaway:** A 7-segment display is a standard output device that uses seven independent segments to form numbers. Understanding how to control it manually is the first step to controlling it automatically.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/03_7-segment-display.png" alt="7-Segment Display in CircuitVerse" width="512px"/><br/><em>Figure: The symbol for a 7-Segment Display on CircuitVerse (left) and its function in a basic circuit (right), taking seven inputs and lighting up the segments based.</em></div></br></br>

Our computer can hear us, but it can’t talk back. So far, all our work is invisible, buried in wires and circuits. How do we make our computer show us numbers in a way we understand?

The answer is the **7-segment display**, a classic output device found in everything from digital clocks to microwaves. It uses seven independently controlled segments, labeled `a` through `g`, arranged in an '8' pattern.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/03_7-segment-display_labeled.png" alt="7-Segment Display labeled" width="512px"/><br/><em>Figure: The standard labeling for the segments of a 7-Segment Display..</em></div></br></br>


By lighting up specific combinations of these seven segments, we can display any digit from 0 to 9.

**Lab: Building the Physical Display**

Let’s start by building the physical canvas for our numbers.

1.  **Construct the Segments:** In Minecraft, place Redstone Lamps in the "8" shape shown above. For good visibility, making each segment 3 lamps long is a great choice.
2.  **Isolate the Segments:** Carefully surround the lamp segments with a non-conductive block like Wool or Concrete. This is crucial to prevent the wiring for one segment from accidentally powering another. I personally use black concrete to make the segments stand out, but this is the only place I recommend using black concrete in this module.
3.  **Create Manual Controls:** Now we need a way to power each of the 7 segments individually. The easiest way is to run a Redstone Repeater into the middle lamp of the segment so that it becomes powered and will share signal with it's neighboring lamps. Place a solid block behind each repeater and attach a **Lever** to it. This will give you manual control over all seven segments, which is perfect for testing.

<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/03_7-segment-display_minecraft.png" alt="7 Segment Display in Minecraft" width="512px"/><br/><em>Figure: Need to update this caption. The image has examples of the 3 stages described above, from left to right. Then the 4th item in the image all the way to the right is a zoomed in look at how each segment is powered for our manual control.</em></div></br></br>

**Practice Lab: Becoming a Human Encoder**

Before we build the complex logic to control this display automatically, let's get a feel for it ourselves. Use the levers you just installed to "draw" the following digits. This exercise will build your intuition for exactly what our machine needs to accomplish.

> **Note:** The levers are on the back of the display, so keep that in mind when flipping specific segments. It might help to label the segments with a sign by the lever that controls it for this exercise.

1.  Flip the levers for segments **`b`** and **`c`**. You should see the digit **`1`**.
2.  Now, try to display the digit **`7`**. (You'll need segments `a`, `b`, and `c`).
3.  Next, create the digit **`4`**. (This requires segments `f`, `g`, `b`, and `c`).
4.  **Challenge:** Try to form the digit **`8`**. What do you notice? Now try to form the digit **`2`**.

Take a moment to appreciate the pattern. For each number, a unique combination of segments must be turned ON. Our job for the rest of this module is to build a machine that does this for us.
z
---

#### Lesson 3.2: The Master Plan: A Two-Stage Translation

Now that we have our display, how do we control it? Our computer thinks in 4-bit binary, but our display needs 7 separate signals. Connecting the 4-bit input directly to the 7 segments would require an incredibly complex web of logic gates.

Instead, let’s think like engineers and break the problem into two much simpler, more manageable stages:

1.  **Decoder:** This first stage will be the "brain" of the operation. Its only job is to look at the 4-bit binary input and determine *which* number (0-9) it represents. It will then activate a single, unique output line corresponding to that number.
2.  **Encoder:** This second stage is the "artist." It receives the simple signal from the decoder (e.g., "the number is 3!") and "draws" the digit by activating the correct combination of the 7 segments.

This modular, two-stage approach is the heart of good engineering. It's easier to build, easier to test, and far easier to fix if something goes wrong.

**Our Signal Flow:**
`[4-bit Input] → [**Decoder**] → [1 of 10 Lines] → [**Encoder/ROM**] → [7 Segment Signals] → [Display]`

---

#### Lesson 3.3: The Decoder Lab: A Simple "Brute-Force" Build

Before we tackle our full 4-bit to 10-line decoder, let's build a smaller, simpler version to prove the concept. We are going to build a **2-bit to 4-line decoder**. This circuit will take a 2-bit binary input (00, 01, 10, 11) and light up one of four corresponding output lamps (L1, L2, L3) representing those values in decimal (0, 1, 2, 3).

By scaling down the problem, we can focus on the core logic without getting overwhelmed. This is a common engineering practice: start small, prove the concept, then scale up. I'm calling this a "brute-force" method because we will build a separate AND gate for each output, rather than using a more elegant design, which we will learn in the next lesson.

**The Logic on Paper**

-   **Inputs:** `B1` (the "2s" place), `B0` (the "1s" place)
-   **Outputs:** `L0`, `L1`, `L2`, `L3`
-   **Logic Gates:** We need one 2-input AND gate for each output.
    -   `L0` (for `00` or `0`) = `(!B1) AND (!B0)`
    -   `L1` (for `01` or `1`) = `(!B1) AND B0`
    -   `L2` (for `10` or `2`) = `B1 AND (!B0)`
    -   `L3` (for `11` or `3`) = `B1 AND B0`

**Lab: Building the 2-to-4 Decoder**

**Step 1: The 2-Bit Bus**
1.  Set up two the standard inputs we've been using throughout the course, the redstone lamp with a lever on one side. Label them `B1` and `B0`.
2.  From these levers, create a **4-line bus**. Run redstone dust from the back of each lamp to a central point and then split each line into two parallel lines. On one line of each pair, place a NOT gate (a block with a torch on the opposite side that the dust runs in to ).
3.  You now have four parallel lines carrying the signals `B1`, `!B1`, `B0`, and `!B0`. Use colored wool to keep them organized!

> **PLACEHOLDER:** Insert a screenshot of the 4-line bus with inputs `B1` and `B0` and their inversions, clearly labeled.

**Step 2: Build and Test the First Gate (`L0`)**
1.  Choose your favorite 2-input AND gate design from Module 2 or the Interlude. Build one of these gates.
2.  Connect the gate's two inputs to the `!B1` line and the `!B0` line on your bus. Be careful with your wiring!
3.  Place a Redstone Lamp at the output of the AND gate. This is your `L0` output.
4.  **Test it!** Set your input levers to `00` (`B1`=OFF, `B0`=OFF). The `L0` lamp should turn ON. Now, flip either lever. The lamp should turn OFF. This proves your first gate is wired correctly.

> **PLACEHOLDER:** Insert a screenshot showing the single AND gate connected to the `!B1` and `!B0` lines of the bus, with its output lamp lit.

**Step 3: Build the Remaining Gates**
1.  Build three more identical 2-input AND gates next to the first one.
2.  Wire them according to the logic table:
    -   **Gate for `L1`:** Connect its inputs to the `!B1` and `B0` bus lines.
    -   **Gate for `L2`:** Connect its inputs to the `B1` and `!B0` bus lines.
    -   **Gate for `L3`:** Connect its inputs to the `B1` and `B0` bus lines.
3.  Place a Redstone Lamp on the output of each gate.

**Step 4: The Grand Test**
Now, cycle through all four possible inputs with your levers:
-   `00` -> Only the `L0` lamp should be ON.
-   `01` -> Only the `L1` lamp should be ON.
-   `10` -> Only the `L2` lamp should be ON.
-   `11` -> Only the `L3` lamp should be ON.

Congratulations, you've built a working decoder!

> **PLACEHOLDER:** Insert a screenshot or GIF of the final, working 2-to-4 decoder, showing how only one lamp lights up at a time as the inputs change.

**Lesson Summary: The Problem of Scale**
Take a look at the space your 2-to-4 decoder occupies. Now, imagine our real goal: a 4-to-10 decoder. We would need **ten** 4-input AND gates, which are much larger than the simple gates we just used. The brute-force method works, but it does not scale well. It creates a massive, resource-hungry machine.

In the next lesson, we will learn a far more elegant and compact solution to this exact problem.

---

#### Lesson 3.4: The Decoder Solution: An Elegant, Compact Design

> **Key Takeaway:** By using an "active-low" design and two clever types of "taps" (Repeater and Torch), we can build a decoder that is vastly smaller and more efficient than the brute-force method from the previous lesson.

In Lesson 3.3, we built a working decoder but also discovered the "problem of scale." A brute-force design using standard AND gates works, but it's huge. Now, we will build the engineer's solution: a design that is compact, fast, and leverages the unique physics of Redstone.

Our method is different. Instead of an "active-high" design where the correct output line turns ON, we will build an **"active-low"** design where the correct line turns **OFF**. This allows a lamp powered by an inverted signal to finally light up.

##### The Core Concept: The Mismatch Detector

The entire structure for a single output line functions as a large **"mismatch detector"**. Its only job is to power its own wire (and thus turn its lamp OFF) if the binary input from the bus does **not** perfectly match the number the line is supposed to represent.

The only time a lamp will stay ON is when the input is a perfect match. In this state, none of the "mismatch" taps activate, leaving the wire unpowered. This "any tap will turn it off" behavior means each output wire acts like a large, custom **OR** gate. The torch under the lamp provides the final **NOT**, making the whole structure a **Multi-Input NOR Gate**.

##### Two Types of Taps: The Key to the Design

We use two different methods to tap the bus. This allows a single bus line (e.g., `B1`) to check for two different conditions depending on which tap we use.

1.  **The Repeater Tap (Checks for a `1`):** A Repeater placed to tap a bus line will only activate if that bus line is **ON (`1`)**. We use this to detect a `1` where we expect a `0`.
2.  **The Torch Tap (Checks for a `0`):** A Torch placed to tap a bus line will only activate if that bus line is **OFF (`0`)**. We use this to detect a `0` where we expect a `1`.

Don't worry if this sounds confusing at first. The key is that each output line will have a unique identity, represented as a 4-bit binary number (e.g., `0011` for line `L3`). Each bit in this identity tells us whether to expect a `0` or a `1` from the corresponding bus line.

##### The Simple Rule for Building

Here is the straightforward rule for programming each output line. It's the key to the entire build.

> To program the wire for an output line `LN` (which represents a binary number over our 4-bit bus `B3 B2 B1 B0`):
> -   For every bit position that is **`0`** in its identity, place a **Repeater Tap** from that bus line.
> -   For every bit position that is **`1`** in its identity, place a **Torch Tap** from that bus line.

---
**Lab: Building the Compact 4-to-10 Decoder**

**A Note on Bit Numbering:** Remember our standard order: `B3` is the 8s place, `B2` is the 4s place, `B1` is the 2s place, and `B0` is the 1s place.

1.  **The Setup:** Lay out your 4 parallel input bus lines. Below them, lay out your 10 parallel output lines. At the end of each output line, place a solid block with a Redstone Torch on its face and a Redstone Lamp on top of it. All 10 lamps should be ON by default.

    > **PLACEHOLDER:** Screenshot of the initial bus and output line setup, with all 10 lamps lit.

2.  **Programming Line `L3` (Identity: `0011`)**
    -   `B3` is `0`: Place a **Repeater Tap** from the `B3` bus line down to the `L3` wire.
    -   `B2` is `0`: Place a **Repeater Tap** from the `B2` bus line down to the `L3` wire.
    -   `B1` is `1`: Place a **Torch Tap** from the `B1` bus line down to the `L3` wire.
    -   `B0` is `1`: Place a **Torch Tap** from the `B0` bus line down to the `L3` wire.

    > **PLACEHOLDER:** Close-up screenshot focused on the `L3` line, clearly showing the two repeaters and two torches in their correct positions relative to the bus.

3.  **Programming Line `L8` (Identity: `1000`)**
    -   `B3` is `1`: Place a **Torch Tap** from the `B3` bus line down to the `L8` wire.
    -   `B2` is `0`: Place a **Repeater Tap** from the `B2` bus line down to the `L8` wire.
    -   `B1` is `0`: Place a **Repeater Tap** from the `B1` bus line to the `L8` wire.
    -   `B0` is `0`: Place a **Repeater Tap** from the `B0` bus line to the `L8` wire.

4.  **Complete All Lines:** Apply this simple rule to the remaining 8 lines. Take your time and double-check each tap placement against the binary identity for that line.

5.  **Test Your Work!** Cycle through all binary inputs from 0 (`0000`) to 9 (`1001`). For each one, verify that only the single, correct lamp remains lit. The `L3` lamp should only be on for input `0011`, and the `L8` lamp only for `1000`.

---
##### Practice Problems

###### Problem 1: Design on Paper

Before you build, an engineer must be able to plan. For output line **`L6` (Identity: `0110`)**, what taps would you need? List out which type of tap (Repeater or Torch) is required for each of the four bus lines (`B3`, `B2`, `B1`, `B0`).

<details>
<summary>Show Solution</summary>
<summary><strong>Solution: Taps for L6 (`0110`)</strong></summary>

Applying our rule:
-   `B3` is `0`: Requires a **Repeater Tap**.
-   `B2` is `1`: Requires a **Torch Tap**.
-   `B1` is `1`: Requires a **Torch Tap**.
-   `B0` is `0`: Requires a **Repeater Tap**.

</details>

##### Problem 2: The Debug Challenge

You've built your decoder, but something is wrong. When you set the input levers to **`1001`** (for the number 9), you notice that the lamp for `L9` is on (which is correct), but the lamp for **`L8`** is *also* on (which is incorrect).

What is the single most likely mistake in your build that would cause this specific error?

<details>
<summary><strong>Solution: Debugging the L8 and L9 Error</strong></summary>

**The Logic:** The `L8` lamp should turn OFF when the input is `1001`. For `L8` to turn off, its wire needs to be powered. This means one of its "mismatch" taps must have activated.

**The Identity of `L8` is `1000`.** Let's compare this to the input `1001`.
-   `B3` is `1`, `L8` expects `1`. No mismatch.
-   `B2` is `0`, `L8` expects `0`. No mismatch.
-   `B1` is `0`, `L8` expects `0`. No mismatch.
-   `B0` is `1`, `L8` expects `0`. **This is a mismatch.**

The tap for `B0` on the `L8` line is supposed to detect this mismatch and power the `L8` wire. Since `L8` expects a `0` for `B0`, the rule says it must have a **Repeater Tap**.

**The Conclusion:** The fact that the `L8` lamp is still ON means its mismatch detector for the `B0` bit failed. The most likely cause is that you **forgot to place the Repeater Tap** from the `B0` bus line to the `L8` output wire. Without that tap, the wire never gets powered, and the lamp stays on.

</details>

---

#### Lesson 3.5: The Encoder: Building a "Diode Matrix" ROM

We now have a working decoder that gives us a single **unpowered** line for any given number. The next step is to build our "artist," the encoder that will take this information and draw the number on our display.

**The Concept: Read-Only Memory**

This stage is effectively a physical **Read-Only Memory (ROM)**. The "address" is the active (unpowered) line from the decoder, and the "data" that it looks up is the pattern of segments for that number. We build this using a structure called a **Diode Matrix**.

-   **The Grid:** The 10 input lines (`L0`–`L9`) from our decoder will run horizontally. The 7 output lines that control the display segments (`a`–`g`) will run vertically, crossing over (but not touching) the input lines.
-   **The "Diodes":** In electronics, a diode lets current flow one way. In Minecraft, a **Redstone Repeater** does the same job perfectly. It ensures a signal flows from our encoder to the display, but not backward.
-   **The Logic:** This is the clever part. Since our active input line is **LOW**, we need to invert the signal again.
    1.  We will place a torch at the base of each of the 7 vertical segment lines. By default, these torches are ON, trying to power all the segments.
    2.  We will run Redstone dust from the **HIGH** (inactive) decoder lines to turn **OFF** the segment torches we don't need.
    3.  When a decoder line like `L3` goes **LOW**, it stops suppressing the torches for segments `a, b, c, d, g`. Those torches are now free to turn ON, and the digit `3` appears.

**Lab: Building the Diode Matrix**

1.  **Layout:** Run your 10 unpowered output lines from the decoder horizontally. Above or below them, run 7 vertical lines for your segment outputs.
2.  **Power the Segments:** At the base of each of the 7 vertical segment lines, place a block with a Redstone Torch on top. These 7 torches are the power source for your display.
3.  **Program the Matrix:** Now for the "programming." Refer to the 7-segment table.
    -   For digit `0`, we need segments `a,b,c,d,e,f` ON and `g` OFF. This means the `L0` line must control the torch for segment `g`. Place a block at the intersection of the `L0` line and the `g` segment line. Run dust from the `L0` line to this block, and from this block to the block that the `g` torch is on. When `L0` is HIGH (inactive), it will keep the `g` torch OFF.
    -   For digit `1`, we need `b,c` ON. This means the `L1` line must suppress the torches for `a,d,e,f,g`. Place connections from the `L1` line to the control blocks of those five torches.
4.  **Add Diodes:** Place a Repeater on each of the 7 vertical segment lines, just after the torch, to ensure power only flows one way towards the display.

> **PLACEHOLDER:** Insert a screenshot of the diode matrix. A close-up of the `L1` or `L2` line showing how it connects to turn OFF specific segment torches would be ideal.

---

#### Lesson 3.6: The Grand Payoff: The Final Connection

The moment of truth has arrived. All the components are built. All that's left is to connect them.

1.  Connect the 10 output lines from your **Decoder** to the 10 input lines of your **Encoder/ROM**.
2.  Connect the 7 output lines from your **Encoder/ROM** to the control inputs of the **7-Segment Display** you built in the very first lesson.

**Let's Trace the Entire Signal for the Digit `3` (`0011`):**

1.  You flip your input levers to `0011`.
2.  **In the Decoder:** The specialized NAND gate for `L3` receives all its required inputs. Its final torch turns OFF, and the `L3` line goes **LOW**. All other lines (`L0-L2`, `L4-L9`) remain HIGH.
3.  **In the Encoder:** The HIGH lines keep the torches for the segments they control turned OFF. The `L3` line, however, is now LOW. It is no longer suppressing the torches for segments `a, b, c, d,` and `g`.
4.  Those five torches turn ON, sending power up their respective vertical lines.
5.  **At the Display:** The signals travel to the display, lighting up segments `a, b, c, d,` and `g`.
6.  You look at your display and see a perfect, glowing **3**.

Congratulations. You have successfully translated a 4-bit binary number into a human-readable digit.

> **PLACEHOLDER:** Insert a glorious wide-shot of the entire finished machine. The input levers should be set to a number (e.g., 9), and the display should clearly show that same number.

---

#### Lesson 3.7: Module 3 Checkpoint

-   **Quiz:**
    1.  What is the primary job of the decoder stage? What about the encoder stage?
    2.  Why did we choose an "active-low" (unpowered) signal for our compact decoder? What Redstone component makes this possible?
    3.  For the number `2` (`0010`), which segments of a 7-segment display should be active?
    4.  In our encoder's "diode matrix," what component acts as the diode, and what is its purpose?

-   **Challenge:**
    > The letter 'H' can be made on a 7-segment display by lighting up segments `b, c, e, f, g`. If we wanted to add an 11th input line (`L10`) to our encoder to display 'H', what would we need to do? Which segment torches would the `L10` line need to control?

---

#### Module 3 Conclusion

This was a massive milestone. You didn't just build a circuit; you engineered a system. By breaking a complex problem down into two distinct, logical stages (a decoder and an encoder), you built something complex in a way that was manageable, testable, and understandable. You have now mastered the concepts of binary-to-decimal decoding and using a hardware ROM to drive an output, two of the most fundamental building blocks in all of digital electronics.

**What’s Next?**
In the next module, you’ll discover a critical flaw in our simple translator when we try to count past 9. You’ll learn about the hexadecimal system and upgrade your display to handle it.

---

#### Key Terms (Module 3)

-   **Decoder:** A circuit that takes a multi-bit binary input and activates a single, corresponding output line.
-   **Encoder:** A circuit that takes a single active input line and translates it into a multi-bit coded output (like the patterns for a 7-segment display).
-   **Active-Low Logic:** A design principle where the "active" or "on" state is represented by a LOW (unpowered) signal, rather than a HIGH (powered) one.
-   **ROM (Read-Only Memory):** A type of storage where data is permanently programmed into the hardware's structure.
-   **Diode Matrix:** A grid of input and output lines where diodes (in our case, Redstone Repeaters and torches) are placed at intersections to create a programmable logic device, often used as a ROM.
-   **BCD (Binary-Coded Decimal):** A method of representing the decimal digits 0-9 using a 4-bit binary code.
-   **7-Segment Display:** An arrangement of seven light segments that can be combined to display numbers and some letters.
