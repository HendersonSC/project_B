# Project 2 Group 12
# July 23, 2019
# Gets data lotto number data from remote server and displays the
# number of times each number has been drawn
from urllib.request import Request, urlopen
from urllib.error import URLError
import shutil
import tempfile
import pandas as pd

#shende25
# Get the data from the remote resource
def get_file(url,data_file):
    # Try contacting the server and getting the data
    try:
        response = urlopen(Request(url))
    except URLError as e:
        # Catch errors related to the URL
        if hasattr(e, 'reason'):
            print('Connection failed!')
            print('Reason: ', e.reason)

        # Catch errors related to the server
        elif hasattr(e, 'code'):
            print('Server Error!')
            print('Error code: ', e.code)

    # Get the data and store for use as a temporary
    else:
        shutil.copyfileobj(response,data_file)
        data_file.seek(0)

#shende25
if __name__ == "__main__":
    # Setup temporary file for holding data
    data_file = tempfile.NamedTemporaryFile()
    # Get data from remote resource
    get_file(input("Enter URL: ",),data_file)
