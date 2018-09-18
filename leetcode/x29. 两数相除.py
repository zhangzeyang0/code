class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = ((dividend > 0) == (divisor > 0))     # 检查是否同号
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = 0
            while dividend >= (divisor << (tmp+1)):    # 二分的思想
                tmp += 1
            dividend -= divisor << tmp
            res += 1 << tmp
        res = res if sign else -res
        return min(max(-2**31, res), 2**31-1)


t = Solution()
print(t.divide(-2147483648, -1))

