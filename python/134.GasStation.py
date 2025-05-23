class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalSum = 0
        start = 0
        currentSum = 0

        for i in range(len(gas)):
            totalSum += (gas[i]- cost[i])

            if currentSum < 0:
                start = i
                currentSum = (gas[i]- cost[i])
                continue

            currentSum += (gas[i]- cost[i])

        if totalSum < 0:
            return -1
        else:
            return start

