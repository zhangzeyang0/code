class Solution(object):
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        循环处理
        """
        if not digits:
            return []
        tdict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
                 '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        if len(digits) == 1:
            return tdict[digits]
        res = [one for one in tdict[digits[0]]]
        for i in digits[1:]:
            for j in range(len(res)):
                temp = res.pop(0)
                for k in tdict[i]:
                    res.append(temp+k)
        return res

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        递归
        """
        if not digits:
            return []
        tdict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
                 '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        if len(digits) == 1:
            return tdict[digits]
        pre = self.letterCombinations(digits[:-1])
        last = tdict[digits[-1]]
        return [i+j for i in pre for j in last]

t = Solution()
print(t.letterCombinations('233'))
