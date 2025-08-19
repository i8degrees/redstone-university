<hr class="pagebreak"/>

## Appendix A: Solutions

This appendix provides solutions to the quizzes, logic puzzles, and debug challenges in the Redstone University curriculum, organized by module and lesson. Each solution is labeled with its problem ID (Module.Lesson.Problem) for easy reference, with a footnote indicating the module where it appears.


## From Binary to Pictures - Building a Digital Display [3]

### Module 3 Checkpoint

#### 3.7.1: Knowledge Check

1.  It breaks the problem down into smaller, independent modules (modularity). This makes each part easier to design, build, and debug.
2.  The Repeater Tap creates a "strongly powered" block, which is necessary to power the Redstone dust on the output line across the 1-block air gap. Simple dust would create a "weakly powered" block, which cannot.
3.  It represents a single "bit" of stored information. Specifically, it's a command to "turn this segment ON when this number line is selected (LOW)."

---

#### 3.7.2: Decoder Design

You want the lamp to be ON only when `B0` is `0`. Our active-low system turns the lamp on when the line is unpowered. You would need a single **Repeater Tap** from the `B0` line. When `B0` is `1` (odd), the repeater powers the `LE` line and turns the lamp off. When `B0` is `0` (even), the repeater is off, the line is unpowered, and the lamp turns on.

---

#### 3.7.3: Encoder Design

The line for the letter 'A' would need to activate every segment *except* for segment **`d`**. Therefore, `d` is the only segment line that would not get a torch tap.

---

#### 3.7.4: Reverse Engineering

Torches are for `1`s, Repeaters are for `0`s. So the identity is `0110`. This is the binary for decimal **6**.

---

#### 3.7.5: Debug Challenge

**The Logic:**
When the input is `2`, the `L2` line from the decoder correctly goes LOW. This is supposed to activate the torches for segments `a, b, d, e, g`.

The display shows a `6`, meaning segments `c` and `f` are ON when they should be OFF, and segment `b` is OFF when it should be ON.

**The Conclusion:**
This points to a catastrophic failure in the "programming" of the `L2` line in your Diode Matrix. You have wired it incorrectly.
-   You have likely **accidentally placed** torch taps from the `L2` line to the segment lines for `c` and `f`.
-   You have likely **forgotten to place** the torch tap from the `L2` line to the segment line for `b`.

---

### The Decoder Lab, Part 2: An Elegant, Compact Solution

#### 3.4.1: Design on Paper

Applying our rule:
-   `B3` is `0`: Requires a **Repeater Tap**.
-   `B2` is `1`: Requires a **Torch Tap**.
-   `B1` is `1`: Requires a **Torch Tap**.
-   `B0` is `0`: Requires a **Repeater Tap**.

---

#### 3.4.2: Debug Challenge

**The Logic:** The $L_8$ lamp should turn OFF when the input is $1001$. For $L_8$ to turn off, its wire needs to be powered. This means one of its "mismatch" taps must have activated.

**The Identity of `L8` is `1000`.** Let's compare this to the input `1001`.
-   `B3` is `1`, `L8` expects `1`. No mismatch.
-   `B2` is `0`, `L8` expects `0`. No mismatch.
-   `B1` is `0`, `L8` expects `0`. No mismatch.
-   `B0` is `1`, `L8` expects `0`. **This is a mismatch.**

The tap for `B0` on the `L8` line is supposed to detect this mismatch and power the `L8` wire. Since `L8` expects a `0` for `B0`, the rule says it must have a **Repeater Tap**.

**The Conclusion:** The fact that the `L8` lamp is still ON means its mismatch detector for the `B0` bit failed. The most likely cause is that you **forgot to place the Repeater Tap** from the `B0` bus line to the `L8` output wire. Without that tap, the wire never gets powered, and the lamp stays on.

---

### The Encoder: Programming a "Diode Matrix" ROM

#### 3.5.1: Design on Paper

The digit `2` uses segments **`a`, `b`, `d`, `e`, and `g`**. Therefore, you would place torch taps at the intersections of the `L2` line and the perpendicular lines for those five segments.

---

#### 3.5.2: Debug Challenge

