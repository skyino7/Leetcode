from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # find the first element that is less than its next element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1


        # 'i' is the index of the first element that is less than its next element
        if i >= 0:
            j = len(nums) - 1
            # find the first element that is greater than nums[i]
            while nums[j] <= nums[i]:
                j -= 1

            # swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the elements after nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            # swap nums[left] and nums[right]
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 6, 5, 4]
    solve = Solution()
    solve.nextPermutation(arr)

    print(*arr)