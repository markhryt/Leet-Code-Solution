class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        hindex = 0

        for i in range(len(citations)):
            if citations[i] > hindex:
                if len(citations) - i >= citations[i]:
                    hindex = citations[i]
                else:
                    hindex = max(hindex, len(citations) - i)

        return hindex
