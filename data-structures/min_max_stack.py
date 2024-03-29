import unittest


class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1][0]

    def pop(self):
        return self.stack.pop()[0]

    def push(self, number):
        self.stack.append(
            (number, min(self.getMin(), number), max(self.getMax(), number)))

    def getMin(self):
        if len(self.stack) > 1:
            return self.stack[-1][1]
        return float('inf')

    def getMax(self):
        if len(self.stack) > 1:
            return self.stack[-1][2]
        return float('-inf')


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(2)
        testMinMaxPeek(self, 2, 2, 2, stack)
        stack.push(7)
        testMinMaxPeek(self, 2, 7, 7, stack)
        stack.push(1)
        testMinMaxPeek(self, 1, 7, 1, stack)
        stack.push(8)
        testMinMaxPeek(self, 1, 8, 8, stack)
        stack.push(3)
        testMinMaxPeek(self, 1, 8, 3, stack)
        stack.push(9)
        testMinMaxPeek(self, 1, 9, 9, stack)
        self.assertEqual(stack.pop(), 9)
        testMinMaxPeek(self, 1, 8, 3, stack)
        self.assertEqual(stack.pop(), 3)
        testMinMaxPeek(self, 1, 8, 8, stack)
        self.assertEqual(stack.pop(), 8)
        testMinMaxPeek(self, 1, 7, 1, stack)
        self.assertEqual(stack.pop(), 1)
        testMinMaxPeek(self, 2, 7, 7, stack)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 2, 2, 2, stack)
        self.assertEqual(stack.pop(), 2)

    def test_case_2(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(8)
        testMinMaxPeek(self, 5, 8, 8, stack)
        stack.push(8)
        testMinMaxPeek(self, 5, 8, 8, stack)
        stack.push(0)
        testMinMaxPeek(self, 0, 8, 0, stack)
        stack.push(8)
        testMinMaxPeek(self, 0, 8, 8, stack)
        stack.push(9)
        testMinMaxPeek(self, 0, 9, 9, stack)
        stack.push(5)
        testMinMaxPeek(self, 0, 9, 5, stack)
        self.assertEqual(stack.pop(), 5)
        testMinMaxPeek(self, 0, 9, 9, stack)
        self.assertEqual(stack.pop(), 9)
        testMinMaxPeek(self, 0, 8, 8, stack)
        self.assertEqual(stack.pop(), 8)
        testMinMaxPeek(self, 0, 8, 0, stack)
        self.assertEqual(stack.pop(), 0)
        testMinMaxPeek(self, 5, 8, 8, stack)
        self.assertEqual(stack.pop(), 8)
        testMinMaxPeek(self, 5, 8, 8, stack)
        self.assertEqual(stack.pop(), 8)
        testMinMaxPeek(self, 5, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)

    def test_case_3(self):
        stack = MinMaxStack()
        stack.push(2)
        testMinMaxPeek(self, 2, 2, 2, stack)
        stack.push(0)
        testMinMaxPeek(self, 0, 2, 0, stack)
        stack.push(5)
        testMinMaxPeek(self, 0, 5, 5, stack)
        stack.push(4)
        testMinMaxPeek(self, 0, 5, 4, stack)
        self.assertEqual(stack.pop(), 4)
        testMinMaxPeek(self, 0, 5, 5, stack)
        self.assertEqual(stack.pop(), 5)
        testMinMaxPeek(self, 0, 2, 0, stack)
        stack.push(4)
        testMinMaxPeek(self, 0, 4, 4, stack)
        stack.push(11)
        testMinMaxPeek(self, 0, 11, 11, stack)
        stack.push(-11)
        testMinMaxPeek(self, -11, 11, -11, stack)
        self.assertEqual(stack.pop(), -11)
        testMinMaxPeek(self, 0, 11, 11, stack)
        self.assertEqual(stack.pop(), 11)
        testMinMaxPeek(self, 0, 4, 4, stack)
        self.assertEqual(stack.pop(), 4)
        testMinMaxPeek(self, 0, 2, 0, stack)
        self.assertEqual(stack.pop(), 0)
        testMinMaxPeek(self, 2, 2, 2, stack)
        self.assertEqual(stack.pop(), 2)
        stack.push(6)
        testMinMaxPeek(self, 6, 6, 6, stack)
        self.assertEqual(stack.pop(), 6)


if __name__ == "__main__":
    unittest.main()
