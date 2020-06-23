/*
 * @lc app=leetcode id=155 lang=csharp
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
public class MinStack {

    /** initialize your data structure here. */
    // Accepted
    // 18/18 cases passed (152 ms)
    // Your runtime beats 95.03 % of csharp submissions
    // Your memory usage beats 100 % of csharp submissions (35.2 MB)
    public List<int> __Stack = new List<int> ();
    public bool cache = false;
    public int m = -1;
    public MinStack () { }

    public void Push (int x) {
        __Stack.Add (x);
        if (__Stack.Count == 0) {
            m = x;
            cache = true;
        } else if (cache && x < m) {
            m = x;
        }
    }

    public void Pop () {
        if (m == __Stack[__Stack.Count - 1]) {
            cache = false;
        }
        __Stack.RemoveAt (__Stack.Count - 1);
    }

    public int Top () {
        return __Stack[__Stack.Count - 1];
    }

    public int GetMin () {
        if (cache) {
            return m;
        } else {
            int minnum = __Stack[0];
            foreach (int i in __Stack) {
                if (minnum > i) {
                    minnum = i;
                }
            }
            m = minnum;
            cache = true;
            return minnum;
        }

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
// @lc code=end