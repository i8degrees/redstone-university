import os
import re
import shutil

SRC_DIR = "src"
COURSE_DIR = "course"
ASSETS_DIR = "assets/images"
PROJECT_ASSETS_SRC_DIR = os.path.join(SRC_DIR, "project_assets")
LESSON_DRAFT_FILENAME = "draft.md"


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
        shutil.copy2(course_intro_src_path, course_intro_dest_path)
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
                shutil.copy2(intro_src_path, intro_dest_path)
                print("  - Published Part Introduction")

            for module_name in sorted(os.listdir(part_src_path)):
                module_src_path = os.path.join(part_src_path, module_name)

                if os.path.isdir(module_src_path) and module_name[0].isdigit():
                    draft_path = os.path.join(module_src_path, LESSON_DRAFT_FILENAME)

                    if os.path.exists(draft_path):
                        print(f"  - Processing Module: {module_name}")

                        with open(draft_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        module_image_src_dir = os.path.join(module_src_path, "images")
                        if os.path.exists(module_image_src_dir):
                            for image_filename in os.listdir(module_image_src_dir):
                                module_prefix = module_name.split("_")[0]
                                new_image_name = f"{module_prefix}_{image_filename}"

                                old_image_path_in_md = f"./images/{image_filename}"
                                new_image_path_in_md = f"../../{ASSETS_DIR}/{new_image_name}"

                                image_src_path = os.path.join(module_image_src_dir, image_filename)
                                image_dest_path = os.path.join(ASSETS_DIR, new_image_name)
                                shutil.copy2(image_src_path, image_dest_path)

                                content = content.replace(old_image_path_in_md, new_image_path_in_md)
                                print(f"    - Migrated image '{image_filename}' and updated path.")

                        # Special case: Replace logo image with custom <picture> HTML
                        logo_md_pattern = r"!\[Redstone University Logo\]\([^)]+\)"
                        logo_html = (
                            '<p align="center">\n'
                            "    <picture>\n"
                            '      <source media="(prefers-color-scheme: light)" srcset="assets/images/logo.png">\n'
                            '      <img alt="Redstone University Logo" src="assets/images/logo-dark.png">\n'
                            "    </picture>\n"
                            "</p>"
                        )
                        content = re.sub(logo_md_pattern, logo_html, content)

                        # Transform Markdown image syntax to centered HTML image blocks with captions
                        def md_img_to_centered_html(md_content):
                            def replacer(match):
                                alt = match.group(1)
                                src = match.group(2)
                                # Try to extract a figure caption from the alt text
                                caption = f"Figure: {alt}" if alt else ""
                                # Centered HTML block for GitHub
                                html = f'<div align="center">' f'<img src="{src}" width="512px"/>'
                                if caption:
                                    html += f"<br/>{caption}"
                                html += "</div>"
                                return html

                            # Replace all Markdown image syntaxes
                            pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
                            return re.sub(pattern, replacer, md_content)

                        content = md_img_to_centered_html(content)

                        final_lesson_name = f"{module_name}.md"
                        final_lesson_path = os.path.join(part_dest_path, final_lesson_name)
                        with open(final_lesson_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"    - Published lesson to '{final_lesson_path}'")

    print("\n✅ Build complete! The 'course' directory is up to date.")


if __name__ == "__main__":
    main()
