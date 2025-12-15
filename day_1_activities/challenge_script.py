# Mini challenge Day 3 Script - WIP Code

# System on
system_on = True

# This loop will run as long as "system_on" is true, which can be made false through
# user input.
while system_on:

    # Firstly, the script prints information to the terminal about how to use the program.
    print("_" * 50)
    print("")
    print("STUDENT LOOKUP TOOL - Hello! Please enter a student name to begin!")
    print("Type in a name to view that student's data.")
    print("Type in 'exit' to abort the program.")
    print("Type in 'add' to add in another student's data.")
    # This one might be scrapped, but I'll put it here anyway:
    print("Type in 'view all' to see all student data.")

    # The response the user gives is assigned to a variable. Afterwards, magic!
    response_main = str(input(""))

    # If the user response happened to be "exit," then the program will simply stop,
    # accomplished by making the variable "system_on" from earlier be false.
    if response_main.lower() == "exit":
        system_on = False