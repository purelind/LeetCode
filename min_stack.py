class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.q.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.q:
            return None
        else:
            return self.q[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.q:
            return None
        else:
            return self.q[-1][1]


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()