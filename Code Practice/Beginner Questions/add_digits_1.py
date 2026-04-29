test_cases = [
    {"input": 38, "expected": 2},
    {"input": 0, "expected": 0},
    {"input": 9, "expected": 9},
    {"input": 123, "expected": 6} # 1+2+3 = 6
]

def add_digits(num):
    while num > 9:
        num = (num // 10) + (num % 10)  
    return num
    
for case in test_cases:
    result = add_digits(case["input"])
    print(f"Input: {case['input']} | Result: {result} | Pass: {result == case['expected']}")