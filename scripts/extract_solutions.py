import os
import re

INPUT_FILE = "course/Redstone-University.md"
OUTPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "appendices/Appendix-B_Solutions.md"


def extract_solutions_by_module_and_lesson(md):
    """
    Finds all <details>...</details> blocks and organizes them by module and lesson.
    Returns a nested dict: {module_title: {lesson_title: [(summary, inner, full_block), ...]}}
    """
    heading_pattern = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)
    details_pattern = re.compile(
        r"(<details>\s*<summary>(.*?)</summary>(.*?)</details>)",
        re.DOTALL | re.IGNORECASE,
    )

    headings = []
    for m in heading_pattern.finditer(md):
        level = len(m.group(1))
        title = m.group(2).strip()
        pos = m.start()
        headings.append((pos, level, title))

    solutions = {}
    for match in details_pattern.finditer(md):
        full_block = match.group(1)
        summary = match.group(2).strip()
        inner = match.group(3).strip()
        pos = match.start()

        module = "Unknown Module"
        lesson = "Unknown Lesson"
        for hpos, hlevel, htitle in reversed(headings):
            if hpos < pos:
                if hlevel == 2 and module == "Unknown Module":
                    module = htitle
                if hlevel == 3 and lesson == "Unknown Lesson":
                    lesson = htitle
                if module != "Unknown Module" and lesson != "Unknown Lesson":
                    break

        if module not in solutions:
            solutions[module] = {}
        if lesson not in solutions[module]:
            solutions[module][lesson] = []
        solutions[module][lesson].append((summary, inner, full_block))
    return solutions


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found. Please run course_concat.py first.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    # Ensure appendices directory exists
    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)

    appendix = ['<hr class="pagebreak"/>\n\n### Appendix B: Solutions to Exercises\n\n---\n']
    replaced_md = md

    solutions = extract_solutions_by_module_and_lesson(md)
    solution_count = 0

    for module in solutions:
        appendix.append(f"## {module}\n")
        for lesson in solutions[module]:
            appendix.append(f"### {lesson}\n")
            for summary, inner, full_block in solutions[module][lesson]:
                solution_count += 1
                reference = "> **Solution available in Appendix B: Solutions to Exercises**\n\n"
                replaced_md = replaced_md.replace(full_block, reference)
                appendix.append(f"**{summary}**\n\n{inner}\n\n---\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(replaced_md)
        f.write("\n\n")
        f.write("\n".join(appendix))

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix))

    print(f"Processed {solution_count} solutions. Output written to {OUTPUT_FILE} and {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
