# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy


class SomeAddonPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__
    # here you define the addons customizable props
    # some_prop = bpy.props.FloatProperty(default=1.0)

    # here you specify how they are drawn
    def draw(self, context):
        addon_properties = context.window.scripter # tym łapie propertisy ze swojego properties group
        layout = self.layout
        row = layout.row
        row.prop(addon_properties, "some_prop")