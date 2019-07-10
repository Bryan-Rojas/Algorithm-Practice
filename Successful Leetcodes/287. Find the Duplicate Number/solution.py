def findDuplicate(self, nums: List[int]) -> int:
    temp = set()
    
    for num in nums:
        if num not in temp:
            temp.add(num)
        else:
            return num