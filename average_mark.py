#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program finds the average of the user's marks

def find_average(marks):
    # This function determines the smallest number

    # Set total to 0
    total = 0

    # Loop through "array" to find smallest
    for counter in marks:
        total += counter
    average = int(total / len(marks))

    return average


def main():
    # This function collects marks
    all_marks = []

    # Input
    try:
        mark = int(input("Enter a mark as a %: "))
        if mark == -1:
            print("There are no marks to average.")
        else:
            all_marks.append(mark)
            while True:
                mark = int(input("Enter a mark as a %: "))
                if mark == -1:
                    break
                all_marks.append(mark)
            # Process (call find_average) and output
            the_average = find_average(all_marks)
            print("\nThe average is {}.".format(the_average))
    except Exception:
        print("Invalid input")
    print("\nDone.")


if __name__ == "__main__":
    main()
