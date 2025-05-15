# Databricks notebook source
# utility/log_code_flow_config.py
import logging
import os
from variables.variables import log_code_flow_file_name

def setup_logger():
    log_path = f"/dbfs/FileStore/tables/Archit/logs/{log_code_flow_file_name}"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()
