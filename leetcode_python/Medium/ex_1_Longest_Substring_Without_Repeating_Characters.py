def length_of_longest_substring(s):
    if not s:
        return 0

    max_length = 0
    start = 0
    seen = {}

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(length_of_longest_substring(s1))  # Output: 3
print(length_of_longest_substring(s2))  # Output: 1
print(length_of_longest_substring(s3))  # Output: 3