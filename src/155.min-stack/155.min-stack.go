/*
 * @lc app=leetcode.cn id=155 lang=golang
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

type MinStack struct {
	Cache bool
	M     int
	Stack []int
	L     int
}

// Accepted
// 18/18 cases passed (16 ms)
// Your runtime beats 95.5 % of golang submissions
// Your memory usage beats 75 % of golang submissions (7.5 MB)
/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{Cache: false, M: -1, Stack: make([]int, 0), L: -1}
}

func (this *MinStack) Push(x int) {
	this.Stack = append(this.Stack, x)
	if this.L == -1 {
		this.M, this.Cache = x, true
	} else if this.Cache && x < this.M {
		this.M = x
	}
	this.L++
}

func (this *MinStack) Pop() {
	if this.Cache && this.Stack[this.L] == this.M {
		this.Cache = false
	}
	this.Stack = this.Stack[:this.L]
	this.L--
}

func (this *MinStack) Top() int {
	return this.Stack[this.L]
}

func (this *MinStack) GetMin() int {
	if this.Cache {
		return this.M
	} else {
		m := this.Stack[0]
		for _, i := range this.Stack {
			if i < m {
				m = i
			}
		}
		this.M = m
		this.Cache = true
		return m
	}
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end
