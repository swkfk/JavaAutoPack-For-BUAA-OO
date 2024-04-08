from PyQt6.QtCore import QSettings

settings = QSettings("kai_Ker", "JavaAutoPacker")

def get_default_javac():
    value = settings.value("javac", "javac")
    settings.sync()
    return value

def get_default_jar():
    value = settings.value("jar", "jar")
    settings.sync()
    return value

def set_default_javac(value: str):
    settings.setValue("javac", value)
    settings.sync()

def set_default_jar(value: str):
    settings.setValue("jar", value)
    settings.sync()
