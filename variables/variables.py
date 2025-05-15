# Databricks notebook source
# variables/variables.py

# Paths inside Databricks Repos (already checked out manually via Git UI)
repo_root_path = "/dbfs/FileStore/tables/Archit/gb_exported_notebooks"

# Paths to config CSVs (upload them via UI to /FileStore/tables/)
table_csv_path = "/dbfs/FileStore/tables/table_mappings.csv"
old_new_ref_csv_path = "/dbfs/FileStore/tables/old__new_references.csv"

# Log file path
log_migration_updates_file_path = "/dbfs/FileStore/tables/Archit/logs/migration_log.jsonl"
log_code_flow_file_name = "code_debug.log"
#log_path = "/dbfs/FileStore/tables/Archit/logs/migration.jsonl"


# File extensions
inclusive_file_extensions = (".sql", ".py", ".ipynb", ".txt")
patterns = {
    "hive_metastore": r"hive_metastore\.\w+(?:\.\w+)?",
    "adls_storage": r"abfss://[^\s\"']+",
    "wasbs_storage": r"wasbs://[^\s\"']+",
    "dbfs_storage": r"/dbfs/[^\s\"']+"
}

# Column headers
col_hive_db = "src_schema"
col_hive_table = "src_table"
col_uc_catalog = "catalog_name"
col_uc_db = "dst_schema"
col_uc_table = "dst_table"
col_old_path = "old"
col_new_path = "new"
