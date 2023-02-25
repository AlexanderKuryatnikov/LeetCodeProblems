from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: len 1': [
        [1],
        0
    ],
    '2: descending nums': [
        [7, 6, 4, 3, 1],
        0
    ],
    '3: ascending nums': [
        [1, 3, 4, 6, 7],
        6
    ],
    '4: shuffled nums': [
        [7, 1, 5, 3, 6, 4],
        5
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.maxProfit(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
