def compute_stats(file):
    try:
        with open(file, "r") as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]

        if numbers:
            total = len(numbers)
            sum_values = sum(numbers)
            average = round(sum_values / total)
            min_value = min(numbers)
            max_value = max(numbers)

            print(f"total = {total}")
            print(f"summation = {sum_values}")
            print(f"average = {average}")
            print(f"Minimum = {min_value}")
            print(f"Maximum = {max_value}")
        else:
            print("total = 0")
            print("summation = 0")
            print("average = 0")
            print("Minimum = None")
            print("Maximum = None")

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file.")

if __name__ == "__main__":
    compute_stats("random_nums.txt")
