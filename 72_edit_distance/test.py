from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        'horse',
        'ros',
        3
    ],
    '2: leetcode example 2': [
        'intention',
        'execution',
        5
    ],
    '3: first string empty': [
        '',
        'abc',
        3
    ],
    '4: second string empty': [
        'abc',
        '',
        3
    ],
    '5: both strings empty': [
        '',
        '',
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minDistance(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
