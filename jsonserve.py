"""
This code loads a JSON-formatted string into a Python dictionary using the json.loads() function, 
and then prints out the "name" and "hide" values from the dictionary.
"""

import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print('Name :', info["name"])
print('Hide :', info["email"]["hide"])


input = '''
[
    {
        "id"  :   "001",
        "x"   :   "2",
        "name"    :   "Chuck"
    },
    {
        "id"  :   "009",
        "x"   :   "7",
        "name"    :   "Chuck"
    }
]
'''
info = json.loads(input)
print('User count   :',len(info))
for item in info:
    print('name', item["name"])
    print('id', item["id"])
    print('attribute', item["x"])