# Scirpting_project
This code is a Python script that can be used to search for subdomains and directories of a given domain. It works by taking a domain name as input and then checking for subdomains and directories by trying to access various URLs formed using the subdomain and directory dictionaries provided.

Prerequisites
To use this script, you need to have Python 3 and the following Python libraries installed:
```sh
python subdomains_directories.py domain_name
```

re
argparse
requests
How to use
Clone this repository to your local machine.
Navigate to the cloned repository folder in your terminal.
Run the script by typing the following command:
python
Copy code
python subdomains_directories.py domain_name
Here, domain_name is the name of the domain you want to search for subdomains and directories of.

Input
The input to the script is the name of the domain you want to search for subdomains and directories of.

Output
The script will create the following output files in the ./outputs folder:

outputsubdomains.bat - This file contains a list of subdomains found for the given domain.
outputdirectories.bat - This file contains a list of directories found for the given domain.
files_output.bat - This file contains a list of links found on the homepage of the given domain.
Limitations
This script has a few limitations:

It can only find subdomains and directories that are listed in the dictionaries provided.
It does not perform any brute-force attacks to find subdomains and directories.
It may not work with all domains.
Disclaimer
This script is intended for educational purposes only. Use it at your own risk. The author is not responsible for any misuse or damage caused by this script.
