#https://api.weatherapi.com/v1/current.json?key=3d351852e3b34079991171859240605&q=jodhpur 
#API KEY :--> 3d351852e3b34079991171859240605 ;

#import python libraries to use them in code;
#Make sure the libraries you want to use are installed in your Python environment. 
# If not, you can install them using pip, Python's package installer. For example:
# used this command in terminal - pip install <library name>.
# Eg. --> pip install pandas


import requests # type: ignore
import json

x = input("Enter your city \n")
print("current weather of this", x ,"is --> ")

url = f"https://api.weatherapi.com/v1/current.json?key=3d351852e3b34079991171859240605&q={x}"

req=requests.get(url)
#print(req.text)
wdic = json.loads(req.text)
print(wdic["current"]["temp_c"])