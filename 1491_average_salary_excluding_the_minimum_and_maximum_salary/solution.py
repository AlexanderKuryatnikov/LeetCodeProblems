from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = salary[0]
        max_salary = salary[0]
        salary_sum = 0

        for amount in salary:
            salary_sum += amount
            if min_salary < amount:
                min_salary = amount
            if max_salary > amount:
                max_salary = amount

        return (salary_sum - max_salary - min_salary) / (len(salary) - 2)
