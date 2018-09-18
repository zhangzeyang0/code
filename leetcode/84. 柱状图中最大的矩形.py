class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        heights.append(-1)
        stack = []
        max_sum = 0
        for i in range(len(heights)):
            if stack and heights[i] < heights[stack[-1]]:

                while len(stack) and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_sum = max(max_sum, h * w)
            stack.append(i)
        return max_sum
t = Solution()
print(t.largestRectangleArea([2,1,5,2,2,2,2,2,2,6]))
