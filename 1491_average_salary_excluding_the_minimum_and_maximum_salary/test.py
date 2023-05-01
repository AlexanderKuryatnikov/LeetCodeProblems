from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [4000, 3000, 1000, 2000],
        2500
    ],
    '2: leetcode example 2': [
        [1000, 2000, 3000],
        2000
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.average(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
