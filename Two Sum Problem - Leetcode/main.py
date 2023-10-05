class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map_diff = {}
        for index1 in range(len(nums)):
            comp_to_target = target - nums[index1]
            index2 = hash_map_diff.get(comp_to_target)
            if index2 != comp_to_target:
                hash_map_diff[nums[index1]] = index1
            if index2 != None:
                return [index2, index1]
