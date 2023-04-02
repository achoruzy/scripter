# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy


class ScripterProperties(bpy.types.PropertyGroup):
    
    some_prop: bpy.props.FloatProperty(
        name='some_prop',        
        default=0.0
    )