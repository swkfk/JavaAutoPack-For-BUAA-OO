__javac = 'javac'
__jar = 'jar'

def get_javac():
    return __javac

def get_jar():
    return __jar

def set_javac(javac: str):
    global __javac
    __javac = javac

def set_jar(jar: str):
    global __jar
    __jar = jar
