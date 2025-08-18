import os
import re
from glob import glob

SRC_DIR = "src"
OUTPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/Z-Appendices/Appendix-A_Solutions.md"


def extract_module_titles(md_content, file_path):
    """
    Extracts module numbers and titles from '## Module X: Title' headings.
    Returns a dictionary of {module_num: title}.
    """
    module_pattern = re.compile(r"^##\s+Module (\d+):\s*(.+)$", re.MULTILINE)
    module_titles = {}
    for match in module_pattern.finditer(md_content):
        module_num = match.group(1)
        title = match.group(2).strip()
        module_titles[module_num] = title
        print(f"📋 Found module in {file_path}: Module {module_num}: {title}")
    return module_titles


def extract_solutions_by_module_and_lesson(md, file_path):
    """
    Finds all <details>...</details> blocks and organizes them by module and lesson.
    Assigns Problem X.Y.Z IDs based on module, lesson, and order.
    Returns a nested dict: {module_title: {lesson_title: [(problem_id, summary, inner, full_block, module_num, lesson_num), ...]}}
    """
    module_pattern = re.compile(r"^##\s+Module (\d+):\s*(.+)$", re.MULTILINE)
    lesson_pattern = re.compile(r"^###\s+Lesson (\d+\.\d+):\s*(.+)$", re.MULTILINE)
    details_pattern = re.compile(r"(<details>\s*<summary>\s*([^<]+)</summary>(.*?)</details>)", re.DOTALL)

    headings = []
    for m in module_pattern.finditer(md):
        module_num = m.group(1)
        module_title = m.group(2).strip()
        headings.append((m.start(), 2, module_title, module_num))
    for m in lesson_pattern.finditer(md):
        lesson_num = m.group(1)
        lesson_title = m.group(2).strip()
        headings.append((m.start(), 3, lesson_title, lesson_num))

    solutions = {}
    for match in details_pattern.finditer(md):
        full_block = match.group(1)
        summary = match.group(2).strip()
        inner = match.group(3).strip()
        pos = match.start()
        module_title = "Unknown Module"
        module_num = "Unknown"
        lesson_title = "Unknown Lesson"
        lesson_num = "Unknown"

        for hpos, hlevel, htitle, hnum in reversed(headings):
            if hpos < pos:
                if hlevel == 2 and module_title == "Unknown Module":
                    module_title = htitle
                    module_num = hnum
                if hlevel == 3 and lesson_title == "Unknown Lesson":
                    lesson_title = htitle
                    lesson_num = hnum
                if module_title != "Unknown Module" and lesson_title != "Unknown Lesson":
                    break

        if module_title not in solutions:
            solutions[module_title] = {}
        if lesson_title not in solutions[module_title]:
            solutions[module_title][lesson_title] = []

        # Assign Problem X.Y.Z ID based on order
        problem_count = len(solutions[module_title][lesson_title]) + 1
        problem_id = (
            f"{module_num}.{lesson_num}.{problem_count}"
            if module_num != "Unknown" and lesson_num != "Unknown"
            else "Unknown"
        )
        solutions[module_title][lesson_title].append((problem_id, summary, inner, full_block, module_num, lesson_num))
        print(f"📄 Extracted solution: Problem {problem_id} in {module_title}, {lesson_title} ({file_path})")

    return solutions


def clean_summary(summary, problem_id):
    """
    Clean up the summary for the appendix, removing boilerplate text.
    Returns only the problem ID if the summary is generic, otherwise keeps the cleaned title.
    """
    cleaned = (
        summary.replace("Click for the solution and explanation", "")
        .replace("Click for answers", "")
        .replace("Click for the step-by-step proof", "")
        .replace("<strong>", "")
        .replace("</strong>", "")
        .strip()
    )
    if not cleaned or cleaned.lower() in ["solution", "solution:"]:
        return problem_id
    if cleaned.lower().startswith("solution:"):
        cleaned = cleaned[8:].strip()
    return f"{problem_id}: {cleaned}" if cleaned else problem_id


def collect_markdown_files(directory):
    """
    Collect all markdown files (*.md) in the src directory.
    """
    files = glob(os.path.join(directory, "**/*.md"), recursive=True)
    return sorted(files)


def main():
    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    all_solutions = {}
    module_titles = {}
    replaced_contents = []

    print(f"🔍 Scanning markdown files in '{SRC_DIR}'...")
    files = collect_markdown_files(SRC_DIR)
    if not files:
        print(f"❌ Error: No markdown files found in '{SRC_DIR}'.")
        return
    print(f"📜 Found {len(files)} markdown files")

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        module_titles.update(extract_module_titles(md, file_path))
        solutions = extract_solutions_by_module_and_lesson(md, file_path)
        for module_title, lessons in solutions.items():
            if module_title not in all_solutions:
                all_solutions[module_title] = {}
            for lesson_title, solution_list in lessons.items():
                if lesson_title not in all_solutions[module_title]:
                    all_solutions[module_title][lesson_title] = []
                all_solutions[module_title][lesson_title].extend(solution_list)

        replaced_md = md
        for module_title, lessons in solutions.items():
            for lesson_title, solution_list in lessons.items():
                for problem_id, _, _, full_block, _, _ in solution_list:
                    reference = (
                        f"> **(Solution for Problem {problem_id} is in Appendix A)**\n"
                        if problem_id != "Unknown"
                        else "> **(Solution is in Appendix A)**\n"
                    )
                    replaced_md = replaced_md.replace(full_block, reference)
        replaced_contents.append((file_path, replaced_md))

    if not all_solutions:
        print(f"❌ Error: No solutions extracted from any files in '{SRC_DIR}'.")
        return

    appendix = [
        '<hr class="pagebreak"/>\n\n'
        "## Appendix A: Solutions\n\n"
        "This appendix provides solutions to the quizzes, logic puzzles, and debug challenges "
        "in the Redstone University curriculum, organized by module and lesson. "
        "Each solution is labeled with its problem ID (Module.Lesson.Problem) for easy reference, "
        "with a footnote indicating the module where it appears.\n"
    ]

    used_modules = sorted(
        set(
            module_num
            for module_title in all_solutions
            for _, _, _, _, module_num, _ in sum(all_solutions[module_title].values(), [])
            if module_num != "Unknown"
        )
    )

    solution_count = 0
    for module_title in sorted(all_solutions.keys()):
        module_num = next(
            (
                mnum
                for mtitle, lessons in all_solutions.items()
                for _, _, _, _, mnum, _ in sum(lessons.values(), [])
                if mtitle == module_title
            ),
            "Unknown",
        )
        if module_num == "Unknown":
            continue
        appendix.append(f"\n## {module_title} [{module_num}]\n")
        for lesson_title in sorted(all_solutions[module_title].keys()):
            appendix.append(f"### {lesson_title}\n")
            for problem_id, summary, inner, _, _, _ in sorted(
                all_solutions[module_title][lesson_title], key=lambda x: x[0]
            ):
                solution_count += 1
                cleaned_summary = clean_summary(summary, problem_id)
                appendix.append(f"#### {cleaned_summary}\n\n{inner}\n\n---\n")

    appendix.append("\n---\n")
    for module in sorted(module_titles.keys(), key=int):
        title = module_titles.get(module, f"Module {module}")
        appendix.append(f"[{module}]: Module {module}: {title}\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for _, content in sorted(replaced_contents, key=lambda x: x[0]):
            f.write(content)
            f.write('\n\n<hr class="pagebreak"/>\n\n')

    print(f"✅ Processed {solution_count} solutions. Output written to {OUTPUT_FILE} and {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
