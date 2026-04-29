# The Test Data
test_cases = [
    {"input": [2, 2, 1], "expected": 1},
    {"input": [4, 1, 2, 1, 2], "expected": 4},
    {"input": [1], "expected": 1},
    {"input": [7, 3, 5, 3, 7], "expected": 5}
]

def single_number(nums):
    if len(nums) == 0:
        return None
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for n in count:
        if count[n] == 1:
            return n


# The Test Runner
for case in test_cases:
    result = single_number(case["input"])
    print(f"Input: {case['input']} | Result: {result} | Pass: {result == case['expected']}")
