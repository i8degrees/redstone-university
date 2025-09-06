# Redstone University Style Guide

This style guide ensures that all content for the Redstone University project is consistent, professional, and clear. Its purpose is to create a seamless learning experience by maintaining a unified voice that is academic yet personable, and engaging for all students.

---

## 1. Course Structure and Headings

A consistent structure helps students navigate the material and understand the hierarchy of information.

-   `##` **Module Titles**: Used for the main title of each module.
    -   **Format**: `## Module X: Title – Subtitle`
    -   **Example**: `## Module 2: The Grammar of Circuits – Foundational Logic Gates`
    -   *Note: Use an en dash (–) for subtitles.*

-   `###` **Lesson and Section Titles**: Used for individual lessons and major module sections.
    -   **Lessons**: `### Lesson X.Y: Title` (e.g., `### Lesson 2.1: The Rules of Thought`)
    -   **Major Sections**: `### Module Summary`, `### Module Introduction`, `### Module Conclusion`, `### Module X Checkpoint`

-   `####` **Subsections**: Used for all standard sections within a lesson or checkpoint.
    -   **Standard Subsections**: `#### The Theory`, `#### Lab & Experiment`, `#### Real-World Connection`, `#### Software Connection`, `#### Key Terms`.
    -   **Practice Problems**: `#### Practice Problem X.Y.Z: Title`

-   `#####` **Sub-subsections**: Avoid using this level to maintain a clean structure. Standardize all nested content to `####`.

**General Rules**:
-   Use sentence case for all titles (capitalize the first word and any proper nouns).
-   Use `---` separators between major sections (those with `###` headings) like lessons, summaries, and checkpoints.
-   A separator may also be used *within* a lesson to improve readability under two specific conditions:
    1.  **To separate theory from practice:** Place a separator before a major, hands-on lab section (e.g., `#### Lab & Experiment`).
    2.  **To separate distinct sub-topics:** In a lesson covering multiple similar items, place a separator between each item's dedicated section (e.g., between each logic gate explanation).
-   Do not use `#` level headings; they are reserved for the main `Part` introductions.

---

## 2. Practice Problems and Checkpoints

Practice problems are a critical learning tool. Their formatting and placement should be predictable and clear.

**Placement**:
-   Place individual practice problems directly after the relevant lesson content.
-   Group cumulative problems under the `### Module X Checkpoint` section at the end of a module.

**Formatting**:
-   **Header**: Every problem must have a unique header.
    -   **Format**: `#### Practice Problem X.Y.Z: Title`
    -   **Numbering (`X.Y.Z`)**:
        -   `X`: Module number.
        -   `Y`: Lesson number (if applicable).
        -   `Z`: Sequential order.
    -   **Title**: Give a descriptive title (e.g., *Knowledge Check*, *Debug Challenge*, *The Simplification*).

-   **Solution**: All solutions must be enclosed in a `<details>` block for a clean, toggleable view.
    -   **Summary Tag**: Always use `<summary><strong>Show Solution</strong></summary>`. This creates a consistent button for all solutions.
    -   **Content**: Inside the block, use bolding for subsections like **Logic:** or **Truth Table:** to guide the student.

**Example Checkpoint Structure**:

```markdown
### Module 2 Checkpoint

#### Practice Problem 2.4.1: Knowledge Check
...problem description...
<details>
<summary><strong>Show Solution</strong></summary>
...detailed solution...
</details>

#### Practice Problem 2.4.2: The Word Problem
...problem description...
<details>
<summary><strong>Show Solution</strong></summary>
...detailed solution...
</details>

#### Key Terms
- **Term**: Definition...
```

---

## 3. Glossary Terms (Key Terms)

To reinforce learning, key terms are defined and collected at the end of each module's checkpoint.

-   **Placement**: Always the last subsection within a `### Module X Checkpoint`.
-   **Header**: `#### Key Terms`.
-   **Format**:
    -   Use a bulleted list.
    -   Bold each term, followed by a colon.
    -   Alphabetize the terms within the list.

