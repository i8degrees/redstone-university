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
2.  **Isolate the Segments:** Carefully surround the lamp segments with a non-conductive block like Wool or Concrete. I use black concrete to make the segments stand out.
3.  **Create Manual Controls:** To power each segment, run a Redstone Repeater into the middle lamp. For now, place a solid block behind each repeater and attach a Lever to it. This gives you manual control for testing.


<div align="center"><img src="https://raw.githubusercontent.com/fielding/redstone-university/refs/heads/main/assets/images/03_7-segment-display_minecraft.png" alt="7 Segment Display in Minecraft" width="512px"/><br/><em>Figure: The display's construction stages. From left to right: the basic lamp layout, the layout isolated with concrete, powering the middle lamps of each segment, and a close-up of the repeater and lever used to control a single segment.</em></div></br></br>

**Practice Lab: Becoming a Human Encoder**

Before we build the complex logic to control this display automatically, let's get a feel for it ourselves. Use the levers you just installed to "draw" the following digits. This exercise will build your intuition for exactly what our machine needs to accomplish.

> **Note:** The levers are on the back of the display, so keep that in mind when flipping specific segments. It might help to label the segments with a sign by the lever that controls it for this exercise.

1.  Flip the levers for segments **`b`** and **`c`**. You should see the digit **`1`**.
2.  Now, try to display the digit **`7`**. (You'll need segments `a`, `b`, and `c`).
3.  Next, create the digit **`4`**. (This requires segments `f`, `g`, `b`, and `c`).
4.  **Challenge:** Try to form the digit **`8`**. What do you notice? Now try to form the digit **`2`**.


---

#### Lesson 3.2: The Master Plan: A Two-Stage Translation

> **Key Takeaway:** Complex engineering problems are best solved by breaking them down into smaller, simpler, manageable stages. The "plan" for our encoder is essentially a lookup table.

Now that we have our display, how do we control it? Our computer thinks in 4-bit binary, but our display needs 7 separate signals. Connecting the 4-bit input directly to the 7 segments would be a nightmare.

Instead, let’s think like engineers and break the problem into two much simpler, more manageable stages:

1.  **Decoder:** This first stage will act as an "identifier". Its only job is to look at the 4-bit binary input and determine *which* number (0-9) it represents. It will then activate a single, unique output line corresponding to that number.
2.  **Encoder:** This second stage is will act as the "mapper". It receives the simple signal from the decoder (e.g., "the number is 3!") and "maps" the signal, and the number it represents, to the correct combination of the 7 segments.

This modular, two-stage approach is the heart of good engineering. It's easier to build, easier to test, and far easier to fix if something goes wrong.

**Our Signal Flow:**
`[4-bit Input] → [**Decoder**] → [1 of 10 Lines] → [**Encoder/ROM**] → [7 Segment Signals] → [Display]`

---

#### Lesson 3.3: The Decoder Lab: A Simple "Brute-Force" Build

> **Key Takeaway:** A decoder can be built by assigning one AND gate to recognize each unique binary input. This "brute-force" method is clear but does not scale well.

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

In the next lesson, we will learn a far more elegant and compact solution.

---

#### Lesson 3.4: The Decoder Lab, Part 2: An Elegant, Compact Solution

> **Key Takeaway:** By using an "active-low" design and two clever types of "taps" (Repeater and Torch), we can build a decoder that is vastly smaller and more efficient.

Welcome to the engineer's solution. Instead of an "active-high" design, we will build an **"active-low"** design where the correct line turns **OFF**.

##### The Core Concept: The Mismatch Detector
Each output line will function as a **"mismatch detector."** Its job is to power its own wire (turning its lamp OFF) if the input does **not** match the line's identity. The only time a lamp stays ON is when the input is a perfect match. A "tap" is simply our term for a connection that reads, or "taps into," the signal from one of the main bus lines.

Technically, the entire structure for each output line is a **Multi-Input NOR Gate**, but thinking of it as a "mismatch detector" is a great way to understand its function.

##### Two Types of Taps: The Key to the Design
We use two different methods to tap the bus. This clever approach allows a single bus line (e.g., `B1`) to do the work of the two separate `B1` and `!B1` lines we needed in the brute-force build, cutting our bus width in half.

1.  **The Repeater Tap (Checks for a `1`):** A Repeater placed to tap a bus line will only activate if that bus line is **ON (`1`)**. We use this to detect a `1` where we expect a `0`.
2.  **The Torch Tap (Checks for a `0`):** A Torch placed to tap a bus line will only activate if that bus line is **OFF (`0`)**. We use this to detect a `0` where we expect a `1`.

##### The Simple Rule for Building
> To program the wire for an output line `LN`:
> *   For every bit position that is **`0`** in its identity, place a **Repeater Tap**.
> *   For every bit position that is **`1`** in its identity, place a **Torch Tap**.

---
##### Lab & Experiment: Building the Compact 4-to-10 Decoder

###### The Setup: Building the Physical Structure
This design relies on a two-layer structure to keep the input and output lines separate.

1.  **Output Layer (Ground Level):** Lay out 10 parallel lines of Redstone dust for your output lines (`L0` through `L9`). Leave at least one empty block between each line to prevent interference. At the end of each line, place a solid block, a Redstone torch on top, and a Redstone Lamp on top of the torch. All 10 lamps should be ON by default.

> **PLACEHOLDER:** A screenshot showing the 10 output lines on the ground, each ending with a lamp and torch.

2.  **Input Layer (Floating):** Now, build a platform for your input bus two blocks off the ground (leaving a 1-block high air gap). On this platform, run your four parallel input bus lines (`B3` to `B0`) so they run perpendicularly across all 10 output lines below.

> **PLACEHOLDER:** A screenshot showing the two-tiered structure: the 10 output lines on the ground and the 4 perpendicular input lines floating above them.

###### Programming the Lines: Placing the Taps
Now we will place our taps to connect the input and output layers.

-   **How to Build a Torch Tap:** At the correct intersection, place a Redstone torch on the side of the block that the input bus line rests on, directly above the output wire below.
-    **How to Build a Repeater Tap:** This requires specific placement to achieve strong power. At the correct intersection, one block *before* the output wire, break the input bus line. On the ground level, place a solid block and put a Repeater on top of it, facing in the direction of signal flow. This "snaking" path is essential. It is important to note that the Repeater itself does not power the output wire directly; it powers the block it runs into, which then becomes strongly powered and can power the output wire.

###### Programming Example: Line `L3` (Identity: `0011`)
-   At the intersection of bus line `B3` and output line `L3`, build a **Repeater Tap**.
-   At the intersection of bus line `B2` and output line `L3`, build a **Repeater Tap**.
-   At the intersection of bus line `B1` and output line `L3`, build a **Torch Tap**.
-   At the intersection of bus line `B0` and output line `L3`, build a **Torch Tap**.

> **PLACEHOLDER:** A close-up, angled screenshot focused on the `L3` line, clearly showing the physical construction of the two repeater taps and two torch taps.

###### Complete All Lines: Using the Reference Chart
Apply the rule and build methods to the remaining 9 lines. Use the chart below to verify your placements. This is your blueprint.


| Bus Line | `L0` | `L1` | `L2` | `L3` | `L4` | `L5` | `L6` | `L7` | `L8` | `L9` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`B3` (8)** | R | R | R | R | R | R | R | R | T | T |
| **`B2` (4)** | R | R | R | R | T | T | T | T | R | R |
| **`B1` (2)** | R | R | T | T | R | R | T | T | R | R |
| **`B0` (1)** | R | T | R | T | R | T | R | T | R | T |
*(R = Repeater Tap, T = Torch Tap)*

###### Test Your Work!
Cycle through inputs `0000` to `1001`. Verify that only one lamp is lit for each input.

---

##### Practice Problems

###### Problem 1: Design on Paper
Before you build, an engineer must be able to plan. For output line **`L6` (Identity: `0110`)**, what taps would you need? List out which type of tap (Repeater or Torch) is required for each of the four bus lines (`B3`, `B2`, `B1`, `B0`).

<details>
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

##### The Concept: Read-Only Memory

This stage is effectively a physical **Read-Only Memory (ROM)**. The "address" is the active (unpowered) line from the decoder, and the "data" that it looks up is the pattern of segments for that number. We build this using a structure called a **Diode Matrix**.

-   **The Grid:** The 10 input lines (`L0`–`L9`) from our decoder will run horizontally. The 7 output lines that control the display segments (`a`–`g`) will run vertically, crossing over (but not touching) the input lines.
-   **The "Diodes":** In electronics, a diode lets current flow one way. In Minecraft, a **Redstone Repeater** does the same job perfectly. It ensures a signal flows from our encoder to the display, but not backward.
-   **The Logic:** This is the clever part. Since our active input line is **LOW**, we need to invert the signal again.
    1.  We will place a torch at the base of each of the 7 vertical segment lines. By default, these torches are ON, trying to power all the segments.
    2.  We will run Redstone dust from the **HIGH** (inactive) decoder lines to turn **OFF** the segment torches we don't need.
    3.  When a decoder line like `L3` goes **LOW**, it stops suppressing the torches for segments `a, b, c, d, g`. Those torches are now free to turn ON, and the digit `3` appears.

##### Lab: Building the Diode Matrix

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

This checkpoint is divided into three parts to test the different skills you've acquired.

##### Part 1: Knowledge Check
1.  Why is a two-stage (Decoder -> Encoder) design generally better than a single, complex circuit?
2.  What is the purpose of the Repeater Tap in our compact decoder? Why can't we just use Redstone dust?
3.  In our Diode Matrix ROM, what does a connection between a horizontal line (`LN`) and a vertical segment line physically represent?

<details>
<summary><strong>Click for answers</strong></summary>
1.  It breaks the problem down, making it easier to design, build, and debug each part independently (modularity).
2.  The Repeater Tap creates a "strongly powered" block, which is necessary to power the Redstone dust on the output line across the 1-block air gap. Simple dust would create a "weakly powered" block, which cannot.
3.  It represents a single "bit" of stored information. Specifically, it's a command to "turn this segment OFF for this number."
</details>

##### Part 2: Logic Puzzles
1.  **Decoder Design:** You want to add a special output line, `LE`, that lights up only for even numbers (`0, 2, 4, 6, 8`). You realize that for all even numbers, the `B0` bit is always `0`. What is the single tap you would need to build a simple detector for this?
2.  **Encoder Design:** The letter 'A' can be made with segments `a, b, c, e, f, g`. On paper, which segment torches would the input line `LA` need to suppress in our Diode Matrix ROM?
3.  **Reverse Engineering:** You see a line in a decoder that has Torch Taps on `B2` and `B1`, and Repeater Taps on `B3` and `B0`. What decimal number is this line designed to detect?

<details>
<summary><strong>Click for solutions</strong></summary>
1.  You want the lamp to be ON only when `B0` is `0`. Our active-low system turns the lamp on when the line is unpowered. You would need a single **Repeater Tap** from the `B0` line. When `B0` is `1` (odd), the repeater powers the `LE` line and turns the lamp off. When `B0` is `0` (even), the repeater is off, the line is unpowered, and the lamp turns on.
2.  The `LA` line would need to suppress the torch for the segment that is OFF: only segment **`d`**.
3.  Torches are for `1`s, Repeaters are for `0`s. So the identity is `0110`. This is the binary for decimal **6**.
</details>

###### Part 3: The Debug Challenge (In-Game)
> In the world download for this module, you will find a section labeled "Module 3 Debug Challenge." The display system is fully connected. When you input **`0010`** (for the number 2), the display incorrectly shows a **`6`**.
>
> **Trace the logic:**
> -   The digit `2` should be `a, b, g, e, d`.
> -   The digit `6` is `a, c, d, e, f, g`.
>
> What is the single most likely point of failure in the system that would cause this specific error? (Hint: The problem is in the Encoder/ROM).

<details>
<summary><strong>Click for the solution</strong></summary>
**The Logic:**
When the input is `2`, the `L2` line from the decoder correctly goes LOW. The `L2` line is supposed to stop suppressing the torches for segments `a,b,d,e,g` and continue suppressing the torches for `c` and `f`.

The display shows a `6`, meaning segments `c` and `f` are ON when they should be OFF, and segment `b` is OFF when it should be ON.

**The Conclusion:**
This points to a catastrophic failure in the "programming" of the `L2` line in your Diode Matrix. You have wired it incorrectly.
-   The connections from the `L2` line to the `c` and `f` segment torches are likely **missing**.
-   You have likely **accidentally added** a connection from the `L2` line to the `b` segment torch.
</details>
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
-   **Tap (Repeater/Torch):** Our term for a connection that reads a signal from a bus line to control another wire.
-   **ROM (Read-Only Memory):** A type of storage where data is permanently programmed into the hardware's structure.
-   **Diode Matrix:** A grid of input and output lines where diodes (in our case, Redstone Repeaters and torches) are placed at intersections to create a programmable logic device, often used as a ROM.
-   **BCD (Binary-Coded Decimal):** A method of representing the decimal digits 0-9 using a 4-bit binary code.
-   **7-Segment Display:** An arrangement of seven light segments that can be combined to display numbers and some letters.
