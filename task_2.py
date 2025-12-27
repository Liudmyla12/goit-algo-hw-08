import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Злиття k відсортованих списків в один відсортований,
    використовуючи мін-купу (heapq).
    """
    heap = []
    result: List[int] = []

    # старт: беремо перший елемент з кожного списку
    for list_idx, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], list_idx, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            next_val = lists[list_idx][next_idx]
            heapq.heappush(heap, (next_val, list_idx, next_idx))

    return result


if __name__ == "__main__":
    lists_ = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists_)
    print("Відсортований список:", merged)
