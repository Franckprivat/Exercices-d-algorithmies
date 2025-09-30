from typing import List

def find_sum_pair(numbers: List[int], k: int) -> List[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return [i, j]
    return [0, 0]

print(find_sum_pair([10, 15, 3, 7], 17))  

# output: [0, 3]