import tkinter as tk
from tkinter import messagebox
from Tree import *
from List import *

Data_List = []  # список дат
Sorted_list = []  # временный список для сортировки
root = tk.Tk()

text_list = tk.Text(root, font=12, width=70, height=25)
text_list.configure(state="disabled")
text_list.place(relx=0.34, rely=0.05)
text_authors = tk.Text(root, font=12, width=25, height=22.35, bg='#BDBABA')
text_authors.configure(state="disabled")
text_authors.place()
text_authors.place_forget()


def insert(tree, data):  # функция вставки элемента в дерево
    if not tree:
        tree = TreeNode(data)
    elif data < tree.data:
        tree = TreeNode(tree.data, insert(tree.left, data), tree.right)
    elif data > tree.data:
        tree = TreeNode(tree.data, tree.left, insert(tree.right, data))
    return tree


class LinkedList:  # класс односвязного списка
    def __init__(self):
        self.head = None
        self.length = 0

    def clear(self):  # функция очистки односвязного списка
        self.__init__()

    def len(self):  # функция подсчета размена односвязного списка
        self.length = 0
        if self.head is not None:
            self.length -= -1
            cur = self.head
            while cur.next is not None:  # перебор элементов для подсчета длины
                cur = cur.next
                self.length -= -1  # подсчет длины односвязного списка
        return self.length

    def add(self, data):  # функция добавления элемента в односвязный список
        split_book = data.split(' : ')
        if not split_book[3].isdigit():  # проверка правильности введенных данных
            messagebox.showerror("TypeError", "Год издания должен быть указан числом")
            return
        if not split_book[4].isdigit():  # проверка правильности введенных данных
            messagebox.showerror("TypeError", "Кол-во экземпляров должно быть указано числом")
            return
        if not split_book[0].isdigit():  # проверка правильности введенных данных
            messagebox.showerror("TypeError", "Id должен быть указан числом")
            return
        cur = self.head
        for i in range(list2.len()):
            while cur is not None:  # перебор элементов для проверки, существует ли введенный id в односвязном списке
                temp1 = cur.value.split(' : ')
                if split_book[0] == temp1[0]:
                    messagebox.showerror("IdError", "Библиотека уже содежит книгу с введенным id " + split_book[0])
                    return
                cur = cur.next
        NewNode = ListNode(data)
        NewNode.next = self.head
        self.head = NewNode

    def del_element(self, index):  # функция удаления элемента из односвязного списка
        if not str(index).isdigit():  # проверка правильности введенных данных
            messagebox.showerror("TypeError", "Id для удаления должен быть указан числом")
            return
        text_authors.place_forget()
        label_authors.place_forget()
        cur = self.head
        temp2 = cur.value.split(' : ')
        if temp2[0] == index:
            self.head = cur.next
            return
        can = False
        while cur is not None:  # перебор элементов списка для нахождения индекса в списке
            temp1 = cur.value.split(' : ')
            if temp1[0] == index:  # проверка наличия индекса в односвязном списке
                can = True
                break
            cur = cur.next
        if can:  # если индекс существует в односвязном списке, то происходит его удаление
            current = self.head
            while current is not None:
                temp2 = current.value.split(' : ')
                if temp2[0] == index:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
        else:
            messagebox.showerror("InputError", "Введен некорректный id")

    def print(self):  # функция вывода односвязного списка на форму
        text_authors.place_forget()
        label_authors.place_forget()
        text_list.configure(state="normal")
        text_list.delete(1.0, tk.END)
        cur = self.head
        while cur is not None:  # перебор элементов односвязного списка для вывода на форму
            tmp = str(cur.value).split(" : ")
            text_list.insert(0.0, "id: " + tmp[0] + " Название: " + tmp[1] + " Автор: " + tmp[2] + " Год: " + tmp[3] +
                             " Кол-во: " + tmp[4])
            text_list.insert(0.0, '\n')
            cur = cur.next
        text_list.configure(state="disabled")

    def author(self):  # функция вывода списка авторов
        cur = self.head
        text_authors.configure(state="normal")
        text_authors.delete(1.0, tk.END)
        text_authors.place(relx=0.74, rely=0.1)
        label_authors.place(relx=0.75, rely=0.101, relwidth=0.20, relheight=0.03)
        while cur is not None:  # перебор элементов односвязного списка для вывода списка авторов на форму
            temp1 = cur.value.split(' : ')
            text_authors.insert(0.0, " " + temp1[2])
            text_authors.insert(0.0, '\n')
            cur = cur.next
        text_authors.configure(state="disabled")

    def tree_sort(self, ):  # функция сортировки с помощью двоичного дерева
        list1.clear()
        cur = self.head
        while cur is not None:
            list1.append(cur.value)
            cur = cur.next


def autoFill():
    with open('lib.txt', encoding="utf8") as f:  # заполнение библиотеки из файла
        list1 = f.read().splitlines()
    text_list.configure(state="normal")
    for el in range(len(list1)):
        list2.add(list1[el])
    list1.reverse()
    for ele in range(len(list1)):  # вывод списка книг на форму
        tmp1 = str(list1[ele]).split(" : ")
        text_list.insert(0.0, "id: " + tmp1[0] + " Название: " + tmp1[1] + " Автор: " + tmp1[2] + " Год: " + tmp1[
            3] + " Кол-во: " + tmp1[4])
        text_list.insert(0.0, '\n')
    text_list.configure(state="disabled")


