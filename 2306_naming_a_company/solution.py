from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        valid_names = 0
        ideas_dict = {}
        for idea in ideas:
            if idea[0] in ideas_dict:
                ideas_dict[idea[0]].add(idea[1:])
            else:
                ideas_dict[idea[0]] = set()
                ideas_dict[idea[0]].add(idea[1:])

        letters = list(ideas_dict.keys())

        for prefix_1 in range(len(letters)):
            for prefix_2 in range(prefix_1 + 1, len(letters)):
                unique_sufix_1 = len(
                    ideas_dict[letters[prefix_1]]
                    - ideas_dict[letters[prefix_2]]
                )
                unique_sufix_2 = len(
                    ideas_dict[letters[prefix_2]]
                    - ideas_dict[letters[prefix_1]]
                )
                print(f'{letters[prefix_1]}  --  {letters[prefix_2]}')
                print(f'{unique_sufix_1}  --  {unique_sufix_2}')
                print(f'valid names {2 * unique_sufix_1 * unique_sufix_2}')
                valid_names += 2 * unique_sufix_1 * unique_sufix_2

        return valid_names
