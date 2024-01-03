class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        memo = {}

        def dfs(string):
            if string in memo:
                return memo[string]

            if not string or len(string) == 0:
                return [""]

            local_res = []

            for w in wordDict:
                if string.startswith(w):
                    sub_words = dfs(string[len(w):])

                    for s_word in sub_words:
                        local_res.append(w + (" " + s_word if s_word else s_word))

            memo[string] = local_res

            return local_res

        return dfs(s)