**Example**:
```markdown
#### Key Terms
- **Binary**: A base-2 number system...
- **Decoder**: A circuit that takes a multi-bit input...
```

---

## 4. Markdown and Formatting Style

Consistent formatting creates a professional and readable course. *(other general rules like Emphasis, Images, etc. would go here)*

### Inline Code and Numbers: A Critical Standard

This is the most detailed formatting rule. Its purpose is to create a clear, consistent, and professional distinction between abstract mathematical concepts, literal data values, and simple descriptive text.

**1. Use LaTeX (`$ ... $`) for Abstract Concepts**

This applies to all mathematical and logical ideas, including **variables**, full **expressions**, and the formal logical **constants** for True and False.

-   **Variables:** `$A$`, `$B$`, `$Y$`
-   **Expressions:** `$A \lor (\neg B \cdot C)`
-   **Logical Constants:** In the context of a mathematical proof or law, use `$1$` for True and `$0$` for False.
    -   **Good**: The Identity Law states that $A \land 1 = A$.
    -   **Good**: We know from the Inverse Law that $B \lor \neg B$ always simplifies to the constant `$1$` (True).
    -   **Bad**: The law is `A AND 1 = A`.

**2. Use Backticks (` `) for Literal Values and Code**

This applies to all concrete, physical data values and code snippets. It represents the actual state of a wire, a number being input, or a line of code.

-   **Data Values:** `1`, `0`
-   **Number bases:** Use prefixes with backticks for concrete values:
    -   **Binary:** `0b0011`
    -   **Hexadecimal:** `0x0C` (uppercase A–F). Pad to full nibbles only when clarity demands it (e.g., 8-bit tables: `0x0C`); otherwise `0xC` is fine.
    -   **Decimal:** `1`, no prefix needed.
-   **Code:** `if (is_ready)`
    -   **Good**: A Redstone signal can be either `1` (ON) or `0` (OFF).
    -   **Good**: Set the input levers to `1011` to represent the number `13`.
    -   **Bad**: A signal can be either $1$ or $0$.

**3. Do Not Format Descriptive Numbers**

If a number is used as part of a descriptive phrase (like an adjective), it should be plain text.

-   **Good**: Our 4-bit computer uses a 7-segment display.
-   **Bad**: Our `4-bit` computer uses a `7-segment` display.

**Putting It All Together: The "Universe" Test**

The key is to identify if you are talking about the **abstract universe of math** or the **physical universe of the circuit**.

-   **Abstract (Math):** The expression `$A \lor 0$` is governed by the Annihilator Law. The variable `$A$` and the constant `$0$` are mathematical concepts.
-   **Physical (Circuit):** To test this, we set the lever for input `$A$` to the value `1`. The signal on the wire is now `1`.

This clear separation in formatting makes complex sentences easy to parse and understand.

> **Best Practice for LaTeX:** To prevent conflicts with Markdown's parser, use proper LaTeX commands instead of ambiguous characters. For example, use `\cdot` or `\times` for multiplication instead of `*`. Use `\text{...}` for embedding normal words inside a formula, as in `$A \text{ OR } B$`.

### Using Dual Notation for Logical Expressions

To ensure our content is both intuitive for beginners and academically sound, we use a system that distinguishes between **defining** the notations and **using** them in prose.

**1. Defining Notations (in the `Symbols` section of a gate introduction)**

The `Symbols` section serves as a formal definition. Here, we will use a nested, labeled list to explicitly break down the different ways an expression can be written. This provides maximum clarity.

**Example for an AND Gate:**
> -   **Symbols:**
>     -   **Logical Notations:**
>         -   *Text-based:* $A \text{ AND } B$
>         -   *Symbolic:* $A \land B$
>     -   **Programming Operator:** `A && B`

**2. Using Notations (in the main body of the text)**

When an expression is used for the first time within a paragraph or section, we will use the **colon-separated dual notation** to link the text-based and symbolic forms inline. This reinforces the equivalence in a flowing, readable way.

