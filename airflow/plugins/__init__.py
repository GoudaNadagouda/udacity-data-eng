from __future__ import division, absolute_import, print_function
from airflow.plugins_manager import AirflowPlugin

import helpers

# Defining the plugin class
class UdacityPlugin(AirflowPlugin):
    name = "plugin"
    helpers = [
        helpers.sql_statements
    ]
