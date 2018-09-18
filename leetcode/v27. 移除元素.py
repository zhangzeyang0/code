class Solution(object):
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        遍历一遍，利用pop直接删除
        """
        start = 0
        while start < len(nums):
            if nums[start] == val:
                nums.pop(start)
            else:
                start += 1
        return len(nums), nums

    def removeElement(self, nums, val):
        idx1 = 0
        idx2 = len(nums)-1
        while idx1 <= idx2:
            if nums[idx1] == val:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx2 -= 1
            else:
                idx1 += 1
        return idx2 + 1, nums[:idx2+1]


t = Solution()
print(t.removeElement([0,1,2,2,3,0,4,2], 2))

