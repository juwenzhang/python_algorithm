# 对于我们实现栈的操作的是，实际上的话就是实现的是我们的操作我们的头节点实现的增删的操作实现

# 设置节点的元素
class Node(object):
    def __init__(self, val, _next = None):
        self.val = val
        self.next = _next


# 开始实现设计我们的栈结构的实现
class Link_Stack(object):
    # 在构造函数中实现设置我们的栈顶
    def __init__(self):
        self.__top = None

    # 栈结构只有两个操作就是一个是推数据进入我们的栈，另一个就是推数据出栈
    def push(self, data):
        # 先实现转化为节点设计
        node = Node(data)
        # 将该节点的指针指向栈顶
        node.next = self.__top
        self.__top = node

    def pop(self):
        # 探究我们的栈是否为空
        if self.__top is None:
            raise Exception("stack is None")
        data = self.__top.val
        # 实现更新头栈顶节点
        self.__top = self.__top.next
        return data

    # 实现获取栈顶元素
    def get_top_data(self):
        if self.__top is None:
            print(None)
            return
        return self.__top.val

    # 实现的是显示栈中的所有的元素
    def show_all_data(self):
        if self.__top is None:
            print(None)
            return
        while self.__top is not None:
            print(self.__top.val)
            self.__top = self.__top.next


if __name__ == "__main__":
    link_stack = Link_Stack()

    # link_stack.push(1)
    # link_stack.push(2)

    print(link_stack.get_top_data())

    link_stack.show_all_data()
