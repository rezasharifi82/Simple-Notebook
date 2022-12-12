# In The Name Of God
import re
from copy import deepcopy


class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data
    def __str__(self):
        return str(self.data)


class stack:
    def __init__(self):
        self.head = 0
        self.top = Node()

    def push(self, data):
        self.top.data = data
        self.top.next = Node()
        self.top.next.prev = self.top
        self.top = self.top.next
        self.head += 1

    def pop(self):
        self.top = self.top.prev
        self.top.next = None
        d = self.top.data
        self.head -= 1
        return d


class line_linked_list:
    def __init__(self):
        self.head = 0  # head data to save useful data
        self.fake=Node()
        self.first = Node(None)
        self.first.prev=self.fake
        self.fake.next=self.first
        self.pointer = Node(None)

    def list_to_linked(self, a: list):
        if(len(a)>0):
            self.chlist = a
            self.head = len(a)
            self.first.data = a[0]
            self.pointer = self.first
            for i in a[1:]:
                b = Node(i)
                self.pointer.next = b
                b = self.pointer
                self.pointer = self.pointer.next
                self.pointer.prev = b
        else:
            print("Not enough page! #55")

    @staticmethod
    def merge_two_linear_linked_list(a: __init__, b: __init__):  # concat two list
        b.first.prev = a.pointer.prev
        # a.pointer=a.pointer.prev
        a.pointer.next = b.first
        a.head += b.head
        a.chlist.extend(b.chlist)
        return a

    @staticmethod
    def insert_node(a: Node, b: int, c: __init__):  # a is node b is possition
        # c is linked list of text
        # inplace insert
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.prev.next = a
                a.next = k
                a.prev = k.prev
                k.prev = a
                c.head += 1
                c.chlist.insert(b - 1, a.data)
                if(i==1):
                    c.first=c.first.prev
                break
            else:
                k = k.next
        else:
            print("Not found that index! #error1058")

    @staticmethod
    def remove_node(b: int, c: __init__):
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.prev.next = k.next
                k.next.prev = k.prev
                c.head -= 1
                c.chlist.pop(b - 1)
                if(i==1):
                    c.first=c.first.next
                break
            else:
                k = k.next
        else:
            print("Not found that line! #error1076")

    @staticmethod
    def replace_node(a: str, b: int, c: __init__):
        # a is string data
        # b is position
        # c is linked list
        # inplace replace
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                k.data = a
                c.chlist[b - 1] = a
                break
            else:
                k = k.next
        else:
            print("Not found that line! #error1095")

    @staticmethod
    def swap_node(a: int, b: int, c: __init__):
        # a is int
        # b is second one
        # c is linked list
        # inplace replace
        a, b = min(a, b), max(a, b)
        an = None
        bn = None
        i = 0
        k = c.first
        while (k != None):
            i += 1
            if (i == b):
                bn = k
                an.data, bn.data = bn.data, an.data
                c.chlist[a - 1], c.chlist[b - 1] = c.chlist[b - 1], c.chlist[a - 1]
                break
            elif (i == a):
                an = k
                k = k.next
            else:
                k = k.next
        else:
            print("Not found that line! #error1095")


    def __str__(self):
        m=self

        k=self.first
        s=""
        while(k!=None):
            s+=str(k.data)+"\n"
            k=k.next
        return s
    def __len__(self):
        k=self.first
        i=0
        while(k!=None):
            i+=1
            k=k.next
        return i

class Page:
    sep = "\s\$\s|\s\$"

    def __init__(self, text):
        self.text = text
        self.prev_page = None
        self.next_page = None
        self.total_lines = self.count_lines()
        linear_list = self.line_list()
        self.linked_list_of_lines = line_linked_list()
        self.linked_list_of_lines.list_to_linked(linear_list)

    def count_lines(self):
        r = str(self.text).count("\n")
        r = int(r)
        return r

    def parse_page(self):
        return self.text

    def line_list(self):
        pa = "\n"
        b = re.split(pa, self.text)
        return b

    def find_in_page(self, s: str):  #find
        i = 0
        fin = []
        z=0
        k = self.linked_list_of_lines.first
        while (k != None):
            if (s in k.data):
                z+=str(k.data).count(s)
                fin.append(("Page line number: "+str(i+1), "Full text: " +str(k.data)))
            i += 1
            k = k.next
        return (z,fin)

    def repfind_in_page(self, s: str, c: str):  #replace and find
        k = self.linked_list_of_lines.first
        i = 0
        while (k != None):
            if (s in k.data):
                k.data = str(k.data).replace(s, c)
                self.linked_list_of_lines.chlist[i] = k.data

            k = k.next
            i += 1

    @staticmethod
    def make_it_new_page(text=None):
        temp = Page()
        temp.text = str(text) + Page.sep
        return temp

    def __str__(self):
        return str(self.linked_list_of_lines)



def read_text_from_terminal():
    b = line_linked_list()
    a = []
    while ((s := input()) != "$finishtyping"):
        a.append(s)
    b.list_to_linked(a)
    return b
    # return first Node


