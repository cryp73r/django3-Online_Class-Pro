import json

def apiCallVer():
    raw_json = {"ver": "v2.2.5","size": "19.3MB" , "url": "https://mega.nz/file/6Jl0HBaA#RkvRsgWN3uuKg9ifsZKxGuXWlNl0Ip0gI_4K5wpztoc"}
    with open('classdetail/templates/classdetail/json/classdetails/raw_data_ver.json', 'w') as outfile:
        json.dump(raw_json, outfile)