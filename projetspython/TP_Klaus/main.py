from pathlib import Path
import subprocess
import sys

SCRIPT_DIR = str(Path(__file__).resolve().parent)+"/scripts"
SCRIPTS = [
    "01_analyse.py"
]

def executer_script(filename=False):
    print(f"\nEXECUTION DE [ {filename} ]\n"+("="*30))
    subprocess.run(
        [sys.executable, f"{SCRIPT_DIR}/{filename}"],
        cwd=SCRIPT_DIR,
        check=True,
    )

def main():
    print(SCRIPT_DIR)
    executer_script(SCRIPTS[0])
