class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count = 0
            if count>res:
                res = count
        return res

            