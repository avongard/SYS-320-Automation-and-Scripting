import syslogCheck
import importlib
importlib.reload(syslogCheck)

# SSH authentication failures
def apache_events(filename, service, term):
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)

    # Found list
    found = []

    # Loop through results
    for eachFound in is_found:
        # print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])

    hosts = set(found)

    for eachValue in hosts:
        print(eachValue)
