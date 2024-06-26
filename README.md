# Java 自动打包机

> 适用于 BUAA OO 课程互测模块！
> 当前版本似乎并不稳定哦

## 功能概述

- 从**压缩包**开始编译并打包为**可执行 Jar 包**
- 支持导入**依赖的 Jar 包**（目前版本仅支持单包依赖）
- 用一些很蠢但很好用的方法**探测主类**
- 支持**图形化界面**与**控制台界面**，满足各类需求


## 依赖与使用

使用 Python (>= 3.10) 运行 `Main.py` 即可。

- 当环境中存在 `PyQt6` 库时，会自动选择*图形化版本*。
- 否则，会启动*控制台版本*，无需安装任何第三方依赖。


## 使用细节

### 通用

在 `Main.py` 中，可以修改 `names` 列表，以指定显示的名称与生成的文件名。


### 图形化版本

- 生成目录、依赖包、`javac` 与 `jar` 路径指定、压缩包均可从文件或文件夹**直接拖拽**，简单易用。
- 当压缩包键入后，没有显示主类，代表程序用的那个很蠢的算法找不到主类，或者找到多个可能的主类，可以手动填写，并点击 “生成”。


### 控制台版本

- 在输入依赖包、压缩包路径时，**直接回车**可以略过。
- 控制台版本不支持在运行时修改 `javac` 与 `jar` 路径，但可在 `AutoPackCore/tui_main.py` 的第 11-12 行修改。

## 已知 Bug

- `javac` 编译信息编码异常

