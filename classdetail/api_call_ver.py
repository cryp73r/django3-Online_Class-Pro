import json

def apiCallVer():
    raw_json = {"ver": "v2.2.5","size": "17.9MB" , "url": "https://mega.nz/file/bYlFEY5T#d3eaxfQ4_PCMTHmPu0qOC84xjgCYiuvrqnBFRhIMSlc"}
    with open('classdetail/templates/classdetail/json/classdetails/raw_data_ver.json', 'w') as outfile:
        json.dump(raw_json, outfile)