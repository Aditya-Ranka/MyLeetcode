"""
Problem: Min Stack
LeetCode: https://leetcode.com/problems/min-stack/
Topic: Stack and Queues
Difficulty: Medium

Approach:
- Initialize empty list to hold (value,current_min) pairs
- On push compute new min as min(value, previous min) and append pair
- Pop removes last pair
- Top returns value part of last pair
- getMin returns min part of last pair

Comments:
- Methods assume stack is non‑empty; pop/top/getMin will raise IndexError on empty stack

Time Complexity: O(1)
Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        self.stack = []   

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
