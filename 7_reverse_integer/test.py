from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: positive number': [
        123,
        321
    ],
    '2: negative number': [
        -123,
        -321
    ],
    '3: round number': [
        1200,
        21
    ],
    '4: negative round number': [
        -1200,
        -21,
    ],
    '5: zero': [
        0,
        0
    ],
    '6: outside 32-bit integer range': [
        pow(2, 32),
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.reverse(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
