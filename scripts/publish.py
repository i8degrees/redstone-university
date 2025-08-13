import os
import re
import shutil

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_DIR = "assets/images"
PROJECT_ASSETS_SRC_DIR = os.path.join(SRC_DIR, "project_assets")
LESSON_DRAFT_FILENAME = "draft.md"

GITHUB_USER = "fielding"
GITHUB_REPO = "redstone-university"
GITHUB_BRANCH = "main"
RAW_BASE_URL = (
    f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/refs/heads/{GITHUB_BRANCH}/assets/images/"
)

TRANSFORM_IMAGES_FOR_GITHUB = True


GATE_SYMBOLS = ["NOT", "AND", "OR", "NAND", "NOR", "XOR", "XNOR"]


def replace_gate_symbols_with_html(md_content):
    """
    Replace Markdown image syntax for gate SVGs with HTML <img> tags with width=64px.
    Only affects images named exactly as the gate symbols in the summary table.
    """

    def replacer(match):
        alt = match.group(1)
        src = match.group(2)
        for gate in GATE_SYMBOLS:
            if src.endswith(f"{gate}.svg"):
                return f'<img src="{src}" alt="{alt}" width="64px">'
        return match.group(0)

    pattern = r"!\[([^\]]*)\]\(([^)]+\.svg)\)"
    return re.sub(pattern, replacer, md_content)


def replace_gate_symbols_svg_with_png(md_content):
    """
    For PDF: Replace Markdown image links to gate SVGs with PNGs (same basename).
    """

    def replacer(match):
        alt = match.group(1)
        src = match.group(2)
        for gate in GATE_SYMBOLS:
            if src.endswith(f"{gate}.svg"):
                png_src = src[:-4] + ".png"
                return f"![{alt}]({png_src})"
        return match.group(0)

    pattern = r"!\[([^\]]*)\]\(([^)]+\.svg)\)"
    return re.sub(pattern, replacer, md_content)


def md_img_with_caption_to_centered_html(md_content):
    """
    Transform Markdown image + caption pairs to centered HTML blocks for GitHub.
    - If an image is followed by a *Figure: ...* line, combine them into a single centered HTML block.
    - If not, fallback to using the alt text as the caption.
    """

    def img_caption_replacer(match):
        alt = match.group(1)
        src = match.group(2)
        caption = match.group(3)
        html = (
            f'<div align="center">'
            f'<img src="{src}" alt="{alt}" width="512px"/><br/>'
            f"<em>{caption}</em>"
            f"</div></br></br>"
        )
        return html

    pattern_pair = r"!\[([^\]]*)\]\(([^)]+)\)\s*\n\s*\*(Figure:[^\n]*)\*"
    md_content = re.sub(pattern_pair, img_caption_replacer, md_content)

    def img_fallback_replacer(match):
        alt = match.group(1)
        src = match.group(2)
        caption = f"Figure: {alt}" if alt else ""
        html = f'<div align="center"><img src="{src}" alt="{alt}" width="512px"/>'
        if caption:
            html += f"<br/>{caption}"
        html += "</div>"
        return html

    pattern_img = r"!\[([^\]]*)\]\(([^)]+)\)"
    md_content = re.sub(pattern_img, img_fallback_replacer, md_content)
    return md_content


def replace_all_image_paths_with_absolute(content, image_map):
    """
    Replace all local image paths in the Markdown content with absolute GitHub raw URLs.
    image_map: dict mapping old local paths (as used in the Markdown) to absolute URLs.
    """
    for old_path, abs_url in image_map.items():
        content = content.replace(old_path, abs_url)
    return content


def replace_logo_with_picture_html(content):
    """
    Replace the Redstone University Logo Markdown image with a <picture> HTML block using absolute URLs.
    """
    logo_md_pattern = r"!\[Redstone University Logo\]\([^)]+\)"
    logo_light_url = RAW_BASE_URL + "logo.png"
    logo_dark_url = RAW_BASE_URL + "logo-dark.png"
    logo_html = (
        '<p align="center">\n'
        "    <picture>\n"
        f'      <source media="(prefers-color-scheme: light)" srcset="{logo_light_url}">\n'
        f'      <img alt="Redstone University Logo" src="{logo_dark_url}">\n'
        "    </picture>\n"
        "</p>"
    )
    return re.sub(logo_md_pattern, logo_html, content)


