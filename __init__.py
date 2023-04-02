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

from .src.addon_preferences import ScripterPreferences
from .src.addon_properties import ScripterProperties
from .src.scripter import python_dependencies


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

print(__package__)

classes = [
    ScripterPreferences.override_idname(__package__),
    ]


def register():
    bpy.types.Scene.scripter = bpy.props.PointerProperty(type=ScripterProperties)
    
    # python_dependencies()
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    

if __name__ == "__main__":
    register()