class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # If the list is empty
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Shorten the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  # If prefix becomes empty, return ""
                    return ""

        return prefix



solution = Solution()

# Test cases
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print(solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(solution.longestCommonPrefix([""]))                         # Output: ""
print(solution.longestCommonPrefix(["a"]))                        # Output: "a"
