class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        想法同三数之和，排序之后计算三数之和，记录最小和，若结果大于target则r-1，若结果小于target则l+1
        """
        if not nums or len(nums) < 3:
            return
        nums.sort()
        flag = abs(target - sum(nums[:3]))
        res = 0
        for i in range(len(nums)):
            #print(i,'#####')
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                #print(nums[l] + nums[r] + nums[i])
                if abs((nums[l] + nums[r] + nums[i] - target)) <= flag:
                    flag = abs((nums[l] + nums[r] + nums[i] - target))
                    res = nums[l] + nums[r] + nums[i]
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                if nums[l] + nums[r] + nums[i] > target:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < target:
                    l += 1
                else:
                    return target
        return res
t = Solution()
print(t.threeSumClosest([0,2,1,-3], 1))
