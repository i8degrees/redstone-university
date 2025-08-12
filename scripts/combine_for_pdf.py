import os

MAIN_FILE = "course/Redstone-University-for-pdf.md"
APPENDIX_B = "appendices/Appendix-B_Solutions.md"
APPENDIX_C = "appendices/Appendix-C_Key-Terms.md"
FINAL_FILE = "course/Redstone-University.md"


def read_file(path):
    if not os.path.exists(path):
        print(f"Warning: {path} does not exist.")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def main():
    main_content = read_file(MAIN_FILE)
    appendix_b = read_file(APPENDIX_B)
    appendix_c = read_file(APPENDIX_C)

    combined = "\n\n".join(part for part in [main_content, appendix_b, appendix_c] if part)

    with open(FINAL_FILE, "w", encoding="utf-8") as f:
        f.write(combined)
        f.write("\n")

    print(f"✅ Combined main content and appendices into {FINAL_FILE}")


if __name__ == "__main__":
    main()
