import re
import argparse
import requests
from urllib.request import urlopen

subdomains_file = open("./subdomains_dictionary.bat", "r")
directories_file = open("./dirs_disctionary.bat", "r")

subdomains_output = open("./outputs/outputsubdomains.bat", "w")
directories_output = open("./outputs/outputdirectories", "w")
f_output = open("./Output/files_output.bat", "w")

parser = argparse.ArgumentParser()
parser.add_argument("domain", help="Domain name")
domain = getattr(parser.parse_args(), "domain")

if not re.match(r"^https?:\/\/", domain):
    secure_input = input("Is the protocol secure? (yes or no) ")
    if secure_input.lower() == "yes":
        domain = "https://" + domain
    elif secure_input.lower() == "no":
        domain = "http://" + domain

try:
    domain_response = requests.get(domain)
except:
    print("Please enter a valid domain name.")
    exit()


trailing_spaces_regex = r'^\s+|\s+$|[^a-zA-Z0-9\s]'

with subdomains_file as subdomains_list:
    subdomain = subdomains_list.readline()
    while subdomain:
        subdomain_no_spaces = re.sub(trailing_spaces_regex, "", subdomain)
        subdomain_protocol = re.match(r"https?:\/\/", subdomain_no_spaces)
        subdomain_without_www = re.sub(r"https?:\/\/www\.", "", subdomain_no_spaces)
        new_subdomain_url = subdomain_protocol + subdomain_no_spaces + "." + subdomain_without_www
        try:
            subdomain_response = requests.get(new_subdomain_url)
            subdomains_output.write(new_subdomain_url + "\n")
        except:
            pass

        subdomain = subdomains_list.readline()


with directories_file as dirs_list:
    directory = dirs_list.readline()
    while directory:
        directory_no_spaces = re.sub(trailing_spaces_regex, "", directory)
        directory_protocol = re.match(r"https?:\/\/", directory_no_spaces)
        directory_without_www = re.sub(r"https?:\/\/www\.", "", directory_no_spaces)
        new_directory_url = directory_protocol + directory_no_spaces + "." + directory_without_www
        try:
            directory_response = requests.get(new_directory_url)
            directories_output.write(new_directory_url + "\n")
        except:
            pass
        directory = dirs_list.readline()

try:
    html = urlopen(domain).read().decode()

    link = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
    matches = re.findall(link, html)
    for link in list(matches):
        f_output.write(link)
except:
    print("Error")

