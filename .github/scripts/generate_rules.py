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
        
        # Parse JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print(f"Invalid JSON in {file_path}")
            return None
        
        # Handle both single object and array of objects
        rules_list = data if isinstance(data, list) else [data]
        
        # Determine severity and rule_type from directory structure
        path_parts = file_path.split(os.sep)
        rule_type = "detection"
        
        if "detection" in path_parts:
            rule_type = "detection"
        elif "filtering" in path_parts:
            rule_type = "filtering"
        
        # Extract metadata from each rule in the file
        extracted_rules = []
        for idx, rule in enumerate(rules_list):
            if not isinstance(rule, dict):
                continue
            
            # Get severity from rule or directory
            severity = rule.get("severity", "info")
            
            # For filtering rules, default to info if not specified
            if rule_type == "filtering" and severity not in ["high", "medium", "low", "info"]:
                severity = "info"
            
            metadata = {
                "name": rule.get("title") or rule.get("name") or Path(file_path).stem,
                "type": rule_type,
                "severity": severity,
                "description": rule.get("description") or rule.get("expression", "")[:100],
                "version": rule.get("version") or "1.0",
                "path": file_path.replace(os.sep, "/"),
                "reference": rule.get("reference") or ""
            }
            extracted_rules.append(metadata)
        
        return extracted_rules
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_rules_catalog():
    """Scan rules directory and generate catalog."""
    rules = []
    
    # Find all rule files
    detection_files = glob.glob("rules/detection/**/*.json", recursive=True)
    filtering_files = glob.glob("rules/filtering/**/*.json", recursive=True)
    
    all_files = sorted(detection_files + filtering_files)
    
    for file_path in all_files:
        extracted = extract_rule_metadata(file_path)
        if extracted:
            rules.extend(extracted)
    
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
