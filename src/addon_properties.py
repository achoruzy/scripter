# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import os
from pathlib import Path

import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       CollectionProperty
                       )


# DEF_LIB_DIR = os.path.expanduser("~") + "/.scripter/lib",
# DEF_LIB_DIR = str((Path(os.path.expanduser("~"))/".scripter/lib").resolve()),


data_for_enum = []
    
    
def enum_items_generator(self,context):
	enum_items = []
	for a,b in enumerate(data_for_enum):
		enum_items.append((b[0], b[0], 'Descrb' + str(b[1]), a))
	return enum_items


class ScripterProperties(bpy.types.PropertyGroup):
    
    pip_libs_dir: StringProperty(
        name = "PIP library directory",
        description = "Directory to store installed python libraries.",
        default = str(Path(os.path.expanduser("~"))),
        maxlen = 1024,
        subtype = "DIR_PATH"
        )
    
    pip_libs_names: EnumProperty(
        items = enum_items_generator, 
        name = "PYPI names",
        description = "Library to install and use names matching with PYPI."
        )