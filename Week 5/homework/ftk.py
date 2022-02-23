import os
import argparse
import re
import sys
import yaml

# Toolkit YAML File
filename = '../../logs/access.log'

# The parser
parser = argparse.ArgumentParser(
    description="A forensic toolkit used to detect parse through a directory and detect executables.",
    epilog="Developed by Michael Portegello, 20220222.")

# Parse arguments
args = parser.parse_args()

# Add argument to pass into the ftk.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--specify", required="True", help="Specify what you want to detect.")

# Attach values to the arguments
rootDirectory = args.directory
specify = args.specify


# Open YAML, grab the tools for the designated toolkit, look for matches
def loadToolkit(toolkit, tool):
    # Open YAML file
    try:
        with open(filename, 'r') as f:
            collection = yaml.safe_load(f)
    except EnvironmentError as e:
        print(e.strerror)

    # Retrieve toolkit to parse
    tools = collection[toolkit][tool]

    output = tools.split(",")

    # Parse and open for contents variable
    with open(filename) as f:
        contents = f.readlines()

    # List to store final parse results
    results = []
    # List to store initial results
    result = []

    # Loop through the list
    for line in contents:
        # Search with tools
        for match in output:
            x = re.findall(r'' + match + '', line)
        # Add results to the list
        for result in x:
            results.append(result)

    # If no results display "No Results"
    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    # Sort the results
    results = sorted(results)

    # Return the results
    return results


def loadDirectory(directory):
    # Check if directory is valid
    if not os.path.isdir(rootDirectory):
        print("Invalid directory => {}".format(rootDirectory))
        exit()

    # Save file list
    fList = []

    # Move through directory
    for root, subfolders, filenames in os.walk(rootDirectory):
        for f in filenames:
            fileList = directory + "/" + f
            fList.append(fileList)
        return fList

# Did not manage to complete the code and produce an output
# Things to continue working on:
# 1. Formatting the output that gets printed to the user.
# 2. How exactly the toolkit gets matched
# 3. Code to link functions and complete the .py file
