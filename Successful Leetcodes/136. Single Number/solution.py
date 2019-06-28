def singleNumber(self, nums: List[int]) -> int:
    countTracker = {}
    
    for num in nums:
        if num not in countTracker:
            countTracker[num] = 1
        else:
            countTracker[num] += 1
            
    for key, val in countTracker.items():
        if val == 1:
            return key