class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 与上一位一样则跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                # 排序数组，大于0则右边减1，小于0则左边加1
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:

                    res.append([nums[i], nums[l], nums[r]])
                    # 相同的数跳过
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
        return res

t = Solution()
print(t.threeSum([-1, 0, 1, 2, -1, -4]))
