# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        index = 0
        for num in nums:
            difference = target - num

            if difference in dict:
                return [index, dict[difference]]
            else:
                dict[num] = index
            
            index += 1
        
        return []