def main():
    print("🚀 Starting Redstone University course build...")

    if os.path.exists(COURSE_DIR):
        shutil.rmtree(COURSE_DIR)
        print(f"🧹 Cleaned old '{COURSE_DIR}' directory.")
    if os.path.exists(ASSETS_DIR):
        shutil.rmtree(ASSETS_DIR)
        print(f"🧹 Cleaned old '{ASSETS_DIR}' directory.")

    os.makedirs(COURSE_DIR)
    os.makedirs(ASSETS_DIR)
    print("📁 Created fresh build directories.")

    if os.path.exists(PROJECT_ASSETS_SRC_DIR):
        for asset_filename in os.listdir(PROJECT_ASSETS_SRC_DIR):
            src_path = os.path.join(PROJECT_ASSETS_SRC_DIR, asset_filename)
            dest_path = os.path.join(ASSETS_DIR, asset_filename)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)
        print(f"🎨 Copied static project assets from '{PROJECT_ASSETS_SRC_DIR}'.")

    course_intro_src_path = os.path.join(SRC_DIR, "introduction.md")
    course_intro_dest_path = os.path.join(COURSE_DIR, "README.md")

    if os.path.exists(course_intro_src_path):
        with open(course_intro_src_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = replace_logo_with_picture_html(content)

        content = replace_gate_symbols_with_html(content)

        image_pattern = r"!\[[^\]]*\]\(([^)]+)\)"
        image_paths = set(re.findall(image_pattern, content))
        image_map = {}
        for path in image_paths:
            filename = os.path.basename(path)
            abs_url = RAW_BASE_URL + filename
            image_map[path] = abs_url
        content = replace_all_image_paths_with_absolute(content, image_map)

        if TRANSFORM_IMAGES_FOR_GITHUB:
            content = md_img_with_caption_to_centered_html(content)

        with open(course_intro_dest_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Published Course Introduction")

    for part_name in sorted(os.listdir(SRC_DIR)):
        part_src_path = os.path.join(SRC_DIR, part_name)
        part_dest_path = os.path.join(COURSE_DIR, part_name)

        if os.path.isdir(part_src_path) and part_name != "project_assets":
            os.makedirs(part_dest_path)
            print(f"\nProcessing Part: {part_name}")

            intro_src_path = os.path.join(part_src_path, "introduction.md")
            intro_dest_path = os.path.join(part_dest_path, "README.md")
            if os.path.exists(intro_src_path):
                with open(intro_src_path, "r", encoding="utf-8") as f:
                    content = f.read()

                content = replace_logo_with_picture_html(content)

                content = replace_gate_symbols_with_html(content)

                image_pattern = r"!\[[^\]]*\]\(([^)]+)\)"
                image_paths = set(re.findall(image_pattern, content))
                image_map = {}
                for path in image_paths:
                    filename = os.path.basename(path)
                    abs_url = RAW_BASE_URL + filename
                    image_map[path] = abs_url
                content = replace_all_image_paths_with_absolute(content, image_map)

                if TRANSFORM_IMAGES_FOR_GITHUB:
                    content = md_img_with_caption_to_centered_html(content)

                with open(intro_dest_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print("  - Published Part Introduction")

            for module_name in sorted(os.listdir(part_src_path)):
                module_src_path = os.path.join(part_src_path, module_name)

                if os.path.isdir(module_src_path) and module_name[0].isdigit():
                    draft_path = os.path.join(module_src_path, LESSON_DRAFT_FILENAME)

                    if os.path.exists(draft_path):
                        print(f"  - Processing Module: {module_name}")

                        with open(draft_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        image_pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
                        found_images = image_pattern.findall(content)
                        image_map = {}

                        for image_path in found_images:
                            if image_path.startswith("http"):
                                continue

                            src_image_full_path = os.path.normpath(os.path.join(module_src_path, image_path))
                            if os.path.exists(src_image_full_path):
                                image_filename = os.path.basename(image_path)
                                module_prefix = module_name.split("_")[0]
                                new_image_name = f"{module_prefix}_{image_filename}"

                                image_dest_path = os.path.join(ASSETS_DIR, new_image_name)
                                shutil.copy2(src_image_full_path, image_dest_path)

                                new_path_for_md = f"../../assets/images/{new_image_name}"
                                content = content.replace(image_path, new_path_for_md)
                                print(
                                    f"    - Migrated image '{image_filename}' to '{new_image_name}' and updated path."
                                )
                            else:
                                print(f"    - WARNING: Image not found at '{src_image_full_path}'")

                        content = replace_logo_with_picture_html(content)

                        content = replace_gate_symbols_with_html(content)

                        if TRANSFORM_IMAGES_FOR_GITHUB:
                            content = md_img_with_caption_to_centered_html(content)

                        final_lesson_name = f"{module_name}.md"
                        final_lesson_path = os.path.join(part_dest_path, final_lesson_name)
                        with open(final_lesson_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"    - Published lesson to '{final_lesson_path}'")

    print("\n✅ Build complete! The 'course' directory is up to date.")


if __name__ == "__main__":
    main()
