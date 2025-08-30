## Module 6: Advanced Arithmetic – Overflow and Subtraction

### Module 6 Summary

-   **Narrative Beat:** Our adder is powerful, but we'll now push it to its breaking point, discovering the fundamental bug of "overflow." We'll learn to harness the Carry Bit to detect it, and then, using a brilliant mathematical trick called Two's Complement, we will teach our existing adder how to subtract.
-   **Learning Goals:**
    -   Discover and understand the concept of arithmetic overflow.
    -   Engineer a solution using the adder's carry-out bit.
    -   Understand how negative numbers are represented in binary using Two's Complement.
    -   Build a unified circuit that can perform both addition and subtraction.
-   **Lesson Overview:**
    -   Lesson 6.1: The Theory – When Numbers Get Too Big
    -   Lesson 6.2: The Lab – Discovering and Handling Overflow
    -   Lesson 6.3: The Theory – The Magic of Two's Complement
    -   Lesson 6.4: The Lab – Building the Adder/Subtractor Unit
-   **Minecraft Artifact:** A unified adder/subtractor unit with an overflow indicator light.

---

### Module 6 Introduction

You've built a fantastic adder and upgraded our computer to speak hexadecimal. It feels like our machine is unstoppable. But every machine, no matter how powerful, has its limits. In this module, we're going to find ours.

First, we will push our 4-bit adder past its breaking point and discover **arithmetic overflow**, a bug that occurs when the answer to a calculation is too big for the computer to hold. You will learn to harness the powerful **Carry Bit** to detect this problem.

Then, we'll ask a new question: how do computers subtract? The answer is a beautiful mathematical trick that is central to all modern computing. We will learn about **Two's Complement**, the system for representing negative numbers, and use it to teach our existing adder how to subtract, doubling its capabilities without doubling its size.

---

### Lesson 6.1: The Theory – When Numbers Get Too Big

> **Key Takeaway:** Arithmetic overflow is a natural consequence of trying to fit a large number into a small, fixed-size container. The carry-out bit is the signal that this has happened.

The components we have built all operate on a **4-bit word size**. This means the largest number they can represent is `` `1111` ``, which we know is `15` in decimal, or `$F$` in hex. This raises a critical question: What happens if we ask our 4-bit adder to calculate an answer that is *larger* than 15?

For example, what is `$C + 5$` (`12 + 5`)? The answer is `17`. But `17` in binary is `` `10001` ``, a 5-bit number!

This situation is called **Arithmetic Overflow**. It's not a flaw in the logic; it's a fundamental limitation of working with a fixed number of bits. When an operation's result exceeds this limit, the 4-bit answer you get is wrong. The `Carry-Out` wire from our adder is the key. It's not an error light; it's the 5th bit of the answer! Our adder is already correctly calculating this 5th bit; we just haven't been using it yet.

---

### Lesson 6.2: The Lab – Discovering and Handling Overflow

> **Key Takeaway:** By connecting the carry-out bit from our adder to an indicator lamp, we can create a physical "overflow flag" that warns us when a calculation is invalid.

#### Lab Part A: Discovering the Overflow Bug

1.  **The Setup:** Your computer should still be configured from the end of Module 5, with the adder's 4-bit `Sum` output connected to your hex display.
2.  **The Crucial Addition:** Connect the final `Carry-Out` wire from the 4th bit of your adder to a single, separate **Redstone Lamp**. This is our overflow indicator.
3.  **The Test:** Set Input A to `` `1100` `` ($C$) and Input B to `` `0101` `` (5).
4.  **The "Aha!" Moment:** Observe the output.
    -   The 4-bit `Sum` bus is outputting `` `0001` ``.
    -   The Hex Display receives this and shows a **`1`**.
    -   The `Carry-Out` lamp is **ON**.

The display says the answer is `1`, but we expected `17`. The result is wrong! But we have a clue: the display is showing the `1` from the ones place, and the Carry-Out lamp is representing the `1` in the sixteens place. Our adder gave us a 5-bit answer, and we only built a display for four of those bits!

![Overflow Bug Minecraft Build](./images/overflow-bug-minecraft.png)
*Figure: The overflow bug in action. Input A (`C`) and Input B (`5`) are added. The 4-bit sum on the main display incorrectly shows `1`, but the crucial Carry-Out lamp is lit, indicating the overflow.*

#### Lab Part B: Engineering the Overflow Flag

The solution for now is simple: that Carry-Out lamp is our official **Overflow Flag**. In the future, our computer's Control Unit will be able to look at this signal. For now, we, the human engineers, will use it as a warning light. If that lamp is on, we know the number on the main display is not the complete answer.

---

### Lesson 6.3: The Theory – The Magic of Two's Complement

> **Key Takeaway:** By using a system called Two's Complement, we can represent negative numbers in binary, allowing us to perform subtraction by using regular addition.

The key to efficient subtraction is to rephrase the problem. The expression `$8 - 3$` is the same as `$8 + (-3)$`. If we can find the binary for `-3`, we can just use our adder! The system all modern computers use is called **Two's Complement**.

