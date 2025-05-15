# Databricks notebook source
# sourceCode/code_migration_framework.py
import os, re, json
from datetime import datetime
from variables.variables import *
from utility.log_code_flow_config import setup_logger
logger = setup_logger()

"""
@Class Name : CodeMigrationFramework
@Parameters:    
    notebook_dir - 
    mapping - 
    log_migration_updates_file_path - 
    patterns-

@Author : Archit
@Date : 06-05-2025
@Updated date - 15-05-2025
@Version : 0.4

@Purpose: This class is responsible for migration of Hive to Databricks  Unity Catalog compatible code transformation. 
          It supports scanning and replacing references such as Hive Metastore table names, ADLS Gen2 paths, WASBS, and DBFS mount points scanning all the folders and files in the directory and updating the references. 
          All the new updates are logged in a JSONL log file.
"""

class CodeMigrationFramework:
    def __init__(self, notebook_dir: str, mapping: dict, log_migration_updates_file_path: str):
        self.notebook_dir = notebook_dir
        self.uc_mapping = mapping

        """ Define regex patterns to detect various legacy reference types in code.
        Each pattern is mapped by type for easy processing during scanning.
        These patterns match:
        - hive_metastore.<db>.<table>
        - abfss://... (Azure Data Lake Gen2)
        - wasbs://... (WASB Blob Storage)
        - /dbfs/... (Databricks File System paths)
        """
        self.patterns = patterns
        self.log_migration_updates_file_path = log_migration_updates_file_path
        os.makedirs(os.path.dirname(self.log_migration_updates_file_path), exist_ok=True)

    """
    @Method: scan_codebase
    @Purpose: Recursively scans all supported code files in the notebook_dir and sends their content for reference identification.
    """
    def scan_codebase(self):
        for root, _, files in os.walk(self.notebook_dir):
            for file in files:
                if file.endswith(inclusive_file_extensions):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        code = f.read()
                    self.identify_references(path, code)

    """
    @Method: identify_references
    @Purpose: Applies regex patterns to the given file content to detect Hive, ADLS, WASBS, and DBFS references. Logs each detected reference for tracking.
    """
    def identify_references(self, notebook_name, code):
        def detect_and_log(ref_type, match_text):
            old_ref = match_text.strip()
            new_ref = self.uc_mapping.get(old_ref)
            if new_ref:
                logger.info(f"[{ref_type}] {old_ref} -> {new_ref}")
            else:
                logger.warning(f" No mapping found for [{ref_type}]: {old_ref}")
            self.log_findings(notebook_name, ref_type, old_ref, new_ref)

        for ref_type, pattern in self.patterns.items():
            for match in re.finditer(pattern, code):
                detect_and_log(ref_type, match.group(0))

        sql_magic_blocks = re.findall(r"# MAGIC\s*%sql\s+(.*?)(?=\n# MAGIC|\Z)", code, re.DOTALL)
        for sql_block in sql_magic_blocks:
            for ref_type, pattern in self.patterns.items():
                for match in re.finditer(pattern, sql_block):
                    detect_and_log(ref_type, match.group(0))

    """
    @Method: log_findings
    @Purpose: Logs each matched reference (and its mapped replacement, if available) to a JSONL log file with timestamp and context.
    """ 
    def log_findings(self, notebook, ref_type, old_value, new_value):
        entry = {
            "notebook": notebook,
            "ref_type": ref_type,
            "old_value": old_value,
            "new_value": new_value,
            "detected_at": datetime.now().isoformat()
        }
        with open(self.log_migration_updates_file_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    """
    @Method: replace_references
    @Purpose: Performs 'find-and-replace' operations across all matching files using the UC mapping dictionary. Writes updated files back in-place.
    """
    def replace_references(self):
        for root, _, files in os.walk(self.notebook_dir):
            for file in files:
                if file.endswith(inclusive_file_extensions):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        code = f.read()

                    matches_found = False
                    original_code = code
                    for old, new in self.uc_mapping.items():
                        if old in code:
                            print(f"MATCH in {path}: {old} -> {new}")
                            matches_found = True
                            code = code.replace(old, new)

                    if not matches_found:
                        print(f" No matches found in file: {path}")

                    if code != original_code:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(code)
                        print(f" File written: {path}")


