# Maximum Points You Can Obtain from Cards:

def maxScore(cardPoints,k):
    current_score = sum(cardPoints[:k])
    max_score = current_score
    for i in range(1, k + 1):
        current_score = current_score - cardPoints[k - i] + cardPoints[-i]
        max_score = max(max_score, current_score)
    return max_score
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))
