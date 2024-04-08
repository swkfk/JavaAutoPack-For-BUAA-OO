import os

from PyQt6.QtCore import QSettings

settings = QSettings("kai_Ker", "JavaAutoPacker")

def get_default_javac():
    value = settings.value("javac", "javac")
    return value

def get_default_jar():
    value = settings.value("jar", "jar")
    return value

def set_default_javac(value: str):
    settings.setValue("javac", value)
    settings.sync()

def set_default_jar(value: str):
    settings.setValue("jar", value)
    settings.sync()

def get_default_path():
    value = settings.value("gen-path", os.getcwd())
    return value

def set_default_path(value: str):
    settings.setValue("gen-path", value)
    settings.sync()
