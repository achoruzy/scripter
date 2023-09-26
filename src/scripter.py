# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


from pathlib import Path
import os, sys, pip


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

            if package not in self._packages_snap:
                self.uninstall_package(package)
                
        self.make_snap()
    
    def update_path(self, new_path: str):
        if self.path:
            sys.path.remove(self.path)
        self._path = Path(new_path)
        sys.path.append(new_path)
        self.handle_dirs()
        
    def add(self, value: str):
        self._packages.add(value)
        
    def remove(self, value: str):
        self._packages.remove(value)
        
    def load(self):
        # here to deserialize from .scripter file
        self.update_path(default_path)
    
    def save(self):
        # here to serialize to .scripter file
        pass
    
    def install_package(self, package: str):
        pip.main(["install", f"--target={self.path}", package])
    
    def uninstall_package(self, package: str):
        pip.main(["uninstall", f"--target={self.path}", package])
    
    def handle_dirs(self):
        self._path.mkdir(parents=True, exist_ok=True)
        
    def make_snap(self):
        self._packages_snap = self._packages.copy()
        