# analyzer.py - analysis logic for the CLI Data Analyzer
def analyze_numbers(numbers):
    count = len(numbers)
    min_val = min(numbers) if numbers else None
    max_val = max(numbers) if numbers else None
    total = sum(numbers)
    average = total / count if count > 0 else 0
    return {
        "count": count,
        "min": min_val,
        "max": max_val,
        "sum": total,
        "average": average
    }

def print_analysis(numbers, results):
    print("Numbers entered:", numbers)
    print("Analysis Results:")
    for key, value in results.items():
        print(f"  {key}: {value}")