class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize with infinity

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Adjust pointers based on the sum
                if current_sum < target:
                    left += 1  # Increase the sum
                elif current_sum > target:
                    right -= 1  # Decrease the sum
                else:
                    # If the exact sum is found, return it immediately
                    return current_sum

        return closest_sum

# Example usage:
nums1 = [-1, 2, 1, -4]
target1 = 1
nums2 = [0, 0, 0]
target2 = 1

sol = Solution()
print(sol.threeSumClosest(nums1, target1))  # Output: 2
print(sol.threeSumClosest(nums2, target2))  # Output: 0