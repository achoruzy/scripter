# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import os
from pathlib import Path

import bpy
from bpy.props import (StringProperty, EnumProperty)

from .scripter import Pypi_Handler
  
    
def pypi_generator(self, context):
	current_view = []
	for i, title in enumerate(Pypi_Handler._packages):
		current_view.append((title, title, f"PYPI library: {title}", i))
	return current_view


class SCRIPTER_PR_properties(bpy.types.PropertyGroup):
    bl_idname = "SCRIPTER_PR_properties"
    
    pip_libs_dir: StringProperty(
        name = "Library installation directory",
        description = "Directory to store installed python libraries.",
        default = str(Path(os.path.expanduser("~")+"\.scripter\lib")),
        maxlen = 1024,
        subtype = "DIR_PATH"
        )
    
    pip_libs_names: EnumProperty(
        items = pypi_generator, 
        name = "PYPI libraries",
        description = "Libraries to install and use names matching with PYPI."
        )