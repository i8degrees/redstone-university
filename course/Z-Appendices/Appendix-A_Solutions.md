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

1. What is the largest number a `5`-bit input interface could input? (Hint: The next bit would be the `16`s place).
2. What is the decimal value of the binary number `1100`?
3. How would you represent the number `10` in binary?

1. The largest number a `5`-bit input interface could input is **`31`**. (In binary: `11111`, which is `$16 + 8 + 4 + 2 + 1 = 31$`.)
2. The decimal value of the binary number `1100` is **`12`**. (`8 + 4 + 0 + 0 = 12`.)
3. The number `10` in binary is **`1010`**. (`8 + 0 + 2 + 0 = 10`.)

</details>


---


### Practice Problem 2.2.1: Boolean Expression Evaluation

Given the Boolean expression $A \text{ OR } \text{NOT } B$ ($A \lor \neg B$), evaluate the output for all possible input combinations (`A`, `B` = `0,0`; `0,1`; `1,0`; `1,1`) and create a truth table. Then, build a Minecraft circuit to verify your results.

**Truth Table for $A \text{ OR } \text{NOT } B$ ($A \lor \neg B$):**

| A | B | !B | A OR !B |
| $A$ | $B$ | $\neg B$ | $A \lor \neg B$ |
|---|---|----|---------|
| `0` | `0` |  `1` |    `1`    |
| `0` | `1` |  `0` |    `0`    |
| `1` | `0` |  `1` |    `1`    |
| `1` | `1` |  `0` |    `1`    |

**Minecraft Circuit**: Use a lever for `A`, a lever for `B`, a redstone torch on `B`’s block for `!B`, merge `A` and `!B` with dust for OR, and connect to a lamp for output. Test all combinations to verify.
</details>


---


### Practice Problem 2.2.2: Logic Gate Design Challenge

Design a circuit that implements the logic $A \text{ AND } \text{NOT } B$ ($A \land \neg B$) using only the NOT and OR primitives (no direct AND gate). Build it in Minecraft and verify with a truth table for all input combinations (`A`, `B` = `0,0`; `0,1`; `1,0`; `1,1`).

**Truth Table for $A \text{ AND } \text{NOT } B$ ($A \land \neg B$):**

| A | B | !B | A AND !B |
| $A$ | $B$ | $\neg B$ | $A \land \neg B$ |
|---|---|----|----------|
| `0` | `0` |  `1` |    `0`     |
| `0` | `1` |  `0` |    `0`     |
| `1` | `0` |  `1` |    `1`     |
| `1` | `1` |  `0` |    `0`     |

**Boolean Expression**: $A \text{ AND } \text{NOT } B = \text{NOT } (\text{NOT } A \text{ OR } B)$ ($A \land \neg B = \neg(\neg A \lor B)$) (by De Morgan’s Law).

**Minecraft Circuit**: Invert `A` to get `!A`. Then, take `!A` and the original `B` and feed them into an OR gate. Finally, invert the result of that OR gate.
</details>


---


### Practice Problem 2.3.1: Circuit Simplification Challenge

Given the expression $(A \text{ OR } B) \text{ AND } (\text{NOT } A \text{ OR } \text{NOT } B)$ [$(A \lor B) \land (\neg A \lor \neg B)$], simplify it using Boolean laws. Show all steps.

**Simplification Steps:**
1. Start with $(A \lor B) \land (\neg A \lor \neg B)$.
2. Apply De Morgan’s Law to the second term: $\neg A \lor \neg B = \neg(A \land B)$.
3. The expression becomes $(A \lor B) \land \neg(A \land B)$.
4. Distribute: $(A \land \neg(A \land B)) \lor (B \land \neg(A \land B))$.
5. Simplify each term:
   - $A \land \neg(A \land B) = A \land (\neg A \lor \neg B) = (A \land \neg A) \lor (A \land \neg B) = 0 \lor (A \land \neg B) = A \land \neg B$.
   - Similarly, $B \land \neg(A \land B) = B \land \neg A$.
6. Final expression: $(A \land \neg B) \lor (\neg A \land B)$, which is $A \text{ XOR } B$ ($A \oplus B$).
</details>


---


### Practice Problem 2.4.1: Two-Switch Light System

