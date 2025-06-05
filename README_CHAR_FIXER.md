# Finnish Character Fixer

Scripts to fix common encoding issues with Finnish characters (äöå) in text files.

## Problem

When text files with Finnish characters are saved with incorrect encoding, you may see:
- `ä` appears as `Ã¤`
- `ö` appears as `Ã¶`
- `å` appears as `Ã¥`
- `Ä` appears as `Ã„`
- `Ö` appears as `Ã–`
- `Å` appears as `Ã…`

## Scripts

### 1. `fix_finnish_chars.py` (Python Script)

Main script that does the character fixing.

**Usage:**
```bash
python3 fix_finnish_chars.py <input_file> [output_file]
```

**Examples:**
```bash
# Fix file in place (creates backup)
python3 fix_finnish_chars.py sanat.txt

# Fix to a new file
python3 fix_finnish_chars.py sanat.txt sanat_fixed.txt
```

**Features:**
- Automatically detects and counts encoding issues
- Creates backup when fixing in place
- Reports number of fixes made
- Verifies that all issues were resolved

### 2. `fix_chars.sh` (Bash Wrapper)

Simple wrapper script for easier usage.

**Usage:**
```bash
./fix_chars.sh <input_file> [output_file]
```

**Examples:**
```bash
# Fix file in place
./fix_chars.sh sanat.txt

# Fix to a new file  
./fix_chars.sh sanat.txt sanat_clean.txt
```

## Example Output

```
Processing file: sanat.txt
File size: 2.8 MB
✓ File read successfully
Found 35039 instances of 'Ã¤'
Found 8279 instances of 'Ã¶'
Found 1 instances of 'Ã¥'
Found 1 instances of 'Ã„'

Fixing 43320 character encoding issues...
Creating backup: sanat.txt.backup
✓ Fixed file written to: sanat.txt
✓ All 43320 character encoding issues fixed successfully!

🎉 Character fixing completed successfully!
```

## What Gets Fixed

| Broken | Fixed | Character |
|--------|--------|-----------|
| `Ã¤`   | `ä`    | a with umlaut (lowercase) |
| `Ã¶`   | `ö`    | o with umlaut (lowercase) |
| `Ã¥`   | `å`    | a with ring (lowercase) |
| `Ã„`   | `Ä`    | A with umlaut (uppercase) |
| `Ã–`   | `Ö`    | O with umlaut (uppercase) |
| `Ã…`   | `Å`    | A with ring (uppercase) |

## Requirements

- Python 3.x
- Text file with Finnish encoding issues

## Safety

- When fixing in place, the script automatically creates a `.backup` file
- The script verifies all fixes were applied correctly
- Read-only operation first to count issues before making changes 