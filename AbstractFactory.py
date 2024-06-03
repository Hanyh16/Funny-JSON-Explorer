from abc import ABC, abstractmethod
from Component import *

# 抽象工厂类，定义了创建容器和叶子的方法
class AbstractFactory(ABC):
    def __init__(self):
        self.container = None
        self.leaf = None
        self.root_container = None

    @abstractmethod
    def create_container(self):
        pass

    @abstractmethod
    def create_leaf(self):
        pass


# 树形风格工厂类
class TreeStyleFactory(AbstractFactory):
    def create_container(self):
        self.container = TreeStyleContainer
    
    def create_leaf(self):
        self.leaf = TreeStyleLeaf


# 矩形风格工厂类
class RectangleStyleFactory(AbstractFactory):
    def create_container(self):
        self.container = RectangleStyleContainer
    
    def create_leaf(self):
        self.leaf = RectangleStyleLeaf