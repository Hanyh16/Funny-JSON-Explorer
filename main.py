from IconFamily import *
from config import icon_family
from AbstractFactory import *
from Director import Director
import argparse
import json

if __name__ == '__main__':
    # 创建参数解析器
    parser = argparse.ArgumentParser(description = 'Funny JSON Explorer (FJE)')
    # 添加命令行参数
    parser.add_argument("-f", "--file", help = "JSON文件路径")
    parser.add_argument("-s", "--style", choices = ['tree', 'rectangle'], help = "风格")
    parser.add_argument("-i", "--icon", choices = ['poker', 'sun', 'star', 'king', 'snow'], help = "图标族")
    # 解析命令行参数
    args = parser.parse_args()

    json_data = None
    # 读取json文件
    with open(args.file, 'r') as f:
        json_data = json.load(f)

    builder = None
    # 根据选择的风格创建相应的工厂
    if args.style == 'tree':
        builder = TreeStyleFactory()
    elif args.style == "rectangle":
        builder = RectangleStyleFactory()

    # 获取所选图标系列的图标
    icons = IconFamily(icon_family).get_icons(args.icon)
    # 创建导演对象，并传入相应的工厂
    director = Director(builder)
    # 创建产品对象
    director.create()
    # 加载json数据到产品对象中
    director._load(json_data, icons)
    # 设置输出每行的最大长度
    line_length = 40
    # 产品信息可视化
    director.show(line_length)