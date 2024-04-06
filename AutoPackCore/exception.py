class CompileErrorException(Exception):
    def __init__(self, return_code: int, stderr: str | bytes):
        if type(stderr) == str:
            self.stderr = stderr
        else:
            self.stderr = stderr.decode('utf-8', errors='replace')
        self.return_code = return_code

    def __str__(self):
        return f"编译或打包错误，返回值：{self.return_code}\n{self.stderr}"


class MainClassNotFoundException(Exception):
    def __str__(self):
        return "检测不到任何一个主类！"


class MainClassDuplicatedException(Exception):
    def __str__(self):
        return "检测到多个潜在的主类！"
