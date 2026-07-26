class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx, val in enumerate(nums):
            otherVal = target - val
            if otherVal in my_dict:
                return [my_dict[otherVal], idx]
            my_dict[val] = idx