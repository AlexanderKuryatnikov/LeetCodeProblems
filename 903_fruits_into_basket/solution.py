from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 1
        try:
            while fruits[max_fruits] == fruits[0]:
                max_fruits += 1
        except IndexError:
            return len(fruits)

        first_fruit_1_index = 0
        last_fruit_1_index = max_fruits - 1
        first_fruit_2_index = max_fruits
        last_fruit_2_index = max_fruits
        max_fruits += 1
        starting_tree = max_fruits

        for i in range(starting_tree, len(fruits)):
            if fruits[i] == fruits[last_fruit_1_index]:
                last_fruit_1_index = i
            elif fruits[i] == fruits[last_fruit_2_index]:
                last_fruit_2_index = i
            else:
                max_fruits = max(
                    max_fruits,
                    i - min(first_fruit_1_index, first_fruit_2_index)
                )
                if last_fruit_1_index > last_fruit_2_index:
                    first_fruit_1_index = last_fruit_2_index + 1
                    first_fruit_2_index = i
                    last_fruit_2_index = i
                else:
                    first_fruit_2_index = last_fruit_1_index + 1
                    first_fruit_1_index = i
                    last_fruit_1_index = i

        max_fruits = max(
            max_fruits,
            len(fruits) - min(first_fruit_1_index, first_fruit_2_index)
        )
        return max_fruits
