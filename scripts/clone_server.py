import os
import subprocess

dir="menzalib/"

if not os.path.exists(dir):
    subprocess.run("git clone https://github.com/LetteraUnica/menzalib.git", shell=True)
    print(f"Cloned {dir}")

os.chdir(dir)
