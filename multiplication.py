# multiplication_table.py

def print_table(number):
    """
    Function to print multiplication table from 1 to 10
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        print("\nMultiplication Table:\n")
        print_table(num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")