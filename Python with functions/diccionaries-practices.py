# Example 5

#def main():
#    # Create a dictionary with student IDs as the keys
#    # and student data stored in a list as the values.
#    students = {
#        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
#        "61-315-0160": ["Michelle", "Davis", "dav21012@byui.edu", 3],
#        "10-450-1203": ["Jorge", "Soares", "soa22005@byui.edu", 15],
#        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
#        "07-103-5621": ["Michelle", "Davis", "dav19008@byui.edu", 0],
#        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
#    }
#
#    # These are the indexes of the elements in the value lists.
#    GIVEN_NAME_INDEX = 0
#    SURNAME_INDEX = 1
#    EMAIL_INDEX = 2
#    CREDITS_INDEX = 3
#
#    total = 0
#
#    # For each item in the list add the number
#    # of credits that the student has earned.
#    for item in students.items():
#        key = item[0]
#        value = item[1]
#
#        # Retrieve the number of credits from the value list.
#        credits = value[CREDITS_INDEX]
#
#        # Add the number of credits to the total.
#        total += credits
#
#    print(f"Total credits earned by all students: {total}")
#
# Example 7

def main():
    # Create a list that contains five student numbers.
    numbers = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names = ["Clint Huish", "Michelle Davis",
            "Jorge Soares", "Abdul Ali", "Michelle Davis"]

    # Convert the numbers list and names list into a dictionary.
    student_dict = dict(zip(numbers, names))

    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)


# Call main to start this program.
if __name__ == "__main__":
    main()