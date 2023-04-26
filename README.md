# SeniorProject
This repository is the one section I worked on for Senior Design. The Senior Design team is building an Industrial Control Systems Information Gathering tool that stores all results into an ontology. When results are stored in the ontology you can then visualize and query the results! The plan is to make a web interface that allows users to input/query information and then have relevant ICS related information be returned to them. The data sources the project would pull from were MITRE, NVD, Exploit-DB, Crt.sh, and the newest addition Nmap XML Files.


We would gather all the relevant ICS-related information from these sources and store them in the ontology. I worked on the Shodan data source. This accepts user input about a domain/organization they would want to scan. It then gathers HTTPS domains associated with that organization using a Certificate Transparency site (Crt.sh) and using Shodan to assist us in finding the http Domains. We then run the scan, and parse through the results to find only ICS related information using a list of keywords. This information would then get sent to our script aggregator so we can convert it into our ontology. 


This specific version of the tool will unfortunately not be made into the final iteration of the project. This is due to Shodan now charging credits for every time I download and store all the HTTP sites. I'm currently working on a work around for this tool to make sure that it's completely free, and scalable! Although this is not in the final iteration of the project, I'm very proud of what I put together.

