class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = float('inf')
        # Loops through tops[0] or bottoms[0]
        for i in (tops[0], bottoms[0]):
            isValid = True
            swapTopCnt, swapBottomCnt = 0, 0
            for top, bottom in zip(tops, bottoms):
                if top == i and bottom == i:
                    continue
                # Count if we have to  Swap Top to Bottom
                elif top == i:
                    swapTopCnt += 1
                # Count if we have to  Swap Bottom to Top
                elif bottom == i:
                    swapBottomCnt += 1
                # If not valid, don't update res
                else:
                    isValid = False
                    break
            # Check whether make all top value equal, or bottom value equal takes minimum swaps
            if isValid:
                res = min(res, swapTopCnt, swapBottomCnt)
                
        return res if res != float('inf') else -1