Design a Minecraft circuit for a two-switch light system where flipping either switch toggles the light’s state (on to off, or off to on). Use only `NOT` and `OR` gates to implement the $A \text{ XOR } B$ ($A \oplus B$) logic.

**Logic:** The light should be ON when exactly one switch is ON ($A \text{ XOR } B$).

**Truth Table:**

| A | B | Light (A XOR B) |
| $A$ | $B$ | Light ($A \oplus B$) |
|---|---|-----------------|
| `0` | `0` |        `0`        |
| `0` | `1` |        `1`        |
| `1` | `0` |        `1`        |
| `1` | `1` |        `0`        |

**Minecraft Circuit:** Build the XOR circuit from Lesson 2.4 (using `NOT` and `OR` gates). Connect levers for `A` and `B`, and a lamp for the output. Test by flipping each lever and verifying the lamp toggles.
</details>


---


### Practice Problem 2.5.1: The Missing Number Challenge

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

---

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


### Practice Problem 2.6.1: Universal Gate Challenge with NOR Gates

Build an $A \text{ AND } B$ ($A \land B$) gate using only NOR gates. Verify it with a truth table in Minecraft for all input combinations (`A`, `B` = `0,0`; `0,1`; `1,0`; `1,1`).

**Logic:** $A \land B = (A \text{ NOR } A) \text{ NOR } (B \text{ NOR } B)$

**Truth Table:**

| A | B | A NOR A | B NOR B | (A NOR A) NOR (B NOR B) |
| $A$ | $B$ | $A \text{ NOR } A$ | $B \text{ NOR } B$ | $(A \text{ NOR } A) \text{ NOR } (B \text{ NOR } B)$ |
|---|---|---------|---------|-------------------------|
| `0` | `0` |    `1`    |    `1`    |            `0`            |
| `0` | `1` |    `1`    |    `0`    |            `0`            |
| `1` | `0` |    `0`    |    `1`    |            `0`            |
| `1` | `1` |    `0`    |    `0`    |            `1`            |

**Minecraft Circuit:** Build three NOR gates using redstone dust mergers and torches. Connect levers for `A` and `B`, and a lamp for the output. Test all combinations to verify AND behavior.
</details>


---


### Practice Problem 2.8.1: Knowledge Check

Test your core understanding with these rapid-fire questions.

1.  What is the key difference in the output of an `OR` gate versus an `XOR` gate?
2.  Which two gates are considered "universal," and what is the name of this property?
3.  Using De Morgan's Law, what is the equivalent expression for `!(A OR B)`?

1.  An **OR** gate outputs `1` if *at least one* input is `1`. An **XOR** gate outputs `1` only if the inputs are *different*.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is `!A AND !B`.

</details>


---


### Practice Problem 2.8.2: The Word Problem

Apply the laws of Boolean algebra to solve these challenges on paper.

A greenhouse has an automated climate control system. An alarm `Y` should sound if the following conditions are met:
*   The system is in "Manual Override" mode (`M` is `True`), **OR**
*   The Temperature `T` is too high **AND** the Water Sprinklers `W` have failed to turn on (`W` is `False`).

Write the single Boolean expression for the alarm $Y$ using dual notation.

The expression translates directly from the requirements:

`Y = M OR (T AND !W)`

The parentheses are crucial to ensure the `AND` condition is evaluated before being `OR`'d with the manual override switch.

</details>


---


### Practice Problem 2.8.3: The Simplification

An engineer has designed a circuit with the expression: `Y = (A AND B) OR (A AND !B) OR (!A AND B)`.

This seems to require three AND gates and two OR gates. Simplify this expression to its most efficient form using Boolean laws.

1.  **Start with the expression:** $Y = (A \land B) \lor (A \land \neg B) \lor (\neg A \land B)$
2.  **Look for common terms to factor:** The first two terms both contain $A$. Let's factor it out using the Distributive Law.
    *   $A \land (B \lor \neg B)$
3.  **Apply the Inverse Law:** We know that $B \lor \neg B$ is always $1$.
    *   So, the first part simplifies to $A \land 1$, which is just $A$.
4.  **Rewrite the expression:** Our expression is now much simpler: $Y = A \lor (\neg A \land B)$
5.  **Apply the Distributive Law again (in a less obvious way):** The law $(X \lor Y) \land (X \lor Z) = X \lor (Y \land Z)$ can be applied here. Let $X = A$.
    *   We can expand $A \lor (\neg A \land B)$ into $(A \lor \neg A) \land (A \lor B)$.
