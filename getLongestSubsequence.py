class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [1]*n        # longest length ending at i
        prev = [-1]*n     # previous index in subsequence

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # Find index of maximum dp value
        max_len = max(dp)
        idx = dp.index(max_len)

        # Reconstruct subsequence
        res = []
        while idx != -1:
            res.append(words[idx])
            idx = prev[idx]

        return res[::-1]  # reverse to get correct order
