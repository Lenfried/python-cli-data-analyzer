def main():
    numbers = []
    # Ask the user how many numbers to enter
    while True:
        try:
            num_count = int(input("How many numbers do you want to enter? "))
            if num_count <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    # Loop to collect inputs
    for i in range(num_count):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Print the list
    print("Numbers entered:", numbers)

    # Define analyze_numbers(numbers)
    # Return count, min, max, sum, average in a dictionary
    def analyze_numbers(numbers):
        count = len(numbers)
        min_val = min(numbers)
        max_val = max(numbers)
        total = sum(numbers)
        average = total / count if count > 0 else 0
        return {
            "count": count,
            "min": min_val,
            "max": max_val,
            "sum": total,
            "average": average
        }

    # Call analyze_numbers and print the results
    stats = analyze_numbers(numbers)
    print("Analysis Results:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()