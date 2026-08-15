/*
Problem: Remove Duplicates from Sorted List
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Topic: Linked List
Difficulty: Easy

Approach:
- Single pass; because the list is sorted, duplicates are adjacent.
- When curr->val == curr->next->val, splice out and delete the next node; otherwise advance curr.

Time Complexity: O(n)
Space Complexity: O(1)
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;
        while (curr && curr->next) {
            if (curr->val == curr->next->val) {
                ListNode* temp = curr->next;
                curr->next = temp->next;
                delete temp;
            } else {
                curr = curr->next;
            }
        }
        return head;
    }
};
