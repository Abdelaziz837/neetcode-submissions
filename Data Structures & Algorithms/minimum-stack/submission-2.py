class MinStack:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, val: int) -> None:
        
        self.l1.append(val)

        if self.l2 :
           last_item = self.l2[-1]

        else:
            last_item = math.inf   

        if last_item >= val:
            self.l2.append(val)

        
    def pop(self) -> None:
        lastitem1 = self.l1[-1]
        lastitem2 = self.l2[-1]

        del self.l1[-1]

        if lastitem1 == lastitem2:
            del self.l2[-1]


    def top(self) -> int:
        last_item = self.l1[-1]

        return last_item

    def getMin(self) -> int:

        return self.l2[-1]
        
