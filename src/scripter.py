# Copyright (C) 2023 Arkadiusz Choruzy


from pathlib import Path
import os, sys, pip, json


settings_path = Path(__file__).parent.resolve()/".scripter"
default_path = Path(os.path.expanduser("~")+"\.scripter\lib")


class Pypi_Handler():
    _packages = set()
    _packages_snap = set()
    _path = None
    
    def __init__(self):
        self.load()
        self.make_snap()
        
    @property
    def path(self):
        return str(self._path) if self._path else None
    
    def update_packages(self):      
        for package in self._packages:
            if not package in os.listdir(self.path):
                self.install_package(package)

        for package in self._packages_snap:
            if package not in self._packages:
                self.uninstall_package(package)
                
        self.make_snap()
    
    def update_path(self, new_path: str):
        if self.path:
            sys.path.remove(self.path)
        self._path = Path(new_path)
        sys.path.append(new_path)
        self.handle_dirs()
        self.save()
            
    def add(self, value: str):
        self._packages.add(value)
        self.save()
        
    def remove(self, value: str):
        self._packages.remove(value)
        self.save()
        
    def load(self):
        settings = JSON_Parser.load_to_dict(settings_path)
        self.update_path(str(default_path))
        self._packages.update(set(settings['packages']))
    
    def save(self):
        content = {
            "lib_path": str(self._path),
            "packages": list(self._packages)
        }
        
        JSON_Parser.save_to_json(settings_path, content)
    
    def install_package(self, package: str):
        pip.main(["install", f"--target={self.path}", package])
    
    def uninstall_package(self, package: str):
        pip.main(["uninstall", f"--target={self.path}", package])
    
    def handle_dirs(self):
        self._path.mkdir(parents=True, exist_ok=True)
        
    def make_snap(self):
        self._packages_snap = self._packages.copy()


class JSON_Parser():
    
    @staticmethod
    def load_to_dict(path: str):
        with open(path) as f:
            loaded = json.load(f)
            return loaded
    
    @staticmethod
    def save_to_json(path: str, content: dict):
        with open(path, "w") as f:
            json.dump(content, fp = f, indent = 4)