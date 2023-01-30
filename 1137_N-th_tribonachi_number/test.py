from solution import solution


TEST_VALUES = {
    '1: n = 0': [
        0,
        0
    ],
    '2: n = 1': [
        1,
        1
    ],
    '3: n = 2': [
        2,
        1
    ],
    '4: n = 3': [
        3,
        2
    ],
    '5: n = 25': [
        25,
        1389537
    ],
    '5: n = 37': [
        37,
        2082876103
    ],
}


def test():
    for test, values in TEST_VALUES.items():
        result = solution.tribonacci(values[0])
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
