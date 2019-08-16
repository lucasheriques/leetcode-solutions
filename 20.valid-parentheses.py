#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []

        table = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in table:
                stack.append(table[char])

            elif char == ')' or char == ']' or char == '}':
                if len(stack) == 0 or char != stack.pop():
                    return False

        return len(stack) == 0
