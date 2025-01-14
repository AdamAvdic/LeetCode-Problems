class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}  # Dictionary to store numbers and their indices
        for i in range(len(nums)):  # Loop through the list
            complement = target - nums[i]  # Find the complement
            if complement in hash_map:  # Check if complement exists in hash_map
                return [hash_map[complement], i]  # Return indices of the pair
            hash_map[nums[i]] = i  # Store current number and its index