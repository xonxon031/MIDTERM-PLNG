def program_1():
    arr = []
    print("Enter 10 real numbers:")
    for _ in range(10):
        arr.append(float(input()))

    pos_sum = 0
    pos_count = 0
    for num in arr:
        if num > 0:
            pos_sum += num
            pos_count += 1
    pos_avg = pos_sum / pos_count if pos_count > 0 else 0
    print(f"Sum of positive numbers: {pos_sum}")
    print(f"Average of positive numbers: {pos_avg}")

    neg_count = 0
    for num in arr:
        if num < 0:
            neg_count += 1
    print(f"Count of negative numbers: {neg_count}")

    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    print(f"Minimum value in array: {min_val}")


def program_2():
    arr = []
    print("Enter 8 integer numbers:")
    for _ in range(8):
        arr.append(int(input()))

    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    print(f"Array after removing duplicates: {unique_arr}")

    if len(unique_arr) < 2:
        print("Array does not have enough distinct elements to find second largest/smallest.")
        return

    unique_arr.sort()
    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]

    print(f"Second largest element: {second_largest}")
    print(f"Second smallest element: {second_smallest}")


def program_3():
    data_input = input("Enter Data in Array: ")
    arr = [int(x) for x in data_input.split()]
    print("Stored Data in Array:", " ".join(map(str, arr)))

    pos = int(input("Enter poss. of Element to Delete: "))

    if 1 <= pos <= len(arr):
        arr.pop(pos - 1)
        print("New data in Array:", " ".join(map(str, arr)))
    else:
        print("Invalid position!")


def program_4():
    size = int(input("Enter Size of Array : "))
    print(f"Enter any {size} elements in Array:")
    elements = input().split()
    arr = [int(x) for x in elements[:size]]

    evens = [str(x) for x in arr if x % 2 == 0]
    odds = [str(x) for x in arr if x % 2 != 0]

    print("Even Elements:", " ".join(evens))
    print("Odd Elements:", " ".join(odds))


def program_5():
    print("*")
    print("A")
    print("AA*")
    print("AAA")


def program_6():
    basic = 12000
    da = 0.12 * basic
    hra = 150
    ta = 120
    others = 450

    pf = 0.14 * basic
    it = 0.15 * basic

    net_salary = basic + da + hra + ta + others - (pf + it)

    print("--- Salary Details ---")
    print(f"Basic Salary : ${basic:.2f}")
    print(f"DA           : ${da:.2f}")
    print(f"HRA          : ${hra:.2f}")
    print(f"TA           : ${ta:.2f}")
    print(f"Others       : ${others:.2f}")
    print(f"PF           : ${pf:.2f}")
    print(f"IT           : ${it:.2f}")
    print(f"Net Salary   : ${net_salary:.2f}")


def main():
    while True:
        print("\nChoose the program you want to run")
        print("Program #1")
        print("Program #2")
        print("Program #3")
        print("Program #4")
        print("Program #5")
        print("Program #6")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            program_1()
        elif choice == "2":
            program_2()
        elif choice == "3":
            program_3()
        elif choice == "4":
            program_4()
        elif choice == "5":
            program_5()
        elif choice == "6":
            program_6()
        else:
            print("Invalid choice!")

        cont = input("\nDo you want to continue ? Y/N ").strip().upper()
        if cont != "Y":
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()