/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
  int i, j = 0;

  int *arr;

  arr = malloc(sizeof(int) * 2);


  for (i = 0; i < numsSize; i++) {
    for (j = 0; j < numsSize; j++) {
      if (i == j) {
        continue;
      } else if (nums[i] + nums[j] == target) {

        arr[0] = i;
        arr[1] = j;
        *returnSize = 2;

        return arr;
      }
    }

  }
  // *returnSize = 0;

  return (0);

}