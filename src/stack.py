class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)
        node.next_node = self.top
        self.top = node

    def is_empty(self):
        return self.top is None

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next_node
        return data

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next_node
        return f'Stack({", ".join(items)})'






