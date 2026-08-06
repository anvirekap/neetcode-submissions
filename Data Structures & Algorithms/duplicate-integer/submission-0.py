class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                count += 1
                if count >= 1:
                    break
        
        if count >= 1:
            return True
        return False