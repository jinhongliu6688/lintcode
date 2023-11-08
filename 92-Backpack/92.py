from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        if m <= 0 or len(a) <= 0:
            return 0

        result = [0 for i in range(m + 1)]
        for w in a:
            for i in range(m, -1, -1):
                if i >= w:
                    result[i] = max(result[i - w] + w, result[i])
        
        return result[m]
