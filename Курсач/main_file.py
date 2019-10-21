id_list = []
Author_List = []
Data_List = []
Sorted_list = []
with open('lib.txt', encoding="utf8") as f:
    list1 = f.read().splitlines()
for i in range(len(list1)):
    temp = str(list1[i])
    str1 = temp.split(' : ')
    id_list.append(str1[0])


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s %s %s)" % (self.left or "", self.key, self.right or "")


def insert(tree, key):
    if not tree:
        tree = Node(key)
    elif key < tree.key:
        tree = Node(tree.key, insert(tree.left, key), tree.right)
    elif key > tree.key:
        tree = Node(tree.key, tree.left, insert(tree.right, key))
    return tree


def print_lib():
    for el in range(len(list1)):
        split_lib = str(list1[el]).split(' : ')
        print("id: " + split_lib[0] + " | Название: " + split_lib[1] +
              " | Автор: " + split_lib[2] + " | Год издания: " + split_lib[3] +
              " | Количество экземпляров: " + split_lib[4])


def add_book(information):
    can = True
    split_book = information.split(' : ')
    for el in id_list:
        if split_book[0] == el:
            can = False
    if can:
        list1.append(information)
        id_list.append(information[0])
    else:
        print("Библиотека уже содержит книгу с id " + information[0])


def remove_book(id_book):
    remove = False
    for el in range(len(list1)):
        split_book = str(list1[el]).split(' : ')
        if int(split_book[0]) == int(id_book):
            remove = True
            list1.pop(el)
            id_list.pop(el)
            break
    if not remove:
        print("Книга с id " + id_book + " не найдена в библиотеке")
    else:
        print("Книга c id " + id_book + " удалена из библиотеки")


def author_list():
    Author_List.clear()
    for el in range(len(list1)):
        split_author = str(list1[el]).split(' : ')
        Author_List.append(split_author[2])
    for el in range(len(Author_List)):
        print(Author_List[el])


def tree_builder():
    tree = None
    for el in range(len(list1)):
        split_tree = str(list1[el]).split(' : ')
        Data_List.append(split_tree[3])
    for j in range(len(Data_List)):
        tree = insert(tree, Data_List[j])
    sorted_tree(tree)


def sorted_tree(tree):
    for el in range(len(Data_List)):
        for j in range(len(Data_List)):
            if sort1(tree)[el] == Data_List[j]:
                Sorted_list.append(list1[j])
    for el in range(len(Sorted_list)):
        list1[el] = Sorted_list[el]
    print_lib()
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
              "\n[5] - Сформированить список авторов"
              "\n[6] - Завершить работу")
        inp = int(input("Выберите действие: "))
        if inp == 1:
            print_lib()
        if inp == 2:
            print("Введите информация о книге о книге в формате"
                  "(id : Название : ФИО автора : год издания : количество): ")
            info = input()
            add_book(info)
        if inp == 3:
            print("Введите id книги для удаления: ")
            id_book = input()
            remove_book(id_book)
        if inp == 4:
            tree_builder()
        if inp == 5:
            author_list()
        if inp == 6:
            print("\nРабота программы завершена")
            exit(0)


main()
