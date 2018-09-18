class Solution(object):
    def generateParenthesis(self, n):
        res = self.generate('', n, n, [])
        return res

    def generate(self, p, left, right, parens):
        if left:
            self.generate(p + '(', left-1, right, parens)
        if right > left:
            self.generate(p + ')', left, right-1, parens)
        if not right:
            parens.append(p)
        return parens

t = Solution()
print(t.generateParenthesis(2))
