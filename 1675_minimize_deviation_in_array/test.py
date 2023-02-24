from solution import Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1, 2, 3, 4],
        1
    ],
    '2: leetcode example 2': [
        [4, 1, 5, 20, 3],
        3
    ],
    '3: leetcode example 3': [
        [2, 10, 8],
        3
    ],
    '4: min div found before cycle end': [
        [18, 16, 15],
        3
    ],
    '5: two numbers 1': [
        [7, 9],
        2
    ],
    '6: two numbers 2': [
        [14, 13],
        1
    ],
    '7: two numbers 3': [
        [14, 16],
        1
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.minimumDeviation(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
