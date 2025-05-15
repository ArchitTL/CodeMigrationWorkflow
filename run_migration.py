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

# REMOVE these sys.path.append lines - they don't work in Databricks Workspace
# sys.path.append("/Workspace/Users/archit.murgudkar@tlconsulting.com.au/CodeMigrationWorkflow_Project/variables/variables.py") 
# sys.path.append("/Workspace/Users/archit.murgudkar@tlconsulting.com.au/CodeMigrationWorkflow_Project/sourceCode/uc_mapping_config.py") 
# sys.path.append("/Workspace/Users/archit.murgudkar@tlconsulting.com.au/CodeMigrationWorkflow_Project/sourceCode/code_migration_framework.py") 
# sys.path.append("/Workspace/Users/archit.murgudkar@tlconsulting.com.au/CodeMigrationWorkflow_Project/utility/log_code_flow_config.py") 


import sys
sys.path.append("/dbfs/FileStore/tables/Archit")

from variables.variables import repo_root_path, log_migration_updates_file_path
from sourceCode.uc_mapping_config import uc_mapping
from sourceCode.code_migration_framework import CodeMigrationFramework
from utility.log_code_flow_config import setup_logger

logger = setup_logger()

# After running the notebooks, now you can use the imported objects
#logger = setup_logger()
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

import sys
sys.path.insert(0, "/dbfs/FileStore/tables/Archit")

import sourceCode.uc_mapping_config
print(sourceCode.uc_mapping_config.__file__)



# COMMAND ----------

# MAGIC %fs ls '/FileStore/tables/Archit/variables/'

# COMMAND ----------

