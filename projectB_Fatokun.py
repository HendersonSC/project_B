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


import pandas as pd
import matplotlib.pyplot as plt

lotto_data_frame = pd.read_csv("http://web.eecs.utk.edu/~cosc505/data/lottonums.csv")
# sfatokun
# Extracting the Winning Numbers and Mega Ball data frame into
# variables "win" and "mega" respectively
win = lotto_data_frame["Winning Numbers"]
mega = lotto_data_frame["Mega Ball"]

# sfatokun
# Flattening out the data frame of the winning number
# into a single list
def winning_num(za):
        z = []
        for a in za:
                n = str(a)
                m = n.split()
                z = z + m
        return z

# sfatokun
# Converting each element in the winning list into
# integer data type
def convert_int(za):
        p = []
        for b in za:
                p1 = [int(b)]
                p = p + p1
        return p

# sfatokun
# Counting the number of occurrence for each number
# from the Winning number data frame
def count_num(za):
        q = []
        for c in range(1,76):
                q1 = [za.count(c)]
                q = q + q1
        return(q)
# sfatokun
# Converting winning number series type to a list type
win_list = winning_num(win)
# Converting all element of the list to type int
win_int = convert_int(win_list)
# Getting the frequency of occurrence for each winning number
win_count = count_num(win_int)

# Converting all element of the mega data frame from type int64
# to type int
mega_int = convert_int(mega)
# Getting the frequency of occurrence for each mega ball number
mega_count = count_num(mega_int)
# Declaring the x-axis lenght (1 to 75)
nums = range(1,76)

# Line plot of the Winning Number and Mega Ball
plt.plot(nums, win_count)
plt.plot(nums, mega_count)
plt.show()
