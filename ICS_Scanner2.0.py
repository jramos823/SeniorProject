#!/usr/bin/env python3

import re
import subprocess
import os
import time


def CrtScraping():
    userinput = input("Please enter the domain you would like to scan: ") #Accepts User Input
    print("[+]Scrapping all possible domains associated with Targets Security Certificate...")
    cmd_curl ='curl -s "https://crt.sh/?q='+userinput+'&output=json" | jq -r \'.[] | "\(.name_value)\\n\(.common_name)"\' | sort -u > "'+userinput+'_crt.sh.txt"'
    print("")
    print("[+]Executing commands!! ")
    subprocess.run(cmd_curl, shell = True)
    domainResults = userinput+'_crt.sh.txt'
    print("[+]File created! --> ", domainResults)
    cmd_host = 'for i in $(cat '+domainResults+');do host $i | grep "has address" | grep '+userinput+' | cut -d " " -f4 >> ip-addresses.txt;done'
    subprocess.run(cmd_host, shell = True)
    print("[+]Validating hosts...")


    

def ShodanExe():
    apikey = '' #Removed Key for Security purposes
    subprocess.run(["shodan", "init", apikey])

    input2 = input("Please enter organization name (e.g. Walmart, Spotify): ")
    cmd_shodan_http = 'shodan search org:'+input2+' port:80 http.status:200 > '+input2+'.http' # Shodan command for more http
    subprocess.run(cmd_shodan_http, shell = True) #Executing command
    print('[+]Searching for HTTP related domains. Creating http.'+input2+' file')
    http_file = open(''+input2+'.http') # Load file into variable
    http_text = http_file.read()
    ip_pattern = r"(?:^|\b(?<!\.))(?:1?\d?\d|2[0-4]\d|25[0-5])(?:\.(?:1?\d?\d|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])"
    ip_addresses = re.findall(ip_pattern, http_text)
    https_addresses = open('ip-addresses.txt', 'a')
    
    for ip in ip_addresses:  #Iterating through IP List
        https_addresses.write(ip+'\n') #Adding http IPs to the already made IP list
    https_addresses.close()
    
    print('[+]Shodan --> Scanning all hosts..')
    allIP = open('ip-addresses.txt', 'r')
    
     
    for ip in allIP:
        print("[+]Scanning: ", ip)
        shodan_host_cmd = 'shodan host '+ip+' >> results.txt'
        with open('results.txt', "a") as outfile:
            subprocess.run(shodan_host_cmd, shell = True, stdout=outfile)
        

def FileParser():
    file = open('results.txt') # Load file into variable
    filetext = file.read()
    testfile = re.split(r"(?:^|\b(?<!\.))(?:1?\d?\d|2[0-4]\d|25[0-5])(?:\.(?:1?\d?\d|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])", filetext)
    

    for index_count, lines in enumerate(testfile):
        ics_words = ["Modbus", "Siemens", "Rockwell", "Allen-Bradley", "Modicon", "Schneider Electric", "SIMATIC", "SIPLUS S7-1500", "S7-300", "S7-400", "S7", "DNP3", "BACnet", "EtherNet/IP", "GE-SRTP", "HART", "PCWorx", "MELSEC-Q", "FINS", "Red Lion", "CODESYS", "ProConOS", "SCADA", "PLC", "DCS", "HMI", "BECKHOFF", "Danfoss ECL Apex", "FATEK", "GE Fanus", "GE SRTP", "GE QuickPanels", "HITACHI EHV", "KEYENCE KV-5000", "Korenix 6550", "Koyo Ethernet", "LS GLOFA FEnet", "LS XGB FEnet", "Memobus", "Mitsubishi", "Omron", "Panasonic", "Schleicher ", "Unitronics" , "Trio", "Wago", "YASKAWA", "YAMAHA", "Camera", "camera", "IP Camera", "printer", "Printer", "502/tcp", "1089/tcp", "1090/tcp", "1091/tcp", "1541/tcp", "2222/tcp", "3480/tcp", "4000/tcp", "18000/tcp", "20000/tcp", "502/udp", "1089/udp", "1090/udp", "1091/udp", "1541/udp", "2222/udp", "3480/udp", "4000/udp", "18000/udp", "20000/udp"]
        for x in ics_words:    
            ics_name_location = lines.find(x)

            if ics_name_location > 0:
                print("_________________________________________________")
                print("[+]Keyword", x, "found!")
                print("[+]Printing Results.....")
                print(testfile[index_count])

                icsfile = open("final_ics_results.txt", "a")
                icsfile.write(testfile[index_count])
                print("[+]All results were stored in final_ics_results.txt!")


CrtScraping()
ShodanExe()
FileParser()
