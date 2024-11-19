# 先实现定义自己的一个一个的节点
class Node(object):
    def __init__(self, data) -> None:
        # 一个节点的数据域
        self.data = data
        # 一个节点的指针域,其存储的是下一个节点的内存地址
        self.next = None


class SingleLinkedList:
    # 在进行实例化的时候我们该有一个初始节点的，通过这个初始节点来实现寻找我们的链表，这个就是头节点了
    def __init__(self) -> None:
        self.__head = None


    # 获取链表长度
    def __get_length_link(self) -> int:
        """
        获取链表长度
        :return:
        """
        p = self.__head
        count = 1
        while p.next is not None:
            p = p.next  # 更新指向
            count += 1
        return count


    # 实现一个函数来保存数据
    def __save_data_in_list(self) -> list:
        """
        将链表元素组成一个列表返回
        :return:
        """
        data_list = []
        current = self.__head
        while current is not None:
            data_list.append(current.data)
            current = current.next
        return data_list


    # 添加单个节点操作
    def append_one_node(self, data) -> None:
        """
        一次性添加一个元素
        :param data: append element`s value
        :return: None
        """
        # 将元素转化为节点
        node = Node(data)
        # 判断头节点是否为空
        if self.__head is None:
            self.__head = node

        # 如果不为空，那就将节点挂载在有值的节点上面
        else:
            current = self.__head
            # 如果节点为空，那就直接实现节点的偏移
            while current.next:
                current = current.next
            current.next = node


    # 添加多个节点
    def append_many_node(self, list_data: list) -> None:
        """
        一次性插入多个元素
        :param list_data:
        :return:
        """
        # 直接遍历列表，实现循环添加单个节点
        for data in list_data:
            self.append_one_node(data)


    # 通过下标添加节点
    def append_node_by_index(self, index: int, data) -> None:
        """
        通过下标插入元素
        :param index:
        :param data:
        :return:
        """
        if index < 1:
            raise IndexError("Index must be greater than 0 \n")
        if index > self.__get_length_link():
            raise IndexError("index out of range!!!\n")

        current_node = self.__head
        node = Node(data)

        if index == 1:
            node.next = self.__head
            self.__head = node
        else:
            # 中间节点的插入
            current_index = 1  # 记录节点的下标
            # 实现偏移
            while current_node and current_index < index - 1:
                current_node = current_node.next
                current_index += 1
            # 插入新节点
            node.next = current_node.next
            current_node.next = node


    # 遍历显示所有的元素
    def show_link_data(self) -> None:
        """
        显示链表啊所有的元素
        :return:
        """
        if self.__head is None:
            print("链表为空")
        else:
            # 从头结点依次遍历整个链表元素
            current = self.__head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print("\n")


    # 通过下标实现查找元素: 这里的使用列表实现的话，时间复杂度有是常数级别的查找元素
    def show_data_by_index(self, index: int) -> None:
        """
        通过下标显示元素
        :param index:
        :return:
        """
        # 或者说和随机插入元素的思路实现一样的，但是这里的话我是前面提前将数据添加入了一个列表中的
        if index > self.__get_length_link():
            raise IndexError("index out of range!!!")
        data_link_list = self.__save_data_in_list()
        print(f"第{index}个元素为: {data_link_list[index - 1]}\n")


    # 删除整个链表
    def clear_link(self) -> None:
        """
        清空链表
        :return:
        """
        self.__head = None


    # 根据下标删除元素
    def delete_link_by_index(self, index: int) -> None:
        """
        根据下标删除元素
        :param index:
        :return:
        """
        if index < 1:
            raise IndexError("Index must be greater than 0 \n")
        if index > self.__get_length_link():
            raise IndexError("index out of range!!!\n")

        if index == 1:
            self.__head = self.__head.next
            return

        current = self.__head
        current_index = 1
        while current and current_index < index - 1:
            current = current.next
            current_index += 1
        new_current = current.next
        current.next = current.next.next
        new_current.next = None


    # 根据值来进行删除元素
    def delete_link_by_value(self, value) -> None:
        """
        根据值来删除元素
        :param value:
        :return:
        """
        # 头节点直接改变头节点指向即可
        if self.__head.data == value:
            self.__head = self.__head.next
            return

        current = self.__head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        if current.next is None:
            raise ValueError("value is not find")


    # 根据下标修改元素
    def set_link_by_index(self, index: int, data) -> None:
        """
        根据下标修改元素
        :param index:
        :param data:
        :return:
        """
        if index < 1:
            raise IndexError("Index must be greater than 0 \n")
        if index > self.__get_length_link():
            raise IndexError("index out of range!!!\n")

        if index == 1:
            self.__head.data = data
            return

        current = self.__head
        current_index = 1
        # 偏移指针
        while current and current_index < index:
            current_index += 1
            current = current.next
        current.data = data


    # 根据值来进行修改链表的值
    def set_link_by_value(self, value, data) -> None:
        """
        根据值来进行修改元素
        :param value: 指定需要用来查找的指标
        :param data: 需要进行替换的元素
        :return:
        """
        current = self.__head
        if current.data == value:
            current.data = data
            return

        while current.next:
            if current.next.data == value:
                current.next.data = data
                return
            current = current.next

        if current.next is None:
            raise ValueError("value is not find!!!")