-   **The Core Rule:** $A \text{ AND } B : A \land B$

**3. The "Teach and Trust" Method for Repetition**

The guideline for repetition remains the same. After the first use of the full dual notation in a section, subsequent mentions should use only the concise, formal symbolic version (e.g., $A \land B$).

**Example of All Rules in Practice:**

> ...as shown in the **Symbols** section above, the text-based form is $A \text{ AND } B$ and the symbolic form is $A \land B$. In this lesson, we will build a circuit for the expression $A \text{ AND } (\text{NOT } B) : A \land (\neg B)$. To build the circuit for $A \land (\neg B)$, we first need to generate the signal for $\neg B$...

### Active‑Low Signals (Diagrams vs Text)

- **Diagrams:** Use the standard **bubble** notation (a small open circle on the pin) to indicate inversion/active‑low.
- **Prose/Equations (LaTeX):** Write active‑low nets with an **overbar**, e.g., $\overline{L_3}$, $\overline{RESET}$. Use this consistently wherever MathJax/LaTeX is available.
- **Fallback when LaTeX isn’t available (labels, filenames, tool pin names):** use the suffix **`_n`**, e.g., `L3_n`, `RESET_n`.
- **Operator vs name:** Use $\neg$ for logical negation in expressions (e.g., $Y=\neg(A\lor B)$). Use the overbar for **net names** (e.g., “the active‑low output $\overline{Y}$”). Avoid `/NAME` and `!NAME`.
- **Bit indices:** In math, prefer subscripts for readability ($B_3$). In labels or code, use `B3`.


### Active‑Low Signals (Diagrams vs Text)

- **Diagrams:** Use the standard **bubble** notation (a small open circle on the pin) to indicate inversion/active‑low, e.g., the outputs of an active‑low decoder line or an active‑low segment driver.
- **Text (LaTeX):** Prefer an overbar, e.g., $\overline{L3}$. When overbars aren’t practical (labels or non‑LaTeX contexts), allow `L3_n`. In prose, write “`L3` (active‑low)” the first time it appears.
- **Do not** use slashes (e.g., `/L3`) or exclamation marks (e.g., `!L3`) for net names in this course; reserve `!` for boolean negation in programming examples.



### Summary Table

| Context | Correct Formatting Example | Incorrect Formatting Example(s) |
| :--- | :--- | :--- |
| **Logical/Mathematical Concept**<br>(Variable, Expression, or Constant) | $A$, $A \land B$, $1$ | `A`, `A`, `$A$` |
| **Literal Data Value**<br>(Physical state, code, numerical string) | `1` , `0`, `1011`, `count = 0` | `1`, $1$ |
| **Descriptive Number**<br>(Used as an adjective in a sentence) | a 4-bit adder | a `4-bit` adder, a `$4$`-bit adder |

---

## 5. Content and Tone

-   **Tone**: Maintain an engaging, educational, and narrative-driven voice. The course follows a personal journey of discovery.
-   **Standard Sections**: Use sections like **Key Takeaway**, **Lab & Experiment**, **Real-World Connection**, and **Software Connection** to frame the content and connect theory to practice.
-   **Module Flow**: Ensure each module follows the standard structure:
    1.  `### Module Summary`
    2.  `### Module Introduction`
    3.  `### Lesson X.Y: Title` (as many as needed)
    4.  `### Module Conclusion`
    5.  `### Module X Checkpoint` (containing practice problems and key terms)

---

## 6. Quality Assurance and Verification

After applying these standards, perform the following checks:

-   **Manual Review**:
    -   Confirm every `<details>` block has the correct header and summary format.
    -   Verify that `#### Key Terms` is the last section in every checkpoint and that its terms are alphabetized.
-   **Scripted Tests**:
    -   Run `extract_solutions.py` and `extract_key_terms.py` to ensure the appendices are generated correctly.
-   **Rendering Checks**:
    -   Confirm the content renders correctly on the target web platform (e.g., GitHub).
    -   Generate a PDF using `combine_for_pdf.py` and Pandoc to check for formatting errors.
