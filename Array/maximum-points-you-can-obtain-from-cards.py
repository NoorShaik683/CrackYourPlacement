class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum = 0
        for i in range(k):
            curr_sum += cardPoints[i]
        if k==len(cardPoints):
            return curr_sum
        right = len(cardPoints)-1
        max_sum=curr_sum
        for i in range(k-1,-1,-1):

            curr_sum = (curr_sum-cardPoints[i])+cardPoints[right]

            if curr_sum>max_sum:
                max_sum=curr_sum
            right-=1
        return max_sum
