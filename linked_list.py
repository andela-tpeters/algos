class Node:
  def __init__(self, cargo=None, next=None):
    self.cargo = cargo
    self.next = next

  def __str__(self):
    return str(self.cargo)

  def print_backward(list):
    if list == None: return
    print_backward(list.next)
    print list,

class LinkedList:
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def print_backward_nicely(list) :
    print "[",
    if list != None :
      head = list
      tail = list.next
      print_backward(tail)
      print head,
    print "]",

  def addNode(self, cargo):
    node = Node(cargo)
    if self.length == 1:
      self.head.next = node
    elif self.length > 1:
      self.tail.next = node

    if self.length == 0: self.head = node

    self.length = self.length + 1
    if self.length > 1: self.tail = node


  def getNode(self, number):
    head = self.head
    node = head
    for x in range(1, number):
      if node == None: return None
      node = node.next
    return node

  def find(self, name):
    pass

  def removeNode(self, number):
    node = self.getNode(number)
    if node == None: return None
    next_node = node.next
    previous_node = self.getNode(number - 1)

    if self.length == number:
        self.tail = previous_node

    if((number > 1) and (previous_node != None)):
      previous_node.next = next_node
    elif number == 1:
      self.head = next_node

    node.next = None
    self.length -= 1
    return node

  def print_list(self):
    if self.head == None: return
    node = self.head
    while(node):
      print node
      node = node.next
    print

llist = LinkedList()
llist.addNode("test1")
llist.addNode("test2")
llist.addNode("test3")
llist.addNode("test5")
llist.addNode("test6")
llist.addNode("test7")
llist.addNode("test8")

