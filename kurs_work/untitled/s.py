Author_List = []
Data_List = []
Sorted_list = []


class Nod:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s %s %s)" % (self.left or "", self.key, self.right or "")


def insert(tree, key):
    if not tree:
        tree = Nod(key)
    elif key < tree.key:
        tree = Nod(tree.key, insert(tree.left, key), tree.right)
    elif key > tree.key:
        tree = Nod(tree.key, tree.left, insert(tree.right, key))
    return tree


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def len(self):
        self.length = 0
        if self.first is not None:
            self.length += 1
            current = self.first
            while current.next is not None:
                current = current.next
                self.length += 1
        return self.length

    def add(self, x):
        can = True
        split_book = x.split(' : ')
        for i in range(list2.len()):
            current = self.first
            while current is not None:
                temp1 = current.value.split(' : ')
                if split_book[0] == temp1[0]:
                    can = False
                current = current.next
        if can:
            if self.first is None:
                self.first = Node(x)
                self.last = self.first
            elif self.last == self.first:
                self.last = Node(x)
                self.first.next = self.last
            else:
                current = Node(x)
                self.last.next = current
                self.last = current
        else:
            print("Библиотека уже содержит книгу с id " + x[0])

    def del_lst(self, i):
        current = self.first
        y = -1
        while current is not None:
            temp1 = current.value.split(' : ')
            y += 1
            if temp1[0] == i:
                break
            current = current.next
        if self.first is None:
            return
        old = curr = self.first
        count = 0
        if y == 0:
            self.first = self.first.next
            return
        while curr is not None:
            if count == y:
                if curr.next == self.last:
                    self.last = curr
                    break
                else:
                    old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    def print(self):
        current = self.first
        while current is not None:
            print(current.value)
            current = current.next

    def author(self):
        current = self.first
        while current is not None:
            temp1 = current.value.split(' : ')
            print(temp1[2])
            current = current.next

    def tree_sort(self):
        list1.clear()
        current = self.first
        while current is not None:
            list1.append(current.value)
            current = current.next


list2 = LinkedList()
with open('lib.txt', encoding="utf8") as f:
    list1 = f.read().splitlines()

for el in range(len(list1)):
    list2.add(list1[el])


def tree_builder():
    tree = None
    list2.tree_sort()
    for l in range(len(list1)):
        split_tree = str(list1[l]).split(' : ')
        Data_List.append(split_tree[3])
    for j in range(len(Data_List)):
        tree = insert(tree, Data_List[j])
    sorted_tree(tree)


def sorted_tree(tree):
    for l in range(len(Data_List)):
        for j in range(len(Data_List)):
            if sort1(tree)[l] == Data_List[j]:
                Sorted_list.append(list1[j])
    list2.clear()
    for l in range(len(Sorted_list)):
        list2.add(Sorted_list[l])
    list2.print()
    Data_List.clear()
    Sorted_list.clear()


def sort1(tree):
    if not tree:
        return []
    return sort1(tree.right) + [tree.key] + sort1(tree.left)


def main():
    while True:
        print("\nМеню:"
              "\n[1] - Посмотреть список книг"
              "\n[2] - Добавить новую книгу"
              "\n[3] - Удалить книгу"
              "\n[4] - Сортировка книг по году издания"
              "\n[5] - Сформировать список авторов"
              "\n[6] - Завершить работу")
        inp = int(input("Выберите действие: "))
        if inp == 1:
            list2.print()
        if inp == 2:
            print("Введите информация о книге о книге в формате"
                  "(id : Название : ФИО автора : год издания : количество): ")
            info = input()
            list2.add(info)
        if inp == 3:
            print("Введите id книги для удаления: ")
            id_book = input()
            list2.del_lst(id_book)
        if inp == 4:
            tree_builder()
        if inp == 5:
            list2.author()
        if inp == 6:
            print("\nРабота программы завершена")
            exit(0)


main()
