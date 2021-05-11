import json

def apiCallVer():
    raw_json = {"ver": "v2.2.5","size": "17.9MB" , "url": "https://mega.nz/file/bYlFEY5T#d3eaxfQ4_PCMTHmPu0qOC84xjgCYiuvrqnBFRhIMSlc"}
    raw_json = json.dumps(raw_json)
    return raw_json