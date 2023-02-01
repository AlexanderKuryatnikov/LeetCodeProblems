from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1 divisor exists 1': [
        'ABCABC',
        'ABC',
        'ABC'
    ],
    '2 divisor exists 2': [
        'ABABAB',
        'ABAB',
        'AB'
    ],
    '3 divisor is a single char 1': [
        'AAAA',
        'AAA',
        'A'
    ],
    '4 divisor is a single char 2': [
        'AAAA',
        'A',
        'A'
    ],
    '5: no divisor 1': [
        'LEET',
        'CODE',
        ''
    ],
    '6: no divisor 2': [
        'ABABABAD',
        'AB',
        ''
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.gcdOfStrings(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
