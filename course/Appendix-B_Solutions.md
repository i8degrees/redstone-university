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

**Minecraft Circuit**: Place a torch on B’s block for NOT B. Merge A and NOT B with dust for OR. Invert the result with another torch for NOT (NOT A OR B). Connect to a lamp and test all combinations.

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

#### Solution for ##### Practice Problems & Challenges

**Answer:** 0

---

#### Solution for ##### Practice Problems & Challenges

**Answer:** 0

---

#### Solution for ##### Practice Problems & Challenges

**Answer:** XNOR

---

#### Solution for ##### Practice Problems & Challenges

**Simplify (A AND B) OR (A AND NOT B)**:
        1. Factor out A: `A AND (B OR NOT B)`.
        2. Since `B OR NOT B = 1`, the expression becomes `A AND 1 = A`.
        **Answer**: `A`.

---

#### Solution for ##### Practice Problems & Challenges

`B NOR C = NOT (B OR C) = NOT (0 OR 1) = NOT 1 = 0`
        `A NAND 0 = NOT (A AND 0) = NOT 0 = 1`

---

#### Solution for ##### Practice Problems & Challenges

Any Boolean function can be built using only NOR gates.

---

#### Solution for ##### Practice Problems & Challenges

The NOT gates needed to invert the AND output in the XOR construction are missing.

---

#### Solution for ##### Practice Problems & Challenges

Use De Morgan’s Law:
        - `A AND B = NOT (NOT A OR NOT B)`
        - `NOT A AND C = NOT (A OR NOT C)`
        - Combine with OR: `[NOT (NOT A OR NOT B)] OR [NOT (A OR NOT C)]`

---

#### Solution for ##### Practice Problems & Challenges

```python
        def find_two_unique(numbers):
            xor_result = 0
            for num in numbers:
                xor_result ^= num
            set_bit = xor_result & -xor_result
            num1, num2 = 0, 0
            for num in numbers:
                if num & set_bit:
                    num1 ^= num
                else:
                    num2 ^= num
            return num1, num2
        # Example: [2, 4, 3, 6, 4, 2] → 3, 6
        print(find_two_unique([2, 4, 3, 6, 4, 2]))
        ```
        **Explanation:** XOR all numbers to get XOR of the two unique numbers. Use a set bit to split numbers into two groups, then XOR each group to find the unique numbers.

---
