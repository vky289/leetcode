class Solution:

    def makesquare(self, matchsticks):
        value = sum(matchsticks)

        if value < 4:
            return False

        if value % 4 != 0:
            return False

        edge = value // 4
        matchsticks.sort(reverse=True)

        def dfs(l1, l2, l3, l4, i):
            if l1 == l2 == l3 == l4 == edge:
                return True

            if i > len(matchsticks) - 1:
                return False

            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False

            return dfs(l1 + matchsticks[i], l2, l3, l4, i+1) or dfs(l1, l2 + matchsticks[i], l3, l4, i+1) or dfs(l1, l2, l3 + matchsticks[i], l4, i+1) or dfs(l1, l2, l3, l4 + matchsticks[i], i+1)

        return dfs(0,0,0,0,0)