If a segment that should be ON is OFF, it means it is not receiving power. The most likely cause is simple: you **forgot to place the torch tap** at the intersection of the horizontal `L4` line and the perpendicular segment `g` line. Without that torch, there is nothing to power the line when `L4` goes low.

---


## Speaking in 1s and 0s – The Input Interface [1]

### Module 1 Checkpoint

#### 1.4.1: Knowledge Check

1. The largest number a `5`-bit input interface could input is **31**. (In binary: `11111`, which is $16 + 8 + 4 + 2 + 1 = 31$.)
2. The decimal value of the binary number `1100` is **12**. (`8 + 4 + 0 + 0 = 12`.)
3. The number `10` in binary is **`1010`**. (`8 + 0 + 2 + 0 = 10`.)

---


## The Language of Logic – A Deep Dive into Boolean Algebra [2]

### Module 2 Checkpoint

#### 2.8.1: Knowledge Check

1.  An **OR** gate outputs `1` if *at least one* input is `1`. An **XOR** gate outputs `1` only if the inputs are *different*.
2.  The **NAND** gate and the **NOR** gate. The property is called **Functional Completeness**.
3.  The equivalent expression is `!A AND !B`.

---

#### 2.8.2: The Word Problem

The expression translates directly from the requirements:

`Y = M OR (T AND !W)`

The parentheses are crucial to ensure the `AND` condition is evaluated before being `OR`'d with the manual override switch.

---

#### 2.8.3: The Simplification

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

---

### Software Superpowers – The XOR Trick for Programmers

#### 2.5.1: The Missing Number Challenge

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

### The Core Operators (The Verbs of Logic)

#### 2.2.1: Boolean Expression Evaluation

**Truth Table for $A \text{ OR } \text{NOT } B$ ($A \lor \neg B$):**

| A | B | !B | A OR !B |
| $A$ | $B$ | $\neg B$ | $A \lor \neg B$ |
|---|---|----|---------|
| `0` | `0` |  `1` |    `1`    |
| `0` | `1` |  `0` |    `0`    |
| `1` | `0` |  `1` |    `1`    |
| `1` | `1` |  `0` |    `1`    |

**Minecraft Circuit**: Use a lever for `A`, a lever for `B`, a redstone torch on `B`’s block for `!B`, merge `A` and `!B` with dust for OR, and connect to a lamp for output. Test all combinations to verify.

---

#### 2.2.2: Logic Gate Design Challenge

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

---

### The Laws of Logic & The Power of Simplification

#### 2.3.1: Circuit Simplification Challenge

**Simplification Steps:**
1. Start with $(A \lor B) \land (\neg A \lor \neg B)$.
2. Apply De Morgan’s Law to the second term: $\neg A \lor \neg B = \neg(A \land B)$.
3. The expression becomes $(A \lor B) \land \neg(A \land B)$.
4. Distribute: $(A \land \neg(A \land B)) \lor (B \land \neg(A \land B))$.
5. Simplify each term:
   - $A \land \neg(A \land B) = A \land (\neg A \lor \neg B) = (A \land \neg A) \lor (A \land \neg B) = 0 \lor (A \land \neg B) = A \land \neg B$.
   - Similarly, $B \land \neg(A \land B) = B \land \neg A$.
6. Final expression: $(A \land \neg B) \lor (\neg A \land B)$, which is $A \text{ XOR } B$ ($A \oplus B$).

---

### The Negated Gates – NAND, NOR, and XNOR

#### 2.6.1: Universal Gate Challenge with NOR Gates

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

---

### The Special Operator – XOR

#### 2.4.1: Two-Switch Light System

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

---


## The Redstone Toolkit – Orientation Day (Optional) [0]

### Module 0 Checkpoint

#### 0.3.1: Knowledge Check

1.  It boosts a signal back to strength 15 and acts as a one-way diode.
2.  No. The dust only weakly powers the block, which cannot transmit power to adjacent dust.
3.  The Redstone Torch.

---


---

[0]: Module 0: The Redstone Toolkit – Orientation Day (Optional)

[1]: Module 1: Speaking in 1s and 0s – The Input Interface

[2]: Module 2: The Language of Logic – A Deep Dive into Boolean Algebra

[3]: Module 3: From Binary to Pictures - Building a Digital Display
