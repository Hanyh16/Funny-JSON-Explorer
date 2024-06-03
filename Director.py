# 指导者类，负责创建产品
class Director:
    def __init__(self, builder):
        self.builder = builder

    def create(self):
        # 创建中间节点和叶子节点
        self.builder.create_container()
        self.builder.create_leaf()

    def _load(self, data, icons):
        # 创建根节点
        self.builder.root_container = self.builder.container('root', 0, icons[0])
        # 初始化容器堆栈，用于跟踪需要处理的容器和数据
        container_stack = [(self.builder.root_container, data)]
        
        # 处理堆栈中的每个元素
        while container_stack:
            current_container, current_data = container_stack.pop()
            
            # 遍历当前数据的每个键值对
            for key, value in current_data.items():
                child_level = current_container.level + 1
                
                if isinstance(value, dict):
                    # 如果值是字典，则创建子容器并压入堆栈
                    child_container = self.builder.container(key, child_level, icons[0])
                    current_container.add(child_container)
                    container_stack.append((child_container, value))
                else:
                    # 如果值不是字典，则创建叶子节点
                    child_leaf = self.builder.leaf(key, value, child_level, icons[1])
                    current_container.add(child_leaf)

    def show(self, line_length):
        # 用于展示结构的方法
        is_last_levels = []  # 追踪各级别的最后一个元素
        for i, child in enumerate(self.builder.root_container.children):
            # 判断当前子节点是否是第一个或最后一个
            is_first = i == 0
            is_last = i == len(self.builder.root_container.children) - 1
            # 绘制子节点
            child.draw(is_first, is_last, is_last_levels, line_length)