def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())  # Change to int() if only integers are expected
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid value: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    return numbers

def calculate_stats(numbers):
    if not numbers:
        return {"total": 0, "sum": 0, "average": 0, "min": None, "max": None}

    total = len(numbers)
    sum_values = sum(numbers)
    average = round(sum_values / total)
    min_value = min(numbers)
    max_value = max(numbers)

    return {
        "total": total,
        "sum": sum_values,
        "average": average,
        "min": min_value,
        "max": max_value,
    }

def print_stats(stats):
    print(f"Total Numbers: {stats['total']}")
    print(f"Summation: {stats['sum']}")
    print(f"Average: {stats['average']}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")

if __name__ == "__main__":
    file_path = "random_nums.txt"  # Ensure this file exists in your working directory
    numbers = read_numbers_from_file(file_path)
    stats = calculate_stats(numbers)
    print_stats(stats)
