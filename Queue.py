class Queue:
    def __init__(self) -> None:
        self.queue=[]
        
    def enqueue(self,val):
        self.queue.append(val)
        
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("No elements present")
    
    def peek(self):
        print(*self.queue,sep=" -> ")