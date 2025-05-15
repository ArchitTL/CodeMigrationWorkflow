# Databricks notebook source
with open("/dbfs/FileStore/tables/Archit/logs/code_debug.log", "r") as f:
    for line in f:
        print(line.strip())


# COMMAND ----------

from variables.variables import *
import os
print("Scanning path:", repo_root_path)
for root, dirs, files in os.walk(repo_root_path):
    for file in files:
        print("FOUND FILE:", os.path.join(root, file))

# COMMAND ----------

# MAGIC %fs ls /FileStore/tables/Archit/logs

# COMMAND ----------

with open(self.log_path, 'a') as f:
    f.write(json.dumps(entry) + '\n')

# COMMAND ----------

# MAGIC %fs ls /FileStore/tables/Archit/gb_exported_notebooks

# COMMAND ----------

import os

for root, dirs, files in os.walk("/dbfs/FileStore/"):
    for file in files:
        print("Found file:", os.path.join(root, file))


# COMMAND ----------

with open("/dbfs/FileStore/tables/Archit/logs/code_debug.log", "r") as f:
    print(f.read())


# COMMAND ----------

