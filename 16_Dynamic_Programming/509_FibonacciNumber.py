"""
Problem: Fibonacci Number
LeetCode: https://leetcode.com/problems/fibonacci-number/
Topic: Dynamic Programming
Difficulty: Easy

Approach:
- Plain recursion straight off F(n) = F(n-1) + F(n-2) with base cases.

Comments:
- Exponential without memoization; an iterative/DP version is O(n). n=0 and n=1 handled explicitly.

Time Complexity: O(2^n) (naive recursion)
Space Complexity: O(n) recursion depth
"""

class Solution:
    def fib(self, n: int) -> int:
        #F(1) = 1
        # F(2) = 1
        #F(3) = 2
        if n==1:
            return 1
        if n==0:
            return 0
        def fibb(n):
            if n ==3:
                return 2
            if n==2:
                return 1
            
            else:
                return fibb(n-1) + fibb(n-2)

        return fibb(n)
