import tkinter as tk
from tkinter import messagebox

Data_List = []
Sorted_list = []
root = tk.Tk()
text_list = tk.Text(root, font=12, width=70, height=25)
text_list.configure(state="disabled")
text_list.place(relx=0.34, rely=0.05)

text_authors = tk.Text(root, font=12, width=25, height=15, bg='#BDBABA')
text_authors.configure(state="disabled")
text_authors.place()
text_authors.place_forget()


class TreeNode:  # класс дерева
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(tree, data):  # функция вставки элемента в дерево
    if not tree:
        tree = TreeNode(data)
    elif data < tree.data:
        tree = TreeNode(tree.data, insert(tree.left, data), tree.right)
    elif data > tree.data:
        tree = TreeNode(tree.data, tree.left, insert(tree.right, data))
    return tree


class ListNode:  # класс ячейки
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:  # класс списка
    def __init__(self):
        self.head = None
        self.length = 0

    def clear(self):  # функция очистки linked list
        self.__init__()

    def len(self):  # функция рассчета размена linked list
        self.length = 0
        if self.head is not None:
            self.length += 1
            cur = self.head
            while cur.next is not None:
                cur = cur.next
                self.length += 1
        return self.length

    def add(self, data):  # функция добавления элемента в linked list
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
            while cur is not None:
                temp1 = cur.value.split(' : ')
                if split_book[0] == temp1[0]:
                    messagebox.showerror("IdError", "Библиотека уже содежит книгу с введенным id " + split_book[0])
                    return
                cur = cur.next
        NewNode = ListNode(data)
        NewNode.next = self.head
        self.head = NewNode

    def del_element(self, index):  # функция удаления элемента из linkedlist
        if not str(index).isdigit():  # проверка правильности введенных данных
            messagebox.showerror("TypeError", "Id для удаления должен быть указан числом")
            return
        text_authors.place_forget()
        label_authors.place_forget()
        cur = self.head
        y = -1
        can = False
        while cur is not None:
            temp1 = cur.value.split(' : ')
            y += 1
            if temp1[0] == index:
                can = True
                break
            cur = cur.next
        if can:
            current = self.head
            if current is not None:
                temp2 = current.value.split(' : ')
                if temp2[0] == index:
                    self.head = current.next
                    return
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

    def print(self):  # функция вывода linked list
        text_authors.place_forget()
        label_authors.place_forget()
        text_list.configure(state="normal")
        text_list.delete(1.0, tk.END)
        cur = self.head
        while cur is not None:
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
        text_authors.place(relx=0.74, rely=0.4)
        label_authors.place(relx=0.75, rely=0.401, relwidth=0.20, relheight=0.03)
        while cur is not None:
            temp1 = cur.value.split(' : ')
            text_authors.insert(0.0, " " + temp1[2])
            text_authors.insert(0.0, '\n')
            cur = cur.next
        text_authors.configure(state="disabled")

    def tree_sort(self):  # функция сортировки с помощью двоичного дерева
        list1.clear()
        cur = self.head
        while cur is not None:
            list1.append(cur.value)
            cur = cur.next


list2 = LinkedList()
with open('lib.txt', encoding="utf8") as f:  # заполнение библиотеки из файла
    list1 = f.read().splitlines()
text_list.configure(state="normal")
for el in range(len(list1)):
    list2.add(list1[el])
list1.reverse()
for ele in range(len(list1)):
    tmp1 = str(list1[ele]).split(" : ")
    text_list.insert(0.0, "id: " + tmp1[0] + " Название: " + tmp1[1] + " Автор: " + tmp1[2] + " Год: " + tmp1[
        3] + " Кол-во: " + tmp1[4])  # вывод списка книг на форму
    text_list.insert(0.0, '\n')
text_list.configure(state="disabled")


def tree_builder():  # функция постоения дерева
    text_authors.place_forget()
    label_authors.place_forget()
    tree = None
    list2.tree_sort()
    for l in range(len(list1)):
        split_tree = str(list1[l]).split(' : ')
        Data_List.append(split_tree[3])
    for j in range(len(Data_List)):
        tree = insert(tree, Data_List[j])
    sorted_tree(tree)


def sorted_tree(tree):  # функция сортировки linked list
    for l in range(len(Data_List)):
        for j in range(len(Data_List)):
            try:
                if sort(tree)[l] == Data_List[j]:
                    Sorted_list.append(list1[j])
            except IndexError:
                pass
    list2.clear()
    for l in range(len(Sorted_list)):
        list2.add(Sorted_list[l])
    list2.print()
    Data_List.clear()
    Sorted_list.clear()


def sort(tree):  # функция сортировки дерева
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
        list2.add(buff)
    else:
        messagebox.showerror("InputError", "Все поля должны быть заполнены")
    list2.print()


# region UI создание графического интерфейса
label_name = tk.Label(root, font=12, text="Список книг в библиотеке:", fg='black', bg='white')
label_name.place(relx=0.4, rely=0.051, relwidth=0.50, relheight=0.03)

button_add = tk.Button(root, text="Добавить", bg='#2E8B57', command=lambda: (add_book(), list2.print()))
button_add.place(relx=0.07, rely=0.40, relwidth=0.20, relheight=0.05)

button_print = tk.Button(root, text="Очистить", bg='#8A0808', command=lambda: (list2.clear(), list2.print()))
button_print.place(relx=0.07, rely=0.91, relwidth=0.20, relheight=0.05)

button_sort = tk.Button(root, text="Отсортировать", bg='#2E8B57', command=lambda: (tree_builder(), list2.print()))
button_sort.place(relx=0.07, rely=0.84, relwidth=0.20, relheight=0.05)

button_del = tk.Button(root, text="Удалить", bg='#8A0808', command=lambda: (list2.del_element(entry_del.get()),
                                                                            list2.print()))
button_del.place(relx=0.07, rely=0.62, relwidth=0.20, relheight=0.05)

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
entry_del.place(relx=0.07, rely=0.55, relwidth=0.20, relheight=0.05)

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
label_del_id.place(relx=0.07, rely=0.5, relwidth=0.20, relheight=0.05)

label_authors = tk.Label(root, font=12, text="Список авторов:", fg='black', bg='#BDBABA')
label_authors.place()
label_authors.place_forget()

# endregion

if __name__ == "__main__":
    root.title("Учет книг в библиотеке")
    root.geometry("1000x500")
    root.resizable(False, False)
    root.mainloop()
