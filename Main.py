try:
    from GuiCore import GuiMain as Main
except ModuleNotFoundError:
    from TuiCore import TuiMain as Main

names = [
    ('TianShu', "天枢星"),
    ('TianXuan', "天璇星"),
    ('TianJi', "天玑星"),
    ('TianQuan', "天权星"),
    ('YuHeng', "玉衡星"),
    ('KaiYang', "开阳星"),
    ('YaoGuang', "摇光星"),
    ('DongMing', "洞明星")
]

if __name__ == '__main__':
    Main(names)
