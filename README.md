# Funny-JSON-Explorer
Funny JSON Explorer(FJE),是一个JSON文件可视化的命令行界面小工具 

## 类图
![UML](UML.png)

## 设计模式

1. **工厂方法**（Factory）：将对象的创建延迟到工厂的子类中，由子类决定创建哪个具体的对象，使用工厂方法模式时，新增新的产品也就是新增新的风格只需要添加对应的工厂类，不需要修改现有代码，对应于Icon-Family风格的使用，每个新的Icon-Family对应新建的一个工厂类和产品类。

工厂方法（Factory） 定义了一个创建对象的接口，但由子类决定实例化哪一个类。用于处理实现不同输出风格。我们首先创建一个总的风格输出工厂(JSONshowFactory),我们在高层应用时创建对象就直接创建JSONshowFactory 对象，而不加以区分风格，然后衍生出两个具体的风格渲染工厂类。我们在JSONObject 和 JSONLeaf中具有一个属性决定渲染风格，对应着有多个产品。而不同风格则对应不同产品。 高层与底层的调用只需要关注最开始的工厂接口即可，而不需要找到真正得到的工厂。 并且这样的架构，我们在后续增加更多风格渲染工厂，调用者也不需要进行修改调用方式。此外，在每一个风格输出工厂中，还有区分叶子和中间节点。渲染的实现取决于 叶子或者中间节点的style属性。每个style属性都是一种showStyle类。

定义一种创建对象的接口，但将具体实例化对象的工作推迟到子类中完成。在本项目中我使用工厂方法模式的具体方法在于AbstractFactory类及其子类TreeStyleFactory和RectangleStyleFactory。首先在抽象工厂类AbstractFactory中定义了两个用于创建对象的抽象函数create_container()和create_leaf()，然后在树形风格工厂类TreeStyleFactory实现了create_container()函数和create_leaf()函数分别用于创建树形风格的中间节点和树形风格的叶子节点；在矩形风格工厂类RectangleStyleFactory中实现了create_container()函数和create_leaf()函数分别用于创建矩形风格的中间节点和矩形风格的叶子节点。这样的话Director类使用工厂来创建对象时并不直接依赖于具体的类名，而且当需要更改具体的实现时，只需替换工厂的子类，而无需修改Director类的代码。


2. 
