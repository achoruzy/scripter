# Copyright (C) 2023  Data Verft Arkadiusz Choruzy aka inDustArk


import bpy

from .scripter import Pypi_Handler


name_text = 'New library name'

class SCRIPTER_OT_pypi_list_add(bpy.types.Operator):
	bl_idname = "scripter.pypi_add"
	bl_label = "SCRIPTER_OT_pypi_list_add"
	bl_description = "Add new PYPI library name to list."

	lib_name: bpy.props.StringProperty(default= "", name = name_text)

	pypi: Pypi_Handler = None

	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self, width=200)

	def execute(self, context):
		if self.lib_name != name_text and self.lib_name != "":
			self.pypi.add(self.lib_name)
		
		return{'FINISHED'}
	
	@classmethod
	def initialize_with(cls, pypi_handler):
		cls.pypi = pypi_handler
		return cls


class SCRIPTER_OT_pypi_list_remove(bpy.types.Operator):
	bl_idname = "scripter.pypi_remove"
	bl_label = "SCRIPTER_OT_pypi_list_remove"
	bl_description = "Remove PYPI library from list."

	pypi: Pypi_Handler = None

	def execute(self, context):
		chosen_lib = bpy.context.scene.scripter.pip_libs_names
		self.pypi.remove(chosen_lib)

		return{'FINISHED'}
	
	@classmethod
	def initialize_with(cls, pypi_handler):
		cls.pypi = pypi_handler
		return cls


class SCRIPTER_OT_pypi_list_update(bpy.types.Operator):
	bl_idname = "scripter.pypi_update"
	bl_label = "SCRIPTER_OT_pypi_list_update"
	bl_description = "Update installed libraries with current list"

	pypi: Pypi_Handler = None

	def execute(self, context):
		self.pypi.update_packages()

		return{'FINISHED'}
	
	@classmethod
	def initialize_with(cls, pypi_handler):
		cls.pypi = pypi_handler
		return cls