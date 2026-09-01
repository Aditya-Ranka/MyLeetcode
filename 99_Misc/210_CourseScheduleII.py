"""
Problem: Course Schedule II
LeetCode: https://leetcode.com/problems/course-schedule-ii/
Topic: Misc
Difficulty: Medium

Approach:
- Create a map from each course to its list of prerequisites
- Define DFS that uses a recursion‑stack set to detect cycles and a visited set for completed nodes
- In DFS, recursively process all prerequisites; if a cycle is found return False
- After processing all prerequisites of a course, add the course to the result list and mark it visited
- Iterate over every course, invoking DFS; if any call returns False, return an empty list
- Return the result list as the course order

Comments:
- Recursive DFS may exceed Python's recursion limit on very deep prerequisite chains
- The result list is built in post‑order, which already yields a valid topological ordering

Time Complexity: O(numCourses+prerequisites)
Space Complexity: O(numCourses+prerequisites)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visit, cycle = set(), set()   
        res = []

        def dfs(crs):
            if crs in cycle:
                return False          
            if crs in visit:
                return True           
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
