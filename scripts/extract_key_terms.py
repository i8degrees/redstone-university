import os
import re
from glob import glob

SRC_DIR = "src"
APPENDIX_FILE = "course/Z-Appendices/Appendix-B_Glossary.md"


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


def extract_key_terms_from_md(md_content, file_path):
    """
    Extracts key terms and definitions from '#### Key Terms (Module X)' sections.
    Returns a list of (term, definition, module_num) tuples with concise logging.
    """
    pattern = re.compile(
        r"^####\s*Key Terms\s*\(Module (\d+)\)\s*\n((?:-\s*\*\*[^*]+\*\*:[^\n]*(?:\n+(?!\s*-)[^\n]*)*\n*)+)",
        re.MULTILINE | re.DOTALL,
    )
    term_pattern = re.compile(r"-\s*\*\*([^*]+?)\*\*:\s*((?:[^\n]*(?:\n+(?!\s*-)[^\n]*)*))(?=\s*(?:-|\n|$))", re.DOTALL)
    all_terms = []

    matches = pattern.finditer(md_content)
    section_count = 0
    for section_match in matches:
        section_count += 1
        module_num = section_match.group(1)
        term_list_str = section_match.group(2).strip()
        print(f"📄 Found 'Key Terms (Module {module_num})' section in {file_path}")

        term_matches = term_pattern.finditer(term_list_str)
        term_count = 0
        for match in term_matches:
            term_count += 1
            term = match.group(1).strip().rstrip(":")
            definition = match.group(2).strip()
            if term and definition:
                all_terms.append((term, definition, module_num))
                print(f"  - Extracted term: '{term}' (Module {module_num})")
            else:
                print(f"  ⚠️ Warning: Skipped invalid term entry in {file_path}: {match.group(0).strip()}")

        print(f"  📝 Extracted {term_count} terms from Module {module_num}")

    if section_count == 0:
        print(f"⚠️ Warning: No 'Key Terms (Module X)' sections found in {file_path}")

    return all_terms


def collect_markdown_files(directory):
    """
    Collect all markdown files (*.md) in the src directory.
    """
    files = glob(os.path.join(directory, "**/*.md"), recursive=True)
    return sorted(files)


def main():
    os.makedirs(os.path.dirname(APPENDIX_FILE), exist_ok=True)

    all_terms = []
    module_titles = {}

    print(f"🔍 Scanning markdown files in '{SRC_DIR}'...")
    files = collect_markdown_files(SRC_DIR)
    if not files:
        print(f"❌ Error: No markdown files found in '{SRC_DIR}'.")
        return
    print(f"📜 Found {len(files)} markdown files: {files}")

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        module_titles.update(extract_module_titles(md, file_path))
        terms = extract_key_terms_from_md(md, file_path)
        all_terms.extend(terms)

    if not all_terms:
        print(f"❌ Error: No terms extracted from any files in '{SRC_DIR}'.")
        return

    sorted_terms = sorted(all_terms, key=lambda x: x[0].lower())

    appendix_content = [
        '<hr class="pagebreak"/>\n\n'
        "## Appendix B: Glossary\n\n"
        "This glossary compiles key terms from the Redstone University curriculum, "
        "organized alphabetically. Each term’s definition is followed by a footnote "
        "indicating the module where it is introduced.\n"
    ]
    seen_terms = set()
    unique_terms = []
    for term, definition, module in sorted_terms:
        if term in seen_terms:
            print(f"⚠️ Warning: Duplicate term '{term}' in Module {module}. Keeping first definition.")
            continue
        seen_terms.add(term)
        unique_terms.append((term, definition, module))
        appendix_content.append(f"**{term}**\n: {definition} [{module}]\n")

    appendix_content.append("\n---\n")
    for module in sorted(module_titles.keys(), key=int):
        title = module_titles.get(module, f"Module {module}")
        appendix_content.append(f"[{module}]: Module {module}: {title}\n")

    with open(APPENDIX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(appendix_content))

    print(f"✅ Extracted and alphabetized {len(unique_terms)} unique key terms into {APPENDIX_FILE}")


if __name__ == "__main__":
    main()