**The Two-Step Rule to find `-X`:**
1.  **Step 1 (Invert):** Invert all the bits of `$X$`. Flip every `` `0` `` to a `` `1` `` and every `` `1` `` to a `` `0` ``. (This is called the "One's Complement").
2.  **Step 2 (Add One):** Add `1` to the result of Step 1.

**Example: Let's find `-3` in 4-bit binary.**
-   Start with positive 3: **`` `0011` ``**
-   **Step 1 (Invert):** `` `0011` `` becomes `` `1100` ``.
-   **Step 2 (Add 1):** `` `1100` `` + `` `0001` `` = `` `1101` ``.
-   So, in 4-bit Two's Complement, **`` `1101` `` represents -3.**

Notice that the leftmost bit (the Most Significant Bit) is now `1`. This is the **sign bit**. If it's `0`, the number is positive. If it's `1`, it's negative.

Let's prove it works by calculating `$8 + (-3)$`:
-   `$8$` is `` `1000` ``.
-   `$-3$` is `` `1101` ``.
-   Adding them gives `` `10101` ``. In Two's Complement, we **discard the final carry bit**, leaving us with `` `0101` ``, which is `5`. It works perfectly!

---

### Lesson 6.4: The Lab – Building the Adder/Subtractor Unit

> **Key Takeaway:** By adding a bank of XOR gates to one of the inputs, we can create a "controllable inverter" that allows our adder to perform subtraction.

Our goal is to create a unified circuit that calculates `$A + B$` or `$A - B$` based on a single control signal. From the theory, we know that `$A - B$` is the same as `$A + (\neg B) + 1$`.

#### Lab Part A: The Controllable Inverter
We need a circuit that can either pass $B$ through unchanged, or invert it. The **XOR gate** is the perfect tool for this!
-   $B \oplus 0 = B$ (Pass-through)
-   $B \oplus 1 = \neg B$ (Invert)

1.  **The Build:** Take your 4-bit input bus for $B$. Before it enters the adder, insert a bank of four XOR gates.
2.  **The Control:** Connect one input of each XOR gate to the corresponding bit from $B$. Connect the *other* input of all four XOR gates together to a single new lever labeled **`Subtract`**.

#### Lab Part B: The "+1" Circuit
This is the easy part. How do we add `1`? Our ripple-carry adder already has a `Carry-In` input on its very first bit!

1.  **The Build:** Connect the same **`Subtract`** lever's signal directly to the `Carry-In` of the first Full Adder module (the `1`s place).

![Adder-Subtractor CircuitVerse Diagram](./images/adder-subtractor-circuitverse.png)
*Figure: The logic for the unified adder/subtractor. A control signal (`Subtract`) simultaneously tells the XOR gates to invert input B and tells the adder to add 1 via the initial Carry-In.*

#### Final Test

1.  **Addition:** Set the `Subtract` lever to **OFF (`0`)**. Test an addition like $7+2$. The display should show `9`.
2.  **Subtraction:** Flip the `Subtract` lever to **ON (`1`)**. The XOR gates now invert input $B$, and the adder receives a Carry-In of `1`. The circuit is now calculating $A + (\neg B) + 1$. Test $7-2$. The display should show `5`.

---

### Module 6 Checkpoint

#### Practice Problem 6.5.1: Knowledge Check
1. What is an "overflow error" in the context of our 4-bit adder?
2. In 4-bit Two's Complement, what is the binary representation for `-1`?
3. Which logic gate was the key to creating our controllable inverter?

<details>
<summary><strong>Show Solution</strong></summary>
1. An overflow error occurs when the result of a calculation is a number greater than `15` and requires more than 4 bits to represent.
2. `1111`. (Start with `0001`, invert to `1110`, add 1 to get `1111`).
3. The **XOR** gate.
</details>

#### Practice Problem 6.5.2: The Word Problem
You perform the calculation `$D - 5$` (hex) which is $13 - 5$ (decimal).
1. What is the 4-bit Two's Complement representation of `-5`?
2. What is the 5-bit binary result when you add `1101` (13) and your answer from part 1?
3. What is the final 4-bit answer after discarding the carry?

<details>
<summary><strong>Show Solution</strong></summary>
1. `-5` is `1011`. (Start with `0101`, invert to `1010`, add 1).
2. `1101` + `1011` = `11000`.
3. The final answer is `1000`, which is `8` in decimal.
</details>

#### Key Terms
- **Arithmetic Overflow**: An error condition that occurs when the result of a calculation is too large to be represented by the available number of bits.
- **Carry Bit**: A bit that stores the overflow from a single column of addition, which is then "carried" over to the next column.
- **Sign Bit**: The most significant bit (MSB) in a signed number representation, which indicates whether the number is positive or negative.
- **Two's Complement**: A mathematical operation and binary representation system used by computers to handle negative numbers, allowing for subtraction using addition.

---

### Module 6 Conclusion

Excellent work. You have now conquered the fundamental challenges of computer arithmetic. You've diagnosed overflow, a core limitation of fixed-size computing, and harnessed the Carry Bit to detect it. Even more impressively, you've implemented the beautiful mathematical trick of Two's Complement, doubling our machine's capability by teaching it to subtract.

Our Arithmetic Unit is nearly complete. In the next module, we will give it the power of awareness by building circuits that can compare numbers and set status flags, the final step before we can assemble the entire processor core.
