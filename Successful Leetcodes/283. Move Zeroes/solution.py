def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_ptr = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
            zero_ptr += 1