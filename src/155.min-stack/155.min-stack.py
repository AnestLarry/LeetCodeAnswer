#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# @lc code=start
class MinStack:
    # Accepted
    # 18/18 cases passed (64 ms)
    # Your runtime beats 99.25 % of python3 submissions
    # Your memory usage beats 5 % of python3 submissions (16.5 MB)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.m = -1
        self.cache = False
        self.L = -1

    def push(self, x: int) -> None:
        if self.L == -1:
            self.m = x
            self.cache = True
        elif self.cache and x < self.m:
            self.m = x
        self.__stack.append(x)
        self.L += 1

    def pop(self) -> None:
        if self.cache and self.__stack[self.L] == self.m:
            self.cache = False
        self.__stack.pop()
        self.L -= 1

    def top(self) -> int:
        return self.__stack[self.L]

    def getMin(self) -> int:
        if not self.cache:
            m = self.__stack[0]
            for i in self.__stack:
                m = i if m > i else m
            self.m = m
            self.cache = True
            return self.m
        else:
            return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
