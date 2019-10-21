id_list = ['1', '2', '3', '4', '5', '6', '7', '8']
Author_List = []
Data_List = []
Sorted_list = []
list1 = ['1 : Говорит седьмой этаж : Алексин А.Г : 1961 : 5',
         '2 : Военная тайна : Гайдар А.П : 1935 : 10',
         '3 : Отель : Артур Хейли : 1865 : 6',
         '4 : Сотников : Быков В.В : 1970 : 7',
         '5 : Война и мир : Толстой Л.Н : 1869 : 9',
         '6 : Письмо к ученому соседу : Чехов А.П : 1880 : 8',
         '7 : Конкуренты : Лукьяненко С.В : 2008 : 2',
         '8 : Пакет : Пантелеев А.И : 1977 : 5']


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
    for i in range(len(list1)):
        print_lst = str(list1[i])
        str1 = print_lst.split(' : ')
        print("id: " + str1[0] + " | Название: " + str1[1] +
              " | Автор: " + str1[2] + " | Год издания: " + str1[3] +
              " | Количество экземпляров: " + str1[4])


def add_book(information):
    can = True
    str1 = information.split(' : ')
    for i in id_list:
        if str1[0] == i:
            can = False
    if can:
        list1.append(information)
        id_list.append(information[0])
    else:
        print("Список уже содержит книгу с данным id")


def remove_book(id_book):
    remove = False
    for i in range(len(list1)):
        print_lst = str(list1[i])
        str1 = print_lst.split(' : ')
        if int(str1[0]) == int(id_book):
            remove = True
            list1.pop(i)
            id_list.pop(i)
            break
    if not remove:
        print("Книга не найдена")
    else:
        print("Книга удалена")


def author_list():
    Author_List.clear()
    for i in range(len(list1)):
        print_lst = str(list1[i])
        str1 = print_lst.split(' : ')
        Author_List.append(str1[2])
    for i in range(len(Author_List)):
        print(Author_List[i])


def tree_builder():
    tree = None
    for i in range(len(list1)):
        print_lst = str(list1[i])
        str1 = print_lst.split(' : ')
        Data_List.append(str1[3])
    for j in range(len(Data_List)):
        tree = insert(tree, Data_List[j])
    sorted_tree(tree)


def sorted_tree(tree):
    for i in range(len(Data_List)):
        for j in range(len(Data_List)):
            if sort1(tree)[i] == Data_List[j]:
                Sorted_list.append(list1[j])
    for i in range(len(Sorted_list)):
        list1[i] = Sorted_list[i]
    print_lib()
    Data_List.clear()
    Sorted_list.clear()


def sort1(tree):
    if not tree:
        return []
    return sort1(tree.right) + [tree.key] + sort1(tree.left)


def main():
    while True:
        print("\n[1] - Посмотреть список книг"
              "\n[2] - Добавить новую книгу"
              "\n[3] - Удалить книгу"
              "\n[4] - Сортировка книг по году издания"
              "\n[5] - Сформированить список авторов"
              "\n[6] - Завершить работу")
        inp = int(input("Выберите действие: "))
        if inp == 1:
            print_lib()
        if inp == 2:
            print("Введите инфо о книге: ")
            info = input()
            add_book(info)
        if inp == 3:
            print("Введите id книги: ")
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
