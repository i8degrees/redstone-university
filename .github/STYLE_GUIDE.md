# Redstone University Style Guide

This style guide ensures that all content for the Redstone University project is consistent, professional, and clear. Its purpose is to create a seamless learning experience by maintaining a unified voice that is academic yet personable, and engaging for all students.

---

## 1. Course Structure and Headings

A consistent structure helps students navigate the material and understand the hierarchy of information.

*   `##` **Module Titles**: Used for the main title of each module.
    *   **Format**: `## Module X: Title – Subtitle`
    *   **Example**: `## Module 2: The Language of Logic – A Deep Dive into Boolean Algebra`
    *   *Note: Use an en dash (–) for subtitles.*

*   `###` **Lesson and Section Titles**: Used for individual lessons and major module sections.
    *   **Lessons**: `### Lesson X.Y: Title` (e.g., `### Lesson 2.1: The Rules of Thought`)
    *   **Major Sections**: `### Module Summary`, `### Module Introduction`, `### Module Conclusion`, `### Module X Checkpoint`

*   `####` **Subsections**: Used for all standard sections within a lesson or checkpoint.
    *   **Standard Subsections**: `#### The Theory`, `#### Lab & Experiment`, `#### Real-World Connection`, `#### Software Connection`, `#### Key Terms`.
    *   **Practice Problems**: `#### Practice Problem X.Y.Z: Title`

*   `#####` **Sub-subsections**: Avoid using this level to maintain a clean structure. Standardize all nested content (like old puzzle headers) to `####`.

**General Rules**:
-   Use sentence case for all titles (capitalize the first word and any proper nouns).
-   Use `---` separators between major sections like lessons and checkpoints.
-   Do not use `#` level headings; they are reserved for the main `Part` introductions.

---

## 2. Practice Problems and Checkpoints

Practice problems are a critical learning tool. Their formatting and placement should be predictable and clear.

**Placement**:
*   Place individual practice problems directly after the relevant lesson content.
*   Group cumulative problems under the `### Module X Checkpoint` section at the end of a module.

**Formatting**:
*   **Header**: Every problem must have a unique header.
    *   **Format**: `#### Practice Problem X.Y.Z: Title`
    *   **Numbering (`X.Y.Z`)**:
        *   `X`: Module number.
        *   `Y`: Lesson number.
        *   `Z`: Sequential order within that lesson.
    *   **Title**: Give a descriptive title (e.g., *Knowledge Check*, *Debug Challenge*, *The Simplification*).

*   **Solution**: All solutions must be enclosed in a `<details>` block for a clean, toggleable view.
    *   **Summary Tag**: Always use `<summary><strong>Show Solution</strong></summary>`. This creates a consistent button for all solutions.
    *   **Content**: Inside the block, use bolding for subsections like **Logic:** or **Truth Table:** to guide the student.

**Example Checkpoint Structure**:

```markdown
### Module 2 Checkpoint

#### Practice Problem 2.8.1: Knowledge Check
...problem description...
<details>
<summary><strong>Show Solution</strong></summary>
...detailed solution...
</details>

#### Practice Problem 2.8.2: The Word Problem
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

*   **Placement**: Always the last subsection within a `### Module X Checkpoint`.
*   **Header**: `#### Key Terms`.
*   **Format**:
    *   Use a bulleted list.
    *   Bold each term, followed by a colon.
    *   Alphabetize the terms within the list.

**Example**:
```markdown
#### Key Terms
- **Binary**: A base-2 number system...
- **Decoder**: A circuit that takes a multi-bit input...
```

---

## 4. Markdown and Formatting Style

Consistent formatting creates a professional and readable course.

*   **Emphasis**:
    *   **Bold**: Use for key terms, section labels (**Key Takeaway:**), and strong emphasis.
    *   *Italics*: Use for figure captions (*Figure: A working AND gate.*) and subtle emphasis.

*   **Images**: `![Alt text](./images/path.png)`, followed by an italicized caption on the next line.

*   **Blockquotes**: Use `>` for important notes or takeaways that should stand out.
    *   **Example**: `> **Engineering Note:** The Redstone Repeater acts as a perfect diode.`

*   **Code Blocks**: Use for all code snippets (Python, etc.) and multi-line Boolean expressions. Specify the language for syntax highlighting (e.g., ` ```python `).

*   **Lists**:
    *   Use numbered lists (`1.`) for sequential steps.
    *   Use bulleted lists (`-`) for non-sequential items.

*   **Tables**: Use Markdown tables for truth tables and summaries. Always center-align columns (`:---:`).

*   **Punctuation**: Use en dashes (`–`) for subtitles and ranges, not em dashes (`—`). Use a single space after periods.

### Inline Code and Numbers: A Critical Standard

This is the most detailed formatting rule. Its goal is to distinguish between descriptive text and raw data values.

*   **DO** use backticks (`` ` ``) for standalone numbers that represent data values.
    *   **Good**: The binary value is `1011`. This is equal to `11` in decimal or `0xB` in hex.
    *   **Good**: Add the numbers `8`, `4`, and `1`.

*   **DO NOT** use backticks for numbers that are part of a descriptive phrase.
    *   **Bad**: Our `4-bit` computer uses a `7-segment` display.
    *   **Good**: Our 4-bit computer uses a 7-segment display.

*   **DO** use LaTeX math mode (`$...$`) for mathematical equations and logical expressions.
    *   **Good**: The sum is $8 + 4 + 1 = 13$. The value is $2^4$.
    *   **Good**: The expression is $A \text{ AND } B$ ($A \land B$). Use dual notation for clarity.

*   **Summary Table**:

| Context                                | Correct Formatting Example         | Incorrect Formatting Example        |
| -------------------------------------- | ---------------------------------- | ----------------------------------- |
| Standalone data value                  | `1101`, `13`, `0xD`                | 1101, $13$                          |
| Number within a descriptive phrase     | a 4-bit adder, a 2-to-4 decoder    | a `4-bit` adder, a `2-to-4` decoder |
| Mathematical or logical equation       | $Y = A + (!B \cdot C)$             | `Y = A + (!B * C)`                  |

---

## 5. Content and Tone

*   **Tone**: Maintain an engaging, educational, and narrative-driven voice. The course follows a personal journey of discovery.
*   **Standard Sections**: Use sections like **Key Takeaway**, **Lab & Experiment**, **Real-World Connection**, and **Software Connection** to frame the content and connect theory to practice.
*   **Module Flow**: Ensure each module follows the standard structure:
    1.  `### Module Summary`
    2.  `### Module Introduction`
    3.  `### Lesson X.Y: Title` (as many as needed)
    4.  `### Module Conclusion`
    5.  `### Module X Checkpoint` (containing practice problems and key terms)

---

## 6. Quality Assurance and Verification

After applying these standards, perform the following checks:

*   **Manual Review**:
    *   Confirm every `<details>` block has the correct header and summary format.
    *   Verify that `#### Key Terms` is the last section in every checkpoint and that its terms are alphabetized.
*   **Scripted Tests**:
    *   Run `extract_solutions.py` and `extract_key_terms.py` to ensure the appendices are generated correctly.
*   **Rendering Checks**:
    *   Confirm the content renders correctly on the target web platform (e.g., GitHub).
    *   Generate a PDF using `combine_for_pdf.py` and Pandoc to check for formatting errors.
