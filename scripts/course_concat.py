import os

COURSE_DIR = "course"
OUTPUT_FILE = os.path.join(COURSE_DIR, "Redstone-University.md")


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


def concatenate_markdown_files(files, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for idx, file_path in enumerate(files):
            with open(file_path, "r", encoding="utf-8") as infile:
                content = infile.read().strip()
                outfile.write(content)
                if idx < len(files) - 1:
                    outfile.write('\n\n<hr class="pagebreak"/>\n\n')


def main():
    print(f"🔍 Collecting markdown files from '{COURSE_DIR}'...")
    files = collect_markdown_files(COURSE_DIR)
    print(f"📝 Concatenating {len(files)} markdown files into '{OUTPUT_FILE}'...")
    concatenate_markdown_files(files, OUTPUT_FILE)
    print("✅ Concatenation complete.")


if __name__ == "__main__":
    main()
