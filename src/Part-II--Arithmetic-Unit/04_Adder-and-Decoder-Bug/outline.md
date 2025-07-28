### **Module 4: The Adder & The First "Bug"**

**(Learning Goals:** Understand how binary addition works. Build a functional 4-bit adder from basic logic gates. Discover and diagnose an "out of range" error through system integration.)

**(Narrative Beat:** "Time for real math! We'll build an adder, the circuit that lets our computer calculate. We'll connect it to our amazing two-stage display that we're so proud of. But what happens when our computer gets an answer it wasn't programmed to show? This is a story about engineering, success, and the thrill of finding our first bug.")

---

#### **Lesson 4.1: The Theory of Binary Addition**

Before we build, we must understand. How do we add `5+3` in binary?

`0101` (5)
`+ 0011` (3)
`------`

We add column by column, from right to left, just like in decimal, but we have to remember a new rule: **1 + 1 = 0, carry the 1.**

1.  **1s Column:** `1 + 1` = `0`, carry a `1` to the 2s column.
2.  **2s Column:** `0 + 1` + (our carry `1`) = `0`, carry a `1` to the 4s column.
3.  **4s Column:** `1 + 0` + (our carry `1`) = `0`, carry a `1` to the 8s column.
4.  **8s Column:** `0 + 0` + (our carry `1`) = `1`. No more carry.

Result: `1000`, which is 8 in decimal. It works!

Notice that for each column, we need to know two things: the **Sum** bit and the **Carry-Out** bit. This is the key to our hardware design.

*   The **Sum** bit is `A XOR B XOR CarryIn`. (The XOR gate is perfect for this!)
*   The **Carry-Out** bit is `(A AND B) OR (CarryIn AND (A XOR B))`.

---

#### **Lesson 4.2: The Lab - Building the 4-Bit Ripple-Carry Adder**

**Goal:** To build a circuit that implements binary addition using the logic gates from Module 2.

**The Concept:** We will build a "Full Adder" module that can handle one column of addition (A, B, and a Carry-In). Then we will chain four of them together. The carry-out from one column "ripples" to become the carry-in for the next.

**The Build: A 1-Bit Full Adder Module**
1.  Using the logic from Lesson 4.1, combine XOR and AND gates to create a single, compact module that has 3 inputs (`A`, `B`, `Cin`) and 2 outputs (`Sum`, `Cout`).
2.  **(A clear ASCII schematic or diagram of a compact Full Adder build would be provided here).**
3.  Test this single module thoroughly.

**The Full 4-Bit Adder:**
1.  **Layout:** Create two 4-bit input registers, Register A and Register B.
2.  **Chaining:** Place four of your Full Adder modules in a line.
3.  **Wiring:**
    *   The `A` and `B` inputs of the first Full Adder connect to the first bit of Register A and Register B. Its `Cin` is tied to 0 (grounded).
    *   The `A` and `B` inputs of the second Full Adder connect to the second bit of the registers. Its `Cin` connects to the `Cout` of the first adder.
    *   Continue this chain for all four bits.
4.  **Output:** The four `Sum` outputs from your adders form the 4-bit result of the addition.

---

#### **Lesson 4.3: The Integration Test & The Failure**

**Goal:** To connect our new "Processor" (the Adder) to our "Display" (the BCD system) and test its functionality.

**The Setup:**
1.  Disconnect the main Input Register from your Stage 1 Decoder (from Module 3).
2.  Instead, connect the **4-bit `Sum` output bus from the Adder** to the 4-bit input of the Stage 1 Decoder.
3.  The inputs to the Adder remain Register A and Register B.

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

#### **Module 4 Checkpoint**

*   **Quiz:**
    1.  In binary, what is `101` + `010`?
    2.  Which two logic gates are the primary components of a Full Adder circuit? (XOR and AND).
    3.  Why did our display show a blank screen when we added 8 + 4?

*   **Real-World Connection: The ALU**
    > You have just built the core of the **Arithmetic Logic Unit (ALU)** found in every CPU on the planet. The ALU is the mathematical brain of the processor, and the ripple-carry adder you built is a fundamental design that, in more advanced forms, is used to this day.

*   **Software Connection (LeetCode): The Software Adder**
    > How would you add two numbers in a language that disabled the `+` key? You'd do exactly what our Redstone machine does! The LeetCode problem "Sum of Two Integers" is solved by repeatedly using XOR for the sum bits and a shifted AND for the carry bits, until the carry is zero. Your hardware knowledge directly translates to this clever software algorithm.
    > ```python
    > def getSum(a, b):
    >     mask = 0xffffffff #
    >     while (b & mask) > 0:
    >         carry = (a & b) << 1
    >         a = a ^ b
    >         b = carry
    >     return a & mask if b > 0 else a
    > ```

**Module 4 Conclusion:**
You have successfully built a machine that can perform mathematics! More importantly, you've experienced the realistic engineering cycle of integrating two working components, only to find a system-level bug. This isn't a failure; it's a discovery. In the next module, we'll act like real engineers and upgrade our system to handle this new challenge.