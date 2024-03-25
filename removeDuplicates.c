int removeDuplicates(int* nums, int numsSize)
{

    int* arr = malloc(sizeof(int) * numsSize);

    int i, j, k = 1;

    arr[0] = nums[0];

    for (i = 1; i < numsSize; i++)
    {
        if (nums[i-1] != nums[i])
        {
            arr[k] = nums[i];
            k++;
        }
    }

    for (j = 0; j < k; j++)
    {
        // printf("%d", arr[j]);
        nums[j] = arr[j];
    }

    free(arr);

    return (k);

}
