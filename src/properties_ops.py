# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy

from .data import PYPI_libraries


default = 'New library name'

class SCRIPTER_OT_pypi_list_add(bpy.types.Operator):
	bl_idname = "scripter.pypi_add"
	bl_label = "SCRIPTER_OT_pypi_list_add"
	bl_description = "Add new PYPI library name for installation."

	new_lib: bpy.props.StringProperty(default= default, name = default)

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self, width=200)

	def execute(self, context):
		global PYPI_libraries
		if self.new_lib != default and self.new_lib != "":
			PYPI_libraries.add(self.new_lib)
		print(PYPI_libraries)

		return{'FINISHED'}


class SCRIPTER_OT_pypi_list_remove(bpy.types.Operator):
	bl_idname = "scripter.pypi_remove"
	bl_label = "SCRIPTER_OT_pypi_list_remove"
	bl_description = "Remove PYPI library and uninstall."

	def execute(self, context):
		global PYPI_libraries
		print(PYPI_libraries)
		PYPI_libraries.remove("pandas")
		print(PYPI_libraries)

		return{'FINISHED'}