"""
Problem: Course Schedule
LeetCode: https://leetcode.com/problems/course-schedule/
Topic: Misc
Difficulty: Medium

Approach:
- Initialize a map from each course to its list of prerequisite courses
- Populate the map using the given prerequisites list
- Define a recursive dfs that detects cycles using a visited set and memoizes safe courses by clearing their prerequisite list
- For each course, invoke dfs; if any call returns false, a cycle exists
- Return true only if all courses are processed without detecting a cycle

Comments:
- The code clears premap[crs] after confirming the course has no cycles, effectively memoizing results and avoiding re‑processing
- Recursive depth may hit Python's recursion limit on very deep prerequisite chains

Time Complexity: O(numCourses + len(prerequisites))
Space Complexity: O(numCourses + len(prerequisites))
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        visit = set()
        x = 0
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs] == []:
                return True
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            premap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
