def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for i in range(1,len(nums)):
            if nums[counter] != nums[i]:
                counter += 1
                nums[counter] = nums[i]
        return counter+1