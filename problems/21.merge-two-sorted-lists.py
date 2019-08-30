#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next

            else:
                tail.next, l2 = l2, l2.next

            tail = tail.next

        tail.next = l1 or l2

        return head.next
