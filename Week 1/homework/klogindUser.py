import klogindCheck
import importlib
importlib.reload(klogindCheck)

# Authentication failures
def ssh_user(filename, searchTerms):
    # Call klogindCheck and return the results
    is_found = klogindCheck._klogin(filename, searchTerms)

    # Found list
    found = []

    # Loop through results
    for eachFound in is_found:
        # print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[5])

    hosts = set(found)

    for eachHost in hosts:
        print(eachHost)


