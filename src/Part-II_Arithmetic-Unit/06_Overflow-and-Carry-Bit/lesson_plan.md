### **Module 6: The "Overflow" Bug & The Carry Bit (Enhanced Edition)**

**(Learning Goals:** Discover and understand the concept of arithmetic **overflow**. Engineer a solution using the adder's **carry-out** bit to create a two-digit display. Appreciate the physical limits of a fixed-size computer.)

**(Narrative Beat:** "Our Hex display is powerful, but let's push it to its absolute limit. What happens when the answer is too big for even a single Hex digit? We'll discover a new, more fundamental bug and learn to harness a single, powerful bit—the carry bit—to solve it.")

---

#### **Lesson 6.1: The Theory - Hitting the Wall**

Congratulations on completing the Hexadecimal upgrade! Our display system is now robust, capable of showing any 4-bit number from `0` to `F`. It feels like our machine is unstoppable. But every machine, no matter how powerful, has its limits. In this lesson, we're going to find ours.

The components we have built—our registers, our adder, our display driver—all operate on a **4-bit word size**. This means the "word" or number they are designed to handle is 4 bits wide. The largest number a 4-bit word can possibly represent is `1111`, which we know is 15 in decimal, or `F` in hex.

This raises a critical question: What happens if we ask our 4-bit adder to calculate an answer that is *larger* than 15?

This situation is called **Arithmetic Overflow**. It's not a mistake or a flaw in the logic; it's a natural consequence of trying to fit a big number into a small box. When this happens, a computer needs a way to signal that the result was too large. This signal is the **Carry Bit**.

The `Carry-Out` wire on our 4-bit adder isn't an error light. It's the 5th bit of the answer! When we add two 4-bit numbers, the result can sometimes be a 5-bit number. Our adder is already correctly calculating this 5th bit; we just haven't been using it yet.

---

#### **Lesson 6.2: The Lab - Discovering the Overflow Bug**

**Goal:** To intentionally create an overflow error and observe the adder's behavior.

**The Setup:**
Your computer should still be set up from the end of Module 5.
*   Two 4-bit Input Registers (A and B).
*   The 4-bit Adder.
*   The Adder's 4-bit `Sum` output is connected to your upgraded 4-to-16 Hex Display system.
*   **Crucially**, make sure the final `Carry-Out` wire from the 4th bit of your adder is connected to a single, separate **Redstone Lamp**. This is our diagnostic light.

**The Integration Test:**
*   **Drill 1 (Success):** Let's do a calculation that fits. Set Register A to `1010` (A) and Register B to `0101` (5).
    *   **The Math:** `A + 5 = F` (or `10 + 5 = 15`).
    *   **The Result:** The Adder outputs `1111`. The Hex Display shows `F`. The Carry-Out lamp is **OFF**. Everything works perfectly. Our confidence is high!

*   **Drill 2 (The "Aha!" Moment - The Bug):** Now, let's push it. Set Register A to `1100` (C) and Register B to `0101` (5).
    *   **The Math:** `C + 5 = 11` in hex (or `12 + 5 = 17` in decimal).
    *   **The Adder's Output:** Look closely at your machine. The 4-bit `Sum` bus is outputting `0001`. The `Carry-Out` lamp is **ON**.
    *   **The Display's Output:** The Hex Display receives the `0001` from the Sum bus and shows a `1`.
    *   **The Problem:** The display says the answer is 1. We expected 17 (or `11` in hex). The result is wrong! But... we have a clue. The main display is showing the `1` from our expected answer, and the Carry-Out lamp is lit, representing the `1` in the 16s place. Our adder didn't fail; it gave us a 5-bit answer, and we only built a display for four of the bits!

---

#### **Lesson 6.3: The Lab - Engineering the 5-Bit Display**

Our Carry-Out lamp is the missing piece of our answer. Let's give it the display it deserves.

**Goal:** To create a second, simpler 7-segment display that shows a `1` when the Carry-Out is ON, and a `0` when it's OFF.

**The Design (The "Tens Digit" Driver):**
This is a simple 1-bit decoder. Let the Carry-Out wire be `C`.
*   To show `0` (when `C=0`), we need segments `a,b,c,d,e,f`.
*   To show `1` (when `C=1`), we need segments `b,c`.
*   The logic is therefore:
    *   `Segments a, d, e, f = !C`
    *   `Segments b, c = True` (always powered)
    *   `Segment g = False` (never powered)

**The Build:**
1.  **The Second Display:** Build a new 7-segment display structure out of lamps, to the left of your main Hex display.
2.  **The Driver Circuit:**
    *   Take the `Carry-Out` wire (`C`) from your adder.
    *   Create the inverted signal, `!C`, by running the `C` wire through a NOT gate.
    *   Wire the driver: Connect the `!C` signal to segments `a, d, e, f` of the new display.
    *   Wire a constant ON source (like a Redstone Block) to segments `b` and `c`.
    *   Leave segment `g` unwired.

---

#### **Lesson 6.4: The Final Test & Payoff**

Let's rerun our "failed" test with our newly upgraded, two-digit display system.

*   **The Test:** Set Register A to `1100` (C) and Register B to `0101` (5).
    1.  The Adder calculates the result. The `Sum` bus outputs `0001`. The `Carry-Out` (`C`) wire turns ON.
    2.  The main Hex Display receives `0001` and shows a `1`.
    3.  Our new "Tens Digit" driver receives `C=1`. It turns on segments `b` and `c`, showing a `1`.
    4.  **The Final Result:** Your displays, side-by-side, now read **`11`**. This is `11` in hexadecimal, which is `1*16 + 1 = 17`. **Success!**

---

#### **Module 6 Checkpoint**

*   **Quiz:**
    1.  What is an "overflow error" in the context of our 4-bit adder?
    2.  If we add `E + 5`, what will the 4-bit `Sum` be, and what will the `Carry-Out` bit be? (Sum: `0011` or `3`, Carry: `1`. The final answer is `13` hex).
    3.  Why didn't we need a full Hex Decoder for our second display? (Because it only ever needs to display 0 or 1).

*   **Real-World Connection: Status Flags**
    > That `Carry-Out` bit you harnessed is extremely important. In a real CPU, its value is stored in a special place called a "status register" as the **Carry Flag**. High-level programs can check this flag after an addition to see if an overflow occurred. This is critical for software that needs to do math with numbers much larger than the CPU's native 64-bit word size (like in cryptography or scientific simulation).

**Module 6 Conclusion:**
You have now conquered overflow! You've diagnosed a fundamental limitation of fixed-size computing and engineered an elegant solution. Our arithmetic unit is now robust and provides a full, accurate 5-bit result across two displays. In the next module, we will complete our arithmetic toolkit by teaching this very same adder how to subtract.
