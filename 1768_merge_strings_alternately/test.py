from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: words with equal length': [
        'abc',
        'pqr',
        'apbqcr'
    ],
    '2: first is shorter': [
        'ab',
        'pqrs',
        'apbqrs'
    ],
    '3: first is longer': [
        'abcd',
        'pq',
        'apbqcd'
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.mergeAlternately(values[0], values[1])
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
