import os

COURSE_DIR = "course"
APPENDIX_A = "course/Z-Appendices/Appendix-A_Solutions.md"
APPENDIX_B = "course/Z-Appendices/Appendix-B_Glossary.md"
FINAL_FILE = "course/Redstone-University.md"


def collect_markdown_files(directory):
    """
    Recursively collect markdown files in the specified order:
    - README.md first (if present)
    - Other .md files in alphabetical order (excluding README.md)
    - Then recurse into subdirectories in alphabetical order
    Returns a list of file paths.
    """
    files = []
    entries = sorted(os.listdir(directory))
    if "README.md" in entries:
        files.append(os.path.join(directory, "README.md"))
    for entry in entries:
        if entry.endswith(".md") and entry != "README.md":
            files.append(os.path.join(directory, entry))
    for entry in entries:
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            files.extend(collect_markdown_files(full_path))
    return files


def read_file(path):
    if not os.path.exists(path):
        print(f"Warning: {path} does not exist.")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def main():
    print(f"🔍 Collecting markdown files from '{COURSE_DIR}'...")
    files = collect_markdown_files(COURSE_DIR)
    print(f"📝 Concatenating {len(files)} markdown files into '{FINAL_FILE}'...")
    combined = ""
    for idx, file_path in enumerate(files):
        content = read_file(file_path)
        if content:
            combined += content
            if idx < len(files) - 1:
                combined += '\n\n<hr class="pagebreak"/>\n\n'
    # Append appendices if they exist
    appendix_a = read_file(APPENDIX_A)
    appendix_b = read_file(APPENDIX_B)
    for appendix in [appendix_a, appendix_b]:
        if appendix:
            combined += '\n\n<hr class="pagebreak"/>\n\n' + appendix
    with open(FINAL_FILE, "w", encoding="utf-8") as f:
        f.write(combined)
        f.write("\n")
    print(f"✅ Combined main content and appendices into {FINAL_FILE}")


if __name__ == "__main__":
    main()
