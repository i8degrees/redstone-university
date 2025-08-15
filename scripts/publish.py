#!/usr/bin/env python3
"""
Builds the course materials for web/github.

This script processes files from the 'src' directory and generates a clean,
browsable course structure in the 'course' directory. It is designed to be
the single source of truth for preparing the course for its web version.

Core responsibilities:
1.  Sets up a clean build environment by deleting and recreating the 'course'
    and 'assets/images' directories.
2.  Traverses the 'src' directory, finding all markdown files (including
    introductions, lessons, etc.).
3.  For each markdown file, it processes all referenced local images:
    - Copies the image to the central 'assets/images' directory with a unique,
      prefixed name to prevent conflicts.
    - Replaces the original relative image path in the markdown with an
      absolute URL pointing to the raw file on GitHub. This ensures images
      render correctly on the web.
4.  Applies GitHub-specific HTML transformations to the markdown content for
    enhanced presentation (e.g., light/dark mode logos, centered images with
    captions, and correctly sized images in tables).
5.  Copies static assets, like logos, that are not referenced directly in
    markdown files.
6.  Writes the final, processed markdown files to the 'course' directory,
    maintaining the original order and structure.
"""

import os
import re
import shutil

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_DIR = "assets"
ASSETS_IMG_DIR = os.path.join(ASSETS_DIR, "images")
LESSON_DRAFT_FILENAME = "draft.md"

GITHUB_USER = "fielding"
GITHUB_REPO = "redstone-university"
GITHUB_BRANCH = "main"
RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/" f"{GITHUB_BRANCH}/"

# This is used for some one off html transformations
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


def apply_github_html_transforms(content):
    """
    Applies several HTML transformations for optimal display on GitHub.
    This includes:
    - Replacing the Redstone University logo with a <picture> block for light/dark
      mode support.
    - Replacing gate SVGs with <img> tags that have a fixed width.
    - Replacing images with captions to be centered and properly formatted.

    Args:
        content (str): The markdown content.

    Returns:
        str: Content with HTML transformations applied.
    """

    def replace_logo(match):
        """Replaces the logo markdown with a <picture> HTML block."""
        logo_light = RAW_BASE_URL + ASSETS_IMG_DIR + "/logo.png"
        logo_dark = RAW_BASE_URL + ASSETS_IMG_DIR + "/logo-dark.png"
        return (
            f'<p align="center"><picture>'
            f'<source media="(prefers-color-scheme: light)" srcset="{logo_light}">'
            f'<img alt="Redstone University Logo" src="{logo_dark}">'
            f"</picture></p>"
        )

    def replace_gate_svgs(match):
        """Replaces gate SVG markdown with an HTML <img> tag with fixed width."""
        alt, src = match.groups()
        return f'<img src="{src}" alt="{alt}" width="64px">'

    def replace_images_with_captions(match):
        """Replaces image + caption markdown with a centered HTML block."""
        alt, src, caption = match.groups()
        return (
            f'<div align="center">'
            f'<img src="{src}" alt="{alt}" width="512px"/><br/>'
            f"<em>{caption}</em>"
            f"</div><br/>"
        )

    content = re.sub(r"!\[Redstone University Logo\]\([^)]+\)", replace_logo, content)

    svg_pattern = r"!\[([^\]]*)\]\((" + "|".join(f"[^)]*?{g}\\.svg" for g in GATE_SYMBOLS) + r")\)"
    content = re.sub(svg_pattern, replace_gate_svgs, content)

    caption_pattern = r"!\[([^\]]*)\]\(([^)]+)\)\s*\n\s*\*(Figure:[^\n]*)\*"
    content = re.sub(caption_pattern, replace_images_with_captions, content)

    return content


def process_markdown_file(src_path, dest_path):
    """
    Processes a single markdown file.

    Reads the content, processes all local images to have absolute GitHub
    URLs, applies HTML transformations, and writes the result to the
    destination.

    Args:
        src_path (str): The full path to the source markdown file.
        dest_path (str): The full path to the destination markdown file.
    """
    print(f"  - Processing: {src_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    image_pattern = re.compile(r"!\[([^\]]*)\]\((?!http)([^)]+)\)")

    def image_path_replacer(match):
        """
        A replacer function for re.sub that processes one image match.
        """
        alt_text, original_path = match.groups()

        src_image_path = os.path.normpath(os.path.join(os.path.dirname(src_path), original_path))

        if not os.path.exists(src_image_path):
            print(f"    - ⚠️ WARNING: Image not found: {src_image_path}")
            return match.group(0)

        module_dir = os.path.basename(os.path.dirname(src_path))
        module_prefix = module_dir.split("_")[0]
        new_image_name = f"{module_prefix}_{os.path.basename(src_image_path)}"
        dest_image_path = os.path.join(ASSETS_IMG_DIR, new_image_name)

        shutil.copy2(src_image_path, dest_image_path)

        absolute_url = RAW_BASE_URL + dest_image_path.replace(os.path.sep, "/")

        return f"![{alt_text}]({absolute_url})"

    content = image_pattern.sub(image_path_replacer, content)
    content = apply_github_html_transforms(content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"    - Published to '{dest_path}'")


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

                if file == LESSON_DRAFT_FILENAME:
                    module_name = os.path.basename(root)
                    dest_file_path = os.path.join(os.path.dirname(dest_file_path), f"{module_name}.md")

                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                process_markdown_file(src_file_path, dest_file_path)

    print("\n✅ Build complete! The 'course' directory is ready for publication.")


if __name__ == "__main__":
    main()
