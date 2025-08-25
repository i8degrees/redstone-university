import os
import re
from glob import glob

SRC_DIR = "src"
OUTPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/Z-Appendices/Appendix-A_Solutions.md"

GITHUB_USER = "fielding"
GITHUB_REPO = "redstone-university"
GITHUB_BRANCH = "main"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/"
ASSETS_IMG_DIR = "assets/images"


def rewrite_image_paths(md_content):
    import re

    def replacer(match):
        alt_text, rel_path = match.groups()
        # Only rewrite if path is relative and points to images/
        if rel_path.startswith("./images/") or rel_path.startswith("images/"):
            image_name = rel_path.split("/")[-1]
            abs_url = RAW_BASE_URL + ASSETS_IMG_DIR + "/" + image_name
            return f"![{alt_text}]({abs_url})"
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replacer, md_content)


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
    Finds all #### Practice Problem X.Y.Z: Title followed by <details>...</details> blocks.
    Extracts the explicit problem_id and title from the #### header.
    Organizes by module and lesson based on surrounding headings.
    Returns a nested dict: {module_title: {lesson_title: [(problem_id, problem_title, summary, inner, full_block, module_num, lesson_num), ...]}}
    """
    module_pattern = re.compile(r"^##\s+Module (\d+):\s*(.+)$", re.MULTILINE)
    lesson_pattern = re.compile(r"^###\s+(Lesson (\d+\.\d+):\s*(.+)|Module (\d+) Checkpoint)$", re.MULTILINE)
    problem_pattern = re.compile(r"^####\s+Practice Problem (\d+\.\d+\.\d+):\s*(.+)$", re.MULTILINE)
    details_pattern = re.compile(r"(<details>\s*<summary>(.*?)</summary>\s*(.*?)</details>)", re.DOTALL)
    headings = []
    for m in module_pattern.finditer(md):
        module_num = m.group(1)
        module_title = m.group(2).strip()
        headings.append((m.start(), 2, module_title, module_num))
    for m in lesson_pattern.finditer(md):
        if m.group(2):
            lesson_num = m.group(2)
            lesson_title = m.group(3).strip()
        else:
            module_num = m.group(4)
            lesson_num = f"{module_num}.checkpoint"
            lesson_title = f"Module {module_num} Checkpoint"
        headings.append((m.start(), 3, lesson_title, lesson_num))
    solutions = {}
    problem_matches = list(problem_pattern.finditer(md))
    details_matches = list(details_pattern.finditer(md))
    for i, prob_match in enumerate(problem_matches):
        problem_id = prob_match.group(1)
        problem_title = prob_match.group(2).strip()
        prob_pos = prob_match.start()
        full_block = inner = summary = None
        for det_match in details_matches:
            if det_match.start() > prob_pos:
                full_block = det_match.group(1)
                summary = det_match.group(2).strip()
                inner = det_match.group(3).strip()
                break
        if not full_block:
            continue
        module_title = "Unknown Module"
        module_num = "Unknown"
        lesson_title = "Unknown Lesson"
        lesson_num = "Unknown"
        for hpos, hlevel, htitle, hnum in reversed(headings):
            if hpos < prob_pos:
                if hlevel == 2 and module_title == "Unknown Module":
                    module_title = htitle
                    module_num = hnum
                if hlevel == 3 and lesson_title == "Unknown Lesson":
                    lesson_title = htitle
                    lesson_num = hnum
                if module_title != "Unknown Module" and lesson_title != "Unknown Lesson":
                    break
        if "." in problem_id:
            parts = problem_id.split(".")
            if len(parts) == 3:
                lesson_num = parts[1]
        if module_title not in solutions:
            solutions[module_title] = {}
        if lesson_title not in solutions[module_title]:
            solutions[module_title][lesson_title] = []
        solutions[module_title][lesson_title].append(
            (problem_id, problem_title, summary, inner, full_block, module_num, lesson_num)
        )
        print(
            f"📄 Extracted solution: Problem {problem_id} ({problem_title}) in {module_title}, {lesson_title} ({file_path})"
        )
    return solutions


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
                for problem_id, _, _, _, full_block, _, _ in solution_list:
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
            for _, _, _, _, _, module_num, _ in sum(all_solutions[module_title].values(), [])
            if module_num != "Unknown"
        )
    )
    module_to_num = {}
    for module_title in all_solutions:
        module_num = next(
            (mnum for lessons in all_solutions[module_title].values() for _, _, _, _, _, mnum, _ in lessons),
            "Unknown",
        )
        if module_num != "Unknown":
            module_to_num[module_title] = module_num
    sorted_module_titles = sorted(module_to_num.keys(), key=lambda t: int(module_to_num[t]))
    solution_count = 0
    for module_title in sorted_module_titles:
        module_num = module_to_num[module_title]
        appendix.append(f"\n## Module {module_num}: {module_title}\n")
        lesson_to_num = {}
        for lesson_title in all_solutions[module_title]:
            lesson_num = next(
                (lnum for _, _, _, _, _, _, lnum in all_solutions[module_title][lesson_title]),
                "Unknown",
            )
            if lesson_num != "Unknown":
                lesson_to_num[lesson_title] = lesson_num
        sorted_lesson_titles = sorted(lesson_to_num.keys(), key=lambda t: float(lesson_to_num[t]))
        for lesson_title in sorted_lesson_titles:
            appendix.append(f"### {lesson_title}\n")
            for problem_id, problem_title, _, inner, _, _, _ in sorted(
                all_solutions[module_title][lesson_title],
                key=lambda x: tuple(map(int, x[0].split("."))),
            ):
                solution_count += 1
                appendix.append(f"#### {problem_id}: {problem_title}\n\n{inner}\n\n---\n")
    appendix.append("\n---\n")
    for module in sorted(module_titles.keys(), key=int):
        title = module_titles.get(module, f"Module {module}")
        appendix.append(f"[{module}]: Module {module}: {title}\n")
    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write(rewrite_image_paths("\n".join(appendix)))
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for _, content in sorted(replaced_contents, key=lambda x: x[0]):
            f.write(rewrite_image_paths(content))
            f.write('\n\n<hr class="pagebreak"/>\n\n')
    print(f"✅ Processed {solution_count} solutions. Output written to {OUTPUT_FILE} and {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
