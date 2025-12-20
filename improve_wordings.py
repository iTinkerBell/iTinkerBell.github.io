#!/usr/bin/env python3
"""
Script to improve wordings in HTML files to be more professional.
Replaces terms like "dependents" with "Consumers" and related variations.
"""

import os
import re
from pathlib import Path

# Define replacement patterns
# Order matters - more specific patterns first
REPLACEMENTS = [
    # Specific phrases first
    (r'First-Level Dependencies', 'Primary Consumers'),
    (r'All Deeper Dependencies', 'Secondary Consumers'),
    (r'Dependent Libraries \(Latest Version:', 'Consumer Libraries (Latest Version:'),
    (r'Dependent Libraries', 'Consumer Libraries'),
    (r'No dependent libraries found', 'No consumer libraries found'),
    (r'with dependents', 'with consumers'),
    (r'for the latest version with dependents', 'for the latest version with consumers'),
    
    # Chart labels and titles
    (r'Dependency Count', 'Consumer Count'),
    
    # General word replacements (case-sensitive)
    (r'\bdependents\b', 'Consumers'),  # whole word only
    (r'\bdependent\b', 'Consumer'),    # whole word only
    
    # Note: We keep "dependencies" as is when it refers to actual dependencies,
    # but we've already replaced "Dependent Libraries" above
]

def process_file(file_path):
    """Process a single HTML file with all replacements."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all replacements
        for pattern, replacement in REPLACEMENTS:
            content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all HTML files."""
    # Get the script directory (project root)
    script_dir = Path(__file__).parent.absolute()
    
    # Find all HTML files
    html_files = []
    
    # Root directory HTML files
    for html_file in script_dir.glob('*.html'):
        html_files.append(html_file)
    
    # HTML files in v1.90 directory
    v190_dir = script_dir / 'v1.90'
    if v190_dir.exists():
        for html_file in v190_dir.glob('*.html'):
            html_files.append(html_file)
        
        # HTML files in v1.90/libraries directory
        libraries_dir = v190_dir / 'libraries'
        if libraries_dir.exists():
            for html_file in libraries_dir.glob('*.html'):
                html_files.append(html_file)
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    processed_count = 0
    for html_file in html_files:
        if process_file(html_file):
            processed_count += 1
            print(f"Updated: {html_file.relative_to(script_dir)}")
    
    print(f"\nProcessing complete!")
    print(f"Total files processed: {len(html_files)}")
    print(f"Files updated: {processed_count}")

if __name__ == '__main__':
    main()
