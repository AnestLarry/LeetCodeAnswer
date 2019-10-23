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

class MinStack2:
    # Accepted
    # 18/18 cases passed (844 ms)
    # Your runtime beats 8.63 % of python3 submissions
    # Your memory usage beats 5.36 % of python3 submissions (17.6 MB)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []

    def push(self, x: int) -> None:
        self.__stack += [x]

    def pop(self) -> None:
        return self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return min(self.__stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

# Fail Code
# class MinStack:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.__root = node(0, None)
#         self.__cur = None
        

#     def push(self, x: int) -> None:
#         if not self.__cur:
#             self.__cur = node(x, self.__root)
#             self.__root.next = self.__cur
#         self.__cur.next = node(x, self.__cur)
#         self.__cur = self.__cur.next

#     def pop(self) -> None:
#         if self.__cur != None:
#             res = self.__cur.val
#             self.__cur = self.__cur.prev
#             self.__cur.next = None
#             return res
#         else:
#             return None

#     def top(self) -> int:
#         if self.__cur:
#             return self.__cur.val
#         else:
#             return None

#     def getMin(self) -> int:
#         cur = self.__root
#         cur = cur.next
#         res = None
#         while cur:
#             if not res:
#                 res = cur.val
#             else:
#                 if res > cur.val:
#                     res = cur.val
#             cur = cur.next
#         return res


# class node:
#     def __init__(self, x: int, prev):
#         self.val: int = x
#         self.prev = None
#         self.next = None
