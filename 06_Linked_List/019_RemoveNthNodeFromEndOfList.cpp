/*
Problem: Remove Nth Node From End of List
LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Topic: Linked List
Difficulty: Medium

Approach:
- Two-pointer gap method with a dummy node before head (handles removing the head itself).
- Advance the fast pointer r by n-1 steps first.
- Then move l (from dummy) and r together until r is the last node; l is now just before the target.
- Unlink with l->next = l->next->next.

Time Complexity: O(L)
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* l = new ListNode;
        ListNode* r = new ListNode;
        ListNode* dummy = new ListNode;
        
        dummy->next = head;
        l = dummy;
        r = head;

        for(int i = 0; i < n-1; i++){
            r = r->next;
        }
        while(r->next){
            l = l->next;
            r = r->next;
        }
        
        
            l->next = l->next->next;
        
        
        return dummy->next;

    }
};
