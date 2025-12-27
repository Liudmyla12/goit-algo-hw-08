import heapq
import sys
from typing import List, Union

Number = Union[int, float]


def min_cost_to_connect_cables(lengths: List[Number]) -> Number:
    """
    Мінімізує загальні витрати на з’єднання кабелів.
    Кожне з’єднання двох кабелів коштує суму їх довжин.
    Оптимальна стратегія: завжди з’єднувати два найкоротші кабелі (мін-купа).
    """
    if not lengths or len(lengths) == 1:
        return 0

    heap = list(lengths)
    heapq.heapify(heap)

    total_cost: Number = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost


def parse_args(argv: List[str]) -> List[Number]:
    """
    Дозволяє запускати так:
    py .\\task_1.py 4 3 2 6
    """
    if len(argv) <= 1:
        return []
    result: List[Number] = []
    for x in argv[1:]:
        try:
            # підтримка цілих і дробових
            v = float(x)
            if v.is_integer():
                result.append(int(v))
            else:
                result.append(v)
        except ValueError:
            raise ValueError(f"Некоректне число: {x}")
    return result


if __name__ == "__main__":
    # Якщо аргументи не передали — беремо приклад
    try:
        cables = parse_args(sys.argv)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)

    if not cables:
        cables = [4, 3, 2, 6]

    total = min_cost_to_connect_cables(cables)
    print(f"Cables: {cables}")
    print(f"Min total cost: {total}")
