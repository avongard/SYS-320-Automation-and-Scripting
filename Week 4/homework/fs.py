import os
import argparse
import yaml
import re
import sys

# Parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and filters for any attacks/attempts.",
    epilog="Developed by Michael Portegello, 2022-02-15."
)

# Add argument to pass into the fs.py
parser.add_argument("-d", "--directory", required="True", help="Enter a valid directory to search from.")
parser.add_argument("-s", "--specify", required="True", help = "Specify a term to search from the playbook.")
# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
specify = args.specify

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# Check the yaml playbook
try:
    with open('playbook.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)

# List to save files
fList = []

# Crawl through provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root + "/" + f
        fList.append(fileList)
    print(fList)

## Main
def specificDirectory(fList, service, term):
    # Query the yaml file for the 'term' or direction
    # and retrieve the strings to search on.
    terms = keywords[service][term]

    listofKeywords = terms.split(",")
    # Open a file
    with open(fList) as f:
         # read in the file and save it to a variable
         contents = f.readlines()

    # Lists to store the results
    results = []
    # Loop through the list returned . Each element is a line from the accumulated fList
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