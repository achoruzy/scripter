# Scripter
# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
    

import bpy

from .src.addon_preferences import SCRIPTER_AP_addon_preferences
from .src.properties import SCRIPTER_PR_properties
from .src.properties_ops import (SCRIPTER_OT_pypi_list_add, SCRIPTER_OT_pypi_list_remove,
                                 SCRIPTER_OT_pypi_list_update)
from .src.scripter import Pypi_Handler


bl_info = {
    "name": "bl_scripter",
    "description": "Tools and utils for scripting blender easier.",
    "author": "Data Verft Arkadiusz Choruzy",
    "version": (2023, 0, 1),
    "blender": (3, 0, 0),
    "location": "Scripting",
    "doc_url": "https://github.com/industArk/bl_scripter/blob/main/README.md",
    "category": "All",
}

pypi = Pypi_Handler()

classes = [
    SCRIPTER_AP_addon_preferences.override_idname(__package__),
    SCRIPTER_PR_properties,
    ]

scripter_classes = [
    SCRIPTER_OT_pypi_list_add,
    SCRIPTER_OT_pypi_list_remove,
    SCRIPTER_OT_pypi_list_update
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    for cls in scripter_classes:
        bpy.utils.register_class(cls.initialize_with(pypi))
    
    bpy.types.Scene.scripter = bpy.props.PointerProperty(type=SCRIPTER_PR_properties)
    
def unregister():
    for cls in scripter_classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.scripter
    

if __name__ == "__main__":
    register()