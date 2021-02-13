# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:42:21 2021

@author: rowe1

Converts a number, solution to a row in html format
"""

import waring_pyramidal as wp
import bisect

def solve_single(x):
    global nums
    
    def helper(target, path):
        nonlocal P, res
        if res or target < 0 or len(path) == 5:
            return None
        if target in P:
            res = path + [target]
            return None
        j = min(len(nums) - 1, bisect.bisect_left(nums, target))
        for i in range(j, -1, -1):
            helper(target - nums[i], path + [nums[i]])
            
    res = []
    P = set(nums)
    helper(x, [])
    return res

def convert_to_html_table_row(n, solution):
    html = ["<tr>\n"]
    html.append("  <td>" + str(n) + "</td>\n")
    html.append("  <td>[")
    for num in solution:
        html.append(str(num))
        html.append(',')
    html.pop()
    html.append("]</td>\n")
    html.append("</tr>")
    print(''.join(html))

if __name__ == "__main__":
    numbers = [1, 9, 100, 500, 1000, 123456, 1234567, 123456789]
    numbers = [10**6, 10**9, 10**12]

    # Find a solution for x = p1 + p2 + p3 + p4 + p5 for x <= 10**20
    nums = wp.pyramidal_nums(numbers[-1])
    
    for n in numbers:
        ans = solve_single(n)
        convert_to_html_table_row(n, ans)