6.  **Apply the Inverse Law again:** We know that $A \lor \neg A$ is always $1$.
    *   The expression becomes: $Y = 1 \land (A \lor B)$
7.  **Apply the Identity Law:** $1 \land$ anything is just the anything.
    *   The final, simplified expression is: $Y = A \text{ OR } B$ ($A \lor B$).

The entire complex circuit simplifies down to a single OR gate!

</details>


---


### Practice Problem 3.4.1: Design on Paper

Before you build, an engineer must be able to plan. For output line **`L6` (Identity: `0110`)**, what taps would you need? List out which type of tap (Repeater or Torch) is required for each of the four bus lines (`B3`, `B2`, `B1`, `B0`).

Applying our rule:
-   `B3` is `0`: Requires a **Repeater Tap**.
-   `B2` is `1`: Requires a **Torch Tap**.
-   `B1` is `1`: Requires a **Torch Tap**.
-   `B0` is `0`: Requires a **Repeater Tap**.

</details>


---


### Practice Problem 3.4.2: Debug Challenge

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


### Practice Problem 3.5.1: Design on Paper

You are programming the line for the digit **`2`**. According to the lookup table, which perpendicular segment lines need a torch tap from the horizontal `L2` line?

The digit `2` uses segments **`a`, `b`, `d`, `e`, and `g`**. Therefore, you would place torch taps at the intersections of the `L2` line and the perpendicular lines for those five segments.

</details>


---


### Practice Problem 3.5.2: Debug Challenge

When you test your encoder by providing a LOW signal to the `L4` line, you expect to see the digit `4` (segments `b, c, f, g`). Instead, the display shows `b, c, f` but **segment `g` remains dark**. What is the most likely cause of this error?

If a segment that should be ON is OFF, it means it is not receiving power. The most likely cause is simple: you **forgot to place the torch tap** at the intersection of the horizontal `L4` line and the perpendicular segment `g` line. Without that torch, there is nothing to power the line when `L4` goes low.

</details>


---


### Practice Problem 3.7.1: Knowledge Check

1.  Why is a two-stage (Decoder → Encoder) design generally better than a single, complex circuit?
2.  What is the purpose of the **Repeater Tap** in our compact decoder? Why can't we just use Redstone dust?
3.  In our Diode Matrix ROM, what does placing a **Torch Tap** at an intersection physically represent?

1.  It breaks the problem down into smaller, independent modules (modularity). This makes each part easier to design, build, and debug.
2.  The Repeater Tap creates a "strongly powered" block, which is necessary to power the Redstone dust on the output line across the 1-block air gap. Simple dust would create a "weakly powered" block, which cannot.
3.  It represents a single "bit" of stored information. Specifically, it's a command to "turn this segment ON when this number line is selected (LOW)."

</details>


---


### Practice Problem 3.7.2: Decoder Design

You want to add a special output line, `LE`, that lights up only for even numbers (`0`, `2`, `4`, `6`, `8`). You realize that for all even numbers, the `B0` bit is always `0`. What is the single tap you would need to build a simple detector for this?

You want the lamp to be ON only when `B0` is `0`. Our active-low system turns the lamp on when the line is unpowered. You would need a single **Repeater Tap** from the `B0` line. When `B0` is `1` (odd), the repeater powers the `LE` line and turns the lamp off. When `B0` is `0` (even), the repeater is off, the line is unpowered, and the lamp turns on.

</details>


---


### Practice Problem 3.7.3: Encoder Design

The letter 'A' can be made with segments `a, b, c, e, f, g`. According to the design of our ROM, which segment line is the *only one* that would **not** have a torch tap placed on it from the `LA` input line?

The line for the letter 'A' would need to activate every segment *except* for segment **`d`**. Therefore, `d` is the only segment line that would not get a torch tap.

</details>


---


### Practice Problem 3.7.4: Reverse Engineering

You see a line in a decoder that has Torch Taps on `B2` and `B1`, and Repeater Taps on `B3` and `B0`. What decimal number is this line designed to detect?

Torches are for `1`s, Repeaters are for `0`s. So the identity is `0110`. This is the binary for decimal **6**.

</details>


---


### Practice Problem 3.7.5: Debug Challenge

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

