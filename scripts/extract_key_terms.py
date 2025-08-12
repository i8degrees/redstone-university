import os
import re

INPUT_FILE = "course/Redstone-University.md"
APPENDIX_FILE = "appendices/Appendix-C_Key-Terms.md"
OUTPUT_FILE = "course/Redstone-University-with-key-terms.md"


def extract_key_terms_sections(md):
    """
    Finds all '#### Key Terms (Module X)' sections and returns a list of tuples:
    (module_heading, key_terms_list)
    """
    pattern = re.compile(r"(#### Key Terms \(Module\s*\d+\)\s*\n((?:- .+\n?)+))", re.MULTILINE)
    results = []
    for match in pattern.finditer(md):
        heading_line = re.match(r"(#### Key Terms \(Module\s*\d+\))", match.group(1))
        heading = heading_line.group(1) if heading_line else "Unknown Module"
        bullets = match.group(2).strip()
        results.append((heading, bullets))
    return results


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found. Please run course_concat.py first.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    appendix = ['<hr class="pagebreak"/>\n\n### Appendix C: Key Terms\n\n---\n']
    key_terms_sections = extract_key_terms_sections(md)
    for heading, bullets in key_terms_sections:
        appendix.append(f"{heading}\n\n{bullets}\n\n---\n")

    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)
    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md)
        f.write("\n\n")
        f.write("\n".join(appendix))

    print(
        f"Extracted {len(key_terms_sections)} key terms sections. Output written to {APPENDIX_FILE} and {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
