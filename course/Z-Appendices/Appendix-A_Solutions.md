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

