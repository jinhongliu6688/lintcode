class Solution:
    """
    @param s: the pearl sequences.
    @param k: every k same pearls together will be removed.
    @return: return the pearls after the game.
    """
    def zuma_gaming(self, s: str, k: int) -> str:
        # write your code here.
        stack = []

        for letter in s:
            if not stack or stack[-1][0] != letter:
                stack.append([letter, 1])
            elif stack[-1][0] == letter:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        
        result = ""
        for x in stack:
            result += x[0] * x[1]
        return result
