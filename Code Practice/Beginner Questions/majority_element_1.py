from collections import Counter

test_cases = [
    {"input": [3, 2, 3], "expected": 3},
    {"input": [2, 2, 1, 1, 1, 2, 2], "expected": 2},
    {"input": [1], "expected": 1}
]

def majority_element(nums):
    counts = Counter(nums)
    for n in counts:
        if counts[n] > (len(nums) / 2):
            return n

for case in test_cases:
    result = majority_element(case["input"])
    print(f"Input: {case['input']} | Result: {result} | Pass: {result == case['expected']}")