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

from .src.addon_preferences import SomeAddonPrefs
from .src.addon_properties import ScripterProperties
from .src.scripter import python_dependencies

bl_info = {
    "name": "Scripter",
    "description": "Tools and utils for scripting blender easier.",
    "author": "Data Verft Arkadiusz Choruzy",
    "version": (2023, 0, 1),
    "blender": (2, 9, 0),
    "location": "Scripting",
    "doc_url": "https://github.com/industArk/bl_scripter/blob/main/README.md",
    "category": "System",
}


classes = [SomeAddonPrefs,]

def register():
    bpy.utils.register_class(ScripterProperties)    
    bpy.types.Window.scripter = bpy.props.PointerProperty(type=ScripterProperties)
    python_dependencies()
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    ...
    

if __name__ == "__main__":
    register()