### **Module 9: The "Real World" Display - The Double Dabble Algorithm (Post-Graduate Module)**

**(Learning Goals:** Understand the algorithm for converting pure binary to Binary Coded Decimal (BCD). Build a complex, multi-stage combinational circuit. Appreciate the hardware complexity required to cater to human-readable formats.)

**(Narrative Beat:** "Welcome to your post-graduate studies at Redstone University. You've built a complete, working computer. It thinks in binary and speaks in hexadecimal, the efficient language of programmers. But we left one problem unsolved: how do we make our 4-bit computer display the number '13' on two separate decimal displays? The hex 'D' is efficient, but it's not how a digital clock or a pocket calculator works. For that, we need a special, more complex translator. This is the engineer's solution. It will be challenging, but the result is truly impressive.")

---

#### **Lesson 9.1: The Theory - The Double Dabble Algorithm**

**The Problem:** We have a 4-bit binary input, `B3 B2 B1 B0`. We need two 4-bit BCD outputs: one for the "Tens" digit and one for the "Ones" digit.

**The Algorithm (for 4 bits):**
The Double Dabble algorithm (also known as a shift-and-add-3 algorithm) is surprisingly simple in concept.
1.  Start with your 4-bit binary number.
2.  Shift all bits one position to the left.
3.  After the shift, look at your "Ones" digit BCD register. If the number in it is **5 or greater**, you **add 3** to it.
4.  Repeat steps 2 and 3 for a total of four shifts. After the final shift, the "Tens" and "Ones" registers will hold the correct BCD values.

**Let's trace it with 13 (`1101`):**
We have two registers, `TENS` and `ONES`. We start with our input shifted in.

| Step        | Action                                 | TENS | ONES | Notes                                |
|:------------|:---------------------------------------|:----:|:----:|:-------------------------------------|
| Start       | Initial State                          | 0000 | 1101 | This is our 4-bit input.             |
| Shift 1     | Shift Left                             | 0001 | 1010 | The MSB of ONES moves to TENS.       |
| Check/Add 1 | ONES (`1010`=10) is >= 5? **Yes.** Add 3. | 0001 | 1101 | `1010 + 0011 = 1101`                 |
| Shift 2     | Shift Left                             | 0011 | 1010 |                                      |
| Check/Add 2 | ONES (`1010`=10) is >= 5? **Yes.** Add 3. | 0011 | 1101 |                                      |
| Shift 3     | Shift Left                             | 0111 | 0100 |                                      |
| Check/Add 3 | ONES (`0100`=4) is >= 5? **No.** Do nothing. | 0111 | 0100 |                                      |
| Shift 4     | Shift Left                             | 1110 | 1000 | **This is not the result!** The algorithm is more complex in hardware. |

**The Hardware Reality (A Combinational Approach):**
The shifting algorithm above is for a sequential circuit. A purely combinational circuit (which is easier to build for this) is different. It's a series of logic stages. For each possible input bit, we calculate if the "add 3" logic needs to trigger. This is complex! A simpler (but larger) approach for Minecraft is a giant lookup table.

---

#### **Lesson 9.2: The Lab - A ROM-Based Binary to BCD Converter**

**The Goal:** Build a "black box" that takes a 4-bit binary input and produces two 4-bit BCD outputs.

**The "Brute Force" ROM Approach:**
Instead of building the complex "add-3" logic, we can leverage the powerful two-stage design from Module 3. Our "Stage 1" will be a full 4-to-16 decoder. Our "Stage 2" will be a ROM programmed with the correct BCD output. This is much larger, but far easier to understand and build.

1.  **The Decoder (Stage 1):** You already have this! It's the 4-to-16 decoder from Module 5, which has 16 output lines (`L0` through `LF`).
2.  **The Encoder/ROM (Stage 2):** This will be our biggest yet.
    *   **Inputs:** The 16 lines (`L0`-`LF`) from the decoder.
    *   **Outputs:** We now need **8 output lines**. 4 for the TENS digit (`T3,T2,T1,T0`) and 4 for the ONES digit (`O3,O2,O1,O0`).
3.  **Programming the ROM:** We use our diode matrix again.
    *   **Input `LD` (13):** This line needs to turn on the "TENS" output to be `0001` (1) and the "ONES" output to be `0011` (3).
        *   We place a diode/repeater connecting `LD` to `T0`.
        *   We place a diode/repeater connecting `LD` to `O1` and `O0`.
    *   **Input `L9` (9):** This line needs to turn on TENS=`0000` and ONES=`1001`.
        *   We connect `L9` to `O3` and `O0`.

**(A diagram of the ROM matrix layout would be essential here).**

---

#### **Lesson 9.3: The Final Assembly**

1.  Take the 4-bit output from your main ALU. This is the input to your new Binary-to-BCD Converter.
2.  The 8 outputs from the converter are split.
3.  The 4 "TENS" bits go to the input of one BCD-to-7-Segment display system (the one from Module 3).
4.  The 4 "ONES" bits go to the input of a *second, identical* BCD-to-7-Segment display system.
5.  Place the two 7-segment displays side-by-side.

**The Final Payoff:**
*   Set your ALU to add `9 + 4`. The ALU outputs `1101` (13).
*   The Binary-to-BCD converter receives `1101`, and the `LD` line activates.
*   The ROM outputs `0001` on the TENS bus and `0011` on the ONES bus.
*   The TENS display decoder receives `0001` and shows a `1`.
*   The ONES display decoder receives `0011` and shows a `3`.
*   Side-by-side, your displays read **"13"**.

---

**Module 9 Conclusion:**
You have now conquered one of the most classic and challenging problems in introductory digital logic design. You've seen that while the programmer's solution (Hex) is efficient for the machine, the engineer's solution for human readability requires significantly more hardware and complexity. You have truly connected the raw binary of the processor to the decimal numbers we use every day. You have completed the full curriculum of Redstone University. The knowledge you have now, from the simplest NOT gate to this complex converter, is the foundation upon which all of modern computing is built. Congratulations.