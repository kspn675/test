class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target not in nums:
                return -1
            else:
                return nums.index(target)