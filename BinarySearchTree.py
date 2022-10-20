class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self,val,position=50) -> None:
        self.root=Node(val)
        self.position=position
        self.__temp=None
        # self.obj={}
        
    def insert(self,val):
        inserted=False
        self.__temp=self.root
        while not inserted:
            if self.__temp.val > val:
                if self.__temp.left:
                    self.__temp=self.__temp.left
                else:
                    self.__temp.left=Node(val)
                    inserted=True
            else :
                if self.__temp.right:
                    self.__temp=self.__temp.right
                else:
                    self.__temp.right = Node(val)
                    inserted=True
                    
    def display(self,value):
        if value:
            # self.obj.update({pos:value.val})
            print(value.val)
            self.display(value.left)
            self.display(value.right)
            
    # def __show(self,obj):
    #     inserted_len=0
    #     pos="r"
         
        
        