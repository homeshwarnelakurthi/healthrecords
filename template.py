import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project folder structure
project_name = "health_records"

list_of_files = [
    f"{project_name}/templates/login.html",
    f"{project_name}/templates/dashboard.html",
    f"{project_name}/templates/view_records.html",
    f"{project_name}/templates/update_record.html",
    f"{project_name}/templates/index.html",
    f"{project_name}/static/style.css",
    f"{project_name}/main.py",
    f"{project_name}/access_control.py",
    f"{project_name}/authentication.py",
    f"{project_name}/confidentiality.py",
    f"{project_name}/db_setup.py",
    f"{project_name}/integrity.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/setup.py",
    f"{project_name}/.dockerignore"
    
]

# Create directories and empty files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it does not exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Create an empty file if it does not exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
