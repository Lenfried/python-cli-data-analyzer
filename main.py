from datetime import datetime


def collect_and_analyze():
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

    # Save the analysis report to a file named report.txt
    with open("report.txt", "a") as f:
        f.write(f"Report generated on {datetime.now()}\n")
        f.write(f"Numbers entered: {numbers}\n")
        f.write("Analysis Results:\n")
        for key, value in stats.items():
            f.write(f"  {key}: {value}\n")
        f.write("\n")

def main():
    while True:
        print("\nMenu:")
        print("1) Enter numbers and analyze")
        print("2) Exit the program")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            collect_and_analyze()
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
if __name__ == "__main__":
    main()