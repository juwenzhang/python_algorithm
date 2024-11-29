# 使用我们的链表作为底层的数据结构实现队列
# from multiprocessing import Queue

class Queue_Node(object):
    def __init__(self, val, back = None):
        self.val = val
        self.back = back  # 记录的是入队的节点指针

class Queue(object):
    # 构造函数
    def __init__(self):
        self.__head = self.__end = Queue_Node(None)

    # 开始我们的入队操作
    def push(self, data):
        self.__head.back = Queue_Node(data)
        # 然后将我们的头节点执行现在新加的节点,实现节点的后移
        self.__head = self.__head.back

    # 出队的操作实现
    def pop(self):
        # 实现的是先进先出
        # 我们这里的 end 节点是一直不用更新的，一直指向的是最初的头节点
        if self.__head == self.__end:
            raise Exception("queue is empty")
        self.__end = self.__end.back
        return self.__end.val

    def show_front_val(self):
        if self.__head.back is None:
            raise Exception("queue is empty")
        return self.__head.back.val

    def show_end_val(self):
        if self.__end:
            return self.__end.val
        raise Exception("queue is empty")


if __name__ == "__main__":
    queue = Queue()

    print(queue.show_end_val())
    queue.push(1)
    # print(queue.show_end_val())
    queue.push(2)
    print(queue.show_end_val())
    queue.push(3)
    print(queue.show_end_val())
    queue.push(4)
    print(queue.show_end_val())

    # 开始出栈
    print(queue.show_end_val())
    print(queue.pop())
    print(queue.show_end_val())
    print(queue.pop())
    print(queue.show_end_val())
    print(queue.pop())
    print(queue.pop())


    # https://developer.aliyun.com/article/953777  队列的实现场景，消息队列的实现