from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: zero': [
        0,
        0
    ],
    '2: one digit': [
        5,
        5
    ],
    '3: two digits': [
        38,
        2
    ],
    '4: multiple digits 1': [
        384567367,
        4
    ],
    '5: multiple digits 2': [
        126,
        9
    ],
    '6: multiple digits 3': [
        127,
        1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.addDigits(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
