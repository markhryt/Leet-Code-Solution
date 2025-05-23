class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candiesGiven = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candiesGiven[i] = candiesGiven[i-1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and not (candiesGiven[i] >  candiesGiven[i+1]):
                candiesGiven[i] =  candiesGiven[i+1] + 1

        total = 0

        for i in candiesGiven:
            total+= i

        return total

