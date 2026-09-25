import pandas as pd
import numpy as np
import io
from pathlib import Path
import subprocess
import sys

csv_text = """ticket_id,channel,resolution_minutes
001,phone,30
002,chat,
003,email,NA
004,phone,0
005,email,unknown"""

SCRIPTS = [
    "01_create_csv.py",
    "02_read_csv.py",
    "03_create_database.py",
    "04_select_data.py",
    #"04_select_data_solutions.py",
    "05_modify_data.py",
]
SCRIPT_DIR="/home/adam/dev/projets/exercice1-python/projetspython/lab_2026_09_25/sql"
def read_csv():
    df = pd.read_csv(
        io.StringIO(csv_text)
        ,dtype={
                "ticket_id": "string",
                "channel": "string",
            }
    )
    print(df.describe())

def start_scripts(scriptname=False):
    if scriptname:
        print(f"\nExécution : {scriptname}", flush=True)
        subprocess.run(
            [sys.executable, f"{SCRIPT_DIR}/{scriptname}"],
            cwd=SCRIPT_DIR,
            check=True,
        )
        return True

    for filename in SCRIPTS:
        print(f"\nExécution : {filename}\n-----------\n", flush=True)

        subprocess.run(
            [sys.executable, f"{SCRIPT_DIR}/{filename}"],
            cwd=SCRIPT_DIR,
            check=True,
        )

def main():
    # read_csv()
    start_scripts()
