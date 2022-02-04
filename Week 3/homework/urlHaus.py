# Imports needed for the code
import csv
import re


# Function that defines urlHausOpen
# Changed the 1 to l in function name
# Indented below the funcion
# Changed while to with
# Removed string from file name
def urlHausOpen(filename, searchTerm):
    # Opens the file "f"
    # Set contents = to csv.review(f)
    # Added the variable for file name
    # Changed from review to reader
    with open(filename) as f:
        contents = csv.reader(f)
        for _ in range(9):
            next(contents)
        # Opens the csv file and grabs the first 9 values from contents
        for eachLine in contents:
            # keyword in searchTerms should be with the x=re.findall line so swapped with eachLine in contents
            # Fixed variable name from searchTerms to searchTerm
            for keyword in searchTerm:
                # Removed + and r
                x = re.findall(keyword, eachLine[2])
                # The code up to this point is looping through the CSV and finding regex matches

                # Added indentation
                for _ in x:
                    # Don't edit this line. It is here to show how it is possible
                    # to remove the "tt" so programs don't convert the malicious
                    # domains to links that an be accidentally clicked on.
                    # Changed from 4 to 7 to print data set
                    the_url = eachLine[2].replace("http", "hxxp")
                    the_src = eachLine[7]
                    print("""
                          URL: {}
                          Info: {}
                           """.format(the_url, the_src) + '*' * 60)
                    # Changed from ,format to .format
                    # Added brackets for URL and Info
                    # We are concatenating after passing in the variables so we need a + and an * for out desired output
                    # The code here will now format into the print and place the values properly in their brackets
