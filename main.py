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

if __name__ == "__main__":
    main()