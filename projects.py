data = []   


def input_data():
    """Input data"""
    global data
    data = input("Enter numbers (space separated): ").split()

    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i = i + 1

    print("Data saved!")


def built_in_summary():
    """Built-in functions"""
    print("Total elements:", len(data))
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Sum:", sum(data))
    print("Average:", round(sum(data) / len(data), 2))


def factorial(n):
    """Recursion"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def filter_data():
    """Lambda function"""
    t = int(input("Enter threshold: "))
    result = []

    for x in data:
        if x >= t:
            result.append(x)

    print("Filtered data:", result)


def sort_data():
    """Sorting"""
    print("Ascending:", sorted(data))
    print("Descending:", sorted(data, reverse=True))


def multiple_values():
    """Return multiple values"""
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)
    return minimum, maximum, average


while True:
    print("\n1.Input Data")
    print("2.Built-in Summary")
    print("3.Factorial")
    print("4.Filter Data")
    print("5.Sort Data")
    print("6.Multiple Values")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        built_in_summary()

    elif choice == 3:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    elif choice == 4:
        filter_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:
        a, b, c = multiple_values()
        print("Min:", a)
        print("Max:", b)
        print("Average:", round(c, 2))

    elif choice == 7:
        print("Program Ended")
        break
