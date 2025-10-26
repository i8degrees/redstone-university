#!/bin/bash
#
#

SRC_DIR="src"
COURSE_DIR="course"
ASSETS_IMG_DIR="assets/images"
PDF_INPUT_FILE=${COURSE_DIR}+"Redstone-University.md"

# Appendices to add at the end
APPENDIX_A="course/Z-Appendices/Appendix-A_Solutions.md"
APPENDIX_B="course/Z-Appendices/Appendix-B_Glossary.md"

# input
SRC="document.md"
PREFIX="course" # install
TEMPLATE_PATH="/usr/share/pandoc/data/templates/eisvogel.latex"
OUTPUT="${PREFIX}/course_file.pdf"

ARGS=(--filter pandoc-latex-environment --listings)
pandoc "${SRC}" -o "${OUTPUT}" \
  --from markdown --template "${TEMPLATE_PATH}" \
#"${ARGS[@]}"
