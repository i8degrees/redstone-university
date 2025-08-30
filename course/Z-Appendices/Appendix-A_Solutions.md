## Appendix A: Solutions

This appendix provides solutions to the practice problems in the Redstone University curriculum, organized by problem number for easy reference.

### Practice Problem 0.3.1: Knowledge Check

1.  What two essential functions does a Redstone Repeater perform?
2.  An engineer powers a block with a line of Redstone Dust. Will a piece of dust placed on top of that block receive power? Why or why not?
3.  What Redstone component is our primitive NOT gate?

1.  It boosts a signal back to strength `15` and acts as a one-way diode.
2.  No. The dust only weakly powers the block, which cannot transmit power to adjacent dust.
3.  The Redstone Torch.

</details>


---


### Practice Problem 1.4.1: Knowledge Check

1. What is the largest number a 5-bit input interface could input? (Hint: The next bit would be the `16`s place).
2. What is the decimal value of the binary number `1100`?
3. How would you represent the number `10` in binary?

1. The largest number a `5`-bit input interface could input is **`31`**. (In binary: `11111`, which is $16 + 8 + 4 + 2 + 1 = 31$.)
2. The decimal value of the binary number `1100` is **`12`**. ($8 + 4 + 0 + 0 = 12$.)
3. The number `10` in binary is **`1010`**. ($8 + 0 + 2 + 0 = 10$.)

</details>


---


### Practice Problem 2.2.1: Boolean Expression Evaluation

Given the Boolean expression $A \text{ OR } (\text{NOT } B)$ ($A \lor (\neg B)$), evaluate the output for all possible input combinations and create a truth table. Then, build a Minecraft circuit to verify your results.

**Truth Table for $A \lor (\neg B)$:**

| $A$ | $B$ | $\neg B$ | $A \lor (\neg B)$ |
|:---:|:---:|:---:|:---:|
| `0` | `0` | `1` | `1` |
| `0` | `1` | `0` | `0` |
| `1` | `0` | `1` | `1` |
| `1` | `1` | `0` | `1` |

**Minecraft Circuit**: Use a lever for input $A$ and another for input $B$. Place a Redstone Torch on the output line of $B$ to create the signal for $\neg B$. Merge the signal from $A$ and the signal from $\neg B$ using Redstone Dust (an OR gate). Connect the final output to a lamp and test all combinations to verify.

</details>


---


### Practice Problem 2.3.1: Logic Gate Design Challenge

Design a circuit that implements the logic $A \text{ AND } (\text{NOT } B)$ ($A \land (\neg B)$) using only the NOT and OR primitives. Build it in Minecraft and verify with a truth table for all input combinations ($A$, $B$ = `0,0`; `0,1`; `1,0`; `1,1`).

**Truth Table for $A \land (\neg B)$:**

| $A$ | $B$ | $\neg B$ | $A \land (\neg B)$ |
|:---:|:---:|:---:|:----------:|
| `0` | `0` | `1` | `0` |
| `0` | `1` | `0` | `0` |
| `1` | `0` | `1` | `1` |
| `1` | `1` | `0` | `0` |

**Boolean Expression**: The expression $A \land (\neg B)$ is equivalent to $\text{NOT}(\text{NOT } A \text{ OR } B)$ ($\neg(\neg A \lor B)$) by De Morgan’s Law.

**Minecraft Circuit**: This requires building a composite AND gate where one of the inputs is inverted first.
1. Create inputs for $A$ and $B$.
2. Use a Redstone Torch on the $B$ input line to create the signal for $\neg B$.
3. Feed the original $A$ signal and the new $\neg B$ signal into a standard composite AND gate (built from two NOTs and an OR, as shown in the lesson).
4. Connect the output to a lamp and test all four states.

</details>


---


### Practice Problem 2.4.1: Knowledge Check

1.  What are the two "primitive" logic gates that Minecraft provides directly through its game mechanics?
2.  What is the primary purpose of a truth table?
3.  What is the key difference in the rule for an OR gate versus an AND gate?

1.  The **NOT** gate (a Redstone Torch) and the **OR** gate (merging Redstone Dust lines).
2.  A truth table's purpose is to define a gate's behavior for every possible combination of inputs. It is the ultimate source of truth for how a logic circuit functions.
3.  An **OR** gate outputs a `1` if *at least one* input is a `1`. An **AND** gate outputs a `1` only if *all* inputs are a `1`.

</details>


