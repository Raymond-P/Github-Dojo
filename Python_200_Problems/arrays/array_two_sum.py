# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution

# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].


def two_sum(nums, target):

    # assuming nums is not empty
    for A, first_number in enumerate(nums):
        for B, second_number in enumerate(nums):
            if first_number + second_number == target:
                return [A, B]
