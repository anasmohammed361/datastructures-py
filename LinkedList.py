class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self._temp1=None
        self._temp2=None

    def add_at_beg(self,val):
        if not self.head:
            self.head=Node(val)
        else:
            self.head,self.head.next=Node(val),self.head

    def add_at_end(self,val):
        if not self.head:
            self.head=Node(val)
        else:
            self._temp1=self.head
            while self._temp1.next:
                self._temp1=self._temp1.next
            self._temp1.next=Node(val)

    def del_from_beg(self):
        if self.head:
            self.head=self.head.next

    def del_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head=None
            return
        self._temp1=self.head
        while self._temp1.next.next:
            self._temp1=self._temp1.next
        self._temp1.next=None

    def display(self):
        self._temp1=self.head
        if self._temp1:
            while self._temp1.next:
                print(self._temp1.val,"->",end=" ")
                self._temp1=self._temp1.next
            print(self._temp1.val)
            
    def sort(self):
        self._temp1=self.head
        while self._temp1.next:
            if self._temp1.val > self._temp1.next.val:
                self._temp1.val,self._temp1.next.val = self._temp1.next.val , self._temp1.val
                self._temp1=self.head
            else : 
                self._temp1=self._temp1.next