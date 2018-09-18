class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        利用栈，反括号出现时上一个正括号一定需要与其配对
        """
        if not s:
            return True
        stack = []
        tdict = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in tdict.values():
                stack.append(i)
            else:
                if len(stack) == 0 or tdict[i] != stack.pop(-1):
                    return False
        return len(stack) == 0
