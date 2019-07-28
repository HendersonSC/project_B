# COSC 505: Summer 2019
# ProjectB - Group 12
# Damilola Olayinka Akamo
# Nicole Callais
# Shane Christopher Henderson
# Stephen Opeyemi Fatokun
#
# 07/22/2019
# A python program retrieving lotto data from an internet website, and plotting
# the frequency of each number to show the most frequently occuring number.
from urllib.request import Request, urlopen
from urllib.error import URLError
import shutil
import tempfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#sfatokun
# Tally the occurances of each winning number
def count_num(df):
    count = np.zeros(75,dtype=np.int32)
    for i in range(1,6):
        nums = df["ball"+str(i)].values
        for j in nums:
            count[j-1] += 1
    return count

#sfatokun
# Tally the occurances of each winning number
def count_pb(df):
    count = np.zeros(75,dtype=np.int32)
    nums = df["Mega Ball"].values
    for j in nums:
        count[j-1] += 1
    print(count)
    return count

#ncallais
# Extracting the Winning Numbers and Mega Ball data
def create_plot(lotto_data_frame):

    # sfatokun
    # Getting the frequency of occurrence for each winning number
    win_count = count_num(df)
    mega_count = count_pb(df)

    # Line plot of the Winning Number and Mega Ball
    ## ncallais
    plt.title('Winning Lotto Numbers Frequency')
    nums = np.arange(1,76)
    print(nums)

    # Label lines
    plt.plot(nums, win_count, label='Lotto Numbers')
    plt.plot(nums, mega_count, label='Megaball')

    # Label x & y axes
    plt.ylabel('Frequency')
    plt.xlabel('Ball Number')

    ## Add legend in upper right corner
    plt.legend(prop={'size': 6}, loc="upper right")

    ### Calculate modes
    win_mode = win_count.argmax() + 1
    win_mode_count = win_count[win_mode]
    mega_mode = mega_count.argmax() + 1
    mega_mode_count = mega_count[mega_mode-1]
    print(mega_mode,mega_mode_count)

    ## Plot arrow for mega mode and label
    mega_label = 'Megaball = '+ str(mega_mode)
    meg_pos = (mega_mode,mega_mode_count)
    meg_txt_pos = (mega_mode+4,mega_mode_count*1.15)
    plt.annotate(s=mega_label, xy=meg_pos, xytext=meg_txt_pos, \
            fontsize=8, arrowprops=dict(facecolor='black',shrink=0.05), \
            horizontalalignment='left', verticalalignment='top')

    ## Plot win mode line and label
    win_label = 'Most frequent = '+ str(win_mode)
    plt.axvline(x=win_mode, color = 'red')
    x_text_annotation = plt.annotate(s=win_label, textcoords='axes fraction', \
            xy=((win_mode/75)+.1,.95), fontsize=8)

    ## Show plot
    plt.show()

#shende25
# Get the data from the remote resource
def get_file(url):
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
        return None

    # Get the data and store for use as a temporary
    else:
        # Setup and return temporary file for holding data
        data_file = tempfile.NamedTemporaryFile()
        shutil.copyfileobj(response,data_file)
        data_file.seek(0)
        return data_file

#shend25 
# Get a working data frame with just necessary information
def get_work_df(data_file):
    # Create "master" dataframe
    df = pd.read_csv(data_file)
    # For the sake of expedience separate out wining numbers and powerball
    df_nums = pd.DataFrame(data=df["Winning Numbers"].str.split().to_list(), \
            columns=["ball1","ball2","ball3","ball4","ball5"]).astype(np.int8)
    df_nums["Mega Ball"] = pd.DataFrame(data=df["Mega Ball"]).astype(np.int8)
    return df_nums

#shende25
if __name__ == "__main__":
    # Get data from remote resource
    data_file = get_file(input("Enter URL: ",))
    if data_file:
        df = get_work_df(data_file)
        create_plot(df)
