import java.awt.List;

/*
 * @lc app=leetcode.cn id=155 lang=java
 *
 * [155] Min Stack
 */
// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.

// Example:

// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin();   --> Returns -3.
// minStack.pop();
// minStack.top();      --> Returns 0.
// minStack.getMin();   --> Returns -2.
// @lc code=start
class MinStack {
    // Accepted
    // 18/18 cases passed (7 ms)
    // Your runtime beats 79.23 % of java submissions
    // Your memory usage beats 14.46 % of java submissions (41.7 MB)
    public List<Integer> myStack = new LinkedList<Integer>();
    public Boolean cache = false;
    public int m = -1;

    /** initialize your data structure here. */
    public MinStack() {
    }

    public void push(int x) {
        if (myStack.size() == 0) {
            m = x;
            cache = true;
        } else if (cache && x < m) {
            m = x;
        }
        myStack.add(x);
    }

    public void pop() {
        if (cache && myStack.get(myStack.size() - 1) == m) {
            cache = false;
        }
        myStack.remove(myStack.size() - 1);
    }

    public int top() {
        return myStack.get(myStack.size() - 1);
    }

    public int getMin() {
        if (cache) {
            return m;
        } else {
            int n = myStack.get(0);
            for (int i : myStack) {
                if (i < n) {
                    n = i;
                }
            }
            m = n;
            cache = true;
            return m;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(x); obj.pop(); int param_3 = obj.top(); int param_4
 * = obj.getMin();
 */
// @lc code=end
