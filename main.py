from datetime import datetime
import numbers
from storage import save_numbers, load_numbers, save_report
from analyzer import analyze_numbers, print_analysis

def collect_numbers():
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

    return numbers

def main():
    stats = None
    while True:
        print("\nMenu:")
        print("1) Enter numbers")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Analyze current numbers")
        print("5) Save analysis report to file")
        print("6) Exit the program")
        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == "1":
            numbers = collect_numbers()
        elif choice == "2":
            try:
                save_numbers(numbers)
            except Exception as e:
                print(f"An error occurred while saving: {e}")
            else:
                print("Numbers saved to data.json")
        elif choice == "3":
            try:
                numbers = load_numbers()
                print("Numbers loaded from data.json:", numbers)
            except Exception as e:
                print(f"An error occurred while loading: {e}")
        elif choice == "4":
            try:
                stats = analyze_numbers(numbers)
                print_analysis(numbers, stats)
            except Exception as e:
                print(f"An error occurred during analysis: {e}")
        elif choice == "5":
            if not numbers or stats is None:
                print("No numbers or analysis results to save. Please enter and analyze numbers first.")
                continue
            try:
                save_report(numbers, stats)
            except Exception as e:
                print(f"An error occurred while saving the report: {e}")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
            
if __name__ == "__main__":
    main()