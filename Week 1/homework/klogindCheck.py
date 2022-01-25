import re
import sys


def _klogin(filename, listofKeywords):
    # Open a file
    with open(filename) as f:

         # read in the file and save it to a variable
         contents = f.readlines()

    # Lists to store the results
    results = []
    # Loop through the list returned . Each element is a line from the smallSyslog file
    for line in contents:

     # Loops through keywords
     for eachKeyword in listofKeywords:

        # If line contains the keyword then it will print
        # if eachKeyword in line:
        # Searches a returns results using a regular expression search
        x = re.findall(r''+eachKeyword+'', line)

        for found in x:

            # Append the returned keywords to the results list
            results.append(found)

    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    # Sort list
    results = sorted(results)

    return results
        # print(x)