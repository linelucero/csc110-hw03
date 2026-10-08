"""
Name: Aline Valenzuela-Lucero
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:
        # check if the input is not a digit print error
        # convert to int
        # check if the int is not in the interval [0 to 10] print error
        # add the int to grades at index idx

        alist = list(range(11)) #list giving the possible values within the range
        in_str = input("Give me the next grade in [0 to 10]:", ) #user input
        if in_str.isdigit(): #conditional in which will reject non digit values or outside the range
            in_str = int(in_str)
            if in_str not in alist:
                print("Error in read_five_ints: input integer outside of range.")
                exit()
            else:
                grades[idx] = in_str #stores the values
        else:
            print("Error in read_five_ints: input string is not for an integer")
            exit()

        '''This functions purpose is for the user to input a grade (digit) with a value of 1-10. Anything outside of
            the values or if its not a digit will not be accepted per the code. Then, it will be stored into the matrix.'''

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    letter = str(input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")) #user picks letter corresponding to average they want.
    if letter == "a": #this method will give the mean and return the mean
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    elif letter == "b": #this method will give the median and return the median
        print("picked: Median")
        avg = statistics.median(grades)
        return avg
    elif letter == "c": #this method will give the mode and return the mode
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    else: #any other input letter will be rejected.
        print("Error in pick_averaging_method: incorrect option picked")
        exit()
    '''This function allows the user to pick an everaging method by inserting a certain letter
        that is later bounded by a conditional statement. Anything other the set letters will be
        rejected. The function then returns the averaging method picked and the value.'''

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    viz = str(input("Pick '1' for print average, or '2' for plot average: ")) #user input stored into variable
    if viz == '1': #conditional if 1 is picked, the list and average are given
        print_list_and_average(average)
    elif viz == '2': #conditional if 2 is picked, plot is given
        plot_grades(average)
    else: #anything else will be an error.
        print("Error in pick_visualization: incorrect option picked")
        exit()
    '''This last function has the user pick a type of visualization, the list and the average from the
        method selected or the plot with the method result. it uses a string input of a digit, to which
        a conditional gives the printed listed if 1 and plot if 2. Any other input will be rejected.'''


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
