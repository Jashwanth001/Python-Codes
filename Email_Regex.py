'''
Q1.Extract Email Addresses Using Regex: Write a Python script that uses regular
expressions to extract all email addresses from a given text.
Q2.Validate Date Format Using Regex: Implement a program that uses regular
expressions to verify if a given date string is in the format DD/MM/YYYY.
Q3.Extract URLs from a String: Develop a Python script to extract all URLs from a given
string, assuming URLs start with http:// or https:// and end with a space or
punctuation.
'''
import re
email = input("Email:")
mob = input("Mob No:")
date = input("Date:")
url = input("Url:")
if re.match( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email):
    print("Matched")
if re.match("^[6-9]{1}([0-9]{9})$",mob):
    print("Matched")
if re.match('^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/[0-1]([0-9]|[1-2])/(19|20)[0-9]{2}$',date):
    print("Matched")
if re.match('^([\w://][\w.=+%]$',url):
    print("Matched")
else:
    print("Not matched")

