class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minStack:
            self.minStack.append(val)
            
        else: 
            self.minStack.append(min(val, self.minStack[-1]))
        return None
           
        # temp_val = val
        # for idx, val enumerate(self.arr):
        #     self.arr[idx], temp_val = temp_val, self.arr[idx + 1]
        # return None


    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()
        return None

        

    def top(self) -> int:
        return None if not self.arr else self.arr[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
