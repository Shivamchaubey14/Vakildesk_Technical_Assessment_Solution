from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    
    for item in data:
        group_key = item[key]
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)
    
    return {k: aggregator(v) for k, v in grouped_data.items()}

# Example usage
data = [
    {'category': 'Item1', 'value': 10},
    {'category': 'Item2', 'value': 20},
    {'category': 'Item1', 'value': 15},
    {'category': 'Item2', 'value': 25},
]

aggregator_function = lambda x: sum(item['value'] for item in x)
print(aggregate_data(data, 'category', aggregator_function))
