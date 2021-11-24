# Databricks notebook source
# MAGIC %run ./app/bootstrap

# COMMAND ----------

# MAGIC %reload_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

from daipeproject.test_module import hello

hello()
