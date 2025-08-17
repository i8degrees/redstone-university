import os
import re

INPUT_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_FILE = "course/Z-Appendices/Appendix-B_Glossary.md"


def extract_module_titles(md_content):
    """
    Extracts module numbers and titles from '## Module X: Title' headings.
    Returns a dictionary of {module_num: title}.
    """
    module_pattern = re.compile(r"^##\s+Module (\d+): (.+)$", re.MULTILINE)
    module_titles = {}
    for match in module_pattern.finditer(md_content):
        module_num = match.group(1)
        title = match.group(2).strip()
        module_titles[module_num] = title
        print(f"📋 Found module: Module {module_num}: {title}")
    return module_titles


def extract_key_terms_from_md(md_content, file_path):
    """
    Extracts key terms and definitions from markdown content under '### Key Terms (Module X)' headings.
    Returns a list of (term, definition, module_num) tuples with detailed logging.
    """
    pattern = re.compile(
        r"^###\s*Key Terms\s*\(Module (\d+)\).*?\n((?:-\s+\*\*[^*]+\*\*:\s*.+?(?=\n-|\n\n|$))+)",
        re.MULTILINE | re.DOTALL,
    )
    term_pattern = re.compile(r"-\s+\*\*([^*]+?)\*\*:\s+(.+?)(?=\n-|\n\n|$)", re.DOTALL)
    all_terms = []

    matches = pattern.finditer(md_content)
    section_count = 0
    for section_match in matches:
        section_count += 1
        module_num = section_match.group(1)
        term_list_str = section_match.group(2)
        print(f"📄 Found 'Key Terms (Module {module_num})' section {section_count} at position {section_match.start()}")

        for match in term_pattern.finditer(term_list_str):
            term = match.group(1).strip().rstrip(":")
            definition = match.group(2).strip()
            if term and definition:
                all_terms.append((term, definition, module_num))
                print(f"  - Extracted term: '{term}' (Module {module_num})")
            else:
                print(f"  ⚠️ Warning: Skipped invalid term entry in {file_path}: {match.group(0)}")

    if section_count == 0:
        print(f"⚠️ Warning: No 'Key Terms' sections found in {file_path}")
    else:
        print(f"📝 Extracted {len(all_terms)} terms from {section_count} sections")

    return all_terms


def main():
    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)

    print(f"🔍 Processing input file: '{INPUT_FILE}'...")
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: {INPUT_FILE} does not exist. Please run course_concat.py and extract_solutions.py first.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md = f.read()

    module_titles = extract_module_titles(md)
    if not module_titles:
        print(f"⚠️ Warning: No module titles found in {INPUT_FILE}")

    terms = extract_key_terms_from_md(md, INPUT_FILE)

    sorted_terms = sorted(terms, key=lambda x: x[0].lower())

    used_modules = sorted(set(module for _, _, module in sorted_terms))
    footnote_map = {module: str(i + 1) for i, module in enumerate(used_modules)}

    appendix_content = [
        '<hr class="pagebreak"/>\n\n'
        "### Appendix B: Glossary\n\n"
        "This glossary compiles key terms from the Redstone University curriculum, "
        "organized alphabetically. Each term includes a footnote indicating the module "
        "where it is introduced.\n"
    ]
    seen_terms = set()
    for term, definition, module in sorted_terms:
        if term in seen_terms:
            print(f"⚠️ Warning: Duplicate term '{term}' in Module {module}. Keeping first definition.")
            continue
        seen_terms.add(term)
        footnote = footnote_map.get(module, "Unknown")
        appendix_content.append(f"**{term}**[{footnote}]\n: {definition}\n")

    appendix_content.append("\n---\n")
    for module in used_modules:
        footnote_num = footnote_map[module]
        title = module_titles.get(module, f"Module {module}")
        appendix_content.append(f"[{footnote_num}]: {title}\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix_content))

    print(f"✅ Extracted and alphabetized {len(seen_terms)} unique key terms into {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
