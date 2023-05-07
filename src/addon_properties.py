# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import os

import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )


class ScripterProperties(bpy.types.PropertyGroup):
    
    pip_lib_dir: StringProperty(
        name="PIP library directory",
        description="Directory to store installed python libraries.",
        default=os.path.expanduser("~") + "/.scripter/lib",
        maxlen=1024,
        subtype="DIR_PATH"
        )