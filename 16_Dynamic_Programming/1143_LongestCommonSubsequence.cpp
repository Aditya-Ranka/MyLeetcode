/*
Problem: Longest Common Subsequence
LeetCode: https://leetcode.com/problems/longest-common-subsequence/description/
Topic: Dynamic Programming, String
Difficulty: Medium  

Approach:
- Use dynamic programming with a 2D array where dp[i][j] represents the length of LCS
  of text1[0..i-1] and text2[0..j-1]
- Fill the array from bottom-right to top-left
- If characters match: dp[i][j] = 1 + dp[i+1][j+1]
- If characters don't match: dp[i][j] = max(dp[i+1][j], dp[i][j+1])
- Return dp[0][0] which contains the length of LCS of the entire strings

Time Complexity: O(m * n) where m and n are lengths of text1 and text2
Space Complexity: O(m * n)
*/


class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            int m = text1.size();
            int n = text2.size();
            vector<vector<int>> arr(m + 1, vector<int>(n + 1, 0));
            for (int i = 0; i < n; i++){
                arr[m][i] = 0;
            }
            for (int i = 0; i < m; i++){
                arr[i][n] = 0;
            }
            for(int i = m-1 ; i >= 0; i--){
                for (int j = n-1 ; j>=0;j--){
                    if (text1[i] == text2[j]){
                        arr[i][j] = 1 + arr[i+1][j+1];
                    }
                    else{
                        arr[i][j] = max(arr[i+1][j], arr[i][j+1]);
                    }
                }
            }
            return arr[0][0];
        }
    };
