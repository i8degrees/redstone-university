## **Module 7: The Subtractor & Negative Numbers**

**(Learning Goals:** Understand how negative numbers are represented in binary using **Two's Complement**. Learn how to build a circuit that can perform subtraction using the existing adder. Appreciate the efficiency and elegance of component reuse in hardware design.)

**(Narrative Beat:** "Our computer is a master of addition, but what about subtraction? Are we going to have to build a whole new, complicated 'subtractor' circuit that's just as big as our adder? No! Thanks to a brilliant mathematical trick that is central to all modern computing, we are going to teach our existing adder how to subtract.")

---

### **Lesson 7.1: The Theory - The Magic of Two's Complement**

The key to efficient subtraction in the binary world is to rephrase the problem. The expression `8 - 3` is exactly the same as `8 + (-3)`. If we can figure out a way to represent negative numbers in binary, we can just add them using our adder!

The system computers use is called **Two's Complement**. Here's the simple, two-step rule to find the negative version of any binary number:

1.  **Step 1: Invert all the bits.** Flip every `0` to a `1` and every `1` to a `0`. (This is called the "One's Complement").
2.  **Step 2: Add one.** Just perform a simple binary addition of `1` to the result of Step 1.

**Example: Let's find -3 in 4-bit binary.**
*   Start with positive 3: **`0011`**
*   **Step 1 (Invert):** `0011` becomes `1100`.
*   **Step 2 (Add 1):** `1100 + 1 = 1101`.
*   So, in the language of 4-bit Two's Complement, **`1101` represents -3.**

**The "Sign Bit":** Notice that the leftmost bit is now a `1`. In this system, the most significant bit (the 8's place in our machine) acts as the **sign bit**. If it's `0`, the number is positive. If it's `1`, the number is negative.

**The Proof: Let's calculate `8 + (-3)`**
*   8 is `1000`.
*   -3 is `1101`.
*   Let's add them with our ripple-carry method:
    ```
      (carry) 1 0 0 0
              1 0 0 0   (8)
            + 1 1 0 1   (-3)
            -----------
            1 0 1 0 1   (Result is 5!)
    ```
*   The 4-bit result is `0101`, which is 5. It worked!
*   **What about that 5th carry bit?** In Two's Complement, if there's a carry-out from the final addition, we simply **discard it**. This is part of the magic of the system.

---

### **Lesson 7.2: The Lab - Building the Adder/Subtractor Unit**

Now we need to build a circuit that can perform the "invert and add one" trick on command.

**Goal:** To create a unified **Adder/Subtractor Unit** that takes two numbers (A and B) and a single control line called `Subtract`.
*   If `Subtract` is `0`, it calculates `A + B`.
*   If `Subtract` is `1`, it calculates `A - B`.

**Part A: The Controllable Inverter**
We need a circuit that can either pass B through unchanged, or invert it. The **XOR gate** is the perfect tool for this! Remember its truth table:
*   `B XOR 0 = B` (The input passes through unchanged).
*   `B XOR 1 = !B` (The input is inverted).

1.  **The Build:** Take your 4-bit input bus for Register B. Before it enters the adder, insert a bank of four XOR gates.
2.  **The Control:** Connect one input of each XOR gate to the corresponding bit from Register B. Connect the *other* input of all four XOR gates together to a single new lever labeled **`Subtract`**.

**Part B: The "+1" Circuit**
This is the easiest part. How do we add 1 to the inverted number? Our adder already has a `Carry-In` input on its very first bit!

1.  **The Build:** Take the same **`Subtract`** lever and connect its wire directly to the `Carry-In` of the first Full Adder module (the 1s place).

**The Final Assembly:**
Your new `Subtract` lever now does two things simultaneously:
1.  It tells the XOR gates whether to invert Register B or not.
2.  It tells the adder whether to add an initial `1` or not.

When `Subtract = 0`: The XOR gates pass B through (`B XOR 0`), and the Carry-In is 0. The circuit calculates `A + B + 0`.
When `Subtract = 1`: The XOR gates invert B (`B XOR 1`), and the Carry-In is 1. The circuit calculates `A + !B + 1`. This is the exact formula for subtraction!

---

### **Lesson 7.3: The Integration & Test**

Connect your new Adder/Subtractor unit to your input interfaces and your two-digit display system.

**The Experiment:**
*   **Test 1 (Addition):**
    1.  Set the **`Subtract`** lever to **OFF (0)**.
    2.  Set Input A to `0111` (7) and Input B to `0010` (2).
    3.  **Result:** The display correctly shows `09`.

*   **Test 2 (Subtraction):**
    1.  Now, flip the **`Subtract`** lever to **ON (1)**.
    2.  The XOR gates invert `0010` to `1101`. The `Carry-In` becomes `1`.
    3.  The adder calculates `0111 + 1101 + 1`.
    4.  **Result:** The adder outputs `...0101`. The display correctly shows `05`. You have successfully calculated `7 - 2 = 5`.

---

### **Module 7 Checkpoint**

*   **Quiz:**
    1.  What are the two steps of the Two's Complement algorithm? (Invert, then add one).
    2.  In our 4-bit system, what does the sign bit `1` indicate? (A negative number).
    3.  Which logic gate was the key to creating our controllable inverter? (XOR).

*   **Real-World Connection: The ALU Control Word**
    > In a real CPU, there isn't a separate "Subtract" lever. The Control Unit sends a multi-bit "control word" to the ALU. A specific bit in that word (e.g., bit #2) would serve this exact purpose, telling the ALU whether to treat the current operation as an addition or a subtraction. You have just built a key part of that control mechanism.

### **Module 7 Conclusion:**
This was a huge leap forward! Our computer's mathematical abilities have now doubled. More importantly, you've learned the beautiful, efficient trick that allows all computers to handle negative numbers and subtraction without needing extra, complex hardware. You have now completed the entire Arithmetic Unit. With this powerful component finished, it is time to move on to the next major phase of our project: assembling the full Processor Core.
