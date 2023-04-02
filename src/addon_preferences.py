# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy


class ScripterPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    
    menus = [
        ("PYTHON", "Python", ""),
        ("CREDITS", "Credits", "")
        ]
    
    menus: bpy.props.EnumProperty(name="Menus", items=menus, default="PYTHON")

    def draw(self, context):       
        layout = self.layout
        column = layout.column(align=True)
        row = column.row()
        row.prop(self, "menus", expand=True)
        box = column.box()

        if self.menus == "PYTHON":
            self.draw_python_menu(box)

        elif self.menus == "CREDITS":
            self.draw_credits_menu(box)
    
    def draw_python_menu(box):
        box.label(text="Python Menu")
        
    def draw_credits_menu(box):
        box.label(text="Credits Menu")     
    
    @classmethod
    def override_idname(cls, name):
        cls.bl_idname = name
        return cls