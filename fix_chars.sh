#!/bin/bash

# Finnish Character Fixer - Bash Wrapper
# Fixes encoding issues with äöå characters

if [ $# -eq 0 ]; then
    echo "Usage: ./fix_chars.sh <filename> [output_filename]"
    echo ""
    echo "Examples:"
    echo "  ./fix_chars.sh sanat.txt"
    echo "  ./fix_chars.sh sanat.txt sanat_clean.txt"
    echo ""
    echo "This fixes common Finnish character encoding issues:"
    echo "  Ã¤ → ä, Ã¶ → ö, Ã¥ → å"
    exit 1
fi

python3 fix_finnish_chars.py "$@" 