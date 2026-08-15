/*
Problem: Search A 2D Matrix
LeetCode: https://leetcode.com/problems/search-a-2d-matrix/description/
Topic: Binary Search
Difficulty: Medium  

Approach:
- Basic hint was that mentioned time complexity was O(log(m*n)) so we can think of binary search.
- So double binary Search:
    1. rows 
    2. columns


Time Complexity: O(log(m*n))
Space Complexity: O(1) if we don't consider the space for the output array. 
*/


class Solution {
    public:
        bool searchMatrix(vector<vector<int>>& matrix, int target) {
            if (matrix.empty() || matrix[0].empty()) return false;
            int max=matrix.size() -1;
            int n = matrix[0].size();
            int min = 0;
            int x=-1;
            while(min <= max){
                int mid = min + (max-min)/2;
                if(matrix[mid][0] == target){
                    return true;
                }
                if(matrix[mid][0] <= target && matrix[mid][n-1] >= target){
                    x = mid;
                    break;
                }
                if(matrix[mid][0] < target){
                    min = mid+1;
                }
                else{
                    max = mid-1;
                }
            }
            if (x == -1) return false;
            max = matrix[0].size()-1;
            min = 0;
            while(min <= max){
                int mid = min + (max -min)/2;
                if(matrix[x][mid] == target){
                    return true;
                }
                if(matrix[x][mid] < target){
                    min = mid+1;
                }
                else{
                    max = mid-1;
                }
            }
        return false;
    
        }
    };
