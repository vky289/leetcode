class Solution:
    def __init__(self):
        self.coins = []
        self.counter = []

    def find_min_coins(self, rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0

        if self.counter[rem-1] != float('inf'):
            return self.counter[rem-1]

        minimum = float('inf')

        for s in self.coins:
            result = self.find_min_coins(rem - s)
            if result >= 0 and result < minimum:
                minimum = 1 + result

        self.counter[rem - 1] = minimum if minimum != float('inf') else -1

        return self.counter[rem-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.counter = [float('inf')]*amount
        if amount < 1:
            return 0

        return self.find_min_coins(amount)
