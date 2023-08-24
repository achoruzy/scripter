# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import pip
import sys
import os
from pathlib import Path
    

def python_dependencies():   
    packages = ['pandas']
    
    path = Path(os.path.expanduser("~")+"\.scripter\lib")
    path.mkdir(parents=True, exist_ok=True)
    deps_path = str(path)
    
    for pack in packages:
        if not pack in os.listdir(deps_path):
            pip.main(["install", f"--target={deps_path}", pack])
    sys.path.append(deps_path)