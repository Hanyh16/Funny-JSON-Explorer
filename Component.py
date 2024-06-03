from abc import ABC, abstractmethod

# 组件类，定义了添加子节点的方法
class Component(ABC):
    def add(self, child):
        pass


# 叶子节点类
class Leaf(Component):
    def __init__(self, name, value, level, icon):
        self.name = name
        self.value = value
        self.level = level
        self.icon = icon

    @abstractmethod
    def draw(self, is_first, is_last, is_last_levels, line_length):
        pass

# 树形风格叶子节点类
class TreeStyleLeaf(Leaf):
    def draw(self, is_first, is_last, is_last_levels, line_length):
        # 构建前缀
        prefix = "".join("    " if is_last_levels[i] else "│   " for i in range(self.level - 1))
        prefix += "└─" if is_last else "├─"
        
        # 打印节点信息
        if self.value is not None:
            print(f"{prefix}{self.icon} {self.name}: {self.value}")
        else:
            print(f"{prefix}{self.icon} {self.name}")

# 矩形风格叶子节点类
class RectangleStyleLeaf(Leaf):
    def draw(self, is_first, is_last, is_last_levels, line_length):
        # 构建前缀
        prefix = "".join("│   " for _ in range(self.level - 1))
        flag = all(is_last_levels[:self.level - 1])
        
        if flag and is_last:
            prefix = '└───' + '───' * (self.level - 2)
            prefix += "┴─"
        else:
            prefix += "├─"
        
        subfix = '─┘' if flag and is_last else '─┤'
        
        # 计算填充长度
        if self.value is not None:
            content_length = len(self.icon) + len(self.name) + len(self.value) + 2
        else:
            content_length = len(self.icon) + len(self.name)
        
        padding = line_length - len(prefix) - content_length
        
        # 打印节点信息
        if self.value is not None:
            print(f"{prefix}{self.icon} {self.name}: {self.value} " + '─' * padding + subfix)
        else:
            print(f"{prefix}{self.icon} {self.name} " + '─' * padding + subfix)

# 中间节点类
class Container(Component):
    def __init__(self, name, level, icon):
        self.name = name
        self.level = level
        self.icon = icon
        self.children = []

    def add(self, child):
        self.children.append(child)

    @abstractmethod
    def draw(self, is_first, is_last, is_last_levels, line_length):
        pass

# 树形风格中间节点类
class TreeStyleContainer(Container):
    def draw(self, is_first, is_last, is_last_levels, line_length):
        # 构建前缀
        prefix = "".join("    " if is_last_levels[i] else "│   " for i in range(self.level - 1))
        prefix += "└─" if is_last else "├─"
        
        # 打印节点信息
        print(f"{prefix}{self.icon} {self.name}")
        
        # 更新 is_last_levels 列表
        is_last_levels.append(is_last)
        
        # 遍历子节点并绘制
        for i, child in enumerate(self.children):
            child.draw(i == 0, i == len(self.children) - 1, is_last_levels, line_length)
        
        # 恢复 is_last_levels 列表
        is_last_levels.pop()

# 矩形风格中间节点类
class RectangleStyleContainer(Container):
    def draw(self, is_first, is_last, is_last_levels, line_length):
        # 构建前缀
        prefix = "│   " * (self.level - 1)
        
        # 根据层次和是否为第一个节点确定前缀和后缀
        if self.level == 1 and is_first:
            prefix += "┌─"
            subfix = '─┐'
        else:
            prefix += "├─"
            subfix = '─┤'
        
        # 计算填充长度
        padding = line_length - len(prefix) - len(self.icon) - len(self.name)
        
        # 打印节点信息
        print(f"{prefix}{self.icon} {self.name} " + '─' * padding + subfix)
        
        # 更新 is_last_levels 列表
        is_last_levels.append(is_last)
        
        # 遍历子节点并绘制
        for i, child in enumerate(self.children):
            child.draw(i == 0, i == len(self.children) - 1, is_last_levels, line_length)
        
        # 恢复 is_last_levels 列表
        is_last_levels.pop()
