import tkinter as tk

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
            print("Библиотека уже содежит книгу с введенным id " + x[0])

    def del_lst(self, i):
        text_authors.place_forget()
        label_authors.place_forget()
        current = self.first
        y = -1
        can = False
        while current is not None:
            temp1 = current.value.split(' : ')
            y += 1
            if temp1[0] == i:
                can = True
                break
            current = current.next
        if can:
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
        else:
            print("Введен некорректный id")
        list2.print()

    def print(self):
        text_authors.place_forget()
        label_authors.place_forget()
        text_list.configure(state="normal")
        text_list.delete(1.0, tk.END)
        current = self.first
        while current is not None:
            tmp = str(current.value).split(" : ")
            text_list.insert(0.0, "id: "+tmp[0]+" Название: "+tmp[1]+" Автор: "+tmp[2]+" Год: "+tmp[3]+" Кол-во: "+tmp[4])
            text_list.insert(0.0, '\n')
            current = current.next
        text_list.configure(state="disabled")

    def author(self):
        current = self.first
        text_authors.configure(state="normal")
        text_authors.delete(1.0, tk.END)
        text_authors.place(relx=0.74, rely=0.4)
        label_authors.place(relx=0.75, rely=0.401, relwidth=0.20, relheight=0.03)
        while current is not None:
            temp1 = current.value.split(' : ')
            text_authors.insert(0.0, " " + temp1[2])
            text_authors.insert(0.0, '\n')
            current = current.next
        text_authors.configure(state="disabled")

    def tree_sort(self):
        list1.clear()
        current = self.first
        while current is not None:
            list1.append(current.value)
            current = current.next


list2 = LinkedList()
with open('lib.txt', encoding="utf8") as f:
    list1 = f.read().splitlines()
text_list.configure(state="normal")
for el in range(len(list1)):
    list2.add(list1[el])
    tmp1 = str(list1[el]).split(" : ")
    text_list.insert(0.0, "id: "+tmp1[0]+" Название: "+tmp1[1]+" Автор: "+tmp1[2]+" Год: "+tmp1[3]+" Кол-во: "+tmp1[4])
    text_list.insert(0.0, '\n')
text_list.configure(state="disabled")


def tree_builder():
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


def add_book():
    text_authors.place_forget()
    label_authors.place_forget()
    if len(entry_id.get()) != 0 and len(entry_title.get()) != 0 and len(entry_author.get()) != 0 and len(entry_year.get()) != 0 and len(entry_count.get()) != 0:
        buff = entry_id.get()+" : "
        buff += entry_title.get()+" : "
        buff += entry_author.get() + " : "
        buff += entry_year.get() + " : "
        buff += entry_count.get()
        list2.add(buff)
    else:
        print("Введены некорректные данные")
    list2.print()


def print_books(book):
    text_list.configure(state="normal")
    text_list.delete(1.0, tk.END)
    text_list.insert(0.0, book)
    text_list.insert(0.0, '\n')
    text_list.configure(state="disabled")


# region UI
label_name = tk.Label(root, font=12, text="Список книг в библиотеке:", fg='black', bg='white')
label_name.place(relx=0.4, rely=0.051, relwidth=0.50, relheight=0.03)

button_add = tk.Button(root, text="Добавить", bg='#2E8B57', command=lambda: add_book())
button_add.place(relx=0.07, rely=0.40, relwidth=0.20, relheight=0.05)

button_print = tk.Button(root, text="Вывести", bg='#2E8B57', command=lambda: list2.print())
button_print.place(relx=0.07, rely=0.91, relwidth=0.20, relheight=0.05)

button_sort = tk.Button(root, text="Отсортировать", bg='#2E8B57', command=lambda: tree_builder())
button_sort.place(relx=0.07, rely=0.84, relwidth=0.20, relheight=0.05)

button_del = tk.Button(root, text="Удалить", bg='#8A0808', command=lambda: list2.del_lst(entry_del.get()))
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