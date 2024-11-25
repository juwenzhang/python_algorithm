# 通过我们的列表实现我们的队列
# 队列的实现的是一边进入一边出
# 实现的是先进先出，后进后出

class Queue(object):
    # 构造函数
    def __init__(self):
        self.__list_queue = []

    # 实现的是我们的入队
    def push_back(self, data):
        self.__list_queue.append(data)

    # 开始实现我们的出队
    def pop_front(self):
        if self.__list_queue == []:
            raise Exception("queue is empty")
        return self.__list_queue.pop(0)

    # 开始实现我们的获取队列大小的操作
    def get_size(self):
        if self.__list_queue == []:
            return "queue is empty"
        return len(self.__list_queue)

    # 实现判断queue 是否为空的函数
    def is_empty(self):
        return self.__list_queue == []

    # 开始实现获取我们的数组中的元素
    def show_queue(self):
        if self.__list_queue == []:
            return None
        for item in self.__list_queue:
            print(item, end="  ")
        print("\n")

if __name__ == "__main__":
    queue = Queue()

    queue.push_back(11)
    queue.push_back(12)

    queue.show_queue()
    print(queue.pop_front())