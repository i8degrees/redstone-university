#!/usr/bin/env python3
"""
Builds the course materials for web publication on GitHub.

This script processes files from the 'src' directory and generates a clean,
browsable course structure in the 'course' directory. It assumes a PNG-first
strategy for all images to ensure maximum compatibility.

Core responsibilities:
1.  Sets up a clean build environment.
2.  Processes all markdown files from the 'src' directory.
3.  For each local image referenced:
    - Copies the image to the central 'assets/images' directory.
    - Replaces its path with an absolute GitHub URL.
    - If the image is a gate symbol (e.g., NOT.png), it's converted to an
      HTML <img> tag with a fixed width for proper table display.
4.  Applies final HTML polishing for logos and figure captions.
5.  Writes the final markdown files to a clean, flat 'course' directory structure.
"""

import os
import re
import shutil

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_DIR = "assets"
ASSETS_IMG_DIR = os.path.join(ASSETS_DIR, "images")

GITHUB_USER = "i8degrees"
GITHUB_REPO = "redstone-university"
GITHUB_BRANCH = "main"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/" f"{GITHUB_BRANCH}/"

# A list of gate names used for special image handling in tables.
GATE_SYMBOLS = ["NOT", "AND", "OR", "NAND", "NOR", "XOR", "XNOR"]


def setup_directories():
    """Cleans and creates the necessary build directories."""
    print("🧹 Cleaning old build directories...")
    if os.path.exists(COURSE_DIR):
        shutil.rmtree(COURSE_DIR)
    if os.path.exists(ASSETS_IMG_DIR):
        shutil.rmtree(ASSETS_IMG_DIR)

    os.makedirs(COURSE_DIR)
    os.makedirs(ASSETS_IMG_DIR)
    print("📁 Created fresh build directories.")


def copy_static_assets():
    """Copies static project assets (e.g., logos) to the build directory."""
    project_assets_src = os.path.join(SRC_DIR, "project_assets")
    if os.path.exists(project_assets_src):
        for asset in os.listdir(project_assets_src):
            shutil.copy2(os.path.join(project_assets_src, asset), ASSETS_IMG_DIR)
        print("🎨 Copied static project assets.")


def process_markdown_file(src_path, dest_path):
    """
    Processes a single markdown file, handling all images in one pass.
    """
    print(f"  - Processing: {src_path} -> {dest_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    image_pattern = re.compile(r"!\[([^\]]*)\]\((?!http)([^)]+)\)")

    def image_replacer(match):
        """
        Copies images and returns the appropriate Markdown or HTML.
        """
        alt_text, original_path = match.groups()

        basename = os.path.basename(original_path)
        filename_no_ext, _ = os.path.splitext(basename)
        is_gate_symbol = filename_no_ext in GATE_SYMBOLS

        abs_url = copy_image_and_get_absolute_url(original_path, src_path)

        if is_gate_symbol:
            return f'<img src="{abs_url}" alt="{alt_text}" width="64px">'
        else:
            return f"![{alt_text}]({abs_url})"

    content = image_pattern.sub(image_replacer, content)

    content = apply_final_html_transforms(content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)


def copy_image_and_get_absolute_url(original_path, markdown_src_path):
    """
    Copies a local image to assets and returns its absolute GitHub URL.
    """
    src_image_path = os.path.normpath(os.path.join(os.path.dirname(markdown_src_path), original_path))

    if not os.path.exists(src_image_path):
        print(f"    - ⚠️ WARNING: Image not found: {src_image_path}")
        return original_path

    module_dir = os.path.basename(os.path.dirname(markdown_src_path))
    module_prefix = module_dir.split("_")[0]
    new_image_name = f"{module_prefix}_{os.path.basename(src_image_path)}"
    dest_image_path = os.path.join(ASSETS_IMG_DIR, new_image_name)

    shutil.copy2(src_image_path, dest_image_path)

    absolute_url = RAW_BASE_URL + dest_image_path.replace(os.path.sep, "/")
    return absolute_url


def apply_final_html_transforms(content):
    """
    Applies non-image-copy transformations for web presentation.
    """
    logo_light = RAW_BASE_URL + ASSETS_IMG_DIR + "/logo.png"
    logo_dark = RAW_BASE_URL + ASSETS_IMG_DIR + "/logo-dark.png"
    logo_html = (
        f'<p align="center"><picture>'
        f'<source media="(prefers-color-scheme: light)" srcset="{logo_light}">'
        f'<img alt="Redstone University Logo" src="{logo_dark}">'
        f"</picture></p>"
    )
    content = re.sub(r"!\[Redstone University Logo\]\([^)]+\)", logo_html, content)

    caption_pattern = r"!\[([^\]]*)\]\(([^)]+)\)\s*\n\s*\*(Figure:[^\n]*)\*"

    def caption_replacer(match):
        alt, src, caption = match.groups()
        return (
            f'<div align="center">'
            f'<img src="{src}" alt="{alt}" width="512px"/><br/>'
            f"<em>{caption}</em>"
            f"</div><br/>"
        )

    content = re.sub(caption_pattern, caption_replacer, content)
    return content


def main():
    """Main function to orchestrate the entire build process."""
    setup_directories()
    copy_static_assets()

    print("\n📝 Processing all markdown source files...")
    for root, _, files in os.walk(SRC_DIR):
        if "project_assets" in root or "images" in root:
            continue

        dest_path = None
        src_path = None

        if "draft.md" in files:
            src_path = os.path.join(root, "draft.md")
            module_name = os.path.basename(root)
            parent_dir_rel_path = os.path.relpath(os.path.dirname(root), SRC_DIR)
            dest_dir = os.path.join(COURSE_DIR, parent_dir_rel_path)
            dest_path = os.path.join(dest_dir, f"{module_name}.md")
        elif "introduction.md" in files:
            src_path = os.path.join(root, "introduction.md")
            relative_dir = os.path.relpath(root, SRC_DIR)
            dest_dir = os.path.join(COURSE_DIR, relative_dir) if relative_dir != "." else COURSE_DIR
            dest_path = os.path.join(dest_dir, "README.md")

        if src_path and dest_path:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            process_markdown_file(src_path, dest_path)

    print("\n✅ Build complete! The 'course' directory has the correct flat structure.")


if __name__ == "__main__":
    main()
