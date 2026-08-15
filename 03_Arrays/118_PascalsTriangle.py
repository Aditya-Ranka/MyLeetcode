"""
Problem: Pascal's Triangle
LeetCode: https://leetcode.com/problems/pascals-triangle/
Topic: Arrays
Difficulty: Easy

Approach:
- Build row by row starting from [[1]].
- Pad the previous row with a 0 on each side; each new entry is temp[j] + temp[j+1].

Time Complexity: O(numRows^2)
Space Complexity: O(numRows^2) output
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            curr = []
            for j in range(len(res[-1])+1):
                curr.append(temp[j]+ temp[j+1])
            res.append(curr)
        return res
