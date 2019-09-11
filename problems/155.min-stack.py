#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
