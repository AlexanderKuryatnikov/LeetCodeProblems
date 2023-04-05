from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        'abacaba',
        4
    ],
    '2: leetcode example 2': [
        'ssssss',
        6
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.partitionString(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
