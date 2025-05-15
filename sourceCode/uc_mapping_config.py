# Databricks notebook source
# sourceCode/uc_mapping_config.py

"""
@Module : uc_mapping_config.py
@Author : Archit
@Date : 06-05-2025
@Updated : 14-05-2025
@Version : 0.2

@Purpose:
This module reads a JSON configuration file that defines mappings from Hive Metastore tables
and storage paths (ADLS/DBFS) to Unity Catalog-compliant destinations. It uses the mapping list
to construct a dictionary (`uc_mapping`) which can be used by the CodeMigrationFramework to update references in code files.
"""

from variables.variables import table_csv_path, old_new_ref_csv_path
from configs.configs_loader import build_uc_mapping_from_csvs

uc_mapping = build_uc_mapping_from_csvs(table_csv_path, old_new_ref_csv_path)
