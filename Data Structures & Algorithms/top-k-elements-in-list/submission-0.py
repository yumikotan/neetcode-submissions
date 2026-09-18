class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hash map to store numbers and its count
        count = {}

        for num in nums:
            if num in count:
                count[num] = count[num]+1
            else:
                count[num]=1
        
        sorted_nums = sorted(count, key = count.get, reverse=True)
        return sorted_nums[:k]