def tree_builder():  # функция постоения дерева
    text_authors.place_forget()
    label_authors.place_forget()
    tree = None
    list2.tree_sort()
    for l in range(len(list1)):  # формирование дерева
        split_tree = str(list1[l]).split(' : ')
        Data_List.append(split_tree[3])
        tree = insert(tree, Data_List[l])
    sorted_tree(tree)  # вызов функции сортировки


def sorted_tree(tree):  # функция сортировки linked list
    for l in range(len(Data_List)):
        for j in range(len(Data_List)):
            try:
                if sort(tree)[l] == Data_List[j]:  # сравнение каждого элемента дерева с каждым элементом списка дат
                    Sorted_list.append(list1[j])  # формирование буферного отсортированного списка
            except IndexError:
                pass
    list2.clear()
    for l in range(len(Sorted_list)):
        list2.add(Sorted_list[l])  # заполнение linked list элементами буферного списка
    list2.print()
    Data_List.clear()
    Sorted_list.clear()


def sort(tree):  # рекурсивная функция сортировки дерева
    if not tree:
        return []
    return sort(tree.right) + [tree.data] + sort(tree.left)


def add_book():  # функция добавления книги в библиотеку
    text_authors.place_forget()
    label_authors.place_forget()
    if len(entry_id.get()) != 0 and len(entry_title.get()) != 0 and len(entry_author.get()) != 0 and \
            len(entry_year.get()) != 0 and len(entry_count.get()) != 0:
        buff = entry_id.get() + " : "
        buff += entry_title.get() + " : "
        buff += entry_author.get() + " : "
        buff += entry_year.get() + " : "
        buff += entry_count.get()
        list2.add(buff)  # добавление книги в linked list
    else:
        messagebox.showerror("InputError", "Все поля должны быть заполнены")
    list2.print()


list1 = []
list2 = LinkedList()
# region UI создание графического интерфейса
label_name = tk.Label(root, font=12, text="Список книг в библиотеке:", fg='black', bg='white')
label_name.place(relx=0.4, rely=0.051, relwidth=0.50, relheight=0.03)

button_add = tk.Button(root, text="Добавить", bg='#2E8B57', command=lambda: (add_book(), list2.print()))
button_add.place(relx=0.07, rely=0.40, relwidth=0.20, relheight=0.05)

button_add = tk.Button(root, text="Автозаполнение", bg='#2E8B57', command=lambda: (list2.clear(), autoFill(), list2.print()))
button_add.place(relx=0.07, rely=0.47, relwidth=0.20, relheight=0.05)

button_print = tk.Button(root, text="Очистить", bg='#8A0808', command=lambda: (list2.clear(), list2.print()))
button_print.place(relx=0.07, rely=0.91, relwidth=0.20, relheight=0.05)

button_sort = tk.Button(root, text="Отсортировать", bg='#2E8B57', command=lambda: (tree_builder(), list2.print()))
button_sort.place(relx=0.07, rely=0.84, relwidth=0.20, relheight=0.05)

button_del = tk.Button(root, text="Удалить", bg='#8A0808', command=lambda: (list2.del_element(entry_del.get()),
                                                                            list2.print()))
button_del.place(relx=0.07, rely=0.67, relwidth=0.20, relheight=0.05)

button_authors = tk.Button(root, text="Список авторов", bg='#2E8B57', command=lambda: list2.author())
button_authors.place(relx=0.07, rely=0.77, relwidth=0.20, relheight=0.05)

entry_id = tk.Entry(root, font=12)
entry_id.place(relx=0.07, rely=0.05, relwidth=0.20, relheight=0.05)

entry_title = tk.Entry(root, font=12)
entry_title.place(relx=0.07, rely=0.12, relwidth=0.20, relheight=0.05)

entry_author = tk.Entry(root, font=12)
entry_author.place(relx=0.07, rely=0.19, relwidth=0.20, relheight=0.05)

entry_year = tk.Entry(root, font=12)
entry_year.place(relx=0.07, rely=0.26, relwidth=0.20, relheight=0.05)

entry_count = tk.Entry(root, font=12)
entry_count.place(relx=0.07, rely=0.33, relwidth=0.20, relheight=0.05)

entry_del = tk.Entry(root, font=12)
entry_del.place(relx=0.07, rely=0.6, relwidth=0.20, relheight=0.05)

label_id = tk.Label(root, font=12, text="Id:", fg='black')
label_id.place(relx=0.045, rely=0.05)

label_title = tk.Label(root, font=12, text="Назв:", fg='black')
label_title.place(relx=0.023, rely=0.12)

label_author = tk.Label(root, font=12, text="Автор:", fg='black')
label_author.place(relx=0.015, rely=0.19)

label_year = tk.Label(root, font=12, text="Год:", fg='black')
label_year.place(relx=0.031, rely=0.26)

label_count = tk.Label(root, font=12, text="Кол-во:", fg='black')
label_count.place(relx=0.01, rely=0.33)

label_del_id = tk.Label(root, font=12, text="Id для удаления:", fg='black')
label_del_id.place(relx=0.07, rely=0.55, relwidth=0.20, relheight=0.05)

label_authors = tk.Label(root, font=12, text="Список авторов:", fg='black', bg='#BDBABA')
label_authors.place()
label_authors.place_forget()

# endregion

if __name__ == "__main__":
    root.title("Учет книг в библиотеке")
    root.geometry("1000x500")
    root.resizable(False, False)
    root.mainloop()
