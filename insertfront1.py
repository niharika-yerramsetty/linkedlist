
#inserting a node to liinked list at front
class node:
   def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
   def __init__(self):
     self.head=None
   def push(self,data):
    new_node=node(data)
    self.head=new_node
    
   def printlist(self):
      lastnode= self.head
      lastnode.next=first
      while (lastnode):
         print(lastnode.data)
         lastnode=lastnode.next
        
      
      
llist=LinkedList()
llist.push(10)
first=node(5)
second=node(17)
first.next=second
llist.printlist()
         




    
