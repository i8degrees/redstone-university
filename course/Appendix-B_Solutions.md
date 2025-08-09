<hr class="pagebreak"/>

### Appendix B: Solutions to Exercises

---

## Part I: The Foundations, Speaking to the Machine

### Module 2: The Language of Logic – A Deep Dive into Boolean Algebra

**<strong>Solution: Boolean Expression Evaluation</strong>**

**Truth Table for A OR !B**:

| A | B | !B | A OR !B |
|---|---|----|---------|
| 0 | 0 |  1 |    1    |
| 0 | 1 |  0 |    0    |
| 1 | 0 |  1 |    1    |
| 1 | 1 |  0 |    1    |

**Minecraft Circuit**: Use a lever for A, a lever for B, a redstone torch on B’s block for !B, merge A and !B with dust for OR, and connect to a lamp for output. Test all combinations to verify.

---

**<strong>Solution: A AND !B Circuit</strong>**

**Truth Table for A AND !B**:

| A | B | !B | A AND !B |
|---|---|----|----------|
| 0 | 0 |  1 |    0     |
| 0 | 1 |  0 |    0     |
| 1 | 0 |  1 |    1     |
| 1 | 1 |  0 |    0     |

**Boolean Expression**: `A AND !B = !(!A OR B)` (by De Morgan’s Law).

**Minecraft Circuit**: Invert A to get !A. Then, take !A and the original B and feed them into an OR gate. Finally, invert the result of that OR gate.

---

**<strong>Solution: Simplifying (A OR B) AND (NOT A OR NOT B)</strong>**

**Simplification Steps:**
1. Start with `(A OR B) AND (!A OR !B)`.
2. Apply De Morgan’s Law to the second term: `!A OR !B = !(A AND B)`.
3. The expression becomes `(A OR B) AND !(A AND B)`.
4. Distribute: `(A AND !(A AND B)) OR (B AND !(A AND B))`.
5. Simplify each term:
   - `A AND !(A AND B) = A AND (!A OR !B) = (A AND !A) OR (A AND !B) = 0 OR (A AND !B) = A AND !B`.
   - Similarly, `B AND !(A AND B) = B AND !A`.
6. Final expression: `(A AND !B) OR (!A AND B)`, which is `A XOR B`.

---

**<strong>Solution: Two-Switch Light System</strong>**

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

**<strong>Click here for the solution and explanation</strong>**

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

**<strong>Solution: AND Gate Using NOR Gates</strong>**

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

**<strong>Click for answers</strong>**

1.  An **OR** gate outputs `1` if *at least one* input is `1`. An **XOR** gate outputs `1` only if the inputs are *different*.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is `!A AND !B`.

---

**<strong>Click for the solution</strong>**

The expression translates directly from the requirements:

`Y = M OR (T AND !W)`

The parentheses are crucial to ensure the `AND` condition is evaluated before being `OR`'d with the manual override switch.

---

**<strong>Click for the step-by-step proof</strong>**

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

### Module 3: From Binary to Pictures - Building a Digital Display

**<strong>Solution: Taps for L6 (`0110`)</strong>**

Applying our rule:
-   `B3` is `0`: Requires a **Repeater Tap**.
-   `B2` is `1`: Requires a **Torch Tap**.
-   `B1` is `1`: Requires a **Torch Tap**.
-   `B0` is `0`: Requires a **Repeater Tap**.

---

**<strong>Solution: Debugging the L8 and L9 Error</strong>**

**The Logic:** The `L8` lamp should turn OFF when the input is `1001`. For `L8` to turn off, its wire needs to be powered. This means one of its "mismatch" taps must have activated.

**The Identity of `L8` is `1000`.** Let's compare this to the input `1001`.
-   `B3` is `1`, `L8` expects `1`. No mismatch.
-   `B2` is `0`, `L8` expects `0`. No mismatch.
-   `B1` is `0`, `L8` expects `0`. No mismatch.
-   `B0` is `1`, `L8` expects `0`. **This is a mismatch.**

The tap for `B0` on the `L8` line is supposed to detect this mismatch and power the `L8` wire. Since `L8` expects a `0` for `B0`, the rule says it must have a **Repeater Tap**.

**The Conclusion:** The fact that the `L8` lamp is still ON means its mismatch detector for the `B0` bit failed. The most likely cause is that you **forgot to place the Repeater Tap** from the `B0` bus line to the `L8` output wire. Without that tap, the wire never gets powered, and the lamp stays on.

---

**<strong>Click for answers</strong>**

1.  It breaks the problem down, making it easier to design, build, and debug each part independently (modularity).
2.  The Repeater Tap creates a "strongly powered" block, which is necessary to power the Redstone dust on the output line across the 1-block air gap. Simple dust would create a "weakly powered" block, which cannot.
3.  It represents a single "bit" of stored information. Specifically, it's a command to "turn this segment OFF for this number."

---

**<strong>Click for solutions</strong>**

1.  You want the lamp to be ON only when `B0` is `0`. Our active-low system turns the lamp on when the line is unpowered. You would need a single **Repeater Tap** from the `B0` line. When `B0` is `1` (odd), the repeater powers the `LE` line and turns the lamp off. When `B0` is `0` (even), the repeater is off, the line is unpowered, and the lamp turns on.
2.  The `LA` line would need to suppress the torch for the segment that is OFF: only segment **`d`**.
3.  Torches are for `1`s, Repeaters are for `0`s. So the identity is `0110`. This is the binary for decimal **6**.

---

**<strong>Click for the solution</strong>**

**The Logic:**
When the input is `2`, the `L2` line from the decoder correctly goes LOW. The `L2` line is supposed to stop suppressing the torches for segments `a,b,d,e,g` and continue suppressing the torches for `c` and `f`.

The display shows a `6`, meaning segments `c` and `f` are ON when they should be OFF, and segment `b` is OFF when it should be ON.

**The Conclusion:**
This points to a catastrophic failure in the "programming" of the `L2` line in your Diode Matrix. You have wired it incorrectly.
-   The connections from the `L2` line to the `c` and `f` segment torches are likely **missing**.
-   You have likely **accidentally added** a connection from the `L2` line to the `b` segment torch.

---
