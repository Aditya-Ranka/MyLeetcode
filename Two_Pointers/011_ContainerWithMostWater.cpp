/*
Problem: Container With Most Water
LeetCode: https://leetcode.com/problems/container-with-most-water/description/
Topic: Two Pointers
Difficulty: Medium  

Approach:
- We use two pointers to find the maximum area.
- We move the pointer that points to the shorter line inward.
- We calculate the area and update the maximum area if the current area is greater.
- We return the maximum area.

- Basic application of L and R pointers. 



Time Complexity: O(n)
Space Complexity: O(1)
*/



class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int maxH = 0;
        while(l<r){
            if(height[l]>height[r]){
                if(maxH < height[r]*(r-l)){
                    maxH = height[r]*(r-l);
                }
                r--;
            }
            else{
                if(maxH < height[l]*(r-l)){
                    maxH = height[l]*(r-l);
                }
                l++;   
            }
        }
        return maxH;
    }
};

