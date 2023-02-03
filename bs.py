#!/usr/bin/env python3

import re


file = open('test.txt') # Load file into variable
filetext = file.read()
#print(filetext)
testfile = re.split("^(?:(?:25[0-5]|2[0-4]\\d|1?\\d?\\d)(?:\\.(?!$)|$)){4}$", filetext)
#testfile = filetext.split('10.10.10.10')


#testfile = re.split('(\d+.\d+.\d+.\d+)(.|\n)*', filetext) 
print(testfile)










# SHADOW REALM 


"""







   #print(block_data_list[2])


    #split by IP using RE
    # Loop through every entry
    # Spot keywords


    #Github co-piolet  
file = open('test.txt') # Load file into variable
filetext = file.read()
block_data_list = []
i = 0
while i < len(filetext):
    block_data = []
    count = 0 
    for j in range(0, len(filetext)):
        i = 1 + i 
        block_data.append(filetext[j])
    print(block_data)
    if filetext[j].find("Hostnames") >= 0:
        count = count + 1 
    if (count >= 2) :
        del(block_data[-1])
        block_data_list.append(block_data)








    """