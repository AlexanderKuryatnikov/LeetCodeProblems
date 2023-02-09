from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        ['coffee', 'donuts', 'time', 'toffee'],
        6
    ],
    '2: leetcode example 2': [
        ['lack', 'back'],
        0
    ],
    '3: single char letters': [
        ['a', 'b', 'c'],
        0
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.distinctNames(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
