# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk



def python_dependencies():
    import pip
    import sys
    import os
    from pathlib import Path
    
    packages = ['pandas']
    deps_path = str(Path(os.path.expanduser("~")+"\.scripter\lib"))
    # check_folder_and_create(deps_path)
    for pack in packages:
        if not pack in os.listdir(deps_path):
            pip.main(["install", f"--target={deps_path}", pack])
    sys.path.append(deps_path)