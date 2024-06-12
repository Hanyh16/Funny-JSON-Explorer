# Funny-JSON-Explorer
Funny JSON Explorer(FJE)，是一个JSON文件可视化的命令行界面小工具。

```
python main.py -f <json file> -s <style> -i <icon family>
```

## 类图
![UML](UML.png)

## 设计模式

1. **工厂方法**（Factory）：在各风格工厂中的`create_container`方法和`create_leaf`方法是工厂模式的方法。

2. **抽象工厂**（Abstract Factory）：`AbstractFactory`是抽象工厂接口，`TreeStyleFactory`和`RectangleStyleFactory`是具体的抽象工厂，它们一起实现了抽象工厂。

3. **建造者模式**（Builder pattern）：`AbstractFactory`是Builder，Director指挥Builder进行生产。Director类的`create`方法用于创建中间节点和叶子节点，`_load`方法和`show`方法分别用于加载json文件和将其可视化，`create_container`和`create_leaf`是Builder的部分方法。

4. **组合模式**（Composite pattern)：`Component`抽象类为中间节点`Container`和叶子节点`Leaf`定义了统一的接口。`Container`类表示具有子节点的中间节点，`Leaf`类表示叶子节点，他们可以通过相同接口进行操作，被一致地使用实现了组合模式。

## 可扩展性

1. 不改变现有代码，只需添加新的抽象工厂，即可添加新的风格：
先在AbstractFactory.py文件中添加新的风格的抽象工厂，然后在Component.py文件中添加新的风格的Leaf类和Contrainer类及其相应的风格的draw函数即可完成添加新的风格。

2. 通过配置文件，可添加新的图标族：
先在config.py文件中添加新的图标族，然后在IconFamily.py中添加相应的索引即可完成添加新的图标族。

## 运行截图

tree+star:<br />
![tree+star](output_images/tree+star.png)
<br />
tree+king:<br />
![tree+king](output_images/tree+king.png)
<br />
rectangle+star:<br />
![rectangle+star](output_images/rectangle+star.png)
<br />
rectangle+king:<br />
![rectangle+king](output_images/rectangle+king.png)
