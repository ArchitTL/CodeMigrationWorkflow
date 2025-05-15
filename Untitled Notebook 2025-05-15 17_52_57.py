# Databricks notebook source


# COMMAND ----------

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
sys.path.append("/dbfs/FileStore/tables/Archit/sourceCode")


from variables.variables import repo_root_path, log_migration_updates_file_path
from uc_mapping_config import uc_mapping
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

# Add DBFS paths to Python's sys.path
import sys
sys.path.append("/dbfs/FileStore/tables/Archit")  # Main project directory

# No need for this second path if the structure is correct in the main directory
# sys.path.append("/dbfs/FileStore/tables/Archit/sourceCode")  

# Make sure your imports match the actual directory structure in DBFS
try:
    # Import specific variables from variables.py
    from variables.variables import repo_root_path, log_migration_updates_file_path
    
    # Import other modules - adjust paths based on your actual file structure
    from sourceCode.uc_mapping_config import uc_mapping
    from sourceCode.code_migration_framework import CodeMigrationFramework
    from utility.log_code_flow_config import setup_logger
    
    print("Imports successful!")
except ImportError as e:
    # Print detailed error message for debugging
    print(f"Import error: {e}")
    
    # List contents of directories to verify structure
    import os
    print("\nProject root directory contents:")
    try:
        print(os.listdir("/dbfs/FileStore/tables/Archit"))
    except Exception as e:
        print(f"Cannot list directory: {e}")
    
    # Try to list variables directory
    try:
        print("\nVariables directory contents:")
        print(os.listdir("/dbfs/FileStore/tables/Archit/variables"))
    except Exception as e:
        print(f"Cannot list variables directory: {e}")
    
    raise

# Initialize logger
logger = setup_logger()

# Initialize framework
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

# MAGIC %fs ls 'FileStore/tables/Archit/utility'

# COMMAND ----------

dbutils.fs.rm('/FileStore/tables/Archit/sourceCode/log_code_flow_config.py')

# COMMAND ----------

import sys

# Clear cached modules from memory
for mod in list(sys.modules):
    if mod.startswith("sourceCode") or mod.startswith("variables") or mod.startswith("utility"):
        del sys.modules[mod]
sys.path.append("/dbfs/FileStore/tables/Archit")
from sourceCode.uc_mapping_config import uc_mapping


# COMMAND ----------

import sys

# Clear cached modules from memory
for mod in list(sys.modules):
    if mod.startswith("sourceCode") or mod.startswith("variables") or mod.startswith("utility"):
        del sys.modules[mod]

# Set correct import root path from DBFS
sys.path.insert(0, "/dbfs/FileStore/tables/Archit")

# COMMAND ----------

