import os
import re
from glob import glob

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_IMG_DIR = "assets/images"
PDF_INPUT_FILE = os.path.join(COURSE_DIR, "Redstone-University.md")

# Appendices to add at the end
APPENDIX_A = "course/Z-Appendices/Appendix-A_Solutions.md"
APPENDIX_B = "course/Z-Appendices/Appendix-B_Glossary.md"

# --- GitHub URL Configuration ---
GITHUB_USER = "fielding"
GITHUB_REPO = "redstone-university"
GITHUB_BRANCH = "main"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/"


def get_course_files_in_order():
    """
    Finds all 'draft.md' and 'introduction.md' files and returns them in the
    correct structural order for the final combined document.
    """
    print("🔎 Determining correct file order for concatenation...")
    ordered_files = []

    main_intro = os.path.join(SRC_DIR, "introduction.md")
    if os.path.exists(main_intro):
        ordered_files.append(main_intro)
        print(f"  - Found main introduction: {main_intro}")

    part_dirs = sorted(glob(os.path.join(SRC_DIR, "Part-*/")))
    for part_dir in part_dirs:
        part_intro = os.path.join(part_dir, "introduction.md")
        if os.path.exists(part_intro):
            ordered_files.append(part_intro)
            print(f"  - Found Part introduction: {part_intro}")

        lesson_dirs = sorted(glob(os.path.join(part_dir, "[0-9]*_*/")))
        for lesson_dir in lesson_dirs:
            draft_file = os.path.join(lesson_dir, "draft.md")
            if os.path.exists(draft_file):
                ordered_files.append(draft_file)

    print("✅ File order determined.")
    return ordered_files


def process_markdown_content(content, file_path):
    """
    Processes the raw markdown content to make it PDF-ready by:
    1. Removing inline solution <details> blocks.
    2. Rewriting image paths to be absolute GitHub URLs, handling prefixes correctly.
    """
    # 1. Remove solution blocks
    solution_placeholder = "> **(Solution for this problem can be found in Appendix A.)**"
    content = re.sub(r"<details>.*?</details>", solution_placeholder, content, flags=re.DOTALL)

    # 2. Define a smarter replacer function for image paths
    def image_path_replacer(match):
        alt_text, original_path = match.groups()

        # If it's already an absolute URL, leave it alone.
        if original_path.startswith("http"):
            return match.group(0)

        image_basename = os.path.basename(original_path)
        new_image_name = ""

        # Check if the markdown file is a lesson module (e.g., /00_Prelude/draft.md).
        # Its parent directory will start with digits and contain an underscore.
        parent_dir_name = os.path.basename(os.path.dirname(file_path))
        if parent_dir_name[:2].isdigit() and "_" in parent_dir_name:
            # This is a lesson module, so we must add the numerical prefix.
            module_prefix = parent_dir_name.split("_")[0]
            new_image_name = f"{module_prefix}_{image_basename}"
        else:
            # This is not a lesson module (e.g., introduction.md), so no prefix is needed.
            # The image is a static asset like 'logo.png'.
            new_image_name = image_basename

        # Construct the final, correct absolute URL
        absolute_url = RAW_BASE_URL + ASSETS_IMG_DIR + "/" + new_image_name
        return f"![{alt_text}]({absolute_url})"

    # Apply the smarter replacer function to the content
    content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image_path_replacer, content)

    return content


def main():
    print("🚀 Starting PDF preparation process...")

    files_to_combine = get_course_files_in_order()
    print(f"📚 Found {len(files_to_combine)} content files to combine for the PDF.")

    full_course_content = []
    for file_path in files_to_combine:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        processed_content = process_markdown_content(content, file_path)
        full_course_content.append(processed_content)

    combined_md = '\n\n<hr class="pagebreak"/>\n\n'.join(full_course_content)

    for appendix_path in [APPENDIX_A, APPENDIX_B]:
        if os.path.exists(appendix_path):
            print(f"➕ Appending {os.path.basename(appendix_path)}...")
            with open(appendix_path, "r", encoding="utf-8") as f:
                appendix_content = f.read()
            combined_md += '\n\n<hr class="pagebreak"/>\n\n' + appendix_content
        else:
            print(f"⚠️ Warning: Appendix file not found at {appendix_path}. Skipping.")

    with open(PDF_INPUT_FILE, "w", encoding="utf-8") as f:
        f.write(combined_md)

    print(f"✅ Successfully created PDF input file at: {PDF_INPUT_FILE}")


if __name__ == "__main__":
    main()
