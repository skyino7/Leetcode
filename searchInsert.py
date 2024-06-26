class Solution(object):
    """Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index
    where it would be if it were inserted in order."""
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1

        return start
