import itertools

class Solution_Not_worked:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = {tuple(sorted(triplet)) for triplet in itertools.combinations(nums, 3) if sum(triplet) == 0}
        return [list(triplet) for triplet in triplets]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array to handle duplicates and use two pointers
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate fixed elements

            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for the left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1  # Move left pointer to increase the sum
                else:
                    right -= 1  # Move right pointer to decrease the sum

        return result

nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))
