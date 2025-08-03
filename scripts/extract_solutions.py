import os
import re

INPUT_FILE = "course/Redstone-University.md"
OUTPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/Appendix-B_Solutions.md"


def extract_details_blocks(md):
    """
    Finds all <details>...</details> blocks and returns a list of tuples:
    (full_block, summary_text, inner_content, preceding_heading)
    """
    pattern = re.compile(
        r"(<details>\s*<summary>(.*?)</summary>(.*?)</details>)",
        re.DOTALL | re.IGNORECASE,
    )
    results = []
    for match in pattern.finditer(md):
        full_block = match.group(1)
        summary = match.group(2).strip()
        inner = match.group(3).strip()
        pre = md[: match.start()]
        headings = list(re.finditer(r"^(#{2,4})\s*(.+)$", pre, re.MULTILINE))
        heading = headings[-1].group(0) if headings else "Unknown Context"
        results.append((full_block, summary, inner, heading))
    return results


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found. Please run course_concat.py first.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    appendix = ["### Appendix B: Solutions to Exercises\n\n---\n"]
    replaced_md = md

    for idx, (full_block, summary, inner, heading) in enumerate(extract_details_blocks(md), 1):
        reference = "> **Solution available in Appendix B: Solutions to Exercises**\n\n"
        replaced_md = replaced_md.replace(full_block, reference)

        appendix.append(f"#### Solution for {heading}\n\n{inner}\n\n---\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(replaced_md)
        f.write("\n\n")
        f.write("\n".join(appendix))

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix))

    print(f"Processed {len(appendix)-1} solutions. Output written to {OUTPUT_FILE} and {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
