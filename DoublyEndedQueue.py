class Dequeue:
    def __init__(self) -> None:
        self.queue=[]
        
    def enrear(self,val):
        self.queue.append(val)
        
    def enfront(self,val):
        self.queue.insert(0,val)
    
    def derear(self):
        if self.queue:
            return self.queue.pop()
        
    def defront(self):
        if self.queue:
            return self.queue.pop(0)
    
    def peek(self):
        print(*self.queue,sep=" -> ")