# <one line to give the program's name and a brief idea of what it does.>
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

bl_info = {
    "name": "Scripter",
    "description": "Tools and utils for scripting blender easier.",
    "author": "Data Verft Arkadiusz Choruzy",
    "version": (2023, 0, 1),
    "blender": (2, 9, 0),
    "location": "Scripting",
    "doc_url": "https://github.com/industArk/bl_scripter/blob/main/README.md",
    "category": "Text Editor",
}


class SomeAddonPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__
    # here you define the addons customizable props
    some_prop = bpy.props.FloatProperty(default=1.0)

    # here you specify how they are drawn
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "some_prop")


def python_dependencies():
    import pip
    import sys
    import os
    
    packages = []
    deps_path = os.path.expanduser("~") + "/.scripter/lib"
    check_folder_and_create(deps_path)
    for pack in packages:
        if not pack in os.listdir(deps_path):
            pip.main(["install", f"--target={deps_path}", pack])
    sys.path.append(deps_path)


classes = [SomeAddonPrefs,]

def register():
    python_dependencies()
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    ...
    

if __name__ == "__main__":
    register()