import os
import re

INPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/Z-Appendices/Appendix-B_Glossary.md"


def extract_key_terms_from_md(md_content):
    """Extracts all key terms and their definitions from markdown content."""
    pattern = re.compile(r"^(#{3,4})\s+Key Terms.*\n((?:- .+\n?)+)", re.MULTILINE)
    term_pattern = re.compile(r"-\s+\*\*([^*]+)\*\*([:\s]+)(.+)")

    all_terms = {}

    for section_match in pattern.finditer(md_content):
        term_list_str = section_match.group(2)
        for match in term_pattern.finditer(term_list_str):
            term = match.group(1).strip().rstrip(":")
            definition = match.group(3).strip()
            if term and term not in all_terms:
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

    appendix_content = ['<hr class="pagebreak"/>\n\n### Appendix B: Glossary\n']

    for term, definition in sorted_terms:
        appendix_content.append(f"**{term}**\n: {definition}\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix_content))

    print(f"Extracted and alphabetized {len(sorted_terms)} unique key terms into {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
