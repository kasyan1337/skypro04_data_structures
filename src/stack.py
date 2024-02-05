class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
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
        self.top = None  # Инициализация вершины стека

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)  # Создание нового узла, который указывает на текущую вершину стека
        self.top = new_node  # Обновление вершины стека на новый узел

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None  # Возвращаем None, если стек пуст
        removed_data = self.top.data  # Сохраняем данные удаляемого узла
        self.top = self.top.next_node  # Перемещаем вершину стека на следующий узел
        return removed_data
