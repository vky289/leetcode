class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1
        else:
            start_index, gas_cost = 0, 0
            for i in range(len(gas)):
                gas_cost += (gas[i] - cost[i])

                if gas_cost < 0:
                    gas_cost = 0
                    start_index = i + 1

            return start_index
