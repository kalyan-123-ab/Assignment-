from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    for item in data:
        if item[key] not in grouped_data:
            grouped_data[item[key]] = []
        grouped_data[item[key]].append(item)

    return {k: aggregator(v) for k, v in grouped_data.items()}

# Example usage
data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 30},
]

result = aggregate_data(data, 'category', lambda items: sum([i['value'] for i in items]))
print(result)  # Output: {'A': 40, 'B': 20}
