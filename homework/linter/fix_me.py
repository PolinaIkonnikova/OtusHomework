def calculate_average(numbers: list[float]) -> float:
    """Calculate average of numbers"""
    total = sum(numbers)
    count = len(numbers)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
