class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        
class BinaryTree:
    def __init__(self,val):
        self.root=Node(val)
        self.level=1
        self.no_by_level=3
        self._temp_level=None
        self.no_of_elements=1
        self.__inserted=False
    
    def _check_level(self):
        if self.no_by_level == self.no_of_elements:
            self.level+=1
            self.no_by_level+=2**self.level

    
    def _insert_by_level(self,node,val,req_level,cur_level=0):
        if self.__inserted:
            return
        
        if cur_level == req_level-1:
            if  node.left == None:
                node.left=Node(val)
                self.no_of_elements+=1
                self.__inserted=True
                
            elif  node.right == None:
                node.right=Node(val)
                self.no_of_elements+=1
                self.__inserted=True
                
        elif cur_level>=req_level:
            return
        
        else:
            if node.left:
                self._insert_by_level(node.left,val,req_level,cur_level+1)
            if node.right:
                self._insert_by_level(node.right,val,req_level,cur_level+1)



    def insert(self,val):
        self.__inserted=False
        self._insert_by_level(self.root,val,self.level)
        self._check_level()

    def display(self,node):
        if node:
            print(node.val)
            self.display(node.left)
            self.display(node.right)