from typing import List


def smallest_missing_positive_integer(nums: List[int]) -> int:
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """

   
    nums = [num for num in nums if num > 0]
    
    if not nums:
        return 1
    
    nums.sort()
    
    
    smallest_missing = 1
    for num in nums:
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            return smallest_missing
    
    return smallest_missing










    



  

