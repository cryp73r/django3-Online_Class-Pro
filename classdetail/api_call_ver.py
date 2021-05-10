import json

def apiCallVer():
    raw_json = {"ver": "v1.2.4", "url": ""}
    with open('classdetail/templates/classdetail/json/classdetails/raw_data_ver.json', 'w') as outfile:
        json.dump(raw_json, outfile)