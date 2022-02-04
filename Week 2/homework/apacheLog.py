import syslogCheck
import importlib
importlib.reload(syslogCheck)

# Proxy
def proxy_events(filename, service, term):
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
        found.append(sp_results[-2])

    hosts = set(found)

    for eachValue in hosts:
        print(eachValue)

# Bytes
def byte_events(filename, service, term):
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
        found.append("Bytes Sent: " + sp_results[4] + "      Bytes Recieved: " + sp_results[7])

    hosts = set(found)

    for eachValue in hosts:
        print(eachValue)


def all_events(filename, service, term):
    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)

    # Found list
    found = []

    # Loop through results
    for eachFound in is_found:
        print(eachFound)