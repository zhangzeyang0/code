class Solution(object):
    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        利用三数之和的思想，多加一层循环即可
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] > target:
                        r -= 1
                    elif nums[l] + nums[r] + nums[i] + nums[j] < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        r -= 1
                        l += 1
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        可实现2～NSum，利用递归，将NSum转为2Sum
        """
        nums.sort()
        res = []
        self.find_n_sum(nums, target, [], res, 4)
        return res


    def find_n_sum(self, nums, target, temp_res, res, n):
        if not nums or len(nums) < n or n < 2:
            return
        if n == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(temp_res+[nums[l], nums[r]])
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
        else:
            # 递归
            for i in range(0, len(nums)-n+1):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                # 将target减去某个值，然后n-1直到n=2
                self.find_n_sum(nums[i+1:], target-nums[i], temp_res+[nums[i]], res, n-1)
        return

t = Solution()
print(t.fourSum([1, 0, -1, 0, -2, 2], 0))
