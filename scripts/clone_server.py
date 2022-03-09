import os
import subprocess
import sys

folder_name = sys.argv[1]

if not os.path.exists(folder_name):
    repository = input("Insert the server repository: ")
    KEY = input("Insert the auth key: ")
    ## TODO: Save the key to a file
    repository_and_key = "https://" + KEY + repository.split("://")[1]
    subprocess.run(f"git clone {repository_and_key} {folder_name}", shell=True)
    print(f"Cloned {folder_name}")
