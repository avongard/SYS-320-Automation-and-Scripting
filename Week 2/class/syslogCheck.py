# Create and interface to search through syslog files
import re
import sys
import yaml

# Open yaml file
try:

    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)


def _syslog(filename, service, term):
    # Query the yaml file for the 'term' or direction
    # and retrieve the strings to search on.
    terms = keywords[service][term]

    listofKeywords = terms.split(",")
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