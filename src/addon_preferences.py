# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy


class SCRIPTER_AP_addon_preferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    
    menus = [
        ("PYTHON", "Python", ""),
        ("CREDITS", "Credits", "")
        ]
    
    menus: bpy.props.EnumProperty(name="Menus", items=menus, default="PYTHON")

    def draw(self, context):
        scripter = context.scene.scripter
           
        layout = self.layout
        column = layout.column(align=True)
        row = column.row()
        row.prop(self, "menus", expand=True)
        box = column.box()

        if self.menus == "PYTHON":
            self.draw_python_menu(box, scripter)

        elif self.menus == "CREDITS":
            self.draw_credits_menu(box, scripter)
    
    def draw_python_menu(self, box, scripter):
        box.label(text="Python Library Installation Settings Menu")
        box.prop(scripter, "pip_libs_dir")
        
        row = box.row(align=True)
        row.prop(scripter, "pip_libs_names")
        row.operator("scripter.pypi_add", text="", icon="ADD")
        row.operator("scripter.pypi_remove", text="", icon="REMOVE")
        
        
    def draw_credits_menu(self, box, scripter):
        box.label(text="Credits Menu")     
    
    @classmethod
    def override_idname(cls, name):
        cls.bl_idname = name
        return cls