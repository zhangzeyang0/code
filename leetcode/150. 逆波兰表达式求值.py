class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        sign_list = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i not in sign_list:
                stack.append(int(i))
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if i == '+':
                    temp_res = temp2 + temp1
                elif i == '-':
                    temp_res = temp2 - temp1
                elif i == '*':
                    temp_res = temp2 * temp1
                elif i == '/':
                    temp_res = int(temp2 / temp1)
                stack.append(temp_res)
        return stack.pop()
t = Solution()
# print(t.evalRPN(["2", "1", "+", "3", "*"]))
# print(t.evalRPN(["4", "13", "5", "/", "+"]))
print(t.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))