class whole_file:
    # first page could handle all the file wihtout problem
    def __init__(self, path=None):  # contains parse method
        r = self.file_input_get(path)
        self.first_page = Page(r[0])
        self.path=path
        self.current_page = self.first_page
        self.file_pointer = self.first_page
        # self.fake=Page("itis\n$\nfake")
        self.total_page = len(r)
        self.page_number = 1
        self.first_page.prev_page=None
        self.actions = stack()
        self.redo = stack()
        r=r[1:]
        for i in r:
            self.file_pointer.next_page = Page(i)
            self.file_pointer.next_page.prev_page = self.file_pointer
            self.file_pointer = self.file_pointer.next_page

        self.now_we_run_the_program()
    def __str__(self):
        m=self
        k=self.first_page
        s=""
        while(k!=None):
            s+=str(k)+"$\n"
            k=k.next_page
        return s

    def add_undo(self):
        d = deepcopy((self.page_number, self.current_page.linked_list_of_lines))
        self.actions.push(d)
    def add_redo(self):
        d = deepcopy((self.page_number, self.current_page.linked_list_of_lines))
        self.redo.push(d)
    def Just_Do_It(self,that:tuple):
        n=int(that[0])
        that=that[1]
        i=1
        k=self.first_page
        while(k!= None):
            if(i==n):
                k.linked_list_of_lines=that

                break
            else:
                i+=1
                k=k.next_page

    def now_we_run_the_program(self):
        s = ""

        while (s != "$exit"):
            print("page number: {}".format(self.page_number))
            self.current_page.total_lines = len(self.current_page.linked_list_of_lines)

            s = input()
            if (s.startswith("$")):  # it is a command
                if ("nextpage" in s):
                    self.page_number += 1
                    if (self.page_number <= self.total_page):
                        self.current_page = self.current_page.next_page
                    else:
                        print("No more page!")
                        self.page_number -= 1
                elif ("previouspage" in s):
                    self.page_number -= 1
                    if (self.page_number > 0):
                        self.current_page = self.current_page.prev_page
                    else:
                        self.page_number += 1
                        print("No more page is available!")
                elif ("where" in s):
                    print("We are at page number {}".format(self.page_number))
                elif ("lines" in s):
                    print(self.current_page.total_lines)

                elif ("show" in s):
                    nes = s.strip()
                    patt = "(\d+)"
                    n = re.search(patt, nes).group()
                    n = int(n)
                    the_lines = self.current_page.linked_list_of_lines.chlist
                    print(the_lines[n-1])
                elif ("append" in s):
                    p = read_text_from_terminal()
                    self.add_undo()
                    # self.current_page.linear_list.extend(p.chlist)
                    self.current_page.linked_list_of_lines = line_linked_list.merge_two_linear_linked_list(
                        self.current_page.linked_list_of_lines, p)
                elif ("insert" in s):  # insert one line
                    self.add_undo()
                    nes = s.strip()
                    patt = "insert\((.+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    n = int(a[1])
                    text = (a[0])
                    a = Node(text)
                    line_linked_list.insert_node(a, n, self.current_page.linked_list_of_lines)
                elif ("remove" in s):
                    self.add_undo()
                    nes = s.strip()
                    patt = "(\d+)"
                    a = re.search(patt, s).group()
                    a = int(a)
                    line_linked_list.remove_node(a, self.current_page.linked_list_of_lines)
                elif ("replace" in s):  # String and line number
                    self.add_undo()
                    nes = s.strip()
                    patt = "replace\((.+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    n = int(a[1])
                    text = (a[0])
                    line_linked_list.replace_node(text, n, self.current_page.linked_list_of_lines)
                elif ("swap" in s):
                    self.add_undo()
                    nes = s.strip()
                    patt = "swap\((\d+),(\d+)\)"
                    a = re.search(patt, s).groups()
                    b = int(a[0])
                    c = int(a[1])
                    line_linked_list.swap_node(b, c, self.current_page.linked_list_of_lines)
                elif ("find" in s):
                    op = self.first_page
                    nes = s.strip()
                    i = 0
                    patt = "find\((.+)\)"
                    a = re.search(patt, s).groups()
                    finder = []
                    tot=0
                    while (op != None):
                        i += 1
                        r = Page.find_in_page(op, a[0])
                        z=r[0]
                        tot+=z
                        r=r[1]
                        finder.extend(["#####","In Page: "+str(i),"We've {} Option".format(z) ,r,"............................"])
                        op = op.next_page

                    if (len(finder) <= 0):
                        print("Not found! #error276")
                    else:
                        # print(len(finder))
                        print(*finder,sep="\n",end="\n")
                        print("In total we have {} options".format(tot))
                elif ("far" in s):
                    self.add_undo()
                    op = self.first_page
                    nes = s.strip()
                    patt = "far\((.+),(.+)\)"
                    a = re.search(patt, s).groups()
                    while (op != None):
                        Page.repfind_in_page(op, a[0], a[1])
                        op = op.next_page
                    print("Mission Passed!")
                elif ("undo" in s):
                    if(self.actions.head>0):
                        self.add_redo()
                        self.Just_Do_It(self.actions.pop())
                    else:
                        print("Not enough actions!#371")
                elif("redo" in s):
                    if (self.redo.head > 0):
                        self.add_undo()
                        self.Just_Do_It(self.redo.pop())
                    else:
                        print("Not enough actions!#377")
                elif("save" in s):
                    o=str(self)
                    print("#######################\n\n")
                    print(o)
                    print("\n\n #######################")
                    i=open(self.path,"w")
                    i.write(o)
                    # s="$exit"











            else:
                print("Not a command!")

        else:
            self.file.close()
            return 0

    def create_linked_mode(self, text=None):  # seperate all those pages
        rege = Page.sep
        flist = re.split(rege, text)
        return flist[:-1]

    def file_input_get(self, file_path):
        self.file = open(file_path, 'r+')
        text = self.file.read()
        r = self.create_linked_mode(text)
        return r
path = "./w.txt"
whole_file(path)
