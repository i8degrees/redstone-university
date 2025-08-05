<hr class="pagebreak"/>

### Appendix B: Solutions to Exercises

---

#### Solution for ##### Practice Problem: Boolean Expression Evaluation

**Truth Table for A OR NOT B**:

| A | B | NOT B | A OR NOT B |
|---|---|-------|------------|
| 0 | 0 |   1   |     1      |
| 0 | 1 |   0   |     0      |
| 1 | 0 |   1   |     1      |
| 1 | 1 |   0   |     1      |

**Minecraft Circuit**: Use a lever for A, a lever for B, a redstone torch on B’s block for NOT B, merge A and NOT B with dust for OR, and connect to a lamp for output. Test all combinations to verify.

---

#### Solution for ##### Practice Problem: Logic Gate Design Challenge

**Truth Table for A AND NOT B**:

| A | B | NOT B | A AND NOT B |
|---|---|-------|-------------|
| 0 | 0 |   1   |      0      |
| 0 | 1 |   0   |      0      |
| 1 | 0 |   1   |      1      |
| 1 | 1 |   0   |      0      |

**Boolean Expression**: `A AND NOT B = !(NOT A OR B)` (by De Morgan’s Law).

**Minecraft Circuit**: Invert A to get !A. Then, take !A and the original B and feed them into an OR gate. Finally, invert the result of that OR gate.

---

#### Solution for ##### Practice Problem: Circuit Simplification Challenge

**Simplification Steps:**
1. Start with `(A OR B) AND (NOT A OR NOT B)`.
2. Apply De Morgan’s Law to the second term: `NOT A OR NOT B = NOT (A AND B)`.
3. The expression becomes `(A OR B) AND NOT (A AND B)`.
4. Distribute: `(A AND NOT (A AND B)) OR (B AND NOT (A AND B))`.
5. Simplify each term:
   - `A AND NOT (A AND B) = A AND (NOT A OR NOT B) = (A AND NOT A) OR (A AND NOT B) = 0 OR (A AND NOT B) = A AND NOT B`.
   - Similarly, `B AND NOT (A AND B) = B AND NOT A`.
6. Final expression: `(A AND NOT B) OR (B AND NOT A)`, which is `A XOR B`.

**Minecraft Circuit**: Build the XOR circuit from Lesson 2.4, as it’s equivalent. Compare it to the original, which requires more blocks and dust.

---

#### Solution for ##### Practice Problem: Two-Switch Light System

**Logic:** The light should be ON when exactly one switch is ON (A XOR B).

**Truth Table:**

| A | B | Light (A XOR B) |
|---|---|-----------------|
| 0 | 0 |        0        |
| 0 | 1 |        1        |
| 1 | 0 |        1        |
| 1 | 1 |        0        |

**Minecraft Circuit:** Build the XOR circuit from Lesson 2.4 (using NOT and OR gates). Connect levers for A and B, and a lamp for the output. Test by flipping each lever and verifying the lamp toggles.

---

#### Solution for #### **Lesson 2.5: Software Superpowers – The XOR Trick for Programmers**

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

---

#### Solution for ##### Practice Problem: Universal Gate Challenge with NOR Gates

**Logic:** `A AND B = (A NOR A) NOR (B NOR B)`

**Truth Table:**

| A | B | A NOR A | B NOR B | (A NOR A) NOR (B NOR B) |
|---|---|---------|---------|-------------------------|
| 0 | 0 |    1    |    1    |            0            |
| 0 | 1 |    1    |    0    |            0            |
| 1 | 0 |    0    |    1    |            0            |
| 1 | 1 |    0    |    0    |            1            |

**Minecraft Circuit:** Build three NOR gates using redstone dust mergers and torches. Connect levers for A and B, and a lamp for the output. Test all combinations to verify AND behavior.

---

#### Solution for ##### Part 1: Knowledge Check

1.  An **OR** gate outputs `1` if *at least one* input is `1`. An **XOR** gate outputs `1` only if the inputs are *different*.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is `!A AND !B`.

---

#### Solution for ###### Puzzle 1: The Word Problem

The expression translates directly from the requirements:

`Y = M OR (T AND !W)`

The parentheses are crucial to ensure the `AND` condition is evaluated before being `OR`'d with the manual override switch.

---

#### Solution for ###### Puzzle 2: The Simplification

1.  **Start with the expression:** `Y = (A AND B) OR (A AND !B) OR (!A AND B)`
2.  **Look for common terms to factor:** The first two terms both contain `A`. Let's factor it out using the Distributive Law.
    *   `A AND (B OR !B)`
3.  **Apply the Inverse Law:** We know that `B OR !B` is always `1`.
    *   So, the first part simplifies to `A AND 1`, which is just `A`.
4.  **Rewrite the expression:** Our expression is now much simpler: `Y = A OR (!A AND B)`
5.  **Apply the Distributive Law again (in a less obvious way):** The law `(X OR Y) AND (X OR Z) = X OR (Y AND Z)` can be applied here. Let `X = A`.
    *   We can expand `A OR (!A AND B)` into `(A OR !A) AND (A OR B)`.
6.  **Apply the Inverse Law again:** We know that `A OR !A` is always `1`.
    *   The expression becomes: `Y = 1 AND (A OR B)`
7.  **Apply the Identity Law:** `1 AND` anything is just the anything.
    *   The final, simplified expression is: `Y = A OR B`.

The entire complex circuit simplifies down to a single OR gate!

---
