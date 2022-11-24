# school_data.py
# JESSICA TRAN, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Add your code within the main function. A docstring is not required for this function.
def main():
    # Import data here
    data_18 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)                                # Import SchoolData_2018-2019.csv file.
    data_19 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)                                # Import SchoolData_2019-2020.csv file.
    data_20 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)                                # Import SchoolData_2020-2021.csv file.
    
    school_codes = ['1224', '1679', '9626', '9806',                                                                         # List of school codes.
    '9813', '9815', '9816', '9823', '9825', 
    '9826', '9829', '9830', '9836', '9847', '9850', 
    '9856', '9857', '9858', '9860', '9865']
    school_name = ['Centennial High School', 'Robert Thirsk School', 'Louise Dean School', 'Queen Elizabeth High School',   # List of school names.
    'Forest Lawn High School', 'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 
    'James Fowler High School', 'Ernest Manning High School', 'William Aberhart High School', 'National Sport School', 
    'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School', 'Jack James High School', 
    'Sir Winston Churchill High School', 'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School']
    code_name = zip(school_codes, school_name)
    name_code = zip(school_name, school_codes)
    # Hint: Create a dictionary for all school names and codes
    dict_code_name = dict(code_name)                                                                                        # Dictionary of school code to name.
    dict_name_code = dict(name_code)                                                                                        # Dictionary of school name to code.
    
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    print('Array Data for 2020 - 2021\n', data_20)                                                                          # Display array data from SchoolData_2018-2019.csv file.
    print('Array Data for 2019 - 2020\n', data_19)                                                                          # Display array data from SchoolData_2019-2020.csv file.
    print('Array Data for 2018 - 2019\n', data_18)                                                                          # Display array data from SchoolData_2020-2021.csv file.
    
   

    # Add request for user input here
    while True:
        user_input = input('Please enter the high school name or code: ')                                                                                                   # Prompt user to input high school name or code.
        if user_input in school_codes:
            school_object = School(dict_code_name[user_input], user_input)
            School.print_all_stats(school_object)
            school_index = school_codes.index(user_input)
            print("\n***Requested School Statistics***\n")                                                                                                                  # Display Requested School Statistics.
            print(f'Mean Enrollment for Grade 10: {int((data_18[school_index][1] + data_19[school_index][1] + data_20[school_index][1])//3)}')                              # Display mean enrollment for grade 10. 
            print(f'Mean Enrollment for Grade 11: {int((data_18[school_index][2] + data_19[school_index][2] + data_20[school_index][2])//3)}')                              # Display mean enrollment for grade 11. 
            print(f'Mean Enrollment for Grade 12: {int((data_18[school_index][3] + data_19[school_index][3] + data_20[school_index][3])/3)}')                               # Display mean enrollment for grade 12. 
            print(f'Total number of students who graduated in the past 3 years: {int((data_18[school_index][3] + data_19[school_index][3] + data_20[school_index][3]))}')   # Display total number of students that graduated in the past 3 years.
            
            break
        elif user_input in school_name: 
            school_object = School(user_input, dict_name_code[user_input])
            School.print_all_stats(school_object)
            school_index = school_codes.index(dict_name_code[user_input])
            print("\n***Requested School Statistics***\n")                                                                                                                  # Display Requested School Statistics.
            print(f'Mean Enrollment for Grade 10: {int((data_18[school_index][1] + data_19[school_index][1] + data_20[school_index][1])//3)}')                              # Display mean enrollment for grade 10.
            print(f'Mean Enrollment for Grade 11: {int((data_18[school_index][2] + data_19[school_index][2] + data_20[school_index][2])//3)}')                              # Display mean enrollment for grade 11.
            print(f'Mean Enrollment for Grade 12: {int((data_18[school_index][3] + data_19[school_index][3] + data_20[school_index][3])/3)}')                               # Display mean enrollment for grade 12.
            print(f'Total number of students who graduated in the past 3 years: {int((data_18[school_index][3] + data_19[school_index][3] + data_20[school_index][3]))}')   # Display total number of students that graduated in the past 3 years.
            break
        else:
            print('You must enter a valid school name or code.')                                                                                                            # Prompt user to enter a valid high shool name or code.
     
    
    # Print school name and code using the given class
    # Add data processing and plotting here
    plt.subplot(1, 1, 1)                                                                                # Plot with one row, one column, in position 1.
    plt.plot([10, 11, 12], data_20[school_index, range(1,4)], 'bo', label = '2021 Enrollment')          # Plot with blue dots for 2021 enrollment.
    plt.plot([10, 11, 12], data_19[school_index, range(1,4)], 'go', label = '2020 Enrollment')          # Plot with green dots for 2020 enrollment.
    plt.plot([10, 11, 12], data_18[school_index, range(1,4)], 'ro', label = '2019 Enrollment')          # Plot with red dots for 2019 enrollment.

    
    plt.xticks((10, 11, 12))                                                                            # Label x-axis starting at 10 ending at 12.
    plt.xlabel('Grade Level')                                                                           # Label x-axis with 'Grade Level'.
    plt.ylabel('Number of Students')                                                                    # Label y-axis with 'Number of Students'.
    plt.title('Grade Enrollment by Year')                                                               # Title the plot as 'Grade Enrollment by Year'.
    plt.legend(shadow = True, loc='upper left')                                                         # Add a legend in the upper left of the graph.
    plt.show()                                                                                          # Display the graph.

    '''BONUS ASSIGNMENT'''
    enrollment_10 = [data_18[school_index][1], data_19[school_index][1], data_20[school_index][1]]      # List of grade 10 enrollment in the past 3 years.
    enrollment_11 = [data_18[school_index][2], data_19[school_index][2], data_20[school_index][2]]      # List of grade 11 enrollment in the past 3 years.
    enrollment_12 = [data_18[school_index][3], data_19[school_index][3], data_20[school_index][3]]      # List of grade 12 enrollment in the past 3 years.

    year = list(range(2019, 2022))
    
    plt.subplot(3, 1, 1)                                                                                # Plot with three rows, one column, in position 1.
    plt.plot(year, enrollment_10, 'y--', label = 'Grade 10')                                            # Plot with yellow dashed line for grade 10 enrollment.
    plt.ylabel('Number of Students')                                                                    # Label y-axis with 'Number of Students'.
    plt.title('Enrollment by Grade')                                                                    # Title the plot as 'Enrollment by Grade'.
    plt.xticks((2019, 2020, 2021))                                                                      # Label x-axis starting at 2019 ending at 2021.
    plt.legend(shadow = True, loc='upper right')                                                        # Add a legend in the upper right of the graph.

    plt.subplot(3, 1, 2)                                                                                # Plot with three rows, one column, in position 2.
    plt.plot(year, enrollment_11, 'm--', label = 'Grade 11')                                            # Plot with magenta dashed line for grade 11 enrollment.
    plt.ylabel('Number of Students')                                                                    # Label y-axis with 'Number of Students'.
    plt.xticks((2019, 2020, 2021))                                                                      # Label x-axis starting at 2019 ending at 2021.
    plt.legend(shadow = True, loc='upper right')                                                        # Add a legend in the upper right of the graph.

    plt.subplot(3, 1, 3)                                                                                # Plot with three rows, one column, in position 3.
    plt.plot(year, enrollment_12, 'c--', label = 'Grade 12')                                            # Plot with cyan dashed line for grade 12 enrollment.
    plt.ylabel('Number of Students')                                                                    # Label y-axis with 'Number of Students'.
    plt.xlabel('Enrollment Year')                                                                       # Label x-axis with 'Enrollment Year'.
    plt.xticks((2019, 2020, 2021))                                                                      # Label x-axis starting at 2019 ending at 2021.
    plt.legend(shadow = True, loc='upper right')                                                        # Add a legend in the upper right of the graph.

    plt.show()                                                                                          # Display the graph.
    
# Do not modify the code below
if __name__ == '__main__':
    main()                                                                                              # Call the main function.

