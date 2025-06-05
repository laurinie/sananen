#!/usr/bin/env python3
"""
Finnish Character Fixer
Fixes common encoding issues with Finnish characters äöå in text files.

Common issues:
- ä appears as Ã¤
- ö appears as Ã¶  
- å appears as Ã¥
"""

import sys
import os
from pathlib import Path

def fix_finnish_chars(input_file, output_file=None):
    """
    Fix Finnish character encoding issues in a text file.
    
    Args:
        input_file (str): Path to input file
        output_file (str, optional): Path to output file. If None, overwrites input file.
    """
    
    # Character replacements mapping
    char_fixes = {
        'Ã¤': 'ä',  # ä
        'Ã¶': 'ö',  # ö  
        'Ã¥': 'å',  # å
        'Ã„': 'Ä',  # Ä
        'Ã–': 'Ö',  # Ö
        'Ã…': 'Å',  # Å
    }
    
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"Error: File '{input_file}' not found!")
        return False
    
    print(f"Processing file: {input_file}")
    print(f"File size: {input_path.stat().st_size / (1024*1024):.1f} MB")
    
    # Read the file
    try:
        with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        print(f"✓ File read successfully")
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Count issues before fixing
    issues_found = 0
    for broken_char in char_fixes.keys():
        count = content.count(broken_char)
        if count > 0:
            print(f"Found {count} instances of '{broken_char}'")
            issues_found += count
    
    if issues_found == 0:
        print("✓ No character encoding issues found!")
        return True
    
    print(f"\nFixing {issues_found} character encoding issues...")
    
    # Apply fixes
    fixed_content = content
    for broken_char, correct_char in char_fixes.items():
        fixed_content = fixed_content.replace(broken_char, correct_char)
    
    # Determine output file
    if output_file is None:
        output_path = input_path
        backup_path = input_path.with_suffix(input_path.suffix + '.backup')
        
        # Create backup
        print(f"Creating backup: {backup_path}")
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        output_path = Path(output_file)
    
    # Write fixed content
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"✓ Fixed file written to: {output_path}")
        
        # Verify fixes
        verification_issues = 0
        for broken_char in char_fixes.keys():
            count = fixed_content.count(broken_char)
            verification_issues += count
        
        if verification_issues == 0:
            print(f"✓ All {issues_found} character encoding issues fixed successfully!")
        else:
            print(f"⚠ Warning: {verification_issues} issues still remain")
            
        return True
        
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix_finnish_chars.py <input_file> [output_file]")
        print("\nExamples:")
        print("  python3 fix_finnish_chars.py sanat.txt")
        print("  python3 fix_finnish_chars.py sanat.txt sanat_fixed.txt")
        print("\nThis script fixes common Finnish character encoding issues:")
        print("  Ã¤ → ä")
        print("  Ã¶ → ö") 
        print("  Ã¥ → å")
        print("  Ã„ → Ä")
        print("  Ã– → Ö")
        print("  Ã… → Å")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = fix_finnish_chars(input_file, output_file)
    
    if success:
        print("\n🎉 Character fixing completed successfully!")
    else:
        print("\n❌ Character fixing failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 