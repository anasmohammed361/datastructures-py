class Stack:
    def __init__(self) -> None:
        self.stack=[]
        self.top=-1
    
    def push(self,val):
        self.stack.append(val)
        self.top+=1
            

    def show_top(self):
        if self.top > 0:
            return self.stack[self.top]
        return None
        
    def pop(self):
        if self.top >= 0:
            self.top -=1
            return self.stack.pop()
        return None

    def show(self):
        print(*self.stack,sep=" -> ")

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
       
    def exists(self,val):
        return (val in self.stack) 