class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        turn = True

        while remove > 0 and n >= remove:
            n -= remove
            remove -= 1
            turn = not turn
        return not turn
        