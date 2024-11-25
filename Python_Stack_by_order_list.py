# 顺序表实现栈结构
# 栈顶的定位是关键点
# list 这个时候就是我们底层的数据结构了
# 为了我们性能的考虑，所以说我们实现的是将我们的列表的尾部作为栈顶的

class List_Stack(object):
    # 初始化函数，封装列表作为我们的底层的数据结构
    def __init__(self):
        self.__list_stack = []

    # 使用我们的 append 方法来实现我们的栈的添加元素
    def push_back(self, data):
        self.__list_stack.append(data)

    # 实现的是我们的出栈
    def pop_back(self):
        if self.__list_stack == []:
            raise Exception("stack is empty")
        return self.__list_stack.pop(-1)

    # 判断我们的栈是否为空
    def is_empty(self):
        # if len(self.__list_stack) > 0:
        #     return False
        # else:
        #     return True
        return self.__list_stack == []


if __name__ == "__main__":
    list_stack = List_Stack()
    print(list_stack.is_empty())  # True

    list_stack.push_back(11)
    print(list_stack.is_empty())  # False

    list_stack.pop_back()
    print(list_stack.is_empty())  # False

    # 栈 stack 的这个数据结构的话还是十分简单的，相比链表的话，其具备的功能这些的的确确少了很多呐