# Funny-JSON-Explorer
Funny JSON Explorer(FJE),是一个JSON文件可视化的命令行界面小工具 

## 类图
![UML](UML.png)

## 设计模式

1. **工厂方法**（Factory）：定义一种创建对象的接口，但将具体实例化对象的工作推迟到子类中完成。在本项目中我使用工厂方法模式的具体方法在于AbstractFactory类及其子类TreeStyleFactory和RectangleStyleFactory。首先在抽象工厂类AbstractFactory中定义了两个用于创建对象的抽象函数create_container()和create_leaf()，然后在树形风格工厂类TreeStyleFactory实现了create_container()函数和create_leaf()函数分别用于创建树形风格的中间节点和树形风格的叶子节点；在矩形风格工厂类RectangleStyleFactory中实现了create_container()函数和create_leaf()函数分别用于创建矩形风格的中间节点和矩形风格的叶子节点。这样的话Director类使用工厂来创建对象时并不直接依赖于具体的类名，而且当需要更改具体的实现时，只需替换工厂的子类，而无需修改Director类的代码。


2. 
