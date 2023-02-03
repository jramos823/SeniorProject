#!/usr/bin/env python3
"""
def FileParser():
  file = open('test_results.txt') # Load file into variable
  filetext = file.readlines()
  #print(filetext[2947]) # TEST DO NOT NEED
  ics_words = ['Modbus','BACnet/IP','DNP3','EtherCAT','Ethernet/IP','BigIP','FL-net','Foundation Fieldbus','ICCP','Modbus TCP','OPC UA Binary','OPC UA Discovery Server','OPC UA XML,PROFINET','ROC PLus']
  
 

  block_data_list = []
  for i in range(0, len(filetext)):
    block_data = []
    count = 0
    for j in range(i, len(filetext)):
      print(filetext[j])
      if(filetext[j].find("Hostnames")):
        count += 1 
      if(count >= 2):
        del block_data[-1]
        block_data_list.append(block_data)
        i = j-1
        break
      block_data.append(filetext[j])
  #for block in block_data_list:
    #print("")

FileParser()  
"""

def FileParser():
    file = open('test_results.txt') # Load file into variable
    filetext = file.readlines()
    block_data_list = []
    i = 0
    while i < len(filetext):
        block_data = []
        count = 0
        for j in range(i, len(filetext)):
            #print(filetext[j])
            if(filetext[j].find("Hostnames") >= 0):
                count += 1 
            if(count >= 2):
                del block_data[-1]
                block_data_list.append(block_data)
                i = j-1
                break
            block_data.append(filetext[j])
            i += 1
        print(block_data_list[0])

FileParser()  