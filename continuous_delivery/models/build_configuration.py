# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BuildConfiguration(Model):
    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'working_directory': {'key': 'workingDirectory', 'type': 'str'},
        'node_type': {'key': 'NodeJsTaskRunner', 'type': 'str'},
        'python_framework': {'key': 'pythonFramework', 'type': 'str'},
        'python_version': {'key': 'pythonExtensionId', 'type': 'str'},
        'django_settings_module': {'key': 'djangoSettingsModule', 'type': 'str'},
        'flask_project_name': {'key': 'flaskProjectName', 'type': 'str'}
    }

    def __init__(self, type=None, working_directory=None, node_type=None, python_framework=None, python_version=None, django_settings_module=None, flask_project_name=None):
        self.type = type
        self.working_directory = working_directory
        self.node_type = node_type
        self.python_framework = python_framework
        self.python_version = python_version
        self.django_settings_module = django_settings_module
        self.flask_project_name = flask_project_name
