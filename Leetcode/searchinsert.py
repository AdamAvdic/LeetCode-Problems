def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #left pointer nums[0]
        leftptr = 0
        #right pointer nums[size]
        rightptr = len(nums)-1 

        while(rightptr>=leftptr):
            #midpoint calculation
            midpoint = leftptr + (rightptr-leftptr) // 2
            #midpoint is the target!
            if nums[midpoint] == target:
                return midpoint
            #midpoint > target, reduce rightptr
            elif nums[midpoint] > target:
                rightptr = midpoint - 1
            else:
                leftptr = midpoint + 1
        return leftptr