---


### Practice Problem 2.4.2: The Word Problem

A simple home security system should sound an alarm ($Y$) if the front door is opened ($A$) **OR** the back door is opened ($B$), but only when the system is armed ($C$).

Write the single Boolean expression for the alarm $Y$. Which gates would you need to build this?

**Boolean Expression:** $Y = (A \lor B) \land C$

**Logic Gates Needed:** You would need one **OR** gate to combine the door sensors ($A \lor B$) and one **AND** gate to check if that result is true AND the system is armed ($C$).

</details>


---


### Practice Problem 2.4.3: The Build Challenge

Design and build a Minecraft circuit that implements the logic $A \text{ AND } (\text{NOT } B)$ ($A \land (\neg B)$). Use only the primitive NOT and OR gates. Verify its function against a truth table for all four input combinations.

**Truth Table:**

| $A$ | $B$ | $\neg B$| $A \land (\neg B)$ |
|:---:|:---:|:---:|:----------:|
| `0` | `0` | `1` | `0` |
| `0` | `1` | `0` | `0` |
| `1` | `0` | `1` | `1` |
| `1` | `1` | `0` | `0` |

**Minecraft Circuit:**
1.  Create inputs for $A$ and $B$.
2.  Use a Redstone Torch on the $B$ input line to create the signal for $\neg B$.
3.  Feed the original $A$ signal and the new $\neg B$ signal into a composite **AND** gate (built from two NOTs and an OR, as shown in Lesson 2.3).
4.  Connect the output to a lamp and test all four states.

</details>


---


### Practice Problem 3.1.1: Circuit Simplification Challenge

Given the expression $(A \text{ OR } B) \text{ AND } (\text{NOT } A \text{ OR } \text{NOT } B)$ ($(A \lor B) \land (\neg A \lor \neg B)$), simplify it using Boolean laws. Show all steps.

**Simplification Steps:**
1.  **Start with the expression:** $(A \lor B) \land (\neg A \lor \neg B)$
2.  **Apply De Morgan’s Law to the second term:** $(\neg A \lor \neg B)$ is equivalent to $\neg(A \land B)$.
3.  **The expression becomes:** $(A \lor B) \land \neg(A \land B)$
4.  **This expression is the definition of Exclusive OR (XOR):** This logic reads as "(A or B is true) AND (they are not both true)."
5.  **Final simplified expression:** $A \text{ XOR } B$ ($A \oplus B$)

</details>


---


### Practice Problem 3.2.1: The Two-Switch Light System

Design a Minecraft circuit for a two-switch light system where flipping either switch toggles the light’s state (on to off, or off to on). This requires implementing the logic $A \text{ XOR } B$ ($A \oplus B$) using only NOT and OR gates.

**Logic:** The light should be ON when exactly one switch is ON, which is the definition of $A \oplus B$.

**Truth Table:**

| $A$ | $B$ | Light ($A \oplus B$) |
|:---:|:---:|:----------------:|
| `0` | `0` | `0` |
| `0` | `1` | `1` |
| `1` | `0` | `1` |
| `1` | `1` | `0` |

**Minecraft Circuit:** Build the XOR circuit from this lesson. Connect levers for inputs $A$ and $B$, and a lamp for the output. Test by flipping each lever individually and verifying that the lamp's state toggles each time.

</details>


---


### Practice Problem 3.3.1: The Missing Number Challenge

Now that you've seen how the XOR trick works, try applying the same core principle to solve a different, but related, problem.

> **The Challenge:**
>
> You are given a list of numbers that contains every number from `0` to `n` exactly once, except for one number which is missing. Your task is to find that missing number.
>
> -   **Example List:** `nums = [3, 0, 1]`
> -   In this example, `n` would be `3`. The full range of numbers should be `[0, 1, 2, 3]`. The missing number is `2`.
>
> **Hint:**
> Think about the two groups of numbers you're dealing with: the list you *have* and the complete list you *should have*. How can you use XOR's self-canceling property to find the single difference between these two groups?

**The Logic:**

The core idea is to XOR all the numbers that *should* be in the list against all the numbers that *are* actually in the list.

1.  First, we calculate the XOR sum of the complete sequence of numbers from 0 to `n`. For our example `[3, 0, 1]`, `n` is 3, so this would be `0 ^ 1 ^ 2 ^ 3`.
2.  Next, we calculate the XOR sum of the numbers in the list we were given: `3 ^ 0 ^ 1`.
3.  If we XOR these two results together, all the numbers that are present in both lists will pair up and cancel out, leaving only the number that was missing from the input list.

