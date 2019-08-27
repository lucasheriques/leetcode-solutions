class Solution:
    def usernamesSystem(self, u):
        table = {}
        output = []

        for user in u:
            quantity = table.get(user, '')
            name = user + str(quantity)
            table[user] = table[user] + 1 if user in table else 1
            output.append(name)

        return output


q = Solution()
print(q.usernamesSystem(['alex', 'xylos', 'alex', 'alan']))
print(q.usernamesSystem(['bob', 'alice']))
print(q.usernamesSystem(['john', 'john', 'tom', 'john']))
