# Databricks notebook source
# run_migration.py
"""
@Script : run_migration.py
@Author : Archit
@Date : 06-05-2025
@Updated : 14-05-2025
@Version : 0.4


@Purpose:
This script serves as the entry point for the migration framework. It loads the prebuilt mapping,
initializes the framework with configuration, and executes scanning and replacement logic.
"""

from variables.variables import *
from sourceCode.uc_mapping_config import uc_mapping
from sourceCode.code_migration_framework import CodeMigrationFramework
from utility.log_code_flow_config import setup_logger

logger = setup_logger()
framework = CodeMigrationFramework(
    notebook_dir=repo_root_path,
    mapping=uc_mapping,
    log_migration_updates_file_path=log_migration_updates_file_path
)

framework.scan_codebase()
framework.replace_references()
logger.info("Migration completed successfully.")
print("Migration completed successfully.")

print("Total mapping entries loaded:", len(uc_mapping))
print("Sample entries:")
for i, (k, v) in enumerate(uc_mapping.items()):
    if i >= 5: break
    print(f"  {k} -> {v}")


# COMMAND ----------

