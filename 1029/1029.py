class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        costs.sort(key = lambda x: x[0]-x[1])

        t_t = 0
        cost_length = len(costs)
        for i in range(cost_length//2):
            t_t += costs[i][0] + costs[cost_length-i-1][1]
        return t_t
