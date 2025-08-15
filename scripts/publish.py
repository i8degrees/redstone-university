#!/usr/bin/env python3
"""
Builds the course materials for web publication on GitHub.

This script processes files from the 'src' directory and generates a clean,
browsable course structure in the 'course' directory. It follows a multi-pass
approach to ensure that different types of content (special SVGs, standard
images, etc.) are handled correctly.

Core responsibilities:
1.  Sets up a clean build environment.
2.  Pass 1 (Special SVGs): Finds all gate SVGs (NOT.svg, etc.), copies them
    to assets, and replaces their Markdown with specific HTML <img> tags for
    proper display in web tables.
3.  Pass 2 (Standard Images): Finds all other local images (PNG, etc.), copies
    them to assets, and replaces their paths with absolute GitHub URLs.
4.  Pass 3 (Final HTML Polish): Applies non-image transformations, such as
    the theme-aware logo and centered captions for figures.
5.  Copies all static assets and writes the final processed markdown files.
"""

import os
import re
import shutil

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_DIR = "assets"
ASSETS_IMG_DIR = os.path.join(ASSETS_DIR, "images")

GITHUB_USER = "fielding"
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
    Processes a single markdown file through a multi-pass system.

    This function ensures that special image types are handled before general
    ones, preventing regex conflicts and ensuring correct output for both web
    and potential PDF builds.

    Args:
        src_path (str): The full path to the source markdown file.
        dest_path (str): The full path to the destination markdown file.
    """
    print(f"  - Processing: {src_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    gate_svg_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]*?(" + "|".join(GATE_SYMBOLS) + r")\.svg)\)")

    def gate_svg_replacer(match):
        """Copies the SVG and returns an HTML <img> tag with a fixed width."""
        alt_text, original_path, _ = match.groups()
        abs_url = copy_image_and_get_absolute_url(original_path, src_path)
        return f'<img src="{abs_url}" alt="{alt_text}" width="64px">'

    content = gate_svg_pattern.sub(gate_svg_replacer, content)

    standard_image_pattern = re.compile(r"!\[([^\]]*)\]\((?!http)([^)]+)\)")

    def standard_image_replacer(match):
        """Copies the image and returns a standard Markdown link with an absolute URL."""
        alt_text, original_path = match.groups()
        abs_url = copy_image_and_get_absolute_url(original_path, src_path)
        return f"![{alt_text}]({abs_url})"

    content = standard_image_pattern.sub(standard_image_replacer, content)

    content = apply_final_html_transforms(content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"    - Published to '{dest_path}'")


def copy_image_and_get_absolute_url(original_path, markdown_src_path):
    """
    Copies a local image to the central assets directory and returns its absolute URL.

    This is a helper function to avoid code duplication. It handles resolving
    the image path, creating a unique prefixed name, copying the file, and
    generating the final raw GitHub URL.

    Args:
        original_path (str): The relative path to the image from the markdown file.
        markdown_src_path (str): The path to the markdown file being processed.

    Returns:
        str: The absolute URL to the image on GitHub.
    """
    src_image_path = os.path.normpath(os.path.join(os.path.dirname(markdown_src_path), original_path))

    if not os.path.exists(src_image_path):
        print(f"    - ⚠️ WARNING: Image not found: {src_image_path}")
        return original_path  # Return original path if not found

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

    This includes the theme-aware logo and centered captions for figures. This
    should be run after all image paths have been finalized.

    Args:
        content (str): The markdown content with absolute image URLs.

    Returns:
        str: Content with final HTML transformations applied.
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
        if "project_assets" in root:
            continue

        for file in files:
            if file.endswith(".md"):
                src_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_file_path, SRC_DIR)
                dest_file_path = os.path.join(COURSE_DIR, relative_path)

                if file.endswith("draft.md"):
                    module_name = os.path.basename(root)
                    dest_file_path = os.path.join(os.path.dirname(dest_file_path), f"{module_name}.md")

                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                process_markdown_file(src_file_path, dest_file_path)

    print("\n✅ Build complete! The 'course' directory is ready for publication.")


if __name__ == "__main__":
    main()
