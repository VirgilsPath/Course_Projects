# Standard case: mixed zeros and numbers
test_1 = [0, 1, 0, 3, 12] 
# Expected: [1, 3, 12, 0, 0]

# All zeros: nothing should change
test_2 = [0, 0, 0]
# Expected: [0, 0, 0]

# No zeros: nothing should change
test_3 = [4, 5, 6]
# Expected: [4, 5, 6]

# Zero at the very end
test_4 = [1, 2, 0]
# Expected: [1, 2, 0]

# Multiple zeros at the beginning
test_5 = [0, 0, 1]
# Expected: [1, 0, 0]

def move_zeroes(nums):
    if nums == []:
        return None
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
move_zeroes(test_1)
print(test_1)