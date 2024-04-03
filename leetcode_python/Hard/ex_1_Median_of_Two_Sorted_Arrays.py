def two_arrs_median(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 == 0:
        # print([1,2,3]//2)
        return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
    else:
        return nums1[len(nums1) // 2]

print(two_arrs_median([1, 3], [2, 4]))
