#!/usr/bin/python3
"""
find the peak in an unordered list of
integers
"""
from typing import List, Optional

def find_peak(list_of_integers: List[int]) -> Optional[int]:
    """
    Find the peak in a list of integers.
    
    Args:
        list_of_integers (List[int]): List of integers.
        
    Returns:
        Optional[int]: The peak integer(s).
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
