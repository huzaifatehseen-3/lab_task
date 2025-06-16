def compute_stats(file):
    total = 0
    sum_values = 0
    min_value = None
    max_value = None
    try:
        with open(file, "r") as f:
            first_line = f.readline().strip()
            if first_line:  # ensure file is not empty
                min_value = max_value = int(first_line)
                sum_values += min_value
                total += 1
            for line in f:
                num = int(line.strip())
                total += 1
                sum_values += num
                if num < min_value:
                    min_value = num
                if num > max_value:
                    max_value = num
        if total > 0:
            average = round(sum_values / total)
        else:
            average = 0
        print(f"total = {total}")
        print(f"summation = {sum_values}")
        print(f"average = {average}")
        print(f"Minimum = {min_value}")
        print(f"Maximum = {max_value}")
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file.")

if __name__ == "__main__":
    compute_stats("random_nums.txt")
