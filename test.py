#!/usr/bin/env python3

def FileParser():
	file = open('test_results.txt') # Load file into variable
	filetext = file.readlines()
	print(filetext[2947]) # TEST DO NOT NEED
	ics_words = 'Modbus','BACnet/IP','DNP3','EtherCAT','Ethernet/IP','BigIP','FL-net','Foundation Fieldbus','ICCP','Modbus TCP','OPC UA Binary','OPC UA Discovery Server','OPC UA XML,PROFINET','ROC PLus'
	ics_words = str(ics_words)
	#print(ics_words) TEST DO NOT NEED 

	valid_block_text = []
	non_valid_block = []
	iter_num = []

	for index_count, lines in enumerate(filetext):
		#print("This is the index: "+ str(index_count))
		#print("This is the linee: "+ lines)
		non_valid_block.append(lines)
		ics_name_location = lines.find("Modbus") # Verifying word exists
		


		if ics_name_location > 0: #If find returns a positive number (which means it found something) do the following
			print(index_count)
			index_count = int(index_count)
			valid_block_text.append(lines)
			#print(valid_block_text)

	valid_index = index_count
	for end_block in filetext[valid_index::]:
		valid_block_text.append(end_block)
		print(valid_block_text)
		continue



			
		#print(index_count)
		#print(lines)
		#print(list(enumerate(lines)))
		
		"""
		for back in reversed(lines):
			print(back)
			break
		"""
		
		"""
		iter_num = enumerate(lines)
		print("Iteration number is: ",list(iter_num))
		"""

				
			
			
		#print(valid_block_text)
			
			
			
		
	
"""
	file.close() 
	#print(filetext[123803])
	FileParser.test = "this is a test"
	ics_words = 'Modbus','BACnet/IP','DNP3','EtherCAT','Ethernet/IP','BigIP','FL-net','Foundation Fieldbus','ICCP','Modbus TCP','OPC UA Binary','OPC UA Discovery Server','OPC UA XML,PROFINET','ROC PLus'
	

	for x in ics_words:

		FileParser.ics_finder = filetext.find(x) # Gets location of text in list

		if x in filetext:
			print("________" * 5)
			print("[+]Query",x,"found at:",FileParser.ics_finder)
			print(" ")

		if x not in filetext:
			print("________" * 5)
			print("[+]Query",x,"not found")
			print(" ")

	

def TextGrabber():
	#print(FileParser.test)
	print(" ")
	textprompt = "Display the results found? [Y/N] > "
	print("_" * len(textprompt))
	userinput = input(textprompt)

	if userinput == "Y":
		print("Success")

	elif userinput == "N":
		print("Failure")

	else:
		print("Please select Y or N")
		TextGrabber()

	

"""
	





FileParser()
#TextGrabber()