#!/usr/bin/env python3
"""
Generate rules.json catalog from rule files in the repository.
This script scans the rules directory and creates a searchable catalog.
"""

import json
import os
import glob
from pathlib import Path


def extract_rule_metadata(file_path):
    """Extract metadata from a rule file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Try to parse as JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = {"title": Path(file_path).stem}
        
        # Determine severity from directory structure
        path_parts = file_path.split(os.sep)
        severity = "info"
        rule_type = "detection"
        
        if "detection" in path_parts:
            rule_type = "detection"
            if "high" in path_parts:
                severity = "high"
            elif "medium" in path_parts:
                severity = "medium"
            elif "low" in path_parts:
                severity = "low"
            else:
                severity = "info"
        elif "filtering" in path_parts:
            rule_type = "filtering"
            severity = "info"
        
        return {
            "name": data.get("title") or data.get("name") or Path(file_path).stem,
            "type": rule_type,
            "severity": severity,
            "description": data.get("description") or "",
            "version": data.get("version") or "1.0",
            "path": file_path.replace(os.sep, "/")
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_rules_catalog():
    """Scan rules directory and generate catalog."""
    rules = []
    
    # Find all rule files
    detection_files = glob.glob("rules/detection/**/*.json", recursive=True)
    filtering_files = glob.glob("rules/filtering/**/*.json", recursive=True)
    
    all_files = detection_files + filtering_files
    
    for file_path in sorted(all_files):
        metadata = extract_rule_metadata(file_path)
        if metadata:
            rules.append(metadata)
    
    return rules


def main():
    """Main entry point."""
    rules = generate_rules_catalog()
    
    # Ensure docs directory exists
    os.makedirs("docs", exist_ok=True)
    
    # Write catalog
    with open("docs/rules.json", "w") as f:
        json.dump(rules, f, indent=2)
    
    print(f"Generated catalog with {len(rules)} rules")
    print("Catalog saved to docs/rules.json")


if __name__ == "__main__":
    main()