`(0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)` can be rearranged as `(0^0) ^ (1^1) ^ (3^3) ^ 2`, which simplifies to `2`.

**The Python Code:**

```python
def missingNumber(nums):
    n = len(nums)
    expected_xor_sum = 0
    for i in range(n + 1):
        expected_xor_sum ^= i

    actual_xor_sum = 0
    for num in nums:
        actual_xor_sum ^= num

    return expected_xor_sum ^ actual_xor_sum
```

</details>


---


### Practice Problem 3.4.1: Universal Gate Challenge

Build an $A \text{ AND } B$ ($A \land B$) gate using only NOR gates. Verify it with a truth table in Minecraft for all four input combinations.

**Logic:** From our universal gate table, we know the expression is $(A \text{ NOR } A) \text{ NOR } (B \text{ NOR } B)$.

**Truth Table Verification:**

| $A$ | $B$ | $A \text{ NOR } A$ ($\neg A$) | $B \text{ NOR } B$ ($\neg B$) | $(\neg A) \text{ NOR } (\neg B)$ | Final Output ($A \land B$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `0` | `1` | `1` | `0` | `0` |
| `0` | `1` | `1` | `0` | `0` | `0` |
| `1` | `0` | `0` | `1` | `0` | `0` |
| `1` | `1` | `0` | `0` | `1` | `1` |

**Minecraft Circuit:** Build three NOR gates. The first takes input $A$ on both of its inputs (creating a NOT gate). The second does the same for input $B$. The outputs of these first two gates become the inputs for the third, final NOR gate, which produces the correct AND result.

</details>


---


### Practice Problem 3.5.1: Knowledge Check

1.  What is the key difference in the output of an OR gate versus an XOR gate when both inputs are `1`?
2.  Which two gates are considered "universal," and what is the name of this powerful property?
3.  Using De Morgan's Law, what is the equivalent expression for $\neg(A \land B)$?

1.  When both inputs are `1`, an **OR** gate outputs `1`, while an **XOR** gate outputs `0`.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is $\neg A \lor \neg B$.

</details>


---


### Practice Problem 3.5.2: The Simplification Challenge

An engineer has designed a circuit with the expression: $Y = (A \text{ AND } C) \text{ OR } (A \text{ AND } B \text{ AND } C) \text{ OR } (A \text{ AND } (\text{NOT } B) \text{ AND } C)$ ($Y = (A \land C) \lor (A \land B \land C) \lor (A \land \neg B \land C)$).

Simplify this expression to its most efficient form using Boolean laws. (Hint: Look for a common factor in all three terms first).

1.  **Start with the expression:** $Y = (A \land C) \lor (A \land B \land C) \lor (A \land \neg B \land C)$
2.  **Factor out the common term $(A \land C)$:** $Y = (A \land C) \land (1 \lor B \lor \neg B)$
3.  **Apply Inverse Law ($B \lor \neg B = 1$):** $Y = (A \land C) \land (1 \lor 1)$
4.  **Apply Idempotent/Annihilator Law ($1 \lor 1 = 1$):** $Y = (A \land C) \land 1$
5.  **Apply Identity Law:** $Y = A \land C$

The entire complex circuit simplifies down to a single AND gate with inputs $A$ and $C$.

</details>


---


### Practice Problem 3.5.3: The Universal Gate Challenge

Build an $A \text{ OR } B$ ($A \lor B$) gate using only **NAND** gates. Provide the Boolean expression for your build and verify it with a truth table.

**Boolean Expression:** From our universal gate table, the expression is $(A \text{ NAND } A) \text{ NAND } (B \text{ NAND } B)$.

**Truth Table Verification:**

| $A$ | $B$ | $A \text{ NAND } A$ ($\neg A$) | $B \text{ NAND } B$ ($\neg B$) | $(\neg A) \text{ NAND } (\neg B)$ | Final Output ($A \lor B$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `0` | `0` | `1` | `1` | `0` | `0` |
| `0` | `1` | `1` | `0` | `1` | `1` |
| `1` | `0` | `0` | `1` | `1` | `1` |
| `1` | `1` | `0` | `0` | `1` | `1` |

</details>


---


### Practice Problem 3.5.4: The Software Challenge

You are given a list where every number appears three times, except for one number that appears only once. Write a Python function using bitwise operators that finds the unique number. (Hint: The self-canceling property of XOR won't work directly. How can you count the `1`s in each bit position across all the numbers?)

**The Logic:** If we sum the bits in each position (the 1s place, 2s place, 4s place, etc.) for all the numbers in the list, the sum for each bit of the triplicate numbers will be a multiple of 3. The unique number's bits will be the "remainders." We can use the modulo operator (`%`) to find these remainders.

**The Python Code:**
```python
def singleNumber_threes(nums):
    result = 0
    # Iterate through each of the 32 bits for a standard integer
    for i in range(32):
        bit_sum = 0
        for num in nums:
            # Check if the i-th bit is set in the current number
            if (num >> i) & 1:
                bit_sum += 1

        # If the sum is not a multiple of 3, the unique number's bit is 1
        if bit_sum % 3 != 0:
            # Reconstruct the result by setting the i-th bit
            result |= (1 << i)

    return result
```
</details>


---


### Practice Problem 4.4.1: Design on Paper

Before you build, an engineer must be able to plan. For output line **`L6` (Identity: `0110`)**, what taps would you need? List out which type of tap (Repeater or Torch) is required for each of the four bus lines (`B3`, `B2`, `B1`, `B0`).

Applying our rule:
-   `B3` is `0`: Requires a **Repeater Tap**.
-   `B2` is `1`: Requires a **Torch Tap**.
-   `B1` is `1`: Requires a **Torch Tap**.
-   `B0` is `0`: Requires a **Repeater Tap**.

</details>


---


### Practice Problem 4.4.2: Debug Challenge

You've built your decoder, but something is wrong. When you set the input levers to **`1001`** (for the number `9`), you notice that the lamp for `L9` is on (which is correct), but the lamp for **`L8`** is *also* on (which is incorrect).

What is the single most likely mistake in your build that would cause this specific error?

**The Logic**: The $L_8$ lamp should turn OFF when the input is `1001`. For $L_8$ to turn off, its wire needs to be powered. This means one of its "mismatch" taps must have activated.

**The Identity of `L8` is `1000`.** Let's compare this to the input `1001`.
-   `B3` is `1`, `L8` expects `1`. No mismatch.
-   `B2` is `0`, `L8` expects `0`. No mismatch.
-   `B1` is `0`, `L8` expects `0`. No mismatch.
-   `B0` is `1`, `L8` expects `0`. **This is a mismatch.**

The tap for `B0` on the `L8` line is supposed to detect this mismatch and power the `L8` wire. Since `L8` expects a `0` for `B0`, the rule says it must have a **Repeater Tap**.

**The Conclusion**: The fact that the `L8` lamp is still ON means its mismatch detector for the `B0` bit failed. The most likely cause is that you **forgot to place the Repeater Tap** from the `B0` bus line to the `L8` output wire. Without that tap, the wire never gets powered, and the lamp stays on.

</details>


---


### Practice Problem 4.5.1: Design on Paper

You are programming the line for the digit **`2`**. According to the lookup table, which perpendicular segment lines need a torch tap from the horizontal `L2` line?

The digit `2` uses segments **`a`, `b`, `d`, `e`, and `g`**. Therefore, you would place torch taps at the intersections of the `L2` line and the perpendicular lines for those five segments.

</details>


---


### Practice Problem 4.5.2: Debug Challenge

When you test your encoder by providing a LOW signal to the `L4` line, you expect to see the digit `4` (segments `b, c, f, g`). Instead, the display shows `b, c, f` but **segment `g` remains dark**. What is the most likely cause of this error?

If a segment that should be ON is OFF, it means it is not receiving power. The most likely cause is simple: you **forgot to place the torch tap** at the intersection of the horizontal `L4` line and the perpendicular segment `g` line. Without that torch, there is nothing to power the line when `L4` goes low.

</details>


---


### Practice Problem 4.7.1: Knowledge Check

1.  Why is a two-stage (Decoder → Encoder) design generally better than a single, complex circuit?
2.  What is the purpose of the **Repeater Tap** in our compact decoder? Why can't we just use Redstone dust?
3.  In our Diode Matrix ROM, what does placing a **Torch Tap** at an intersection physically represent?

1.  It breaks the problem down into smaller, independent modules (modularity). This makes each part easier to design, build, and debug.
2.  The Repeater Tap creates a "strongly powered" block, which is necessary to power the Redstone dust on the output line across the 1-block air gap. Simple dust would create a "weakly powered" block, which cannot.
3.  It represents a single "bit" of stored information. Specifically, it's a command to "turn this segment ON when this number line is selected (LOW)."

</details>


---


### Practice Problem 4.7.2: Decoder Design

You want to add a special output line, `LE`, that lights up only for even numbers (`0`, `2`, `4`, `6`, `8`). You realize that for all even numbers, the `B0` bit is always `0`. What is the single tap you would need to build a simple detector for this?

You want the lamp to be ON only when `B0` is `0`. Our active-low system turns the lamp on when the line is unpowered. You would need a single **Repeater Tap** from the `B0` line. When `B0` is `1` (odd), the repeater powers the `LE` line and turns the lamp off. When `B0` is `0` (even), the repeater is off, the line is unpowered, and the lamp turns on.

</details>


---


### Practice Problem 4.7.3: Encoder Design

The letter 'A' can be made with segments `a, b, c, e, f, g`. According to the design of our ROM, which segment line is the *only one* that would **not** have a torch tap placed on it from the `LA` input line?

The line for the letter 'A' would need to activate every segment *except* for segment **`d`**. Therefore, `d` is the only segment line that would not get a torch tap.

</details>


---


### Practice Problem 4.7.4: Reverse Engineering

You see a line in a decoder that has Torch Taps on `B2` and `B1`, and Repeater Taps on `B3` and `B0`. What decimal number is this line designed to detect?

Torches are for `1`s, Repeaters are for `0`s. So the identity is `0110`. This is the binary for decimal **6**.

</details>


---


### Practice Problem 4.7.5: Debug Challenge

In the world download for this module, you will find a section labeled "Module 3 Debug Challenge." The display system is fully connected. When you input **`0010`** (for the number 2), the display incorrectly shows a **`6`**.

**Trace the logic**:
  - The digit `2` should be `a, b, g, e, d`.
  - The digit `6` is `a, c, d, e, f, g`.

What is the single most likely point of failure in the system that would cause this specific error? (Hint: The problem is in the Encoder/ROM).

**The Logic**:
When the input is `2`, the `L2` line from the decoder correctly goes LOW. This is supposed to activate the torches for segments `a, b, d, e, g`.

The display shows a `6`, meaning segments `c` and `f` are ON when they should be OFF, and segment `b` is OFF when it should be ON.

**The Conclusion**:
This points to a catastrophic failure in the "programming" of the `L2` line in your Diode Matrix. You have wired it incorrectly.
-   You have likely **accidentally placed** torch taps from the `L2` line to the segment lines for `c` and `f`.
-   You have likely **forgotten to place** the torch tap from the `L2` line to the segment line for `b`.

</details>


---


### Practice Problem 5.6.1: Knowledge Check
1. In binary, what is `1011` + `0010`?
2. What is the hexadecimal representation of the binary number `1101`?
3. What is the decimal value of the hexadecimal number `$B$`?

1. `` `1101` `` (which is $11+2=13$).
2. `$D$`.
3. `11`.
</details>


---


### Practice Problem 6.5.1: Knowledge Check
1. What is an "overflow error" in the context of our 4-bit adder?
2. In 4-bit Two's Complement, what is the binary representation for `-1`?
3. Which logic gate was the key to creating our controllable inverter?

1. An overflow error occurs when the result of a calculation is a number greater than `15` and requires more than 4 bits to represent.
2. `1111`. (Start with `0001`, invert to `1110`, add 1 to get `1111`).
3. The **XOR** gate.
</details>


---


### Practice Problem 6.5.2: The Word Problem
You perform the calculation `$D - 5$` (hex) which is $13 - 5$ (decimal).
1. What is the 4-bit Two's Complement representation of `-5`?
2. What is the 5-bit binary result when you add `1101` (13) and your answer from part 1?
3. What is the final 4-bit answer after discarding the carry?

1. `-5` is `1011`. (Start with `0101`, invert to `1010`, add 1).
2. `1101` + `1011` = `11000`.
3. The final answer is `1000`, which is `8` in decimal.
</details>


---


### Practice Problem 7.5.1: Knowledge Check
1. Why are status flags generally more efficient than dedicated comparator circuits in a real CPU?
2. What calculation would a CPU perform to check if `$A > B$`? What flag would it look at?
3. What is the logic gate used to create the Zero Flag circuit?

1. Status flags allow the CPU to get many pieces of information (zero, negative, carry, overflow) from a single arithmetic operation (like subtraction), rather than needing separate, bulky hardware for every possible comparison.
2. It would calculate `$B - A$`. If the **Negative Flag** is `1`, it means the result was negative, which means that $A$ must have been greater than $B$.
3. A **NOR** gate.
</details>


---


### Practice Problem 7.5.2: Design Challenge
Design a circuit that detects if a 4-bit number is the specific value `` `1111` `` (`15` decimal). What single logic gate can accomplish this?

To check if all four bits ($Y_3, Y_2, Y_1, Y_0$) are `1`, you would need a single **4-input AND gate**. Its output will only be `1` if all of its inputs are `1`.
</details>


---


### Practice Problem 8.4.1: Knowledge Check
1. In plain English, what does a Multiplexer do?
2. If we want to build a MUX that can select between *four* different 4-bit buses, how many select lines would we need?
3. What is the Boolean expression for a 2-to-1 MUX?

1. A Multiplexer (or MUX) selects one of several data inputs and forwards it to a single output.
2. We would need **two** select lines. To represent four choices (0, 1, 2, 3), you need 2 bits (`` `00` ``, `` `01` ``, `` `10` ``, `` `11` ``).
3. $Y = (A \land \neg S) \lor (B \land S)$
</details>


---


### Practice Problem 8.4.2: The Demultiplexer
A **Demultiplexer (DEMUX)** does the opposite of a MUX. It takes one data input and routes it to one of many possible outputs, based on a select line. Sketch out a logic diagram for a 1-to-2 DEMUX with one data input ($D$), one select line ($S$), and two outputs ($Y_0$ and $Y_1$).

**Logic:**
- If $S=0$, then $Y_0$ should equal $D$, and $Y_1$ should be `0`. The expression is $Y_0 = D \land \neg S$.
- If $S=1$, then $Y_1$ should equal $D$, and $Y_0$ should be `0`. The expression is $Y_1 = D \land S$.

**Diagram:**
![1-to-2 DEMUX CircuitVerse Diagram](./images/demux-circuitverse.png)
*Figure: A 1-to-2 DEMUX. The data input D is sent to two AND gates. The select line S (and its inverse) determines which of the AND gates opens to let the data through to its corresponding output.*

</details>


---


### Practice Problem 9.5.1: Knowledge Check
1. In a bitwise ALU, why are all calculations performed in parallel?
2. What is the purpose of the decoder in the MUX control circuit?
3. If our ALU result is `` `1000` ``, what will the state of the Z and N flags be?

1. It's simpler to have all units working at once and then select the desired output, rather than trying to build complex logic to turn the different units on and off.
2. The decoder takes the binary "opcode" from the select lines and turns it into a single "active" line to open the correct AND gatekeepers in the multiplexer.
3. The Z (Zero) flag will be `0` because the result is not `0000`. The N (Negative) flag will be `1` because the most significant bit is `1`.
</details>


---


### Practice Problem 9.5.2: The Expansion
You want to add a new function to your ALU: `NOT A`. You assign it the opcode `` `11` ``. Describe the steps you would need to take to add this new lane.

1. **Build the Lane:** Build a new "calculation lane" that consists of four NOT gates, taking its input from the 4-bit Bus A.
2. **Expand the MUX:** For each of the four output bits, you would need to add a fifth AND gate to the final OR gate.
3. **Connect the Lane:** This new AND gate would take its data input from one bit of your new `NOT A` lane, and its control input from the `` `11` `` output of your 2-to-4 decoder.
</details>


---


### Practice Problem 10.3.1: Knowledge Check
1. What is the key difference between a combinational circuit and a sequential circuit?
2. What is the purpose of a "feedback loop" in memory circuits?
3. What is the role of the "Write Enable" line on a Gated D-Latch?

1. A **combinational** circuit's output depends only on its current inputs. A **sequential** circuit's output depends on its current inputs *and* its previous state (it has memory).
2. A feedback loop, where a gate's output is connected back to its input, is what allows a circuit to hold its state and "remember" a value even after the initial input is gone.
3. The "Write Enable" line acts as a gatekeeper. When it is ON, the latch is "open" and copies its data input. When it is OFF, the latch is "closed" and holds its current value, ignoring the data input.
</details>


---


### Practice Problem 10.3.2: The RS Latch
The circuit that forms the core of our D-Latch is often an **RS Latch**, built from two cross-coupled NOR gates. It has two inputs: $S$ (Set) and $R$ (Reset). Pulsing $S$ forces the output $Q$ to `1`. Pulsing $R$ forces $Q$ to `0`. What do you think happens if you pulse both $S$ and $R$ at the same time? Why might this be considered an "invalid" or "forbidden" state?

If both $S$ and $R$ inputs on a NOR-based RS Latch are set to `1`, both NOR gates will be forced to output `0`. This means both the $Q$ and $\neg Q$ outputs would be `0`, which violates the rule that they must be opposites. When the inputs are then returned to `0`, the latch enters an unpredictable "race condition," and it's impossible to know what state it will settle in. This is why the Gated D-Latch is a safer, more predictable design.
</details>


---


### Practice Problem 11.3.1: Knowledge Check
1. In the term "16x4-bit RAM," what does the "16" represent, and what does the "4" represent?
2. What is the role of the decoder in a RAM module?
3. Why is the `Write Enable` signal necessary? What problem does it solve?

1. The "16" represents the number of unique memory locations or addresses. The "4" represents the number of bits that can be stored at each of those locations.
2. The decoder takes the binary address from the Address Bus and activates a single "select line" to choose which of the many registers will be active for a read or write operation.
3. The `Write Enable` signal is necessary to differentiate between reading from and writing to a memory address. When it's OFF, the selected register outputs its data but doesn't change it. When it's ON, the selected register overwrites its current data with the data from the Data In bus.
</details>


---


### Practice Problem 11.3.2: The Expansion
You want to upgrade your computer's memory from 16x4-bit to **256x4-bit**.
1. How many registers would you need to build?
2. How many bits would your Address Bus need to be to select one of 256 unique addresses?
3. What kind of decoder would you need?

1. You would need **256** individual 4-bit registers.
2. To represent 256 unique values ($2^8$), your Address Bus would need to be **8 bits** wide.
3. You would need an **8-to-256 decoder**.
</details>


---


### Practice Problem 12.5.1: Knowledge Check
1. What are the three steps of the Fetch-Decode-Execute cycle?
2. What is the difference between the Program Counter and the Instruction Register?
3. What is the key hardware component that makes a conditional jump (like `JIZ`) possible?

1. **Fetch:** Get the instruction from memory. **Decode:** Determine what the instruction means. **Execute:** Activate the correct components to perform the instruction.
2. The **Program Counter (PC)** holds the address of the *next* instruction to be fetched. The **Instruction Register (IR)** holds the *current* instruction that is being decoded and executed.
3. The **Status Flags** (specifically, the Zero Flag in this case). The Control Unit's decision to jump is based on the state of this flag.
</details>


---


### Practice Problem 12.5.2: The Programmer
Write the RU-v1 assembly code for a program that calculates `$5 - 3$` and stores the result in RAM address `10`.

```assembly
LDI A, 5     // Load the number 5 into Register A
LDI B, 3     // Load the number 3 into Register B
SUB          // Subtract B from A
STA     // Store the result in RAM address 10 (0xA)
HLT          // Halt
```
</details>


---


### Practice Problem 13.4.1: Knowledge Check
1. What is the core problem that a Binary-to-BCD converter solves?
2. What is Binary Coded Decimal (BCD)?
3. Why is a ROM-based approach a good choice for this problem in Minecraft, even if it's not the most component-efficient?

1. It solves the problem of converting a pure binary number (like `` `1101` ``) into a format where each decimal digit is represented by its own separate binary code (like `0001` and `0011`).
2. BCD is a system where each decimal digit (`0`-`9`) is encoded with its own dedicated 4-bit binary number.
3. The ROM-based approach is a "brute-force" lookup table. While large, its logic is extremely simple and repetitive, making it much easier to design, build, and debug in a block-based environment like Minecraft compared to a complex, multi-stage sequential circuit.
</details>


---


### Practice Problem 13.4.2: The Programmer
If you had a 4-bit binary number stored in a variable in Python, how could you calculate the TENS and ONES digits using software?

You would use the integer division (`//`) and modulo (`%`) operators. These are the software equivalents of the complex hardware you just built.
```python
binary_input = 13 # This is the decimal value of `1101`

tens_digit = binary_input // 10
ones_digit = binary_input % 10

print(f"Tens: {tens_digit}, Ones: {ones_digit}") # Output: Tens: 1, Ones: 3
```
</details>


---

