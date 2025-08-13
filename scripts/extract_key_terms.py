import os
import re

INPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/appendices/Appendix-C_Key-Terms.md"


def extract_key_terms_from_md(md_content):
    """Extracts all key terms and their definitions from markdown content."""
    # Pattern to find a list of terms under a "Key Terms" heading
    pattern = re.compile(r"#### Key Terms(?: \(Module \d+\))?\s*\n((?:- .+\n?)+)", re.MULTILINE)
    # Pattern to extract individual terms and definitions from a list
    term_pattern = re.compile(r"- \s*\*\*([^*]+)\*\*: \s*(.+)")

    all_terms = {}

    for section_match in pattern.finditer(md_content):
        term_list_str = section_match.group(1)
        for term_match in term_pattern.finditer(term_list_str):
            term = term_match.group(1).strip()
            definition = term_match.group(2).strip()
            if term not in all_terms:
                all_terms[term] = definition

    return all_terms


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)

    key_terms = extract_key_terms_from_md(md)

    sorted_terms = sorted(key_terms.items())

    appendix_content = ['<hr class="pagebreak"/>\n\n### Appendix C: Key Terms\n']

    for term, definition in sorted_terms:
        appendix_content.append(f"**{term}**\n: {definition}\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix_content))

    print(f"Extracted and alphabetized {len(sorted_terms)} unique key terms into {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
