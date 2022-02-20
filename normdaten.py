"""
Skript um eine Reihe von Informationen über Normdaten abzurufen. 
"""

import re
import requests

base = "http://www.wikidata.org/entity/"
id = "Q161930"

result = requests.get(base+id)
string = str(result.json())

qid = re.findall("\'item\', \'id\': \'(.*?)\'", string)[0]
label_de = re.findall("\'de\', \'value\': \'(.*?)\'", string)[0]
latitude = re.findall("latitude\': (.*?)\,", string)[0]
longitude = re.findall("longitude\': (.*?)\,", string)[0]

print("\nqid:", qid)
print("label_de:", label_de)
print("lat:", latitude)
print("long:", longitude)


