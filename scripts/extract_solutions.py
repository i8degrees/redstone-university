import os
import re
from glob import glob

SRC_DIR = "src"
APPENDIX_FILE = "course/Z-Appendices/Appendix-A_Solutions.md"


def extract_solutions_from_file(md_content, file_path):
    """
    Extracts all solutions from a single markdown file's content.
    Returns a list of tuples: (problem_id, problem_title, solution_content, module_num, lesson_num)
    """
    solutions = []
    pattern = re.compile(
        r"^####\s+Practice Problem\s+([\d\.]+):\s*(.*?)\s*\n(<details>.*?</details>)", re.MULTILINE | re.DOTALL
    )

    path_parts = file_path.split(os.sep)
    module_num = "0"
    lesson_num = "0"
    if len(path_parts) > 2:
        module_dir = next(
            (
                part
                for part in reversed(path_parts)
                if part.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
            ),
            None,
        )
        if module_dir:
            module_num = module_dir.split("_")[0]

    for match in pattern.finditer(md_content):
        problem_id, problem_title, details_block = match.groups()
        problem_title = problem_title.strip()

        inner_content_match = re.search(r"<summary>.*?</summary>(.*)", details_block, re.DOTALL)
        inner_content = inner_content_match.group(1).strip() if inner_content_match else ""

        id_parts = problem_id.split(".")
        if len(id_parts) == 3:
            module_num = id_parts[0]
            lesson_num = id_parts[1]

        solutions.append((problem_id, problem_title, inner_content))
        print(f"  - Extracted solution for Problem {problem_id} from {file_path}")

    return solutions


def main():
    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)

    all_solutions = []
    print(f"🔍 Scanning for markdown files in '{SRC_DIR}'...")
    files = sorted(glob(os.path.join(SRC_DIR, "**/*.md"), recursive=True))

    for file_path in files:
        if "project_assets" in file_path or "images" in file_path:
            continue
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        all_solutions.extend(extract_solutions_from_file(content, file_path))

    if not all_solutions:
        print("⚠️ No solutions found. Appendix will be empty.")
        return

    all_solutions.sort(key=lambda x: [int(part) for part in x[0].split(".")])

    appendix_content = [
        "## Appendix A: Solutions\n\n"
        "This appendix provides solutions to the practice problems in the Redstone University curriculum, organized by problem number for easy reference.\n"
    ]

    solution_count = 0
    for problem_id, problem_title, inner_content in all_solutions:
        solution_count += 1
        appendix_content.append(f"### Practice Problem {problem_id}: {problem_title}\n")
        appendix_content.append(inner_content)
        appendix_content.append("\n\n---\n\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix_content))

    print(f"✅ Generated Appendix A with {solution_count} solutions at: {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
